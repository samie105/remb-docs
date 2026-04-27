---
title: "Drizzle <> MySQL"
source: "https://orm.drizzle.team/docs/get-started-mysql"
canonical_url: "https://orm.drizzle.team/docs/get-started-mysql"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:40:52.991Z"
content_hash: "9a6dded7491593e3960f60515f26d10a94bbf3a5178bb9347c2041d34e77773c"
menu_path: ["Drizzle <> MySQL"]
section_path: []
content_language: "en"
---
To use Drizzle with a MySQL database, you should use the `mysql2` driver

According to the **[official website](https://github.com/sidorares/node-mysql2)**, `mysql2` is a MySQL client for Node.js with focus on performance.

Drizzle ORM natively supports `mysql2` with `drizzle-orm/mysql2` package.

#### Step 1 - Install packages[](#step-1---install-packages)

```
npm i drizzle-orm mysql2
npm i -D drizzle-kit
```

```
yarn add drizzle-orm mysql2
yarn add -D drizzle-kit
```

```
pnpm add drizzle-orm mysql2
pnpm add -D drizzle-kit
```

```
bun add drizzle-orm mysql2
bun add -D drizzle-kit
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

```typescript
import { drizzle } from "drizzle-orm/mysql2";

const db = drizzle(process.env.DATABASE_URL);

const response = await db.select().from(...)
```

```typescript
import { drizzle } from "drizzle-orm/mysql2";

// You can specify any property from the mysql2 connection options
const db = drizzle({ connection:{ uri: process.env.DATABASE_URL }});

const response = await db.select().from(...)
```

If you need to provide your existing driver:

Client connection

Pool connection

```typescript
import { drizzle } from "drizzle-orm/mysql2";
import mysql from "mysql2/promise";

const connection = await mysql.createConnection({
  host: "host",
  user: "user",
  database: "database",
  ...
});

const db = drizzle({ client: connection });
```

```typescript
import { drizzle } from "drizzle-orm/mysql2";
import mysql from "mysql2/promise";

const poolConnection = mysql.createPool({
  host: "host",
  user: "user",
  database: "database",
  ...
});

const db = drizzle({ client: poolConnection });
```

IMPORTANT

For the built in `migrate` function with DDL migrations we and drivers strongly encourage you to use single `client` connection.

For querying purposes feel free to use either `client` or `pool` based on your business demands.

#### What’s next?[](#whats-next)
