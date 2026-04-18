---
title: "Bearer Auth Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/bearer-auth"
canonical_url: "https://hono.dev/docs/middleware/builtin/bearer-auth"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:33.878Z"
content_hash: "3e6405b13f40a17a1348028be2d311c19fcaa110926be1ec7baf6c5c5f06b869"
menu_path: ["Bearer Auth Middleware ​"]
section_path: []
nav_prev: {"path": "hono/docs/middleware/builtin/basic-auth/index.md", "title": "Basic Auth Middleware \u200b"}
nav_next: {"path": "hono/docs/middleware/builtin/body-limit/index.md", "title": "Body Limit Middleware \u200b"}
---

## Bearer Auth Middleware [​](#bearer-auth-middleware)

The Bearer Auth Middleware provides authentication by verifying an API token in the Request header. The HTTP clients accessing the endpoint will add the `Authorization` header with `Bearer {token}` as the header value.

Using `curl` from the terminal, it would look like this:

sh

```
curl -H 'Authorization: Bearer honoiscool' http://localhost:8787/auth/page
```

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { bearerAuth } from 'hono/bearer-auth'
```

## Usage [​](#usage)

NOTE

Your `token` must match the regex `/[A-Za-z0-9._~+/-]+=*/`, otherwise a 400 error will be returned. Notably, this regex accommodates both URL-safe Base64- and standard Base64-encoded JWTs. This middleware does not require the bearer token to be a JWT, just that it matches the above regex.

ts

```
const app = new Hono()

const token = 'honoiscool'

app.use('/api/*', bearerAuth({ token }))

app.get('/api/page', (c) => {
  return c.json({ message: 'You are authorized' })
})
```

To restrict to a specific route + method:

ts

```
const app = new Hono()

const token = 'honoiscool'

app.get('/api/page', (c) => {
  return c.json({ message: 'Read posts' })
})

app.post('/api/page', bearerAuth({ token }), (c) => {
  return c.json({ message: 'Created post!' }, 201)
})
```

To implement multiple tokens (E.g., any valid token can read but create/update/delete are restricted to a privileged token):

ts

```
const app = new Hono()

const readToken = 'read'
const privilegedToken = 'read+write'
const privilegedMethods = ['POST', 'PUT', 'PATCH', 'DELETE']

app.on('GET', '/api/page/*', async (c, next) => {
  // List of valid tokens
  const bearer = bearerAuth({ token: [readToken, privilegedToken] })
  return bearer(c, next)
})
app.on(privilegedMethods, '/api/page/*', async (c, next) => {
  // Single valid privileged token
  const bearer = bearerAuth({ token: privilegedToken })
  return bearer(c, next)
})

// Define handlers for GET, POST, etc.
```

If you want to verify the value of the token yourself, specify the `verifyToken` option; returning `true` means it is accepted.

ts

```
const app = new Hono()

app.use(
  '/auth-verify-token/*',
  bearerAuth({
    verifyToken: async (token, c) => {
      return token === 'dynamic-token'
    },
  })
)
```

## Options [​](#options)

### required token: `string` | `string[]` [​](#token-string-string)

The string to validate the incoming bearer token against.

### optional realm: `string` [​](#realm-string)

The domain name of the realm, as part of the returned WWW-Authenticate challenge header. The default is `""`. See more: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate#directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate#directives)

### optional prefix: `string` [​](#prefix-string)

The prefix (or known as `schema`) for the Authorization header value. The default is `"Bearer"`.

### optional headerName: `string` [​](#headername-string)

The header name. The default value is `Authorization`.

### optional hashFunction: `Function` [​](#hashfunction-function)

A function to handle hashing for safe comparison of authentication tokens.

### optional verifyToken: `(token: string, c: Context) => boolean | Promise<boolean>` [​](#verifytoken-token-string-c-context-boolean-promise-boolean)

The function to verify the token.

### optional noAuthenticationHeader: `object` [​](#noauthenticationheader-object)

Customizes the error response when the request does not have an authentication header.

*   `wwwAuthenticateHeader`: `string | object | MessageFunction` - Customizes the WWW-Authenticate header value.
*   `message`: `string | object | MessageFunction` - The custom message for the response body.

`MessageFunction` is `(c: Context) => string | object | Promise<string | object>`.

### optional invalidAuthenticationHeader: `object` [​](#invalidauthenticationheader-object)

Customizes the error response when the authentication header format is invalid.

*   `wwwAuthenticateHeader`: `string | object | MessageFunction` - Customizes the WWW-Authenticate header value.
*   `message`: `string | object | MessageFunction` - The custom message for the response body.

### optional invalidToken: `object` [​](#invalidtoken-object)

Customizes the error response when the token is invalid.

*   `wwwAuthenticateHeader`: `string | object | MessageFunction` - Customizes the WWW-Authenticate header value.
*   `message`: `string | object | MessageFunction` - The custom message for the response body.


