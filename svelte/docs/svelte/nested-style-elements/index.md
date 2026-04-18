---
title: "Nested <style> elements"
source: "https://svelte.dev/docs/svelte/nested-style-elements"
canonical_url: "https://svelte.dev/docs/svelte/nested-style-elements"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:55.581Z"
content_hash: "af8655887ea6480aceb865fe655ccd2bc21b345e263cf57d106a5fe458cb2ebd"
menu_path: ["Nested <style> elements"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/custom-properties/index.md", "title": "Custom properties"}
nav_next: {"path": "svelte/docs/svelte/svelte-boundary/index.md", "title": "<svelte:boundary>"}
---

There can only be one top-level `<style>` tag per component.

However, it is possible to have a `<style>` tag nested inside other elements or logic blocks.

In that case, the `<style>` tag will be inserted as-is into the DOM; no scoping or processing will be done on the `<style>` tag.

```
<div>
	<style>
		/* this style tag will be inserted as-is */
		div {
			/* this will apply to all `<div>` elements in the DOM */
			color: red;
		}
	</style>
</div>
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/04-styling/04-nested-style-elements.md) [llms.txt](/docs/svelte/nested-style-elements/llms.txt)

previous next

[Custom properties](/docs/svelte/custom-properties) [<svelte:boundary>](/docs/svelte/svelte-boundary)
