# Quick Start Example

A complete walkthrough of setting up your first site.

## Scenario: Personal Documentation Site

Let's say you have an Obsidian vault called "My Notes" with documentation you want to share.

### Vault Structure
```
My Notes/
├── My Notes.md           # Will become homepage
├── Projects/
│   ├── Projects.md       # Projects overview
│   ├── Website.md        # Project details
│   └── App Ideas.md      # More projects
├── Learning/
│   ├── Learning.md       # Learning index
│   ├── Python.md         # Programming notes
│   └── Design.md         # Design notes
├── _drafts/
│   └── _unfinished.md    # Won't appear in navigation
└── Resources/
    └── diagram.png       # Will be copied to output
```

### Step 1: Build the Site

```bash
# Clone the generator
git clone https://github.com/yourusername/obsidian-static-site-generator
cd obsidian-static-site-generator

# Install dependencies
python -m venv .venv
source .venv/bin/activate
pip install watchdog

# Build your site
python build_site.py "/path/to/My Notes"
```

### Step 2: Generated Output

The generator creates:
```
Outputs/My_Notes/
├── index.html            # From "My Notes.md"
├── projects.html         # From "Projects/Projects.md"
├── website.html          # From "Projects/Website.md"
├── app-ideas.html        # From "Projects/App Ideas.md"
├── learning.html         # From "Learning/Learning.md"
├── python.html           # From "Learning/Python.md"
├── design.html           # From "Learning/Design.md"
├── unfinished.html       # From "_drafts/_unfinished.md" (hidden from nav)
├── style.css             # Theme CSS
└── Resources/
    └── diagram.png       # Copied asset
```

### Step 3: Navigation Structure

The generated navigation will be:
- **My Notes** (homepage)
- **Projects** (dropdown)
  - Projects (main page)
  - Website
  - App Ideas
- **Learning** (dropdown)
  - Learning (main page)
  - Python
  - Design

Note: `_unfinished.md` is not in the navigation but still accessible via URL.

### Step 4: Development Server

```bash
# Start live development server
python serve.py "/path/to/My Notes"
```

Visit `http://localhost:8000` to see your site. Edit any markdown file and watch it rebuild automatically!

### Step 5: Customization

Try different themes:
```bash
# Dark theme
python serve.py "/path/to/My Notes" dark-theme

# Custom theme (create Themes/my-theme.css first)
python serve.py "/path/to/My Notes" my-theme
```

### Step 6: Deploy

Deploy the contents of `Outputs/My_Notes/` to any static hosting:

- **GitHub Pages**: Push to `docs/` folder
- **Netlify**: Drag and drop the folder
- **Vercel**: Connect your repository
- **Traditional hosting**: Upload via FTP

## Result

You now have a clean, navigable website that:
- ✅ Preserves your Obsidian organization
- ✅ Has working navigation between pages
- ✅ Includes all your assets
- ✅ Looks professional with minimal effort
- ✅ Updates automatically during development

This basic example shows how the generator transforms your personal notes into a shareable website with zero configuration!
