---
title: "Drizzle <> Turso Cloud"
source: "https://orm.drizzle.team/docs/connect-turso"
canonical_url: "https://orm.drizzle.team/docs/connect-turso"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:15.250Z"
content_hash: "aa6e88c0b19eea4869ddd4a933dfae4bd064bb9beaa2183bd87d2e1f593bcd01"
menu_path: ["Drizzle <> Turso Cloud"]
section_path: []
nav_prev: {"path": "drizzle/docs/connect-tidb/index.md", "title": "Drizzle <> TiDB Serverless"}
nav_next: {"path": "drizzle/docs/connect-turso-database/index.md", "title": "Drizzle <> Turso Database"}
---

According to the **[official website](https://turso.tech/drizzle)**, Turso is a **[libSQL](https://github.com/libsql/libsql)** powered edge SQLite database as a service.

Drizzle ORM natively supports libSQL driver. We embrace SQL dialects and dialect specific drivers and syntax and mirror most popular SQLite-like `all`, `get`, `values` and `run` query methods syntax.

#### Step 1 - Install packages[](#step-1---install-packages)

npm

yarn

pnpm

bun

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

Drizzle has native support for all `@libsql/client` driver variations:

`@libsql/client`

defaults to `node` import, automatically changes to `web` if `target` or `platform` is set for bundler, e.g. `esbuild --platform=browser`

`@libsql/client/node`

`node` compatible module, supports `:memory:`, `file`, `wss`, `http` and `turso` connection protocols

`@libsql/client/web`

module for fullstack web frameworks like `next`, `nuxt`, `astro`, etc.

`@libsql/client/http`

module for `http` and `https` connection protocols

`@libsql/client/ws`

module for `ws` and `wss` connection protocols

`@libsql/client/sqlite3`

module for `:memory:` and `file` connection protocols

`@libsql/client-wasm`

Separate experimental package for WASM

  

default

node

web

http

web sockets

wasm

```
import { drizzle } from 'drizzle-orm/libsql';

const db = drizzle({ connection: {
  url: process.env.DATABASE_URL, 
  authToken: process.env.DATABASE_AUTH_TOKEN 
}});
```

```
import { drizzle } from 'drizzle-orm/libsql/node';

const db = drizzle({ connection: {
  url: process.env.DATABASE_URL, 
  authToken: process.env.DATABASE_AUTH_TOKEN 
}});
```

```
import { drizzle } from 'drizzle-orm/libsql/web';

const db = drizzle({ connection: {
  url: process.env.DATABASE_URL, 
  authToken: process.env.DATABASE_AUTH_TOKEN 
}});
```

```
import { drizzle } from 'drizzle-orm/libsql/http';

const db = drizzle({ connection: {
  url: process.env.DATABASE_URL, 
  authToken: process.env.DATABASE_AUTH_TOKEN 
}});
```

```
import { drizzle } from 'drizzle-orm/libsql/ws';

const db = drizzle({ connection: {
  url: process.env.DATABASE_URL, 
  authToken: process.env.DATABASE_AUTH_TOKEN 
}});
```

```
import { drizzle } from 'drizzle-orm/libsql/wasm';

const db = drizzle({ connection: {
  url: process.env.DATABASE_URL, 
  authToken: process.env.DATABASE_AUTH_TOKEN 
}});
```

If you need to provide your existing driver:

default

web

```
import { drizzle } from 'drizzle-orm/libsql';
import { createClient } from '@libsql/client';

const client = createClient({ 
  url: process.env.DATABASE_URL,
  authToken: process.env.DATABASE_AUTH_TOKEN
});

const db = drizzle({ client });

const result = await db.select().from(users).all()
```

```
import { drizzle } from 'drizzle-orm/libsql/web';
import { createClient } from '@libsql/client/web';

const client = createClient({ 
  url: process.env.DATABASE_URL,
  authToken: process.env.DATABASE_AUTH_TOKEN
});

const db = drizzle({ client });

const result = await db.select().from(users).all()
```

#### Step 3 - make a query[](#step-3---make-a-query)

```
import { drizzle } from 'drizzle-orm/libsql';
import * as s from 'drizzle-orm/sqlite-core';

const db = drizzle({ connection: {
  url: process.env.DATABASE_URL, 
  authToken: process.env.DATABASE_AUTH_TOKEN 
}});

const users = s.sqliteTable("users", {
  id: s.integer(),
  name: s.text(),
})

const result = await db.select().from(users);
```

#### What’s next?[](#whats-next)
