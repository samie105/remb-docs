---
title: "{#key ...}"
source: "https://svelte.dev/docs/svelte/key"
canonical_url: "https://svelte.dev/docs/svelte/key"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:33.555Z"
content_hash: "305386b6be469e0ec057336f55cc11c4525cb7af07b931f697a755c89aa4d607"
menu_path: ["{#key ...}"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/each/index.md", "title": "{#each ...}"}
nav_next: {"path": "svelte/docs/svelte/await/index.md", "title": "{#await ...}"}
---

```
{#key expression}...{/key}
```

Key blocks destroy and recreate their contents when the value of an expression changes. When used around components, this will cause them to be reinstantiated and reinitialised:

```
{#key value}
	<Component />
{/key}
```

It's also useful if you want a transition to play whenever a value changes:

```
{#key value}
	<div transition:fade>{value}</div>
{/key}
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/03-template-syntax/04-key.md) [llms.txt](/docs/svelte/key/llms.txt)

previous next

[{#each ...}](/docs/svelte/each) [{#await ...}](/docs/svelte/await)


