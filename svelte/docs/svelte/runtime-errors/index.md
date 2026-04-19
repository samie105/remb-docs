---
title: "Runtime errors"
source: "https://svelte.dev/docs/svelte/runtime-errors"
canonical_url: "https://svelte.dev/docs/svelte/runtime-errors"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:29.163Z"
content_hash: "894efc62a5f838242e58f855663979cd3d2980d164090386f1e40b75fdc7cbbc"
menu_path: ["Runtime errors"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/compiler-warnings/index.md", "title": "Compiler warnings"}
nav_next: {"path": "svelte/docs/svelte/runtime-warnings/index.md", "title": "Runtime warnings"}
---

## Client errors[](#Client-errors)

### async\_derived\_orphan[](#Client-errors-async_derived_orphan)

```
Cannot create a `$derived(...)` with an `await` expression outside of an effect tree
```

In Svelte there are two types of reaction — [`$derived`](/docs/svelte/$derived) and [`$effect`](/docs/svelte/$effect). Deriveds can be created anywhere, because they run _lazily_ and can be [garbage collected](https://developer.mozilla.org/en-US/docs/Glossary/Garbage_collection) if nothing references them. Effects, by contrast, keep running eagerly whenever their dependencies change, until they are destroyed.

Because of this, effects can only be created inside other effects (or [effect roots](/docs/svelte/$effect#$effect.root), such as the one that is created when you first mount a component) so that Svelte knows when to destroy them.

Some sleight of hand occurs when a derived contains an `await` expression: Since waiting until we read `{await getPromise()}` to call `getPromise` would be too late, we use an effect to instead call it proactively, notifying Svelte when the value is available. But since we're using an effect, we can only create asynchronous deriveds inside another effect.

### bind\_invalid\_checkbox\_value[](#Client-errors-bind_invalid_checkbox_value)

```
Using `bind:value` together with a checkbox input is not allowed. Use `bind:checked` instead
```

### bind\_invalid\_export[](#Client-errors-bind_invalid_export)

```
Component %component% has an export named `%key%` that a consumer component is trying to access using `bind:%key%`, which is disallowed. Instead, use `bind:this` (e.g. `<%name% bind:this={component} />`) and then access the property on the bound component instance (e.g. `component.%key%`)
```

### bind\_not\_bindable[](#Client-errors-bind_not_bindable)

```
A component is attempting to bind to a non-bindable property `%key%` belonging to %component% (i.e. `<%name% bind:%key%={...}>`). To mark a property as bindable: `let { %key% = $bindable() } = $props()`
```

### component\_api\_changed[](#Client-errors-component_api_changed)

```
Calling `%method%` on a component instance (of %component%) is no longer valid in Svelte 5
```

See the [migration guide](/docs/svelte/v5-migration-guide#Components-are-no-longer-classes) for more information.

### component\_api\_invalid\_new[](#Client-errors-component_api_invalid_new)

```
Attempted to instantiate %component% with `new %name%`, which is no longer valid in Svelte 5. If this component is not under your control, set the `compatibility.componentApi` compiler option to `4` to keep it working.
```

See the [migration guide](/docs/svelte/v5-migration-guide#Components-are-no-longer-classes) for more information.

### derived\_references\_self[](#Client-errors-derived_references_self)

```
A derived value cannot reference itself recursively
```

### each\_key\_duplicate[](#Client-errors-each_key_duplicate)

```
Keyed each block has duplicate key at indexes %a% and %b%
```

```
Keyed each block has duplicate key `%value%` at indexes %a% and %b%
```

### each\_key\_volatile[](#Client-errors-each_key_volatile)

```
Keyed each block has key that is not idempotent — the key for item at index %index% was `%a%` but is now `%b%`. Keys must be the same each time for a given item
```

The key expression in a keyed each block must return the same value when called multiple times for the same item. Using expressions like `[item.a, item.b]` creates a new array each time, which will never be equal to itself. Instead, use a primitive value or create a stable key like `item.a + '-' + item.b`.

### effect\_in\_teardown[](#Client-errors-effect_in_teardown)

```
`%rune%` cannot be used inside an effect cleanup function
```

### effect\_in\_unowned\_derived[](#Client-errors-effect_in_unowned_derived)

```
Effect cannot be created inside a `$derived` value that was not itself created inside an effect
```

### effect\_orphan[](#Client-errors-effect_orphan)

```
`%rune%` can only be used inside an effect (e.g. during component initialisation)
```

### effect\_pending\_outside\_reaction[](#Client-errors-effect_pending_outside_reaction)

```
`$effect.pending()` can only be called inside an effect or derived
```

### effect\_update\_depth\_exceeded[](#Client-errors-effect_update_depth_exceeded)

```
Maximum update depth exceeded. This typically indicates that an effect reads and writes the same piece of state
```

If an effect updates some state that it also depends on, it will re-run, potentially in a loop:

```
let let count: numbercount = function $state<0>(initial: 0): 0 (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state(0);

function $effect(fn: () => void | (() => void)): void
namespace $effectRuns code when a component is mounted to the DOM, and then whenever its dependencies change, i.e. $state or $derived values.
The timing of the execution is after the DOM has been updated.
Example:
$effect(() => console.log('The count is now ' + count));If you return a function from the effect, it will be called right before the effect is run again, or when the component is unmounted.
Does not run during server-side rendering.
@see{@link https://svelte.dev/docs/svelte/$effect Documentation}@paramfn The function to execute$effect(() => {
	// this both reads and writes `count`,
	// so will run in an infinite loop
	let count: numbercount += 1;
});
```

(Svelte intervenes before this can crash your browser tab.)

The same applies to array mutations, since these both read and write to the array:

```
let let array: string[]array = function $state<string[]>(initial: string[]): string[] (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state(['hello']);

function $effect(fn: () => void | (() => void)): void
namespace $effectRuns code when a component is mounted to the DOM, and then whenever its dependencies change, i.e. $state or $derived values.
The timing of the execution is after the DOM has been updated.
Example:
$effect(() => console.log('The count is now ' + count));If you return a function from the effect, it will be called right before the effect is run again, or when the component is unmounted.
Does not run during server-side rendering.
@see{@link https://svelte.dev/docs/svelte/$effect Documentation}@paramfn The function to execute$effect(() => {
	let array: string[]array.Array<string>.push(...items: string[]): numberAppends new elements to the end of an array, and returns the new length of the array.
@paramitems New elements to add to the array.push('goodbye');
});
```

Note that it's fine for an effect to re-run itself as long as it 'settles':

```
function $effect(fn: () => void | (() => void)): void
namespace $effectRuns code when a component is mounted to the DOM, and then whenever its dependencies change, i.e. $state or $derived values.
The timing of the execution is after the DOM has been updated.
Example:
$effect(() => console.log('The count is now ' + count));If you return a function from the effect, it will be called right before the effect is run again, or when the component is unmounted.
Does not run during server-side rendering.
@see{@link https://svelte.dev/docs/svelte/$effect Documentation}@paramfn The function to execute$effect(() => {
	// this is okay, because sorting an already-sorted array
	// won't result in a mutation
	let array: string[]array.Array<string>.sort(compareFn?: ((a: string, b: string) => number) | undefined): string[]Sorts an array in place.
This method mutates the array and returns a reference to the same array.
@paramcompareFn Function used to determine the order of the elements. It is expected to return
a negative value if the first argument is less than the second argument, zero if they're equal, and a positive
value otherwise. If omitted, the elements are sorted in ascending, UTF-16 code unit order.
ts [11,2,22,1].sort((a, b) => a - b) sort();
});
```

Often when encountering this issue, the value in question shouldn't be state (for example, if you are pushing to a `logs` array in an effect, make `logs` a normal array rather than `$state([])`). In the rare cases where you really _do_ need to write to state in an effect — [which you should avoid]($effect#When-not-to-use-$effect) — you can read the state with [untrack](svelte#untrack) to avoid adding it as a dependency.

### flush\_sync\_in\_effect[](#Client-errors-flush_sync_in_effect)

```
Cannot use `flushSync` inside an effect
```

The `flushSync()` function can be used to flush any pending effects synchronously. It cannot be used if effects are currently being flushed — in other words, you can call it after a state change but _not_ inside an effect.

This restriction only applies when using the `experimental.async` option, which will be active by default in Svelte 6.

### fork\_discarded[](#Client-errors-fork_discarded)

```
Cannot commit a fork that was already discarded
```

### fork\_timing[](#Client-errors-fork_timing)

```
Cannot create a fork inside an effect or when state changes are pending
```

### get\_abort\_signal\_outside\_reaction[](#Client-errors-get_abort_signal_outside_reaction)

```
`getAbortSignal()` can only be called inside an effect or derived
```

### hydratable\_missing\_but\_required[](#Client-errors-hydratable_missing_but_required)

```
Expected to find a hydratable with key `%key%` during hydration, but did not.
```

This can happen if you render a hydratable on the client that was not rendered on the server, and means that it was forced to fall back to running its function blockingly during hydration. This is bad for performance, as it blocks hydration until the asynchronous work completes.

```
<script>
  import { hydratable } from 'svelte';

	if (BROWSER) {
		// bad! nothing can become interactive until this asynchronous work is done
		await hydratable('foo', get_slow_random_number);
	}
</script>
```

### hydration\_failed[](#Client-errors-hydration_failed)

```
Failed to hydrate the application
```

### invalid\_snippet[](#Client-errors-invalid_snippet)

```
Could not `{@render}` snippet due to the expression being `null` or `undefined`. Consider using optional chaining `{@render snippet?.()}`
```

### lifecycle\_legacy\_only[](#Client-errors-lifecycle_legacy_only)

```
`%name%(...)` cannot be used in runes mode
```

### props\_invalid\_value[](#Client-errors-props_invalid_value)

```
Cannot do `bind:%key%={undefined}` when `%key%` has a fallback value
```

### props\_rest\_readonly[](#Client-errors-props_rest_readonly)

```
Rest element properties of `$props()` such as `%property%` are readonly
```

### rune\_outside\_svelte[](#Client-errors-rune_outside_svelte)

```
The `%rune%` rune is only available inside `.svelte` and `.svelte.js/ts` files
```

### set\_context\_after\_init[](#Client-errors-set_context_after_init)

```
`setContext` must be called when a component first initializes, not in a subsequent effect or after an `await` expression
```

This restriction only applies when using the `experimental.async` option, which will be active by default in Svelte 6.

### state\_descriptors\_fixed[](#Client-errors-state_descriptors_fixed)

```
Property descriptors defined on `$state` objects must contain `value` and always be `enumerable`, `configurable` and `writable`.
```

### state\_prototype\_fixed[](#Client-errors-state_prototype_fixed)

```
Cannot set prototype of `$state` object
```

### state\_unsafe\_mutation[](#Client-errors-state_unsafe_mutation)

```
Updating state inside `$derived(...)`, `$inspect(...)` or a template expression is forbidden. If the value should not be reactive, declare it without `$state`
```

This error occurs when state is updated while evaluating a `$derived`. You might encounter it while trying to 'derive' two pieces of state in one go:

```
<script>
	let count = $state(0);

	let even = $state(true);

	let odd = $derived.by(() => {
		even = count % 2 === 0;
		return !even;
	});
</script>

<button onclick={() => count++}>{count}</button>

<p>{count} is even: {even}</p>
<p>{count} is odd: {odd}</p>
```

This is forbidden because it introduces instability: if `<p>{count} is even: {even}</p>` is updated before `odd` is recalculated, `even` will be stale. In most cases the solution is to make everything derived:

```
let let even: booleaneven = function $derived<boolean>(expression: boolean): boolean
namespace $derivedDeclares derived state, i.e. one that depends on other state variables.
The expression inside $derived(...) should be free of side-effects.
Example:
let double = $derived(count * 2);@see{@link https://svelte.dev/docs/svelte/$derived Documentation}@paramexpression The derived state expression$derived(let count: numbercount % 2 === 0);
let let odd: booleanodd = function $derived<boolean>(expression: boolean): boolean
namespace $derivedDeclares derived state, i.e. one that depends on other state variables.
The expression inside $derived(...) should be free of side-effects.
Example:
let double = $derived(count * 2);@see{@link https://svelte.dev/docs/svelte/$derived Documentation}@paramexpression The derived state expression$derived(!let even: booleaneven);
```

If side-effects are unavoidable, use [`$effect`]($effect) instead.

### svelte\_boundary\_reset\_onerror[](#Client-errors-svelte_boundary_reset_onerror)

```
A `<svelte:boundary>` `reset` function cannot be called while an error is still being handled
```

If a [`<svelte:boundary>`](svelte/docs/svelte/svelte-boundary/index.md) has an `onerror` function, it must not call the provided `reset` function synchronously since the boundary is still in a broken state. Typically, `reset()` is called later, once the error has been resolved.

If it's possible to resolve the error inside the `onerror` callback, you must at least wait for the boundary to settle before calling `reset()`, for example using [`tick`](svelte/docs/svelte/lifecycle-hooks/index.md#tick):

```
<svelte:boundary onerror={async (error, reset) => {
	fixTheError();
	await tick();
	reset();
}}>

</svelte:boundary>
```

## Server errors[](#Server-errors)

### async\_local\_storage\_unavailable[](#Server-errors-async_local_storage_unavailable)

```
The node API `AsyncLocalStorage` is not available, but is required to use async server rendering.
```

Some platforms require configuration flags to enable this API. Consult your platform's documentation.

### await\_invalid[](#Server-errors-await_invalid)

```
Encountered asynchronous work while rendering synchronously.
```

You (or the framework you're using) called [`render(...)`](svelte-server#render) with a component containing an `await` expression. Either `await` the result of `render` or wrap the `await` (or the component containing it) in a [`<svelte:boundary>`](svelte-boundary) with a `pending` snippet.

### dynamic\_element\_invalid\_tag[](#Server-errors-dynamic_element_invalid_tag)

```
`<svelte:element this="%tag%">` is not a valid element name — the element will not be rendered
```

The value passed to the `this` prop of `<svelte:element>` must be a valid HTML element, SVG element, MathML element, or custom element name. A value containing invalid characters (such as whitespace or special characters) was provided, which could be a security risk. Ensure only valid tag names are passed.

### html\_deprecated[](#Server-errors-html_deprecated)

```
The `html` property of server render results has been deprecated. Use `body` instead.
```

### hydratable\_clobbering[](#Server-errors-hydratable_clobbering)

```
Attempted to set `hydratable` with key `%key%` twice with different values.

%stack%
```

This error occurs when using `hydratable` multiple times with the same key. To avoid this, you can:

*   Ensure all invocations with the same key result in the same value
*   Update the keys to make both instances unique

```
<script>
  import { hydratable } from 'svelte';

  // which one should "win" and be serialized in the rendered response?
  const one = hydratable('not-unique', () => 1);
  const two = hydratable('not-unique', () => 2);
</script>
```

### hydratable\_serialization\_failed[](#Server-errors-hydratable_serialization_failed)

```
Failed to serialize `hydratable` data for key `%key%`.

`hydratable` can serialize anything [`uneval` from `devalue`](https://npmjs.com/package/uneval) can, plus Promises.

Cause:
%stack%
```

### invalid\_csp[](#Server-errors-invalid_csp)

```
`csp.nonce` was set while `csp.hash` was `true`. These options cannot be used simultaneously.
```

### invalid\_id\_prefix[](#Server-errors-invalid_id_prefix)

```
The `idPrefix` option cannot include `--`.
```

### lifecycle\_function\_unavailable[](#Server-errors-lifecycle_function_unavailable)

```
`%name%(...)` is not available on the server
```

Certain methods such as `mount` cannot be invoked while running in a server context. Avoid calling them eagerly, i.e. not during render.

### server\_context\_required[](#Server-errors-server_context_required)

```
Could not resolve `render` context.
```

Certain functions such as `hydratable` cannot be invoked outside of a `render(...)` call, such as at the top level of a module.

## Shared errors[](#Shared-errors)

### experimental\_async\_required[](#Shared-errors-experimental_async_required)

```
Cannot use `%name%(...)` unless the `experimental.async` compiler option is `true`
```

### invalid\_default\_snippet[](#Shared-errors-invalid_default_snippet)

```
Cannot use `{@render children(...)}` if the parent component uses `let:` directives. Consider using a named snippet instead
```

This error would be thrown in a setup like this:

Parent

```
<List {items} let:entry>
	<span>{entry}</span>
</List>
```

List

```
<script>
	let { items, children } = $props();
</script>

<ul>
	{#each items as item}
		<li>{@render children(item)}</li>
	{/each}
</ul>
```

```
<script lang="ts">
	let { items, children } = $props();
</script>

<ul>
	{#each items as item}
		<li>{@render children(item)}</li>
	{/each}
</ul>
```

Here, `List.svelte` is using `{@render children(item)` which means it expects `Parent.svelte` to use snippets. Instead, `Parent.svelte` uses the deprecated `let:` directive. This combination of APIs is incompatible, hence the error.

### invalid\_snippet\_arguments[](#Shared-errors-invalid_snippet_arguments)

```
A snippet function was passed invalid arguments. Snippets should only be instantiated via `{@render ...}`
```

### invariant\_violation[](#Shared-errors-invariant_violation)

```
An invariant violation occurred, meaning Svelte's internal assumptions were flawed. This is a bug in Svelte, not your app — please open an issue at https://github.com/sveltejs/svelte, citing the following message: "%message%"
```

### lifecycle\_outside\_component[](#Shared-errors-lifecycle_outside_component)

```
`%name%(...)` can only be used during component initialisation
```

Certain lifecycle methods can only be used during component initialisation. To fix this, make sure you're invoking the method inside the _top level of the instance script_ of your component.

```
<script>
	import { onMount } from 'svelte';

	function handleClick() {
		// This is wrong
		onMount(() => {})
	}

	// This is correct
	onMount(() => {})
</script>

<button onclick={handleClick}>click me</button>
```

### missing\_context[](#Shared-errors-missing_context)

```
Context was not set in a parent component
```

The [`createContext()`](svelte#createContext) utility returns a `[get, set]` pair of functions. `get` will throw an error if `set` was not used to set the context in a parent component.

### snippet\_without\_render\_tag[](#Shared-errors-snippet_without_render_tag)

```
Attempted to render a snippet without a `{@render}` block. This would cause the snippet code to be stringified instead of its content being rendered to the DOM. To fix this, change `{snippet}` to `{@render snippet()}`.
```

A component throwing this error will look something like this (`children` is not being rendered):

```
<script>
	let { children } = $props();
</script>

{children}
```

...or like this (a parent component is passing a snippet where a non-snippet value is expected):

Parent

```
<ChildComponent>
  {#snippet label()}
	<span>Hi!</span>
  {/snippet}
</ChildComponent>
```

Child

```
<script>
  let { label } = $props();
</script>

<!-- This component doesn't expect a snippet, but the parent provided one -->
<p>{label}</p>
```

```
<script lang="ts">
  let { label } = $props();
</script>

<!-- This component doesn't expect a snippet, but the parent provided one -->
<p>{label}</p>
```

### store\_invalid\_shape[](#Shared-errors-store_invalid_shape)

```
`%name%` is not a store with a `subscribe` method
```

### svelte\_element\_invalid\_this\_value[](#Shared-errors-svelte_element_invalid_this_value)

```
The `this` prop on `<svelte:element>` must be a string, if defined
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/98-reference/30-runtime-errors.md) [llms.txt](/docs/svelte/runtime-errors/llms.txt)

previous next

[Compiler warnings](/docs/svelte/compiler-warnings) [Runtime warnings](/docs/svelte/runtime-warnings)
