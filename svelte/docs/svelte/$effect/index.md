---
title: "$effect"
source: "https://svelte.dev/docs/svelte/$effect"
canonical_url: "https://svelte.dev/docs/svelte/$effect"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:16.564Z"
content_hash: "a834fe901394df302477a70401d87f7bd1362bb55f7d69d96782136c71aa6854"
menu_path: ["$effect"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/$derived/index.md", "title": "$derived"}
nav_next: {"path": "svelte/docs/svelte/$props/index.md", "title": "$props"}
---

Effects are functions that run when state updates, and can be used for things like calling third-party libraries, drawing on `<canvas>` elements, or making network requests. They only run in the browser, not during server-side rendering.

Generally speaking, you should _not_ update state inside effects, as it will make code more convoluted and will often lead to never-ending update cycles. If you find yourself doing so, see [when not to use `$effect`](#When-not-to-use-$effect) to learn about alternative approaches.

You can create an effect with the `$effect` rune ([demo](/playground/untitled#H4sIAAAAAAAAE31S246bMBD9lZF3pSRSAqTVvrCAVPUP2sdSKY4ZwJJjkD0hSVH-vbINuWxXfQH5zMyZc2ZmZLVUaFn6a2R06ZGlHmBrpvnBvb71fWQHVOSwPbf4GS46TajJspRlVhjZU1HqkhQSWPkHIYdXS5xw-Zas3ueI6FRn7qHFS11_xSRZhIxbFtcDtw7SJb1iXaOg5XIFeQGjzyPRaevYNOGZIJ8qogbpe8CWiy_VzEpTXiQUcvPDkSVrSNZz1UlW1N5eLcqmpdXUvaQ4BmqlhZNUCgxuzFHDqUWNAxrYeUM76AzsnOsdiJbrBp_71lKpn3RRbii-4P3f-IMsRxS-wcDV_bL4PmSdBa2wl7pKnbp8DMgVvJm8ZNskKRkEM_OzyOKQFkgqOYBQ3Nq89Ns0nbIl81vMFN-jKoLMTOr-SOBOJS-Z8f5Y6D1wdcR8dFqvEBdetK-PHwj-z-cH8oHPY54wRJ8Ys7iSQ3Bg3VA9azQbmC9k35kKzYa6PoVtfwbbKVnBixBiGn7Pq0rqJoUtHiCZwAM3jdTPWCVtr_glhVrhecIa3vuksJ_b7TqFs4DPyriSjd5IwoNNQaAmNI-ESfR2p8zimzvN1swdCkvJHPH6-_oX8o1SgcIDAAA=)):

```
<script>
	let size = $state(50);
	let color = $state('#ff3e00');

	let canvas;

	$effect(() => {
		const context = canvas.getContext('2d');
		context.clearRect(0, 0, canvas.width, canvas.height);

		// this will re-run whenever `color` or `size` change
		context.fillStyle = color;
		context.fillRect(0, 0, size, size);
	});
</script>

<canvas bind:this={canvas} width="100" height="100"></canvas>
```

When Svelte runs an effect function, it tracks which pieces of state (and derived state) are accessed (unless accessed inside [`untrack`](svelte#untrack)), and re-runs the function when that state later changes.

> If you're having difficulty understanding why your `$effect` is rerunning or is not running see [understanding dependencies](#Understanding-dependencies). Effects are triggered differently than the `$:` blocks you may be used to if coming from Svelte 4.

### Understanding lifecycle[](#Understanding-lifecycle)

Your effects run after the component has been mounted to the DOM, and in a [microtask](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API/Microtask_guide) after state changes. Re-runs are batched (i.e. changing `color` and `size` in the same moment won't cause two separate runs), and happen after any DOM updates have been applied.

You can use `$effect` anywhere, not just at the top level of a component, as long as it is called while a parent effect is running.

> Svelte uses effects internally to represent logic and expressions in your template — this is how `<h1>hello {name}!</h1>` updates when `name` changes.

An effect can return a _teardown function_ which will run immediately before the effect re-runs:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA41Swa6bMBD8lZX1DqGlJemRB5F66KH33kqlZ8xQrDprZC-hEeLfK-AlL6l66Mna3Rnv7OxOivUJKldf2hZGSKBD40dWqWqtQ1T590nVOuIV9rnvP8YznEClyngWsESVqyKaYHs5VlyJg5DxAwuV9BRFC3b75PlaOVnnbITx3MQ3wGG_3zBcyRNWLbtdQuWRpiVVSZbRt85GGq1zVIMCTIAWNDR2YJwR6OX-6xcyneafiBvdeI5ClgXhrB2VFCFfX6PHRgt20f6-pMPzlprTB9VXnZUEyBCY_uJnGdmW9M1Lagc2Yj2TjdQHf7YNmpSsbMOEge-YOiF7OqGxWuAuVKP1ASQdaHOFAj6EgeMdpU5WD1aQ8afeM1iWXg2iBH9Bc5vMQYfb2Fc3kuuY6zsvYZG97ZOL7nCcVlPmIusOW64eRDyTZ-Os-VVOmwe7h-2-K-lTMh-j8yNCkW2U43-Ss43c6ih3ZJWqf12i4LeoXMKAVMmlX-rL-ar5R6pEWzdablTeahcx_wH9Im6v8wIAAA)

```
<script>
	let count = $state(0);
	let milliseconds = $state(1000);

	$effect(() => {
		// This will be recreated whenever `milliseconds` changes
		const interval = setInterval(() => {
			count += 1;
		}, milliseconds);

		return () => {
			// if a teardown function is provided, it will run
			// a) immediately before the effect re-runs
			// b) when the component is destroyed
			clearInterval(interval);
		};
	});
</script>

<h1>{count}</h1>

<button onclick={() => (milliseconds *= 2)}>slower</button>
<button onclick={() => (milliseconds /= 2)}>faster</button>
```

```
<script lang="ts">
	let count = $state(0);
	let milliseconds = $state(1000);

	$effect(() => {
		// This will be recreated whenever `milliseconds` changes
		const interval = setInterval(() => {
			count += 1;
		}, milliseconds);

		return () => {
			// if a teardown function is provided, it will run
			// a) immediately before the effect re-runs
			// b) when the component is destroyed
			clearInterval(interval);
		};
	});
</script>

<h1>{count}</h1>

<button onclick={() => (milliseconds *= 2)}>slower</button>
<button onclick={() => (milliseconds /= 2)}>faster</button>
```

Teardown functions also run when the effect is destroyed, which happens when its parent is destroyed (for example, a component is unmounted) or the parent effect re-runs.

### Understanding dependencies[](#Understanding-dependencies)

`$effect` automatically picks up any reactive values (`$state`, `$derived`, `$props`) that are _synchronously_ read inside its function body (including indirectly, via function calls) and registers them as dependencies. When those dependencies change, the `$effect` schedules a re-run.

If `$state` and `$derived` are used directly inside the `$effect` (for example, during creation of a [reactive class](svelte/docs/svelte/$state/index.md#Classes)), those values will _not_ be treated as dependencies.

Values that are read _asynchronously_ — after an `await` or inside a `setTimeout`, for example — will not be tracked. Here, the canvas will be repainted when `color` changes, but not when `size` changes ([demo](/playground/untitled#H4sIAAAAAAAAE31T246bMBD9lZF3pWSlBEirfaEQqdo_2PatVIpjBrDkGGQPJGnEv1e2IZfVal-wfHzmzJyZ4cIqqdCy9M-F0blDlnqArZjmB3f72XWRHVCRw_bc4me4aDWhJstSlllhZEfbQhekkMDKfwg5PFvihMvX5OXH_CJa1Zrb0-Kpqr5jkiwC48rieuDWQbqgZ6wqFLRcvkC-hYvnkWi1dWqa8ESQTxFRjfQWsOXiWzmr0sSLhEJu3p1YsoJkNUcdZUnN9dagrBu6FVRQHAM10sJRKgUG16bXcGxQ44AGdt7SDkTDdY02iqLHnJVU6hedlWuIp94JW6Tf8oBt_8GdTxlF0b4n0C35ZLBzXb3mmYn3ae6cOW74zj0YVzDNYXRHFt9mprNgHfZSl6mzml8CMoLvTV6wTZIUDEJv5us2iwMtiJRyAKG4tXnhl8O0yhbML0Wm-B7VNlSSSd31BG7z8oIZZ6dgIffAVY_5xdU9Qrz1Bnx8fCfwtZ7v8Qc9j3nB8PqgmMWlHIID6-bkVaPZwDySfWtKNGtquxQ23Qlsq2QJT0KIqb8dL0up6xQ2eIBkAg_c1FI_YqW0neLnFCqFpwmreedJYT7XX8FVOBfwWRhXstZrSXiwKQjUhOZeMIleb5JZfHWn2Yq5pWEpmR7Hv-N_wEqT8hEEAAA=)):

```
function $effect(fn: () => void | (() => void)): void
namespace $effectRuns code when a component is mounted to the DOM, and then whenever its dependencies change, i.e. $state or $derived values.
The timing of the execution is after the DOM has been updated.
Example:
$effect(() => console.log('The count is now ' + count));If you return a function from the effect, it will be called right before the effect is run again, or when the component is unmounted.
Does not run during server-side rendering.
@see{@link https://svelte.dev/docs/svelte/$effect Documentation}@paramfn The function to execute$effect(() => {
	const const context: CanvasRenderingContext2Dcontext = let canvas: {
    width: number;
    height: number;
    getContext(type: "2d", options?: CanvasRenderingContext2DSettings): CanvasRenderingContext2D;
}canvas.function getContext(type: "2d", options?: CanvasRenderingContext2DSettings): CanvasRenderingContext2DgetContext('2d');
	const context: CanvasRenderingContext2Dcontext.CanvasRect.clearRect(x: number, y: number, w: number, h: number): voidMDN Reference
clearRect(0, 0, let canvas: {
    width: number;
    height: number;
    getContext(type: "2d", options?: CanvasRenderingContext2DSettings): CanvasRenderingContext2D;
}canvas.width: numberwidth, let canvas: {
    width: number;
    height: number;
    getContext(type: "2d", options?: CanvasRenderingContext2DSettings): CanvasRenderingContext2D;
}canvas.height: numberheight);

	// this will re-run whenever `color` changes...
	const context: CanvasRenderingContext2Dcontext.CanvasFillStrokeStyles.fillStyle: string | CanvasGradient | CanvasPatternMDN Reference
fillStyle = let color: stringcolor;

	function setTimeout<[]>(callback: () => void, delay?: number): NodeJS.Timeout (+2 overloads)Schedules execution of a one-time callback after delay milliseconds.
The callback will likely not be invoked in precisely delay milliseconds.
Node.js makes no guarantees about the exact timing of when callbacks will fire,
nor of their ordering. The callback will be called as close as possible to the
time specified.
When delay is larger than 2147483647 or less than 1 or NaN, the delay
will be set to 1. Non-integer delays are truncated to an integer.
If callback is not a function, a TypeError will be thrown.
This method has a custom variant for promises that is available using
timersPromises.setTimeout().
@sincev0.0.1@paramcallback The function to call when the timer elapses.@paramdelay The number of milliseconds to wait before calling the
callback. Default: 1.@paramargs Optional arguments to pass when the callback is called.@returnsfor use with clearTimeout()setTimeout(() => {
		// ...but not when `size` changes
		const context: CanvasRenderingContext2Dcontext.CanvasRect.fillRect(x: number, y: number, w: number, h: number): voidMDN Reference
fillRect(0, 0, let size: numbersize, let size: numbersize);
	}, 0);
});
```

An effect only reruns when the object it reads changes, not when a property inside it changes. (If you want to observe changes _inside_ an object at dev time, you can use [`$inspect`]($inspect).)

```
<script>
	let state = $state({ value: 0 });
	let derived = $derived({ value: state.value * 2 });

	// this will run once, because `state` is never reassigned (only mutated)
	$effect(() => {
		state;
	});

	// this will run whenever `state.value` changes...
	$effect(() => {
		state.value;
	});

	// ...and so will this, because `derived` is a new object each time
	$effect(() => {
		derived;
	});
</script>

<button onclick={() => (state.value += 1)}>
	{state.value}
</button>

<p>{state.value} doubled is {derived.value}</p>
```

An effect only depends on the values that it read the last time it ran. This has interesting implications for effects that have conditional code.

For instance, if `condition` is `true` in the code snippet below, the code inside the `if` block will run and `color` will be evaluated. This means that changes to either `condition` or `color` [will cause the effect to re-run](/playground/untitled#H4sIAAAAAAAAE21RQW6DMBD8ytaNBJHaJFLViwNIVZ8RcnBgXVk1xsILTYT4e20TQg89IOPZ2fHM7siMaJBx9tmaWpFqjQNlAKXEihx7YVJpdIyfRkY3G4gB8Pi97cPanRtQU8AuwuF_eNUaQuPlOMtc1SlLRWlKUo1tOwJflUikQHZtA0klzCDc64Imx0ANn8bInV1CDhtHgjClrsftcSXotluLybOUb3g4JJHhOZs5WZpuIS9gjNqkJKQP5e2ClrR4SMdZ13E4xZ8zTPOTJU2A2uE_PQ9COCI926_hTVarIU4hu_REPlBrKq2q73ycrf1N-vS4TMUsulaVg3EtR8H9rFgsg8uUsT1B2F9eshigZHBRpuaD0D3mY8Qm2BfB5N2YyRzdNEYVDy0Ja-WsFjcOUuP1HvFLWA6H3XuHTUSmmDV2--0TXonxsKbp7G9C6R__NONS-MFNvxj_d6mBAgAA).

Conversely, if `condition` is `false`, `color` will not be evaluated, and the effect will _only_ re-run again when `condition` changes.

```
import function confetti(opts?: ConfettiOptions): voidconfetti from 'canvas-confetti';

let let condition: booleancondition = function $state<true>(initial: true): true (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state(true);
let let color: stringcolor = function $state<"#ff3e00">(initial: "#ff3e00"): "#ff3e00" (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state('#ff3e00');

function $effect(fn: () => void | (() => void)): void
namespace $effectRuns code when a component is mounted to the DOM, and then whenever its dependencies change, i.e. $state or $derived values.
The timing of the execution is after the DOM has been updated.
Example:
$effect(() => console.log('The count is now ' + count));If you return a function from the effect, it will be called right before the effect is run again, or when the component is unmounted.
Does not run during server-side rendering.
@see{@link https://svelte.dev/docs/svelte/$effect Documentation}@paramfn The function to execute$effect(() => {
	if (let condition: truecondition) {
		function confetti(opts?: ConfettiOptions): voidconfetti({ ConfettiOptions.colors: string[]colors: [let color: stringcolor] });
	} else {
		function confetti(opts?: ConfettiOptions): voidconfetti();
	}
});
```

## $effect.pre[](#$effect.pre)

In rare cases, you may need to run code _before_ the DOM updates. For this we can use the `$effect.pre` rune:

```
<script>
	import { tick } from 'svelte';

	let div = $state();
	let messages = $state([]);

	// ...

	$effect.pre(() => {
		if (!div) return; // not yet mounted

		// reference `messages` array length so that this code re-runs whenever it changes
		messages.length;

		// autoscroll when new messages are added
		if (div.offsetHeight + div.scrollTop > div.scrollHeight - 20) {
			tick().then(() => {
				div.scrollTo(0, div.scrollHeight);
			});
		}
	});
</script>

<div bind:this={div}>
	{#each messages as message}
		<p>{message}</p>
	{/each}
</div>
```

Apart from the timing, `$effect.pre` works exactly like `$effect`.

## $effect.tracking[](#$effect.tracking)

The `$effect.tracking` rune is an advanced feature that tells you whether or not the code is running inside a tracking context, such as an effect or inside your template:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA32Q0WrDMAxFf0UTgybgJO-uZ9h3LHvwPKWYObKJ1bUj5N-Hu8IeMvYqHc6V7orsZkKNjzRN5KWXxfmPwKemRYVTiFRQv6z45grdyeec-_JJUQgV-sRCLAU1muKXkMWOPIpPXFKkPqZTcwgMPs05MbFAITlnfVCwD2yPMAwwuVho5Gq5I03TwpOFtY726h_mP6Ms5yqUrT2ObIbfM9lkGxiE5hydkIZ1r9jMkC2Yh667eaDrLCr8qwqhq6CukEL5ynVf-8PtVaG4EC-B31Hf3tu-AQVqZkt3AQAA)

```
<script>
	console.log('in component setup:', $effect.tracking()); // false

	$effect(() => {
		console.log('in effect:', $effect.tracking()); // true
	});
</script>

<p>in template: {$effect.tracking()}</p> <!-- true -->
```

```
<script lang="ts">
	console.log('in component setup:', $effect.tracking()); // false

	$effect(() => {
		console.log('in effect:', $effect.tracking()); // true
	});
</script>

<p>in template: {$effect.tracking()}</p> <!-- true -->
```

It is used to implement abstractions like [`createSubscriber`](/docs/svelte/svelte-reactivity#createSubscriber), which will create listeners to update reactive values but _only_ if those values are being tracked (rather than, for example, read inside an event handler).

## $effect.pending[](#$effect.pending)

When using [`await`](await-expressions) in components, the `$effect.pending()` rune tells you how many promises are pending in the current [boundary](svelte-boundary), not including child boundaries:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA3WRT0-EQAzFv0pTPUAgspp4YVkSv4EHb-KhQMdMZMuEKa6byXx3w7Jq_Hd975f2tS-g0J6xxEs2hju9ciy9lWfM0diBPZaPAVvyfMbunLvyrzwoY47dKMqiHkusfDdZp3UjjQ6sQLCDS6-knFyn2w-1_VJvTqo0Sv4oHZhZOrWjAPV9Qjm0KYTFbZQOZBWED3A_jXvrOUlMCrsaPOuD3fM4a2JyuN1s0nQLRQE0qTW2szRAzwMd1zET6zwJEGTQnvLERqriK7VU7aw6CozSDbZ72YXktIWyLNaUZVWx-vW_ZLuQ7TeykcrVgSJkENoIOwjrNZ9HxqpwJy5cWAM_OkjSuAStXH0WwK0f8CWE3-w6KhTWRMzxr76U3xRLnWbOUY9u8ZeSMT7lqGSHg5UeS0OD5_gO8IuoEhkCAAA)

```
<script>
	let a = $state(1);
	let b = $state(2);

	async function add(a, b) {
		await new Promise((f) => setTimeout(f, 500)); // artificial delay
		return a + b;
	}
</script>

<button onclick={() => a++}>a++</button>
<button onclick={() => b++}>b++</button>

<p>{a} + {b} = {await add(a, b)}</p>

{#if $effect.pending()}
	<p>pending promises: {$effect.pending()}</p>
{/if}
```

```
<script lang="ts">
	let a = $state(1);
	let b = $state(2);

	async function add(a, b) {
		await new Promise((f) => setTimeout(f, 500)); // artificial delay
		return a + b;
	}
</script>

<button onclick={() => a++}>a++</button>
<button onclick={() => b++}>b++</button>

<p>{a} + {b} = {await add(a, b)}</p>

{#if $effect.pending()}
	<p>pending promises: {$effect.pending()}</p>
{/if}
```

## $effect.root[](#$effect.root)

The `$effect.root` rune is an advanced feature that creates a non-tracked scope that doesn't auto-cleanup. This is useful for nested effects that you want to manually control. This rune also allows for the creation of effects outside of the component initialisation phase.

```
const const destroy: () => voiddestroy = namespace $effect
function $effect(fn: () => void | (() => void)): voidRuns code when a component is mounted to the DOM, and then whenever its dependencies change, i.e. $state or $derived values.
The timing of the execution is after the DOM has been updated.
Example:
$effect(() => console.log('The count is now ' + count));If you return a function from the effect, it will be called right before the effect is run again, or when the component is unmounted.
Does not run during server-side rendering.
@see{@link https://svelte.dev/docs/svelte/$effect Documentation}@paramfn The function to execute$effect.function $effect.root(fn: () => void | (() => void)): () => voidThe $effect.root rune is an advanced feature that creates a non-tracked scope that doesn't auto-cleanup. This is useful for
nested effects that you want to manually control. This rune also allows for creation of effects outside of the component
initialisation phase.
Example:
<script>
  let count = $state(0);

  const cleanup = $effect.root(() => {
	$effect(() => {
	  console.log(count);
	})

	return () => {
	  console.log('effect root cleanup');
	}
  });
</script>

<button onclick={() => cleanup()}>cleanup</button>@see{@link https://svelte.dev/docs/svelte/$effect#$effect.root Documentation}root(() => {
	function $effect(fn: () => void | (() => void)): void
namespace $effectRuns code when a component is mounted to the DOM, and then whenever its dependencies change, i.e. $state or $derived values.
The timing of the execution is after the DOM has been updated.
Example:
$effect(() => console.log('The count is now ' + count));If you return a function from the effect, it will be called right before the effect is run again, or when the component is unmounted.
Does not run during server-side rendering.
@see{@link https://svelte.dev/docs/svelte/$effect Documentation}@paramfn The function to execute$effect(() => {
		// setup
	});

	return () => {
		// cleanup
	};
});

// later...
const destroy: () => voiddestroy();
```

## When not to use $effect[](#When-not-to-use-$effect)

In general, `$effect` is best considered something of an escape hatch — useful for things like analytics and direct DOM manipulation — rather than a tool you should use frequently. In particular, avoid using it to synchronise state. Instead of this...

```
<script>
	let count = $state(0);
	let doubled = $state();

	// don't do this!
	$effect(() => {
		doubled = count * 2;
	});
</script>
```

...do this:

```
<script>
	let count = $state(0);
	let doubled = $derived(count * 2);
</script>
```

> For things that are more complicated than a simple expression like `count * 2`, you can also use `$derived.by`.

If you're using an effect because you want to be able to reassign the derived value (to build an optimistic UI, for example) note that [deriveds can be directly overridden]($derived#Overriding-derived-values) as of Svelte 5.25.

You might be tempted to do something convoluted with effects to link one value to another. The following example shows two inputs for "money spent" and "money left" that are connected to each other. If you update one, the other should update accordingly. Instead of using effects for this...

[Open in playground](/playground/untitled#H4sIAAAAAAAAA5VSQWrDQAz8iioCdcBN3EMvGzvQN_RY97Cx5XRhIy9ZJU0w_nuxHCelhEKPmtHMSEIdst0RGnwjEcdbiGKFwDFQ01AlEZK65UeBugX5dPFhjik2zlNE897hxka6GLyGsIhH8kKYYtWyEEtEg3ms9i7IuuRSqpajgLRiPRTwnGWrAfUkEAOxQAEzzU-y-ZXx1PwgVKsklzIbZ0ySORRr6AZo0Gj_GPI0GqtZ_6dsGmDSDTY3Wb68bcG5txvyulDuOBwE5ByoKHFveUslwsZxbY7WH6jo1LeHnT0VnXr3sFTphVlOqJZD0tX9f0HDwHdzlLjGDNWvlChnT9qr4HSR2sXg7dlA4-m0GrGtDQayxQvtxtvoZVSOKd57BKGToJH9gVIchkej34P9R4pinf9yXKNprI_UfwOoIBNKjAIAAA)

```
<script>
	const total = 100;
	let spent = $state(0);
	let left = $state(total);

	$effect(() => {
		left = total - spent;
	});

	$effect(() => {
		spent = total - left;
	});
</script>

<label>
	<input type="range" bind:value={spent} max={total} />
	{spent}/{total} spent
</label>

<label>
	<input type="range" bind:value={left} max={total} />
	{left}/{total} left
</label>

<style>
	label {
		display: flex;
		gap: 0.5em;
	}
</style>
```

```
<script lang="ts">
	const total = 100;
	let spent = $state(0);
	let left = $state(total);

	$effect(() => {
		left = total - spent;
	});

	$effect(() => {
		spent = total - left;
	});
</script>

<label>
	<input type="range" bind:value={spent} max={total} />
	{spent}/{total} spent
</label>

<label>
	<input type="range" bind:value={left} max={total} />
	{left}/{total} left
</label>

<style>
	label {
		display: flex;
		gap: 0.5em;
	}
</style>
```

...use `oninput` callbacks or — better still — [function bindings](bind#Function-bindings) where possible:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA5VSu27DMAz8FYLo4ABu4g5dFDtA9m4d6w6KTbsCFFqw6Dxg-N8LKXESFFk68o7HO1IakfWeUOEniRhuwYsWgqORH2gGrsR0DDvDteHWY4qNseRRfY24056u2q1zS38gK4QpVh0LsXhUmPuqN042JZdSdewFpBNtoYC3LFsH1JKAd8QCBbxE6yRb3BhLTSRq6s2B6uSifr0oYhuXcks5uFoLfVAjSRAuYAx0KfP8WR3IaDGVnK_uETm3ekc2ps0Nu0FAzo6KEnvNLZUY76AO2g5UjHHqBHt9KsY4eYJVlF6Z1YzGMjjdpv_PKFlAsYmh04cVnzqHprtxqP74ejlbir0RnC9UG--sPitoLJ3WF6zVTkG2fKf9w62iHFN89u5CJ0El_UAphnVQxc-C03eKoo09Gq5RNdp6mn4B47i_z3YCAAA)

```
<script>
	const total = 100;
	let spent = $state(0);
	let left = $derived(total - spent);

	function updateLeft(left) {
		spent = total - left;
	}
</script>

<label>
	<input type="range" bind:value={spent} max={total} />
	{spent}/{total} spent
</label>

<label>
	<input type="range" bind:value={() => left, updateLeft} max={total} />
	{left}/{total} left
</label>

<style>
	label {
		display: flex;
		gap: 0.5em;
	}
</style>
```

```
<script lang="ts">
	const total = 100;
	let spent = $state(0);
	let left = $derived(total - spent);

	function updateLeft(left) {
		spent = total - left;
	}
</script>

<label>
	<input type="range" bind:value={spent} max={total} />
	{spent}/{total} spent
</label>

<label>
	<input type="range" bind:value={() => left, updateLeft} max={total} />
	{left}/{total} left
</label>

<style>
	label {
		display: flex;
		gap: 0.5em;
	}
</style>
```

If you absolutely have to update `$state` within an effect and run into an infinite loop because you read and write to the same `$state`, use [untrack](svelte#untrack).

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/02-runes/04-$effect.md) [llms.txt](/docs/svelte/$effect/llms.txt)

previous next

[$derived](/docs/svelte/$derived) [$props](/docs/svelte/$props)


