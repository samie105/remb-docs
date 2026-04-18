---
title: "svelte/action"
source: "https://svelte.dev/docs/svelte/svelte-action"
canonical_url: "https://svelte.dev/docs/svelte/svelte-action"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:20.855Z"
content_hash: "7594c45a6a5387f13738f55c6acb5b68a42a13b59b11a28baf3ad2e10583601b"
menu_path: ["svelte/action"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/svelte/index.md", "title": "svelte"}
nav_next: {"path": "svelte/docs/svelte/svelte-animate/index.md", "title": "svelte/animate"}
---

This module provides types for [actions](use), which have been superseded by [attachments](@attach).

## Action[](#Action)

Actions are functions that are called when an element is created. You can use this interface to type such actions. The following example defines an action that only works on `<div>` elements and optionally accepts a parameter which it has a default value for:

```
export const const myAction: Action<HTMLDivElement, {
    someProperty: boolean;
} | undefined>myAction: type Action = /*unresolved*/ anyAction<HTMLDivElement, { someProperty: booleansomeProperty: boolean } | undefined> = (node: anynode, param: {
    someProperty: boolean;
}param = { someProperty: booleansomeProperty: true }) => {
	// ...
}
```

`Action<HTMLDivElement>` and `Action<HTMLDivElement, undefined>` both signal that the action accepts no parameters.

You can return an object with methods `update` and `destroy` from the function and type which additional attributes and events it has. See interface `ActionReturn` for more details.

```
interface Action<
	Element = HTMLElement,
	Parameter = undefined,
	Attributes extends Record<string, any> = Record<
		never,
		any
	>
> {…}
```

```
<Node extends Element>(
	...args: undefined extends Parameter
		? [node: Node, parameter?: Parameter]
		: [node: Node, parameter: Parameter]
): void | ActionReturn<Parameter, Attributes>;
```

## ActionReturn[](#ActionReturn)

Actions can return an object containing the two properties defined in this interface. Both are optional.

*   update: An action can have a parameter. This method will be called whenever that parameter changes, immediately after Svelte has applied updates to the markup. `ActionReturn` and `ActionReturn<undefined>` both mean that the action accepts no parameters.
*   destroy: Method that is called after the element is unmounted

Additionally, you can specify which additional attributes and events the action enables on the applied element. This applies to TypeScript typings only and has no effect at runtime.

Example usage:

```
interface Attributes {
	Attributes.newprop?: string | undefinednewprop?: string;
	'on:event': (e: CustomEvent<boolean>e: interface CustomEvent<T = any>The CustomEvent interface represents events initialized by an application for any purpose.
MDN Reference
CustomEvent<boolean>) => void;
}

export function function myAction(node: HTMLElement, parameter: Parameter): ActionReturn<Parameter, Attributes>myAction(node: HTMLElementnode: HTMLElement, parameter: Parameterparameter: type Parameter = /*unresolved*/ anyParameter): type ActionReturn = /*unresolved*/ anyActionReturn<type Parameter = /*unresolved*/ anyParameter, Attributes> {
	// ...
	return {
		update: (updatedParameter: any) => voidupdate: (updatedParameter: anyupdatedParameter) => {...},
		destroy: () => {...}
	};
}
```

```
interface ActionReturn<
	Parameter = undefined,
	Attributes extends Record<string, any> = Record<
		never,
		any
	>
> {…}
```

```
update?: (parameter: Parameter) => void;
```

```
destroy?: () => void;
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/98-reference/21-svelte-action.md) [llms.txt](/docs/svelte/svelte-action/llms.txt)

previous next

[svelte](/docs/svelte/svelte) [svelte/animate](/docs/svelte/svelte-animate)

