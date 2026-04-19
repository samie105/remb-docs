---
title: "{@const ...}"
source: "https://svelte.dev/docs/svelte/@const"
canonical_url: "https://svelte.dev/docs/svelte/@const"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:48.790Z"
content_hash: "830bf6ffb90a34bd5f6e183cc6da63ff3018e6934a7c02163edf053b5d527811"
menu_path: ["{@const ...}"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/@attach/index.md", "title": "{@attach ...}"}
nav_next: {"path": "svelte/docs/svelte/@debug/index.md", "title": "{@debug ...}"}
---

The `{@const ...}` tag defines a local constant.

```
{#each boxes as box}
	{@const area = box.width * box.height}
	{box.width} * {box.height} = {area}
{/each}
```

`{@const}` is only allowed as an immediate child of a block — `{#if ...}`, `{#each ...}`, `{#snippet ...}` and so on — a `<Component />` or a `<svelte:boundary>`.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/03-template-syntax/10-@const.md) [llms.txt](/docs/svelte/@const/llms.txt)

previous next

[{@attach ...}](/docs/svelte/@attach) [{@debug ...}](/docs/svelte/@debug)
