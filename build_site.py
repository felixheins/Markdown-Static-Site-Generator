#!/usr/bin/env python3
"""
Convert an Obsidian vault to a single-folder static site.

Usage
-----
    python build_site.py <vault_dir> <output_dir>

Requires
--------
    pip install markdown pygments
"""

import sys, re, shutil, unicodedata, datetime
from pathlib import Path
import markdown

HIGHLIGHT_RE = re.compile(r'==(.+?)==')

def slugify(text:str, allow_unicode=False)->str:
    if allow_unicode:
        text = unicodedata.normalize("NFKC", text)
    else:
        text = unicodedata.normalize("NFKD", text).encode("ascii","ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s]+", "-", text).strip("-_")

# ── pre-processor ──────────────────────────────────────────────────────────────
def preprocess(md:str) -> str:
    # ==highlight== → <mark>
    md = HIGHLIGHT_RE.sub(lambda m:f"<mark>{m.group(1)}</mark>", md)

    # ![[Embed]] first
    def embed(m):
        inner=m.group(1).strip(); tgt, *alias=inner.split("|",1)
        disp=alias[0] if alias else tgt; return f"![{disp}]({slugify(tgt)}.html)"
    md = re.sub(r"!\[\[([^\]]+)\]\]", embed, md)

    # [[WikiLink]]
    def link(m):
        inner=m.group(1).strip(); tgt,*alias=inner.split("|",1)
        disp=alias[0] if alias else tgt; return f"[{disp}]({slugify(tgt)}.html)"
    md = re.sub(r"\[\[([^\]]+)\]\]", link, md)
    return md

# ── navigation generation ─────────────────────────────────────────────────────
def generate_navigation(pages, vault_index_file=None, current_depth=0):
    """Generate navigation HTML for all pages"""
    # Determine path prefix based on depth (0 = root, 1 = subdirectory)
    path_prefix = "../" if current_depth > 0 else ""
    
    # Add Home link first - use vault index file title if available
    # This will be left-aligned while other items are right-aligned
    if vault_index_file:
        home_title = vault_index_file[0]  # Use the title of the vault index file
        home_link = f"<li class='home-link'><a href='{path_prefix}index.html' class='nav-link'>{home_title}</a></li>"
    else:
        home_link = f"<li class='home-link'><a href='{path_prefix}index.html' class='nav-link'>Home</a></li>"
    
    # Collect other menu items (will be right-aligned)
    other_items = []
    
    # Sort directories to put root directory first
    sorted_dirs = sorted(pages.keys(), key=lambda x: (str(x) != ".", str(x)))
    
    for directory in sorted_dirs:
        dir_pages = pages[directory]
        
        if directory == Path("."):  # Root directory
            # Add root pages directly to menu (but skip the vault index file since it's already Home)
            for title, slug, is_index, parent_dir in sorted(dir_pages, key=lambda x: (not x[2], x[0])):  # Index files first
                if slug != "index.html":  # Skip the vault index file
                    # Convert slug to clean URL (remove .html)
                    clean_url = path_prefix + slug.replace('.html', '/')
                    other_items.append(f"<li><a href='{clean_url}' class='nav-link'>{title}</a></li>")
        else:
            # Create dropdown for subdirectory
            dir_name = directory.name
            
            # Find index file for this directory
            index_file = None
            other_files = []
            
            for title, slug, is_index, parent_dir in dir_pages:
                if is_index:
                    # Convert to clean URL
                    clean_slug = path_prefix + slug.replace('.html', '/')
                    index_file = (title, clean_slug)
                else:
                    # Convert to clean URL
                    clean_slug = path_prefix + slug.replace('.html', '/')
                    other_files.append((title, clean_slug))
            
            # Create dropdown menu item
            if index_file:
                # Directory has an index file
                dropdown_content = f"<a href='{index_file[1]}' class='dropdown-main'>{dir_name}</a>"
            else:
                # No index file, just directory name
                dropdown_content = f"<span class='dropdown-main'>{dir_name}</span>"
            
            # Always add dropdown with files (including index file if it exists)
            all_files = []
            if index_file:
                all_files.append(index_file)
            all_files.extend(sorted(other_files))
            
            if all_files:
                file_links = "\n".join(f"<li><a href='{slug}'>{title}</a></li>" 
                                     for title, slug in all_files)
                dropdown_content += f"""
<ul class='dropdown-content'>
{file_links}
</ul>"""
            
            other_items.append(f"<li class='dropdown'>{dropdown_content}</li>")
    
    # Combine home link (left) with other items (right) in a flex container
    other_items_html = ''.join(other_items)
    return f"""<div class='nav-container'>
{home_link}
<ul class='nav-right'>
{other_items_html}
</ul>
</div>"""

# ── main build steps ───────────────────────────────────────────────────────────
def build_notes(vault:Path, out:Path):
    md = markdown.Markdown(
        extensions=["toc","footnotes","tables","fenced_code","codehilite","meta"],
        extension_configs={"codehilite":{"guess_lang":False}},
        output_format="html5",
    )
    pages = {}  # Store pages organized by directory (for navigation only)
    all_pages = []  # Store all pages for navigation (non-underscore only)
    all_files_to_process = []  # Store ALL files to process (including underscore files)
    vault_index_file = None  # Track if there's a vault-level index file
    
    # First pass: collect all pages
    for file in vault.rglob("*.md"):
        # Skip files in Resources directory for site generation
        if "Resources" in file.parts:
            continue
            
        raw=file.read_text(encoding="utf-8")
        html=md.convert(preprocess(raw))
        title = md.Meta.get("title",[file.stem])[0] if hasattr(md,"Meta") else file.stem
        
        # Determine relative path from vault root
        rel_path = file.relative_to(vault)
        parent_dir = rel_path.parent
        
        # Special case: if file name matches the vault directory name, treat it as root index
        vault_name = vault.name
        if file.stem.lower() == vault_name.lower():
            parent_dir = Path(".")  # Force it to be root level
            is_index = True
            slug = "index.html"  # This becomes the main index.html
            vault_index_file = (title, slug, file)
        else:
            slug = slugify(file.stem)+".html"
            # Check if this is a directory index file (same name as directory)
            is_index = file.stem.lower() == parent_dir.name.lower() if parent_dir.name else False
        
        page_info = (title, slug, is_index, parent_dir, file)
        all_files_to_process.append(page_info)
        
        # Only add to navigation if file doesn't start with underscore
        if not file.stem.startswith("_"):
            # Create directory structure in pages dict
            if parent_dir not in pages:
                pages[parent_dir] = []
            
            nav_page_info = (title, slug, is_index, parent_dir)
            pages[parent_dir].append(nav_page_info)
            all_pages.append(nav_page_info)
        
        md.reset()
    
    # Generate navigation HTML
    nav_html = generate_navigation(pages, vault_index_file, 0)
    
    # Second pass: write HTML files with navigation (process ALL files including underscore files)
    for title, slug, is_index, parent_dir, file_path in all_files_to_process:
        raw = file_path.read_text(encoding="utf-8")
        html = md.convert(preprocess(raw))
        
        # Create directory structure for clean URLs
        if slug == "index.html":
            # Main index stays at root
            output_path = out / "index.html"
            css_path = "style.css"
            current_nav_html = generate_navigation(pages, vault_index_file, 0)
        else:
            # Create directory for each page with index.html inside
            page_name = slug.replace('.html', '')
            page_dir = out / page_name
            page_dir.mkdir(exist_ok=True)
            output_path = page_dir / "index.html"
            css_path = "../style.css"
            current_nav_html = generate_navigation(pages, vault_index_file, 1)
        
        tpl=f"""<!doctype html><html lang='en'><head>
<meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>{title}</title><link rel='stylesheet' href='{css_path}'>
<style>
.top-nav {{ position: fixed; top: 0; left: 0; right: 0; background: var(--paper); padding: 15px 25px; z-index: 1000; border-bottom: 1px solid var(--faint); }}
.nav-container {{ display: flex; justify-content: space-between; align-items: center; }}
.home-link {{ flex-shrink: 0; }}
.nav-right {{ display: flex; list-style: none; margin: 0; padding: 0; }}
.nav-right > li {{ margin-left: 25px; }}
.dropdown {{ position: relative; display: inline-block; }}
.dropdown-content {{ display: none; position: absolute; right: 0; background-color: var(--paper); min-width: 200px; box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.15); z-index: 1001; border: 1px solid var(--faint); border-radius: 4px; }}
.dropdown-content li {{ list-style: none; }}
.dropdown-content a {{ color: var(--ink); padding: 10px 15px; text-decoration: none; display: block; font-size: 14px; border-bottom: 1px solid #f0f0f0; }}
.dropdown-content a:last-child {{ border-bottom: none; }}
.dropdown-content a:hover {{ background-color: var(--highlight); }}
.dropdown:hover .dropdown-content {{ display: block; }}
.dropdown-main {{ display: inline-block; padding: 8px 0; cursor: pointer; color: var(--ink); text-decoration: none; }}
.dropdown-main:hover {{ color: var(--accent); }}
.nav-link {{ display: inline-block; padding: 8px 0; text-decoration: none; color: var(--ink); }}
.nav-link:hover {{ color: var(--accent); }}
.home-link {{ list-style: none; }}
body {{ padding-top: 70px; }}
</style>
</head><body>
<nav class="top-nav">{current_nav_html}</nav>
<article>
{html}
</article></body></html>"""
        output_path.write_text(tpl,encoding="utf-8")
        md.reset()
    
    return pages, vault_index_file

def copy_assets(vault:Path, out:Path):
    for f in vault.rglob("*"):
        if f.is_dir() or f.suffix.lower() in {".md",".canvas"}: continue
        dest=out/f.relative_to(vault); dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(f,dest)

def write_index(pages, vault_index_file, out:Path):
    # Only create a dummy index if there's no vault-level index file
    if vault_index_file is None:
        nav_html = generate_navigation(pages, vault_index_file)
        
        # Create a simple index page with navigation
        html=f"""<!doctype html><html lang='en'><head>
<meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>Site Index</title><link rel='stylesheet' href='style.css'>
<style>
.top-nav {{ position: fixed; top: 0; left: 0; right: 0; background: var(--paper); padding: 15px 25px; z-index: 1000; border-bottom: 1px solid var(--faint); }}
.nav-container {{ display: flex; justify-content: space-between; align-items: center; }}
.home-link {{ flex-shrink: 0; }}
.nav-right {{ display: flex; list-style: none; margin: 0; padding: 0; }}
.nav-right > li {{ margin-left: 25px; }}
.dropdown {{ position: relative; display: inline-block; }}
.dropdown-content {{ display: none; position: absolute; right: 0; background-color: var(--paper); min-width: 200px; box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.15); z-index: 1001; border: 1px solid var(--faint); border-radius: 4px; }}
.dropdown-content li {{ list-style: none; }}
.dropdown-content a {{ color: var(--ink); padding: 10px 15px; text-decoration: none; display: block; font-size: 14px; border-bottom: 1px solid #f0f0f0; }}
.dropdown-content a:last-child {{ border-bottom: none; }}
.dropdown-content a:hover {{ background-color: var(--highlight); }}
.dropdown:hover .dropdown-content {{ display: block; }}
.dropdown-main {{ display: inline-block; padding: 8px 0; cursor: pointer; color: var(--ink); text-decoration: none; }}
.dropdown-main:hover {{ color: var(--accent); }}
.nav-link {{ display: inline-block; padding: 8px 0; text-decoration: none; color: var(--ink); }}
.nav-link:hover {{ color: var(--accent); }}
.home-link {{ list-style: none; }}
body {{ padding-top: 70px; }}
</style>
</head><body>
<nav class="top-nav">{nav_html}</nav>
<article>
<h1>Site Index</h1>
<p>Welcome to the site. Use the navigation menu above to browse all pages.</p>
<p class='generated'>Generated {datetime.date.today()}</p>
</article>
</body></html>"""
        (out/"index.html").write_text(html,encoding="utf-8")

def copy_theme(script_dir: Path, out: Path, theme_name: str = "paper-theme"):
    """Copy theme CSS file to output directory"""
    themes_dir = script_dir / "Themes"
    theme_file = themes_dir / f"{theme_name}.css"
    
    # Check if specified theme exists, fallback to paper-theme
    if not theme_file.exists():
        theme_file = themes_dir / "paper-theme.css"
        if not theme_file.exists():
            print(f"Warning: Theme '{theme_name}' not found, and default paper-theme.css is missing")
            return False
    
    # Copy theme as style.css in output
    shutil.copy2(theme_file, out / "style.css")
    return True

def list_available_themes(script_dir: Path):
    """List all available themes in the Themes directory"""
    themes_dir = script_dir / "Themes"
    if not themes_dir.exists():
        return []
    
    themes = []
    for css_file in themes_dir.glob("*.css"):
        theme_name = css_file.stem
        themes.append(theme_name)
    
    return sorted(themes)

def main():
    if len(sys.argv) < 2:
        print("Usage: python build_site.py <vault_dir> [output_dir] [theme_name]")
        print("Available themes:")
        script_dir = Path(__file__).parent
        themes = list_available_themes(script_dir)
        if themes:
            for theme in themes:
                print(f"  - {theme}")
        else:
            print("  No themes found in Themes directory")
        sys.exit(1)
    
    # Parse arguments
    vault_path = sys.argv[1]
    script_dir = Path(__file__).parent
    
    # Default output to Outputs directory if not specified
    if len(sys.argv) >= 3 and not sys.argv[2].startswith('--'):
        output_path = sys.argv[2]
        theme_name = sys.argv[3] if len(sys.argv) > 3 else "paper-theme"
    else:
        # Create default output path in Outputs directory
        vault_name = Path(vault_path).name.replace(' ', '_')
        output_path = str(script_dir / "Outputs" / vault_name)
        theme_name = sys.argv[2] if len(sys.argv) > 2 else "paper-theme"
    
    vault, out = map(lambda p: Path(p).expanduser().resolve(), [vault_path, output_path])
    script_dir = Path(__file__).parent
    
    if not vault.is_dir(): 
        print("Vault not found")
        sys.exit(1)
    
    # Create output directory
    if out.exists(): 
        shutil.rmtree(out)
    out.mkdir(parents=True)
    
    # Copy theme
    if not copy_theme(script_dir, out, theme_name):
        sys.exit(1)
    
    # Build site
    pages, vault_index_file = build_notes(vault, out)
    copy_assets(vault, out)
    write_index(pages, vault_index_file, out)
    
    print(f"✓ Site exported to {out}")
    print(f"✓ Using theme: {theme_name}")

if __name__=="__main__":
    main()
