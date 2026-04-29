---
title: "<svelte:body>"
source: "https://svelte.dev/docs/svelte/svelte-body"
canonical_url: "https://svelte.dev/docs/svelte/svelte-body"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:35.021Z"
content_hash: "12a52267ee7dbd5240a681ef61f6ea0b33d7bf8f709e5be0bc463ae6dc311d87"
menu_path: ["<svelte:body>"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/svelte-document/index.md", "title": "<svelte:document>"}
nav_next: {"path": "svelte/docs/svelte/svelte-head/index.md", "title": "<svelte:head>"}
---

```
<svelte:body onevent={handler} />
```

Similarly to `<svelte:window>`, this element allows you to add listeners to events on `document.body`, such as `mouseenter` and `mouseleave`, which don't fire on `window`. It also lets you use [actions](use) on the `<body>` element.

As with `<svelte:window>` and `<svelte:document>`, this element may only appear at the top level of your component and must never be inside a block or element.

```
<svelte:body onmouseenter={handleMouseenter} onmouseleave={handleMouseleave} use:someAction />
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/05-special-elements/04-svelte-body.md) [llms.txt](/docs/svelte/svelte-body/llms.txt)

previous next

[<svelte:document>](../svelte-document/index.md) [<svelte:head>](../svelte-head/index.md)
