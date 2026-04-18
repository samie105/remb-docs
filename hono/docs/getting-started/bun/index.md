---
title: "Bun ​"
source: "https://hono.dev/docs/getting-started/bun"
canonical_url: "https://hono.dev/docs/getting-started/bun"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:57.843Z"
content_hash: "f2be62890ae52fccfc2a21c06bf7937ec6520b5e67a88b0ab7ec1c15d1be5556"
menu_path: ["Bun ​"]
section_path: []
---
[Bun](https://bun.com/) is another JavaScript runtime. It's not Node.js or Deno. Bun includes a transcompiler, we can write the code with TypeScript. Hono also works on Bun.

## 1\. Install Bun [​](#_1-install-bun)

To install `bun` command, follow the instruction in [the official web site](https://bun.com/).

## 2\. Setup [​](#_2-setup)

### 2.1. Setup a new project [​](#_2-1-setup-a-new-project)

A starter for Bun is available. Start your project with "bun create" command. Select `bun` template for this example.

sh

```
bun create hono@latest my-app
```

Move into my-app and install the dependencies.

sh

```
cd my-app
bun install
```

### 2.2. Setup an existing project [​](#_2-2-setup-an-existing-project)

On an existing Bun project, we only need to install `hono` dependencies on the project root directory via

sh

```
bun add hono
```

Then add the `dev` command to your existing `package.json`.

json

```
{
  "scripts": {
    "dev": "bun run --hot src/index.ts"
  }
}
```

See the [Bun starter template](https://github.com/honojs/starter/tree/main/templates/bun) for a minimal example setup. This is the output of running `bun create hono@latest`.

## 3\. Hello World [​](#_3-hello-world)

"Hello World" script is below. Almost the same as writing on other platforms.

ts

```
import { Hono } from 'hono'

const app = new Hono()
app.get('/', (c) => c.text('Hello Bun!'))

export default app
```

If you are setting up Hono on an existing project, the `bun run dev` command expects the "Hello World" script to be placed in `src/index.tx`

## 4\. Run [​](#_4-run)

Run the command.

sh

```
bun run dev
```

Then, access `http://localhost:3000` in your browser.

## Change port number [​](#change-port-number)

You can specify the port number with exporting the `port`.

ts

```
import { Hono } from 'hono'

const app = new Hono()
app.get('/', (c) => c.text('Hello Bun!'))

export default app 
export default { 
  port: 3000, 
  fetch: app.fetch, 
} 
```

## Serve static files [​](#serve-static-files)

To serve static files, use `serveStatic` which is imported from `hono/bun`.

ts

```
import { serveStatic } from 'hono/bun'

const app = new Hono()

app.use('/static/*', serveStatic({ root: './' }))
app.use('/favicon.ico', serveStatic({ path: './favicon.ico' }))
app.get('/', (c) => c.text('You can access: /static/hello.txt'))
app.get('*', serveStatic({ path: './static/fallback.txt' }))
```

For the above code, it will work well with the following directory structure.

```
./
├── favicon.ico
├── src
└── static
    ├── demo
    │   └── index.html
    ├── fallback.txt
    ├── hello.txt
    └── images
        └── dinotocat.png
```

### `rewriteRequestPath` [​](#rewriterequestpath)

If you want to map `http://localhost:3000/static/*` to `./statics`, you can use the `rewriteRequestPath` option:

ts

```
app.get(
  '/static/*',
  serveStatic({
    root: './',
    rewriteRequestPath: (path) =>
      path.replace(/^\/static/, '/statics'),
  })
)
```

### `mimes` [​](#mimes)

You can add MIME types with `mimes`:

ts

```
app.get(
  '/static/*',
  serveStatic({
    mimes: {
      m3u8: 'application/vnd.apple.mpegurl',
      ts: 'video/mp2t',
    },
  })
)
```

### `onFound` [​](#onfound)

You can specify handling when the requested file is found with `onFound`:

ts

```
app.get(
  '/static/*',
  serveStatic({
    // ...
    onFound: (_path, c) => {
      c.header('Cache-Control', `public, immutable, max-age=31536000`)
    },
  })
)
```

### `onNotFound` [​](#onnotfound)

You can specify handling when the requested file is not found with `onNotFound`:

ts

```
app.get(
  '/static/*',
  serveStatic({
    onNotFound: (path, c) => {
      console.log(`${path} is not found, you access ${c.req.path}`)
    },
  })
)
```

### `precompressed` [​](#precompressed)

The `precompressed` option checks if files with extensions like `.br` or `.gz` are available and serves them based on the `Accept-Encoding` header. It prioritizes Brotli, then Zstd, and Gzip. If none are available, it serves the original file.

ts

```
app.get(
  '/static/*',
  serveStatic({
    precompressed: true,
  })
)
```

## Testing [​](#testing)

You can use `bun:test` for testing on Bun.

ts

```
import { describe, expect, it } from 'bun:test'
import app from '.'

describe('My first test', () => {
  it('Should return 200 Response', async () => {
    const req = new Request('http://localhost/')
    const res = await app.fetch(req)
    expect(res.status).toBe(200)
  })
})
```

Then, run the command.

sh

```
bun test index.test.ts
```
