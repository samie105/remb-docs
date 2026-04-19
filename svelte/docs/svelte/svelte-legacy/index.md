---
title: "svelte/legacy"
source: "https://svelte.dev/docs/svelte/svelte-legacy"
canonical_url: "https://svelte.dev/docs/svelte/svelte-legacy"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:42.726Z"
content_hash: "5e0f60e36ad28290f984dc5be45850440bc1531c027ec4d1e5ffe7cff409b4ca"
menu_path: ["svelte/legacy"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/svelte-events/index.md", "title": "svelte/events"}
nav_next: {"path": "svelte/docs/svelte/svelte-motion/index.md", "title": "svelte/motion"}
---

This module provides various functions for use during the migration, since some features can't be replaced one to one with new features. All imports are marked as deprecated and should be migrated away from over time.

```
import {
	function asClassComponent<Props extends Record<string, any>, Exports extends Record<string, any>, Events extends Record<string, any>, Slots extends Record<string, any>>(component: SvelteComponent<Props, Events, Slots> | Component<Props>): ComponentType<SvelteComponent<Props, Events, Slots> & Exports>Takes the component function and returns a Svelte 4 compatible component constructor.
@deprecatedUse this only as a temporary solution to migrate your imperative component code to Svelte 5.referenceasClassComponent,
	function createBubbler(): (type: string) => (event: Event) => booleanFunction to create a bubble function that mimic the behavior of on:click without handler available in svelte 4.
@deprecatedUse this only as a temporary solution to migrate your automatically delegated events in Svelte 5.referencecreateBubbler,
	function createClassComponent<Props extends Record<string, any>, Exports extends Record<string, any>, Events extends Record<string, any>, Slots extends Record<string, any>>(options: ComponentConstructorOptions<Props> & {
    component: ComponentType<SvelteComponent<Props, Events, Slots>> | Component<Props>;
}): SvelteComponent<Props, Events, Slots> & ExportsTakes the same options as a Svelte 4 component and the component function and returns a Svelte 4 compatible component.
@deprecatedUse this only as a temporary solution to migrate your imperative component code to Svelte 5.referencecreateClassComponent,
	function handlers(...handlers: EventListener[]): EventListenerFunction to mimic the multiple listeners available in svelte 4
@deprecatedhandlers,
	function nonpassive(node: HTMLElement, [event, handler]: [event: string, handler: () => EventListener]): voidSubstitute for the nonpassive event modifier, implemented as an action
@deprecatedreferencenonpassive,
	function once(fn: (event: Event, ...args: Array<unknown>) => void): (event: Event, ...args: unknown[]) => voidSubstitute for the once event modifier
@deprecatedreferenceonce,
	function passive(node: HTMLElement, [event, handler]: [event: string, handler: () => EventListener]): voidSubstitute for the passive event modifier, implemented as an action
@deprecatedreferencepassive,
	function preventDefault(fn: (event: Event, ...args: Array<unknown>) => void): (event: Event, ...args: unknown[]) => voidSubstitute for the preventDefault event modifier
@deprecatedreferencepreventDefault,
	function run(fn: () => void | (() => void)): voidRuns the given function once immediately on the server, and works like $effect.pre on the client.
@deprecatedUse this only as a temporary solution to migrate your component code to Svelte 5.run,
	function self(fn: (event: Event, ...args: Array<unknown>) => void): (event: Event, ...args: unknown[]) => voidSubstitute for the self event modifier
@deprecatedreferenceself,
	function stopImmediatePropagation(fn: (event: Event, ...args: Array<unknown>) => void): (event: Event, ...args: unknown[]) => voidSubstitute for the stopImmediatePropagation event modifier
@deprecatedreferencestopImmediatePropagation,
	function stopPropagation(fn: (event: Event, ...args: Array<unknown>) => void): (event: Event, ...args: unknown[]) => voidSubstitute for the stopPropagation event modifier
@deprecatedreferencestopPropagation,
	function trusted(fn: (event: Event, ...args: Array<unknown>) => void): (event: Event, ...args: unknown[]) => voidSubstitute for the trusted event modifier
@deprecatedreferencetrusted
} from 'svelte/legacy';
```

## asClassComponent[](#asClassComponent)

> Use this only as a temporary solution to migrate your imperative component code to Svelte 5.

Takes the component function and returns a Svelte 4 compatible component constructor.

```
function asClassComponent<
	Props extends Record<string, any>,
	Exports extends Record<string, any>,
	Events extends Record<string, any>,
	Slots extends Record<string, any>
>(
	component:
		| SvelteComponent<Props, Events, Slots>
		| Component<Props>
): ComponentType<
	SvelteComponent<Props, Events, Slots> & Exports
>;
```

## createBubbler[](#createBubbler)

> Use this only as a temporary solution to migrate your automatically delegated events in Svelte 5.

Function to create a `bubble` function that mimic the behavior of `on:click` without handler available in svelte 4.

```
function createBubbler(): (
	type: string
) => (event: Event) => boolean;
```

## createClassComponent[](#createClassComponent)

> Use this only as a temporary solution to migrate your imperative component code to Svelte 5.

Takes the same options as a Svelte 4 component and the component function and returns a Svelte 4 compatible component.

```
function createClassComponent<
	Props extends Record<string, any>,
	Exports extends Record<string, any>,
	Events extends Record<string, any>,
	Slots extends Record<string, any>
>(
	options: ComponentConstructorOptions<Props> & {
		component:
			| ComponentType<SvelteComponent<Props, Events, Slots>>
			| Component<Props>;
	}
): SvelteComponent<Props, Events, Slots> & Exports;
```

## handlers[](#handlers)

Function to mimic the multiple listeners available in svelte 4

```
function handlers(
	...handlers: EventListener[]
): EventListener;
```

## nonpassive[](#nonpassive)

Substitute for the `nonpassive` event modifier, implemented as an action

```
function nonpassive(
	node: HTMLElement,
	[event, handler]: [
		event: string,
		handler: () => EventListener
	]
): void;
```

## once[](#once)

Substitute for the `once` event modifier

```
function once(
	fn: (event: Event, ...args: Array<unknown>) => void
): (event: Event, ...args: unknown[]) => void;
```

## passive[](#passive)

Substitute for the `passive` event modifier, implemented as an action

```
function passive(
	node: HTMLElement,
	[event, handler]: [
		event: string,
		handler: () => EventListener
	]
): void;
```

## preventDefault[](#preventDefault)

Substitute for the `preventDefault` event modifier

```
function preventDefault(
	fn: (event: Event, ...args: Array<unknown>) => void
): (event: Event, ...args: unknown[]) => void;
```

## run[](#run)

> Use this only as a temporary solution to migrate your component code to Svelte 5.

Runs the given function once immediately on the server, and works like `$effect.pre` on the client.

```
function run(fn: () => void | (() => void)): void;
```

## self[](#self)

Substitute for the `self` event modifier

```
function self(
	fn: (event: Event, ...args: Array<unknown>) => void
): (event: Event, ...args: unknown[]) => void;
```

## stopImmediatePropagation[](#stopImmediatePropagation)

Substitute for the `stopImmediatePropagation` event modifier

```
function stopImmediatePropagation(
	fn: (event: Event, ...args: Array<unknown>) => void
): (event: Event, ...args: unknown[]) => void;
```

## stopPropagation[](#stopPropagation)

Substitute for the `stopPropagation` event modifier

```
function stopPropagation(
	fn: (event: Event, ...args: Array<unknown>) => void
): (event: Event, ...args: unknown[]) => void;
```

## trusted[](#trusted)

Substitute for the `trusted` event modifier

```
function trusted(
	fn: (event: Event, ...args: Array<unknown>) => void
): (event: Event, ...args: unknown[]) => void;
```

## LegacyComponentType[](#LegacyComponentType)

Support using the component as both a class and function during the transition period

```
type LegacyComponentType = {
	new (o: ComponentConstructorOptions): SvelteComponent;
	(
		...args: Parameters<Component<Record<string, any>>>
	): ReturnType<
		Component<Record<string, any>, Record<string, any>>
	>;
};
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/98-reference/21-svelte-legacy.md) [llms.txt](/docs/svelte/svelte-legacy/llms.txt)

previous next

[svelte/events](/docs/svelte/svelte-events) [svelte/motion](/docs/svelte/svelte-motion)
