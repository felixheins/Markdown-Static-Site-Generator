# Markdown Static Site Generator

A lightweight, theme-driven static site generator that converts your Obsidian-styled Markdown files into a beautiful website with live development server support.

## Overview

Transform your Obsidian markdown files into a fully-featured static website with:
- **Wiki-style navigation** - Automatic menu generation from your file structure
- **Beautiful themes** - Paper and dark themes with responsive design
- **Live development** - Auto-rebuilding development server with file watching
- **Zero configuration** - Works out of the box with sensible defaults

## Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/obsidian-static-site-generator
cd obsidian-static-site-generator

# Set up virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install watchdog
```

### Basic Usage

```bash
# Build your vault to static HTML
python build_site.py /path/to/your/vault

# Start development server with live reload
python serve.py /path/to/your/vault

# Use specific theme
python build_site.py /path/to/your/vault --theme dark-theme
```

Your site will be generated in the `Outputs/` directory, ready to deploy to any static hosting service.

## Key Features

- **📁 Smart Navigation** - Automatic dropdown menus for subdirectories
- **🎨 Theme System** - Easy-to-customize CSS themes with variables
- **🔄 Live Development** - File watching with instant rebuilds
- **📱 Responsive Design** - Mobile-friendly layouts
- **🔗 Wiki Links** - Preserves Obsidian-style `[[links]]`
- **📝 Markdown Support** - Full CommonMark with extensions
- **🚀 Fast Builds** - Efficient processing of large vaults
- **📋 Privacy Control** - Files starting with `_` excluded from navigation

---

*Open source project - contributions welcome!*
