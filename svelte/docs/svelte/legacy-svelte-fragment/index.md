---
title: "<svelte:fragment>"
source: "https://svelte.dev/docs/svelte/legacy-svelte-fragment"
canonical_url: "https://svelte.dev/docs/svelte/legacy-svelte-fragment"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:18.060Z"
content_hash: "0a52d45f58eb91935bc8e5948fb305bcc5849f4ade167929a9c632a29040630d"
menu_path: ["<svelte:fragment>"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/legacy-$$slots/index.md", "title": "$$slots"}
nav_next: {"path": "svelte/docs/svelte/legacy-svelte-component/index.md", "title": "<svelte:component>"}
---

The `<svelte:fragment>` element allows you to place content in a [named slot](legacy-slots) without wrapping it in a container DOM element. This keeps the flow layout of your document intact.

Widget

```
<div>
	<slot name="header">No header was provided</slot>
	<p>Some content between header and footer</p>
	<slot name="footer" />
</div>
```

App

```
<script>
	import Widget from './Widget.svelte';
</script>

<Widget>
	<h1 slot="header">Hello</h1>
	<svelte:fragment slot="footer">
		<p>All rights reserved.</p>
		<p>Copyright (c) 2019 Svelte Industries</p>
	</svelte:fragment>
</Widget>
```

```
<script lang="ts">
	import Widget from './Widget.svelte';
</script>

<Widget>
	<h1 slot="header">Hello</h1>
	<svelte:fragment slot="footer">
		<p>All rights reserved.</p>
		<p>Copyright (c) 2019 Svelte Industries</p>
	</svelte:fragment>
</Widget>
```

> In Svelte 5+, this concept is obsolete, as snippets don't create a wrapping element

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/99-legacy/22-legacy-svelte-fragment.md) [llms.txt](/docs/svelte/legacy-svelte-fragment/llms.txt)

previous next

[$$slots](/docs/svelte/legacy-$$slots) [<svelte:component>](../legacy-svelte-component/index.md)
