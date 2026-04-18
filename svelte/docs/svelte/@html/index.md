---
title: "{@html ...}"
source: "https://svelte.dev/docs/svelte/@html"
canonical_url: "https://svelte.dev/docs/svelte/@html"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:52.293Z"
content_hash: "12c326c4ef0683d083c71824580f1ab43304032c36c64f1c2ba8d0603580f3ef"
menu_path: ["{@html ...}"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/@render/index.md", "title": "{@render ...}"}
nav_next: {"path": "svelte/docs/svelte/@attach/index.md", "title": "{@attach ...}"}
---

To inject raw HTML into your component, use the `{@html ...}` tag:

```
<article>
	{@html content}
</article>
```

> Make sure that you either escape the passed string or only populate it with values that are under your control in order to prevent [XSS attacks](https://owasp.org/www-community/attacks/xss/). Never render unsanitized content.

The expression should be valid standalone HTML — this will not work, because `</div>` is not valid HTML:

```
{@html '<div>'}content{@html '</div>'}
```

It also will not compile Svelte code.

## Styling[](#Styling)

Content rendered this way is 'invisible' to Svelte and as such will not receive [scoped styles](scoped-styles). In other words, this will not work, and the `a` and `img` styles will be regarded as unused:

```
<article>
	{@html content}
</article>

<style>
	article {
		a { color: hotpink }
		img { width: 100% }
	}
</style>
```

Instead, use the `:global` modifier to target everything inside the `<article>`:

```
<style>
	article :global {
		a { color: hotpink }
		img { width: 100% }
	}
</style>
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/03-template-syntax/08-@html.md) [llms.txt](/docs/svelte/@html/llms.txt)

previous next

[{@render ...}](/docs/svelte/@render) [{@attach ...}](/docs/svelte/@attach)


