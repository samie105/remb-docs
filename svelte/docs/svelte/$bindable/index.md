---
title: "$bindable"
source: "https://svelte.dev/docs/svelte/$bindable"
canonical_url: "https://svelte.dev/docs/svelte/$bindable"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:17.118Z"
content_hash: "b1d486e8885eb422f60dc0491a2be21c1843554c0c701e542caa2c5a7068d1ad"
menu_path: ["$bindable"]
section_path: []
---
Ordinarily, props go one way, from parent to child. This makes it easy to understand how data flows around your app.

In Svelte, component props can be _bound_, which means that data can also flow _up_ from child to parent. This isn't something you should do often — overuse can make your data flow unpredictable and your components harder to maintain — but it can simplify your code if used sparingly and carefully.

It also means that a state proxy can be _mutated_ in the child.

> Mutation is also possible with normal props, but is strongly discouraged — Svelte will warn you if it detects that a component is mutating state it does not 'own'.

To mark a prop as bindable, we use the `$bindable` rune:

FancyInput

```
<script>
	let { value = $bindable(), ...props } = $props();
</script>

<input bind:value={value} {...props} />

<style>
	input {
		font-family: 'Comic Sans MS';
		color: deeppink;
	}
</style>
```

```
<script lang="ts">
	let { value = $bindable(), ...props } = $props();
</script>

<input bind:value={value} {...props} />

<style>
	input {
		font-family: 'Comic Sans MS';
		color: deeppink;
	}
</style>
```

Now, a component that uses `<FancyInput>` can add the [`bind:`](bind) directive ([demo](/playground/untitled#H4sIAAAAAAAAE3WQwWrDMBBEf2URBSfg2nfFMZRCoYeecqx6UJx1IyqvhLUONcb_XqSkTUOSk1az7DBvJtEai0HI90nw6FHIJIhckO7i78n7IhzQctS2OuAtvXHESByEFFVoeuO5VqTYdN71DC-amvGV_MDQ9q6DrCjP0skkWymKJxYZOgxBfyKs4SGwZlxke7TWZcuVoqo8-1P1z3lraCcP2g64nk4GM5S1osrXf0JV-lrkgvGbheR-wDm_g30V8JL-1vpOCZFogpQsEsWcemtxscyhKArfOx9gjps0Lq4hzRVfemaYfu-PoIqqwKPFY_XpaIqj4tYRP7a6M3aUkD27zjSw0RTgbZN6Z8WNs66XsEP03tBXUueUJFlelvYx_wCuI3leNwIAAA==)):

App

```
<script>
	import FancyInput from './FancyInput.svelte';

	let message = $state('hello');
</script>

<FancyInput bind:value={message} />
<p>{message}</p>
```

```
<script lang="ts">
	import FancyInput from './FancyInput.svelte';

	let message = $state('hello');
</script>

<FancyInput bind:value={message} />
<p>{message}</p>
```

The parent component doesn't _have_ to use `bind:` — it can just pass a normal prop. Some parents don't want to listen to what their children have to say.

In this case, you can specify a fallback value for when no prop is passed at all:

FancyInput

```
let { let value: anyvalue = function $bindable<"fallback">(fallback?: "fallback" | undefined): "fallback"
namespace $bindableDeclares a prop as bindable, meaning the parent component can use bind:propName={value} to bind to it.
let { propName = $bindable() }: { propName: boolean } = $props();@see{@link https://svelte.dev/docs/svelte/$bindable Documentation}$bindable('fallback'), ...let props: anyprops } = function $props(): any
namespace $propsDeclares the props that a component accepts. Example:
let { optionalProp = 42, requiredProp, bindableProp = $bindable() }: { optionalProp?: number; requiredProps: string; bindableProp: boolean } = $props();@see{@link https://svelte.dev/docs/svelte/$props Documentation}$props();
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/02-runes/06-$bindable.md) [llms.txt](/docs/svelte/$bindable/llms.txt)

previous next

[$props](/docs/svelte/$props) [$inspect](/docs/svelte/$inspect)
