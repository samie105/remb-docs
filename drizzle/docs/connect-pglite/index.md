---
title: "Drizzle <> PGlite"
source: "https://orm.drizzle.team/docs/connect-pglite"
canonical_url: "https://orm.drizzle.team/docs/connect-pglite"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:30:49.684Z"
content_hash: "4a439b8efc48582e4b71969f4b55228f0dd068a64d56c77c15ef9a84f7234485"
menu_path: ["Drizzle <> PGlite"]
section_path: []
content_language: "en"
---
According to the **[official repo](https://github.com/electric-sql/pglite)**, PGlite is a WASM Postgres build packaged into a TypeScript client library that enables you to run Postgres in the browser, Node.js and Bun, with no need to install any other dependencies. It is only 2.6mb gzipped.

It can be used as an ephemeral in-memory database, or with persistence either to the file system (Node/Bun) or indexedDB (Browser).

Unlike previous “Postgres in the browser” projects, PGlite does not use a Linux virtual machine - it is simply Postgres in WASM.

#### Step 1 - Install packages[](#step-1---install-packages)

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

```typescript
import { drizzle } from 'drizzle-orm/pglite';

const db = drizzle();

await db.select().from(...);
```

```typescript
import { drizzle } from 'drizzle-orm/pglite';

const db = drizzle('path-to-dir');

await db.select().from(...);
```

```typescript
import { drizzle } from 'drizzle-orm/pglite';

// connection is a native PGLite configuration
const db = drizzle({ connection: { dataDir: 'path-to-dir' }});

await db.select().from(...);
```

If you need to provide your existing driver:

```typescript
import { PGlite } from '@electric-sql/pglite';
import { drizzle } from 'drizzle-orm/pglite';

// In-memory Postgres
const client = new PGlite();
const db = drizzle({ client });

await db.select().from(users);
```

#### What’s next?[](#whats-next)
