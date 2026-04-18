---
title: "ConnInfo Helper ​"
source: "https://hono.dev/docs/helpers/conninfo"
canonical_url: "https://hono.dev/docs/helpers/conninfo"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:07.391Z"
content_hash: "a86dcf32a142685f28a757be69243577bfedc97bddd9ae22d7bcf985f5e7fa3d"
menu_path: ["ConnInfo Helper ​"]
section_path: []
nav_prev: {"path": "hono/docs/helpers/adapter/index.md", "title": "Adapter Helper \u200b"}
nav_next: {"path": "hono/docs/helpers/cookie/index.md", "title": "Cookie Helper \u200b"}
---

The ConnInfo Helper helps you to get the connection information. For example, you can get the client's remote address easily.

## Import [​](#import)

Cloudflare WorkersDenoBunVercelAWS LambdaCloudflare PagesNetlifyLambda@EdgeNode.js

ts

```
import { Hono } from 'hono'
import { getConnInfo } from 'hono/cloudflare-workers'
```

ts

```
import { Hono } from 'hono'
import { getConnInfo } from 'hono/deno'
```

ts

```
import { Hono } from 'hono'
import { getConnInfo } from 'hono/bun'
```

ts

```
import { Hono } from 'hono'
import { getConnInfo } from 'hono/vercel'
```

ts

```
import { Hono } from 'hono'
import { getConnInfo } from 'hono/aws-lambda'
```

ts

```
import { Hono } from 'hono'
import { getConnInfo } from 'hono/cloudflare-pages'
```

ts

```
import { Hono } from 'hono'
import { getConnInfo } from 'hono/netlify'
```

ts

```
import { Hono } from 'hono'
import { getConnInfo } from 'hono/lambda-edge'
```

ts

```
import { Hono } from 'hono'
import { getConnInfo } from '@hono/node-server/conninfo'
```

## Usage [​](#usage)

ts

```
const app = new Hono()

app.get('/', (c) => {
  const info = getConnInfo(c) // info is `ConnInfo`
  return c.text(`Your remote address is ${info.remote.address}`)
})
```

## Type Definitions [​](#type-definitions)

The type definitions of the values that you can get from `getConnInfo()` are the following:

ts

```
type AddressType = 'IPv6' | 'IPv4' | undefined

type NetAddrInfo = {
  /**
   * Transport protocol type
   */
  transport?: 'tcp' | 'udp'
  /**
   * Transport port number
   */
  port?: number

  address?: string
  addressType?: AddressType
} & (
  | {
      /**
       * Host name such as IP Addr
       */
      address: string

      /**
       * Host name type
       */
      addressType: AddressType
    }
  | {}
)

/**
 * HTTP Connection information
 */
interface ConnInfo {
  /**
   * Remote information
   */
  remote: NetAddrInfo
}
```


