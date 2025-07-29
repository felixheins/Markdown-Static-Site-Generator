# Implementation Details

Technical implementation details and code examples for the Obsidian Static Site Generator.

## Core Architecture

The generator consists of three main components:

### 1. Build System (`build_site.py`)

```python
def build_notes(vault: Path, out: Path):
    """Main build function that processes markdown files"""
    md = markdown.Markdown(
        extensions=["toc", "footnotes", "tables", "fenced_code", "codehilite", "meta"],
        extension_configs={"codehilite": {"guess_lang": False}},
        output_format="html5"
    )
    
    pages = {}  # Organize pages by directory
    vault_index_file = None
    
    # Process all markdown files
    for file in vault.rglob("*.md"):
        if "Resources" in file.parts or file.stem.startswith("_"):
            continue  # Skip resources and private files
            
        # Convert markdown to HTML
        raw = file.read_text(encoding="utf-8")
        html = md.convert(preprocess(raw))
        
        # Generate navigation structure
        # ... (navigation logic)
```

### 2. Development Server (`serve.py`)

```python
class BuildHandler(FileSystemEventHandler):
    """Watches for file changes and triggers rebuilds"""
    
    def on_modified(self, event):
        if self.should_rebuild(event.src_path):
            print(f"🔄 File changed: {Path(event.src_path).name}")
            # Debounce rapid changes
            if hasattr(self, '_timer'):
                self._timer.cancel()
            self._timer = threading.Timer(0.5, self.build_callback)
            self._timer.start()

def start_web_server(output_path, host='localhost', port=8000):
    """Start HTTP server with custom directory handling"""
    handler = functools.partial(QuietHTTPRequestHandler, directory=output_path)
    with CustomTCPServer((host, port), handler) as httpd:
        httpd.serve_forever()
```

### 3. Theme System

```python
def copy_theme(script_dir: Path, output_dir: Path, theme_name: str):
    """Copy theme CSS to output directory"""
    theme_file = script_dir / "Themes" / f"{theme_name}.css"
    if theme_file.exists():
        shutil.copy2(theme_file, output_dir / "style.css")
        return True
    return False
```

## Key Processing Functions

### Wiki Link Conversion

```python
def preprocess(text: str) -> str:
    """Convert Obsidian-style [[links]] to markdown links"""
    def replace_wiki_link(match):
        link_text = match.group(1)
        # Handle [[Link|Display Text]] format
        if '|' in link_text:
            target, display = link_text.split('|', 1)
        else:
            target = display = link_text
        
        # Convert to web-friendly slug
        slug = slugify(target) + '.html'
        return f'[{display}]({slug})'
    
    # Replace [[Link]] patterns
    return re.sub(r'\[\[([^\]]+)\]\]', replace_wiki_link, text)
```

### Navigation Generation

```python
def generate_navigation(pages, vault_index_file=None):
    """Generate hierarchical navigation HTML"""
    menu_items = []
    
    # Add home link
    if vault_index_file:
        home_title = vault_index_file[0]
        menu_items.append(f"<li><a href='index.html' class='nav-link'>{home_title}</a></li>")
    
    # Process directories in order (root first)
    sorted_dirs = sorted(pages.keys(), key=lambda x: (str(x) != ".", str(x)))
    
    for directory in sorted_dirs:
        if directory == Path("."):
            # Root level pages
            for title, slug, is_index, parent_dir in sorted(pages[directory]):
                if slug != "index.html":  # Skip main index
                    menu_items.append(f"<li><a href='{slug}' class='nav-link'>{title}</a></li>")
        else:
            # Create dropdown for subdirectory
            # ... (dropdown logic)
    
    return f"<ul>{''.join(menu_items)}</ul>"
```

## File Watching Implementation

```python
def start_file_watcher(vault_path, output_path, theme_name, build_callback):
    """Set up file system watching for live reload"""
    event_handler = BuildHandler(vault_path, output_path, theme_name, build_callback)
    observer = Observer()
    
    # Watch multiple directories
    observer.schedule(event_handler, str(vault_path), recursive=True)
    
    themes_dir = Path(__file__).parent / "Themes"
    if themes_dir.exists():
        observer.schedule(event_handler, str(themes_dir), recursive=True)
    
    observer.start()
    return observer
```

## Theme Architecture

### CSS Variable System

```css
:root {
    /* Core color palette */
    --paper: #fefcf6;    /* Background */
    --ink: #4a4a4a;      /* Text */
    --accent: #d73502;   /* Links/highlights */
    --faint: #e8e3d3;    /* Borders */
    --highlight: #f4f1e8; /* Code blocks */
    
    /* Typography */
    --font-family: 'Charter', 'Iowan Old Style', serif;
    --font-size: 17px;
    --line-height: 1.5;
    
    /* Layout */
    --content-width: 750px;
    --padding: 25px;
}
```

### Responsive Navigation

```css
.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: var(--paper);
    box-shadow: 0px 8px 16px rgba(0,0,0,0.15);
    z-index: 1001;
}

.dropdown:hover .dropdown-content {
    display: block;
}

/* Mobile responsive */
@media (max-width: 768px) {
    .dropdown-content {
        position: static;
        display: block;
        box-shadow: none;
    }
}
```

## Build Process Flow

1. **File Discovery** - Recursively find all `.md` files
2. **Filtering** - Skip Resources/ and `_` prefixed files for navigation
3. **Processing** - Convert markdown to HTML with wiki link resolution
4. **Navigation** - Generate hierarchical menu structure
5. **Template** - Apply HTML template with navigation and theme
6. **Output** - Write HTML files and copy assets
7. **Theme** - Copy selected CSS theme as `style.css`

## Extension Points

### Custom Themes
Create `Themes/my-theme.css` with CSS variables:
```css
:root {
    --paper: #1a1a1a;
    --ink: #e6e6e6;
    --accent: #4a9eff;
}
```

### Custom Processing
Extend `preprocess()` function for additional markdown transformations:
```python
def preprocess(text: str) -> str:
    text = convert_wiki_links(text)
    text = process_custom_syntax(text)  # Your extensions
    return text
```

### Build Hooks
Add custom build steps by modifying the main build function:
```python
def build_notes(vault: Path, out: Path):
    # Standard processing
    pages, vault_index_file = process_markdown_files(vault, out)
    
    # Custom post-processing
    generate_sitemap(pages, out)
    optimize_images(out)
    
    return pages, vault_index_file
```

This implementation provides a solid foundation while remaining simple and extensible.

### Python

```python
#!/usr/bin/env python3
"""
Example Python code with various features
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Optional

class DocumentProcessor:
    """Process Obsidian documents for web publishing"""
    
    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.highlight_pattern = re.compile(r'==(.+?)==')
    
    def process_highlights(self, text: str) -> str:
        """Convert ==highlight== syntax to HTML marks"""
        return self.highlight_pattern.sub(r'<mark>\1</mark>', text)
    
    def slugify(self, text: str, allow_unicode: bool = False) -> str:
        """Convert text to URL-friendly slug"""
        if allow_unicode:
            import unicodedata
            text = unicodedata.normalize("NFKC", text)
        else:
            text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
        
        text = re.sub(r"[^\w\s-]", "", text.lower())
        return re.sub(r"[-\s]+", "-", text).strip("-_")
```

### JavaScript

```javascript
// JavaScript example with modern features
class SiteNavigator {
    constructor(menuData) {
        this.menuData = menuData;
        this.currentPage = window.location.pathname;
    }
    
    generateDropdown(items) {
        return items.map(item => `
            <li><a href="${item.url}">${item.title}</a></li>
        `).join('');
    }
    
    async loadPage(url) {
        try {
            const response = await fetch(url);
            const html = await response.text();
            return html;
        } catch (error) {
            console.error('Failed to load page:', error);
            return null;
        }
    }
    
    // Arrow function example
    highlightCurrentPage = () => {
        const links = document.querySelectorAll('nav a');
        links.forEach(link => {
            if (link.getAttribute('href') === this.currentPage) {
                link.classList.add('active');
            }
        });
    }
}
```

### CSS

```css
/* Advanced CSS for the navigation system */
.dropdown {
    position: relative;
    display: inline-block;
    transition: all 0.3s ease;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: var(--paper);
    min-width: 200px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    border: 1px solid var(--faint);
    border-radius: 4px;
    z-index: 1000;
    top: 100%;
    left: 0;
}

.dropdown:hover .dropdown-content {
    display: block;
    animation: slideDown 0.2s ease-out;
}

@keyframes slideDown {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.dropdown-content a {
    color: var(--ink);
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    border-bottom: 1px solid var(--faint);
}

.dropdown-content a:last-child {
    border-bottom: none;
}

.dropdown-content a:hover {
    background-color: var(--highlight);
}
```

### Shell/Bash

```bash
#!/bin/bash
# Build script for the Obsidian site converter

set -e  # Exit on any error

VAULT_DIR="$1"
OUTPUT_DIR="$2"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -z "$VAULT_DIR" ] || [ -z "$OUTPUT_DIR" ]; then
    echo "Usage: $0 <vault_directory> <output_directory>"
    exit 1
fi

echo "🔄 Building static site..."
echo "📁 Vault: $VAULT_DIR"
echo "📤 Output: $OUTPUT_DIR"

# Activate virtual environment if it exists
if [ -d "$SCRIPT_DIR/.venv" ]; then
    echo "🐍 Activating virtual environment..."
    source "$SCRIPT_DIR/.venv/bin/activate"
fi

# Run the conversion
python "$SCRIPT_DIR/build_site.py" "$VAULT_DIR" "$OUTPUT_DIR"

echo "✅ Site built successfully!"
echo "🌐 Open $OUTPUT_DIR/index.html in your browser"

# Optional: Start local server
if command -v python &> /dev/null; then
    echo "🚀 Starting local server on http://localhost:8000"
    cd "$OUTPUT_DIR"
    python -m http.server 8000
fi
```

## Inline Code Examples

The converter handles inline code like `variable_name`, `function()`, and `--command-line-flags`.

Here are some examples in context:

- Use `python build_site.py` to run the converter
- The `slugify()` function converts titles to URLs
- Set the `--highlight` CSS variable for custom colors
- The `re.compile()` method creates regex patterns

## Code with Highlighting

You can even combine code with ==highlighting==:

The ==`build_notes()`== function is the core of the conversion process. It uses ==`markdown.Markdown()`== to process each file.

## Algorithm Description

Here's how the conversion process works:

```
1. Scan vault directory for .md files
   ├── Skip Resources/ folder for navigation
   ├── Group files by directory
   └── Identify index files (same name as directory)

2. Process each markdown file
   ├── Read file content
   ├── Apply preprocessing (wiki links, highlights)
   ├── Convert markdown to HTML
   └── Wrap in HTML template

3. Generate navigation structure
   ├── Create dropdown menus for subdirectories
   ├── Link index files as main dropdown items
   └── Generate CSS for dropdown behavior

4. Copy assets and create output
   ├── Copy all non-.md files (including Resources/)
   ├── Write HTML files
   └── Create index.html with navigation
```

## Configuration Examples

The converter can be customized through various configuration options:

```python
# Markdown extensions configuration
extensions = [
    "toc",           # Table of contents
    "footnotes",     # Footnote support
    "tables",        # Enhanced tables
    "fenced_code",   # Code block fencing
    "codehilite",    # Syntax highlighting
    "meta"           # YAML frontmatter
]

extension_configs = {
    "codehilite": {
        "guess_lang": False,    # Don't guess language
        "use_pygments": True,   # Use Pygments highlighter
        "css_class": "highlight" # CSS class for code blocks
    }
}
```

## Cross-References

For more examples, see:
- [[Examples]] - The main examples index
- [[Basic Example]] - Simpler markdown features
- [[Complex Example]] - Advanced formatting combinations

---

This code example demonstrates comprehensive syntax highlighting and code-focused content processing.
