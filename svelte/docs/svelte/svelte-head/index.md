---
title: "<svelte:head>"
source: "https://svelte.dev/docs/svelte/svelte-head"
canonical_url: "https://svelte.dev/docs/svelte/svelte-head"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:41.248Z"
content_hash: "12866bbc2ca38f102b2597a8eb6e9fb7ff239632b4045968da01378dfc9ce136"
menu_path: ["<svelte:head>"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/svelte-body/index.md", "title": "<svelte:body>"}
nav_next: {"path": "svelte/docs/svelte/svelte-element/index.md", "title": "<svelte:element>"}
---

```
<svelte:head>...</svelte:head>
```

This element makes it possible to insert elements into `document.head`. During server-side rendering, `head` content is exposed separately to the main `body` content.

As with `<svelte:window>`, `<svelte:document>` and `<svelte:body>`, this element may only appear at the top level of your component and must never be inside a block or element.

```
<svelte:head>
	<title>Hello world!</title>
	<meta name="description" content="This is where the description goes for SEO" />
</svelte:head>
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/05-special-elements/05-svelte-head.md) [llms.txt](/docs/svelte/svelte-head/llms.txt)

previous next

[<svelte:body>](/docs/svelte/svelte-body) [<svelte:element>](/docs/svelte/svelte-element)


