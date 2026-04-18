---
title: "Basic Auth Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/basic-auth"
canonical_url: "https://hono.dev/docs/middleware/builtin/basic-auth"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:31.988Z"
content_hash: "8d06ff03597f6695a1c5dea95a04e8abaccc9ba4fda5fed06d8367daa6cb9954"
menu_path: ["Basic Auth Middleware ​"]
section_path: []
nav_prev: {"path": "hono/docs/helpers/websocket/index.md", "title": "WebSocket Helper \u200b"}
nav_next: {"path": "hono/docs/middleware/builtin/bearer-auth/index.md", "title": "Bearer Auth Middleware \u200b"}
---

## Basic Auth Middleware [​](#basic-auth-middleware)

This middleware can apply Basic authentication to a specified path. Implementing Basic authentication with Cloudflare Workers or other platforms is more complicated than it seems, but with this middleware, it's a breeze.

For more information about how the Basic auth scheme works under the hood, see the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#basic_authentication_scheme).

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { basicAuth } from 'hono/basic-auth'
```

## Usage [​](#usage)

ts

```
const app = new Hono()

app.use(
  '/auth/*',
  basicAuth({
    username: 'hono',
    password: 'acoolproject',
  })
)

app.get('/auth/page', (c) => {
  return c.text('You are authorized')
})
```

To restrict to a specific route + method:

ts

```
const app = new Hono()

app.get('/auth/page', (c) => {
  return c.text('Viewing page')
})

app.delete(
  '/auth/page',
  basicAuth({ username: 'hono', password: 'acoolproject' }),
  (c) => {
    return c.text('Page deleted')
  }
)
```

If you want to verify the user by yourself, specify the `verifyUser` option; returning `true` means it is accepted.

ts

```
const app = new Hono()

app.use(
  basicAuth({
    verifyUser: (username, password, c) => {
      return (
        username === 'dynamic-user' && password === 'hono-password'
      )
    },
  })
)
```

## Options [​](#options)

### required username: `string` [​](#username-string)

The username of the user who is authenticating.

### required password: `string` [​](#password-string)

The password value for the provided username to authenticate against.

### optional realm: `string` [​](#realm-string)

The domain name of the realm, as part of the returned WWW-Authenticate challenge header. The default is `"Secure Area"`.  
See more: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate#directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate#directives)

### optional hashFunction: `Function` [​](#hashfunction-function)

A function to handle hashing for safe comparison of passwords.

### optional verifyUser: `(username: string, password: string, c: Context) => boolean | Promise<boolean>` [​](#verifyuser-username-string-password-string-c-context-boolean-promise-boolean)

The function to verify the user.

### optional invalidUserMessage: `string | object | MessageFunction` [​](#invalidusermessage-string-object-messagefunction)

`MessageFunction` is `(c: Context) => string | object | Promise<string | object>`. The custom message if the user is invalid.

### optional onAuthSuccess: `(c: Context, username: string) => void | Promise<void>` [​](#onauthsuccess-c-context-username-string-void-promise-void)

A callback function invoked after successful authentication. This allows you to set context variables or perform side effects without re-parsing the Authorization header.

ts

```
app.use(
  '/auth/*',
  basicAuth({
    username: 'hono',
    password: 'acoolproject',
    onAuthSuccess: (c, username) => {
      c.set('username', username)
    },
  })
)

app.get('/auth/page', (c) => {
  const username = c.get('username')
  return c.text(`Hello, ${username}!`)
})
```

## More Options [​](#more-options)

### optional ...users: `{ username: string, password: string }[]` [​](#users-username-string-password-string)

## Recipes [​](#recipes)

### Defining Multiple Users [​](#defining-multiple-users)

This middleware also allows you to pass arbitrary parameters containing objects defining more `username` and `password` pairs.

ts

```
app.use(
  '/auth/*',
  basicAuth(
    {
      username: 'hono',
      password: 'acoolproject',
      // Define other params in the first object
      realm: 'www.example.com',
    },
    {
      username: 'hono-admin',
      password: 'super-secure',
      // Cannot redefine other params here
    },
    {
      username: 'hono-user-1',
      password: 'a-secret',
      // Or here
    }
  )
)
```

Or less hardcoded:

ts

```
import { users } from '../config/users'

app.use(
  '/auth/*',
  basicAuth(
    {
      realm: 'www.example.com',
      ...users[0],
    },
    ...users.slice(1)
  )
)
```

