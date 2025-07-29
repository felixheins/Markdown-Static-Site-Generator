# Site Builder

Comprehensive guide to the static site generation system.

## 🏗️ Build System

### Smart File Processing
- **Markdown to HTML** - Converts `.md` files to web pages
- **Wiki Link Conversion** - Transforms `[[Page Name]]` to proper HTML links
- **Asset Copying** - Automatically includes images and resources
- **Navigation Generation** - Creates menus from file structure

### Directory Intelligence
- **Automatic Navigation** - Builds dropdown menus from folder hierarchy
- **Index File Detection** - Uses `folder-name.md` as directory homepage
- **Privacy Control** - Files starting with `_` excluded from navigation
- **Resource Handling** - `Resources/` folders copied but not added to navigation

## 🎨 Theme System

### Built-in Themes
```bash
# Available themes
python build_site.py /vault --theme paper-theme  # Default warm theme
python build_site.py /vault --theme dark-theme   # Modern dark mode
```

### Theme Structure
Themes use CSS custom properties for easy customization:

```css
:root {
  --paper: #fbf9f7;      /* Background color */
  --ink: #222;           /* Text color */
  --highlight: #fff8b7;  /* Highlight color */
  --faint: #666;         /* Secondary text */
  --accent: #ffb347;     /* Links and accents */
}
```

### Creating Custom Themes
1. Copy an existing theme: `cp paper-theme.css my-theme.css`
2. Edit CSS variables and styles
3. Use with: `python build_site.py /vault --theme my-theme`

## 🔄 Development Server

### Live Development Features
- **File Watching** - Monitors markdown, CSS, and Python files
- **Auto Rebuild** - Regenerates site when files change  
- **Local Server** - Serves your site at `http://localhost:8000`
- **Background Process** - Non-blocking terminal operation

### Server Commands
```bash
# Basic development server
python serve.py "Demo Site"

# Custom port and theme
python serve.py "Demo Site" --port 3000
python serve.py "Demo Site" dark-theme

# Network accessible (for testing on devices)
python serve.py "Demo Site" --host 0.0.0.0
```

## 📱 Navigation System

### Automatic Menu Generation
The builder creates navigation menus automatically:

```
Your Vault/
├── Vault Name.md          # Becomes "Home" in navigation
├── Page One.md            # Root level nav item
├── Folder/
│   ├── Folder.md          # Dropdown main item
│   ├── Subpage.md         # Appears in dropdown
│   └── _private.md        # Hidden from navigation
└── Resources/
    └── image.png          # Copied but not in navigation
```

Results in navigation:
- **Home** (Vault Name)
- **Page One**  
- **Folder** ▼
  - Folder (index)
  - Subpage

### Privacy and Organization
- **Underscore Files**: Files starting with `_` are built but hidden from navigation
- **Resource Exclusion**: `Resources/` folders are copied but not added to menus
- **Index Priority**: Files matching folder names become dropdown main items

## 🚀 Static Output

### Generated Structure
```
Outputs/VaultName/
├── index.html             # Homepage
├── page-one.html          # Individual pages (slugified)
├── folder/
│   ├── folder.html        # Folder index
│   ├── subpage.html       # Subpages
│   └── private.html       # Hidden files (still built)
├── style.css              # Theme CSS
└── Resources/             # Copied assets
    └── image.png
```

### Deployment Ready Features
- **Self-contained** - All assets bundled together
- **No Dependencies** - Pure HTML/CSS output
- **Clean URLs** - SEO-friendly page names
- **Mobile Responsive** - Works on all devices

## 🔧 Build Commands

### Basic Usage
```bash
# Build to default output location
python build_site.py "Your Vault"

# Custom output directory  
python build_site.py "Your Vault" --output /custom/path

# Specific theme
python build_site.py "Your Vault" --theme dark-theme

# All options together
python build_site.py "Your Vault" /custom/output dark-theme
```

### Output Locations
- **Default**: `Outputs/VaultName/` (spaces become underscores)
- **Custom**: Any directory you specify
- **Relative**: Relative to script location
- **Absolute**: Full system paths supported

## 🎯 Advanced Features

### File Processing Rules
1. **Markdown files** (`.md`) are converted to HTML
2. **Index detection** - Files matching folder names become directory indexes  
3. **Wiki links** - `[[Page Name]]` becomes clickable navigation
4. **Asset preservation** - All non-markdown files are copied
5. **Slug generation** - Filenames become URL-friendly

### Theme Development
Themes are standard CSS files with these requirements:
- Use CSS custom properties for colors
- Include navigation styles for dropdowns
- Provide responsive design rules
- Support both light and dark preferences

### Performance Considerations
- **Fast builds** - Efficient markdown processing
- **Selective updates** - Development server only rebuilds changed files
- **Optimized output** - Clean HTML structure
- **Asset handling** - Smart copying without duplication

This build system transforms any organized markdown collection into a professional static website with minimal configuration required.

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