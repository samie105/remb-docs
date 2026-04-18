---
title: "Drizzle <> Bun SQLite"
source: "https://orm.drizzle.team/docs/connect-bun-sqlite"
canonical_url: "https://orm.drizzle.team/docs/connect-bun-sqlite"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:45.653Z"
content_hash: "a1a72e2607799583dd86bdc8673dfd97fb22fef6330b161484a93968dd646e8a"
menu_path: ["Drizzle <> Bun SQLite"]
section_path: []
nav_prev: {"path": "drizzle/docs/connect-cloudflare-d1/index.md", "title": "Drizzle <> Cloudflare D1"}
nav_next: {"path": "drizzle/docs/connect-node-sqlite/index.md", "title": "Drizzle <> Node SQLite"}
---

According to the **[official website](https://bun.sh/)**, Bun is a fast all-in-one JavaScript runtime.

Drizzle ORM natively supports **[`bun:sqlite`](https://bun.sh/docs/api/sqlite)** module and it’s crazy fast 🚀

We embrace SQL dialects and dialect specific drivers and syntax and unlike any other ORM, for synchronous drivers like `bun:sqlite` we have both **async** and **sync** APIs and we mirror most popular SQLite-like `all`, `get`, `values` and `run` query methods syntax.

#### Step 1 - Install packages[](#step-1---install-packages)

npm

yarn

pnpm

bun

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

```
import { drizzle } from 'drizzle-orm/bun-sqlite';

const db = drizzle();

const result = await db.select().from(...);
```

If you need to provide your existing driver:

```
import { drizzle } from 'drizzle-orm/bun-sqlite';
import { Database } from 'bun:sqlite';

const sqlite = new Database('sqlite.db');
const db = drizzle({ client: sqlite });

const result = await db.select().from(...);
```

If you want to use **sync** APIs:

```
import { drizzle } from 'drizzle-orm/bun-sqlite';
import { Database } from 'bun:sqlite';

const sqlite = new Database('sqlite.db');
const db = drizzle({ client: sqlite });

const result = db.select().from(users).all();
const result = db.select().from(users).get();
const result = db.select().from(users).values();
const result = db.select().from(users).run();
```

#### What’s next?[](#whats-next)

