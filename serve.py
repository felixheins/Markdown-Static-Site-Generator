#!/usr/bin/env python3
"""
Live development server for Obsidian Static Site Generator

This server watches for file changes in your vault and automatically rebuilds
the site, then serves it on a local web server for immediate preview.

Usage: python serve.py <vault_dir> [theme_name] [--port PORT] [--host HOST]
"""

import sys
import time
import threading
import http.server
import socketserver
import functools
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import webbrowser
import subprocess
import shutil

# Import the build functions from build_site.py
try:
    from build_site import build_notes, copy_assets, write_index, copy_theme, list_available_themes
except ImportError:
    print("Error: Could not import build_site.py functions")
    print("Make sure build_site.py is in the same directory as serve.py")
    sys.exit(1)


class BuildHandler(FileSystemEventHandler):
    """Handles file system events and triggers rebuilds"""
    
    def __init__(self, vault_path, output_path, theme_name, build_callback):
        self.vault_path = Path(vault_path).resolve()
        self.output_path = Path(output_path).resolve()
        self.theme_name = theme_name
        self.build_callback = build_callback
        self.last_build_time = 0
        self.build_delay = 1.0  # Minimum seconds between builds
        
    def should_rebuild(self, file_path):
        """Check if file change should trigger a rebuild"""
        file_path = Path(file_path)
        
        # Ignore hidden files and directories
        if any(part.startswith('.') for part in file_path.parts):
            return False
            
        # Only rebuild for markdown files in vault or theme files
        if file_path.suffix == '.md':
            # Check if the file is within the vault directory
            try:
                file_path.relative_to(self.vault_path)
                return True
            except ValueError:
                # File is not within vault directory
                return False
        if file_path.suffix == '.css' and 'Themes' in str(file_path):
            return True
        if file_path.name in ['build_site.py', 'serve.py']:
            return True
            
        return False
    
    def on_modified(self, event):
        if event.is_directory:
            return
            
        # Throttle rebuilds to avoid excessive builds
        current_time = time.time()
        if current_time - self.last_build_time < self.build_delay:
            return
            
        if self.should_rebuild(event.src_path):
            print(f"\n🔄 File changed: {Path(event.src_path).name}")
            self.last_build_time = current_time
            # Use a timer to debounce rapid file changes
            if hasattr(self, '_timer'):
                self._timer.cancel()
            self._timer = threading.Timer(0.5, self.build_callback)
            self._timer.start()
    
    def on_created(self, event):
        self.on_modified(event)
    
    def on_deleted(self, event):
        if not event.is_directory and self.should_rebuild(event.src_path):
            print(f"\n🗑️  File deleted: {Path(event.src_path).name}")
            if hasattr(self, '_timer'):
                self._timer.cancel()
            self._timer = threading.Timer(0.5, self.build_callback)
            self._timer.start()


class QuietHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler that doesn't log every request and serves from a specific directory"""
    
    def __init__(self, *args, directory=None, **kwargs):
        self.serve_directory = directory
        super().__init__(*args, **kwargs)
    
    def translate_path(self, path):
        """Translate a /-separated PATH to the local filename syntax, serving from our directory"""
        if self.serve_directory is None:
            return super().translate_path(path)
        
        import urllib.parse
        import posixpath
        
        # Parse the path
        path = path.split('?', 1)[0]
        path = path.split('#', 1)[0]
        path = urllib.parse.unquote(path)
        path = posixpath.normpath(path)
        
        # Remove leading slash and join with our directory
        words = path.split('/')
        words = filter(None, words)
        path = str(self.serve_directory)
        for word in words:
            path = Path(path) / word
        
        return str(path)
    
    def log_message(self, format, *args):
        # Only log errors, not every request
        if args[1] != '200':
            super().log_message(format, *args)


def build_site(vault_path, output_path, theme_name):
    """Build the static site"""
    try:
        vault = Path(vault_path).expanduser().resolve()
        output = Path(output_path).expanduser().resolve()
        script_dir = Path(__file__).parent
        
        if not vault.is_dir():
            print(f"❌ Vault not found: {vault}")
            print(f"   Vault path provided: {vault_path}")
            print(f"   Resolved vault path: {vault}")
            return False
        
        # Create output directory
        if output.exists():
            shutil.rmtree(output)
        output.mkdir(parents=True, exist_ok=True)
        
        # Copy theme
        if not copy_theme(script_dir, output, theme_name):
            print(f"❌ Failed to copy theme: {theme_name}")
            return False
        
        # Build site
        print(f"🔨 Building site...")
        pages, vault_index_file = build_notes(vault, output)
        copy_assets(vault, output)
        write_index(pages, vault_index_file, output)
        
        print(f"✅ Site built successfully")
        print(f"📁 Output: {output}")
        print(f"🎨 Theme: {theme_name}")
        return True
        
    except Exception as e:
        print(f"❌ Build failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def start_file_watcher(vault_path, output_path, theme_name, build_callback):
    """Start watching for file changes"""
    vault_path = Path(vault_path).resolve()
    
    event_handler = BuildHandler(vault_path, output_path, theme_name, build_callback)
    observer = Observer()
    
    # Watch the vault directory
    observer.schedule(event_handler, str(vault_path), recursive=True)
    
    # Watch the themes directory
    themes_dir = Path(__file__).parent / "Themes"
    if themes_dir.exists():
        observer.schedule(event_handler, str(themes_dir), recursive=True)
    
    # Watch the build script
    script_dir = Path(__file__).parent
    observer.schedule(event_handler, str(script_dir), recursive=False)
    
    observer.start()
    print(f"👀 Watching for changes in:")
    print(f"   📂 {vault_path}")
    print(f"   🎨 {themes_dir}")
    print(f"   🛠️  {script_dir}")
    
    return observer


def start_web_server(output_path, host='localhost', port=8000):
    """Start the web server"""
    output_path = Path(output_path).resolve()
    
    class CustomTCPServer(socketserver.TCPServer):
        allow_reuse_address = True
    
    # Create a partial function with the directory parameter
    handler = functools.partial(QuietHTTPRequestHandler, directory=output_path)
    
    try:
        with CustomTCPServer((host, port), handler) as httpd:
            server_url = f"http://{host}:{port}"
            print(f"🌐 Server running at {server_url}")
            print(f"📁 Serving: {output_path}")
            
            # Open browser automatically
            def open_browser():
                time.sleep(1)  # Give server time to start
                webbrowser.open(server_url)
            
            browser_thread = threading.Thread(target=open_browser, daemon=True)
            browser_thread.start()
            
            # Serve forever
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use. Try a different port:")
            print(f"   python serve.py <vault> [theme] --port {port + 1}")
        else:
            print(f"❌ Server error: {e}")


def parse_arguments():
    """Parse command line arguments"""
    args = sys.argv[1:]
    
    if len(args) < 1:
        return None, None, None, None, None
    
    vault_path = args[0]
    theme_name = "paper-theme"
    host = "localhost"
    port = 8000
    
    i = 1
    while i < len(args):
        arg = args[i]
        
        if arg == "--port" and i + 1 < len(args):
            try:
                port = int(args[i + 1])
                i += 2
            except ValueError:
                print(f"❌ Invalid port number: {args[i + 1]}")
                return None, None, None, None, None
        elif arg == "--host" and i + 1 < len(args):
            host = args[i + 1]
            i += 2
        elif not arg.startswith("--"):
            # This should be the theme name
            theme_name = arg
            i += 1
        else:
            print(f"❌ Unknown argument: {arg}")
            return None, None, None, None, None
    
    # Create output path
    vault_name = Path(vault_path).name.replace(' ', '_')
    script_dir = Path(__file__).parent
    output_path = script_dir / "Outputs" / f"{vault_name}_dev"
    
    return vault_path, str(output_path), theme_name, host, port


def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Obsidian Static Site Generator - Development Server")
        print()
        print("Usage: python serve.py <vault_dir> [theme_name] [options]")
        print()
        print("Arguments:")
        print("  vault_dir     Path to your Obsidian vault")
        print("  theme_name    Theme to use (optional, default: paper-theme)")
        print()
        print("Options:")
        print("  --port PORT   Port to serve on (default: 8000)")
        print("  --host HOST   Host to bind to (default: localhost)")
        print()
        print("Available themes:")
        script_dir = Path(__file__).parent
        themes = list_available_themes(script_dir)
        if themes:
            for theme in themes:
                print(f"  - {theme}")
        else:
            print("  No themes found in Themes directory")
        print()
        print("Examples:")
        print("  python serve.py ~/MyVault")
        print("  python serve.py ~/MyVault dark-theme")
        print("  python serve.py ~/MyVault paper-theme --port 3000")
        print("  python serve.py ~/MyVault --host 0.0.0.0 --port 8080")
        return
    
    vault_path, output_path, theme_name, host, port = parse_arguments()
    
    if not all([vault_path, output_path, theme_name, host, port]):
        return
    
    # Convert to absolute paths BEFORE changing directories
    vault_path = str(Path(vault_path).expanduser().resolve())
    output_path = str(Path(output_path).expanduser().resolve())
    
    # Validate vault exists
    if not Path(vault_path).exists():
        print(f"❌ Vault directory not found: {vault_path}")
        return
    
    # Validate theme exists
    script_dir = Path(__file__).parent
    themes = list_available_themes(script_dir)
    if theme_name not in themes:
        print(f"❌ Theme not found: {theme_name}")
        print("Available themes:")
        for theme in themes:
            print(f"  - {theme}")
        return
    
    print("🚀 Obsidian Static Site Generator - Development Server")
    print("=" * 60)
    
    # Initial build
    if not build_site(vault_path, output_path, theme_name):
        print("❌ Initial build failed. Exiting.")
        return
    
    # Set up rebuild callback with correct arguments
    # Store the original paths to avoid variable scope issues
    original_vault_path = vault_path
    original_output_path = output_path
    original_theme_name = theme_name
    
    def rebuild_callback():
        print("🔄 Rebuilding...")
        print(f"   📂 Vault: {original_vault_path}")
        print(f"   📁 Output: {original_output_path}")
        print(f"   🎨 Theme: {original_theme_name}")
        if build_site(original_vault_path, original_output_path, original_theme_name):
            print("✅ Rebuild complete")
        else:
            print("❌ Rebuild failed")
    
    # Start file watcher
    observer = start_file_watcher(vault_path, output_path, theme_name, rebuild_callback)
    
    print("\n" + "=" * 60)
    print("💡 Development server ready!")
    print(f"   📝 Edit files in: {Path(vault_path).resolve()}")
    print(f"   🎨 Change themes in: {script_dir}/Themes/")
    print(f"   🔄 Auto-rebuild on file save")
    print(f"   ⌨️  Press Ctrl+C to stop")
    print("=" * 60)
    
    try:
        # Start web server (this blocks)
        start_web_server(output_path, host, port)
    finally:
        # Clean up file watcher
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()
