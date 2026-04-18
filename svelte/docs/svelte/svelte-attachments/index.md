---
title: "svelte/attachments"
source: "https://svelte.dev/docs/svelte/svelte-attachments"
canonical_url: "https://svelte.dev/docs/svelte/svelte-attachments"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:42.539Z"
content_hash: "49184ede84589a9664e121b79369e0cc5d70033c7088e6e74fee8cec22153fb7"
menu_path: ["svelte/attachments"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/svelte-animate/index.md", "title": "svelte/animate"}
nav_next: {"path": "svelte/docs/svelte/svelte-compiler/index.md", "title": "svelte/compiler"}
---

```
import { function createAttachmentKey(): symbolCreates an object key that will be recognised as an attachment when the object is spread onto an element,
as a programmatic alternative to using {@attach ...}. This can be useful for library authors, though
is generally not needed when building an app.
<script>
	import { createAttachmentKey } from 'svelte/attachments';

	const props = {
		class: 'cool',
		onclick: () => alert('clicked'),
		[createAttachmentKey()]: (node) => {
			node.textContent = 'attached!';
		}
	};
</script>

<button {...props}>click me</button>@since5.29referencecreateAttachmentKey, function fromAction<E extends EventTarget, T extends unknown>(action: Action<E, T, Record<never, any>> | ((element: E, arg: T) => void | ActionReturn<T, Record<never, any>>), fn: () => T): Attachment<E> (+1 overload)Converts an action into an attachment keeping the same behavior.
It's useful if you want to start using attachments on components but you have actions provided by a library.
Note that the second argument, if provided, must be a function that returns the argument to the
action function, not the argument itself.
<!-- with an action -->
<div use:foo={bar}>...</div>

<!-- with an attachment -->
<div {@attach fromAction(foo, () => bar)}>...</div>referencefromAction } from 'svelte/attachments';
```

## createAttachmentKey[](#createAttachmentKey)

> Available since 5.29

Creates an object key that will be recognised as an attachment when the object is spread onto an element, as a programmatic alternative to using `{@attach ...}`. This can be useful for library authors, though is generally not needed when building an app.

```
<script>
	import { createAttachmentKey } from 'svelte/attachments';

	const props = {
		class: 'cool',
		onclick: () => alert('clicked'),
		[createAttachmentKey()]: (node) => {
			node.textContent = 'attached!';
		}
	};
</script>

<button {...props}>click me</button>
```

```
function createAttachmentKey(): symbol;
```

## fromAction[](#fromAction)

Converts an [action](/docs/svelte/use) into an [attachment](/docs/svelte/@attach) keeping the same behavior. It's useful if you want to start using attachments on components but you have actions provided by a library.

Note that the second argument, if provided, must be a function that _returns_ the argument to the action function, not the argument itself.

```
<!-- with an action -->
<div use:foo={bar}>...</div>

<!-- with an attachment -->
<div {@attach fromAction(foo, () => bar)}>...</div>
```

```
function fromAction<
	E extends EventTarget,
	T extends unknown
>(
	action:
		| Action<E, T>
		| ((element: E, arg: T) => void | ActionReturn<T>),
	fn: () => T
): Attachment<E>;
```

```
function fromAction<E extends EventTarget>(
	action:
		| Action<E, void>
		| ((element: E) => void | ActionReturn<void>)
): Attachment<E>;
```

## Attachment[](#Attachment)

An [attachment](/docs/svelte/@attach) is a function that runs when an element is mounted to the DOM, and optionally returns a function that is called when the element is later removed.

It can be attached to an element with an `{@attach ...}` tag, or by spreading an object containing a property created with [`createAttachmentKey`](/docs/svelte/svelte-attachments#createAttachmentKey).

```
interface Attachment<T extends EventTarget = Element> {…}
```

```
(element: T): void | (() => void);
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/98-reference/21-svelte-attachments.md) [llms.txt](/docs/svelte/svelte-attachments/llms.txt)

previous next

[svelte/animate](/docs/svelte/svelte-animate) [svelte/compiler](/docs/svelte/svelte-compiler)


