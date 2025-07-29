# Features

Comprehensive overview of all capabilities in the Obsidian Static Site Generator.

## 🏗️ Build System

### Smart File Processing
- **Markdown to HTML** - Full CommonMark support with extensions
- **Wiki Link Conversion** - Preserves `[[Page Name]]` linking
- **Asset Copying** - Automatically includes images and resources
- **Index Generation** - Creates navigation from file structure

### Directory Intelligence
- **Automatic Navigation** - Builds menus from folder hierarchy
- **Index File Detection** - Uses folder-name.md as directory index
- **Root Level Support** - Handles vault-level index files

## 🎨 Theme System

### Built-in Themes
- **Paper Theme** - Warm, reMarkable-inspired design
- **Dark Theme** - Modern dark mode with blue accents

### Theme Features
- **CSS Variables** - Easy customization with custom properties
- **Responsive Design** - Mobile-first approach
- **Navigation Styling** - Dropdown menus and hover effects
- **Typography Control** - Font families, sizes, and spacing

### Customization
```bash
# Use built-in themes
python build_site.py /vault --theme dark-theme

# Create custom themes in Themes/ directory
```

## 🔄 Development Server

### Live Development
- **File Watching** - Monitors markdown and CSS changes
- **Auto Rebuild** - Instant site regeneration on save
- **Hot Reload** - Browser refresh on changes
- **Multi-format Support** - Watches .md, .css, and build scripts

### Server Features
- **Custom Ports** - Avoid conflicts with `--port` option
- **Network Access** - Use `--host 0.0.0.0` for device testing
- **Error Handling** - Clear feedback on build failures
- **Background Mode** - Non-blocking terminal operation

## 📱 Navigation System

### Automatic Menu Generation
- **Hierarchical Structure** - Mirrors your folder organization
- **Dropdown Menus** - Subdirectories become collapsible sections
- **Smart Ordering** - Index files appear first in dropdowns
- **Clean URLs** - Slugified filenames for web-friendly paths

### Privacy Controls
- **Underscore Files** - Files starting with `_` excluded from navigation
- **Resource Exclusion** - Resources/ folders ignored for navigation
- **Selective Processing** - Full control over what appears publicly

## 📝 Content Features

### Markdown Support
- **Tables** - Full table formatting
- **Code Blocks** - Syntax highlighting with language detection
- **Footnotes** - Academic-style footnote support
- **Table of Contents** - Auto-generated TOC from headers
- **Metadata** - Front matter support for titles and meta

### Link Processing
- **Wiki Links** - `[[Page Name]]` converted to proper HTML links
- **Cross References** - Maintains link integrity across pages
- **Asset Links** - Images and files properly resolved
- **External Links** - Standard markdown links preserved

## 🚀 Deployment Ready

### Static Output
- **Self-contained** - All assets bundled together
- **CDN Friendly** - Optimized for content delivery networks
- **No Dependencies** - Pure HTML/CSS output
- **Fast Loading** - Minimal overhead and optimized structure

### Hosting Compatibility
- **GitHub Pages** - Direct deployment support
- **Netlify** - Drag-and-drop ready
- **Vercel** - Static hosting compatible
- **Any Web Server** - Standard HTML/CSS/JS output

## ⚡ Performance

### Build Optimization
- **Fast Processing** - Efficient markdown parsing
- **Selective Updates** - Development server only rebuilds changed content
- **Asset Optimization** - Smart copying and organization
- **Memory Efficient** - Handles large vaults without issues

### Output Optimization
- **Clean HTML** - Semantic markup structure
- **CSS Variables** - Efficient styling system
- **Minimal JavaScript** - Pure CSS navigation system
- **Mobile Optimized** - Responsive design patterns

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

### Development Server
```bash
# Basic server
python serve.py /path/to/vault

# Custom port and theme
python serve.py /vault theme-name --port 3000

# Network accessible
python serve.py /vault --host 0.0.0.0 --port 8080
```

## 📁 File Organization

### Supported Structure
```
Your Vault/
├── Vault Name.md          # Becomes index.html
├── Page One.md            # Root level page
├── Page Two.md            # Root level page
├── Folder/
│   ├── Folder.md          # Folder index (dropdown main)
│   ├── Subpage.md         # Appears in dropdown
│   └── _private.md        # Hidden from navigation
└── Resources/
    └── image.png          # Copied to output
```

### Output Structure
```
Outputs/VaultName/
├── index.html             # Main page
├── page-one.html          # Slugified names
├── page-two.html
├── folder/
│   ├── folder.html        # Folder index
│   ├── subpage.html
│   └── private.html       # Still generated, not in nav
├── style.css              # Theme CSS
└── Resources/
    └── image.png          # Copied assets
```

This system provides everything you need to convert your Obsidian vault into a professional static website with minimal configuration and maximum flexibility.

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
