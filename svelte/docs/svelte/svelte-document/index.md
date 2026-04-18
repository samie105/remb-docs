---
title: "<svelte:document>"
source: "https://svelte.dev/docs/svelte/svelte-document"
canonical_url: "https://svelte.dev/docs/svelte/svelte-document"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:34.357Z"
content_hash: "7fdca52a51c269a6dd037f119326eff89262c460c95f5e1fbc42cf4ceec61567"
menu_path: ["<svelte:document>"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/svelte-window/index.md", "title": "<svelte:window>"}
nav_next: {"path": "svelte/docs/svelte/svelte-body/index.md", "title": "<svelte:body>"}
---

```
<svelte:document onevent={handler} />
```

```
<svelte:document bind:prop={value} />
```

Similarly to `<svelte:window>`, this element allows you to add listeners to events on `document`, such as `visibilitychange`, which don't fire on `window`. It also lets you use [attachments](@attach) on `document`.

As with `<svelte:window>`, this element may only appear the top level of your component and must never be inside a block or element.

```
<svelte:document onvisibilitychange={handleVisibilityChange} {@attach someAttachment} />
```

You can also bind to the following properties:

*   `activeElement`
*   `fullscreenElement`
*   `pointerLockElement`
*   `visibilityState`

All are readonly.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/05-special-elements/03-svelte-document.md) [llms.txt](/docs/svelte/svelte-document/llms.txt)

previous next

[<svelte:window>](/docs/svelte/svelte-window) [<svelte:body>](/docs/svelte/svelte-body)

