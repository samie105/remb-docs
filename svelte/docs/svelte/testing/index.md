---
title: "Testing"
source: "https://svelte.dev/docs/svelte/testing"
canonical_url: "https://svelte.dev/docs/svelte/testing"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:42.221Z"
content_hash: "a0436461bbb132ece0a9c3757180cdb2099e6f52d41c3e8c29b2839a640c6afd"
menu_path: ["Testing"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/best-practices/index.md", "title": "Best practices"}
nav_next: {"path": "svelte/docs/svelte/typescript/index.md", "title": "TypeScript"}
---

Testing helps you write and maintain your code and guard against regressions. Testing frameworks help you with that, allowing you to describe assertions or expectations about how your code should behave. Svelte is unopinionated about which testing framework you use — you can write unit tests, integration tests, and end-to-end tests using solutions like [Vitest](https://vitest.dev/), [Jasmine](https://jasmine.github.io/), [Cypress](https://www.cypress.io/) and [Playwright](https://playwright.dev/).

## Unit and component tests with Vitest[](#Unit-and-component-tests-with-Vitest)

Unit tests allow you to test small isolated parts of your code. Integration tests allow you to test parts of your application to see if they work together. If you're using Vite (including via SvelteKit), we recommend using [Vitest](https://vitest.dev/). You can use the Svelte CLI to [setup Vitest](/docs/cli/vitest) either during project creation or later on.

To setup Vitest manually, first install it:

```
npm install -D vitest
```

Then adjust your `vite.config.js`:

vite.config

```
import { function defineConfig(config: UserConfig): UserConfig (+4 overloads)defineConfig } from 'vitest/config';

export default function defineConfig(config: UserConfig): UserConfig (+4 overloads)defineConfig({
	// ...
	// Tell Vitest to use the `browser` entry points in `package.json` files, even though it's running in Node
	resolve?: AllResolveOptions | undefinedresolve: var process: NodeJS.Processprocess.NodeJS.Process.env: NodeJS.ProcessEnvThe process.env property returns an object containing the user environment.
See environ(7).
An example of this object looks like:
{
  TERM: 'xterm-256color',
  SHELL: '/usr/local/bin/bash',
  USER: 'maciej',
  PATH: '~/.bin/:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin',
  PWD: '/Users/maciej',
  EDITOR: 'vim',
  SHLVL: '1',
  HOME: '/Users/maciej',
  LOGNAME: 'maciej',
  _: '/usr/local/bin/node'
}It is possible to modify this object, but such modifications will not be
reflected outside the Node.js process, or (unless explicitly requested)
to other Worker threads.
In other words, the following example would not work:
node -e 'process.env.foo = "bar"' && echo $fooWhile the following will:
import { env } from 'node:process';

env.foo = 'bar';
console.log(env.foo);Assigning a property on process.env will implicitly convert the value
to a string. This behavior is deprecated. Future versions of Node.js may
throw an error when the value is not a string, number, or boolean.
import { env } from 'node:process';

env.test = null;
console.log(env.test);
// => 'null'
env.test = undefined;
console.log(env.test);
// => 'undefined'Use delete to delete a property from process.env.
import { env } from 'node:process';

env.TEST = 1;
delete env.TEST;
console.log(env.TEST);
// => undefinedOn Windows operating systems, environment variables are case-insensitive.
import { env } from 'node:process';

env.TEST = 1;
console.log(env.test);
// => 1Unless explicitly specified when creating a Worker instance,
each Worker thread has its own copy of process.env, based on its
parent thread's process.env, or whatever was specified as the env option
to the Worker constructor. Changes to process.env will not be visible
across Worker threads, and only the main thread can make changes that
are visible to the operating system or to native add-ons. On Windows, a copy of process.env on a Worker instance operates in a case-sensitive manner
unlike the main thread.
@sincev0.1.27env.string | undefinedVITEST
		? {
				EnvironmentResolveOptions.conditions?: string[] | undefinedconditions: ['browser']
			}
		: var undefinedundefined
});
```

> If loading the browser version of all your packages is undesirable, because (for example) you also test backend libraries, [you may need to resort to an alias configuration](https://github.com/testing-library/svelte-testing-library/issues/222#issuecomment-1909993331)

You can now write unit tests for code inside your `.js/.ts` files:

multiplier.svelte.test

```
import { function flushSync<T = void>(fn?: (() => T) | undefined): TSynchronously flush any pending updates.
Returns void if no callback is provided, otherwise returns the result of calling the callback.
referenceflushSync } from 'svelte';
import { const expect: ExpectStaticexpect, const test: TestAPIDefines a test case with a given name and test function. The test function can optionally be configured with test options.
@paramname - The name of the test or a function that will be used as a test name.@paramoptionsOrFn - Optional. The test options or the test function if no explicit name is provided.@paramoptionsOrTest - Optional. The test function or options, depending on the previous parameters.@throwsError If called inside another test function.@example// Define a simple test
test('should add two numbers', () => {
  expect(add(1, 2)).toBe(3);
});@example// Define a test with options
test('should subtract two numbers', { retry: 3 }, () => {
  expect(subtract(5, 2)).toBe(3);
});test } from 'vitest';
import { import multipliermultiplier } from './multiplier.svelte.js';

test<object>(name: string | Function, fn?: TestFunction<object> | undefined, options?: number): void (+1 overload)Defines a test case with a given name and test function. The test function can optionally be configured with test options.
@paramname - The name of the test or a function that will be used as a test name.@paramoptionsOrFn - Optional. The test options or the test function if no explicit name is provided.@paramoptionsOrTest - Optional. The test function or options, depending on the previous parameters.@throwsError If called inside another test function.@example// Define a simple test
test('should add two numbers', () => {
  expect(add(1, 2)).toBe(3);
});@example// Define a test with options
test('should subtract two numbers', { retry: 3 }, () => {
  expect(subtract(5, 2)).toBe(3);
});test('Multiplier', () => {
	let let double: anydouble = import multipliermultiplier(0, 2);

	expect<any>(actual: any, message?: string): Assertion<any> (+1 overload)expect(let double: anydouble.value).JestAssertion<any>.toEqual: <number>(expected: number) => voidUsed when you want to check that two objects have the same value.
This matcher recursively checks the equality of all fields, rather than checking for object identity.
@exampleexpect(user).toEqual({ name: 'Alice', age: 30 });
toEqual(0);

	let double: anydouble.set(5);

	expect<any>(actual: any, message?: string): Assertion<any> (+1 overload)expect(let double: anydouble.value).JestAssertion<any>.toEqual: <number>(expected: number) => voidUsed when you want to check that two objects have the same value.
This matcher recursively checks the equality of all fields, rather than checking for object identity.
@exampleexpect(user).toEqual({ name: 'Alice', age: 30 });
toEqual(10);
});
```

multiplier.svelte

```
/**
 * @param {number} initial
 * @param {number} k
 */
export function function multiplier(initial: number, k: number): {
    readonly value: number;
    set: (c: number) => void;
}@paraminitial @paramk multiplier(initial: number@paraminitial initial, k: number@paramk k) {
	let let count: numbercount = function $state<number>(initial: number): number (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state(initial: number@paraminitial initial);

	return {
		get value: numbervalue() {
			return let count: numbercount * k: number@paramk k;
		},
		/** @param {number} c */
		set: (c: number) => void@paramc set: (c: number@paramc c) => {
			let count: numbercount = c: number@paramc c;
		}
	};
}
```

```
export function function multiplier(initial: number, k: number): {
    readonly value: number;
    set: (c: number) => void;
}multiplier(initial: numberinitial: number, k: numberk: number) {
	let let count: numbercount = function $state<number>(initial: number): number (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state(initial: numberinitial);

	return {
		get value: numbervalue() {
			return let count: numbercount * k: numberk;
		},

		set: (c: number) => voidset: (c: numberc: number) => {
			let count: numbercount = c: numberc;
		}
	};
}
```

### Using runes inside your test files[](#Unit-and-component-tests-with-Vitest-Using-runes-inside-your-test-files)

Since Vitest processes your test files the same way as your source files, you can use runes inside your tests as long as the filename includes `.svelte`:

multiplier.svelte.test

```
import { function flushSync<T = void>(fn?: (() => T) | undefined): TSynchronously flush any pending updates.
Returns void if no callback is provided, otherwise returns the result of calling the callback.
referenceflushSync } from 'svelte';
import { const expect: ExpectStaticexpect, const test: TestAPIDefines a test case with a given name and test function. The test function can optionally be configured with test options.
@paramname - The name of the test or a function that will be used as a test name.@paramoptionsOrFn - Optional. The test options or the test function if no explicit name is provided.@paramoptionsOrTest - Optional. The test function or options, depending on the previous parameters.@throwsError If called inside another test function.@example// Define a simple test
test('should add two numbers', () => {
  expect(add(1, 2)).toBe(3);
});@example// Define a test with options
test('should subtract two numbers', { retry: 3 }, () => {
  expect(subtract(5, 2)).toBe(3);
});test } from 'vitest';
import { import multipliermultiplier } from './multiplier.svelte.js';

test<object>(name: string | Function, fn?: TestFunction<object> | undefined, options?: number): void (+1 overload)Defines a test case with a given name and test function. The test function can optionally be configured with test options.
@paramname - The name of the test or a function that will be used as a test name.@paramoptionsOrFn - Optional. The test options or the test function if no explicit name is provided.@paramoptionsOrTest - Optional. The test function or options, depending on the previous parameters.@throwsError If called inside another test function.@example// Define a simple test
test('should add two numbers', () => {
  expect(add(1, 2)).toBe(3);
});@example// Define a test with options
test('should subtract two numbers', { retry: 3 }, () => {
  expect(subtract(5, 2)).toBe(3);
});test('Multiplier', () => {
	let let count: numbercount = function $state<0>(initial: 0): 0 (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state(0);
	let let double: anydouble = import multipliermultiplier(() => let count: numbercount, 2);

	expect<any>(actual: any, message?: string): Assertion<any> (+1 overload)expect(let double: anydouble.value).JestAssertion<any>.toEqual: <number>(expected: number) => voidUsed when you want to check that two objects have the same value.
This matcher recursively checks the equality of all fields, rather than checking for object identity.
@exampleexpect(user).toEqual({ name: 'Alice', age: 30 });
toEqual(0);

	let count: numbercount = 5;

	expect<any>(actual: any, message?: string): Assertion<any> (+1 overload)expect(let double: anydouble.value).JestAssertion<any>.toEqual: <number>(expected: number) => voidUsed when you want to check that two objects have the same value.
This matcher recursively checks the equality of all fields, rather than checking for object identity.
@exampleexpect(user).toEqual({ name: 'Alice', age: 30 });
toEqual(10);
});
```

multiplier.svelte

```
/**
 * @param {() => number} getCount
 * @param {number} k
 */
export function function multiplier(getCount: () => number, k: number): {
    readonly value: number;
}@paramgetCount @paramk multiplier(getCount: () => number@paramgetCount getCount, k: number@paramk k) {
	return {
		get value: numbervalue() {
			return getCount: () => number@paramgetCount getCount() * k: number@paramk k;
		}
	};
}
```

```
export function function multiplier(getCount: () => number, k: number): {
    readonly value: number;
}multiplier(getCount: () => numbergetCount: () => number, k: numberk: number) {
	return {
		get value: numbervalue() {
			return getCount: () => numbergetCount() * k: numberk;
		}
	};
}
```

If the code being tested uses effects, you need to wrap the test inside `$effect.root`:

logger.svelte.test

```
import { function flushSync<T = void>(fn?: (() => T) | undefined): TSynchronously flush any pending updates.
Returns void if no callback is provided, otherwise returns the result of calling the callback.
referenceflushSync } from 'svelte';
import { const expect: ExpectStaticexpect, const test: TestAPIDefines a test case with a given name and test function. The test function can optionally be configured with test options.
@paramname - The name of the test or a function that will be used as a test name.@paramoptionsOrFn - Optional. The test options or the test function if no explicit name is provided.@paramoptionsOrTest - Optional. The test function or options, depending on the previous parameters.@throwsError If called inside another test function.@example// Define a simple test
test('should add two numbers', () => {
  expect(add(1, 2)).toBe(3);
});@example// Define a test with options
test('should subtract two numbers', { retry: 3 }, () => {
  expect(subtract(5, 2)).toBe(3);
});test } from 'vitest';
import { import loggerlogger } from './logger.svelte.js';

test<object>(name: string | Function, fn?: TestFunction<object> | undefined, options?: number): void (+1 overload)Defines a test case with a given name and test function. The test function can optionally be configured with test options.
@paramname - The name of the test or a function that will be used as a test name.@paramoptionsOrFn - Optional. The test options or the test function if no explicit name is provided.@paramoptionsOrTest - Optional. The test function or options, depending on the previous parameters.@throwsError If called inside another test function.@example// Define a simple test
test('should add two numbers', () => {
  expect(add(1, 2)).toBe(3);
});@example// Define a test with options
test('should subtract two numbers', { retry: 3 }, () => {
  expect(subtract(5, 2)).toBe(3);
});test('Effect', () => {
	const const cleanup: () => voidcleanup = namespace $effect
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
		let let count: numbercount = function $state<0>(initial: 0): 0 (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state(0);

		// logger uses an $effect to log updates of its input
		let let log: anylog = import loggerlogger(() => let count: numbercount);

		// effects normally run after a microtask,
		// use flushSync to execute all pending effects synchronously
		flushSync<void>(fn?: (() => void) | undefined): voidSynchronously flush any pending updates.
Returns void if no callback is provided, otherwise returns the result of calling the callback.
referenceflushSync();
		expect<any>(actual: any, message?: string): Assertion<any> (+1 overload)expect(let log: anylog).JestAssertion<any>.toEqual: <number[]>(expected: number[]) => voidUsed when you want to check that two objects have the same value.
This matcher recursively checks the equality of all fields, rather than checking for object identity.
@exampleexpect(user).toEqual({ name: 'Alice', age: 30 });
toEqual([0]);

		let count: numbercount = 1;
		flushSync<void>(fn?: (() => void) | undefined): voidSynchronously flush any pending updates.
Returns void if no callback is provided, otherwise returns the result of calling the callback.
referenceflushSync();

		expect<any>(actual: any, message?: string): Assertion<any> (+1 overload)expect(let log: anylog).JestAssertion<any>.toEqual: <number[]>(expected: number[]) => voidUsed when you want to check that two objects have the same value.
This matcher recursively checks the equality of all fields, rather than checking for object identity.
@exampleexpect(user).toEqual({ name: 'Alice', age: 30 });
toEqual([0, 1]);
	});

	const cleanup: () => voidcleanup();
});
```

logger.svelte

```
/**
 * @param {() => any} getValue
 */
export function function logger(getValue: () => any): any[]@paramgetValue logger(getValue: () => any@paramgetValue getValue) {
	/** @type {any[]} */
	let let log: any[]@type{any[]}log = [];

	function $effect(fn: () => void | (() => void)): void
namespace $effectRuns code when a component is mounted to the DOM, and then whenever its dependencies change, i.e. $state or $derived values.
The timing of the execution is after the DOM has been updated.
Example:
$effect(() => console.log('The count is now ' + count));If you return a function from the effect, it will be called right before the effect is run again, or when the component is unmounted.
Does not run during server-side rendering.
@see{@link https://svelte.dev/docs/svelte/$effect Documentation}@paramfn The function to execute$effect(() => {
		let log: any[]@type{any[]}log.Array<any>.push(...items: any[]): numberAppends new elements to the end of an array, and returns the new length of the array.
@paramitems New elements to add to the array.push(getValue: () => any@paramgetValue getValue());
	});

	return let log: any[]@type{any[]}log;
}
```

```
export function function logger(getValue: () => any): any[]logger(getValue: () => anygetValue: () => any) {
	let let log: any[]log: any[] = [];

	function $effect(fn: () => void | (() => void)): void
namespace $effectRuns code when a component is mounted to the DOM, and then whenever its dependencies change, i.e. $state or $derived values.
The timing of the execution is after the DOM has been updated.
Example:
$effect(() => console.log('The count is now ' + count));If you return a function from the effect, it will be called right before the effect is run again, or when the component is unmounted.
Does not run during server-side rendering.
@see{@link https://svelte.dev/docs/svelte/$effect Documentation}@paramfn The function to execute$effect(() => {
		let log: any[]log.Array<any>.push(...items: any[]): numberAppends new elements to the end of an array, and returns the new length of the array.
@paramitems New elements to add to the array.push(getValue: () => anygetValue());
	});

	return let log: any[]log;
}
```

### Component testing[](#Unit-and-component-tests-with-Vitest-Component-testing)

It is possible to test your components in isolation, which allows you to render them in a browser (real or simulated), simulate behavior, and make assertions, without spinning up your whole app.

> Before writing component tests, think about whether you actually need to test the component, or if it's more about the logic _inside_ the component. If so, consider extracting out that logic to test it in isolation, without the overhead of a component.

To get started, install jsdom (a library that shims DOM APIs):

```
npm install -D jsdom
```

Then adjust your `vite.config.js`:

vite.config

```
import { function defineConfig(config: UserConfig): UserConfig (+4 overloads)defineConfig } from 'vitest/config';

export default function defineConfig(config: UserConfig): UserConfig (+4 overloads)defineConfig({
	UserConfig.plugins?: PluginOption[] | undefinedArray of vite plugins to use.
plugins: [
		/* ... */
	],
	UserConfig.test?: InlineConfig | undefinedOptions for Vitest
test: {
		// If you are testing components client-side, you need to set up a DOM environment.
		// If not all your files should have this environment, you can use a
		// `// @vitest-environment jsdom` comment at the top of the test files instead.
		InlineConfig.environment?: VitestEnvironment | undefinedRunning environment
Supports 'node', 'jsdom', 'happy-dom', 'edge-runtime'
If used unsupported string, will try to load the package vitest-environment-${env}
@default'node'environment: 'jsdom'
	},
	// Tell Vitest to use the `browser` entry points in `package.json` files, even though it's running in Node
	resolve?: AllResolveOptions | undefinedresolve: var process: NodeJS.Processprocess.NodeJS.Process.env: NodeJS.ProcessEnvThe process.env property returns an object containing the user environment.
See environ(7).
An example of this object looks like:
{
  TERM: 'xterm-256color',
  SHELL: '/usr/local/bin/bash',
  USER: 'maciej',
  PATH: '~/.bin/:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin',
  PWD: '/Users/maciej',
  EDITOR: 'vim',
  SHLVL: '1',
  HOME: '/Users/maciej',
  LOGNAME: 'maciej',
  _: '/usr/local/bin/node'
}It is possible to modify this object, but such modifications will not be
reflected outside the Node.js process, or (unless explicitly requested)
to other Worker threads.
In other words, the following example would not work:
node -e 'process.env.foo = "bar"' && echo $fooWhile the following will:
import { env } from 'node:process';

env.foo = 'bar';
console.log(env.foo);Assigning a property on process.env will implicitly convert the value
to a string. This behavior is deprecated. Future versions of Node.js may
throw an error when the value is not a string, number, or boolean.
import { env } from 'node:process';

env.test = null;
console.log(env.test);
// => 'null'
env.test = undefined;
console.log(env.test);
// => 'undefined'Use delete to delete a property from process.env.
import { env } from 'node:process';

env.TEST = 1;
delete env.TEST;
console.log(env.TEST);
// => undefinedOn Windows operating systems, environment variables are case-insensitive.
import { env } from 'node:process';

env.TEST = 1;
console.log(env.test);
// => 1Unless explicitly specified when creating a Worker instance,
each Worker thread has its own copy of process.env, based on its
parent thread's process.env, or whatever was specified as the env option
to the Worker constructor. Changes to process.env will not be visible
across Worker threads, and only the main thread can make changes that
are visible to the operating system or to native add-ons. On Windows, a copy of process.env on a Worker instance operates in a case-sensitive manner
unlike the main thread.
@sincev0.1.27env.string | undefinedVITEST
		? {
				EnvironmentResolveOptions.conditions?: string[] | undefinedconditions: ['browser']
			}
		: var undefinedundefined
});
```

After that, you can create a test file in which you import the component to test, interact with it programmatically and write expectations about the results:

component.test

```
import { function flushSync<T = void>(fn?: (() => T) | undefined): TSynchronously flush any pending updates.
Returns void if no callback is provided, otherwise returns the result of calling the callback.
referenceflushSync, function mount<Props extends Record<string, any>, Exports extends Record<string, any>>(component: ComponentType<SvelteComponent<Props>> | Component<Props, Exports, any>, options: MountOptions<Props>): ExportsMounts a component to the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component.
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
import type Component = SvelteComponent<Record<string, any>, any, any>
const Component: LegacyComponentTypeComponent from './Component.svelte';

test<object>(name: string | Function, fn?: TestFunction<object> | undefined, options?: number): void (+1 overload)Defines a test case with a given name and test function. The test function can optionally be configured with test options.
@paramname - The name of the test or a function that will be used as a test name.@paramoptionsOrFn - Optional. The test options or the test function if no explicit name is provided.@paramoptionsOrTest - Optional. The test function or options, depending on the previous parameters.@throwsError If called inside another test function.@example// Define a simple test
test('should add two numbers', () => {
  expect(add(1, 2)).toBe(3);
});@example// Define a test with options
test('should subtract two numbers', { retry: 3 }, () => {
  expect(subtract(5, 2)).toBe(3);
});test('Component', () => {
	// Instantiate the component using Svelte's `mount` API
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
referencemount(const Component: LegacyComponentTypeComponent, {
		target: Document | Element | ShadowRootTarget element where the component will be mounted.
target: var document: Documentwindow.document returns a reference to the document contained in the window.
MDN Reference
document.Document.body: HTMLElementThe Document.body property represents the null if no such element exists.
MDN Reference
body, // `document` exists because of jsdom
		props?: Record<string, any> | undefinedComponent properties.
props: { initial: numberinitial: 0 }
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
toBe('<button>0</button>');

	// Click the button, then flush the changes so you can synchronously write expectations
	var document: Documentwindow.document returns a reference to the document contained in the window.
MDN Reference
document.Document.body: HTMLElementThe Document.body property represents the null if no such element exists.
MDN Reference
body.ParentNode.querySelector<"button">(selectors: "button"): HTMLButtonElement | null (+4 overloads)Returns the first element that is a descendant of node that matches selectors.
MDN Reference
querySelector('button').HTMLElement.click(): voidThe HTMLElement.click() method simulates a mouse click on an element.
MDN Reference
click();
	flushSync<void>(fn?: (() => void) | undefined): voidSynchronously flush any pending updates.
Returns void if no callback is provided, otherwise returns the result of calling the callback.
referenceflushSync();

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
toBe('<button>1</button>');

	// Remove the component from the DOM
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

While the process is very straightforward, it is also low level and somewhat brittle, as the precise structure of your component may change frequently. Tools like [@testing-library/svelte](https://testing-library.com/docs/svelte-testing-library/intro/) can help streamline your tests. The above test could be rewritten like this:

component.test

```
import { function render<C extends Component<any, any, string> | SvelteComponent<any, any, any>, Q extends Queries = typeof import("/vercel/path0/node_modules/.pnpm/@testing-library+dom@10.4.1/node_modules/@testing-library/dom/types/queries")>(Component: ComponentImport<C>, options?: ComponentOptions<C>, renderOptions?: RenderOptions<Q>): RenderResult<C, Q>Render a component into the document.
@template{import('@testing-library/svelte-core/types').Component} C@template{DomTestingLibrary.Queries} [Q=typeof DomTestingLibrary.queries]@paramComponent - The component to render.@paramoptions - Customize how Svelte renders the component.@paramrenderOptions - Customize how Testing Library sets up the document and binds queries.@returnsThe rendered component and bound testing functions.render, const screen: Screen<typeof import("/vercel/path0/node_modules/.pnpm/@testing-library+dom@10.4.1/node_modules/@testing-library/dom/types/queries")>screen } from '@testing-library/svelte';
import const userEvent: {
    readonly setup: typeof setupMain;
    readonly clear: typeof clear;
    readonly click: typeof click;
    readonly copy: typeof copy;
    readonly cut: typeof cut;
    readonly dblClick: typeof dblClick;
    readonly deselectOptions: typeof deselectOptions;
    readonly hover: typeof hover;
    readonly keyboard: typeof keyboard;
    ... 7 more ...;
    readonly tab: typeof tab;
}userEvent from '@testing-library/user-event';
import { const expect: ExpectStaticexpect, const test: TestAPIDefines a test case with a given name and test function. The test function can optionally be configured with test options.
@paramname - The name of the test or a function that will be used as a test name.@paramoptionsOrFn - Optional. The test options or the test function if no explicit name is provided.@paramoptionsOrTest - Optional. The test function or options, depending on the previous parameters.@throwsError If called inside another test function.@example// Define a simple test
test('should add two numbers', () => {
  expect(add(1, 2)).toBe(3);
});@example// Define a test with options
test('should subtract two numbers', { retry: 3 }, () => {
  expect(subtract(5, 2)).toBe(3);
});test } from 'vitest';
import type Component = SvelteComponent<Record<string, any>, any, any>
const Component: LegacyComponentTypeComponent from './Component.svelte';

test<object>(name: string | Function, fn?: TestFunction<object> | undefined, options?: number): void (+1 overload)Defines a test case with a given name and test function. The test function can optionally be configured with test options.
@paramname - The name of the test or a function that will be used as a test name.@paramoptionsOrFn - Optional. The test options or the test function if no explicit name is provided.@paramoptionsOrTest - Optional. The test function or options, depending on the previous parameters.@throwsError If called inside another test function.@example// Define a simple test
test('should add two numbers', () => {
  expect(add(1, 2)).toBe(3);
});@example// Define a test with options
test('should subtract two numbers', { retry: 3 }, () => {
  expect(subtract(5, 2)).toBe(3);
});test('Component', async () => {
	const const user: UserEventuser = const userEvent: {
    readonly setup: typeof setupMain;
    readonly clear: typeof clear;
    readonly click: typeof click;
    readonly copy: typeof copy;
    readonly cut: typeof cut;
    readonly dblClick: typeof dblClick;
    readonly deselectOptions: typeof deselectOptions;
    readonly hover: typeof hover;
    readonly keyboard: typeof keyboard;
    ... 7 more ...;
    readonly tab: typeof tab;
}userEvent.setup: (options?: Options) => UserEventStart a "session" with userEvent.
All APIs returned by this function share an input device state and a default configuration.
setup();
	render<SvelteComponent<Record<string, any>, any, any>, typeof import("/vercel/path0/node_modules/.pnpm/@testing-library+dom@10.4.1/node_modules/@testing-library/dom/types/queries")>(Component: ComponentImport<SvelteComponent<Record<string, any>, any, any>>, options?: ComponentOptions<SvelteComponent<Record<string, any>, any, any>> | undefined, renderOptions?: RenderOptions<typeof import("/vercel/path0/node_modules/.pnpm/@testing-library+dom@10.4.1/node_modules/@testing-library/dom/types/queries")> | undefined): RenderResult<...>Render a component into the document.
@template{import('@testing-library/svelte-core/types').Component} C@template{DomTestingLibrary.Queries} [Q=typeof DomTestingLibrary.queries]@paramComponent - The component to render.@paramoptions - Customize how Svelte renders the component.@paramrenderOptions - Customize how Testing Library sets up the document and binds queries.@returnsThe rendered component and bound testing functions.render(const Component: LegacyComponentTypeComponent);

	const const button: HTMLElementbutton = const screen: Screen<typeof import("/vercel/path0/node_modules/.pnpm/@testing-library+dom@10.4.1/node_modules/@testing-library/dom/types/queries")>screen.getByRole<HTMLElement>(role: ByRoleMatcher, options?: ByRoleOptions | undefined): HTMLElement (+1 overload)getByRole('button');
	expect<HTMLElement>(actual: HTMLElement, message?: string): Assertion<HTMLElement> (+1 overload)expect(const button: HTMLElementbutton).toHaveTextContent(0);

	await const user: UserEventuser.click: (element: Element) => Promise<void>click(const button: HTMLElementbutton);
	expect<HTMLElement>(actual: HTMLElement, message?: string): Assertion<HTMLElement> (+1 overload)expect(const button: HTMLElementbutton).toHaveTextContent(1);
});
```

When writing component tests that involve two-way bindings, context or snippet props, it's best to create a wrapper component for your specific test and interact with that. `@testing-library/svelte` contains some [examples](https://testing-library.com/docs/svelte-testing-library/example).

## Component tests with Storybook[](#Component-tests-with-Storybook)

[Storybook](https://storybook.js.org) is a tool for developing and documenting UI components, and it can also be used to test your components. They're run with Vitest's browser mode, which renders your components in a real browser for the most realistic testing environment.

To get started, first install Storybook ([using Svelte's CLI](/docs/cli/storybook)) in your project via `npx sv add storybook` and choose the recommended configuration that includes testing features. If you're already using Storybook, and for more information on Storybook's testing capabilities, follow the [Storybook testing docs](https://storybook.js.org/docs/writing-tests?renderer=svelte) to get started.

You can create stories for component variations and test interactions with the [play function](https://storybook.js.org/docs/writing-tests/interaction-testing?renderer=svelte#writing-interaction-tests), which allows you to simulate behavior and make assertions using the Testing Library and Vitest APIs. Here's an example of two stories that can be tested, one that renders an empty LoginForm component and one that simulates a user filling out the form:

LoginForm.stories

```
<script module>
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, fn } from 'storybook/test';

	import LoginForm from './LoginForm.svelte';

	const { Story } = defineMeta({
		component: LoginForm,
		args: {
			// Pass a mock function to the `onSubmit` prop
			onSubmit: fn(),
		}
	});
</script>
 
<Story name="Empty Form" />
 
<Story
	name="Filled Form"
	play={async ({ args, canvas, userEvent }) => {
		// Simulate a user filling out the form
		await userEvent.type(canvas.getByTestId('email'), 'email@provider.com');
		await userEvent.type(canvas.getByTestId('password'), 'a-random-password');
		await userEvent.click(canvas.getByRole('button'));

		// Run assertions
		await expect(args.onSubmit).toHaveBeenCalledTimes(1);
		await expect(canvas.getByText('You’re in!')).toBeInTheDocument();
	}}
/>
```

## End-to-end tests with Playwright[](#End-to-end-tests-with-Playwright)

E2E (short for 'end to end') tests allow you to test your full application through the eyes of the user. This section uses [Playwright](https://playwright.dev/) as an example, but you can also use other solutions like [Cypress](https://www.cypress.io/) or [NightwatchJS](https://nightwatchjs.org/).

You can use the Svelte CLI to [setup Playwright](/docs/cli/playwright) either during project creation or later on. You can also [set it up with `npm init playwright`](https://playwright.dev/docs/intro). Additionally, you may also want to install an IDE plugin such as [the VS Code extension](https://playwright.dev/docs/getting-started-vscode) to be able to execute tests from inside your IDE.

If you've run `npm init playwright` or are not using Vite, you may need to adjust the Playwright config to tell Playwright what to do before running the tests — mainly starting your application at a certain port. For example:

playwright.config

```
const const config: {
    webServer: {
        command: string;
        port: number;
    };
    testDir: string;
    testMatch: RegExp;
}config = {
	webServer: {
    command: string;
    port: number;
}webServer: {
		command: stringcommand: 'npm run build && npm run preview',
		port: numberport: 4173
	},
	testDir: stringtestDir: 'tests',
	testMatch: RegExptestMatch: /(.+\.)?(test|spec)\.[jt]s/
};

export default const config: {
    webServer: {
        command: string;
        port: number;
    };
    testDir: string;
    testMatch: RegExp;
}config;
```

You can now start writing tests. These are totally unaware of Svelte as a framework, so you mainly interact with the DOM and write assertions.

tests/hello-world.spec

```
import { import expectexpect, import testtest } from '@playwright/test';

import testtest('home page has expected h1', async ({ page }) => {
	await page: anypage.goto('/');
	await import expectexpect(page: anypage.locator('h1')).toBeVisible();
});
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/07-misc/02-testing.md) [llms.txt](/docs/svelte/testing/llms.txt)

previous next

[Best practices](/docs/svelte/best-practices) [TypeScript](/docs/svelte/typescript)


