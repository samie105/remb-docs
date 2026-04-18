---
title: "JWK Auth Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/jwk"
canonical_url: "https://hono.dev/docs/middleware/builtin/jwk"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:10.197Z"
content_hash: "1e1e314caeabb249f7677c1b9397560019c8c2f8ba21ad437bea1e775037ad47"
menu_path: ["JWK Auth Middleware ​"]
section_path: []
nav_prev: {"path": "hono/docs/middleware/builtin/jsx-renderer/index.md", "title": "JSX Renderer Middleware \u200b"}
nav_next: {"path": "hono/docs/middleware/builtin/jwt/index.md", "title": "JWT Auth Middleware \u200b"}
---

## JWK Auth Middleware [​](#jwk-auth-middleware)

The JWK Auth Middleware authenticates requests by verifying tokens using JWK (JSON Web Key). It checks for an `Authorization` header and other configured sources, such as cookies, if specified. It validates tokens using the provided `keys`, retrieves keys from `jwks_uri` if specified, and supports token extraction from cookies if the `cookie` option is set.

## What this middleware validates [​](#what-this-middleware-validates)

For each token, `jwk()`:

*   Parses and validates the JWT header format.
*   Requires a `kid` header and finds a matching key by `kid`.
*   Rejects symmetric algorithms (`HS256`, `HS384`, `HS512`).
*   Requires the header `alg` to be included in the configured `alg` allowlist.
*   If a matched JWK has an `alg` field, requires it to match the JWT header `alg`.
*   Verifies the token signature with the matched key.
*   By default, validates time-based claims: `nbf`, `exp`, and `iat`.

Optional claim validation can be configured with the `verification` option:

*   `iss`: validates issuer when provided.
*   `aud`: validates audience when provided.

If you need additional token checks beyond the above (for example, custom application-level authorization rules), add them in your own middleware after `jwk()`.

INFO

The Authorization header sent from the client must have a specified scheme.

Example: `Bearer my.token.value` or `Basic my.token.value`

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { jwk } from 'hono/jwk'
import { verifyWithJwks } from 'hono/jwt'
```

## Usage [​](#usage)

ts

```
const app = new Hono()

app.use(
  '/auth/*',
  jwk({
    jwks_uri: `https://${backendServer}/.well-known/jwks.json`,
    alg: ['RS256'],
  })
)

app.get('/auth/page', (c) => {
  return c.text('You are authorized')
})
```

Get payload:

ts

```
const app = new Hono()

app.use(
  '/auth/*',
  jwk({
    jwks_uri: `https://${backendServer}/.well-known/jwks.json`,
    alg: ['RS256'],
  })
)

app.get('/auth/page', (c) => {
  const payload = c.get('jwtPayload')
  return c.json(payload) // eg: { "sub": "1234567890", "name": "John Doe", "iat": 1516239022 }
})
```

Anonymous access:

ts

```
const app = new Hono()

app.use(
  '/auth/*',
  jwk({
    jwks_uri: (c) =>
      `https://${c.env.authServer}/.well-known/jwks.json`,
    alg: ['RS256'],
    allow_anon: true,
  })
)

app.get('/auth/page', (c) => {
  const payload = c.get('jwtPayload')
  return c.json(payload ?? { message: 'hello anon' })
})
```

## Using `verifyWithJwks` outside of middleware [​](#using-verifywithjwks-outside-of-middleware)

The `verifyWithJwks` utility function can be used to verify JWT tokens outside of Hono's middleware context, such as in SvelteKit SSR pages or other server-side environments:

ts

```
const id_payload = await verifyWithJwks(
  id_token,
  {
    jwks_uri: 'https://your-auth-server/.well-known/jwks.json',
    allowedAlgorithms: ['RS256'],
  },
  {
    cf: { cacheEverything: true, cacheTtl: 3600 },
  }
)
```

## Configuring JWKS fetch request options [​](#configuring-jwks-fetch-request-options)

To configure how JWKS is retrieved from `jwks_uri`, pass fetch request options as the second argument of `jwk()`.

This argument is `RequestInit` and is used only for the JWKS fetch request.

ts

```
const app = new Hono()

app.use(
  '/auth/*',
  jwk(
    {
      jwks_uri: `https://${backendServer}/.well-known/jwks.json`,
      alg: ['RS256'],
    },
    {
      headers: {
        Authorization: 'Bearer TOKEN',
      },
    }
  )
)
```

## Options [​](#options)

### required alg: `AsymmetricAlgorithm[]` [​](#alg-asymmetricalgorithm)

An array of allowed asymmetric algorithms used for token verification.

Available types are `RS256` | `RS384` | `RS512` | `PS256` | `PS384` | `PS512` | `ES256` | `ES384` | `ES512` | `EdDSA`.

### optional keys: `HonoJsonWebKey[] | (c: Context) => Promise<HonoJsonWebKey[]>` [​](#keys-honojsonwebkey-c-context-promise-honojsonwebkey)

The values of your public keys, or a function that returns them. The function receives the Context object.

### optional jwks\_uri: `string` | `(c: Context) => Promise<string>` [​](#jwks-uri-string-c-context-promise-string)

If this value is set, attempt to fetch JWKs from this URI, expecting a JSON response with `keys`, which are added to the provided `keys` option. You can also pass a callback function to dynamically determine the JWKS URI using the Context.

### optional allow\_anon: `boolean` [​](#allow-anon-boolean)

If this value is set to `true`, requests without a valid token will be allowed to pass through the middleware. Use `c.get('jwtPayload')` to check if the request is authenticated. The default is `false`.

### optional cookie: `string` [​](#cookie-string)

If this value is set, then the value is retrieved from the cookie header using that value as a key, which is then validated as a token.

### optional headerName: `string` [​](#headername-string)

The name of the header to look for the JWT token. The default is `Authorization`.

### optional verification: `VerifyOptions` [​](#verification-verifyoptions)

Configure claim validation behavior in addition to signature verification:

*   `iss`: expected issuer.
*   `aud`: expected audience.
*   `exp`, `nbf`, `iat`: enabled by default, can be disabled if needed.


