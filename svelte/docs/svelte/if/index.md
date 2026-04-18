---
title: "{#if ...}"
source: "https://svelte.dev/docs/svelte/if"
canonical_url: "https://svelte.dev/docs/svelte/if"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:33.036Z"
content_hash: "730707bf29c7a72ec6ffb17221445f7c0169e86c32ac7052311f29b13a65aac7"
menu_path: ["{#if ...}"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/basic-markup/index.md", "title": "Basic markup"}
nav_next: {"path": "svelte/docs/svelte/each/index.md", "title": "{#each ...}"}
---

```
{#if expression}...{/if}
```

```
{#if expression}...{:else if expression}...{/if}
```

```
{#if expression}...{:else}...{/if}
```

Content that is conditionally rendered can be wrapped in an if block.

```
{#if answer === 42}
	<p>what was the question?</p>
{/if}
```

Additional conditions can be added with `{:else if expression}`, optionally ending in an `{:else}` clause.

```
{#if porridge.temperature > 100}
	<p>too hot!</p>
{:else if 80 > porridge.temperature}
	<p>too cold!</p>
{:else}
	<p>just right!</p>
{/if}
```

(Blocks don't have to wrap elements, they can also wrap text within elements.)

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/03-template-syntax/02-if.md) [llms.txt](/docs/svelte/if/llms.txt)

previous next

[Basic markup](/docs/svelte/basic-markup) [{#each ...}](/docs/svelte/each)

