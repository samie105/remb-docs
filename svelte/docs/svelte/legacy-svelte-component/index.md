---
title: "<svelte:component>"
source: "https://svelte.dev/docs/svelte/legacy-svelte-component"
canonical_url: "https://svelte.dev/docs/svelte/legacy-svelte-component"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:25.895Z"
content_hash: "3030d41bb4f1561130bf12e54f9ac43603f8d1b8b3d9691b900da0ee4a0c40ed"
menu_path: ["<svelte:component>"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/legacy-svelte-fragment/index.md", "title": "<svelte:fragment>"}
nav_next: {"path": "svelte/docs/svelte/legacy-svelte-self/index.md", "title": "<svelte:self>"}
---

In runes mode, `<MyComponent>` will re-render if the value of `MyComponent` changes. See the [Svelte 5 migration guide](/docs/svelte/v5-migration-guide#svelte:component-is-no-longer-necessary) for an example.

In legacy mode, it won't — we must use `<svelte:component>`, which destroys and recreates the component instance when the value of its `this` expression changes:

```
<svelte:component this={MyComponent} />
```

If `this` is falsy, no component is rendered.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/99-legacy/30-legacy-svelte-component.md) [llms.txt](/docs/svelte/legacy-svelte-component/llms.txt)

previous next

[<svelte:fragment>](/docs/svelte/legacy-svelte-fragment) [<svelte:self>](/docs/svelte/legacy-svelte-self)

