---
title: "Template directives reference"
source: "https://docs.astro.build/en/reference/directives-reference/"
canonical_url: "https://docs.astro.build/en/reference/directives-reference/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:11.406Z"
content_hash: "be8a2efc926930810f65d100af9eabb4d1edcca948ba749bf6f01c9174427ffa"
menu_path: ["Template directives reference"]
section_path: []
nav_prev: {"path": "astro/en/reference/astro-syntax/index.md", "title": "Template expressions reference"}
nav_next: {"path": "astro/en/reference/configuration-reference/index.md", "title": "Configuration Reference"}
---

# Template directives reference

**Template directives** are a special kind of HTML attribute available inside of any Astro component template (`.astro` files), and some can also be used in `.mdx` files.

Template directives are used to control an element or component’s behavior in some way. A template directive could enable some compiler feature that makes your life easier (like using `class:list` instead of `class`). Or, a directive could tell the Astro compiler to do something special with that component (like hydrating with `client:load`).

This page describes all of the template directives available to you in Astro, and how they work.

## Rules

[Section titled “Rules”](#rules)

For a template directive to be valid, it must:

*   Include a colon `:` in its name, using the form `X:Y` (ex: `client:load`).
*   Be visible to the compiler (ex: `<X {...attr}>` would not work if `attr` contained a directive).

Some template directives, but not all, can take a custom value:

*   `<X client:load />` (takes no value)
*   `<X class:list={['some-css-class']} />` (takes an array)

A template directive is never included directly in the final HTML output of a component.

## Common Directives

[Section titled “Common Directives”](#common-directives)

### `class:list`

[Section titled “class:list”](#classlist)

`class:list={...}` takes an array of class values and converts them into a class string. This is powered by @lukeed’s popular [clsx](https://github.com/lukeed/clsx) helper library.

`class:list` takes an array of several different possible value kinds:

*   `string`: Added to the element `class`
*   `Object`: All truthy keys are added to the element `class`
*   `Array`: flattened
*   `false`, `null`, or `undefined`: skipped

```
<!-- This --><span class:list={[ 'hello goodbye', { world: true }, [ 'friend' ] ]} /><!-- Becomes --><span class="hello goodbye world friend"></span>
```

### `set:html`

[Section titled “set:html”](#sethtml)

`set:html={string}` injects an HTML string into an element, similar to setting `el.innerHTML`.

**The value is not automatically escaped by Astro!** Be sure that you trust the value, or that you have escaped it manually before passing it to the template. Forgetting to do this will open you up to [Cross Site Scripting (XSS) attacks.](https://owasp.org/www-community/attacks/xss/)

```
---const rawHTMLString = "Hello <strong>World</strong>"---<h1>{rawHTMLString}</h1>  <!-- Output: <h1>Hello &lt;strong&gt;World&lt;/strong&gt;</h1> --><h1 set:html={rawHTMLString} />  <!-- Output: <h1>Hello <strong>World</strong></h1> -->
```

You can also use `set:html` on a `<Fragment>` to avoid adding an unnecessary wrapper element. This can be especially useful when fetching HTML from a CMS.

```
---const cmsContent = await fetchHTMLFromMyCMS();---<Fragment set:html={cmsContent}>
```

`set:html={Promise<string>}` injects an HTML string into an element that is wrapped in a Promise.

This can be used to inject HTML stored externally, such as in a database.

```
---import api from '../db/api.js';---<article set:html={api.getArticle(Astro.props.id)}></article>
```

`set:html={Promise<Response>}` injects a [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) into an element.

This is most helpful when using `fetch()`. For example, fetching old posts from a previous static-site generator.

```
<article set:html={fetch('http://example/old-posts/making-soup.html')}></article>
```

`set:html` can be used on any tag and does not have to include HTML. For example, use with [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) on a `<script>` tag to add a [JSON-LD](https://json-ld.org/) schema to your page.

```
<script type="application/ld+json" set:html={JSON.stringify({  "@context": "https://schema.org/",  "@type": "Person",  name: "Houston",  hasOccupation: {    "@type": "Occupation",    name: "Astronaut"  }})}/>
```

### `set:text`

[Section titled “set:text”](#settext)

`set:text={string}` injects a text string into an element, similar to setting `el.innerText`. Unlike `set:html`, the `string` value that is passed is automatically escaped by Astro.

This is equivalent to just passing a variable into a template expression directly (ex: `<div>{someText}</div>`) and therefore this directive is not commonly used.

## Client Directives

[Section titled “Client Directives”](#client-directives)

These directives control how [UI Framework components](../../guides/framework-components/index.md) are hydrated on the page.

By default, a UI Framework component is not hydrated in the client. If no `client:*` directive is provided, its HTML is rendered onto the page without JavaScript.

A client directive can only be used on a UI framework component that is directly imported into a `.astro` component. Hydration directives are not supported when using [dynamic tags](../astro-syntax/index.md#dynamic-tags) and [custom components passed via the `components` prop](../../guides/integrations-guide/mdx/index.md#passing-components-to-mdx-content).

### `client:load`

[Section titled “client:load”](#clientload)

*   **Priority:** High
*   **Useful for:** Immediately-visible UI elements that need to be interactive as soon as possible.

Load and hydrate the component JavaScript immediately on page load.

```
<BuyButton client:load />
```

### `client:idle`

[Section titled “client:idle”](#clientidle)

*   **Priority:** Medium
*   **Useful for:** Lower-priority UI elements that don’t need to be immediately interactive.

Load and hydrate the component JavaScript once the page is done with its initial load and the `requestIdleCallback` event has fired. If you are in a browser that doesn’t support [`requestIdleCallback`](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestIdleCallback), then the document [`load`](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event) event is used.

```
<ShowHideButton client:idle />
```

#### `timeout`

[Section titled “timeout”](#timeout)

**Added in:** `astro@4.15.0`

The maximum time to wait, in milliseconds, before hydrating the component, even if the page is not yet done with its initial load.

This allows you to pass a value for [the `timeout` option from the `requestIdleCallback()` specification](https://www.w3.org/TR/requestidlecallback/#the-requestidlecallback-method). This means you can delay hydration for lower-priority UI elements with more control to ensure your element is interactive within a specified time frame.

```
<ShowHideButton client:idle={{timeout: 500}} />
```

### `client:visible`

[Section titled “client:visible”](#clientvisible)

*   **Priority:** Low
*   **Useful for:** Low-priority UI elements that are either far down the page (“below the fold”) or so resource-intensive to load that you would prefer not to load them at all if the user never saw the element.

Load and hydrate the component JavaScript once the component has entered the user’s viewport. This uses an `IntersectionObserver` internally to keep track of visibility.

```
<HeavyImageCarousel client:visible />
```

#### `client:visible={{rootMargin}}`

[Section titled “client:visible={{rootMargin}}”](#clientvisiblerootmargin)

**Added in:** `astro@4.1.0`

Optionally, a value for `rootMargin` can be passed to the underlying `IntersectionObserver`. When `rootMargin` is specified, the component JavaScript will hydrate when a specified margin (in pixels) around the component enters the viewport, rather than the component itself.

```
<HeavyImageCarousel client:visible={{rootMargin: "200px"}} />
```

Specifying a `rootMargin` value can reduce layout shifts (CLS), allow more time for a component to hydrate on slower internet connections, and make components interactive sooner, enhancing the stability and responsiveness of the page.

### `client:media`

[Section titled “client:media”](#clientmedia)

*   **Priority:** Low
*   **Useful for:** Sidebar toggles, or other elements that might only be visible on certain screen sizes.

`client:media={string}` loads and hydrates the component JavaScript once a certain CSS media query is met.

```
<SidebarToggle client:media="(max-width: 50em)" />
```

### `client:only`

[Section titled “client:only”](#clientonly)

`client:only={string}` **skips** HTML server rendering, and renders only on the client. It acts similarly to `client:load` in that it loads, renders, and hydrates the component immediately on page load.

**You must pass the component’s correct framework as a value!** Because Astro doesn’t run the component during your build / on the server, Astro doesn’t know what framework your component uses unless you tell it explicitly.

```
<SomeReactComponent client:only="react" /><SomePreactComponent client:only="preact" /><SomeSvelteComponent client:only="svelte" /><SomeVueComponent client:only="vue" /><SomeSolidComponent client:only="solid-js" />
```

#### Display loading content

[Section titled “Display loading content”](#display-loading-content)

For components that render only on the client, it is also possible to display fallback content while they are loading. Use `slot="fallback"` on any child element to create content that will be displayed only until your client component is available:

```
<ClientComponent client:only="vue">  <div slot="fallback">Loading</div></ClientComponent>
```

### Custom Client Directives

[Section titled “Custom Client Directives”](#custom-client-directives)

Since Astro 2.6.0, integrations can also add custom `client:*` directives to change how and when components should be hydrated.

Visit the [`addClientDirective` API](../integrations-reference/index.md#addclientdirective-option) page to learn more about creating a custom client directive.

## Server Directives

[Section titled “Server Directives”](#server-directives)

These directives control how server island components are rendered.

### `server:defer`

[Section titled “server:defer”](#serverdefer)

The `server:defer` directive transforms the component into a server island, causing it to be rendered on demand, outside the scope of the rest of the page rendering.

See more about using [server island components](../../guides/server-islands/index.md).

```
<Avatar server:defer />
```

## Script & Style Directives

[Section titled “Script & Style Directives”](#script--style-directives)

These directives can only be used on HTML `<script>` and `<style>` tags, to control how your client-side JavaScript and CSS are handled on the page.

### `is:global`

[Section titled “is:global”](#isglobal)

By default, Astro automatically scopes `<style>` CSS rules to the component. You can opt-out of this behavior with the `is:global` directive.

`is:global` makes the contents of a `<style>` tag apply globally on the page when the component is included. This disables Astro’s CSS scoping system. This is equivalent to wrapping all of the selectors within a `<style>` tag with `:global()`.

You can combine `<style>` and `<style is:global>` together in the same component, to create some global style rules while still scoping most of your component CSS.

See the [Styling & CSS](../../guides/styling/index.md#global-styles) page for more details about how global styles work.

```
<style is:global>  body a { color: red; }</style>
```

### `is:inline`

[Section titled “is:inline”](#isinline)

By default, Astro will process, optimize, and bundle any `<script>` and `<style>` tags that it sees on the page. You can opt-out of this behavior with the `is:inline` directive.

`is:inline` tells Astro to leave the `<script>` or `<style>` tag as-is in the final output HTML. The contents will not be processed, optimized, or bundled. This limits some Astro features, like importing an npm package or using a compile-to-CSS language like Sass.

The `is:inline` directive means that `<style>` and `<script>` tags:

*   Will not be bundled into an external file. This means that [attributes like `defer`](https://javascript.info/script-async-defer) which control the loading of an external file will have no effect.
*   Will not be deduplicated—the element will appear as many times as it is rendered.
*   Will not have its `import`/`@import`/`url()` references resolved relative to the `.astro` file.
*   Will be rendered in the final output HTML exactly where it is authored.
*   Styles will be global and not scoped to the component.

```
<style is:inline>  /* inline: relative & npm package imports are not supported. */  @import '/assets/some-public-styles.css';  span { color: green; }</style>
<script is:inline>  /* inline: relative & npm package imports are not supported. */  console.log('I am inlined right here in the final output HTML.');</script>
```

See how [client-side scripts](../../guides/client-side-scripts/index.md) work in Astro components.

### `define:vars`

[Section titled “define:vars”](#definevars)

`define:vars={...}` can pass server-side variables from your component frontmatter into the client `<script>` or `<style>` tags. Any JSON-serializable frontmatter variable is supported, including `props` passed to your component through `Astro.props`. Values are serialized with [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).

```
---const foregroundColor = "rgb(221 243 228)";const backgroundColor = "rgb(24 121 78)";const message = "Astro is awesome!";---<style define:vars={{ textColor: foregroundColor, backgroundColor }}>  h1 {    background-color: var(--backgroundColor);    color: var(--textColor);  }</style>
<script define:vars={{ message }}>  alert(message);</script>
```

## Advanced Directives

[Section titled “Advanced Directives”](#advanced-directives)

### `is:raw`

[Section titled “is:raw”](#israw)

`is:raw` instructs the Astro compiler to treat any children of that element as text. This means that all special Astro templating syntax will be ignored inside of this component.

For example, if you had a custom Katex component that converted some text to HTML, you could have users do this:

```
---import Katex from '../components/Katex.astro';---<Katex is:raw>Some conflicting {syntax} here</Katex>
```

[Contribute](../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
