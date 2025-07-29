# Features

## Overview

The Markdown Static Site Generator transforms your markdown files into a beautiful static website with minimal configuration.

## 🏗️ Build System

### Smart File Processing
- **Markdown to HTML** - Converts markdown files to web pages
- **Wiki Link Conversion** - Preserves `[[Page Name]]` linking style
- **Asset Copying** - Automatically includes images and resources
- **Navigation Generation** - Creates menus from file structure

### Directory Intelligence
- **Automatic Navigation** - Builds dropdown menus from folder hierarchy
- **Index File Detection** - Uses folder-name.md as directory homepage
- **Privacy Control** - Files starting with `_` excluded from navigation

## 🎨 Theme System

### Built-in Themes
- **Paper Theme** - Warm, readable design
- **Dark Theme** - Modern dark mode

### Theme Features
- **CSS Variables** - Easy customization with custom properties
- **Responsive Design** - Works on mobile and desktop
- **Navigation Styling** - Dropdown menus and hover effects

### Using Themes
```bash
# Use built-in themes
python build_site.py /vault --theme dark-theme

# Create custom themes in the root directory
```

## 🔄 Development Server

### Live Development
- **File Watching** - Monitors markdown and CSS changes
- **Auto Rebuild** - Regenerates site when files change
- **Local Server** - Serves your site at localhost:8000

### Server Options
```bash
# Custom port
python serve.py /vault --port 3000

# Different theme
python serve.py /vault dark-theme
```

## 📱 Navigation System

### Automatic Menu Generation
- **Hierarchical Structure** - Mirrors your folder organization
- **Dropdown Menus** - Subdirectories become collapsible sections
- **Clean URLs** - Converts filenames to web-friendly paths

## 📝 Content Features

### Markdown Support
- **Standard Markdown** - Headers, lists, links, images
- **Tables** - Full table formatting
- **Code Blocks** - Programming code with formatting

### Link Processing
- **Wiki Links** - `[[Page Name]]` converted to proper HTML links
- **Asset Links** - Images and files properly resolved
- **External Links** - Standard markdown links preserved

## 🚀 Static Output

### Generated Files
- **Self-contained** - All assets bundled together
- **No Dependencies** - Pure HTML/CSS output
- **Fast Loading** - Optimized file structure

### Deployment Ready
- **GitHub Pages** - Can be deployed directly
- **Netlify/Vercel** - Works with static hosting services
- **Any Web Server** - Standard HTML files

## 🔧 Configuration Options

### Build Commands
```bash
# Basic build
python build_site.py /path/to/vault

# Custom output location
python build_site.py /vault --output /custom/path

# Specific theme
python build_site.py /vault --theme theme-name
```

### File Organization
```
Your Vault/
├── Vault Name.md          # Becomes index.html
├── Page One.md            # Root level page
├── Folder/
│   ├── Folder.md          # Folder index
│   └── Subpage.md         # Appears in dropdown
└── Resources/
    └── image.png          # Copied to output
```

This system provides everything you need to convert your markdown files into a professional static website.

## Custom CSS Variables

Beyond the basic theme variables, you can create additional CSS custom properties for more complex theming:

```css
:root {
  /* Core theme variables */
  --paper: #fbf9f7;
  --ink: #222;
  --highlight: #fff8b7;
  --faint: #666;
  --accent: #ffb347;
  
  /* Extended variables for advanced theming */
  --border-radius: 4px;
  --shadow: 0 2px 4px rgba(0,0,0,0.1);
  --transition: 0.2s ease-in-out;
  --max-width: 75ch;
  
  /* Typography scale */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  
  /* Spacing scale */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
}
```

## Advanced Navigation Styling

### Dropdown Menus

The navigation system supports dropdown menus for subdirectories. You can style these with advanced CSS:

```css
.nav-dropdown {
  position: relative;
  display: inline-block;
}

.nav-dropdown-content {
  display: none;
  position: absolute;
  background: var(--paper);
  min-width: 200px;
  box-shadow: var(--shadow);
  border: 1px solid var(--faint);
  border-radius: var(--border-radius);
  z-index: 1000;
}

.nav-dropdown:hover .nav-dropdown-content {
  display: block;
}

.nav-dropdown-content a {
  display: block;
  padding: var(--space-sm) var(--space-md);
  transition: background-color var(--transition);
}

.nav-dropdown-content a:hover {
  background: var(--highlight);
}
```

## Dark Mode Implementation

Create themes that support automatic dark mode detection:

```css
/* Default light theme */
:root {
  --paper: #fbf9f7;
  --ink: #222;
  --highlight: #fff8b7;
  --faint: #666;
  --accent: #ffb347;
}

/* Dark mode override */
@media (prefers-color-scheme: dark) {
  :root {
    --paper: #1a1a1a;
    --ink: #e0e0e0;
    --highlight: #3a3a00;
    --faint: #888;
    --accent: #6ab7ff;
  }
  
  /* Adjust images for dark mode */
  img {
    filter: brightness(0.8) contrast(1.2);
  }
}
```

## Typography Enhancements

### Advanced Font Loading

Load custom fonts efficiently:

```css
/* Font loading with fallbacks */
@font-face {
  font-family: 'CustomFont';
  src: url('fonts/CustomFont.woff2') format('woff2'),
       url('fonts/CustomFont.woff') format('woff');
  font-display: swap; /* Improves loading performance */
}

body {
  font-family: 'CustomFont', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
```

### Responsive Typography

Create fluid, responsive typography:

```css
/* Fluid typography that scales with viewport */
:root {
  --fluid-min-width: 320;
  --fluid-max-width: 1140;
  --fluid-min-size: 16;
  --fluid-max-size: 19;
}

html {
  font-size: calc(
    var(--fluid-min-size) * 1px + 
    (var(--fluid-max-size) - var(--fluid-min-size)) * 
    (100vw - var(--fluid-min-width) * 1px) / 
    (var(--fluid-max-width) - var(--fluid-min-width))
  );
}
```

## Animation and Transitions

Add subtle animations to enhance user experience:

```css
/* Page transition effects */
.page-content {
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Hover animations */
.nav-links a {
  transition: all var(--transition);
  position: relative;
}

.nav-links a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--accent);
  transition: width var(--transition);
}

.nav-links a:hover::after {
  width: 100%;
}
```

## Print Styles

Create print-friendly versions of your themes:

```css
@media print {
  /* Remove navigation and interactive elements */
  .navigation,
  .nav-dropdown {
    display: none !important;
  }
  
  /* Optimize typography for print */
  body {
    font-size: 12pt;
    line-height: 1.4;
    color: #000;
    background: #fff;
  }
  
  /* Show URLs for links */
  a[href^="http"]:after {
    content: " (" attr(href) ")";
    font-size: 0.8em;
    color: #666;
  }
  
  /* Force black text for print */
  * {
    color: #000 !important;
    background: #fff !important;
  }
}
```

## Accessibility Enhancements

### Enhanced Focus Indicators

Create better focus indicators for keyboard navigation:

```css
/* Enhanced focus styles */
a:focus,
button:focus,
[tabindex]:focus {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: var(--border-radius);
}

/* Skip to content link */
.skip-to-content {
  position: absolute;
  top: -40px;
  left: 6px;
  background: var(--accent);
  color: var(--paper);
  padding: 8px;
  text-decoration: none;
  transition: top 0.3s;
}

.skip-to-content:focus {
  top: 6px;
}
```

### High Contrast Mode Support

Support Windows High Contrast mode:

```css
@media (prefers-contrast: high) {
  :root {
    --paper: Canvas;
    --ink: CanvasText;
    --accent: LinkText;
    --highlight: Highlight;
    --faint: GrayText;
  }
  
  /* Remove subtle styling that may not work in high contrast */
  .subtle-border,
  .subtle-shadow {
    border: 1px solid;
    box-shadow: none;
  }
}
```

## Performance Optimization

### CSS Optimization

Optimize your theme CSS for better performance:

```css
/* Use efficient selectors */
.nav-links a { /* Good: class-based selector */ }

/* Minimize repaints and reflows */
.hover-element {
  /* Use transform instead of changing position */
  transform: translateY(-2px);
  transition: transform var(--transition);
}

/* Optimize animations */
.animated-element {
  /* Only animate transform and opacity for best performance */
  transition: transform var(--transition), opacity var(--transition);
  will-change: transform, opacity;
}
```

## Testing Your Advanced Theme

### Cross-browser Testing
Test your advanced features across different browsers:
- Chrome/Chromium
- Firefox  
- Safari
- Edge

### Performance Testing
Use browser dev tools to check:
- CSS loading time
- Animation performance (60fps)
- Mobile performance
- Accessibility audit scores

### Feature Detection
Use feature detection for advanced CSS:

```css
/* Support for older browsers */
@supports (display: grid) {
  .advanced-layout {
    display: grid;
  }
}

@supports not (display: grid) {
  .advanced-layout {
    display: flex;
    flex-wrap: wrap;
  }
}
```

These advanced techniques will help you create sophisticated, performant, and accessible themes for the Obsidian Static Site Generator.

---

For more theme development guidance, see:
- [[Creating a New Theme]] - Step-by-step theme creation
- [[Theme Structure]] - Understanding CSS organization
- [[Styling Examples]] - Visual examples of all components
