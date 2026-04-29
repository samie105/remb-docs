---
title: "Imperative component API"
source: "https://svelte.dev/docs/svelte/imperative-component-api"
canonical_url: "https://svelte.dev/docs/svelte/imperative-component-api"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:00.428Z"
content_hash: "51a014aa9fc0489e4fa01441f7d65678d4e067751edbd1667ccdac4fbc81e30a"
menu_path: ["Imperative component API"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/lifecycle-hooks/index.md", "title": "Lifecycle hooks"}
nav_next: {"path": "svelte/docs/svelte/hydratable/index.md", "title": "Hydratable data"}
---

Every Svelte application starts by imperatively creating a root component. On the client this component is mounted to a specific element. On the server, you want to get back a string of HTML instead which you can render. The following functions help you achieve those tasks.

## mount[](#mount)

Instantiates a component and mounts it to the given target:

```
import { function mount<Props extends Record<string, any>, Exports extends Record<string, any>>(component: ComponentType<SvelteComponent<Props>> | Component<Props, Exports, any>, options: MountOptions<Props>): ExportsMounts a component to the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component.
Transitions will play during the initial render unless the intro option is set to false.
referencemount } from 'svelte';
import type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentTypeApp from './App.svelte';

const const app: {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>app = mount<Record<string, any>, {
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
referencemount(const App: LegacyComponentTypeApp, {
	target: Document | Element | ShadowRootTarget element where the component will be mounted.
target: var document: Documentwindow.document returns a reference to the document contained in the window.
MDN Reference
document.ParentNode.querySelector<Element>(selectors: string): Element | null (+4 overloads)Returns the first element that is a descendant of node that matches selectors.
MDN Reference
querySelector('#app'),
	props?: Record<string, any> | undefinedComponent properties.
props: { some: stringsome: 'property' }
});
```

You can mount multiple components per page, and you can also mount from within your application, for example when creating a tooltip component and attaching it to the hovered element.

Note that unlike calling `new App(...)` in Svelte 4, things like effects (including `onMount` callbacks, and action functions) will not run during `mount`. If you need to force pending effects to run (in the context of a test, for example) you can do so with `flushSync()`.

## unmount[](#unmount)

Unmounts a component that was previously created with [`mount`](#mount) or [`hydrate`](#hydrate).

If `options.outro` is `true`, [transitions](transition) will play before the component is removed from the DOM:

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
import type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentTypeApp from './App.svelte';

const const app: {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>app = mount<Record<string, any>, {
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
referencemount(const App: LegacyComponentTypeApp, { target: Document | Element | ShadowRootTarget element where the component will be mounted.
target: var document: Documentwindow.document returns a reference to the document contained in the window.
MDN Reference
document.Document.body: HTMLElementThe Document.body property represents the null if no such element exists.
MDN Reference
body });

// later
function unmount(component: Record<string, any>, options?: {
    outro?: boolean;
} | undefined): Promise<void>Unmounts a component that was previously mounted using mount or hydrate.
Since 5.13.0, if options.outro is true, transitions will play before the component is removed from the DOM.
Returns a Promise that resolves after transitions have completed if options.outro is true, or immediately otherwise (prior to 5.13.0, returns void).
import { mount, unmount } from 'svelte';
import App from './App.svelte';

const app = mount(App, { target: document.body });

// later...
unmount(app, { outro: true });referenceunmount(const app: {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>app, { outro?: boolean | undefinedoutro: true });
```

Returns a `Promise` that resolves after transitions have completed if `options.outro` is true, or immediately otherwise.

## render[](#render)

Only available on the server and when compiling with the `server` option. Takes a component and returns an object with `body` and `head` properties on it, which you can use to populate the HTML when server-rendering your app:

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
import type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentTypeApp from './App.svelte';

const const result: RenderOutputresult = render<SvelteComponent<Record<string, any>, any, any>, Record<string, any>>(component: ComponentType<SvelteComponent<Record<string, any>, any, any>>, options?: {
    props?: Omit<Record<string, any>, "$$slots" | "$$events"> | undefined;
    context?: Map<any, any>;
    idPrefix?: string;
    csp?: Csp;
    transformError?: ((error: unknown) => unknown | Promise<unknown>) | undefined;
} | undefined): RenderOutputOnly available on the server and when compiling with the server option.
Takes a component and returns an object with body and head properties on it, which you can use to populate the HTML when server-rendering your app.
referencerender(const App: LegacyComponentTypeApp, {
	props?: Omit<Record<string, any>, "$$slots" | "$$events"> | undefinedprops: { some: stringsome: 'property' }
});
const result: RenderOutputresult.SyncRenderOutput.body: stringHTML that goes somewhere into the <body>
body; // HTML for somewhere in this <body> tag
const result: RenderOutputresult.SyncRenderOutput.head: stringHTML that goes into the <head>
head; // HTML for somewhere in this <head> tag
```

## hydrate[](#hydrate)

Like `mount`, but will reuse up any HTML rendered by Svelte's SSR output (from the [`render`](#render) function) inside the target and make it interactive:

```
import { function hydrate<Props extends Record<string, any>, Exports extends Record<string, any>>(component: ComponentType<SvelteComponent<Props>> | Component<Props, Exports, any>, options: {} extends Props ? {
    target: Document | Element | ShadowRoot;
    props?: Props;
    events?: Record<string, (e: any) => any>;
    context?: Map<any, any>;
    intro?: boolean;
    recover?: boolean;
    transformError?: (error: unknown) => unknown;
} : {
    target: Document | Element | ShadowRoot;
    props: Props;
    events?: Record<string, (e: any) => any>;
    context?: Map<any, any>;
    intro?: boolean;
    recover?: boolean;
    transformError?: (error: unknown) => unknown;
}): ExportsHydrates a component on the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component
referencehydrate } from 'svelte';
import type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentTypeApp from './App.svelte';

const const app: {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>app = hydrate<Record<string, any>, {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>>(component: ComponentType<SvelteComponent<Record<string, any>, any, any>> | Component<Record<string, any>, {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>, any>, options: {
    ...;
}): {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<...>Hydrates a component on the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component
referencehydrate(const App: LegacyComponentTypeApp, {
	target: Document | Element | ShadowRoottarget: var document: Documentwindow.document returns a reference to the document contained in the window.
MDN Reference
document.ParentNode.querySelector<Element>(selectors: string): Element | null (+4 overloads)Returns the first element that is a descendant of node that matches selectors.
MDN Reference
querySelector('#app'),
	props?: Record<string, any> | undefinedprops: { some: stringsome: 'property' }
});
```

As with `mount`, effects will not run during `hydrate` — use `flushSync()` immediately afterwards if you need them to.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/06-runtime/04-imperative-component-api.md) [llms.txt](/docs/svelte/imperative-component-api/llms.txt)

previous next

[Lifecycle hooks](../lifecycle-hooks/index.md) [Hydratable data](../hydratable/index.md)
