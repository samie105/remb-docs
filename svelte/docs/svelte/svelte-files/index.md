---
title: ".svelte files"
source: "https://svelte.dev/docs/svelte/svelte-files"
canonical_url: "https://svelte.dev/docs/svelte/svelte-files"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:48.540Z"
content_hash: "9f31fd2e739ed40469a826e4fd33b14acf18b3fc1dbd384d7b6334381af9acf1"
menu_path: [".svelte files"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/getting-started/index.md", "title": "Getting started"}
nav_next: {"path": "svelte/docs/svelte/svelte-js-files/index.md", "title": ".svelte.js and .svelte.ts files"}
---

Components are the building blocks of Svelte applications. They are written into `.svelte` files, using a superset of HTML.

All three sections — script, styles and markup — are optional.

MyComponent

```
<script module>
	// module-level logic goes here
	// (you will rarely use this)
</script>

<script>
	// instance-level logic goes here
</script>

<!-- markup (zero or more items) goes here -->

<style>
	/* styles go here */
</style>
```

```
<script module>
	// module-level logic goes here
	// (you will rarely use this)
</script>

<script lang="ts">
	// instance-level logic goes here
</script>

<!-- markup (zero or more items) goes here -->

<style>
	/* styles go here */
</style>
```

## <script>[](#script)

A `<script>` block contains JavaScript (or TypeScript, when adding the `lang="ts"` attribute) that runs when a component instance is created. Variables declared (or imported) at the top level can be referenced in the component's markup.

In addition to normal JavaScript, you can use _runes_ to declare [component props]($props) and add reactivity to your component. Runes are covered in the next section.

## <script module>[](#script-module)

A `<script>` tag with a `module` attribute runs once when the module first evaluates, rather than for each component instance. Variables declared in this block can be referenced elsewhere in the component, but not vice versa.

```
<script module>
	let total = 0;
</script>

<script>
	total += 1;
	console.log(`instantiated ${total} times`);
</script>
```

You can `export` bindings from this block, and they will become exports of the compiled module. You cannot `export default`, since the default export is the component itself.

> If you are using TypeScript and import such exports from a `module` block into a `.ts` file, make sure to have your editor setup so that TypeScript knows about them. This is the case for our VS Code extension and the IntelliJ plugin, but in other cases you might need to setup our [TypeScript editor plugin](https://www.npmjs.com/package/typescript-svelte-plugin).

> Legacy mode
> 
> In Svelte 4, this script tag was created using `<script context="module">`

## <style>[](#style)

CSS inside a `<style>` block will be scoped to that component.

```
<style>
	p {
		/* this will only affect <p> elements in this component */
		color: burlywood;
	}
</style>
```

For more information, head to the section on [styling](scoped-styles).

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/01-introduction/03-svelte-files.md) [llms.txt](/docs/svelte/svelte-files/llms.txt)

previous next

[Getting started](../getting-started/index.md) [.svelte.js and .svelte.ts files](../svelte-js-files/index.md)
