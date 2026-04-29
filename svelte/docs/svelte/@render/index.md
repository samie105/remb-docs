---
title: "{@render ...}"
source: "https://svelte.dev/docs/svelte/@render"
canonical_url: "https://svelte.dev/docs/svelte/@render"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:09.892Z"
content_hash: "921f2b56608f3dbe0337cb6e84ca3d6445e3b477be3a0b54ea3d80e6b0ed3134"
menu_path: ["{@render ...}"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/snippet/index.md", "title": "{#snippet ...}"}
nav_next: {"path": "svelte/docs/svelte/@html/index.md", "title": "{@html ...}"}
---

To render a [snippet](snippet), use a `{@render ...}` tag.

```
{#snippet sum(a, b)}
	<p>{a} + {b} = {a + b}</p>
{/snippet}

{@render sum(1, 2)}
{@render sum(3, 4)}
{@render sum(5, 6)}
```

The expression can be an identifier like `sum`, or an arbitrary JavaScript expression:

```
{@render (cool ? coolSnippet : lameSnippet)()}
```

## Optional snippets[](#Optional-snippets)

If the snippet is potentially undefined — for example, because it's an incoming prop — then you can use optional chaining to only render it when it _is_ defined:

```
{@render children?.()}
```

Alternatively, use an [`{#if ...}`](if) block with an `:else` clause to render fallback content:

```
{#if children}
	{@render children()}
{:else}
	<p>fallback content</p>
{/if}
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/03-template-syntax/07-@render.md) [llms.txt](/docs/svelte/@render/llms.txt)

previous next

[{#snippet ...}](../snippet/index.md) [{@html ...}](/docs/svelte/@html)
