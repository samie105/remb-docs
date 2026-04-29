---
title: "style:"
source: "https://svelte.dev/docs/svelte/style"
canonical_url: "https://svelte.dev/docs/svelte/style"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:44.132Z"
content_hash: "64074b0b25f969a00f7c1fa31b4e844da611a4a9e67baa44bc36f860d43a7077"
menu_path: ["style:"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/animate/index.md", "title": "animate:"}
nav_next: {"path": "svelte/docs/svelte/class/index.md", "title": "class"}
---

The `style:` directive provides a shorthand for setting multiple styles on an element.

```
<!-- These are equivalent -->
<div style:color="red">...</div>
<div style="color: red;">...</div>
```

The value can contain arbitrary expressions:

```
<div style:color={myColor}>...</div>
```

The shorthand form is allowed:

```
<div style:color>...</div>
```

Multiple styles can be set on a single element:

```
<div style:color style:width="12rem" style:background-color={darkMode ? 'black' : 'white'}>...</div>
```

To mark a style as important, use the `|important` modifier:

```
<div style:color|important="red">...</div>
```

When `style:` directives are combined with `style` attributes, the directives will take precedence, even over `!important` properties:

```
<div style:color="red" style="color: blue">This will be red</div>
<div style:color="red" style="color: blue !important">This will still be red</div>
```

You can set CSS custom properties:

```
<div style:--columns={columns}>...</div>
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/03-template-syntax/17-style.md) [llms.txt](/docs/svelte/style/llms.txt)

previous next

[animate:](../animate/index.md) [class](../class/index.md)
