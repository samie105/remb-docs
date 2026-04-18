---
title: "Route Helper ​"
source: "https://hono.dev/docs/helpers/route"
canonical_url: "https://hono.dev/docs/helpers/route"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:07.976Z"
content_hash: "c220a1485f493c4a3d7b33fcb64fe839138c7f4f2d5b54629d14bf2b0705ffbd"
menu_path: ["Route Helper ​"]
section_path: []
---
The Route Helper provides enhanced routing information for debugging and middleware development. It allows you to access detailed information about matched routes and the current route being processed.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import {
  matchedRoutes,
  routePath,
  baseRoutePath,
  basePath,
} from 'hono/route'
```

## Usage [​](#usage)

### Basic route information [​](#basic-route-information)

ts

```
const app = new Hono()

app.get('/posts/:id', (c) => {
  const currentPath = routePath(c) // '/posts/:id'
  const routes = matchedRoutes(c) // Array of matched routes

  return c.json({
    path: currentPath,
    totalRoutes: routes.length,
  })
})
```

### Working with sub-applications [​](#working-with-sub-applications)

ts

```
const app = new Hono()
const apiApp = new Hono()

apiApp.get('/posts/:id', (c) => {
  return c.json({
    routePath: routePath(c), // '/posts/:id'
    baseRoutePath: baseRoutePath(c), // '/api'
    basePath: basePath(c), // '/api' (with actual params)
  })
})

app.route('/api', apiApp)
```

## `matchedRoutes()` [​](#matchedroutes)

Returns an array of all routes that matched the current request, including middleware.

ts

```
app.all('/api/*', (c, next) => {
  console.log('API middleware')
  return next()
})

app.get('/api/users/:id', (c) => {
  const routes = matchedRoutes(c)
  // Returns: [
  //   { method: 'ALL', path: '/api/*', handler: [Function] },
  //   { method: 'GET', path: '/api/users/:id', handler: [Function] }
  // ]
  return c.json({ routes: routes.length })
})
```

## `routePath()` [​](#routepath)

Returns the route path pattern registered for the current handler.

ts

```
app.get('/posts/:id', (c) => {
  console.log(routePath(c)) // '/posts/:id'
  return c.text('Post details')
})
```

### Using with index parameter [​](#using-with-index-parameter)

You can optionally pass an index parameter to get the route path at a specific position, similar to `Array.prototype.at()`.

ts

```
app.all('/api/*', (c, next) => {
  return next()
})

app.get('/api/users/:id', (c) => {
  console.log(routePath(c, 0)) // '/api/*' (first matched route)
  console.log(routePath(c, -1)) // '/api/users/:id' (last matched route)
  return c.text('User details')
})
```

## `baseRoutePath()` [​](#baseroutepath)

Returns the base path pattern of the current route as specified in routing.

ts

```
const subApp = new Hono()
subApp.get('/posts/:id', (c) => {
  return c.text(baseRoutePath(c)) // '/:sub'
})

app.route('/:sub', subApp)
```

### Using with index parameter [​](#using-with-index-parameter-1)

You can optionally pass an index parameter to get the base route path at a specific position, similar to `Array.prototype.at()`.

ts

```
app.all('/api/*', (c, next) => {
  return next()
})

const subApp = new Hono()
subApp.get('/users/:id', (c) => {
  console.log(baseRoutePath(c, 0)) // '/' (first matched route)
  console.log(baseRoutePath(c, -1)) // '/api' (last matched route)
  return c.text('User details')
})

app.route('/api', subApp)
```

## `basePath()` [​](#basepath)

Returns the base path with embedded parameters from the actual request.

ts

```
const subApp = new Hono()
subApp.get('/posts/:id', (c) => {
  return c.text(basePath(c)) // '/api' (for request to '/api/posts/123')
})

app.route('/:sub', subApp)
```
