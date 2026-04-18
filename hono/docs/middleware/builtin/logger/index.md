---
title: "Logger Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/logger"
canonical_url: "https://hono.dev/docs/middleware/builtin/logger"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:14.649Z"
content_hash: "7f8a79f8a8478758775a84d113fd360aa72cdc4ff35632a3f108fedf650f2ad2"
menu_path: ["Logger Middleware ​"]
section_path: []
---
## Logger Middleware [​](#logger-middleware)

It's a simple logger.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { logger } from 'hono/logger'
```

## Usage [​](#usage)

ts

```
const app = new Hono()

app.use(logger())
app.get('/', (c) => c.text('Hello Hono!'))
```

## Logging Details [​](#logging-details)

The Logger Middleware logs the following details for each request:

*   **Incoming Request**: Logs the HTTP method, request path, and incoming request.
*   **Outgoing Response**: Logs the HTTP method, request path, response status code, and request/response times.
*   **Status Code Coloring**: Response status codes are color-coded for better visibility and quick identification of status categories. Different status code categories are represented by different colors.
*   **Elapsed Time**: The time taken for the request/response cycle is logged in a human-readable format, either in milliseconds (ms) or seconds (s).

By using the Logger Middleware, you can easily monitor the flow of requests and responses in your Hono application and quickly identify any issues or performance bottlenecks.

You can also extend the middleware further by providing your own `PrintFunc` function for tailored logging behavior.

TIP

To disable _status code coloring_, you can set a `NO_COLOR` environment variable. This is a common way to disable ANSI color escape codes in logging libraries, and is described at [https://no-color.org/](https://no-color.org/). Note that Cloudflare Workers do not have a `process.env` object, so will default to plaintext log output.

## PrintFunc [​](#printfunc)

The Logger Middleware accepts an optional `PrintFunc` function as a parameter. This function allows you to customize the logger and add additional logs.

## Options [​](#options)

### optional fn: `PrintFunc(str: string, ...rest: string[])` [​](#fn-printfunc-str-string-rest-string)

*   `str`: Passed by the logger.
*   `...rest`: Additional string props to be printed to console.

### Example [​](#example)

Setting up a custom `PrintFunc` function to the Logger Middleware:

ts

```
export const customLogger = (message: string, ...rest: string[]) => {
  console.log(message, ...rest)
}

app.use(logger(customLogger))
```

Setting up the custom logger in a route:

ts

```
app.post('/blog', (c) => {
  // Routing logic

  customLogger('Blog saved:', `Path: ${blog.url},`, `ID: ${blog.id}`)
  // Output
  // <-- POST /blog
  // Blog saved: Path: /blog/example, ID: 1
  // --> POST /blog 201 93ms

  // Return Context
})
```
