# Markdown Support

Complete showcase of all markdown elements supported by the Markdown Static Site Generator.

## Text Formatting

**Bold text** 
<details><summary>Show markdown syntax</summary>

```markdown
**Bold text**
```
</details>

*Italic text*
<details><summary>Show markdown syntax</summary>

```markdown
*Italic text*
```
</details>

***Bold and italic***
<details><summary>Show markdown syntax</summary>

```markdown
***Bold and italic***
```
</details>

~~Strikethrough~~
<details><summary>Show markdown syntax</summary>

```markdown
~~Strikethrough~~
```
</details>

==Highlighted text==
<details><summary>Show markdown syntax</summary>

```markdown
==Highlighted text==
```
</details>

Inline `code` with backticks
<details><summary>Show markdown syntax</summary>

```markdown
Inline `code` with backticks
```
</details>

## Headers

# Header 1
<details><summary>Show markdown syntax</summary>

```markdown
# Header 1
```
</details>

## Header 2
<details><summary>Show markdown syntax</summary>

```markdown
## Header 2
```
</details>

### Header 3
<details><summary>Show markdown syntax</summary>

```markdown
### Header 3
```
</details>

#### Header 4
##### Header 5
###### Header 6

<details><summary>Show syntax for Headers 4-6</summary>

```markdown
#### Header 4
##### Header 5
###### Header 6
```
</details>

## Lists

### Unordered Lists
- Item 1
- Item 2
  - Nested item
  - Another nested item
- Item 3

<details><summary>Show markdown syntax</summary>

```markdown
- Item 1
- Item 2
  - Nested item
  - Another nested item
- Item 3
```
</details>

### Ordered Lists
1. First item
2. Second item
   1. Nested numbered item
   2. Another nested item
3. Third item

<details><summary>Show markdown syntax</summary>

```markdown
1. First item
2. Second item
   1. Nested numbered item
   2. Another nested item
3. Third item
```
</details>

### Task Lists
- [x] Completed task
- [ ] Incomplete task
- [x] Another completed task

<details><summary>Show markdown syntax</summary>

```markdown
- [x] Completed task
- [ ] Incomplete task
- [x] Another completed task
```
</details>

## Links

### Standard Links
[External link](https://example.com)

[Link with title](https://example.com "Title text")

<details><summary>Show markdown syntax</summary>

```markdown
[External link](https://example.com)
[Link with title](https://example.com "Title text")
```
</details>

### Wiki Links (Obsidian-style)
[[Getting Started]] - Links to other pages

[[Features|Custom link text]] - Wiki link with custom display text

<details><summary>Show markdown syntax</summary>

```markdown
[[Getting Started]]
[[Features|Custom link text]]
```
</details>

### Reference Links
[Reference link][1]

[Another reference][ref]

[1]: https://example.com
[ref]: https://github.com

<details><summary>Show markdown syntax</summary>

```markdown
[Reference link][1]
[Another reference][ref]

[1]: https://example.com
[ref]: https://github.com
```
</details>

## Images

![Alt text](Resources/sample-image.txt "Optional title")

<details><summary>Show markdown syntax</summary>

```markdown
![Alt text](Resources/sample-image.txt "Optional title")
```
</details>

### Image with Reference
![Reference image][img1]

[img1]: Resources/sample-image.txt "Sample image"

<details><summary>Show markdown syntax</summary>

```markdown
![Reference image][img1]

[img1]: Resources/sample-image.txt "Sample image"
```
</details>

## Code Blocks

### Basic Code Block
```
Plain code block
No syntax highlighting
```

<details><summary>Show markdown syntax</summary>

````markdown
```
Plain code block
No syntax highlighting
```
````
</details>

### Syntax Highlighted Code
```python
def hello_world():
    print("Hello, World!")
    return True
```

<details><summary>Show markdown syntax</summary>

````markdown
```python
def hello_world():
    print("Hello, World!")
    return True
```
````
</details>

```javascript
function greetUser(name) {
    console.log(`Hello, ${name}!`);
    return name.toUpperCase();
}
```

<details><summary>Show markdown syntax</summary>

````markdown
```javascript
function greetUser(name) {
    console.log(`Hello, ${name}!`);
    return name.toUpperCase();
}
```
````
</details>

```bash
# Shell commands
cd /path/to/directory
python build_site.py "Demo Site"
```

<details><summary>Show markdown syntax</summary>

````markdown
```bash
# Shell commands
cd /path/to/directory
python build_site.py "Demo Site"
```
````
</details>

## Tables

| Feature | Description | Status |
|---------|-------------|--------|
| Wiki Links | `[[Page Name]]` linking | ✅ Supported |
| Themes | CSS-based styling | ✅ Supported |
| Live Server | Development server | ✅ Supported |
| Tables | This table! | ✅ Supported |

<details><summary>Show markdown syntax</summary>

```markdown
| Feature | Description | Status |
|---------|-------------|--------|
| Wiki Links | `[[Page Name]]` linking | ✅ Supported |
| Themes | CSS-based styling | ✅ Supported |
| Live Server | Development server | ✅ Supported |
| Tables | This table! | ✅ Supported |
```
</details>

### Table Alignment

| Left Aligned | Center Aligned | Right Aligned |
|:-------------|:--------------:|--------------:|
| Left | Center | Right |
| Text | Text | Text |

<details><summary>Show markdown syntax</summary>

```markdown
| Left Aligned | Center Aligned | Right Aligned |
|:-------------|:--------------:|--------------:|
| Left | Center | Right |
| Text | Text | Text |
```
</details>

## Quotes

> This is a blockquote
> 
> It can span multiple lines
> and paragraphs

<details><summary>Show markdown syntax</summary>

```markdown
> This is a blockquote
> 
> It can span multiple lines
> and paragraphs
```
</details>

> Nested quotes:
> > This is nested
> > inside another quote

<details><summary>Show markdown syntax</summary>

```markdown
> Nested quotes:
> > This is nested
> > inside another quote
```
</details>

## Horizontal Rules

Three or more dashes:

---

Three or more asterisks:

***

<details><summary>Show markdown syntax</summary>

```markdown
Three or more dashes:
---

Three or more asterisks:
***
```
</details>

## Line Breaks

Hard line break with two spaces at end  
This line follows a hard break

<details><summary>Show markdown syntax</summary>

```markdown
Hard line break with two spaces at end  
This line follows a hard break
```
Note: Two spaces at the end of the first line create the line break.
</details>

Soft line break
continues on same paragraph

<details><summary>Show markdown syntax</summary>

```markdown
Soft line break
continues on same paragraph
```
</details>

## Footnotes

Here's a sentence with a footnote[^1].

Another footnote reference[^note].

[^1]: This is the footnote content.
[^note]: Named footnotes work too.

<details><summary>Show markdown syntax</summary>

```markdown
Here's a sentence with a footnote[^1].

Another footnote reference[^note].

[^1]: This is the footnote content.
[^note]: Named footnotes work too.
```
</details>

## HTML Elements

You can use <mark>HTML tags</mark> directly in markdown.

<details>
<summary>Click to expand</summary>

This content is hidden by default and can be expanded.

</details>

<details><summary>Show markdown syntax</summary>

```markdown
You can use <mark>HTML tags</mark> directly in markdown.

<details>
<summary>Click to expand</summary>

This content is hidden by default and can be expanded.

</details>
```
</details>

## Escape Characters

\*Not italic\* - Escaped asterisks  
\`Not code\` - Escaped backticks  
\[Not a link\] - Escaped brackets

<details><summary>Show markdown syntax</summary>

```markdown
\*Not italic\* - Escaped asterisks
\`Not code\` - Escaped backticks
\[Not a link\] - Escaped brackets
```
</details>

---

**Note**: This generator supports all standard CommonMark features plus Obsidian-style extensions like wiki links (`[[Page Name]]`) and highlights (`==text==`). All elements are automatically styled by your chosen theme.