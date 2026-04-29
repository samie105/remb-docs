---
title: "html Helper ​"
source: "https://hono.dev/docs/helpers/html"
canonical_url: "https://hono.dev/docs/helpers/html"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:25.545Z"
content_hash: "571515fe3e00190cbda88948ec414f457047318efcdee79006f56ee2d8e6fcd7"
menu_path: ["html Helper ​"]
section_path: []
nav_prev: {"path": "../factory/index.md", "title": "Factory Helper \u200b"}
nav_next: {"path": "../jwt/index.md", "title": "JWT Authentication Helper \u200b"}
---

The html Helper lets you write HTML in JavaScript template literal with a tag named `html`. Using `raw()`, the content will be rendered as is. You have to escape these strings by yourself.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { html, raw } from 'hono/html'
```

## `html` [​](#html)

ts

```
const app = new Hono()

app.get('/:username', (c) => {
  const { username } = c.req.param()
  return c.html(
    html`<!doctype html>
      <h1>Hello! ${username}!</h1>`
  )
})
```

### Insert snippets into JSX [​](#insert-snippets-into-jsx)

Insert the inline script into JSX:

tsx

```
app.get('/', (c) => {
  return c.html(
    <html>
      <head>
        <title>Test Site</title>
        {html`
          <script>
            // No need to use dangerouslySetInnerHTML.
            // If you write it here, it will not be escaped.
          </script>
        `}
      </head>
      <body>Hello!</body>
    </html>
  )
})
```

### Act as functional component [​](#act-as-functional-component)

Since `html` returns an HtmlEscapedString, it can act as a fully functional component without using JSX.

#### Use `html` to speed up the process instead of `memo` [​](#use-html-to-speed-up-the-process-instead-of-memo)

typescript

```
const Footer = () => html`
  <footer>
    <address>My Address...</address>
  </footer>
`
```

### Receives props and embeds values [​](#receives-props-and-embeds-values)

typescript

```
interface SiteData {
  title: string
  description: string
  image: string
  children?: any
}
const Layout = (props: SiteData) => html`
<html>
<head>
  <meta charset="UTF-8">
  <title>${props.title}</title>
  <meta name="description" content="${props.description}">
  <head prefix="og: http://ogp.me/ns#">
  <meta property="og:type" content="article">
  <!-- More elements slow down JSX, but not template literals. -->
  <meta property="og:title" content="${props.title}">
  <meta property="og:image" content="${props.image}">
</head>
<body>
  ${props.children}
</body>
</html>
`

const Content = (props: { siteData: SiteData; name: string }) => (
  <Layout {...props.siteData}>
    <h1>Hello {props.name}</h1>
  </Layout>
)

app.get('/', (c) => {
  const props = {
    name: 'World',
    siteData: {
      title: 'Hello <> World',
      description: 'This is a description',
      image: 'https://example.com/image.png',
    },
  }
  return c.html(<Content {...props} />)
})
```

## `raw()` [​](#raw)

ts

```
app.get('/', (c) => {
  const name = 'John &quot;Johnny&quot; Smith'
  return c.html(html`<p>I'm ${raw(name)}.</p>`)
})
```

## Tips [​](#tips)

Thanks to these libraries, Visual Studio Code and vim also interprets template literals as HTML, allowing syntax highlighting and formatting to be applied.

*   [https://marketplace.visualstudio.com/items?itemName=bierner.lit-html](https://marketplace.visualstudio.com/items?itemName=bierner.lit-html)
*   [https://github.com/MaxMEllon/vim-jsx-pretty](https://github.com/MaxMEllon/vim-jsx-pretty)
