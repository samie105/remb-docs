---
title: "Imperative component API"
source: "https://svelte.dev/docs/svelte/legacy-component-api"
canonical_url: "https://svelte.dev/docs/svelte/legacy-component-api"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:54.085Z"
content_hash: "ad288c15af1c2d91bf01146466a6adab8b6c3afc57928eb81333a5187a01b84e"
menu_path: ["Imperative component API"]
section_path: []
nav_prev: {"path": "../legacy-svelte-self/index.md", "title": "<svelte:self>"}
---

In Svelte 3 and 4, the API for interacting with a component is different than in Svelte 5. Note that this page does _not_ apply to legacy mode components in a Svelte 5 application.

## Creating a component[](#Creating-a-component)

```
const const component: anycomponent = new Component(options);
```

A client-side component — that is, a component compiled with `generate: 'dom'` (or the `generate` option left unspecified) is a JavaScript class.

```
import type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentTypeApp from './App.svelte';

const const app: SvelteComponent<Record<string, any>, any, any>app = new new App(o: ComponentConstructorOptions): SvelteComponentApp({
	ComponentConstructorOptions<Record<string, any>>.target: Document | Element | ShadowRoottarget: var document: Documentwindow.document returns a reference to the document contained in the window.
MDN Reference
document.Document.body: HTMLElementThe Document.body property represents the null if no such element exists.
MDN Reference
body,
	ComponentConstructorOptions<Record<string, any>>.props?: Record<string, any> | undefinedprops: {
		// assuming App.svelte contains something like
		// `export let answer`:
		answer: numberanswer: 42
	}
});
```

The following initialisation options can be provided:

option

default

description

`target`

**none**

An `HTMLElement` or `ShadowRoot` to render to. This option is required

`anchor`

`null`

A child of `target` to render the component immediately before

`props`

`{}`

An object of properties to supply to the component

`context`

`new Map()`

A `Map` of root-level context key-value pairs to supply to the component

`hydrate`

`false`

See below

`intro`

`false`

If `true`, will play transitions on initial render, rather than waiting for subsequent state changes

Existing children of `target` are left where they are.

The `hydrate` option instructs Svelte to upgrade existing DOM (usually from server-side rendering) rather than creating new elements. It will only work if the component was compiled with the [`hydratable: true` option](/docs/svelte-compiler#compile). Hydration of `<head>` elements only works properly if the server-side rendering code was also compiled with `hydratable: true`, which adds a marker to each element in the `<head>` so that the component knows which elements it's responsible for removing during hydration.

Whereas children of `target` are normally left alone, `hydrate: true` will cause any children to be removed. For that reason, the `anchor` option cannot be used alongside `hydrate: true`.

The existing DOM doesn't need to match the component — Svelte will 'repair' the DOM as it goes.

index

```
import type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentTypeApp from './App.svelte';

const const app: SvelteComponent<Record<string, any>, any, any>app = new new App(o: ComponentConstructorOptions): SvelteComponentApp({
	ComponentConstructorOptions<Record<string, any>>.target: Document | Element | ShadowRoottarget: var document: Documentwindow.document returns a reference to the document contained in the window.
MDN Reference
document.ParentNode.querySelector<Element>(selectors: string): Element | null (+4 overloads)Returns the first element that is a descendant of node that matches selectors.
MDN Reference
querySelector('#server-rendered-html'),
	ComponentConstructorOptions<Record<string, any>>.hydrate?: boolean | undefinedhydrate: true
});
```

> In Svelte 5+, use [`mount`](svelte#mount) instead

## $set[](#$set)

```
component.$set(props);
```

Programmatically sets props on an instance. `component.$set({ x: 1 })` is equivalent to `x = 1` inside the component's `<script>` block.

Calling this method schedules an update for the next microtask — the DOM is _not_ updated synchronously.

```
component.$set({ answer: numberanswer: 42 });
```

> In Svelte 5+, use `$state` instead to create a component props and update that
> 
> ```
> let module props
> let props: {
>     answer: number;
> }props = function $state<{
>     answer: number;
> }>(initial: {
>     answer: number;
> }): {
>     answer: number;
> } (+1 overload)
> namespace $stateDeclares reactive state.
> Example:
> let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state({ answer: numberanswer: 42 });
> const const component: anycomponent = mount(Component, { props: {
>     answer: number;
> }props });
> // ...
> module props
> let props: {
>     answer: number;
> }props.answer: numberanswer = 24;
> ```

## $on[](#$on)

```
component.$on(ev, callback);
```

Causes the `callback` function to be called whenever the component dispatches an `event`.

A function is returned that will remove the event listener when called.

```
const const off: anyoff = component.$on('selected', (event: anyevent) => {
	var console: ConsoleThe console module provides a simple debugging console that is similar to the
JavaScript console mechanism provided by web browsers.
The module exports two specific components:

A Console class with methods such as console.log(), console.error() and console.warn() that can be used to write to any Node.js stream.
A global console instance configured to write to process.stdout and
process.stderr. The global console can be used without importing the node:console module.

Warning: The global console object's methods are neither consistently
synchronous like the browser APIs they resemble, nor are they consistently
asynchronous like all other Node.js streams. See the note on process I/O for
more information.
Example using the global console:
console.log('hello world');
// Prints: hello world, to stdout
console.log('hello %s', 'world');
// Prints: hello world, to stdout
console.error(new Error('Whoops, something bad happened'));
// Prints error message and stack trace to stderr:
//   Error: Whoops, something bad happened
//     at [eval]:5:15
//     at Script.runInThisContext (node:vm:132:18)
//     at Object.runInThisContext (node:vm:309:38)
//     at node:internal/process/execution:77:19
//     at [eval]-wrapper:6:22
//     at evalScript (node:internal/process/execution:76:60)
//     at node:internal/main/eval_string:23:3

const name = 'Will Robinson';
console.warn(`Danger ${name}! Danger!`);
// Prints: Danger Will Robinson! Danger!, to stderrExample using the Console class:
const out = getStreamSomehow();
const err = getStreamSomehow();
const myConsole = new console.Console(out, err);

myConsole.log('hello world');
// Prints: hello world, to out
myConsole.log('hello %s', 'world');
// Prints: hello world, to out
myConsole.error(new Error('Whoops, something bad happened'));
// Prints: [Error: Whoops, something bad happened], to err

const name = 'Will Robinson';
myConsole.warn(`Danger ${name}! Danger!`);
// Prints: Danger Will Robinson! Danger!, to err@seesourceconsole.Console.log(message?: any, ...optionalParams: any[]): void (+1 overload)Prints to stdout with newline. Multiple arguments can be passed, with the
first used as the primary message and all additional used as substitution
values similar to printf(3)
(the arguments are all passed to util.format()).
const count = 5;
console.log('count: %d', count);
// Prints: count: 5, to stdout
console.log('count:', count);
// Prints: count: 5, to stdoutSee util.format() for more information.
@sincev0.1.100log(event: anyevent.detail.selection);
});

const off: anyoff();
```

> In Svelte 5+, pass callback props instead

## $destroy[](#$destroy)

```
component.$destroy();
```

Removes a component from the DOM and triggers any `onDestroy` handlers.

> In Svelte 5+, use [`unmount`](svelte#unmount) instead

## Component props[](#Component-props)

```
component.prop;
```

```
module componentcomponent.component.prop: anyprop = value;
```

If a component is compiled with `accessors: true`, each instance will have getters and setters corresponding to each of the component's props. Setting a value will cause a _synchronous_ update, rather than the default async update caused by `component.$set(...)`.

By default, `accessors` is `false`, unless you're compiling as a custom element.

```
var console: ConsoleThe console module provides a simple debugging console that is similar to the
JavaScript console mechanism provided by web browsers.
The module exports two specific components:

A Console class with methods such as console.log(), console.error() and console.warn() that can be used to write to any Node.js stream.
A global console instance configured to write to process.stdout and
process.stderr. The global console can be used without importing the node:console module.

Warning: The global console object's methods are neither consistently
synchronous like the browser APIs they resemble, nor are they consistently
asynchronous like all other Node.js streams. See the note on process I/O for
more information.
Example using the global console:
console.log('hello world');
// Prints: hello world, to stdout
console.log('hello %s', 'world');
// Prints: hello world, to stdout
console.error(new Error('Whoops, something bad happened'));
// Prints error message and stack trace to stderr:
//   Error: Whoops, something bad happened
//     at [eval]:5:15
//     at Script.runInThisContext (node:vm:132:18)
//     at Object.runInThisContext (node:vm:309:38)
//     at node:internal/process/execution:77:19
//     at [eval]-wrapper:6:22
//     at evalScript (node:internal/process/execution:76:60)
//     at node:internal/main/eval_string:23:3

const name = 'Will Robinson';
console.warn(`Danger ${name}! Danger!`);
// Prints: Danger Will Robinson! Danger!, to stderrExample using the Console class:
const out = getStreamSomehow();
const err = getStreamSomehow();
const myConsole = new console.Console(out, err);

myConsole.log('hello world');
// Prints: hello world, to out
myConsole.log('hello %s', 'world');
// Prints: hello world, to out
myConsole.error(new Error('Whoops, something bad happened'));
// Prints: [Error: Whoops, something bad happened], to err

const name = 'Will Robinson';
myConsole.warn(`Danger ${name}! Danger!`);
// Prints: Danger Will Robinson! Danger!, to err@seesourceconsole.Console.log(message?: any, ...optionalParams: any[]): void (+1 overload)Prints to stdout with newline. Multiple arguments can be passed, with the
first used as the primary message and all additional used as substitution
values similar to printf(3)
(the arguments are all passed to util.format()).
const count = 5;
console.log('count: %d', count);
// Prints: count: 5, to stdout
console.log('count:', count);
// Prints: count: 5, to stdoutSee util.format() for more information.
@sincev0.1.100log(component.count);
component.count += 1;
```

> In Svelte 5+, this concept is obsolete. If you want to make properties accessible from the outside, `export` them

## Server-side component API[](#Server-side-component-API)

```
const const result: anyresult = Component.render(...)
```

Unlike client-side components, server-side components don't have a lifespan after you render them — their whole job is to create some HTML and CSS. For that reason, the API is somewhat different.

A server-side component exposes a `render` method that can be called with optional props. It returns an object with `head`, `html`, and `css` properties, where `head` contains the contents of any `<svelte:head>` elements encountered.

You can import a Svelte component directly into Node using `svelte/register`.

```
var require: NodeJS.Require
(id: string) => anyUsed to import modules, JSON, and local files.
@sincev0.1.13require('svelte/register');

const const App: anyApp = var require: NodeJS.Require
(id: string) => anyUsed to import modules, JSON, and local files.
@sincev0.1.13require('./App.svelte').default;

const { const head: anyhead, const html: anyhtml, const css: anycss } = const App: anyApp.render({
	answer: numberanswer: 42
});
```

The `.render()` method accepts the following parameters:

parameter

default

description

`props`

`{}`

An object of properties to supply to the component

`options`

`{}`

An object of options

The `options` object takes in the following options:

option

default

description

`context`

`new Map()`

A `Map` of root-level context key-value pairs to supply to the component

```
const { const head: anyhead, const html: anyhtml, const css: anycss } = App.render(
	// props
	{ answer: numberanswer: 42 },
	// options
	{
		context: Map<string, string>context: new var Map: MapConstructor
new <string, string>(iterable?: Iterable<readonly [string, string]> | null | undefined) => Map<string, string> (+3 overloads)Map([['context-key', 'context-value']])
	}
);
```

> In Svelte 5+, use [`render`](svelte-server#render) instead

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/99-legacy/40-legacy-component-api.md) [llms.txt](/docs/svelte/legacy-component-api/llms.txt)

previous next

[<svelte:self>](/docs/svelte/legacy-svelte-self)
