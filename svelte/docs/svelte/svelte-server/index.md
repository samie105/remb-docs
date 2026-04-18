---
title: "svelte/server"
source: "https://svelte.dev/docs/svelte/svelte-server"
canonical_url: "https://svelte.dev/docs/svelte/svelte-server"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:16.616Z"
content_hash: "44fe7c5b78519b6c133bc27cf6f79534c98fde9c5ccebfd54bb14990b7866aad"
menu_path: ["svelte/server"]
section_path: []
---
```
import { function render<Comp extends SvelteComponent<any> | Component<any>, Props extends ComponentProps<Comp> = ComponentProps<Comp>>(...args: {} extends Props ? [component: Comp extends SvelteComponent<any> ? ComponentType<Comp> : Comp, options?: {
    props?: Omit<Props, "$$slots" | "$$events">;
    context?: Map<any, any>;
    idPrefix?: string;
    csp?: Csp;
    transformError?: (error: unknown) => unknown | Promise<unknown>;
}] : [component: Comp extends SvelteComponent<any> ? ComponentType<Comp> : Comp, options: {
    props: Omit<Props, "$$slots" | "$$events">;
    context?: Map<any, any>;
    idPrefix?: string;
    csp?: Csp;
    transformError?: (error: unknown) => unknown | Promise<unknown>;
}]): RenderOutputOnly available on the server and when compiling with the server option.
Takes a component and returns an object with body and head properties on it, which you can use to populate the HTML when server-rendering your app.
referencerender } from 'svelte/server';
```

## render[](#render)

Only available on the server and when compiling with the `server` option. Takes a component and returns an object with `body` and `head` properties on it, which you can use to populate the HTML when server-rendering your app.

```
function render<
	Comp extends SvelteComponent<any> | Component<any>,
	Props extends ComponentProps<Comp> = ComponentProps<Comp>
>(
	...args: {} extends Props
		? [
				component: Comp extends SvelteComponent<any>
					? ComponentType<Comp>
					: Comp,
				options?: {
					props?: Omit<Props, '$$slots' | '$$events'>;
					context?: Map<any, any>;
					idPrefix?: string;
					csp?: Csp;
					transformError?: (
						error: unknown
					) => unknown | Promise<unknown>;
				}
			]
		: [
				component: Comp extends SvelteComponent<any>
					? ComponentType<Comp>
					: Comp,
				options: {
					props: Omit<Props, '$$slots' | '$$events'>;
					context?: Map<any, any>;
					idPrefix?: string;
					csp?: Csp;
					transformError?: (
						error: unknown
					) => unknown | Promise<unknown>;
				}
			]
): RenderOutput;
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/98-reference/21-svelte-server.md) [llms.txt](/docs/svelte/svelte-server/llms.txt)

previous next

[svelte/reactivity](/docs/svelte/svelte-reactivity) [svelte/store](/docs/svelte/svelte-store)
