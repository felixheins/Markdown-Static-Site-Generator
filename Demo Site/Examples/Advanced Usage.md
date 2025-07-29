# Complex Example

# Advanced Usage Example

A comprehensive example showing advanced features and organization patterns.

## Scenario: Technical Documentation Site

This example shows how to structure a complex technical documentation site with multiple sections, nested content, and advanced features.

### Complex Vault Structure

```
TechDocs/
├── TechDocs.md                    # Homepage
├── Getting Started/
│   ├── Getting Started.md         # Quick start guide
│   ├── Installation.md            # Installation steps
│   ├── Configuration.md           # Config options
│   └── _troubleshooting-draft.md  # Hidden from nav
├── API Documentation/
│   ├── API Documentation.md       # API overview
│   ├── Authentication/
│   │   ├── Authentication.md      # Auth overview
│   │   ├── OAuth.md              # OAuth details
│   │   └── API Keys.md           # API key management
│   ├── Endpoints/
│   │   ├── Endpoints.md          # Endpoints overview
│   │   ├── Users.md              # User endpoints
│   │   ├── Projects.md           # Project endpoints
│   │   └── Files.md              # File endpoints
│   └── SDKs/
│       ├── SDKs.md               # SDK overview
│       ├── Python SDK.md         # Python integration
│       ├── JavaScript SDK.md     # JS integration
│       └── REST Examples.md      # REST examples
├── Guides/
│   ├── Guides.md                 # Tutorials index
│   ├── Beginner/
│   │   ├── Beginner.md           # Beginner guide index
│   │   ├── First Steps.md        # Basic tutorial
│   │   └── Common Patterns.md    # Patterns guide
│   ├── Advanced/
│   │   ├── Advanced.md           # Advanced guide index
│   │   ├── Custom Integrations.md # Integration guide
│   │   └── Performance.md        # Performance tips
│   └── Best Practices.md         # General best practices
├── Reference/
│   ├── Reference.md              # Reference index
│   ├── Error Codes.md            # Error reference
│   ├── Rate Limits.md            # Rate limiting info
│   └── Changelog.md             # Version history
├── _internal/
│   ├── _meeting-notes.md         # Internal notes (hidden)
│   └── _roadmap-draft.md         # Internal roadmap (hidden)
└── Resources/
    ├── architecture-diagram.png  # Technical diagrams
    ├── flow-chart.svg           # Process flows
    └── logo.png                 # Branding assets
```

### Generated Navigation Structure

This complex structure generates the following navigation:

- **TechDocs** (homepage)
- **Getting Started** (dropdown)
  - Getting Started (overview)
  - Installation
  - Configuration
- **API Documentation** (dropdown)
  - API Documentation (overview)
  - **Authentication** (sub-dropdown)
    - Authentication (overview)
    - OAuth
    - API Keys
  - **Endpoints** (sub-dropdown)
    - Endpoints (overview)
    - Users
    - Projects
    - Files
  - **SDKs** (sub-dropdown)
    - SDKs (overview)
    - Python SDK
    - JavaScript SDK
    - REST Examples
- **Guides** (dropdown)
  - Guides (overview)
  - **Beginner** (sub-dropdown)
    - Beginner (overview)
    - First Steps
    - Common Patterns
  - **Advanced** (sub-dropdown)
    - Advanced (overview)
    - Custom Integrations
    - Performance
  - Best Practices
- **Reference** (dropdown)
  - Reference (overview)
  - Error Codes
  - Rate Limits
  - Changelog

### Advanced Build Commands

```bash
# Build for production with custom output
python build_site.py TechDocs --output /var/www/docs --theme dark-theme

# Development with custom port for team access
python serve.py TechDocs --host 0.0.0.0 --port 8080

# Multiple theme builds for A/B testing
python build_site.py TechDocs --output dist/light --theme paper-theme
python build_site.py TechDocs --output dist/dark --theme dark-theme
```

### Cross-References and Linking

The complex structure supports sophisticated cross-referencing:

```markdown
# In API Documentation.md
For authentication details, see [[Authentication]].
For specific endpoint information, check [[Endpoints]].

# In OAuth.md  
After setting up OAuth, you can test with the [[Python SDK]].
See [[Error Codes]] for troubleshooting authentication issues.

# In First Steps.md
Complete the [[Installation]] before proceeding.
Advanced users may skip to [[Advanced]] tutorials.
```

### Content Organization Patterns

#### Index File Strategy
Each directory has an index file (same name as directory) that serves as:
- **Overview page** - Explains the section
- **Navigation hub** - Links to subsections  
- **Main dropdown target** - What users see when clicking dropdown

#### Privacy Levels
- **Public pages** - Normal .md files, appear in navigation
- **Hidden pages** - _underscore.md files, accessible but not in navigation
- **Resources** - Assets copied but not processed as pages

#### Hierarchical Information Architecture
- **Top level** - Major product areas
- **Second level** - Functional categories
- **Third level** - Specific topics and implementations
- **Cross-cutting** - Reference materials accessible from anywhere

### Advanced Features Demonstrated

#### Multi-level Dropdowns
The navigation system handles nested folders elegantly:
- Main categories become top-level dropdowns
- Subdirectories become nested dropdowns
- Index files serve as section overviews

#### Asset Management
Resources are automatically:
- Copied to output directory
- Accessible via relative paths
- Preserved in original structure

#### Internal Documentation
Files starting with `_` allow for:
- Internal team documentation
- Draft content not ready for publication
- Template files for consistency
- Meeting notes and planning documents

### Deployment Strategies

#### Multi-environment Builds
```bash
# Staging environment
python build_site.py TechDocs --output staging/ --theme paper-theme

# Production environment  
python build_site.py TechDocs --output production/ --theme dark-theme

# Internal documentation (includes _internal files)
# Custom build script could process these separately
```

#### CI/CD Integration
```yaml
# GitHub Actions example
- name: Build documentation
  run: |
    python build_site.py TechDocs --output public/
    # Deploy public/ directory to hosting service
```

## Results

This advanced example demonstrates:

- ✅ **Scalable organization** - Handles complex information hierarchies
- ✅ **Professional navigation** - Multi-level dropdowns with clear structure
- ✅ **Content privacy** - Internal documents hidden from public navigation
- ✅ **Cross-referencing** - Maintains links across complex structures
- ✅ **Asset management** - Handles images, diagrams, and resources
- ✅ **Team workflows** - Supports collaborative documentation development
- ✅ **Deployment flexibility** - Multiple build targets and environments

This shows how the generator scales from simple personal sites to enterprise-level documentation systems while maintaining simplicity and zero configuration.

## Advanced Formatting Combinations

Here's text with ==highlighted **bold** text== and other combinations:

- **Bold** with ==highlighting==
- *Italic* with `inline code`
- ==Highlighted text with [[wiki links]]== 

## Nested Lists

1. First level item
   - Second level bullet
   - Another second level
     - Third level bullet
     - Another third level
2. Back to first level
   1. Numbered sub-item
   2. Another numbered sub-item

## Task Lists with Complex Items

- [x] Completed task with ==highlighting==
- [x] Completed task with **bold text**
- [ ] Pending task with `code`
- [ ] Pending task with [[Internal Link]]

## Complex Code Blocks

Here's a more complex code example with multiple languages:

```python
class ObsidianConverter:
    def __init__(self, vault_path, output_path):
        self.vault = Path(vault_path)
        self.output = Path(output_path)
        self.markdown = markdown.Markdown(
            extensions=["toc", "footnotes", "tables", "fenced_code", "codehilite", "meta"],
            extension_configs={"codehilite": {"guess_lang": False}},
            output_format="html5",
        )
    
    def convert_wiki_links(self, text):
        """Convert [[wiki links]] to markdown links"""
        pattern = r'\[\[([^\]|]+)(\|([^\]]+))?\]\]'
        return re.sub(pattern, self._replace_wiki_link, text)
```

```bash
# Build the demo site
python build_site.py demo_site_md demo_output

# Serve locally for testing
cd demo_output
python -m http.server 8000
```

## Advanced Tables

| Feature | Implementation | Status | Notes |
|---------|----------------|---------|-------|
| Wiki Links | Regex replacement | ✅ Complete | Handles aliases |
| Highlighting | `==text==` → `<mark>` | ✅ Complete | CSS styled |
| Code Blocks | Pygments | ✅ Complete | Multiple languages |
| Dropdowns | CSS + HTML | ✅ Complete | Hover activated |
| Assets | File copying | ✅ Complete | Preserves structure |

## Blockquotes with Complex Content

> This blockquote contains ==highlighted text==, **bold text**, and even `code snippets`.
> 
> It can also contain [[wiki links]] and other markdown features.
> 
> > Nested blockquotes are also supported
> > With their own styling

## Multiple Cross-References

This complex example references:
- Back to [[Examples]] index
- The simple [[Basic Example]]
- Main [[Demo Site]] page
- [[Styling Examples]] for more visual elements
- [[Advanced Features]] for technical details
- [[Navigation Demo]] for menu information

## Footnotes and References

This converter supports footnotes[^1] and multiple references[^2] within the same document.

The footnotes appear at the bottom of the page with proper linking[^3].

---

[^1]: This is the first footnote with some explanation.
[^2]: This is the second footnote with different content.
[^3]: This footnote demonstrates multiple references to footnotes within a single document.

This complex example shows how various markdown features work together in the converted site.
