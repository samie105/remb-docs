---
title: "Database connection with Drizzle"
source: "https://orm.drizzle.team/docs/connect-overview"
canonical_url: "https://orm.drizzle.team/docs/connect-overview"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:30:16.395Z"
content_hash: "61437c8a342a3b2b41ef462101947a035ae7b5719ec0d1dadf1b4ac93863a311"
menu_path: ["Database connection with Drizzle"]
section_path: []
content_language: "en"
---
Drizzle ORM runs SQL queries on your database via **database drivers**.

```ts
import { drizzle } from "drizzle-orm/node-postgres"
import { users } from "./schema"

const db = drizzle(process.env.DATABASE_URL);
const usersCount = await db.$count(users);
```

```plaintext
                        ┌──────────────────────┐
                        │   db.$count(users)   │ <--- drizzle query
                        └──────────────────────┘     
                            │               ʌ
select count(*) from users -│               │
                            │               │- [{ count: 0 }]
                            v               │
                         ┌─────────────────────┐
                         │    node-postgres    │ <--- database driver
                         └─────────────────────┘
                            │               ʌ
01101000 01100101 01111001 -│               │
                            │               │- 01110011 01110101 01110000
                            v               │
                         ┌────────────────────┐
                         │      Database      │ 
                         └────────────────────┘
```

```ts
import { pgTable, integer, text } from "drizzle-orm";

export const users = pgTable("users", {
  id: integer("id").generateAlwaysAsIdentity(),
  name: text("name"),
})
```

Under the hood Drizzle will create a **node-postgres** driver instance which you can access via `db.$client` if necessary

```ts
import { drizzle } from "drizzle-orm/node-postgres"

const db = drizzle(process.env.DATABASE_URL);
const pool = db.$client;
```

```ts
// above is equivalent to
import { drizzle } from "drizzle-orm/node-postgres";
import { Pool } from "pg";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});
const db = drizzle({ client: pool });
```

Drizzle is by design natively compatible with every **edge** or **serverless** runtime, whenever you’d need access to a serverless database - we’ve got you covered

Neon HTTP

Neon with websockets

Vercel Postgres

PlanetScale HTTP

Cloudflare d1

```ts
import { drizzle } from "drizzle-orm/neon-http";

const db = drizzle(process.env.DATABASE_URL);
```

```ts
import { drizzle } from "drizzle-orm/neon-serverless";

const db = drizzle(process.env.DATABASE_URL);
```

```ts
import { drizzle } from "drizzle-orm/vercel-postgres";

const db = drizzle();
```

```ts
import { drizzle } from "drizzle-orm/planetscale";

const db = drizzle(process.env.DATABASE_URL);
```

```ts
import { drizzle } from "drizzle-orm/d1";

const db = drizzle({ connection: env.DB });
```

And yes, we do support runtime specific drivers like [Bun SQLite](https://orm.drizzle.team/docs/connect-bun-sqlite) or [Expo SQLite](https://orm.drizzle.team/docs/connect-expo-sqlite):

```ts
import { drizzle } from "drizzle-orm/bun-sqlite"

const db = drizzle(); // <--- will create an in-memory db
const db = drizzle("./sqlite.db");
```

```ts
import { drizzle } from "drizzle-orm/expo-sqlite";
import { openDatabaseSync } from "expo-sqlite";

const expo = openDatabaseSync("db.db");
const db = drizzle(expo);
```

#### Database connection URL[](#database-connection-url)

Just in case if you’re not familiar with database connection URL concept

```plaintext
postgresql://alex:AbC123dEf@ep-cool-darkness-123456.us-east-2.aws.neon.tech/dbname
             └──┘ └───────┘ └─────────────────────────────────────────────┘ └────┘
              ʌ    ʌ          ʌ                                              ʌ
        role -│    │          │- hostname                                    │- database
                   │
                   │- password
```

#### Next steps[](#next-steps)

Feel free to check out per-driver documentations
