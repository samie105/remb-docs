---
title: "$$props and $$restProps"
source: "https://svelte.dev/docs/svelte/legacy-$$props-and-$$restProps"
canonical_url: "https://svelte.dev/docs/svelte/legacy-$$props-and-$$restProps"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:36.336Z"
content_hash: "b335bd33e802e693c12da866a8569834d334637f9a1a37936c429f0a91273467"
menu_path: ["$$props and $$restProps"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/legacy-export-let/index.md", "title": "export let"}
nav_next: {"path": "svelte/docs/svelte/legacy-on/index.md", "title": "on:"}
---

In runes mode, getting an object containing all the props that were passed in is easy, using the [`$props`]($props) rune.

In legacy mode, we use `$$props` and `$$restProps`:

*   `$$props` contains all the props that were passed in, including ones that are not individually declared with the `export` keyword
*   `$$restProps` contains all the props that were passed in _except_ the ones that were individually declared

For example, a `<Button>` component might need to pass along all its props to its own `<button>` element, except the `variant` prop:

```
<script>
	export let variant;
</script>

<button {...$$restProps} class="variant-{variant} {$$props.class ?? ''}">
	click me
</button>

<style>
	.variant-danger {
		background: red;
	}
</style>
```

In Svelte 3/4 using `$$props` and `$$restProps` creates a modest performance penalty, so they should only be used when needed.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/99-legacy/04-legacy-$$props-and-$$restProps.md) [llms.txt](/docs/svelte/legacy-$$props-and-$$restProps/llms.txt)

previous next

[export let](../legacy-export-let/index.md) [on:](../legacy-on/index.md)
