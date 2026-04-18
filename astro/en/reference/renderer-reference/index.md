---
title: "Astro Renderer API"
source: "https://docs.astro.build/en/reference/renderer-reference/"
canonical_url: "https://docs.astro.build/en/reference/renderer-reference/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:58.950Z"
content_hash: "d53e43690339f51a303c0cbb9426d82c7af331509ebe56a6ad17abeac1888180"
menu_path: ["Astro Renderer API"]
section_path: []
---
# Astro Renderer API

Astro is designed to support any UI framework. This ability is powered by renderers, which are [integrations](/en/reference/integrations-reference/). See the [front-end frameworks guide](/en/guides/framework-components/) to learn how to use UI components from different frameworks in Astro.

## What is a renderer?

[Section titled “What is a renderer?”](#what-is-a-renderer)

A renderer is a special kind of [integration](/en/reference/integrations-reference/) that tells Astro how to detect and render component syntaxes it does not handle natively, such as [UI framework components](/en/guides/framework-components/). A renderer consists of two parts:

*   a server module imported during development and production builds to render components to HTML.
*   an optional client module imported in the browser to hydrate components with [client directives](/en/reference/directives-reference/#client-directives).

## Building a renderer

[Section titled “Building a renderer”](#building-a-renderer)

When you need to add support for a new component syntax in Astro, create an integration and call `addRenderer()` in the [`astro:config:setup`](/en/reference/integrations-reference/#astroconfigsetup) hook. This allows you to define the [server entrypoint](#building-a-server-entrypoint) that Astro should use for rendering components. Optionally, you can also define the [client entrypoint](#building-a-client-entrypoint) used for hydration.

The following example shows how to register a renderer in an Astro integration:

```
export default function createIntegration() {  return {    name: "@example/my-renderer",    hooks: {      "astro:config:setup": ({ addRenderer }) => {        addRenderer({          name: "@example/my-renderer",          clientEntrypoint: "@example/my-renderer/client.js",          serverEntrypoint: "@example/my-renderer/server.js",        });      },    },  };}
```

## Building a server entrypoint

[Section titled “Building a server entrypoint”](#building-a-server-entrypoint)

You will need to create a file that runs during server-side rendering and defines how to render the component syntax. The server module must default-export an object that implements the [`SSRLoadedRendererValue`](#ssrloadedrenderervalue) interface.

The following example shows a minimal server-side renderer implementing `check()` and `renderToStaticMarkup()`:

```
import type { AstroComponentMetadata, NamedSSRLoadedRendererValue } from 'astro';
async function check(Component: unknown) {  return typeof Component === 'function' && Component.name === 'MyCustomComponent';}
async function renderToStaticMarkup(  Component: any,  props: Record<string, unknown>,  slots: Record<string, string>,  metadata?: AstroComponentMetadata,) {  const rendered = Component(props);
  return {    attrs: metadata?.hydrate ? { 'data-my-renderer': 'true' } : undefined,    html: `<${rendered.tag}>${rendered.text}${slots.default ?? ''}</${rendered.tag}>`,  };}
const renderer: NamedSSRLoadedRendererValue = {  name: 'my-renderer',  check,  renderToStaticMarkup,};
export default renderer;
```

## Building a client entrypoint

[Section titled “Building a client entrypoint”](#building-a-client-entrypoint)

When your renderer supports [client directives](/en/reference/directives-reference/#client-directives), create a client entrypoint that defines how to hydrate components in the browser. The client module must default-export a function that receives the island element and returns an async hydrator function.

Astro dispatches a custom `astro:unmount` event on the island’s root element each time an island is removed from the page. You can listen for this event in your client entrypoint to clean up any mounted application state.

The following example shows a minimal client entrypoint that hydrates components in the browser:

```
export default (element: HTMLElement) =>  async (    Component: any,    props: Record<string, unknown>,    slots: Record<string, string>,    { client }: { client: string },  ) => {    const rendered = Component({ ...props, slots });
    if (client === 'only') {      element.innerHTML = '';    }
    const node = document.createElement(rendered.tag);    node.textContent = rendered.text;    element.appendChild(node);
    element.addEventListener('astro:unmount', () => node.remove(), { once: true });  };
```

## Renderer types reference

[Section titled “Renderer types reference”](#renderer-types-reference)

The following types can be imported from the `astro` module:

```
import type {  AstroComponentMetadata,  AstroRenderer,  NamedSSRLoadedRendererValue,  SSRLoadedRenderer,  SSRLoadedRendererValue,} from "astro";
```

### `AstroComponentMetadata`

[Section titled “AstroComponentMetadata”](#astrocomponentmetadata)

**Type:** `{ displayName: string; hydrate?: 'load' | 'idle' | 'visible' | 'media' | 'only'; hydrateArgs?: any; componentUrl?: string; componentExport?: { value: string; namespace?: boolean }; astroStaticSlot: true; }`

Contains information about the component being rendered, including its hydration directive.

#### `AstroComponentMetadata.displayName`

[Section titled “AstroComponentMetadata.displayName”](#astrocomponentmetadatadisplayname)

**Type:** `string`

Defines the component name, used for error messages and debugging.

#### `AstroComponentMetadata.hydrate`

[Section titled “AstroComponentMetadata.hydrate”](#astrocomponentmetadatahydrate)

**Type:** `'load' | 'idle' | 'visible' | 'media' | 'only'`

Defines the [client directive](/en/reference/directives-reference/#client-directives) used on the component. If no value is provided, the component will not be hydrated on the client.

Renderers can use this value to conditionally include client-side hydration state. For example, a renderer can skip serializing transfer state for components that will not be hydrated:

```
async function renderToStaticMarkup(Component, props, children, metadata) {  const willHydrate = !!metadata?.hydrate;  // Skip serializing hydration state if the component won't be hydrated  return render(Component, props, { includeTransferState: willHydrate });}
```

#### `AstroComponentMetadata.hydrateArgs`

[Section titled “AstroComponentMetadata.hydrateArgs”](#astrocomponentmetadatahydrateargs)

**Type:** `any`

Specifies the additional arguments passed to the hydration directive.

For example, this could be the media query string for `client:media` (i.e. `"(max-width: 768px)"`) or the renderer hint for `client:only` (i.e. `"react"`).

#### `AstroComponentMetadata.componentUrl`

[Section titled “AstroComponentMetadata.componentUrl”](#astrocomponentmetadatacomponenturl)

**Type:** `string`

Defines the URL of the component’s source file.

#### `AstroComponentMetadata.componentExport`

[Section titled “AstroComponentMetadata.componentExport”](#astrocomponentmetadatacomponentexport)

**Type:** `{ value: string; namespace?: boolean }`

Describes the component’s export Astro will load on the client for hydrated components.

##### `AstroComponentMetadata.componentExport.namespace`

[Section titled “AstroComponentMetadata.componentExport.namespace”](#astrocomponentmetadatacomponentexportnamespace)

**Type:** `boolean`

Indicates whether the export is a namespace export.

##### `AstroComponentMetadata.componentExport.value`

[Section titled “AstroComponentMetadata.componentExport.value”](#astrocomponentmetadatacomponentexportvalue)

**Type:** `string`

Defines the name of the export (e.g. `"default"` for default exports).

#### `AstroComponentMetadata.astroStaticSlot`

[Section titled “AstroComponentMetadata.astroStaticSlot”](#astrocomponentmetadataastrostaticslot)

**Type:** `true`

Indicates that Astro supports the static slot optimization for this component. Renderers that set [`supportsAstroStaticSlot`](#ssrloadedrenderervaluesupportsastrostaticslot) to `true` can use this in combination with [`hydrate`](#astrocomponentmetadatahydrate) to determine how to render slots.

### `AstroRenderer`

[Section titled “AstroRenderer”](#astrorenderer)

**Type:** `{ name: string; clientEntrypoint?: string | URL; serverEntrypoint: string | URL; }`

Describes a [component renderer added by an integration](/en/reference/integrations-reference/#addrenderer-option).

#### `AstroRenderer.name`

[Section titled “AstroRenderer.name”](#astrorenderername)

**Type:** `string`

Defines the unique renderer’s public name.

#### `AstroRenderer.clientEntrypoint`

[Section titled “AstroRenderer.clientEntrypoint”](#astrorenderercliententrypoint)

**Type:** `string | URL`

Defines the import path of the renderer that runs on the client whenever your component is used.

#### `AstroRenderer.serverEntrypoint`

[Section titled “AstroRenderer.serverEntrypoint”](#astrorendererserverentrypoint)

**Type:** `string | URL`

Defines the import path of the renderer that runs during server-side requests or static builds whenever your component is used.

### `NamedSSRLoadedRendererValue`

[Section titled “NamedSSRLoadedRendererValue”](#namedssrloadedrenderervalue)

Extends [`SSRLoadedRendererValue`](#ssrloadedrenderervalue) with a required `name` property.

### `SSRLoadedRenderer`

[Section titled “SSRLoadedRenderer”](#ssrloadedrenderer)

**Type:** `Pick<[AstroRenderer](#astrorenderer), ‘name’ | ‘clientEntrypoint’> & { ssr: [SSRLoadedRendererValue](#ssrloadedrenderervalue); }`

Describes a renderer available for the server to use. This is a subset of [`AstroRenderer`](#astrorenderer) with additional properties.

#### `SSRLoadedRenderer.ssr`

[Section titled “SSRLoadedRenderer.ssr”](#ssrloadedrendererssr)

**Type:** [`SSRLoadedRendererValue`](#ssrloadedrenderervalue)

Defines the functions and configuration used by the server for this framework.

### `SSRLoadedRendererValue`

[Section titled “SSRLoadedRendererValue”](#ssrloadedrenderervalue)

**Type:** `object`

Contains the functions and configuration necessary to render components on the server from a specific UI framework.

#### `SSRLoadedRendererValue.name`

[Section titled “SSRLoadedRendererValue.name”](#ssrloadedrenderervaluename)

**Type:** `string`

Specifies the name identifier for the renderer.

#### `SSRLoadedRendererValue.check()`

[Section titled “SSRLoadedRendererValue.check()”](#ssrloadedrenderervaluecheck)

**Type:** `(Component: any, props: any, slots: Record<string, string>, metadata?: [AstroComponentMetadata](#astrocomponentmetadata)) => Promise<boolean>`

Determines whether the renderer can handle a component. This function is called for each registered renderer until one returns `true`.

#### `SSRLoadedRendererValue.renderToStaticMarkup()`

[Section titled “SSRLoadedRendererValue.renderToStaticMarkup()”](#ssrloadedrenderervaluerendertostaticmarkup)

**Type:** `(Component: any, props: any, slots: Record<string, string>, metadata?: [AstroComponentMetadata](#astrocomponentmetadata)) => Promise<{ html: string; attrs?: Record<string, string>; }>`

Renders a framework component on the server and returns the resulting HTML string along with any optional attributes to be passed to the client entrypoint.

#### `SSRLoadedRendererValue.supportsAstroStaticSlot`

[Section titled “SSRLoadedRendererValue.supportsAstroStaticSlot”](#ssrloadedrenderervaluesupportsastrostaticslot)

**Type:** `boolean`  

**Added in:** `astro@2.5.0`

Indicates whether the renderer supports Astro’s static slot optimization. When true, Astro prevents the removal of nested slots within islands.

#### `SSRLoadedRendererValue.renderHydrationScript()`

[Section titled “SSRLoadedRendererValue.renderHydrationScript()”](#ssrloadedrenderervaluerenderhydrationscript)

**Type:** `() => string`  

**Added in:** `astro@4.1.0`

Returns an HTML string to inject once per page before the first hydrated component handled by this renderer. This is useful for renderers that need page-level hydration setup.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
