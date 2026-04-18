---
title: "$props"
source: "https://svelte.dev/docs/svelte/$props"
canonical_url: "https://svelte.dev/docs/svelte/$props"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:17.529Z"
content_hash: "4be339cc4d5829dc3be1b4e9e436dd26cbf499f434d7ea9a2972779cbc24d543"
menu_path: ["$props"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/$effect/index.md", "title": "$effect"}
nav_next: {"path": "svelte/docs/svelte/$bindable/index.md", "title": "$bindable"}
---

The inputs to a component are referred to as _props_, which is short for _properties_. You pass props to components just like you pass attributes to elements:

App

```
<script>
	import MyComponent from './MyComponent.svelte';
</script>

<MyComponent adjective="cool" />
```

```
<script lang="ts">
	import MyComponent from './MyComponent.svelte';
</script>

<MyComponent adjective="cool" />
```

On the other side, inside `MyComponent.svelte`, we can receive props with the `$props` rune...

MyComponent

```
<script>
	let props = $props();
</script>

<p>this component is {props.adjective}</p>
```

```
<script lang="ts">
	let props = $props();
</script>

<p>this component is {props.adjective}</p>
```

...though more commonly, you'll [_destructure_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) your props:

MyComponent

```
<script>
	let { adjective } = $props();
</script>

<p>this component is {adjective}</p>
```

```
<script lang="ts">
	let { adjective } = $props();
</script>

<p>this component is {adjective}</p>
```

## Fallback values[](#Fallback-values)

Destructuring allows us to declare fallback values, which are used if the parent component does not set a given prop (or the value is `undefined`):

```
let { let adjective: anyadjective = 'happy' } = function $props(): any
namespace $propsDeclares the props that a component accepts. Example:
let { optionalProp = 42, requiredProp, bindableProp = $bindable() }: { optionalProp?: number; requiredProps: string; bindableProp: boolean } = $props();@see{@link https://svelte.dev/docs/svelte/$props Documentation}$props();
```

> Fallback values are not turned into reactive state proxies (see [Updating props](#Updating-props) for more info)

## Renaming props[](#Renaming-props)

We can also use the destructuring assignment to rename props, which is necessary if they're invalid identifiers, or a JavaScript keyword like `super`:

```
let { super: let trouper: anytrouper = 'lights are gonna find me' } = function $props(): any
namespace $propsDeclares the props that a component accepts. Example:
let { optionalProp = 42, requiredProp, bindableProp = $bindable() }: { optionalProp?: number; requiredProps: string; bindableProp: boolean } = $props();@see{@link https://svelte.dev/docs/svelte/$props Documentation}$props();
```

## Rest props[](#Rest-props)

Finally, we can use a _rest property_ to get, well, the rest of the props:

```
let { let a: anya, let b: anyb, let c: anyc, ...let others: anyothers } = function $props(): any
namespace $propsDeclares the props that a component accepts. Example:
let { optionalProp = 42, requiredProp, bindableProp = $bindable() }: { optionalProp?: number; requiredProps: string; bindableProp: boolean } = $props();@see{@link https://svelte.dev/docs/svelte/$props Documentation}$props();
```

## Updating props[](#Updating-props)

References to a prop inside a component update when the prop itself updates — when `count` changes in `App.svelte`, it will also change inside `Child.svelte`. But the child component is able to temporarily override the prop value, which can be useful for unsaved ephemeral state:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA6WQQU-EQAyF_0rTmCxEsuiVBRLjX_AmHmah6MShM5kp6obw380AyarZPXlsXt9rvzchq4GwwCcanPXKa3OC0XVKNL-C89YFzLDXhgIWzxMeVaDN8eDcPnyQEcIMW8tCLAELLEPrtZO64UZ0DBV4fNOmg97bAXb7fJk26-7QcFw0JNDakQUquAmihJK79NBwmZ_TuDyOIpbBcmt0-15NSQpVDclqvK3gPp2Xs4scIHHKE0tawLSszDFvzVjz1r82EfIaM7wEJ_QlWIgfKUM5uajHRnDOfhXyk-t6JZF02ljnSLuUnPwfto3nL7Kesf68eBXsJUNR2nxq7rDolQk0fwNciJZcKgIAAA)

```
<script>
	import Child from './Child.svelte';

	let count = $state(0);
</script>

<button onclick={() => (count += 1)}>
	clicks (parent): {count}
</button>

<Child {count} />
```

```
<script lang="ts">
	import Child from './Child.svelte';

	let count = $state(0);
</script>

<button onclick={() => (count += 1)}>
	clicks (parent): {count}
</button>

<Child {count} />
```

```
<script>
	let { count } = $props();
</script>

<button onclick={() => (count += 1)}>
	clicks (child): {count}
</button>
```

```
<script lang="ts">
	let { count } = $props();
</script>

<button onclick={() => (count += 1)}>
	clicks (child): {count}
</button>
```

While you can temporarily _reassign_ props, you should not _mutate_ props unless they are [bindable]($bindable).

If the prop is a regular object, the mutation will have no effect:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA3WQzU7DMBCEX2W1QmorQgJXk0RC3HkBwiFxN6rBWVvxpoAsvztKWonw0-N6Z3a-cURuB0KFT45vRmq1mCOBH50PmGFvLAVUzxG7NtBZ-eB9Ho5khTBD7ViIJaDCMujReKkbbsQM3o0Cjwdj99CPboBNXizT2bq5b7gsvh1cnrSueyUtVYyg3cSi4BZSgqLGDP-LF_oQVDJOlKF8-nk_M2PKfiCvky9DWxKIZwJIUMHV8g_b3R_WbhJxDI61NfqtitsdVDXE-UhRwKENwA6o70nL_HY6mS-N4LqCu4ZTWiIXf1AQ15I0x50iVr1_dbjY_CVDaY19N7xH1bc2UPoCtLcdIuUBAAA)

```
<script>
	import Child from './Child.svelte';
</script>

<Child object={{ count: 0 }} />
```

```
<script lang="ts">
	import Child from './Child.svelte';
</script>

<Child object={{ count: 0 }} />
```

```
<script>
	let { object } = $props();
</script>

<button onclick={() => {
	// has no effect
	object.count += 1
}}>
	clicks: {object.count}
</button>
```

```
<script lang="ts">
	let { object } = $props();
</script>

<button onclick={() => {
	// has no effect
	object.count += 1
}}>
	clicks: {object.count}
</button>
```

If the prop is a reactive state proxy, however, then mutations _will_ have an effect but you will see an [`ownership_invalid_mutation`](runtime-warnings#Client-warnings-ownership_invalid_mutation) warning, because the component is mutating state that does not 'belong' to it:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA3WRzU7DMBCEX2VZIbWIqIFr2lRCcOEZCAcn2VKDs47idUMV-d1R4lSUnx6tmV1_Mzsgq4Yww2c-KKNraLwo0ZYxwZ025DB7GbBUjmbfQ9uu3IGMECZYWRZicZjhxlWdbmVbcCG6aW0n8LjXpoZdZxtYrNLpNY8u1gWPRkMCtnynSiCHaydKaDlU1rNkcBdu1gVv0u-9vIkbhzgSIN1igv9xCX0KZtJ5SlCO7aiPYTAkP7KcI11OM0IOJ8wwgradbd3yL17pRSyD5cro6iMfljeQb2EYl6Qp9NoYqJR3BLInmGJCScb2IBZ8WyuhZPaWXqDXsgcFvepY89sKniwvJN6HZluEcnC0HupJtj1fjWJUVvGT2xzuCw5hijOxuezUYrSEMUrEP-v0Vz8XW31NUJQ2veYas50yjsIXg_8-OVgCAAA)

```
<script>
	import Child from './Child.svelte';

	let object = $state({count: 0});
</script>

<Child {object} />
```

```
<script lang="ts">
	import Child from './Child.svelte';

	let object = $state({count: 0});
</script>

<Child {object} />
```

```
<script>
	let { object } = $props();
</script>

<button onclick={() => {
	// will cause the count below to update,
	// but with a warning. Don't mutate
	// objects you don't own!
	object.count += 1
}}>
	clicks: {object.count}
</button>
```

```
<script lang="ts">
	let { object } = $props();
</script>

<button onclick={() => {
	// will cause the count below to update,
	// but with a warning. Don't mutate
	// objects you don't own!
	object.count += 1
}}>
	clicks: {object.count}
</button>
```

The fallback value of a prop not declared with `$bindable` is left untouched — it is not turned into a reactive state proxy — meaning mutations will not cause updates:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA3WQ3U7DMAyFX8WykLaJssJtWCch7nkBykWaOVpY5kSNO0BR3h21m0T5u7Tsc87nk5H1kVDhU-CbnrQRdyKw2vtOmwPEPsSEFVrnKaF6ztjpRBfJQ4zrdCIvhBWawEIsCRVukuldlG3LrbhjDL3A4975Hdg-HGGxrqfpIl3ct7ypvxS8Od_WW6zwryChd0El_UAVykcc9yMdluob3DzjfzxPAhlC90pGoIEMJgwsCm6hQIEGrqYClqtfkN0gEhgCG-_MocnLFTRbyKNnXcNeJ-AAZO3o6yzIflbqSfuBwCUYEu1GxTl_PWXDdQN3LZcy8U3uSUGen5QR5gwwK-nHw__W9FKhaOffHO9QWe0TlU9fV1N9BQIAAA)

```
<script>
	import Child from './Child.svelte';
</script>

<Child />
```

```
<script lang="ts">
	import Child from './Child.svelte';
</script>

<Child />
```

```
<script>
	let { object = { count: 0 } } = $props();
</script>

<button onclick={() => {
	// has no effect if the fallback value is used
	object.count += 1
}}>
	clicks: {object.count}
</button>
```

```
<script lang="ts">
	let { object = { count: 0 } } = $props();
</script>

<button onclick={() => {
	// has no effect if the fallback value is used
	object.count += 1
}}>
	clicks: {object.count}
</button>
```

In summary: don't mutate props. Either use callback props to communicate changes, or — if parent and child should share the same object — use the [`$bindable`]($bindable) rune.

## Type safety[](#Type-safety)

You can add type safety to your components by annotating your props, as you would with any other variable declaration. In TypeScript that might look like this...

```
<script lang="ts">
	let { adjective }: { adjective: string } = $props();
</script>
```

...while in JSDoc you can do this:

```
<script>
	/** @type {{ adjective: string }} */
	let { adjective } = $props();
</script>
```

You can, of course, separate the type declaration from the annotation:

```
<script lang="ts">
	interface Props {
		adjective: string;
	}

	let { adjective }: Props = $props();
</script>
```

> Interfaces for native DOM elements are provided in the `svelte/elements` module (see [Typing wrapper components](typescript#Typing-wrapper-components))

If your component exposes [snippet](snippet) props like `children`, these should be typed using the `Snippet` interface imported from `'svelte'` — see [Typing snippets](snippet#Typing-snippets) for examples.

Adding types is recommended, as it ensures that people using your component can easily discover which props they should provide.

## $props.id()[](#$props.id\(\))

This rune, added in version 5.20.0, generates an ID that is unique to the current component instance. When hydrating a server-rendered component, the value will be consistent between server and client.

This is useful for linking elements via attributes like `for` and `aria-labelledby`.

```
<script>
	const uid = $props.id();
</script>

<form>
	<label for="{uid}-firstname">First Name: </label>
	<input id="{uid}-firstname" type="text" />

	<label for="{uid}-lastname">Last Name: </label>
	<input id="{uid}-lastname" type="text" />
</form>
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/02-runes/05-$props.md) [llms.txt](/docs/svelte/$props/llms.txt)

previous next

[$effect](/docs/svelte/$effect) [$bindable](/docs/svelte/$bindable)

