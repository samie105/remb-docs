---
title: "svelte/store"
source: "https://svelte.dev/docs/svelte/svelte-store"
canonical_url: "https://svelte.dev/docs/svelte/svelte-store"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:27.741Z"
content_hash: "bd715ae23423dc746074f151f587ddd9fddb52f75e90bebb722578d57e4d0a2a"
menu_path: ["svelte/store"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/svelte-server/index.md", "title": "svelte/server"}
nav_next: {"path": "svelte/docs/svelte/svelte-transition/index.md", "title": "svelte/transition"}
---

```
import {
	function derived<S extends Stores, T>(stores: S, fn: (values: StoresValues<S>, set: (value: T) => void, update: (fn: Updater<T>) => void) => Unsubscriber | void, initial_value?: T | undefined): Readable<T> (+1 overload)Derived value store by synchronizing one or more readable stores and
applying an aggregation function over its input values.
referencederived,
	function fromStore<V>(store: Writable<V>): {
    current: V;
} (+1 overload)referencefromStore,
	function get<T>(store: Readable<T>): TGet the current value from a store by subscribing and immediately unsubscribing.
referenceget,
	function readable<T>(value?: T | undefined, start?: StartStopNotifier<T> | undefined): Readable<T>Creates a Readable store that allows reading by subscription.
@paramvalue initial valuereferencereadable,
	function readonly<T>(store: Readable<T>): Readable<T>Takes a store and returns a new one derived from the old one that is readable.
@paramstore - store to make readonlyreferencereadonly,
	function toStore<V>(get: () => V, set: (v: V) => void): Writable<V> (+1 overload)referencetoStore,
	function writable<T>(value?: T | undefined, start?: StartStopNotifier<T> | undefined): Writable<T>Create a Writable store that allows both updating and reading by subscription.
@paramvalue initial valuereferencewritable
} from 'svelte/store';
```

## derived[](#derived)

Derived value store by synchronizing one or more readable stores and applying an aggregation function over its input values.

```
function derived<S extends Stores, T>(
	stores: S,
	fn: (
		values: StoresValues<S>,
		set: (value: T) => void,
		update: (fn: Updater<T>) => void
	) => Unsubscriber | void,
	initial_value?: T | undefined
): Readable<T>;
```

```
function derived<S extends Stores, T>(
	stores: S,
	fn: (values: StoresValues<S>) => T,
	initial_value?: T | undefined
): Readable<T>;
```

## fromStore[](#fromStore)

```
function fromStore<V>(store: Writable<V>): {
	current: V;
};
```

```
function fromStore<V>(store: Readable<V>): {
	readonly current: V;
};
```

## get[](#get)

Get the current value from a store by subscribing and immediately unsubscribing.

```
function get<T>(store: Readable<T>): T;
```

## readable[](#readable)

Creates a `Readable` store that allows reading by subscription.

```
function readable<T>(
	value?: T | undefined,
	start?: StartStopNotifier<T> | undefined
): Readable<T>;
```

## readonly[](#readonly)

Takes a store and returns a new one derived from the old one that is readable.

```
function readonly<T>(store: Readable<T>): Readable<T>;
```

## toStore[](#toStore)

```
function toStore<V>(
	get: () => V,
	set: (v: V) => void
): Writable<V>;
```

```
function toStore<V>(get: () => V): Readable<V>;
```

## writable[](#writable)

Create a `Writable` store that allows both updating and reading by subscription.

```
function writable<T>(
	value?: T | undefined,
	start?: StartStopNotifier<T> | undefined
): Writable<T>;
```

## Readable[](#Readable)

Readable interface for subscribing.

```
interface Readable<T> {…}
```

```
subscribe(this: void, run: Subscriber<T>, invalidate?: () => void): Unsubscriber;
```

*   `run` subscription callback
*   `invalidate` cleanup callback

Subscribe on value changes.

## StartStopNotifier[](#StartStopNotifier)

Start and stop notification callbacks. This function is called when the first subscriber subscribes.

```
type StartStopNotifier<T> = (
	set: (value: T) => void,
	update: (fn: Updater<T>) => void
) => void | (() => void);
```

## Subscriber[](#Subscriber)

Callback to inform of a value updates.

```
type Subscriber<T> = (value: T) => void;
```

## Unsubscriber[](#Unsubscriber)

Unsubscribes from value updates.

```
type Unsubscriber = () => void;
```

## Updater[](#Updater)

Callback to update a value.

```
type Updater<T> = (value: T) => T;
```

## Writable[](#Writable)

Writable interface for both updating and subscribing.

```
interface Writable<T> extends Readable<T> {…}
```

```
set(this: void, value: T): void;
```

*   `value` to set

Set value and inform subscribers.

```
update(this: void, updater: Updater<T>): void;
```

*   `updater` callback

Update value using callback and inform subscribers.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/98-reference/21-svelte-store.md) [llms.txt](/docs/svelte/svelte-store/llms.txt)

previous next

[svelte/server](/docs/svelte/svelte-server) [svelte/transition](/docs/svelte/svelte-transition)
