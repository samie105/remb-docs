---
title: "Validation ​"
source: "https://hono.dev/docs/guides/validation"
canonical_url: "https://hono.dev/docs/guides/validation"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:34.709Z"
content_hash: "655355a1eebdb8cd30ab1ea6cd5182eea733a7519e5c0fcb1ce5f4220bdde048"
menu_path: ["Validation ​"]
section_path: []
nav_prev: {"path": "../testing/index.md", "title": "Testing \u200b"}
nav_next: {"path": "../rpc/index.md", "title": "RPC \u200b"}
---

Hono provides only a very thin Validator. However, it can be powerful when combined with a third-party Validator. In addition, the RPC feature allows you to share API specifications with your clients through types.

## Manual validator [​](#manual-validator)

First, introduce a way to validate incoming values without using the third-party Validator.

Import `validator` from `hono/validator`.

ts

```
import { validator } from 'hono/validator'
```

To validate form data, specify `form` as the first argument and a callback as the second argument. In the callback, validates the value and return the validated values at the end. The `validator` can be used as middleware.

ts

```
app.post(
  '/posts',
  validator('form', (value, c) => {
    const body = value['body']
    if (!body || typeof body !== 'string') {
      return c.text('Invalid!', 400)
    }
    return {
      body: body,
    }
  }),
  //...
```

Within the handler, you can get the validated value with `c.req.valid('form')`.

ts

```
, (c) => {
  const { body } = c.req.valid('form')
  // ... do something
  return c.json(
    {
      message: 'Created!',
    },
    201
  )
}
```

Validation targets include `json`, `query`, `header`, `param` and `cookie` in addition to `form`.

WARNING

When you validate `json` or `form`, the request _must_ contain a matching `content-type` header (e.g. `Content-Type: application/json` for `json`). Otherwise, the request body will not be parsed and you will receive an empty object (`{}`) as value in the callback.

It is important to set the `content-type` header when testing using [`app.request()`](../../api/request/index.md).

Given an application like this.

ts

```
const app = new Hono()
app.post(
  '/testing',
  validator('json', (value, c) => {
    // pass-through validator
    return value
  }),
  (c) => {
    const body = c.req.valid('json')
    return c.json(body)
  }
)
```

Your tests can be written like this.

ts

```
// ❌ this will not work
const res = await app.request('/testing', {
  method: 'POST',
  body: JSON.stringify({ key: 'value' }),
})
const data = await res.json()
console.log(data) // {}

// ✅ this will work
const res = await app.request('/testing', {
  method: 'POST',
  body: JSON.stringify({ key: 'value' }),
  headers: new Headers({ 'Content-Type': 'application/json' }),
})
const data = await res.json()
console.log(data) // { key: 'value' }
```

WARNING

When you validate `header`, you need to use **lowercase** name as the key.

If you want to validate the `Idempotency-Key` header, you need to use `idempotency-key` as the key.

ts

```
// ❌ this will not work
app.post(
  '/api',
  validator('header', (value, c) => {
    // idempotencyKey is always undefined
    // so this middleware always return 400 as not expected
    const idempotencyKey = value['Idempotency-Key']

    if (idempotencyKey == undefined || idempotencyKey === '') {
      throw new HTTPException(400, {
        message: 'Idempotency-Key is required',
      })
    }
    return { idempotencyKey }
  }),
  (c) => {
    const { idempotencyKey } = c.req.valid('header')
    // ...
  }
)

// ✅ this will work
app.post(
  '/api',
  validator('header', (value, c) => {
    // can retrieve the value of the header as expected
    const idempotencyKey = value['idempotency-key']

    if (idempotencyKey == undefined || idempotencyKey === '') {
      throw new HTTPException(400, {
        message: 'Idempotency-Key is required',
      })
    }
    return { idempotencyKey }
  }),
  (c) => {
    const { idempotencyKey } = c.req.valid('header')
    // ...
  }
)
```

## Multiple validators [​](#multiple-validators)

You can also include multiple validators to validate different parts of request:

ts

```
app.post(
  '/posts/:id',
  validator('param', ...),
  validator('query', ...),
  validator('json', ...),
  (c) => {
    //...
  }
```

## With Zod [​](#with-zod)

You can use [Zod](https://zod.dev/), one of third-party validators. We recommend using a third-party validator.

Install from the Npm registry.

npmyarnpnpmbun

sh

```
npm i zod
```

sh

```
yarn add zod
```

sh

```
pnpm add zod
```

sh

```
bun add zod
```

Import `z` from `zod`.

ts

```
import * as z from 'zod'
```

Write your schema.

ts

```
const schema = z.object({
  body: z.string(),
})
```

You can use the schema in the callback function for validation and return the validated value.

ts

```
const route = app.post(
  '/posts',
  validator('form', (value, c) => {
    const parsed = schema.safeParse(value)
    if (!parsed.success) {
      return c.text('Invalid!', 401)
    }
    return parsed.data
  }),
  (c) => {
    const { body } = c.req.valid('form')
    // ... do something
    return c.json(
      {
        message: 'Created!',
      },
      201
    )
  }
)
```

## Zod Validator Middleware [​](#zod-validator-middleware)

You can use the [Zod Validator Middleware](https://github.com/honojs/middleware/tree/main/packages/zod-validator) to make it even easier.

npmyarnpnpmbun

sh

```
npm i @hono/zod-validator
```

sh

```
yarn add @hono/zod-validator
```

sh

```
pnpm add @hono/zod-validator
```

sh

```
bun add @hono/zod-validator
```

And import `zValidator`.

ts

```
import { zValidator } from '@hono/zod-validator'
```

And write as follows.

ts

```
const route = app.post(
  '/posts',
  zValidator(
    'form',
    z.object({
      body: z.string(),
    })
  ),
  (c) => {
    const validated = c.req.valid('form')
    // ... use your validated data
  }
)
```

## Standard Schema Validator Middleware [​](#standard-schema-validator-middleware)

[Standard Schema](https://standardschema.dev/) is a specification that provides a common interface for TypeScript validation libraries. It was created by the maintainers of Zod, Valibot, and ArkType to allow ecosystem tools to work with any validation library without needing custom adapters.

The [Standard Schema Validator Middleware](https://github.com/honojs/middleware/tree/main/packages/standard-validator) lets you use any Standard Schema-compatible validation library with Hono, giving you the flexibility to choose your preferred validator while maintaining consistent type safety.

npmyarnpnpmbun

sh

```
npm i @hono/standard-validator
```

sh

```
yarn add @hono/standard-validator
```

sh

```
pnpm add @hono/standard-validator
```

sh

```
bun add @hono/standard-validator
```

Import `sValidator` from the package:

ts

```
import { sValidator } from '@hono/standard-validator'
```

### With Zod [​](#with-zod-1)

You can use Zod with the Standard Schema validator:

npmyarnpnpmbun

sh

```
npm i zod
```

sh

```
yarn add zod
```

sh

```
pnpm add zod
```

sh

```
bun add zod
```

ts

```
import * as z from 'zod'
import { sValidator } from '@hono/standard-validator'

const schema = z.object({
  name: z.string(),
  age: z.number(),
})

app.post('/author', sValidator('json', schema), (c) => {
  const data = c.req.valid('json')
  return c.json({
    success: true,
    message: `${data.name} is ${data.age}`,
  })
})
```

### With Valibot [​](#with-valibot)

[Valibot](https://valibot.dev/) is a lightweight alternative to Zod with a modular design:

npmyarnpnpmbun

sh

```
npm i valibot
```

sh

```
yarn add valibot
```

sh

```
pnpm add valibot
```

sh

```
bun add valibot
```

ts

```
import * as v from 'valibot'
import { sValidator } from '@hono/standard-validator'

const schema = v.object({
  name: v.string(),
  age: v.number(),
})

app.post('/author', sValidator('json', schema), (c) => {
  const data = c.req.valid('json')
  return c.json({
    success: true,
    message: `${data.name} is ${data.age}`,
  })
})
```

### With ArkType [​](#with-arktype)

[ArkType](https://arktype.io/) offers TypeScript-native syntax for runtime validation:

npmyarnpnpmbun

sh

```
npm i arktype
```

sh

```
yarn add arktype
```

sh

```
pnpm add arktype
```

sh

```
bun add arktype
```

ts

```
import { type } from 'arktype'
import { sValidator } from '@hono/standard-validator'

const schema = type({
  name: 'string',
  age: 'number',
})

app.post('/author', sValidator('json', schema), (c) => {
  const data = c.req.valid('json')
  return c.json({
    success: true,
    message: `${data.name} is ${data.age}`,
  })
})
```
