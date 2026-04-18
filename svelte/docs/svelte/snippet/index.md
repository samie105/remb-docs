---
title: "{#snippet ...}"
source: "https://svelte.dev/docs/svelte/snippet"
canonical_url: "https://svelte.dev/docs/svelte/snippet"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:14.185Z"
content_hash: "1e1ea9ce8bb7fe39ca919b8ca3153b13b55ad03f7f1a178174cadde7d4b7cfc1"
menu_path: ["{#snippet ...}"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/await/index.md", "title": "{#await ...}"}
nav_next: {"path": "svelte/docs/svelte/@render/index.md", "title": "{@render ...}"}
---

```
{#snippet name()}...{/snippet}
```

```
{#snippet name(param1, param2, paramN)}...{/snippet}
```

Snippets, and [render tags](@render), are a way to create reusable chunks of markup inside your components. Instead of writing duplicative code like [this](/playground/untitled#H4sIAAAAAAAAE5VUYW-kIBD9K8Tmsm2yXXRzvQ-s3eR-R-0HqqOQKhAZb9sz_vdDkV1t000vRmHewMx7w2AflbIGG7GnPlK8gYhFv42JthG-m9Gwf6BGcLbVXZuPSGrzVho8ZirDGpDIhldgySN5GpEMez9kaNuckY1ANJZRamRuu2ZnhEZt6a84pvs43mzD4pMsUDDi8DMkQFYCGdkvsJwblFq5uCik9bmJ4JZwUkv1eoknWigX2eGNN6aGXa6bjV8ybP-X7sM36T58SVcrIIV2xVIaA41xeD5kKqWXuqpUJEefOqVuOkL9DfBchGrzWfu0vb-RpTd3o-zBR045Ga3HfuE5BmJpKauuhbPtENlUF2sqR9jqpsPSxWsMrlngyj3VJiyYjJXb1-lMa7IWC-iSk2M5Zzh-SJjShe-siq5kpZRPs55BbSGU5YPyte4vVV_VfFXxVb10dSLf17pS2lM5HnpPxw4Zpv6x-F57p0jI3OKlVnhv5V9wPQrNYQQ9D_f6aGHlC89fq1Z3qmDkJCTCweOGF4VUFSPJvD_DhreVdA0eu8ehJJ5x91dBaBkpWm3ureCFPt3uzRv56d4kdp-2euG38XZ6dsnd3ZmPG9yRBCrzRUvi-MccOdwz3qE-fOZ7AwAhlrtTUx3c76vRhSwlFBHDtoPhefgHX3dM0PkEAAA=)...

```
{#each images as image}
	{#if image.href}
		<a href={image.href}>
			<figure>
				<img src={image.src} alt={image.caption} width={image.width} height={image.height} />
				<figcaption>{image.caption}</figcaption>
			</figure>
		</a>
	{:else}
		<figure>
			<img src={image.src} alt={image.caption} width={image.width} height={image.height} />
			<figcaption>{image.caption}</figcaption>
		</figure>
	{/if}
{/each}
```

...you can write [this](/playground/untitled#H4sIAAAAAAAAE5VUYW-bMBD9KxbRlERKY4jWfSA02n5H6QcXDmwVbMs-lnaI_z6D7TTt1moTAnPvzvfenQ_GpBEd2CS_HxPJekjy5IfWyS7BFz0b9id0CM62ajDVjBS2MkLjqZQldoBE9KwFS-7I_YyUOPqlRGuqnKw5orY5pVpUduj3mitUln5LU3pI0_UuBp9FjTwnDr9AHETLMSeHK6xiGoWSLi9yYT034cwSRjohn17zcQPNFTs8s153sK9Uv_Yh0-5_5d7-o9zbD-UqCaRWrllSYZQxLw_HUhb0ta-y4NnJUxfUvc7QuLJSaO0a3oh2MLBZat8u-wsPnXzKQvTtVVF34xK5d69ThFmHEQ4SpzeVRediTG8rjD5vBSeN3E5JyHh6R1DQK9-iml5kjzQUN_lSgVU8DhYLx7wwjSvRkMDvTjiwF4zM1kXZ7DlF1eN3A7IG85e-zRrYEjjm0FkI4Cc7Ripm0pHOChexhcWXzreeZyRMU6Mk3ljxC9w4QH-cQZ_b3T5pjHxk1VNr1CDrnJy5QDh6XLO6FrLNSRb2l9gz0wo3S6m7HErSgLsPGMHkpDZK31jOanXeHPQz-eruLHUP0z6yTbpbrn223V70uMXNSpQSZjpL0y8hcxxpNqA6_ql3BQAxlxvfpQ_uT9GrWjQC6iRHM8D0MP0GQsIi92QEAAA=):

```
{#snippet figure(image)}
	<figure>
		<img src={image.src} alt={image.caption} width={image.width} height={image.height} />
		<figcaption>{image.caption}</figcaption>
	</figure>
{/snippet}

{#each images as image}
	{#if image.href}
		<a href={image.href}>
			{@render figure(image)}
		</a>
	{:else}
		{@render figure(image)}
	{/if}
{/each}
```

Like function declarations, snippets can have an arbitrary number of parameters, which can have default values, and you can destructure each parameter. You cannot use rest parameters, however.

## Snippet scope[](#Snippet-scope)

Snippets can be declared anywhere inside your component. They can reference values declared outside themselves, for example in the `<script>` tag or in `{#each ...}` blocks...

[Open in playground](/playground/untitled#H4sIAAAAAAAAA22Q0WrDMAxFf0VRB2nALO9eGrZv6OMyqJOqncG1jaVuK8b_PtwFBmOv96BzJWX05kKoce9tjCSMCk_WEaN-zTgbppW_xPjIH-SEUOESvJAXRo0DL8lGGSc_iSOBDBdiNmeCHRystAznREZAAjAR3MK1OUCBHTzEFCJvu6fJD_2vxOcN_6wC7-Rc2Nb-rlT9EMd7BLlmpYG8VpVm6OM4-dyvo-Uuek7kj5RWT2ucXaitqr9kDnPbFVT4361CX4Ja0pUUyi1WXh-E5U2hGOs-rT-iPhnHVL4BFIsl2E4BAAA)

```
<script>
	let { message = `it's great to see you!` } = $props();
</script>

{#snippet hello(name)}
	<p>hello {name}! {message}!</p>
{/snippet}

{@render hello('alice')}
{@render hello('bob')}
```

```
<script lang="ts">
	let { message = `it's great to see you!` } = $props();
</script>

{#snippet hello(name)}
	<p>hello {name}! {message}!</p>
{/snippet}

{@render hello('alice')}
{@render hello('bob')}
```

...and they are 'visible' to everything in the same lexical scope (i.e. siblings, and children of those siblings):

```
<div>
	{#snippet x()}
		{#snippet y()}...{/snippet}

		<!-- this is fine -->
		{@render y()}
	{/snippet}

	<!-- this will error, as `y` is not in scope -->
	{@render y()}
</div>

<!-- this will also error, as `x` is not in scope -->
{@render x()}
```

Snippets can reference themselves and each other:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA22QS2oDMRBEryLaGxvkGXsrjInPkGUmC3mmFQRKj1C3P0EIco5scsUcIciZfLCz66aqHkVlIPuMYOAeg1smdJiQek9PisnHiMKgwfmADOYhw94yToFdjA0fMQiChn4kQRIGA3k2JdU-WJbRufmidNTJhqOl7cf72-umvZwd5XbyVgP9JvvxQDKMJ5rTVzbPvFOktmp1eb9hmUrTND-4KuS7hDRg-stQS7WeOAYDY7myXhXNrXflptwtd71aFNDw3x6CZwEj6YAa5CVWvY4I5VGDWB9OngYwztYyn_B_XViDAQAA)

```
{#snippet blastoff()}
	<span>🚀</span>
{/snippet}

{#snippet countdown(n)}
	{#if n > 0}
		<span>{n}...</span>
		{@render countdown(n - 1)}
	{:else}
		{@render blastoff()}
	{/if}
{/snippet}

{@render countdown(10)}
```

## Passing snippets to components[](#Passing-snippets-to-components)

### Explicit props[](#Passing-snippets-to-components-Explicit-props)

Within the template, snippets are values just like any other. As such, they can be passed to components as props:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA3VS224bIRD9lRGpZLtde5NIeSFk1VZqv6BvcR7YhfWiYsAwbmIh_r1iL74leZzDmTMznBOJ4VtJKPn15rRqFEIwyjmJ4Lx1gRSkVVoGQp8jqXmQI_uHc6vwT2qUpCCNNSgNBkIJC41XDqu1WaPaOusR_vBaS2i93cJsVfbV2Dp7XJtMbKwJCK3fKwzwBM8ZW2OEPIvCjDunZZgVsMMDhYcCnFeNpHAPqbii1txww4_cu9sj-e49uemk9-qkfH9i364eIGX6y-PasPJ0lIk30_90kgvp54uex7Cr-gNYiV01ITs8XNS9-gWCFrkekViO0ulykLevczGNEVUUq3xAYiWK6gzc4eEd1g_8iAlf4er1cjobXBMc-VMcnEkQh5MTRG9fE5QVKchHeUD5hoSi38uC4MHl9xwikoqLDJ1H4fMUaYkQ-0WK8cuL_COQ4Am-9BmdL65NYpil-_Z4o9qxLw3-M8xlNRS59FX87qUR0p88ZSX6kZLdmRpiqdo0hJZhbcVh5MQbyZuu3xJ4AJE-VB-NPNOOZe4brC0nQVYe1zcs4GG8pAchDo35i5dcq42hoGWLjwNcWy-kXwbHG2U2FG57fNy41wf01GC3bDqlxfzefLtbTJo1b_5uvN0bQeHnHtGa37yRFwr9CnSjbc31HLtFAVeQOKo5LsSww-pBbicVVg4HnZJzlYJPs_NSEORKvyojCG25DjL9BzevAka8BAAA)

```
<script>
	import Table from './Table.svelte';

	const fruits = [
		{ name: 'apples', qty: 5, price: 2 },
		{ name: 'bananas', qty: 10, price: 1 },
		{ name: 'cherries', qty: 20, price: 0.5 }
	];
</script>

{#snippet header()}
	<th>fruit</th>
	<th>qty</th>
	<th>price</th>
	<th>total</th>
{/snippet}

{#snippet row(d)}
	<td>{d.name}</td>
	<td>{d.qty}</td>
	<td>{d.price}</td>
	<td>{d.qty * d.price}</td>
{/snippet}

<Table data={fruits} {header} {row} />
```

```
<script lang="ts">
	import Table from './Table.svelte';

	const fruits = [
		{ name: 'apples', qty: 5, price: 2 },
		{ name: 'bananas', qty: 10, price: 1 },
		{ name: 'cherries', qty: 20, price: 0.5 }
	];
</script>

{#snippet header()}
	<th>fruit</th>
	<th>qty</th>
	<th>price</th>
	<th>total</th>
{/snippet}

{#snippet row(d)}
	<td>{d.name}</td>
	<td>{d.qty}</td>
	<td>{d.price}</td>
	<td>{d.qty * d.price}</td>
{/snippet}

<Table data={fruits} {header} {row} />
```

```
<script>
	let { data, header, row } = $props();
</script>

<table>
	{#if header}
		<thead>
			<tr>{@render header()}</tr>
		</thead>
	{/if}

	<tbody>
		{#each data as d}
			<tr>{@render row(d)}</tr>
		{/each}
	</tbody>
</table>

<style>
	table {
		text-align: left;
		border-spacing: 0;
	}

	tbody tr:nth-child(2n+1) {
		background: ButtonFace;
	}

	table :global(th), table :global(td) {
		padding: 0.5em;
	}
</style>
```

```
<script lang="ts">
	let { data, header, row } = $props();
</script>

<table>
	{#if header}
		<thead>
			<tr>{@render header()}</tr>
		</thead>
	{/if}

	<tbody>
		{#each data as d}
			<tr>{@render row(d)}</tr>
		{/each}
	</tbody>
</table>

<style>
	table {
		text-align: left;
		border-spacing: 0;
	}

	tbody tr:nth-child(2n+1) {
		background: ButtonFace;
	}

	table :global(th), table :global(td) {
		padding: 0.5em;
	}
</style>
```

Think about it like passing content instead of data to a component. The concept is similar to slots in web components.

### Implicit props[](#Passing-snippets-to-components-Implicit-props)

As an authoring convenience, snippets declared directly _inside_ a component implicitly become props _on_ the component:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA3VSwW7bMAz9FUIdkKRz47ZAL4pibDsM2H23pgfZomNhiqxKzLpA8L8Plp24SdOjnh4fH8kXmZU7ZJz92jmjK00QrHYOCZxvXWAZq7XBwPhzZKUMOLK_O7cMf9EQsoxVrSW0FBhnIlReOyo2dkN651pP8FuWBqH27Q5myzy9xtLZamN7YtXaQFD7vaYAa3jusQ1F6HtxmEnnDIZZBq904PCUgfO6Qg6P0GUX1FJaaeWJ-3B_Ij98JFcNeq8n5ceJfb98gq6nv6w2VuTTUFYM4yhJch0Hy12aNt4cF9egVOjni27oJ6gpElHk1BQT9kqHCyQ1v8CoJWlOWMzHJt2wuampb9_mamqpiqiW_ZydyEkVZ_ArHa6gqfl1NtzCh__3TsRw1YJl7Fo8CP8R4-T3mDE6uP6_zxTrsrNIvU_G56EySBDT-rNx0Vk_O3Swhi8psvPFh5tRsjcsTNdj3XQelMeZ-6cv4jePVqGfLily8se15FNBzHU9XkJQ2arDyIk3KKsmuQQZQHVX1ceTvdOOeV-X2CI_Cor8ZN-KQIdxkgRCHAr7Fd9Jo7eWg8GaVgNctl6hvwtOVtpuOdwnfHSc9IE8t9TcVY02av5ovz4sjpqlrP5sfbu3isOPPVFrf8oKzxSSBb41bSnNnJpFBheQOqk5qdTgYfmEu6OKyIeBpuRcpODT7LxkjKQ2b9oqxmtpAnb_AUx9fWbLBAAA)

```
<script>
	import Table from './Table.svelte';

	const fruits = [
		{ name: 'apples', qty: 5, price: 2 },
		{ name: 'bananas', qty: 10, price: 1 },
		{ name: 'cherries', qty: 20, price: 0.5 }
	];
</script>

<Table data={fruits}>
	{#snippet header()}
		<th>fruit</th>
		<th>qty</th>
		<th>price</th>
		<th>total</th>
	{/snippet}

	{#snippet row(d)}
		<td>{d.name}</td>
		<td>{d.qty}</td>
		<td>{d.price}</td>
		<td>{d.qty * d.price}</td>
	{/snippet}
</Table>
```

```
<script lang="ts">
	import Table from './Table.svelte';

	const fruits = [
		{ name: 'apples', qty: 5, price: 2 },
		{ name: 'bananas', qty: 10, price: 1 },
		{ name: 'cherries', qty: 20, price: 0.5 }
	];
</script>

<Table data={fruits}>
	{#snippet header()}
		<th>fruit</th>
		<th>qty</th>
		<th>price</th>
		<th>total</th>
	{/snippet}

	{#snippet row(d)}
		<td>{d.name}</td>
		<td>{d.qty}</td>
		<td>{d.price}</td>
		<td>{d.qty * d.price}</td>
	{/snippet}
</Table>
```

```
<script>
	let { data, header, row } = $props();
</script>

<table>
	{#if header}
		<thead>
			<tr>{@render header()}</tr>
		</thead>
	{/if}

	<tbody>
		{#each data as d}
			<tr>{@render row(d)}</tr>
		{/each}
	</tbody>
</table>

<style>
	table {
		text-align: left;
		border-spacing: 0;
	}

	tbody tr:nth-child(2n+1) {
		background: ButtonFace;
	}

	table :global(th), table :global(td) {
		padding: 0.5em;
	}
</style>
```

```
<script lang="ts">
	let { data, header, row } = $props();
</script>

<table>
	{#if header}
		<thead>
			<tr>{@render header()}</tr>
		</thead>
	{/if}

	<tbody>
		{#each data as d}
			<tr>{@render row(d)}</tr>
		{/each}
	</tbody>
</table>

<style>
	table {
		text-align: left;
		border-spacing: 0;
	}

	tbody tr:nth-child(2n+1) {
		background: ButtonFace;
	}

	table :global(th), table :global(td) {
		padding: 0.5em;
	}
</style>
```

### Implicit children snippet[](#Passing-snippets-to-components-Implicit-children-snippet)

Any content inside the component tags that is _not_ a snippet declaration implicitly becomes part of the `children` snippet:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA3WQwU7DQAxEf8VYSG2lTXsPIQJufAPhkGwcsarXWe06FBTl31HV0KiFHu3xaN54RKk9YY6vPrCzTsF-OG4jCSRxIZCiwc4xJczfRmzqRLPhOYRt-iRWQoO2FyXRhDkWyUYXtKykUudDHxVeBtVeoIu9h9V2dxpn8-qhkmK3eKQ4yaVlZ_fgqZjvSzT4X7TSl2KucSCD-h2O-pEXJ3OBexF6m5hJYVx-MMEj3IfYh7Te_AG9yzKIlAZWODhmaAiK5hp-XkCWlZX8yuNTJGkpnoPWm-l8uvS8Zr5Z9d2g1o4PTlrMu5oTTT8t5Ku72QEAAA)

```
<script>
	import Button from './Button.svelte';
</script>

<Button>click me</Button>
```

```
<script lang="ts">
	import Button from './Button.svelte';
</script>

<Button>click me</Button>
```

```
<script>
	let { children } = $props();
</script>

<!-- result will be <button>click me</button> -->
<button>{@render children()}</button>
```

```
<script lang="ts">
	let { children } = $props();
</script>

<!-- result will be <button>click me</button> -->
<button>{@render children()}</button>
```

> Note that you cannot have a prop called `children` if you also have content inside the component — for this reason, you should avoid having props with that name

### Optional snippet props[](#Passing-snippets-to-components-Optional-snippet-props)

You can declare snippet props as being optional. You can either use optional chaining to not render anything if the snippet isn't set...

```
<script>
	let { children } = $props();
</script>

{@render children?.()}
```

...or use an `#if` block to render fallback content:

```
<script>
	let { children } = $props();
</script>

{#if children}
	{@render children()}
{:else}
	fallback content
{/if}
```

## Typing snippets[](#Typing-snippets)

Snippets implement the `Snippet` interface imported from `'svelte'`:

```
<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		data: any[];
		children: Snippet;
		row: Snippet<[any]>;
	}

	let { data, children, row }: Props = $props();
</script>
```

With this change, red squigglies will appear if you try and use the component without providing a `data` prop and a `row` snippet. Notice that the type argument provided to `Snippet` is a tuple, since snippets can have multiple parameters.

We can tighten things up further by declaring a generic, so that `data` and `row` refer to the same type:

```
<script lang="ts" generics="T">
	import type { Snippet } from 'svelte';

	let {
		data,
		children,
		row
	}: {
		data: T[];
		children: Snippet;
		row: Snippet<[T]>;
	} = $props();
</script>
```

## Exporting snippets[](#Exporting-snippets)

Snippets declared at the top level of a `.svelte` file can be exported from a `<script module>` for use in other components, provided they don't reference any declarations in a non-module `<script>` (whether directly or indirectly, via other snippets):

[Open in playground](/playground/untitled#H4sIAAAAAAAAA3XPwU4DIRAG4FeZjIdqStroEVtjDz6FeGDLbELCzhKY1jWEdzc021RtPcP_z_cXZDsQanyb4piEHGT2MZJkVNj7QBn1e8HOZpo_7mJc5SMFIVS4H1mIJaPGTd4nH-XFsBE_tDIoYJ2DCn0aB1is1ufqOb94NrxZX2JcXhOxo9Ri948Knh6qYVR467LQJKglHUihfMX23rhY1S_tn5M3yTCM7hDoJKfpp_wKeDf3nYRWQdeERoqtsITSVdhCsbCErhou5731MuGa8--OD4Viffj07FD3NmSq3-doRU-tAQAA)

```
<script>
	import { add } from './snippets.svelte';
</script>

{@render add(1, 2)}
```

```
<script lang="ts">
	import { add } from './snippets.svelte';
</script>

{@render add(1, 2)}
```

```
<script module>
	export { add };
</script>

{#snippet add(a, b)}
	{a} + {b} = {a + b}
{/snippet}
```

> This requires Svelte 5.5.0 or newer

## Programmatic snippets[](#Programmatic-snippets)

Snippets can be created programmatically with the [`createRawSnippet`](svelte#createRawSnippet) API. This is intended for advanced use cases.

## Snippets and slots[](#Snippets-and-slots)

In Svelte 4, content can be passed to components using [slots](legacy-slots). Snippets are more powerful and flexible, and so slots have been deprecated in Svelte 5.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/03-template-syntax/06-snippet.md) [llms.txt](/docs/svelte/snippet/llms.txt)

previous next

[{#await ...}](/docs/svelte/await) [{@render ...}](/docs/svelte/@render)
