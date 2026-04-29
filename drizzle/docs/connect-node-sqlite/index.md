---
title: "Drizzle <> Node SQLite"
source: "https://orm.drizzle.team/docs/connect-node-sqlite"
canonical_url: "https://orm.drizzle.team/docs/connect-node-sqlite"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:29:42.113Z"
content_hash: "7ae809f83b80ea69c791979056c786455666d21d544786adf6d5258d6803e22a"
menu_path: ["Drizzle <> Node SQLite"]
section_path: []
content_language: "en"
nav_prev: {"path": "../connect-bun-sqlite/index.md", "title": "Drizzle <> Bun SQLite"}
nav_next: {"path": "../connect-cloudflare-do/index.md", "title": "Drizzle <> Cloudflare Durable Objects SQLite"}
---

Drizzle ORM natively supports **[`node:sqlite`](https://nodejs.org/api/sqlite.html)** module

We embrace SQL dialects and dialect specific drivers and syntax and unlike any other ORM, for synchronous drivers like `node:sqlite` we have both **async** and **sync** APIs and we mirror most popular SQLite-like `all`, `get`, `values` and `run` query methods syntax.

#### Step 1 - Install packages[](#step-1---install-packages)

```
npm i drizzle-orm
npm i -D drizzle-kit
```

```
yarn add drizzle-orm
yarn add -D drizzle-kit
```

```
pnpm add drizzle-orm
pnpm add -D drizzle-kit
```

```
bun add drizzle-orm
bun add -D drizzle-kit
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

```typescript
import { drizzle } from 'drizzle-orm/node-sqlite';

const db = drizzle("sqlite.db");

const result = await db.select().from(...);
```

If you need to provide your existing driver:

```typescript
import { drizzle } from 'drizzle-orm/node-sqlite';
import { DatabaseSync } from 'node:sqlite';

const sqlite = new DatabaseSync('sqlite.db');
const db = drizzle({ client: sqlite });

const result = await db.select().from(...);
```

If you want to use **sync** APIs:

```typescript
import { drizzle } from 'drizzle-orm/node-sqlite';
import { DatabaseSync } from 'node:sqlite';

const sqlite = new Database('sqlite.db');
const db = drizzle({ client: sqlite });

const result = db.select().from(users).all();
const result = db.select().from(users).get();
const result = db.select().from(users).values();
const result = db.select().from(users).run();
```

#### What’s next?[](#whats-next)
