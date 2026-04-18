---
title: "IP Restriction Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/ip-restriction"
canonical_url: "https://hono.dev/docs/middleware/builtin/ip-restriction"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:30.356Z"
content_hash: "c6c0290683fa2126c299e288a8d06e9924ce08882b7001bdd7270b6f3c24656d"
menu_path: ["IP Restriction Middleware ​"]
section_path: []
---
## IP Restriction Middleware [​](#ip-restriction-middleware)

IP Restriction Middleware is middleware that limits access to resources based on the IP address of the user.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { ipRestriction } from 'hono/ip-restriction'
```

## Usage [​](#usage)

For your application running on Bun, if you want to allow access only from local, you can write it as follows. Specify the rules you want to deny in the `denyList` and the rules you want to allow in the `allowList`.

ts

```
import { Hono } from 'hono'
import { getConnInfo } from 'hono/bun'
import { ipRestriction } from 'hono/ip-restriction'

const app = new Hono()

app.use(
  '*',
  ipRestriction(getConnInfo, {
    denyList: [],
    allowList: ['127.0.0.1', '::1'],
  })
)

app.get('/', (c) => c.text('Hello Hono!'))
```

Pass the `getConninfo` from the [ConnInfo helper](https://hono.dev/docs/helpers/conninfo) appropriate for your environment as the first argument of `ipRestriction`. For example, for Deno, it would look like this:

ts

```
import { getConnInfo } from 'hono/deno'
import { ipRestriction } from 'hono/ip-restriction'

//...

app.use(
  '*',
  ipRestriction(getConnInfo, {
    // ...
  })
)
```

## Rules [​](#rules)

Follow the instructions below for writing rules.

### IPv4 [​](#ipv4)

*   `192.168.2.0` - Static IP Address
*   `192.168.2.0/24` - CIDR Notation
*   `*` - ALL Addresses

### IPv6 [​](#ipv6)

*   `::1` - Static IP Address
*   `::1/10` - CIDR Notation
*   `*` - ALL Addresses

## Error handling [​](#error-handling)

To customize the error, return a `Response` in the third argument.

ts

```
app.use(
  '*',
  ipRestriction(
    getConnInfo,
    {
      denyList: ['192.168.2.0/24'],
    },
    async (remote, c) => {
      return c.text(`Blocking access from ${remote.addr}`, 403)
    }
  )
)
```
