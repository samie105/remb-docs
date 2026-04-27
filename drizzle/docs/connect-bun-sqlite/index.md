---
title: "Drizzle <> Bun SQLite"
source: "https://orm.drizzle.team/docs/connect-bun-sqlite"
canonical_url: "https://orm.drizzle.team/docs/connect-bun-sqlite"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:27:27.065Z"
content_hash: "20a7220f7255f3a6add95581f8c1c056912907ad794632e78fd9693497ec75a6"
menu_path: ["Drizzle <> Bun SQLite"]
section_path: []
content_language: "en"
---
According to the **[official website](https://bun.sh/)**, Bun is a fast all-in-one JavaScript runtime.

Drizzle ORM natively supports **[`bun:sqlite`](https://bun.sh/docs/api/sqlite)** module and it’s crazy fast 🚀

We embrace SQL dialects and dialect specific drivers and syntax and unlike any other ORM, for synchronous drivers like `bun:sqlite` we have both **async** and **sync** APIs and we mirror most popular SQLite-like `all`, `get`, `values` and `run` query methods syntax.

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
import { drizzle } from 'drizzle-orm/bun-sqlite';

const db = drizzle();

const result = await db.select().from(...);
```

If you need to provide your existing driver:

```typescript
import { drizzle } from 'drizzle-orm/bun-sqlite';
import { Database } from 'bun:sqlite';

const sqlite = new Database('sqlite.db');
const db = drizzle({ client: sqlite });

const result = await db.select().from(...);
```

If you want to use **sync** APIs:

```typescript
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
