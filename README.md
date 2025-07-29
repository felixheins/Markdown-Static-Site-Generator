# Markdown Static Site Generator

A lightweight, theme-driven static site generator that converts your Obsidian-styled Markdown files into a beautiful website with live development server support.

![Demo Site](https://img.shields.io/badge/demo-live-brightgreen)
![Python](https://img.shields.io/badge/python-3.7+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- **📁 Smart Navigation** - Automatic dropdown menus from your file structure
- **🎨 Beautiful Themes** - Paper and dark themes with Garamond typography
- **🔄 Live Development** - Auto-rebuilding server with file watching
- **🔗 Wiki Links** - Preserves Obsidian-style `[[links]]`
- **📱 Responsive Design** - Mobile-friendly layouts
- **📋 Privacy Control** - Files starting with `_` excluded from navigation
- **🚀 Zero Configuration** - Works out of the box

## Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/felixheins/Markdown-Static-Site-Generator.git
cd Markdown-Static-Site-Generator

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Generate the Demo Site

```bash
# Build the included demo site
python build_site.py "Demo Site"

# Or start development server with live reload
python serve.py "Demo Site"
```

Visit `http://localhost:8000` to see the demo site with full documentation.

### 3. Build Your Own Site

```bash
# Build your Obsidian vault
python build_site.py "/path/to/your/vault"

# Development server with live reload
python serve.py "/path/to/your/vault"

# Use different theme
python build_site.py "/path/to/your/vault" --theme dark-theme
```

## Available Themes

- **paper-theme** (default) - Warm, elegant design with Garamond typography
- **dark-theme** - Modern dark mode with beautiful contrast

## Demo Site Structure

The included `Demo Site/` shows the generator's capabilities:

```
Demo Site/
├── Demo Site.md           # Homepage
├── Documentation/         # Full documentation
│   ├── Getting Started.md # Installation & usage
│   └── Features.md        # Complete feature list
└── Examples/              # Usage examples
    ├── Quick Start.md     # Step-by-step tutorial
    ├── Advanced Usage.md  # Complex scenarios
    └── Implementation Details.md  # Technical details
```

## Usage

### Build Commands

```bash
# Basic build
python build_site.py /path/to/vault

# Custom output directory
python build_site.py /path/to/vault --output /custom/output

# Specific theme
python build_site.py /path/to/vault --theme dark-theme
```

### Development Server

```bash
# Basic server
python serve.py /path/to/vault

# Custom port
python serve.py /path/to/vault --port 3000

# Network accessible
python serve.py /path/to/vault --host 0.0.0.0
```

## File Organization

- Files starting with `_` are excluded from navigation (but still built)
- `Resources/` folders are copied but not processed as pages
- Directory structure becomes navigation hierarchy
- Index files (same name as directory) become dropdown main pages

## Deployment

The generator creates static HTML/CSS that works with any hosting:

- **GitHub Pages** - Copy `Outputs/` to `docs/` folder
- **Netlify** - Drag and drop the output folder
- **Vercel** - Connect your repository
- **Traditional hosting** - Upload via FTP

## Contributing

Contributions welcome! Please read the documentation in the Demo Site for implementation details.

## License

MIT License - see LICENSE file for details.

---

*Generate beautiful static sites from your Markdown files with zero configuration.*
