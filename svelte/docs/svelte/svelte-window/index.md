---
title: "<svelte:window>"
source: "https://svelte.dev/docs/svelte/svelte-window"
canonical_url: "https://svelte.dev/docs/svelte/svelte-window"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:07.089Z"
content_hash: "8ac320b3517c77cb8b307e09e9eaf9933aeed53a27df4be22f64d66c652deba9"
menu_path: ["<svelte:window>"]
section_path: []
nav_prev: {"path": "../svelte-boundary/index.md", "title": "<svelte:boundary>"}
nav_next: {"path": "../svelte-document/index.md", "title": "<svelte:document>"}
---

```
<svelte:window onevent={handler} />
```

```
<svelte:window bind:prop={value} />
```

The `<svelte:window>` element allows you to add event listeners to the `window` object without worrying about removing them when the component is destroyed, or checking for the existence of `window` when server-side rendering.

This element may only appear at the top level of your component — it cannot be inside a block or element.

```
<script>
	function handleKeydown(event) {
		alert(`pressed the ${event.key} key`);
	}
</script>

<svelte:window onkeydown={handleKeydown} />
```

You can also bind to the following properties:

*   `innerWidth`
*   `innerHeight`
*   `outerWidth`
*   `outerHeight`
*   `scrollX`
*   `scrollY`
*   `online` — an alias for `window.navigator.onLine`
*   `devicePixelRatio`

All except `scrollX` and `scrollY` are readonly.

```
<svelte:window bind:scrollY={y} />
```

> Note that the page will not be scrolled to the initial value to avoid accessibility issues. Only subsequent changes to the bound variable of `scrollX` and `scrollY` will cause scrolling. If you have a legitimate reason to scroll when the component is rendered, call `scrollTo()` in an `$effect`.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/05-special-elements/02-svelte-window.md) [llms.txt](/docs/svelte/svelte-window/llms.txt)

previous next

[<svelte:boundary>](/docs/svelte/svelte-boundary) [<svelte:document>](/docs/svelte/svelte-document)
