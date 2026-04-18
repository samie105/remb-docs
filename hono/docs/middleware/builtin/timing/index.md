---
title: "Server-Timing Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/timing"
canonical_url: "https://hono.dev/docs/middleware/builtin/timing"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:11.608Z"
content_hash: "f792b08ef6629547f60b64f43c000423933a896ed12d43be281c85f3c8866bb8"
menu_path: ["Server-Timing Middleware ​"]
section_path: []
nav_prev: {"path": "hono/docs/middleware/builtin/timeout/index.md", "title": "Timeout Middleware \u200b"}
nav_next: {"path": "hono/docs/middleware/builtin/trailing-slash/index.md", "title": "Trailing Slash Middleware \u200b"}
---

## Server-Timing Middleware [​](#server-timing-middleware)

The [Server-Timing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Server-Timing) Middleware provides performance metrics in the response headers.

## Import [​](#import)

npm

ts

```
import { Hono } from 'hono'
import {
  timing,
  setMetric,
  startTime,
  endTime,
  wrapTime,
} from 'hono/timing'
import type { TimingVariables } from 'hono/timing'
```

## Usage [​](#usage)

js

```
// Specify the variable types to infer the `c.get('metric')`:
type Variables = TimingVariables

const app = new Hono<{ Variables: Variables }>()

// add the middleware to your router
app.use(timing());

app.get('/', async (c) => {

  // add custom metrics
  setMetric(c, 'region', 'europe-west3')

  // add custom metrics with timing, must be in milliseconds
  setMetric(c, 'custom', 23.8, 'My custom Metric')

  // start a new timer
  startTime(c, 'db');
  const data = await db.findMany(...);

  // end the timer
  endTime(c, 'db');

  // ...or you can also just wrap a Promise using this function:
  const data = await wrapTime(c, 'db', db.findMany(...));

  return c.json({ response: data });
});
```

### Conditionally enabled [​](#conditionally-enabled)

ts

```
const app = new Hono()

app.use(
  '*',
  timing({
    // c: Context of the request
    enabled: (c) => c.req.method === 'POST',
  })
)
```

## Result [​](#result)

![](https://hono.dev/images/timing-example.png)

## Options [​](#options)

### optional total: `boolean` [​](#total-boolean)

Show the total response time. The default is `true`.

### optional enabled: `boolean` | `(c: Context) => boolean` [​](#enabled-boolean-c-context-boolean)

Whether timings should be added to the headers or not. The default is `true`.

### optional totalDescription: `boolean` [​](#totaldescription-boolean)

Description for the total response time. The default is `Total Response Time`.

### optional autoEnd: `boolean` [​](#autoend-boolean)

If `startTime()` should end automatically at the end of the request. If disabled, not manually ended timers will not be shown.

### optional crossOrigin: `boolean` | `string` | `(c: Context) => boolean | string` [​](#crossorigin-boolean-string-c-context-boolean-string)

The origin this timings header should be readable.

*   If false, only from current origin.
*   If true, from all origin.
*   If string, from this domain(s). Multiple domains must be separated with a comma.

The default is `false`. See more [docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Timing-Allow-Origin).

