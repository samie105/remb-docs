---
title: "Context"
source: "https://svelte.dev/docs/svelte/context"
canonical_url: "https://svelte.dev/docs/svelte/context"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:48.278Z"
content_hash: "cee9b0584f9e704cc14179a3c24c32ae3508678a2d32b4773ddb02ba9c51eec1"
menu_path: ["Context"]
section_path: []
nav_prev: {"path": "../stores/index.md", "title": "Stores"}
nav_next: {"path": "../lifecycle-hooks/index.md", "title": "Lifecycle hooks"}
---

Context allows components to access values owned by parent components without passing them down as props (potentially through many layers of intermediate components, known as 'prop-drilling').

By creating a `[get, set]` pair of functions with `createContext`, you can set the context in a parent component and get it in a child component:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA42SwW6DMAyGX8WyJgESAvVKKdrUF9hlp9IDAzMipQEl7toJ8e5TAFFgm8Yx8e8__2enRZVdCCM81orpzuhjKSQZjE4tvmeGxvJL0wTmkyQT-phbrWKDEcYm16LhJFUpi0tTa4bXTJNiKHV9AScIh-PY7OxnwmMlZDHp-tNMFocPaxUPLv0z8dAXJlYz3qOPvwXtiSLWV_KRvxpbt3TY-Qu4RcR_-VowxG-G9Dgy6CaGfLjpKVXKkqw6t3E1KejgAE-NrhvjeqNi6eS2YBNF4NxqLQsHOm89iPZZkypIT66u1z3g1yAb-eej34D_sRE_r5VhuBrScFg1uT_A4mqXVCRlDa3tCGy0zgehjCgI5gnjsNrNFr4KvxF5jBqwWQJPkLmmjGnNOPvFSigmXWY5gQWD1iIP6zOshfrYp6qzOrr3lsM0Tss5-Ku_dIbD8uXYFhPX2z-AF9H_xD37yJmQN6EKjMpMGuq-AU_UQgfsAwAA)

```
<script>
	import Parent from './Parent.svelte';
	import Child from './Child.svelte';
</script>

<Parent>
	<Child />
</Parent>
```

```
<script lang="ts">
	import Parent from './Parent.svelte';
	import Child from './Child.svelte';
</script>

<Parent>
	<Child />
</Parent>
```

```
<script>
	import { setUserContext } from './context';

	let { children } = $props();

	setUserContext({ name: 'world' });
</script>

{@render children()}
```

```
<script lang="ts">
	import { setUserContext } from './context';

	let { children } = $props();

	setUserContext({ name: 'world' });
</script>

{@render children()}
```

```
<script>
	import { getUserContext } from './context';

	const user = getUserContext();
</script>

<h1>hello {user.name}, inside Child.svelte</h1>
```

```
<script lang="ts">
	import { getUserContext } from './context';

	const user = getUserContext();
</script>

<h1>hello {user.name}, inside Child.svelte</h1>
```

```
import { function createContext<T>(): [() => T, (context: T) => T]Returns a [get, set] pair of functions for working with context in a type-safe way.
get will throw an error if no parent component called set.
@since5.40.0referencecreateContext } from 'svelte';

interface User {
	User.name: stringname: string;
}

export const [const getUserContext: () => UsergetUserContext, const setUserContext: (context: User) => UsersetUserContext] = createContext<User>(): [() => User, (context: User) => User]Returns a [get, set] pair of functions for working with context in a type-safe way.
get will throw an error if no parent component called set.
@since5.40.0referencecreateContext<User>();
```

> `createContext` was added in version 5.40. If you are using an earlier version of Svelte, you must use `setContext` and `getContext` instead.

This is particularly useful when `Parent.svelte` is not directly aware of `Child.svelte`, but instead renders it as part of a `children` [snippet](snippet) as shown above.

## setContext and getContext[](#setContext-and-getContext)

As an alternative to `createContext`, you can use `setContext` and `getContext` directly. The parent component sets context with `setContext(key, value)`...

Parent

```
<script>
	import { setContext } from 'svelte';

	setContext('my-context', 'hello from Parent.svelte');
</script>
```

```
<script lang="ts">
	import { setContext } from 'svelte';

	setContext('my-context', 'hello from Parent.svelte');
</script>
```

...and the child retrieves it with `getContext`:

Child

```
<script>
	import { getContext } from 'svelte';

	const message = getContext('my-context');
</script>

<h1>{message}, inside Child.svelte</h1>
```

```
<script lang="ts">
	import { getContext } from 'svelte';

	const message = getContext('my-context');
</script>

<h1>{message}, inside Child.svelte</h1>
```

The key (`'my-context'`, in the example above) and the context itself can be any JavaScript value.

> `createContext` is preferred since it provides better type safety and makes it unnecessary to use keys.

In addition to [`setContext`](svelte#setContext) and [`getContext`](svelte#getContext), Svelte exposes [`hasContext`](svelte#hasContext) and [`getAllContexts`](svelte#getAllContexts) functions.

## Using context with state[](#Using-context-with-state)

You can store reactive state in context...

[Open in playground](/playground/untitled#H4sIAAAAAAAAA42S226DMAyGX8WKJpVqCLpbCkhTH6P0gqZmjQYBJWbthHj3KQkU2FaJKw4-_P9nu2Myr5BF7FBLwjvBTdAVNOWEzGeFKFGz6Nixc65xyHxvmkB_YWkzuCmTpFnEYs2VaCjNZEaiampF0IFGOtStJFTQQ6HqCjZByJ1WQHqzn2UfrqK8PJLs1yBk02RGJRLwoV0CL9am15lIRvZ_BDvz1W-HgkneG-pMJA4nqzI-t0S1hFryUvDPpPO2kKSjTGCf8JrAW-_IJFdYoSTTxpW6Ns59mD57XamUwM4JKdQ4F2E--28BZpAsItWiz-i7MXGzNdb7i6XNp7libR8r1ibNzKWeb2Qq8_7OuUm7BWofh82M6pfDlVyTpyXVg4QrzAnH6x5h5mcljKUi5wgjcufY7D3Jtjqj2meyN7l4t20d93HC9WeHfoJkqRoPgdTb7ifehfOntCefUS7Km5AXFhV5qbH_AYUaIeGzAwAA)

```
<script>
	import { setCounter } from './context.ts';
	import Child from './Child.svelte';

	let counter = $state({
		count: 0
	});

	setCounter(counter);
</script>

<button onclick={() => counter.count += 1}>
	increment
</button>

<Child />
<Child />
<Child />

<button onclick={() => counter.count = 0}>
	reset
</button>
```

```
<script lang="ts">
	import { setCounter } from './context.ts';
	import Child from './Child.svelte';

	let counter = $state({
		count: 0
	});

	setCounter(counter);
</script>

<button onclick={() => counter.count += 1}>
	increment
</button>

<Child />
<Child />
<Child />

<button onclick={() => counter.count = 0}>
	reset
</button>
```

```
<script>
	import { getCounter } from './context.ts';

	const counter = getCounter();
</script>

<p>{counter.count}</p>
```

```
<script lang="ts">
	import { getCounter } from './context.ts';

	const counter = getCounter();
</script>

<p>{counter.count}</p>
```

```
import { function createContext<T>(): [() => T, (context: T) => T]Returns a [get, set] pair of functions for working with context in a type-safe way.
get will throw an error if no parent component called set.
@since5.40.0referencecreateContext } from 'svelte';

interface Counter {
	Counter.count: numbercount: number;
}

export const [const getCounter: () => CountergetCounter, const setCounter: (context: Counter) => CountersetCounter] = createContext<Counter>(): [() => Counter, (context: Counter) => Counter]Returns a [get, set] pair of functions for working with context in a type-safe way.
get will throw an error if no parent component called set.
@since5.40.0referencecreateContext<Counter>();
```

...though note that if you _reassign_ `counter` instead of updating it, you will 'break the link' — in other words instead of this...

```
<button onclick={() => counter = { count: 0 } }>
	reset
</button>
```

...you must do this:

```
<button onclick={() => counter.count = 0}>
	reset
</button>
```

Svelte will warn you if you get it wrong.

## Component testing[](#Component-testing)

When writing [component tests](testing#Unit-and-component-tests-with-Vitest-Component-testing), it can be useful to create a wrapper component that sets the context in order to check the behaviour of a component that uses it. As of version 5.49, you can do this sort of thing:

```
import { function mount<Props extends Record<string, any>, Exports extends Record<string, any>>(component: ComponentType<SvelteComponent<Props>> | Component<Props, Exports, any>, options: MountOptions<Props>): ExportsMounts a component to the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component.
Transitions will play during the initial render unless the intro option is set to false.
referencemount, function unmount(component: Record<string, any>, options?: {
    outro?: boolean;
} | undefined): Promise<void>Unmounts a component that was previously mounted using mount or hydrate.
Since 5.13.0, if options.outro is true, transitions will play before the component is removed from the DOM.
Returns a Promise that resolves after transitions have completed if options.outro is true, or immediately otherwise (prior to 5.13.0, returns void).
import { mount, unmount } from 'svelte';
import App from './App.svelte';

const app = mount(App, { target: document.body });

// later...
unmount(app, { outro: true });referenceunmount } from 'svelte';
import { const expect: ExpectStaticexpect, const test: TestAPIDefines a test case with a given name and test function. The test function can optionally be configured with test options.
@paramname - The name of the test or a function that will be used as a test name.@paramoptionsOrFn - Optional. The test options or the test function if no explicit name is provided.@paramoptionsOrTest - Optional. The test function or options, depending on the previous parameters.@throwsError If called inside another test function.@example// Define a simple test
test('should add two numbers', () => {
  expect(add(1, 2)).toBe(3);
});@example// Define a test with options
test('should subtract two numbers', { retry: 3 }, () => {
  expect(subtract(5, 2)).toBe(3);
});test } from 'vitest';
import { import setUserContextsetUserContext } from './context';
import type MyComponent = SvelteComponent<Record<string, any>, any, any>
const MyComponent: LegacyComponentTypeMyComponent from './MyComponent.svelte';

test<object>(name: string | Function, fn?: TestFunction<object> | undefined, options?: number): void (+1 overload)Defines a test case with a given name and test function. The test function can optionally be configured with test options.
@paramname - The name of the test or a function that will be used as a test name.@paramoptionsOrFn - Optional. The test options or the test function if no explicit name is provided.@paramoptionsOrTest - Optional. The test function or options, depending on the previous parameters.@throwsError If called inside another test function.@example// Define a simple test
test('should add two numbers', () => {
  expect(add(1, 2)).toBe(3);
});@example// Define a test with options
test('should subtract two numbers', { retry: 3 }, () => {
  expect(subtract(5, 2)).toBe(3);
});test('MyComponent', () => {
	function function (local function) Wrapper(...args: any[]): {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>Wrapper(...args: any[]args) {
		import setUserContextsetUserContext({ name: stringname: 'Bob' });
		return function MyComponent(internals: Brand<"ComponentInternals">, props: Record<string, any>): ReturnType<Component<Record<string, any>, Record<string, any>>>MyComponent(...args: any[]args);
	}

	const const component: {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>component = mount<Record<string, any>, {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>>(component: ComponentType<SvelteComponent<Record<string, any>, any, any>> | Component<Record<string, any>, {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>, any>, options: MountOptions<...>): {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<...>Mounts a component to the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component.
Transitions will play during the initial render unless the intro option is set to false.
referencemount(function (local function) Wrapper(...args: any[]): {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>Wrapper, {
		target: Document | Element | ShadowRootTarget element where the component will be mounted.
target: var document: Documentwindow.document returns a reference to the document contained in the window.
MDN Reference
document.Document.body: HTMLElementThe Document.body property represents the null if no such element exists.
MDN Reference
body
	});

	expect<string>(actual: string, message?: string): Assertion<string> (+1 overload)expect(var document: Documentwindow.document returns a reference to the document contained in the window.
MDN Reference
document.Document.body: HTMLElementThe Document.body property represents the null if no such element exists.
MDN Reference
body.Element.innerHTML: stringThe innerHTML property of the Element interface gets or sets the HTML or XML markup contained within the element.
MDN Reference
innerHTML).JestAssertion<string>.toBe: <string>(expected: string) => voidChecks that a value is what you expect. It calls Object.is to compare values.
Don't use toBe with floating-point numbers.
@exampleexpect(result).toBe(42);
expect(status).toBe(true);
toBe('<h1>Hello Bob!</h1>');

	function unmount(component: Record<string, any>, options?: {
    outro?: boolean;
} | undefined): Promise<void>Unmounts a component that was previously mounted using mount or hydrate.
Since 5.13.0, if options.outro is true, transitions will play before the component is removed from the DOM.
Returns a Promise that resolves after transitions have completed if options.outro is true, or immediately otherwise (prior to 5.13.0, returns void).
import { mount, unmount } from 'svelte';
import App from './App.svelte';

const app = mount(App, { target: document.body });

// later...
unmount(app, { outro: true });referenceunmount(const component: {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>component);
});
```

This approach also works with [`hydrate`](imperative-component-api#hydrate) and [`render`](imperative-component-api#render).

## Replacing global state[](#Replacing-global-state)

When you have state shared by many different components, you might be tempted to put it in its own module and just import it wherever it's needed:

state.svelte

```
export const const myGlobalState: {
    user: {};
}myGlobalState = function $state<{
    user: {};
}>(initial: {
    user: {};
}): {
    user: {};
} (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state({
	user: {}user: {
		// ...
	}
	// ...
});
```

In many cases this is perfectly fine, but there is a risk: if you mutate the state during server-side rendering (which is discouraged, but entirely possible!)...

App

```
<script>
	import { myGlobalState } from './state.svelte.js';

	let { data } = $props();

	if (data.user) {
		myGlobalState.user = data.user;
	}
</script>
```

```
<script lang="ts">
	import { myGlobalState } from './state.svelte.js';

	let { data } = $props();

	if (data.user) {
		myGlobalState.user = data.user;
	}
</script>
```

...then the data may be accessible by the _next_ user. Context solves this problem because it is not shared between requests.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/06-runtime/02-context.md) [llms.txt](/docs/svelte/context/llms.txt)

previous next

[Stores](/docs/svelte/stores) [Lifecycle hooks](/docs/svelte/lifecycle-hooks)
