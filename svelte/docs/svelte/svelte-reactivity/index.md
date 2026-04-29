---
title: "svelte/reactivity"
source: "https://svelte.dev/docs/svelte/svelte-reactivity"
canonical_url: "https://svelte.dev/docs/svelte/svelte-reactivity"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:19.280Z"
content_hash: "0b6830adadbb185127895a570a3ab656f7424352fc56bd8d9ea78aba3e32fbe0"
menu_path: ["svelte/reactivity"]
section_path: []
nav_prev: {"path": "../svelte-reactivity-window/index.md", "title": "svelte/reactivity/window"}
nav_next: {"path": "../svelte-server/index.md", "title": "svelte/server"}
---

Svelte provides reactive versions of various built-ins like [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map), [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) and [`URL`](https://developer.mozilla.org/en-US/docs/Web/API/URL) that can be used just like their native counterparts, as well as a handful of additional utilities for handling reactivity.

```
import {
	class MediaQueryCreates a media query and provides a current property that reflects whether or not it matches.
Use it carefully — during server-side rendering, there is no way to know what the correct value should be, potentially causing content to change upon hydration.
If you can use the media query in CSS to achieve the same effect, do that.
<script>
	import { MediaQuery } from 'svelte/reactivity';

	const large = new MediaQuery('min-width: 800px');
</script>

<h1>{large.current ? 'large screen' : 'small screen'}</h1>@extendsReactiveValue<boolean> *@since5.7.0referenceMediaQuery,
	class SvelteDateA reactive version of the built-in Date object.
Reading the date (whether with methods like date.getTime() or date.toString(), or via things like Intl.DateTimeFormat)
in an effect or derived
will cause it to be re-evaluated when the value of the date changes.
<script>
	import { SvelteDate } from 'svelte/reactivity';

	const date = new SvelteDate();

	const formatter = new Intl.DateTimeFormat(undefined, {
	  hour: 'numeric',
	  minute: 'numeric',
	  second: 'numeric'
	});

	$effect(() => {
		const interval = setInterval(() => {
			date.setTime(Date.now());
		}, 1000);

		return () => {
			clearInterval(interval);
		};
	});
</script>

<p>The time is {formatter.format(date)}</p>referenceSvelteDate,
	class SvelteMap<K, V>A reactive version of the built-in Map object.
Reading contents of the map (by iterating, or by reading map.size or calling map.get(...) or map.has(...) as in the tic-tac-toe example below) in an effect or derived
will cause it to be re-evaluated as necessary when the map is updated.
Note that values in a reactive map are not made deeply reactive.
<script>
	import { SvelteMap } from 'svelte/reactivity';
	import { result } from './game.js';

	let board = new SvelteMap();
	let player = $state('x');
	let winner = $derived(result(board));

	function reset() {
		player = 'x';
		board.clear();
	}
</script>

<div class="board">
	{#each Array(9), i}
		<button
			disabled={board.has(i) || winner}
			onclick={() => {
				board.set(i, player);
				player = player === 'x' ? 'o' : 'x';
			}}
		>{board.get(i)}</button>
	{/each}
</div>

{#if winner}
	<p>{winner} wins!</p>
	<button onclick={reset}>reset</button>
{:else}
	<p>{player} is next</p>
{/if}referenceSvelteMap,
	class SvelteSet<T>A reactive version of the built-in Set object.
Reading contents of the set (by iterating, or by reading set.size or calling set.has(...) as in the example below) in an effect or derived
will cause it to be re-evaluated as necessary when the set is updated.
Note that values in a reactive set are not made deeply reactive.
<script>
	import { SvelteSet } from 'svelte/reactivity';
	let monkeys = new SvelteSet();

	function toggle(monkey) {
		if (monkeys.has(monkey)) {
			monkeys.delete(monkey);
		} else {
			monkeys.add(monkey);
		}
	}
</script>

{#each ['🙈', '🙉', '🙊'] as monkey}
	<button onclick={() => toggle(monkey)}>{monkey}</button>
{/each}

<button onclick={() => monkeys.clear()}>clear</button>

{#if monkeys.has('🙈')}<p>see no evil</p>{/if}
{#if monkeys.has('🙉')}<p>hear no evil</p>{/if}
{#if monkeys.has('🙊')}<p>speak no evil</p>{/if}referenceSvelteSet,
	class SvelteURLA reactive version of the built-in URL object.
Reading properties of the URL (such as url.href or url.pathname) in an effect or derived
will cause it to be re-evaluated as necessary when the URL changes.
The searchParams property is an instance of SvelteURLSearchParams.
Example:
<script>
	import { SvelteURL } from 'svelte/reactivity';

	const url = new SvelteURL('https://example.com/path');
</script>

<!-- changes to these... -->
<input bind:value={url.protocol} />
<input bind:value={url.hostname} />
<input bind:value={url.pathname} />

<hr />

<!-- will update `href` and vice versa -->
<input bind:value={url.href} size="65" />referenceSvelteURL,
	class SvelteURLSearchParamsA reactive version of the built-in URLSearchParams object.
Reading its contents (by iterating, or by calling params.get(...) or params.getAll(...) as in the example below) in an effect or derived
will cause it to be re-evaluated as necessary when the params are updated.
<script>
	import { SvelteURLSearchParams } from 'svelte/reactivity';

	const params = new SvelteURLSearchParams('message=hello');

	let key = $state('key');
	let value = $state('value');
</script>

<input bind:value={key} />
<input bind:value={value} />
<button onclick={() => params.append(key, value)}>append</button>

<p>?{params.toString()}</p>

{#each params as [key, value]}
	<p>{key}: {value}</p>
{/each}referenceSvelteURLSearchParams,
	function createSubscriber(start: (update: () => void) => (() => void) | void): () => voidReturns a subscribe function that integrates external event-based systems with Svelte's reactivity.
It's particularly useful for integrating with web APIs like MediaQuery, IntersectionObserver, or WebSocket.
If subscribe is called inside an effect (including indirectly, for example inside a getter),
the start callback will be called with an update function. Whenever update is called, the effect re-runs.
If start returns a cleanup function, it will be called when the effect is destroyed.
If subscribe is called in multiple effects, start will only be called once as long as the effects
are active, and the returned teardown function will only be called when all effects are destroyed.
It's best understood with an example. Here's an implementation of MediaQuery:
import { createSubscriber } from 'svelte/reactivity';
import { on } from 'svelte/events';

export class MediaQuery {
	#query;
	#subscribe;

	constructor(query) {
		this.#query = window.matchMedia(`(${query})`);

		this.#subscribe = createSubscriber((update) => {
			// when the `change` event occurs, re-run any effects that read `this.current`
			const off = on(this.#query, 'change', update);

			// stop listening when all the effects are destroyed
			return () => off();
		});
	}

	get current() {
		// This makes the getter reactive, if read in an effect
		this.#subscribe();

		// Return the current state of the query, whether or not we're in an effect
		return this.#query.matches;
	}
}@since5.7.0referencecreateSubscriber
} from 'svelte/reactivity';
```

## MediaQuery[](#MediaQuery)

> Available since 5.7.0

Creates a media query and provides a `current` property that reflects whether or not it matches.

Use it carefully — during server-side rendering, there is no way to know what the correct value should be, potentially causing content to change upon hydration. If you can use the media query in CSS to achieve the same effect, do that.

```
<script>
	import { MediaQuery } from 'svelte/reactivity';

	const large = new MediaQuery('min-width: 800px');
</script>

<h1>{large.current ? 'large screen' : 'small screen'}</h1>
```

```
class MediaQuery extends ReactiveValue<boolean> {…}
```

```
constructor(query: string, fallback?: boolean | undefined);
```

*   `query` A media query string
*   `fallback` Fallback value for the server

## SvelteDate[](#SvelteDate)

A reactive version of the built-in [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) object. Reading the date (whether with methods like `date.getTime()` or `date.toString()`, or via things like [`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)) in an [effect](/docs/svelte/$effect) or [derived](/docs/svelte/$derived) will cause it to be re-evaluated when the value of the date changes.

```
<script>
	import { SvelteDate } from 'svelte/reactivity';

	const date = new SvelteDate();

	const formatter = new Intl.DateTimeFormat(undefined, {
	  hour: 'numeric',
	  minute: 'numeric',
	  second: 'numeric'
	});

	$effect(() => {
		const interval = setInterval(() => {
			date.setTime(Date.now());
		}, 1000);

		return () => {
			clearInterval(interval);
		};
	});
</script>

<p>The time is {formatter.format(date)}</p>
```

```
class SvelteDate extends Date {…}
```

```
constructor(...params: any[]);
```

## SvelteMap[](#SvelteMap)

A reactive version of the built-in [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) object. Reading contents of the map (by iterating, or by reading `map.size` or calling `map.get(...)` or `map.has(...)` as in the [tic-tac-toe example](/playground/0b0ff4aa49c9443f9b47fe5203c78293) below) in an [effect](/docs/svelte/$effect) or [derived](/docs/svelte/$derived) will cause it to be re-evaluated as necessary when the map is updated.

Note that values in a reactive map are _not_ made [deeply reactive](/docs/svelte/$state#Deep-state).

```
<script>
	import { SvelteMap } from 'svelte/reactivity';
	import { result } from './game.js';

	let board = new SvelteMap();
	let player = $state('x');
	let winner = $derived(result(board));

	function reset() {
		player = 'x';
		board.clear();
	}
</script>

<div class="board">
	{#each Array(9), i}
		<button
			disabled={board.has(i) || winner}
			onclick={() => {
				board.set(i, player);
				player = player === 'x' ? 'o' : 'x';
			}}
		>{board.get(i)}</button>
	{/each}
</div>

{#if winner}
	<p>{winner} wins!</p>
	<button onclick={reset}>reset</button>
{:else}
	<p>{player} is next</p>
{/if}
```

```
class SvelteMap<K, V> extends Map<K, V> {…}
```

```
constructor(value?: Iterable<readonly [K, V]> | null | undefined);
```

```
set(key: K, value: V): this;
```

## SvelteSet[](#SvelteSet)

A reactive version of the built-in [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) object. Reading contents of the set (by iterating, or by reading `set.size` or calling `set.has(...)` as in the [example](/playground/53438b51194b4882bcc18cddf9f96f15) below) in an [effect](/docs/svelte/$effect) or [derived](/docs/svelte/$derived) will cause it to be re-evaluated as necessary when the set is updated.

Note that values in a reactive set are _not_ made [deeply reactive](/docs/svelte/$state#Deep-state).

```
<script>
	import { SvelteSet } from 'svelte/reactivity';
	let monkeys = new SvelteSet();

	function toggle(monkey) {
		if (monkeys.has(monkey)) {
			monkeys.delete(monkey);
		} else {
			monkeys.add(monkey);
		}
	}
</script>

{#each ['🙈', '🙉', '🙊'] as monkey}
	<button onclick={() => toggle(monkey)}>{monkey}</button>
{/each}

<button onclick={() => monkeys.clear()}>clear</button>

{#if monkeys.has('🙈')}<p>see no evil</p>{/if}
{#if monkeys.has('🙉')}<p>hear no evil</p>{/if}
{#if monkeys.has('🙊')}<p>speak no evil</p>{/if}
```

```
class SvelteSet<T> extends Set<T> {…}
```

```
constructor(value?: Iterable<T> | null | undefined);
```

```
add(value: T): this;
```

## SvelteURL[](#SvelteURL)

A reactive version of the built-in [`URL`](https://developer.mozilla.org/en-US/docs/Web/API/URL) object. Reading properties of the URL (such as `url.href` or `url.pathname`) in an [effect](/docs/svelte/$effect) or [derived](/docs/svelte/$derived) will cause it to be re-evaluated as necessary when the URL changes.

The `searchParams` property is an instance of [SvelteURLSearchParams](/docs/svelte/svelte-reactivity#SvelteURLSearchParams).

[Example](/playground/5a694758901b448c83dc40dc31c71f2a):

```
<script>
	import { SvelteURL } from 'svelte/reactivity';

	const url = new SvelteURL('https://example.com/path');
</script>

<!-- changes to these... -->
<input bind:value={url.protocol} />
<input bind:value={url.hostname} />
<input bind:value={url.pathname} />

<hr />

<!-- will update `href` and vice versa -->
<input bind:value={url.href} size="65" />
```

```
class SvelteURL extends URL {…}
```

```
get searchParams(): SvelteURLSearchParams;
```

## SvelteURLSearchParams[](#SvelteURLSearchParams)

A reactive version of the built-in [`URLSearchParams`](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams) object. Reading its contents (by iterating, or by calling `params.get(...)` or `params.getAll(...)` as in the [example](/playground/b3926c86c5384bab9f2cf993bc08c1c8) below) in an [effect](/docs/svelte/$effect) or [derived](/docs/svelte/$derived) will cause it to be re-evaluated as necessary when the params are updated.

```
<script>
	import { SvelteURLSearchParams } from 'svelte/reactivity';

	const params = new SvelteURLSearchParams('message=hello');

	let key = $state('key');
	let value = $state('value');
</script>

<input bind:value={key} />
<input bind:value={value} />
<button onclick={() => params.append(key, value)}>append</button>

<p>?{params.toString()}</p>

{#each params as [key, value]}
	<p>{key}: {value}</p>
{/each}
```

```
class SvelteURLSearchParams extends URLSearchParams {…}
```

```
[REPLACE](params: URLSearchParams): void;
```

## createSubscriber[](#createSubscriber)

> Available since 5.7.0

Returns a `subscribe` function that integrates external event-based systems with Svelte's reactivity. It's particularly useful for integrating with web APIs like `MediaQuery`, `IntersectionObserver`, or `WebSocket`.

If `subscribe` is called inside an effect (including indirectly, for example inside a getter), the `start` callback will be called with an `update` function. Whenever `update` is called, the effect re-runs.

If `start` returns a cleanup function, it will be called when the effect is destroyed.

If `subscribe` is called in multiple effects, `start` will only be called once as long as the effects are active, and the returned teardown function will only be called when all effects are destroyed.

It's best understood with an example. Here's an implementation of [`MediaQuery`](/docs/svelte/svelte-reactivity#MediaQuery):

```
import { function createSubscriber(start: (update: () => void) => (() => void) | void): () => voidReturns a subscribe function that integrates external event-based systems with Svelte's reactivity.
It's particularly useful for integrating with web APIs like MediaQuery, IntersectionObserver, or WebSocket.
If subscribe is called inside an effect (including indirectly, for example inside a getter),
the start callback will be called with an update function. Whenever update is called, the effect re-runs.
If start returns a cleanup function, it will be called when the effect is destroyed.
If subscribe is called in multiple effects, start will only be called once as long as the effects
are active, and the returned teardown function will only be called when all effects are destroyed.
It's best understood with an example. Here's an implementation of MediaQuery:
import { createSubscriber } from 'svelte/reactivity';
import { on } from 'svelte/events';

export class MediaQuery {
	#query;
	#subscribe;

	constructor(query) {
		this.#query = window.matchMedia(`(${query})`);

		this.#subscribe = createSubscriber((update) => {
			// when the `change` event occurs, re-run any effects that read `this.current`
			const off = on(this.#query, 'change', update);

			// stop listening when all the effects are destroyed
			return () => off();
		});
	}

	get current() {
		// This makes the getter reactive, if read in an effect
		this.#subscribe();

		// Return the current state of the query, whether or not we're in an effect
		return this.#query.matches;
	}
}@since5.7.0referencecreateSubscriber } from 'svelte/reactivity';
import { function on<Type extends keyof WindowEventMap>(window: Window, type: Type, handler: (this: Window, event: WindowEventMap[Type] & {
    currentTarget: Window;
}) => any, options?: AddEventListenerOptions | undefined): () => void (+4 overloads)Attaches an event handler to the window and returns a function that removes the handler. Using this
rather than addEventListener will preserve the correct order relative to handlers added declaratively
(with attributes like onclick), which use event delegation for performance reasons
referenceon } from 'svelte/events';

export class class MediaQueryMediaQuery {
	#query;
	#subscribe;

	constructor(query: anyquery) {
		this.#query = var window: Window & typeof globalThisThe window property of a Window object points to the window object itself.
MDN Reference
window.function matchMedia(query: string): MediaQueryListThe Window interface's matchMedia() method returns a new MediaQueryList object that can then be used to determine if the document matches the media query string, as well as to monitor the document to detect when it matches (or stops matching) that media query.
MDN Reference
matchMedia(`(${query: anyquery})`);

		this.#subscribe = function createSubscriber(start: (update: () => void) => (() => void) | void): () => voidReturns a subscribe function that integrates external event-based systems with Svelte's reactivity.
It's particularly useful for integrating with web APIs like MediaQuery, IntersectionObserver, or WebSocket.
If subscribe is called inside an effect (including indirectly, for example inside a getter),
the start callback will be called with an update function. Whenever update is called, the effect re-runs.
If start returns a cleanup function, it will be called when the effect is destroyed.
If subscribe is called in multiple effects, start will only be called once as long as the effects
are active, and the returned teardown function will only be called when all effects are destroyed.
It's best understood with an example. Here's an implementation of MediaQuery:
import { createSubscriber } from 'svelte/reactivity';
import { on } from 'svelte/events';

export class MediaQuery {
	#query;
	#subscribe;

	constructor(query) {
		this.#query = window.matchMedia(`(${query})`);

		this.#subscribe = createSubscriber((update) => {
			// when the `change` event occurs, re-run any effects that read `this.current`
			const off = on(this.#query, 'change', update);

			// stop listening when all the effects are destroyed
			return () => off();
		});
	}

	get current() {
		// This makes the getter reactive, if read in an effect
		this.#subscribe();

		// Return the current state of the query, whether or not we're in an effect
		return this.#query.matches;
	}
}@since5.7.0referencecreateSubscriber((update: () => voidupdate) => {
			// when the `change` event occurs, re-run any effects that read `this.current`
			const const off: () => voidoff = on<MediaQueryList, "change">(element: MediaQueryList, type: "change", handler: (this: MediaQueryList, event: MediaQueryListEvent & {
    currentTarget: MediaQueryList;
}) => any, options?: AddEventListenerOptions | undefined): () => void (+4 overloads)Attaches an event handler to an element and returns a function that removes the handler. Using this
rather than addEventListener will preserve the correct order relative to handlers added declaratively
(with attributes like onclick), which use event delegation for performance reasons
referenceon(this.#query, 'change', update: () => voidupdate);

			// stop listening when all the effects are destroyed
			return () => const off: () => voidoff();
		});
	}

	get MediaQuery.current: booleancurrent() {
		// This makes the getter reactive, if read in an effect
		this.#subscribe();

		// Return the current state of the query, whether or not we're in an effect
		return this.#query.MediaQueryList.matches: booleanThe matches read-only property of the true if the document currently matches the media query list, or false if not.
MDN Reference
matches;
	}
}
```

```
function createSubscriber(
	start: (update: () => void) => (() => void) | void
): () => void;
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/98-reference/21-svelte-reactivity.md) [llms.txt](/docs/svelte/svelte-reactivity/llms.txt)

previous next

[svelte/reactivity/window](/docs/svelte/svelte-reactivity-window) [svelte/server](/docs/svelte/svelte-server)
