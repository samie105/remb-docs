---
title: "JSX Renderer Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/jsx-renderer"
canonical_url: "https://hono.dev/docs/middleware/builtin/jsx-renderer"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:33.204Z"
content_hash: "a71886415eef814bd00c8b8aef7a82c3e83dae50ca7b7aa80371ff114be9e67f"
menu_path: ["JSX Renderer Middleware ​"]
section_path: []
nav_prev: {"path": "../ip-restriction/index.md", "title": "IP Restriction Middleware \u200b"}
nav_next: {"path": "../jwk/index.md", "title": "JWK Auth Middleware \u200b"}
---

## JSX Renderer Middleware [​](#jsx-renderer-middleware)

JSX Renderer Middleware allows you to set up the layout when rendering JSX with the `c.render()` function, without the need for using `c.setRenderer()`. Additionally, it enables access to instances of Context within components through the use of `useRequestContext()`.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { jsxRenderer, useRequestContext } from 'hono/jsx-renderer'
```

## Usage [​](#usage)

jsx

```
const app = new Hono()

app.get(
  '/page/*',
  jsxRenderer(({ children }) => {
    return (
      <html>
        <body>
          <header>Menu</header>
          <div>{children}</div>
        </body>
      </html>
    )
  })
)

app.get('/page/about', (c) => {
  return c.render(<h1>About me!</h1>)
})
```

## Options [​](#options)

### optional docType: `boolean` | `string` [​](#doctype-boolean-string)

If you do not want to add a DOCTYPE at the beginning of the HTML, set the `docType` option to `false`.

tsx

```
app.use(
  '*',
  jsxRenderer(
    ({ children }) => {
      return (
        <html>
          <body>{children}</body>
        </html>
      )
    },
    { docType: false }
  )
)
```

And you can specify the DOCTYPE.

tsx

```
app.use(
  '*',
  jsxRenderer(
    ({ children }) => {
      return (
        <html>
          <body>{children}</body>
        </html>
      )
    },
    {
      docType:
        '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">',
    }
  )
)
```

### optional stream: `boolean` | `Record<string, string>` [​](#stream-boolean-record-string-string)

If you set it to `true` or provide a Record value, it will be rendered as a streaming response.

tsx

```
const AsyncComponent = async () => {
  await new Promise((r) => setTimeout(r, 1000)) // sleep 1s
  return <div>Hi!</div>
}

app.get(
  '*',
  jsxRenderer(
    ({ children }) => {
      return (
        <html>
          <body>
            <h1>SSR Streaming</h1>
            {children}
          </body>
        </html>
      )
    },
    { stream: true }
  )
)

app.get('/', (c) => {
  return c.render(
    <Suspense fallback={<div>loading...</div>}>
      <AsyncComponent />
    </Suspense>
  )
})
```

If `true` is set, the following headers are added:

ts

```
{
  'Transfer-Encoding': 'chunked',
  'Content-Type': 'text/html; charset=UTF-8',
  'Content-Encoding': 'Identity'
}
```

You can customize the header values by specifying the Record values.

### Function-based Options [​](#function-based-options)

You can pass a function that receives a `Context` object instead of a static options object. This allows you to dynamically set options based on the request context, such as environment variables or request parameters.

tsx

```
app.use(
  '*',
  jsxRenderer(
    ({ children }) => {
      return (
        <html>
          <body>{children}</body>
        </html>
      )
    },
    (c) => ({
      stream: c.req.header('X-Enable-Streaming') === 'true',
    })
  )
)
```

As a concrete example, you can use this to disable streaming when generating static sites (SSG) with `<Suspense>`, by using the [`isSSGContext`](../../../helpers/ssg/index.md#isssgcontext) helper:

tsx

```
app.use(
  '*',
  jsxRenderer(
    ({ children }) => {
      return (
        <div>
          <Suspense fallback={'loading...'}>
            <Component />
          </Suspense>
        </div>
      )
    },
    (c) => ({
      stream: !isSSGContext(c),
    })
  )
)
```

## Nested Layouts [​](#nested-layouts)

The `Layout` component enables nesting the layouts.

tsx

```
app.use(
  jsxRenderer(({ children }) => {
    return (
      <html>
        <body>{children}</body>
      </html>
    )
  })
)

const blog = new Hono()
blog.use(
  jsxRenderer(({ children, Layout }) => {
    return (
      <Layout>
        <nav>Blog Menu</nav>
        <div>{children}</div>
      </Layout>
    )
  })
)

app.route('/blog', blog)
```

## `useRequestContext()` [​](#userequestcontext)

`useRequestContext()` returns an instance of Context.

tsx

```
import { useRequestContext, jsxRenderer } from 'hono/jsx-renderer'

const app = new Hono()
app.use(jsxRenderer())

const RequestUrlBadge: FC = () => {
  const c = useRequestContext()
  return <b>{c.req.url}</b>
}

app.get('/page/info', (c) => {
  return c.render(
    <div>
      You are accessing: <RequestUrlBadge />
    </div>
  )
})
```

WARNING

You can't use `useRequestContext()` with the Deno's `precompile` JSX option. Use the `react-jsx`:

json

```
   "compilerOptions": {
     "jsx": "precompile", 
     "jsx": "react-jsx", 
     "jsxImportSource": "hono/jsx"
   }
 }
```

## Extending `ContextRenderer` [​](#extending-contextrenderer)

By defining `ContextRenderer` as shown below, you can pass additional content to the renderer. This is handy, for instance, when you want to change the contents of the head tag depending on the page.

tsx

```
declare module 'hono' {
  interface ContextRenderer {
    (
      content: string | Promise<string>,
      props: { title: string }
    ): Response
  }
}

const app = new Hono()

app.get(
  '/page/*',
  jsxRenderer(({ children, title }) => {
    return (
      <html>
        <head>
          <title>{title}</title>
        </head>
        <body>
          <header>Menu</header>
          <div>{children}</div>
        </body>
      </html>
    )
  })
)

app.get('/page/favorites', (c) => {
  return c.render(
    <div>
      <ul>
        <li>Eating sushi</li>
        <li>Watching baseball games</li>
      </ul>
    </div>,
    {
      title: 'My favorites',
    }
  )
})
```
