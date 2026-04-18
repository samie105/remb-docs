---
title: "$$slots"
source: "https://svelte.dev/docs/svelte/legacy-$$slots"
canonical_url: "https://svelte.dev/docs/svelte/legacy-$$slots"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:11.280Z"
content_hash: "dadd625910134d0450fd19f055c202e0335842db1061d5798059d4ce7ad83691"
menu_path: ["$$slots"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/legacy-slots/index.md", "title": "<slot>"}
nav_next: {"path": "svelte/docs/svelte/legacy-svelte-fragment/index.md", "title": "<svelte:fragment>"}
---

In runes mode, we know which [snippets](snippet) were provided to a component, as they're just normal props.

In legacy mode, the way to know if content was provided for a given slot is with the `$$slots` object, whose keys are the names of the slots passed into the component by the parent.

Card

```
<div>
	<slot name="title" />
	{#if $$slots.description}
		<!-- This <hr> and slot will render only if `slot="description"` is provided. -->
		<hr />
		<slot name="description" />
	{/if}
</div>
```

App

```
<Card>
	<h1 slot="title">Blog Post Title</h1>
	<!-- No slot named "description" was provided so the optional slot will not be rendered. -->
</Card>
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/99-legacy/21-legacy-$$slots.md) [llms.txt](/docs/svelte/legacy-$$slots/llms.txt)

previous next

[<slot>](/docs/svelte/legacy-slots) [<svelte:fragment>](/docs/svelte/legacy-svelte-fragment)
