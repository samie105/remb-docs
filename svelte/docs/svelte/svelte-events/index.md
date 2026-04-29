---
title: "svelte/events"
source: "https://svelte.dev/docs/svelte/svelte-events"
canonical_url: "https://svelte.dev/docs/svelte/svelte-events"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:16.773Z"
content_hash: "fefcaf36b80fedde03fe3ad37bfe80055a5ec009ef29290620620ac2ee14a559"
menu_path: ["svelte/events"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/svelte-easing/index.md", "title": "svelte/easing"}
nav_next: {"path": "svelte/docs/svelte/svelte-legacy/index.md", "title": "svelte/legacy"}
---

```
import { function on<Type extends keyof WindowEventMap>(window: Window, type: Type, handler: (this: Window, event: WindowEventMap[Type] & {
    currentTarget: Window;
}) => any, options?: AddEventListenerOptions | undefined): () => void (+4 overloads)Attaches an event handler to the window and returns a function that removes the handler. Using this
rather than addEventListener will preserve the correct order relative to handlers added declaratively
(with attributes like onclick), which use event delegation for performance reasons
referenceon } from 'svelte/events';
```

## on[](#on)

Attaches an event handler to the window and returns a function that removes the handler. Using this rather than `addEventListener` will preserve the correct order relative to handlers added declaratively (with attributes like `onclick`), which use event delegation for performance reasons

```
function on<Type extends keyof WindowEventMap>(
	window: Window,
	type: Type,
	handler: (
		this: Window,
		event: WindowEventMap[Type] & { currentTarget: Window }
	) => any,
	options?: AddEventListenerOptions | undefined
): () => void;
```

```
function on<Type extends keyof DocumentEventMap>(
	document: Document,
	type: Type,
	handler: (
		this: Document,
		event: DocumentEventMap[Type] & {
			currentTarget: Document;
		}
	) => any,
	options?: AddEventListenerOptions | undefined
): () => void;
```

```
function on<
	Element extends HTMLElement,
	Type extends keyof HTMLElementEventMap
>(
	element: Element,
	type: Type,
	handler: (
		this: Element,
		event: HTMLElementEventMap[Type] & {
			currentTarget: Element;
		}
	) => any,
	options?: AddEventListenerOptions | undefined
): () => void;
```

```
function on<
	Element extends MediaQueryList,
	Type extends keyof MediaQueryListEventMap
>(
	element: Element,
	type: Type,
	handler: (
		this: Element,
		event: MediaQueryListEventMap[Type] & {
			currentTarget: Element;
		}
	) => any,
	options?: AddEventListenerOptions | undefined
): () => void;
```

```
function on(
	element: EventTarget,
	type: string,
	handler: EventListener,
	options?: AddEventListenerOptions | undefined
): () => void;
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/98-reference/21-svelte-events.md) [llms.txt](/docs/svelte/svelte-events/llms.txt)

previous next

[svelte/easing](../svelte-easing/index.md) [svelte/legacy](../svelte-legacy/index.md)
