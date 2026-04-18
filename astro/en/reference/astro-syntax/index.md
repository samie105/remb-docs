---
title: "Template expressions reference"
source: "https://docs.astro.build/en/reference/astro-syntax/"
canonical_url: "https://docs.astro.build/en/reference/astro-syntax/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:38.335Z"
content_hash: "142d6af8bd5a4028a9f5399d39fb5e0331e6793b1ca660ed6404bbece3586379"
menu_path: ["Template expressions reference"]
section_path: []
nav_prev: {"path": "astro/en/contribute/index.md", "title": "Contribute to Astro"}
nav_next: {"path": "astro/en/reference/directives-reference/index.md", "title": "Template directives reference"}
---

# Template expressions reference

Astro component syntax is a superset of HTML. The syntax was designed to feel familiar to anyone with experience writing HTML or JSX, and adds support for including components and JavaScript expressions.

## JSX-like Expressions

[Section titled “JSX-like Expressions”](#jsx-like-expressions)

You can define local JavaScript variables inside of the frontmatter component script between the two code fences (`---`) of an Astro component. You can then inject these variables into the component’s HTML template using JSX-like expressions!

### Variables

[Section titled “Variables”](#variables)

Local variables can be added into the HTML using the curly braces syntax:

```
---const name = "Astro";---<div>  <h1>Hello {name}!</h1>  <!-- Outputs <h1>Hello Astro!</h1> --></div>
```

### Dynamic Attributes

[Section titled “Dynamic Attributes”](#dynamic-attributes)

Local variables can be used in curly braces to pass attribute values to both HTML elements and components:

```
---const name = "Astro";---<h1 class={name}>Attribute expressions are supported</h1>
<MyComponent templateLiteralNameAttribute={`MyNameIs${name}`} />
```

### Dynamic HTML

[Section titled “Dynamic HTML”](#dynamic-html)

Local variables can be used in JSX-like functions to produce dynamically-generated HTML elements:

```
---const items = ["Dog", "Cat", "Platypus"];---<ul>  {items.map((item) => (    <li>{item}</li>  ))}</ul>
```

Astro can conditionally display HTML using JSX logical operators and ternary expressions.

```
---const visible = true;---{visible && <p>Show me!</p>}
{visible ? <p>Show me!</p> : <p>Else show me!</p>}
```

### Dynamic Tags

[Section titled “Dynamic Tags”](#dynamic-tags)

You can also use dynamic tags by assigning an HTML tag name to a variable or with a component import reassignment:

```
---import MyComponent from "./MyComponent.astro";const Element = 'div'const Component = MyComponent;---<Element>Hello!</Element> <!-- renders as <div>Hello!</div> --><Component /> <!-- renders as <MyComponent /> -->
```

When using dynamic tags:

*   **Variable names must be capitalized.** For example, use `Element`, not `element`. Otherwise, Astro will try to render your variable name as a literal HTML tag.
    
*   **Hydration directives are not supported.** When using [`client:*` hydration directives](/en/guides/framework-components/#hydrating-interactive-components), Astro needs to know which components to bundle for production, and the dynamic tag pattern prevents this from working.
    
*   **The [define:vars directive](/en/reference/directives-reference/#definevars) is not supported.** If you cannot wrap the children with an extra element (e.g `<div>`), then you can manually add a ``style={`--myVar:${value}`}`` to your Element.
    

### Fragments

[Section titled “Fragments”](#fragments)

Astro supports `<> </>` notation and also provides a built-in `<Fragment />` component. This component can be useful to avoid wrapper elements when adding [`set:*` directives](/en/reference/directives-reference/#sethtml) to inject an HTML string.

The following example renders paragraph text using the `<Fragment />` component:

```
---const htmlString = '<p>Raw HTML content</p>';---<Fragment set:html={htmlString} />
```

### Differences between Astro and JSX

[Section titled “Differences between Astro and JSX”](#differences-between-astro-and-jsx)

Astro component syntax is a superset of HTML. It was designed to feel familiar to anyone with HTML or JSX experience, but there are a couple of key differences between `.astro` files and JSX.

#### Attributes

[Section titled “Attributes”](#attributes)

In Astro, you use the standard `kebab-case` format for all HTML attributes instead of the `camelCase` used in JSX. This even works for `class`, which is not supported by React.

```
<div className="box" dataValue="3" /><div class="box" data-value="3" />
```

#### Multiple Elements

[Section titled “Multiple Elements”](#multiple-elements)

An Astro component template can render multiple elements with no need to wrap everything in a single `<div>` or `<>`, unlike JavaScript or JSX.

```
---// Template with multiple elements---<p>No need to wrap elements in a single containing element.</p><p>Astro supports multiple root elements in a template.</p>
```

#### Comments

[Section titled “Comments”](#comments)

In Astro, you can use standard HTML comments or JavaScript-style comments.

```
------<!-- HTML comment syntax is valid in .astro files -->{/* JS comment syntax is also valid */}
```

## Component utilities

[Section titled “Component utilities”](#component-utilities)

### `Astro.slots`

[Section titled “Astro.slots”](#astroslots)

`Astro.slots` contains utility functions for modifying an Astro component’s slotted children.

#### `Astro.slots.has()`

[Section titled “Astro.slots.has()”](#astroslotshas)

**Type:** `(slotName: string) => boolean`

You can check whether content for a specific slot name exists with `Astro.slots.has()`. This can be useful when you want to wrap slot contents but only want to render the wrapper elements when the slot is being used.

```
------<slot />
{Astro.slots.has('more') && (  <aside>    <h2>More</h2>    <slot name="more" />  </aside>)}
```

#### `Astro.slots.render()`

[Section titled “Astro.slots.render()”](#astroslotsrender)

**Type:** `(slotName: string, args?: any[]) => Promise<string>`

You can asynchronously render the contents of a slot to a string of HTML using `Astro.slots.render()`.

```
---const html = await Astro.slots.render('default');---<Fragment set:html={html} />
```

`Astro.slots.render()` optionally accepts a second argument: an array of parameters that will be forwarded to any function children. This can be useful for custom utility components.

For example, this `<Shout />` component converts its `message` prop to uppercase and passes it to the default slot:

```
---const message = Astro.props.message.toUpperCase();let html = '';if (Astro.slots.has('default')) {  html = await Astro.slots.render('default', [message]);}---<Fragment set:html={html} />
```

A callback function passed as `<Shout />`’s child will receive the all-caps `message` parameter:

```
---import Shout from "../components/Shout.astro";---<Shout message="slots!">  {(message) => <div>{message}</div>}</Shout>
<!-- renders as <div>SLOTS!</div> -->
```

Callback functions can be passed to named slots inside a wrapping HTML element tag with a `slot` attribute. This element is only used to transfer the callback to a named slot and will not be rendered onto the page.

```
<Shout message="slots!">  <fragment slot="message">    {(message) => <div>{message}</div>}  </fragment></Shout>
```

Use a standard HTML element for the wrapping tag or any lowercase tag (e.g. `<fragment>` instead of `<Fragment />`) that will not be interpreted as a component. Do not use the HTML `<slot>` element as this will be interpreted as an Astro slot.

### `Astro.self`

[Section titled “Astro.self”](#astroself)

`Astro.self` allows Astro components to be recursively called. This behavior lets you render an Astro component from within itself by using `<Astro.self>` in the component template. This can help iterate over large data stores and nested data structures.

```
---const { items } = Astro.props;---<ul class="nested-list">  {items.map((item) => (    <li>      <!-- If there is a nested data-structure we render `<Astro.self>` -->      <!-- and can pass props through with the recursive call -->      {Array.isArray(item) ? (        <Astro.self items={item} />      ) : (        item      )}    </li>  ))}</ul>
```

This component could then be used like this:

```
---import NestedList from './NestedList.astro';---<NestedList items={['A', ['B', 'C'], 'D']} />
```

And would render HTML like this:

```
<ul class="nested-list">  <li>A</li>  <li>    <ul class="nested-list">      <li>B</li>      <li>C</li>    </ul>  </li>  <li>D</li></ul>
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

