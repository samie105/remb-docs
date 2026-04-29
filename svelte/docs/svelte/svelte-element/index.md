---
title: "<svelte:element>"
source: "https://svelte.dev/docs/svelte/svelte-element"
canonical_url: "https://svelte.dev/docs/svelte/svelte-element"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:11.460Z"
content_hash: "08d3f8b64d27badbd081fd22eddd7ba3ce62a6ac31767e2b22a730fff6b353a1"
menu_path: ["<svelte:element>"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/svelte-head/index.md", "title": "<svelte:head>"}
nav_next: {"path": "svelte/docs/svelte/svelte-options/index.md", "title": "<svelte:options>"}
---

```
<svelte:element this={expression} />
```

The `<svelte:element>` element lets you render an element that is unknown at author time, for example because it comes from a CMS. Any properties and event listeners present will be applied to the element.

The only supported binding is `bind:this`, since Svelte's built-in bindings do not work with generic elements.

If `this` has a nullish value, the element and its children will not be rendered.

If `this` is the name of a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element) (e.g., `br`) and `<svelte:element>` has child elements, a runtime error will be thrown in development mode:

```
<script>
	let tag = $state('hr');
</script>

<svelte:element this={tag}>
	This text cannot appear inside an hr element
</svelte:element>
```

Svelte tries its best to infer the correct namespace from the element's surroundings, but it's not always possible. You can make it explicit with an `xmlns` attribute:

```
<svelte:element this={tag} xmlns="http://www.w3.org/2000/svg" />
```

`this` needs to be a valid DOM element tag, things like `#text` or `svelte:head` will not work.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/05-special-elements/06-svelte-element.md) [llms.txt](/docs/svelte/svelte-element/llms.txt)

previous next

[<svelte:head>](../svelte-head/index.md) [<svelte:options>](../svelte-options/index.md)
