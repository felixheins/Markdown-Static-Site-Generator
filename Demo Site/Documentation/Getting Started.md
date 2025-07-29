# Getting Started

Get up and running with the Obsidian Static Site Generator in minutes.

## Prerequisites

- Python 3.7+
- An Obsidian vault with markdown files

## Quick Setup

### 1. Download & Install

```bash
# Clone the repository
git clone https://github.com/yourusername/obsidian-static-site-generator
cd obsidian-static-site-generator

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install watchdog
```

### 2. Build Your First Site

```bash
# Build your vault
python build_site.py "/path/to/your/vault"

# Or start development server
python serve.py "/path/to/your/vault"
```

Your site will be available at `http://localhost:8000` with live reload enabled.

## Development Workflow

1. **Edit Content** - Modify markdown files in your vault
2. **See Changes** - Development server rebuilds automatically
3. **Customize Theme** - Edit CSS files in `Themes/` directory
4. **Deploy** - Copy `Outputs/VaultName/` to your hosting service

## Directory Structure

```
obsidian-static-site-generator/
├── build_site.py          # Main build script
├── serve.py               # Development server
├── Themes/                # Theme CSS files
│   ├── paper-theme.css    # Default theme
│   └── dark-theme.css     # Dark mode theme
└── Outputs/               # Generated sites
    └── YourVault/         # Your built website
```

## Build Options

```bash
# Specify output directory
python build_site.py /path/to/vault --output /custom/output

# Use different theme
python build_site.py /path/to/vault --theme dark-theme

# Development server on custom port
python serve.py /path/to/vault --port 3000
```

## Next Steps

- Explore the **Features** page to see all capabilities
- Try different themes with `--theme` option
- Customize themes by editing CSS files
- Deploy your site to GitHub Pages, Netlify, or Vercel

## Common Issues

**Port already in use?**
```bash
python serve.py /path/to/vault --port 8001
```

**Theme not found?**
```bash
# List available themes
python build_site.py
```

**Build errors?**
- Check that vault path exists
- Ensure markdown files are valid
- Verify Python dependencies are installed

## Theme File Structure

All themes are stored in the `Themes/` directory with the naming pattern: `theme-name.css`

```
Themes/
├── paper-theme.css      # Default warm theme
├── dark-theme.css       # Dark mode theme  
└── your-theme.css       # Your custom theme
```

## Step 1: Create Your Theme File

Create a new CSS file in the `Themes/` directory:

```bash
touch Themes/my-custom-theme.css
```

## Step 2: Define CSS Variables

Start with the essential CSS custom properties. These variables control the core colors and typography:

```css
/* my-custom-theme.css */

:root {
  --paper: #ffffff;        /* Background color */
  --ink: #333333;          /* Primary text color */
  --highlight: #ffeb3b;    /* Highlight/selection color */
  --faint: #666666;        /* Secondary text color */
  --accent: #2196f3;       /* Link and accent color */
  font-size: 18px;         /* Base font size */
}
```

## Step 3: Base Styles

Add the fundamental styling that all themes need:

```css
* { box-sizing: border-box; }

html, body {
  margin: 0;
  padding: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  line-height: 1.6;
}

body {
  max-width: 75ch;
  margin: 3rem auto;
  padding: 0 1rem;
}
```

## Step 4: Typography

Define heading styles and text formatting:

```css
h1, h2, h3, h4, h5, h6 {
  font-family: inherit;
  margin: 2.2em 0 .6em;
  font-weight: 600;
  color: var(--accent);
}

h1 { font-size: 2.2em; }
h2 { font-size: 1.8em; }
h3 { font-size: 1.4em; }

a {
  color: var(--accent);
  text-decoration: none;
  border-bottom: 1px solid var(--accent);
}

a:hover {
  background: var(--highlight);
}
```

## Step 5: Code and Content Blocks

Style code blocks, quotes, and other content:

```css
code, pre {
  font-family: "SF Mono", Monaco, "Cascadia Code", monospace;
  background: var(--highlight);
  padding: .2em .4em;
  border-radius: 3px;
  font-size: 0.9em;
}

pre {
  overflow-x: auto;
  padding: 1.2em;
  border-left: 4px solid var(--accent);
}

blockquote {
  margin: 1.5em 0;
  padding: 1em 1.5em;
  background: var(--highlight);
  border-left: 4px solid var(--accent);
  border-radius: 4px;
}

mark {
  background: var(--highlight);
  padding: 0 .2em;
}
```

## Step 6: Tables and Lists

Add table and list styling:

```css
table {
  border-collapse: collapse;
  margin: 2em 0;
  width: 100%;
  border: 1px solid var(--faint);
}

th, td {
  border: 1px solid var(--faint);
  padding: .8em 1em;
  text-align: left;
}

th {
  background: var(--highlight);
  font-weight: 600;
}

ul, ol {
  padding-left: 1.5em;
}

.task-list-item {
  list-style: none;
}

.task-list-item input {
  margin-right: .8em;
  accent-color: var(--accent);
}
```

## Step 7: Responsive Design

Make your theme mobile-friendly:

```css
/* Responsive Design */
@media (max-width: 768px) {
  :root { font-size: 16px; }
  body { 
    max-width: 95%;
    margin: 1.5rem auto;
    padding: 0 1.5rem;
  }
  
  h1, h2, h3, h4, h5, h6 {
    margin: 1.8em 0 .5em;
  }
  
  table {
    font-size: 0.9rem;
    overflow-x: auto;
    display: block;
    white-space: nowrap;
  }
}

@media (max-width: 480px) {
  :root { font-size: 15px; }
  body {
    margin: 1rem auto;
    padding: 0 1rem;
  }
  
  th, td {
    padding: .3em .4em;
  }
}

@media (min-width: 1200px) {
  body {
    max-width: 85ch;
  }
}
```

## Step 8: Navigation Styling

Add responsive navigation styles:

```css
/* Navigation Styles */
.navigation {
  background: var(--paper);
  border-bottom: 1px solid var(--faint);
  padding: 0.8rem 0;
  margin-bottom: 2rem;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-container {
  max-width: 85ch;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 1rem;
}

.nav-links {
  display: flex;
  gap: 1.5rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-links a {
  color: var(--ink);
  text-decoration: none;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.nav-links a:hover {
  background: var(--highlight);
}

/* Responsive Navigation */
@media (max-width: 768px) {
  .nav-container {
    flex-direction: column;
    gap: 1rem;
  }
  
  .nav-links {
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
  }
}
```

## Step 9: Final Touches

Add any special elements and the generated footer:

```css
.callout {
  border: 1px solid var(--accent);
  background: var(--highlight);
  padding: 1.2em;
  margin: 1.5em 0;
  border-radius: 6px;
}

.generated {
  font-size: .85rem;
  color: var(--faint);
  margin-top: 3em;
  text-align: center;
  border-top: 1px solid var(--faint);
  padding-top: 1em;
}
```

## Step 10: Test Your Theme

Build your site with the new theme:

```bash
python build_site.py /path/to/vault my-custom-theme
```

## Theme Design Tips

### Color Harmony
- Use tools like [Coolors.co](https://coolors.co) or [Adobe Color](https://color.adobe.com) for color palette generation
- Ensure sufficient contrast for accessibility (4.5:1 minimum for normal text)
- Test your colors in both light and dark environments

### Typography
- Choose web-safe font stacks or load web fonts
- Maintain consistent vertical rhythm with line-height
- Use a modular scale for font sizes (1.25, 1.414, 1.618 ratios work well)

### Responsive Design
- Design mobile-first, then enhance for larger screens
- Test on actual devices or browser dev tools
- Consider touch targets (minimum 44px for interactive elements)

### Performance
- Minimize CSS file size
- Use CSS custom properties for maintainability
- Avoid heavy animations or large background images

## Common Pitfalls

- **Forgetting responsive design** - Always test on mobile
- **Poor contrast** - Ensure text is readable
- **Inconsistent spacing** - Use consistent margins and padding
- **Breaking navigation** - Always include navigation styles
- **Missing fallbacks** - Provide fallback fonts and colors

Need help? Check out the [[Theme Structure]] guide for more details on how themes are organized, or look at [[Styling Examples]] to see all the components in action.
