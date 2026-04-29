---
title: "<slot>"
source: "https://svelte.dev/docs/svelte/legacy-slots"
canonical_url: "https://svelte.dev/docs/svelte/legacy-slots"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:51.848Z"
content_hash: "c698e5cc9164fdc65b8f18e6ea7a07b640e7f91cd5b89c84f09398b0f9149810"
menu_path: ["<slot>"]
section_path: []
nav_prev: {"path": "../legacy-on/index.md", "title": "on:"}
nav_next: {"path": "../legacy-$$slots/index.md", "title": "$$slots"}
---

In Svelte 5, content can be passed to components in the form of [snippets](snippet) and rendered using [render tags](@render).

In legacy mode, content inside component tags is considered _slotted content_, which can be rendered by the component using a `<slot>` element:

App

```
<script>
	import Modal from './Modal.svelte';
</script>

<Modal>This is some slotted content</Modal>
```

```
<script lang="ts">
	import Modal from './Modal.svelte';
</script>

<Modal>This is some slotted content</Modal>
```

Modal

```
<div class="modal">
	<slot></slot>
</div>
```

> If you want to render a regular `<slot>` element, you can use `<svelte:element this={'slot'} />`.

## Named slots[](#Named-slots)

A component can have _named_ slots in addition to the default slot. On the parent side, add a `slot="..."` attribute to an element, component or [`<svelte:fragment>`](legacy-svelte-fragment) directly inside the component tags.

App

```
<script>
	import Modal from './Modal.svelte';

	let open = true;
</script>

{#if open}
	<Modal>
		This is some slotted content

		<div slot="buttons">
			<button on:click={() => open = false}>
				close
			</button>
		</div>
	</Modal>
{/if}
```

```
<script lang="ts">
	import Modal from './Modal.svelte';

	let open = true;
</script>

{#if open}
	<Modal>
		This is some slotted content

		<div slot="buttons">
			<button on:click={() => open = false}>
				close
			</button>
		</div>
	</Modal>
{/if}
```

On the child side, add a corresponding `<slot name="...">` element:

Modal

```
<div class="modal">
	<slot></slot>
	<hr>
	<slot name="buttons"></slot>
</div>
```

## Fallback content[](#Fallback-content)

If no slotted content is provided, a component can define fallback content by putting it inside the `<slot>` element:

```
<slot>
	This will be rendered if no slotted content is provided
</slot>
```

## Passing data to slotted content[](#Passing-data-to-slotted-content)

Slots can be rendered zero or more times and can pass values _back_ to the parent using props. The parent exposes the values to the slot template using the `let:` directive.

FancyList

```
<ul>
	{#each items as data}
		<li class="fancy">
			<!-- 'item' here... -->
			<slot item={process(data)} />
		</li>
	{/each}
</ul>
```

App

```
<!-- ...corresponds to 'item' here: -->
<FancyList {items} let:item={processed}>
	<div>{processed.text}</div>
</FancyList>
```

The usual shorthand rules apply — `let:item` is equivalent to `let:item={item}`, and `<slot {item}>` is equivalent to `<slot item={item}>`.

Named slots can also expose values. The `let:` directive goes on the element with the `slot` attribute.

FancyList

```
<ul>
	{#each items as item}
		<li class="fancy">
			<slot name="item" item={process(data)} />
		</li>
	{/each}
</ul>

<slot name="footer" />
```

App

```
<FancyList {items}>
	<div slot="item" let:item>{item.text}</div>
	<p slot="footer">Copyright (c) 2019 Svelte Industries</p>
</FancyList>
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/99-legacy/20-legacy-slots.md) [llms.txt](/docs/svelte/legacy-slots/llms.txt)

previous next

[on:](/docs/svelte/legacy-on) [$$slots](/docs/svelte/legacy-$$slots)
