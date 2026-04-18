---
title: "in: and out:"
source: "https://svelte.dev/docs/svelte/in-and-out"
canonical_url: "https://svelte.dev/docs/svelte/in-and-out"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:09.014Z"
content_hash: "1d4af99ed43638f1825a99e289e28d0bedef71df95e9e4c55b638ba297dfcc2d"
menu_path: ["in: and out:"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/transition/index.md", "title": "transition:"}
nav_next: {"path": "svelte/docs/svelte/animate/index.md", "title": "animate:"}
---

The `in:` and `out:` directives are identical to [`transition:`](transition), except that the resulting transitions are not bidirectional — an `in` transition will continue to 'play' alongside the `out` transition, rather than reversing, if the block is outroed while the transition is in progress. If an out transition is aborted, transitions will restart from scratch.

```
<script>
  import { fade, fly } from 'svelte/transition';

  let visible = $state(false);
</script>

<label>
  <input type="checkbox" bind:checked={visible}>
  visible
</label>

{#if visible}
	<div in:fly={{ y: 200 }} out:fade>flies in, fades out</div>
{/if}
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/03-template-syntax/15-in-and-out.md) [llms.txt](/docs/svelte/in-and-out/llms.txt)

previous next

[transition:](/docs/svelte/transition) [animate:](/docs/svelte/animate)

