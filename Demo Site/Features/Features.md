# Features Overview

Quick reference of all Markdown Static Site Generator capabilities.

## Feature Comparison

| Feature Category | What It Does | Status | Learn More |
|------------------|--------------|--------|------------|
| **Markdown Processing** | Full markdown support with extensions | ✅ Complete | [[Markdown]] |
| **Wiki Links** | `[[Page Name]]` Obsidian-style linking | ✅ Complete | [[Markdown]] |
| **Theme System** | CSS-based themes with variables | ✅ Complete | [[Site builder]] |
| **Live Development** | Auto-rebuild development server | ✅ Complete | [[Site builder]] |
| **Navigation** | Automatic menu from folder structure | ✅ Complete | [[Site builder]] |
| **Static Output** | Self-contained HTML/CSS websites | ✅ Complete | [[Site builder]] |

## Builder vs Markdown Features

### Builder Features
These are capabilities of the site generation system:

| Feature | Description |
|---------|-------------|
| **File Watching** | Monitors changes and rebuilds automatically |
| **Theme Selection** | Choose from built-in themes or create custom |
| **Asset Copying** | Includes images and files in output |
| **Clean URLs** | Converts filenames to web-friendly slugs |
| **Privacy Control** | Files starting with `_` hidden from navigation |
| **Deployment Ready** | Output works on any static hosting |

### Markdown Features  
These are content formatting options:

| Element | Syntax | Output |
|---------|--------|--------|
| **Headers** | `# Header` | HTML headings h1-h6 |
| **Emphasis** | `*italic*` `**bold**` | Styled text formatting |
| **Links** | `[text](url)` `[[WikiLink]]` | Clickable links |
| **Lists** | `- item` `1. item` `- [ ] task` | Formatted lists |
| **Code** | `` `code` `` `'''block'''` | Syntax highlighted code |
| **Tables** | `| col | col |` | HTML tables with styling |
| **Images** | `![alt](src)` | Embedded images |
| **Quotes** | `> quote` | Styled blockquotes |

## Quick Start

1. **Install**: Clone repository and install dependencies
2. **Build**: `python build_site.py "your-vault"`  
3. **Develop**: `python serve.py "your-vault"`
4. **Deploy**: Copy output folder to web hosting

## Detailed Documentation

- **[[Markdown]]** - Complete markdown syntax reference with examples
- **[[Site builder]]** - In-depth build system and theme documentation  

This generator supports everything you need to convert Obsidian vaults or markdown folders into professional static websites.