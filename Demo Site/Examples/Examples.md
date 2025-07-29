# Examples

This is the index page for the Examples section. It demonstrates how directory index files work.

## What Are Examples?

# Examples

Real-world examples and use cases for the Obsidian Static Site Generator.

## Example Sites

### Personal Knowledge Base
Transform your personal Obsidian vault into a public knowledge repository:

- **Documentation sites** - Technical guides and tutorials
- **Digital gardens** - Interconnected thoughts and ideas
- **Research repositories** - Academic notes and references
- **Project documentation** - Software project wikis

### Blog-style Sites
Use the generator for content-focused websites:

- **Technical blogs** - Programming tutorials and insights
- **Learning journals** - Study notes and progress tracking
- **Recipe collections** - Organized cooking knowledge
- **Travel guides** - Location-based information

## Configuration Examples

### Multi-theme Setup
```bash
# Build the same content with different themes
python build_site.py /vault --output /dist/light --theme paper-theme
python build_site.py /vault --output /dist/dark --theme dark-theme
```

### Development Workflow
```bash
# Terminal 1: Development server
python serve.py /vault --port 8000

# Terminal 2: Theme development  
python serve.py /vault --port 8001 custom-theme
```

### Deployment Examples
```bash
# GitHub Pages deployment
python build_site.py /vault --output /docs

# Netlify deployment
python build_site.py /vault --output /public

# Custom hosting
python build_site.py /vault --output /var/www/html
```

## Vault Structure Examples

### Simple Blog Structure
```
My Blog/
├── My Blog.md             # Homepage
├── About.md               # About page
├── Contact.md             # Contact page
├── Posts/
│   ├── Posts.md           # Blog index
│   ├── First Post.md      # Individual posts
│   └── Second Post.md
└── _drafts/
    └── _work-in-progress.md  # Hidden from navigation
```

### Documentation Site
```
Project Docs/
├── README.md              # Homepage (Project Docs.md)
├── Installation.md        # Setup guide
├── API/
│   ├── API.md            # API overview
│   ├── Authentication.md  # Auth docs
│   └── Endpoints.md      # Endpoint reference
├── Guides/
│   ├── Guides.md         # Tutorials index
│   ├── Quick Start.md    # Getting started
│   └── Advanced Usage.md # Advanced topics
└── Resources/
    └── logo.png          # Assets
```

### Knowledge Base
```
Knowledge Base/
├── Knowledge Base.md      # Homepage
├── Programming/
│   ├── Programming.md     # Programming index
│   ├── Python/
│   │   ├── Python.md      # Python index
│   │   ├── Basics.md      # Python basics
│   │   └── Advanced.md    # Advanced Python
│   └── JavaScript/
│       ├── JavaScript.md  # JS index
│       └── Frameworks.md  # JS frameworks
├── Tools/
│   ├── Tools.md          # Tools index
│   ├── VS Code.md        # Editor notes
│   └── Git.md            # Version control
└── _templates/
    └── _page-template.md  # Template (hidden)
```

## Integration Examples

### GitHub Actions Workflow
```yaml
# .github/workflows/deploy.yml
name: Deploy Site
on:
  push:
    branches: [ main ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install watchdog
      - name: Build site
        run: python build_site.py vault/ --output dist/
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

### Docker Setup
```dockerfile
# Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "serve.py", "/vault", "--host", "0.0.0.0"]
```

These examples show the flexibility of the generator for different types of content and deployment scenarios.

## Available Examples

You can find the following examples in this section:

- [[Basic Example]] - Simple markdown formatting
- [[Complex Example]] - Advanced features and combinations
- [[Code Example]] - Programming-focused content

## Directory Structure

This page exists as `Examples/Examples.md`, which makes it the "index" page for the Examples directory. When you hover over "Examples" in the main navigation, this page becomes the main link, with other files in the directory appearing as dropdown items.

## Index Page Benefits

Having an index page for each directory provides:

1. **Context**: Explains what the section contains
2. **Navigation**: Overview of available content
3. **Organization**: Clear structure for visitors
4. **SEO**: Better search engine understanding

## Cross-References

From here, you can navigate back to:
- [[Demo Site]] - The main homepage
- [[Styling Examples]] - Visual formatting examples
- [[Navigation Demo]] - How menus work
- [[Advanced Features]] - Complex functionality

---

This demonstrates how directory index files create a hierarchical navigation structure.
