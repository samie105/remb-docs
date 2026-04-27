---
title: "Drizzle <> SQLite"
source: "https://orm.drizzle.team/docs/get-started-sqlite"
canonical_url: "https://orm.drizzle.team/docs/get-started-sqlite"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:41:27.546Z"
content_hash: "80d74397a583fb012676792b7c65064f971cdfceb0fa968c91eddf81c511b19d"
menu_path: ["Drizzle <> SQLite"]
section_path: []
content_language: "en"
---
Drizzle has native support for SQLite connections with the `libsql` and `better-sqlite3` drivers.

There are a few differences between the `libsql` and `better-sqlite3` drivers that we discovered while using both and integrating them with the Drizzle ORM. For example:

At the driver level, there may not be many differences between the two, but the main one is that `libSQL` can connect to both SQLite files and `Turso` remote databases. LibSQL is a fork of SQLite that offers a bit more functionality compared to standard SQLite, such as:

-   More ALTER statements are available with the `libSQL` driver, allowing you to manage your schema more easily than with just `better-sqlite3`.
-   You can configure the encryption at rest feature natively.
-   A large set of extensions supported by the SQLite database is also supported by `libSQL`.

## libsql[](#libsql)

#### Step 1 - Install packages[](#step-1---install-packages)

```
npm i drizzle-orm @libsql/client
npm i -D drizzle-kit
```

```
yarn add drizzle-orm @libsql/client
yarn add -D drizzle-kit
```

```
pnpm add drizzle-orm @libsql/client
pnpm add -D drizzle-kit
```

```
bun add drizzle-orm @libsql/client
bun add -D drizzle-kit
```

#### Step 2 - Initialize the driver[](#step-2---initialize-the-driver)

Drizzle has native support for all @libsql/client driver variations:

|  |  |
| --- | --- |
| `@libsql/client` | defaults to `node` import, automatically changes to `web` if `target` or `platform` is set for bundler, e.g. `esbuild --platform=browser` |
| `@libsql/client/node` | `node` compatible module, supports `:memory:`, `file`, `wss`, `http` and `turso` connection protocols |
| `@libsql/client/web` | module for fullstack web frameworks like `next`, `nuxt`, `astro`, etc. |
| `@libsql/client/http` | module for `http` and `https` connection protocols |
| `@libsql/client/ws` | module for `ws` and `wss` connection protocols |
| `@libsql/client/sqlite3` | module for `:memory:` and `file` connection protocols |
| `@libsql/client-wasm` | Separate experimental package for WASM |

  

default

node

web

http

web sockets

wasm

```typescript
import { drizzle } from 'drizzle-orm/libsql';

const db = drizzle({ connection: {
  url: process.env.DATABASE_URL, 
  authToken: process.env.DATABASE_AUTH_TOKEN 
}});
```

```typescript
import { drizzle } from 'drizzle-orm/libsql/node';

const db = drizzle({ connection: {
  url: process.env.DATABASE_URL, 
  authToken: process.env.DATABASE_AUTH_TOKEN 
}});
```

```typescript
import { drizzle } from 'drizzle-orm/libsql/web';

const db = drizzle({ connection: {
  url: process.env.DATABASE_URL, 
  authToken: process.env.DATABASE_AUTH_TOKEN 
}});
```

```typescript
import { drizzle } from 'drizzle-orm/libsql/http';

const db = drizzle({ connection: {
  url: process.env.DATABASE_URL, 
  authToken: process.env.DATABASE_AUTH_TOKEN 
}});
```

```typescript
import { drizzle } from 'drizzle-orm/libsql/ws';

const db = drizzle({ connection: {
  url: process.env.DATABASE_URL, 
  authToken: process.env.DATABASE_AUTH_TOKEN 
}});
```

```typescript
import { drizzle } from 'drizzle-orm/libsql/wasm';

const db = drizzle({ connection: {
  url: process.env.DATABASE_URL, 
  authToken: process.env.DATABASE_AUTH_TOKEN 
}});
```

#### Step 3 - make a query[](#step-3---make-a-query)

```typescript
import { drizzle } from 'drizzle-orm/libsql';

const db = drizzle(process.env.DATABASE_URL);
 
const result = await db.execute('select 1');
```

```typescript
import { drizzle } from 'drizzle-orm/libsql';

// You can specify any property from the libsql connection options
const db = drizzle({ connection: { url:'', authToken: '' }});
 
const result = await db.execute('select 1');
```

If you need a synchronous connection, you can use our additional connection API, where you specify a driver connection and pass it to the Drizzle instance.

```typescript
import { drizzle } from 'drizzle-orm/libsql';
import { createClient } from '@libsql/client';

const client = createClient({ url: process.env.DATABASE_URL, authToken: process.env.DATABASE_AUTH_TOKEN });
const db = drizzle(client);

const result = await db.execute('select 1');
```

## better-sqlite3[](#better-sqlite3)

#### Step 1 - Install packages[](#step-1---install-packages-1)

```
npm i drizzle-orm better-sqlite3
npm i -D drizzle-kit @types/better-sqlite3
```

```
yarn add drizzle-orm better-sqlite3
yarn add -D drizzle-kit @types/better-sqlite3
```

```
pnpm add drizzle-orm better-sqlite3
pnpm add -D drizzle-kit @types/better-sqlite3
```

```
bun add drizzle-orm better-sqlite3
bun add -D drizzle-kit @types/better-sqlite3
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

better-sqlite3

better-sqlite3 with config

```typescript
import { drizzle } from 'drizzle-orm/better-sqlite3';

const db = drizzle(process.env.DATABASE_URL);

const result = await db.execute('select 1');
```

```typescript
import { drizzle } from 'drizzle-orm/better-sqlite3';

// You can specify any property from the better-sqlite3 connection options
const db =  drizzle({ connection: { source: process.env.DATABASE_URL }});

const result = await db.execute('select 1');
```

If you need to provide your existing driver:

```typescript
import { drizzle } from 'drizzle-orm/better-sqlite3';
import Database from 'better-sqlite3';

const sqlite = new Database('sqlite.db');
const db = drizzle({ client: sqlite });

const result = await db.execute('select 1');
```

#### What’s next?[](#whats-next)
