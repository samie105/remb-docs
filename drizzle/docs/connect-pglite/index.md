---
title: "Drizzle <> PGlite"
source: "https://orm.drizzle.team/docs/connect-pglite"
canonical_url: "https://orm.drizzle.team/docs/connect-pglite"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:34.687Z"
content_hash: "86baef8854f2ee27b0f57814f9fdadaa30d458dc9b0c882598e1ea9b3cc4d68d"
menu_path: ["Drizzle <> PGlite"]
section_path: []
nav_prev: {"path": "drizzle/docs/connect-xata/index.md", "title": "Drizzle <> Xata"}
nav_next: {"path": "drizzle/docs/connect-nile/index.md", "title": "Drizzle <> Nile"}
---

According to the **[official repo](https://github.com/electric-sql/pglite)**, PGlite is a WASM Postgres build packaged into a TypeScript client library that enables you to run Postgres in the browser, Node.js and Bun, with no need to install any other dependencies. It is only 2.6mb gzipped.

It can be used as an ephemeral in-memory database, or with persistence either to the file system (Node/Bun) or indexedDB (Browser).

Unlike previous “Postgres in the browser” projects, PGlite does not use a Linux virtual machine - it is simply Postgres in WASM.

#### Step 1 - Install packages[](#step-1---install-packages)

npm

yarn

pnpm

bun

```
npm i drizzle-orm @electric-sql/pglite
npm i -D drizzle-kit
```

```
yarn add drizzle-orm @electric-sql/pglite
yarn add -D drizzle-kit
```

```
pnpm add drizzle-orm @electric-sql/pglite
pnpm add -D drizzle-kit
```

```
bun add drizzle-orm @electric-sql/pglite
bun add -D drizzle-kit
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

In-Memory

In directory

With extra config options

```
import { drizzle } from 'drizzle-orm/pglite';

const db = drizzle();

await db.select().from(...);
```

```
import { drizzle } from 'drizzle-orm/pglite';

const db = drizzle('path-to-dir');

await db.select().from(...);
```

```
import { drizzle } from 'drizzle-orm/pglite';

// connection is a native PGLite configuration
const db = drizzle({ connection: { dataDir: 'path-to-dir' }});

await db.select().from(...);
```

If you need to provide your existing driver:

```
import { PGlite } from '@electric-sql/pglite';
import { drizzle } from 'drizzle-orm/pglite';

// In-memory Postgres
const client = new PGlite();
const db = drizzle({ client });

await db.select().from(users);
```

#### What’s next?[](#whats-next)
