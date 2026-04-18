---
title: "Drizzle ORM - Update many with different values for each row"
source: "https://orm.drizzle.team/docs/guides/update-many-with-different-value"
canonical_url: "https://orm.drizzle.team/docs/guides/update-many-with-different-value"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:07:44.722Z"
content_hash: "7dc750daebb39badb1ec4050212c4e1f65ea98d7ac0742e995db16e03b579ec2"
menu_path: ["Drizzle ORM - Update many with different values for each row"]
section_path: []
nav_prev: {"path": "drizzle/docs/guides/unique-case-insensitive-email/index.md", "title": "Drizzle ORM - Unique and Case-Insensitive Email Handling"}
nav_next: {"path": "drizzle/docs/guides/upsert/index.md", "title": "Drizzle ORM - Upsert Query"}
---

Drizzle | Update many with different values for each row

PostgreSQL

MySQL

SQLite

To implement update many with different values for each row within 1 request you can use `sql` operator with `case` statement and `.update().set()` methods like this:

```
import { SQL, inArray, sql } from 'drizzle-orm';
import { users } from './schema';

const db = drizzle(...);

const inputs = [
  {
    id: 1,
    city: 'New York',
  },
  {
    id: 2,
    city: 'Los Angeles',
  },
  {
    id: 3,
    city: 'Chicago',
  },
];

// You have to be sure that inputs array is not empty
if (inputs.length === 0) {
  return;
}

const sqlChunks: SQL[] = [];
const ids: number[] = [];

sqlChunks.push(sql`(case`);

for (const input of inputs) {
  sqlChunks.push(sql`when ${users.id} = ${input.id} then ${input.city}`);
  ids.push(input.id);
}

sqlChunks.push(sql`end)`);

const finalSql: SQL = sql.join(sqlChunks, sql.raw(' '));

await db.update(users).set({ city: finalSql }).where(inArray(users.id, ids));
```

```
update users set "city" = 
  (case when id = 1 then 'New York' when id = 2 then 'Los Angeles' when id = 3 then 'Chicago' end)
where id in (1, 2, 3)
```

