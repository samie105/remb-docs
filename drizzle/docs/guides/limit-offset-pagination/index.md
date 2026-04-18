---
title: "Drizzle ORM - SQL Limit/Offset pagination"
source: "https://orm.drizzle.team/docs/guides/limit-offset-pagination"
canonical_url: "https://orm.drizzle.team/docs/guides/limit-offset-pagination"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:05:28.526Z"
content_hash: "842f1215489691d39724d1ed329db213f1defb64fa27a0390aabc914101b356d"
menu_path: ["Drizzle ORM - SQL Limit/Offset pagination"]
section_path: []
nav_prev: {"path": "drizzle/docs/guides/incrementing-a-value/index.md", "title": "Drizzle ORM - SQL Increment value"}
nav_next: {"path": "drizzle/docs/guides/mysql-local-setup/index.md", "title": "Drizzle ORM - How to setup MySQL locally"}
---

Drizzle | SQL Limit/Offset pagination

PostgreSQL

MySQL

SQLite

This guide demonstrates how to implement `limit/offset` pagination in Drizzle:

index.ts

schema.ts

```
import { asc } from 'drizzle-orm';
import { users } from './schema';

const db = drizzle(...);

await db
  .select()
  .from(users)
  .orderBy(asc(users.id)) // order by is mandatory
  .limit(4) // the number of rows to return
  .offset(4); // the number of rows to skip
```

```
select * from users order by id asc limit 4 offset 4;
```

```
// 5-8 rows returned
[
  {
    id: 5,
    firstName: 'Beth',
    lastName: 'Davis',
    createdAt: 2024-03-11T20:51:46.787Z
  },
  {
    id: 6,
    firstName: 'Charlie',
    lastName: 'Miller',
    createdAt: 2024-03-11T21:15:46.787Z
  },
  {
    id: 7,
    firstName: 'Clara',
    lastName: 'Wilson',
    createdAt: 2024-03-11T21:33:46.787Z
  },
  {
    id: 8,
    firstName: 'David',
    lastName: 'Moore',
    createdAt: 2024-03-11T21:45:46.787Z
  }
]
```

Limit is the number of rows to return `(page size)` and offset is the number of rows to skip `((page number - 1) * page size)`. For consistent pagination, ensure ordering by a unique column. Otherwise, the results can be inconsistent.

If you need to order by a non-unique column, you should also append a unique column to the ordering.

This is how you can implement `limit/offset` pagination with 2 columns:

```
const getUsers = async (page = 1, pageSize = 3) => {
  await db
    .select()
    .from(users)
    .orderBy(asc(users.firstName), asc(users.id)) // order by first_name (non-unique), id (pk)
    .limit(pageSize) 
    .offset((page - 1) * pageSize);
}

await getUsers();
```

Drizzle has useful relational queries API, that lets you easily implement `limit/offset` pagination:

```
import * as schema from './db/schema';

const db = drizzle({ schema });

const getUsers = async (page = 1, pageSize = 3) => {
  await db.query.users.findMany({
    orderBy: (users, { asc }) => asc(users.id),
    limit: pageSize,
    offset: (page - 1) * pageSize,
  });
};

await getUsers();
```

Drizzle has simple and flexible API, which lets you easily create custom solutions. This is how you can create custom function for pagination using `.$dynamic()` function:

```
import { SQL, asc } from 'drizzle-orm';
import { PgColumn, PgSelect } from 'drizzle-orm/pg-core';

function withPagination<T extends PgSelect>(
  qb: T,
  orderByColumn: PgColumn | SQL | SQL.Aliased,
  page = 1,
  pageSize = 3,
) {
  return qb
    .orderBy(orderByColumn)
    .limit(pageSize)
    .offset((page - 1) * pageSize);
}

const query = db.select().from(users); // query that you want to execute with pagination

await withPagination(query.$dynamic(), asc(users.id));
```

You can improve performance of `limit/offset` pagination by using `deferred join` technique. This method performs the pagination on a subset of the data instead of the entire table.

To implement it you can do like this:

```
const getUsers = async (page = 1, pageSize = 10) => {
   const sq = db
    .select({ id: users.id })
    .from(users)
    .orderBy(users.id)
    .limit(pageSize)
    .offset((page - 1) * pageSize)
    .as('subquery');

   await db.select().from(users).innerJoin(sq, eq(users.id, sq.id)).orderBy(users.id);
};
```

**Benefits** of `limit/offset` pagination: it’s simple to implement and pages are easily reachable, which means that you can navigate to any page without having to save the state of the previous pages.

**Drawbacks** of `limit/offset` pagination: degradation in query performance with increasing offset because database has to scan all rows before the offset to skip them, and inconsistency due to data shifts, which can lead to the same row being returned on different pages or rows being skipped.

This is how it works:

```
const getUsers = async (page = 1, pageSize = 3) => {
  await db
    .select()
    .from(users)
    .orderBy(asc(users.id))
    .limit(pageSize)
    .offset((page - 1) * pageSize);
};

// user is browsing the first page
await getUsers();
```

```
// results for the first page
[
  {
    id: 1,
    firstName: 'Alice',
    lastName: 'Johnson',
    createdAt: 2024-03-10T17:17:06.148Z
  },
  {
    id: 2,
    firstName: 'Alex',
    lastName: 'Smith',
    createdAt: 2024-03-10T17:19:06.147Z
  },
  {
    id: 3,
    firstName: 'Aaron',
    lastName: 'Williams',
    createdAt: 2024-03-10T17:22:06.147Z
  }
]
```

```
// while user is browsing the first page, a row with id 2 is deleted
await db.delete(users).where(eq(users.id, 2));

// user navigates to the second page
await getUsers(2);
```

```
// second page, row with id 3 was skipped
[
  {
    id: 5,
    firstName: 'Beth',
    lastName: 'Davis',
    createdAt: 2024-03-10T17:34:06.147Z
  },
  {
    id: 6,
    firstName: 'Charlie',
    lastName: 'Miller',
    createdAt: 2024-03-10T17:58:06.147Z
  },
  {
    id: 7,
    firstName: 'Clara',
    lastName: 'Wilson',
    createdAt: 2024-03-10T18:16:06.147Z
  }
]
```

So, if your database experiences frequently insert and delete operations in real time or you need high performance to paginate large tables, you should consider using [cursor-based](drizzle/docs/guides/cursor-based-pagination/index.md) pagination instead.

To learn more about `deferred join` technique you should follow these guides: [Planetscale Pagination Guide](https://planetscale.com/blog/mysql-pagination) and [Efficient Pagination Guide by Aaron Francis](https://aaronfrancis.com/2022/efficient-pagination-using-deferred-joins).


