---
title: "{#each ...}"
source: "https://svelte.dev/docs/svelte/each"
canonical_url: "https://svelte.dev/docs/svelte/each"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:32.425Z"
content_hash: "d510ed28cbd3eeca877be5d7e1a1ccabdf3ee4fd97b7a170a93862bba51bb54c"
menu_path: ["{#each ...}"]
section_path: []
---
```
{#each expression as name}...{/each}
```

```
{#each expression as name, index}...{/each}
```

Iterating over values can be done with an each block. The values in question can be arrays, array-like objects (i.e. anything with a `length` property), or iterables like `Map` and `Set`. (Internally, they are converted to arrays with [`Array.from`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from).)

If the value is `null` or `undefined`, it is treated the same as an empty array (which will cause [else blocks](#Else-blocks) to be rendered, where applicable).

```
<h1>Shopping list</h1>
<ul>
	{#each items as item}
		<li>{item.name} x {item.qty}</li>
	{/each}
</ul>
```

An each block can also specify an _index_, equivalent to the second argument in an `array.map(...)` callback:

```
{#each items as item, i}
	<li>{i + 1}: {item.name} x {item.qty}</li>
{/each}
```

## Keyed each blocks[](#Keyed-each-blocks)

```
{#each expression as name (key)}...{/each}
```

```
{#each expression as name, index (key)}...{/each}
```

If a _key_ expression is provided — which must uniquely identify each list item — Svelte will use it to intelligently update the list when data changes by inserting, moving and deleting items, rather than adding or removing items at the end and updating the state in the middle.

The key can be any object, but strings and numbers are recommended since they allow identity to persist when the objects themselves change.

```
{#each items as item (item.id)}
	<li>{item.name} x {item.qty}</li>
{/each}

<!-- or with additional index value -->
{#each items as item, i (item.id)}
	<li>{i + 1}: {item.name} x {item.qty}</li>
{/each}
```

You can freely use destructuring and rest patterns in each blocks.

```
{#each items as { id, name, qty }, i (id)}
	<li>{i + 1}: {name} x {qty}</li>
{/each}

{#each objects as { id, ...rest }}
	<li><span>{id}</span><MyComponent {...rest} /></li>
{/each}

{#each items as [id, ...rest]}
	<li><span>{id}</span><MyComponent values={rest} /></li>
{/each}
```

## Each blocks without an item[](#Each-blocks-without-an-item)

```
{#each expression}...{/each}
```

```
{#each expression, index}...{/each}
```

In case you just want to render something `n` times, you can omit the `as` part:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA3WR3WrDMAyFX0VoDFqWtHRXxWsKY4-x7MKx1dbUtY2t_hHy7sNu1m2w3QmdT8c6co9OHggFvu0oJei8jBor3BhLCcV7j51MNCKvIczSiSwTVqi8Y3KcUOBKmxMoK1NqWlTZpy4-La5b13L_QFLtoAdLbss7AUsYKojS7Ycs_wfkFUag5e8nRGel2jf9JBvAU8Gm8AjP0DQNLIb1aq7NaT06z7NzcbmXd92tEl8tFXT2Y23ob8PapGDlVcA2Gv1y6-WyZjoEK5lq5e3x4JKASIEkT5YVLDZxOrLRn_-TOh81RQGLcIHkrdFQUo2qTIEU11Gy8QIWuVv6swJ9rddyJ9V-G_3RafFrvuQtSW8BscK_fpDpwig4HqlCvoas52Pi8FEhS2PPxmkUG2kTDZ_S2A6dJwIAAA)

```
<div class="chess-board">
	{#each { length: 8 }, rank}
		{#each { length: 8 }, file}
			<div class:black={(rank + file) % 2 === 1}></div>
		{/each}
	{/each}
</div>

<style>
	.chess-board {
		display: grid;
		grid-template-columns: repeat(8, 1fr);
		rows: repeat(8, 1fr);
		border: 1px solid black;
		aspect-ratio: 1;

		.black {
			background: black;
		}
	}
</style>
```

## Else blocks[](#Else-blocks)

```
{#each expression as name}...{:else}...{/each}
```

An each block can also have an `{:else}` clause, which is rendered if the list is empty.

```
{#each todos as todo}
	<p>{todo.text}</p>
{:else}
	<p>No tasks today!</p>
{/each}
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/03-template-syntax/03-each.md) [llms.txt](/docs/svelte/each/llms.txt)

previous next

[{#if ...}](/docs/svelte/if) [{#key ...}](/docs/svelte/key)
