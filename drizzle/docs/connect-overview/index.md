---
title: "Database connection with Drizzle"
source: "https://orm.drizzle.team/docs/connect-overview"
canonical_url: "https://orm.drizzle.team/docs/connect-overview"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:34.188Z"
content_hash: "bb4624bf38695477bd74cbc74b4666e351f885b08398fbe692770866c91e3c0c"
menu_path: ["Database connection with Drizzle"]
section_path: []
nav_prev: {"path": "drizzle/docs/relations-schema-declaration/index.md", "title": "Drizzle Relations Fundamentals"}
nav_next: {"path": "drizzle/docs/data-querying/index.md", "title": "Drizzle Queries + CRUD"}
---

Drizzle ORM runs SQL queries on your database via **database drivers**.

index.ts

schema.ts

```
import { drizzle } from "drizzle-orm/node-postgres"
import { users } from "./schema"

const db = drizzle(process.env.DATABASE_URL);
const usersCount = await db.$count(users);
```

```
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

```
import { pgTable, integer, text } from "drizzle-orm";

export const users = pgTable("users", {
  id: integer("id").generateAlwaysAsIdentity(),
  name: text("name"),
})
```

Under the hood Drizzle will create a **node-postgres** driver instance which you can access via `db.$client` if necessary

```
import { drizzle } from "drizzle-orm/node-postgres"

const db = drizzle(process.env.DATABASE_URL);
const pool = db.$client;
```

```
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

```
import { drizzle } from "drizzle-orm/neon-http";

const db = drizzle(process.env.DATABASE_URL);
```

```
import { drizzle } from "drizzle-orm/neon-serverless";

const db = drizzle(process.env.DATABASE_URL);
```

```
import { drizzle } from "drizzle-orm/vercel-postgres";

const db = drizzle();
```

```
import { drizzle } from "drizzle-orm/planetscale";

const db = drizzle(process.env.DATABASE_URL);
```

```
import { drizzle } from "drizzle-orm/d1";

const db = drizzle({ connection: env.DB });
```

And yes, we do support runtime specific drivers like [Bun SQLite](drizzle/docs/connect-bun-sqlite/index.md) or [Expo SQLite](drizzle/docs/connect-expo-sqlite/index.md):

```
import { drizzle } from "drizzle-orm/bun-sqlite"

const db = drizzle(); // <--- will create an in-memory db
const db = drizzle("./sqlite.db");
```

```
import { drizzle } from "drizzle-orm/expo-sqlite";
import { openDatabaseSync } from "expo-sqlite";

const expo = openDatabaseSync("db.db");
const db = drizzle(expo);
```

#### Database connection URL[](#database-connection-url)

Just in case if you’re not familiar with database connection URL concept

```
postgresql://alex:AbC123dEf@ep-cool-darkness-123456.us-east-2.aws.neon.tech/dbname
             └──┘ └───────┘ └─────────────────────────────────────────────┘ └────┘
              ʌ    ʌ          ʌ                                              ʌ
        role -│    │          │- hostname                                    │- database
                   │
                   │- password
```

#### Next steps[](#next-steps)

Feel free to check out per-driver documentations


