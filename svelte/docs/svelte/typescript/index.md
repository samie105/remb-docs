---
title: "TypeScript"
source: "https://svelte.dev/docs/svelte/typescript"
canonical_url: "https://svelte.dev/docs/svelte/typescript"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:05.902Z"
content_hash: "9839f72fb608911a6daf7030e8e21441df10d35ef6e9fe36b7ecfaad9e10ff15"
menu_path: ["TypeScript"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/testing/index.md", "title": "Testing"}
nav_next: {"path": "svelte/docs/svelte/custom-elements/index.md", "title": "Custom elements"}
---

You can use TypeScript within Svelte components. IDE extensions like the [Svelte VS Code extension](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode) will help you catch errors right in your editor, and [`svelte-check`](https://www.npmjs.com/package/svelte-check) does the same on the command line, which you can integrate into your CI.

## <script lang="ts">[](#script-lang-ts)

To use TypeScript inside your Svelte components, add `lang="ts"` to your `script` tags:

```
<script lang="ts">
	let name: string = 'world';

	function greet(name: string) {
		alert(`Hello, ${name}!`);
	}
</script>

<button onclick={(e: Event) => greet(e.target.innerText)}>
	{name as string}
</button>
```

Doing so allows you to use TypeScript's _type-only_ features. That is, all features that just disappear when transpiling to JavaScript, such as type annotations or interface declarations. Features that require the TypeScript compiler to output actual code are not supported. This includes:

*   using enums
*   using `private`, `protected` or `public` modifiers in constructor functions together with initializers
*   using features that are not yet part of the ECMAScript standard (i.e. not level 4 in the TC39 process) and therefore not implemented yet within Acorn, the parser we use for parsing JavaScript

If you want to use one of these features, you need to setup up a `script` preprocessor.

## Preprocessor setup[](#Preprocessor-setup)

To use non-type-only TypeScript features within Svelte components, you need to add a preprocessor that will turn TypeScript into JavaScript.

### Using Vite[](#Preprocessor-setup-Using-Vite)

If you're using SvelteKit, or Vite _without_ SvelteKit, you can use `vitePreprocess` from `@sveltejs/vite-plugin-svelte` in your config file:

svelte.config

```
import { function vitePreprocess(opts?: VitePreprocessOptions): import("svelte/compiler").PreprocessorGroupvitePreprocess } from '@sveltejs/vite-plugin-svelte';

const const config: {
    preprocess: PreprocessorGroup;
}config = {
	// Note the additional `{ script: true }`
	preprocess: PreprocessorGrouppreprocess: function vitePreprocess(opts?: VitePreprocessOptions): import("svelte/compiler").PreprocessorGroupvitePreprocess({ VitePreprocessOptions.script?: boolean | undefinedpreprocess script block with vite pipeline.
Since svelte5 this is not needed for typescript anymore
@defaultfalsescript: true })
};

export default const config: {
    preprocess: PreprocessorGroup;
}config;
```

### Using other build tools[](#Preprocessor-setup-Using-other-build-tools)

If you're using tools like Rollup (via [rollup-plugin-svelte](https://github.com/sveltejs/rollup-plugin-svelte)) or Webpack (via [svelte-loader](https://github.com/sveltejs/svelte-loader)) instead, install `typescript` and `svelte-preprocess` and add the preprocessor to the plugin config. See the respective plugin READMEs for more info.

> If you're starting a new project, we recommend using SvelteKit or Vite instead

## tsconfig.json settings[](#tsconfig.json-settings)

When using TypeScript, make sure your `tsconfig.json` is setup correctly.

*   Use a [`target`](https://www.typescriptlang.org/tsconfig/#target) of at least `ES2015` so classes are not compiled to functions
*   Set [`verbatimModuleSyntax`](https://www.typescriptlang.org/tsconfig/#verbatimModuleSyntax) to `true` so that imports are left as-is
*   Set [`isolatedModules`](https://www.typescriptlang.org/tsconfig/#isolatedModules) to `true` so that each file is looked at in isolation. TypeScript has a few features which require cross-file analysis and compilation, which the Svelte compiler and tooling like Vite don't do.

## Typing $props[](#Typing-$props)

Type `$props` just like a regular object with certain properties.

```
<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		requiredProperty: number;
		optionalProperty?: boolean;
		snippetWithStringArgument: Snippet<[string]>;
		eventHandler: (arg: string) => void;
		[key: string]: unknown;
	}

	let {
		requiredProperty,
		optionalProperty,
		snippetWithStringArgument,
		eventHandler,
		...everythingElse
	}: Props = $props();
</script>

<button onclick={() => eventHandler('clicked button')}>
	{@render snippetWithStringArgument('hello')}
</button>
```

## Generic $props[](#Generic-$props)

Components can declare a generic relationship between their properties. One example is a generic list component that receives a list of items and a callback property that receives an item from the list. To declare that the `items` property and the `select` callback operate on the same types, add the `generics` attribute to the `script` tag:

```
<script lang="ts" generics="Item extends { text: string }">
	interface Props {
		items: Item[];
		select(item: Item): void;
	}

	let { items, select }: Props = $props();
</script>

{#each items as item}
	<button onclick={() => select(item)}>
		{item.text}
	</button>
{/each}
```

The content of `generics` is what you would put between the `<...>` tags of a generic function. In other words, you can use multiple generics, `extends` and fallback types.

## Typing wrapper components[](#Typing-wrapper-components)

In case you're writing a component that wraps a native element, you may want to expose all the attributes of the underlying element to the user. In that case, use (or extend from) one of the interfaces provided by `svelte/elements`. Here's an example for a `Button` component:

```
<script lang="ts">
	import type { HTMLButtonAttributes } from 'svelte/elements';

	let { children, ...rest }: HTMLButtonAttributes = $props();
</script>

<button {...rest}>
	{@render children?.()}
</button>
```

Not all elements have a dedicated type definition. For those without one, use `SvelteHTMLElements`:

```
<script lang="ts">
	import type { SvelteHTMLElements } from 'svelte/elements';

	let { children, ...rest }: SvelteHTMLElements['div'] = $props();
</script>

<div {...rest}>
	{@render children?.()}
</div>
```

## Typing $state[](#Typing-$state)

You can type `$state` like any other variable.

```
let let count: numbercount: number = function $state<0>(initial: 0): 0 (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state(0);
```

If you don't give `$state` an initial value, part of its types will be `undefined`.

```
// Error: Type 'number | undefined' is not assignable to type 'number'
let let count: numbercount: number = function $state<number>(): number | undefined (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state();
```

If you know that the variable _will_ be defined before you first use it, use an `as` casting. This is especially useful in the context of classes:

```
class class CounterCounter {
	Counter.count: numbercount = function $state<number>(): number | undefined (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state() as number;
	constructor(initial: numberinitial: number) {
		this.Counter.count: numbercount = initial: numberinitial;
	}
}
```

## The Component type[](#The-Component-type)

Svelte components are of type `Component`. You can use it and its related types to express a variety of constraints.

Using it together with dynamic components to restrict what kinds of component can be passed to it:

```
<script lang="ts">
	import type { Component } from 'svelte';

	interface Props {
		// only components that have at most the "prop"
		// property required can be passed
		DynamicComponent: Component<{ prop: string }>;
	}

	let { DynamicComponent }: Props = $props();
</script>

<DynamicComponent prop="foo" />
```

> Legacy mode
> 
> In Svelte 4, components were of type `SvelteComponent`

To extract the properties from a component, use `ComponentProps`.

```
import type { interface Component<Props extends Record<string, any> = {}, Exports extends Record<string, any> = {}, Bindings extends keyof Props | "" = string>Can be used to create strongly typed Svelte components.
Example:You have component library on npm called component-library, from which
you export a component called MyComponent. For Svelte+TypeScript users,
you want to provide typings. Therefore you create a index.d.ts:
import type { Component } from 'svelte';
export declare const MyComponent: Component<{ foo: string }> {}Typing this makes it possible for IDEs like VS Code with the Svelte extension
to provide intellisense and to use the component like this in a Svelte file
with TypeScript:
<script lang="ts">
	import { MyComponent } from "component-library";
</script>
<MyComponent foo={'bar'} />Component, type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const props: ComponentProps<typeof MyComponent> = { foo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { Component, ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

function withProps<TComponent extends Component<any>>(
	component: TComponent,
	props: ComponentProps<TComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
withProps(MyComponent, { foo: 'bar' });referenceComponentProps } from 'svelte';
import type MyComponent = SvelteComponent<Record<string, any>, any, any>
const MyComponent: LegacyComponentTypeMyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const const props: Record<string, any>props: type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const props: ComponentProps<typeof MyComponent> = { foo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { Component, ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

function withProps<TComponent extends Component<any>>(
	component: TComponent,
	props: ComponentProps<TComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
withProps(MyComponent, { foo: 'bar' });referenceComponentProps<typeof const MyComponent: LegacyComponentTypeMyComponent> = { foo: stringfoo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { interface Component<Props extends Record<string, any> = {}, Exports extends Record<string, any> = {}, Bindings extends keyof Props | "" = string>Can be used to create strongly typed Svelte components.
Example:You have component library on npm called component-library, from which
you export a component called MyComponent. For Svelte+TypeScript users,
you want to provide typings. Therefore you create a index.d.ts:
import type { Component } from 'svelte';
export declare const MyComponent: Component<{ foo: string }> {}Typing this makes it possible for IDEs like VS Code with the Svelte extension
to provide intellisense and to use the component like this in a Svelte file
with TypeScript:
<script lang="ts">
	import { MyComponent } from "component-library";
</script>
<MyComponent foo={'bar'} />Component, type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const props: ComponentProps<typeof MyComponent> = { foo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { Component, ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

function withProps<TComponent extends Component<any>>(
	component: TComponent,
	props: ComponentProps<TComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
withProps(MyComponent, { foo: 'bar' });ComponentProps } from 'svelte';
import type MyComponent = SvelteComponent<Record<string, any>, any, any>
const MyComponent: LegacyComponentTypeMyComponent from './MyComponent.svelte';

function function withProps<TComponent extends Component<any>>(component: TComponent, props: ComponentProps<TComponent>): voidwithProps<function (type parameter) TComponent in withProps<TComponent extends Component<any>>(component: TComponent, props: ComponentProps<TComponent>): voidTComponent extends interface Component<Props extends Record<string, any> = {}, Exports extends Record<string, any> = {}, Bindings extends keyof Props | "" = string>Can be used to create strongly typed Svelte components.
Example:You have component library on npm called component-library, from which
you export a component called MyComponent. For Svelte+TypeScript users,
you want to provide typings. Therefore you create a index.d.ts:
import type { Component } from 'svelte';
export declare const MyComponent: Component<{ foo: string }> {}Typing this makes it possible for IDEs like VS Code with the Svelte extension
to provide intellisense and to use the component like this in a Svelte file
with TypeScript:
<script lang="ts">
	import { MyComponent } from "component-library";
</script>
<MyComponent foo={'bar'} />Component<any>>(
	component: TComponent extends Component<any>component: function (type parameter) TComponent in withProps<TComponent extends Component<any>>(component: TComponent, props: ComponentProps<TComponent>): voidTComponent,
	props: ComponentProps<TComponent>props: type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const props: ComponentProps<typeof MyComponent> = { foo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { Component, ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

function withProps<TComponent extends Component<any>>(
	component: TComponent,
	props: ComponentProps<TComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
withProps(MyComponent, { foo: 'bar' });referenceComponentProps } from 'svelte';
import type MyComponent = SvelteComponent<Record<string, any>, any, any>
const MyComponent: LegacyComponentTypeMyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const const props: Record<string, any>props: type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const props: ComponentProps<typeof MyComponent> = { foo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { Component, ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

function withProps<TComponent extends Component<any>>(
	component: TComponent,
	props: ComponentProps<TComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
withProps(MyComponent, { foo: 'bar' });referenceComponentProps<typeof const MyComponent: LegacyComponentTypeMyComponent> = { foo: stringfoo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { Component, ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

function withProps<TComponent extends Component<any>>(
	component: TComponent,
	props: ComponentProps<TComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
withProps(MyComponent, { foo: 'bar' });ComponentProps<function (type parameter) TComponent in withProps<TComponent extends Component<any>>(component: TComponent, props: ComponentProps<TComponent>): voidTComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
function withProps<LegacyComponentType>(component: LegacyComponentType, props: Record<string, any>): voidwithProps(const MyComponent: LegacyComponentTypeMyComponent, { foo: stringfoo: 'bar' });ComponentProps } from 'svelte';
import type MyComponent = SvelteComponent<Record<string, any>, any, any>
const MyComponent: LegacyComponentTypeMyComponent from './MyComponent.svelte';

function function withProps<TComponent extends Component<any>>(component: TComponent, props: ComponentProps<TComponent>): voidwithProps<function (type parameter) TComponent in withProps<TComponent extends Component<any>>(component: TComponent, props: ComponentProps<TComponent>): voidTComponent extends interface Component<Props extends Record<string, any> = {}, Exports extends Record<string, any> = {}, Bindings extends keyof Props | "" = string>Can be used to create strongly typed Svelte components.
Example:You have component library on npm called component-library, from which
you export a component called MyComponent. For Svelte+TypeScript users,
you want to provide typings. Therefore you create a index.d.ts:
import type { Component } from 'svelte';
export declare const MyComponent: Component<{ foo: string }> {}Typing this makes it possible for IDEs like VS Code with the Svelte extension
to provide intellisense and to use the component like this in a Svelte file
with TypeScript:
<script lang="ts">
	import { MyComponent } from "component-library";
</script>
<MyComponent foo={'bar'} />Component<any>>(
	component: TComponent extends Component<any>component: function (type parameter) TComponent in withProps<TComponent extends Component<any>>(component: TComponent, props: ComponentProps<TComponent>): voidTComponent,
	props: ComponentProps<TComponent>props: type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const props: ComponentProps<typeof MyComponent> = { foo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { Component, ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

function withProps<TComponent extends Component<any>>(
	component: TComponent,
	props: ComponentProps<TComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
withProps(MyComponent, { foo: 'bar' });referenceComponentProps } from 'svelte';
import type MyComponent = SvelteComponent<Record<string, any>, any, any>
const MyComponent: LegacyComponentTypeMyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const const props: Record<string, any>props: type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const props: ComponentProps<typeof MyComponent> = { foo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { Component, ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

function withProps<TComponent extends Component<any>>(
	component: TComponent,
	props: ComponentProps<TComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
withProps(MyComponent, { foo: 'bar' });referenceComponentProps<typeof const MyComponent: LegacyComponentTypeMyComponent> = { foo: stringfoo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { interface Component<Props extends Record<string, any> = {}, Exports extends Record<string, any> = {}, Bindings extends keyof Props | "" = string>Can be used to create strongly typed Svelte components.
Example:You have component library on npm called component-library, from which
you export a component called MyComponent. For Svelte+TypeScript users,
you want to provide typings. Therefore you create a index.d.ts:
import type { Component } from 'svelte';
export declare const MyComponent: Component<{ foo: string }> {}Typing this makes it possible for IDEs like VS Code with the Svelte extension
to provide intellisense and to use the component like this in a Svelte file
with TypeScript:
<script lang="ts">
	import { MyComponent } from "component-library";
</script>
<MyComponent foo={'bar'} />Component, type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const props: ComponentProps<typeof MyComponent> = { foo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { Component, ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

function withProps<TComponent extends Component<any>>(
	component: TComponent,
	props: ComponentProps<TComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
withProps(MyComponent, { foo: 'bar' });ComponentProps } from 'svelte';
import type MyComponent = SvelteComponent<Record<string, any>, any, any>
const MyComponent: LegacyComponentTypeMyComponent from './MyComponent.svelte';

function function withProps<TComponent extends Component<any>>(component: TComponent, props: ComponentProps<TComponent>): voidwithProps<function (type parameter) TComponent in withProps<TComponent extends Component<any>>(component: TComponent, props: ComponentProps<TComponent>): voidTComponent extends interface Component<Props extends Record<string, any> = {}, Exports extends Record<string, any> = {}, Bindings extends keyof Props | "" = string>Can be used to create strongly typed Svelte components.
Example:You have component library on npm called component-library, from which
you export a component called MyComponent. For Svelte+TypeScript users,
you want to provide typings. Therefore you create a index.d.ts:
import type { Component } from 'svelte';
export declare const MyComponent: Component<{ foo: string }> {}Typing this makes it possible for IDEs like VS Code with the Svelte extension
to provide intellisense and to use the component like this in a Svelte file
with TypeScript:
<script lang="ts">
	import { MyComponent } from "component-library";
</script>
<MyComponent foo={'bar'} />Component<any>>(
	component: TComponent extends Component<any>component: function (type parameter) TComponent in withProps<TComponent extends Component<any>>(component: TComponent, props: ComponentProps<TComponent>): voidTComponent,
	props: ComponentProps<TComponent>props: type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const props: ComponentProps<typeof MyComponent> = { foo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { Component, ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

function withProps<TComponent extends Component<any>>(
	component: TComponent,
	props: ComponentProps<TComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
withProps(MyComponent, { foo: 'bar' });referenceComponentProps } from 'svelte';
import type MyComponent = SvelteComponent<Record<string, any>, any, any>
const MyComponent: LegacyComponentTypeMyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const const props: Record<string, any>props: type ComponentProps<Comp extends SvelteComponent | Component<any, any>> = Comp extends SvelteComponent<infer Props extends Record<string, any>, any, any> ? Props : Comp extends Component<infer Props extends Record<string, any>, any, string> ? Props : neverConvenience type to get the props the given component expects.
Example: Ensure a variable contains the props expected by MyComponent:
import type { ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

// Errors if these aren't the correct props expected by MyComponent.
const props: ComponentProps<typeof MyComponent> = { foo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { Component, ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

function withProps<TComponent extends Component<any>>(
	component: TComponent,
	props: ComponentProps<TComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
withProps(MyComponent, { foo: 'bar' });referenceComponentProps<typeof const MyComponent: LegacyComponentTypeMyComponent> = { foo: stringfoo: 'bar' }; In Svelte 4, you would do ComponentProps<MyComponent> because MyComponent was a class.
Example: A generic function that accepts some component and infers the type of its props:
import type { Component, ComponentProps } from 'svelte';
import MyComponent from './MyComponent.svelte';

function withProps<TComponent extends Component<any>>(
	component: TComponent,
	props: ComponentProps<TComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
withProps(MyComponent, { foo: 'bar' });ComponentProps<function (type parameter) TComponent in withProps<TComponent extends Component<any>>(component: TComponent, props: ComponentProps<TComponent>): voidTComponent>
) {};

// Errors if the second argument is not the correct props expected by the component in the first argument.
function withProps<LegacyComponentType>(component: LegacyComponentType, props: Record<string, any>): voidwithProps(const MyComponent: LegacyComponentTypeMyComponent, { foo: stringfoo: 'bar' });ComponentProps<function (type parameter) TComponent in withProps<TComponent extends Component<any>>(component: TComponent, props: ComponentProps<TComponent>): voidTComponent>
) {}

// Errors if the second argument is not the correct props expected
// by the component in the first argument.
function withProps<LegacyComponentType>(component: LegacyComponentType, props: Record<string, any>): voidwithProps(const MyComponent: LegacyComponentTypeMyComponent, { foo: stringfoo: 'bar' });
```

To declare that a variable expects the constructor or instance type of a component:

```
<script lang="ts">
	import MyComponent from './MyComponent.svelte';

	let componentConstructor: typeof MyComponent = MyComponent;
	let componentInstance: MyComponent;
</script>

<MyComponent bind:this={componentInstance} />
```

## Enhancing built-in DOM types[](#Enhancing-built-in-DOM-types)

Svelte provides a best effort of all the HTML DOM types that exist. Sometimes you may want to use experimental attributes or custom events coming from an action. In these cases, TypeScript will throw a type error, saying that it does not know these types. If it's a non-experimental standard attribute/event, this may very well be a missing typing from our [HTML typings](https://github.com/sveltejs/svelte/blob/main/packages/svelte/elements.d.ts). In that case, you are welcome to open an issue and/or a PR fixing it.

In case this is a custom or experimental attribute/event, you can enhance the typings by augmenting the `svelte/elements` module like this:

additional-svelte-typings.d

```
import { HTMLButtonAttributes } from 'svelte/elements';

declare module 'svelte/elements' {
	// add a new element
	export interface SvelteHTMLElements {
		'custom-button': HTMLButtonAttributes;
	}

	// add a new global attribute that is available on all html elements
	export interface interface HTMLAttributes<T extends EventTarget>HTMLAttributes<function (type parameter) T in HTMLAttributes<T extends EventTarget>T> {
		HTMLAttributes<T extends EventTarget>.globalattribute?: string | undefinedglobalattribute?: string;
	}

	// add a new attribute for button elements
	export interface HTMLButtonAttributes {
		HTMLButtonAttributes.veryexperimentalattribute?: string | undefinedveryexperimentalattribute?: string;
	}
}

export {}; // ensure this is not an ambient module, else types will be overridden instead of augmented
```

Then make sure that the `d.ts` file is referenced in your `tsconfig.json`. If it reads something like `"include": ["src/**/*"]` and your `d.ts` file is inside `src`, it should work. You may need to reload for the changes to take effect.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/07-misc/03-typescript.md) [llms.txt](/docs/svelte/typescript/llms.txt)

previous next

[Testing](/docs/svelte/testing) [Custom elements](/docs/svelte/custom-elements)


