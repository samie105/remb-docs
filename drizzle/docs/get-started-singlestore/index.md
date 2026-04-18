---
title: "Drizzle <> SingleStore"
source: "https://orm.drizzle.team/docs/get-started-singlestore"
canonical_url: "https://orm.drizzle.team/docs/get-started-singlestore"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:48.663Z"
content_hash: "e2d675d6387c8c175598a19f7680119523281c6aebfb9f20495b2a37c56ee9a7"
menu_path: ["Drizzle <> SingleStore"]
section_path: []
nav_prev: {"path": "drizzle/docs/get-started-cockroach/index.md", "title": "Drizzle <> PostgreSQL"}
nav_next: {"path": "drizzle/docs/connect-planetscale-postgres/index.md", "title": "Drizzle <> PlanetScale Postgres"}
---

To use Drizzle with a SingleStore database, you should use the `mysql2` driver

Drizzle ORM natively supports `mysql2` with `drizzle-orm/singlestore` package.

#### Step 1 - Install packages[](#step-1---install-packages)

npm

yarn

pnpm

bun

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

mysql2

mysql with config

```
import { drizzle } from "drizzle-orm/singlestore";

const db = drizzle(process.env.DATABASE_URL);

const response = await db.select().from(...)
```

```
import { drizzle } from "drizzle-orm/singlestore";

// You can specify any property from the mysql2 connection options
const db = drizzle({ connection:{ uri: process.env.DATABASE_URL }});

const response = await db.select().from(...)
```

If you need to provide your existing driver:

Client connection

Pool connection

```
import { drizzle } from "drizzle-orm/singlestore";
import mysql from "mysql2/promise";

const connection = await mysql.createConnection({
  host: "host",
  user: "user",
  database: "database",
  ...
});

const db = drizzle({ client: connection });
```

```
import { drizzle } from "drizzle-orm/singlestore";
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

#### Limitations[](#limitations)

Currently, the SingleStore dialect has a set of limitations and features that do not work on the SingleStore database side:

*   SingleStore’s serial column type only ensures the uniqueness of column values.
*   `ORDER BY` and `LIMIT` cannot be chained together.
*   Foreign keys are not supported (check).
*   `INTERSECT ALL` and `EXCEPT ALL` operations are not supported by SingleStore.
*   Nested transactions are not supported by [SingleStore](https://docs.singlestore.com/cloud/reference/sql-reference/procedural-sql-reference/transactions-in-stored-procedures/).
*   SingleStore [only supports](https://docs.singlestore.com/cloud/getting-started-with-singlestore-helios/about-singlestore-helios/singlestore-helios-faqs/durability/) one `isolationLevel`.
*   The FSP option in `DATE`, `TIMESTAMP`, and `DATETIME` is not supported.
*   The relational API is not supported and will be implemented once the SingleStore team develops all the necessary APIs for it.
*   There may be more limitations because SingleStore is not 100% compatible with MySQL.

#### What’s next?[](#whats-next)

