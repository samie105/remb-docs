---
title: "Filter and conditional operators"
source: "https://orm.drizzle.team/docs/operators"
canonical_url: "https://orm.drizzle.team/docs/operators"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:17:36.567Z"
content_hash: "8b31c53673c56679ac52d873496d0b2e10bff1029125c990afcd5cc8b96c4e0b"
menu_path: ["Filter and conditional operators"]
section_path: []
nav_prev: {"path": "drizzle/docs/delete/index.md", "title": "SQL Delete"}
nav_next: {"path": "drizzle/docs/query-utils/index.md", "title": "Drizzle query utils"}
---

## Filter and conditional operators

We natively support all dialect specific filter and conditional operators.

You can import all filter & conditional from `drizzle-orm`:

```
import { eq, ne, gt, gte, ... } from "drizzle-orm";
```

### eq[](#eq)

PostgreSQL

MySQL

SQLite

SingleStore

Value equal to `n`

```
import { eq } from "drizzle-orm";

db.select().from(table).where(eq(table.column, 5));
```

```
SELECT * FROM table WHERE table.column = 5
```

```
import { eq } from "drizzle-orm";

db.select().from(table).where(eq(table.column1, table.column2));
```

```
SELECT * FROM table WHERE table.column1 = table.column2
```

### ne[](#ne)

PostgreSQL

MySQL

SQLite

SingleStore

Value is not equal to `n`

```
import { ne } from "drizzle-orm";

db.select().from(table).where(ne(table.column, 5));
```

```
SELECT * FROM table WHERE table.column <> 5
```

```
import { ne } from "drizzle-orm";

db.select().from(table).where(ne(table.column1, table.column2));
```

```
SELECT * FROM table WHERE table.column1 <> table.column2
```

### gt[](#gt)

PostgreSQL

MySQL

SQLite

SingleStore

Value is greater than `n`

```
import { gt } from "drizzle-orm";

db.select().from(table).where(gt(table.column, 5));
```

```
SELECT * FROM table WHERE table.column > 5
```

```
import { gt } from "drizzle-orm";

db.select().from(table).where(gt(table.column1, table.column2));
```

```
SELECT * FROM table WHERE table.column1 > table.column2
```

### gte[](#gte)

PostgreSQL

MySQL

SQLite

SingleStore

Value is greater than or equal to `n`

```
import { gte } from "drizzle-orm";

db.select().from(table).where(gte(table.column, 5));
```

```
SELECT * FROM table WHERE table.column >= 5
```

```
import { gte } from "drizzle-orm";

db.select().from(table).where(gte(table.column1, table.column2));
```

```
SELECT * FROM table WHERE table.column1 >= table.column2
```

### lt[](#lt)

PostgreSQL

MySQL

SQLite

SingleStore

Value is less than `n`

```
import { lt } from "drizzle-orm";

db.select().from(table).where(lt(table.column, 5));
```

```
SELECT * FROM table WHERE table.column < 5
```

```
import { lt } from "drizzle-orm";

db.select().from(table).where(lt(table.column1, table.column2));
```

```
SELECT * FROM table WHERE table.column1 < table.column2
```

### lte[](#lte)

PostgreSQL

MySQL

SQLite

SingleStore

Value is less than or equal to `n`.

```
import { lte } from "drizzle-orm";

db.select().from(table).where(lte(table.column, 5));
```

```
SELECT * FROM table WHERE table.column <= 5
```

```
import { lte } from "drizzle-orm";

db.select().from(table).where(lte(table.column1, table.column2));
```

```
SELECT * FROM table WHERE table.column1 <= table.column2
```

### exists[](#exists)

PostgreSQL

MySQL

SQLite

SingleStore

Value exists

```
import { exists } from "drizzle-orm";

const query = db.select().from(table2)
db.select().from(table).where(exists(query));
```

```
SELECT * FROM table WHERE EXISTS (SELECT * from table2)
```

### notExists[](#notexists)

```
import { notExists } from "drizzle-orm";

const query = db.select().from(table2)
db.select().from(table).where(notExists(query));
```

```
SELECT * FROM table WHERE NOT EXISTS (SELECT * from table2)
```

### isNull[](#isnull)

PostgreSQL

MySQL

SQLite

SingleStore

Value is `null`

```
import { isNull } from "drizzle-orm";

db.select().from(table).where(isNull(table.column));
```

```
SELECT * FROM table WHERE table.column IS NULL
```

### isNotNull[](#isnotnull)

PostgreSQL

MySQL

SQLite

SingleStore

Value is not `null`

```
import { isNotNull } from "drizzle-orm";

db.select().from(table).where(isNotNull(table.column));
```

```
SELECT * FROM table WHERE table.column IS NOT NULL
```

### inArray[](#inarray)

PostgreSQL

MySQL

SQLite

SingleStore

Value is in array of values

```
import { inArray } from "drizzle-orm";

db.select().from(table).where(inArray(table.column, [1, 2, 3, 4]));
```

```
SELECT * FROM table WHERE table.column in (1, 2, 3, 4)
```

```
import { inArray } from "drizzle-orm";

const query = db.select({ data: table2.column }).from(table2);
db.select().from(table).where(inArray(table.column, query));
```

```
SELECT * FROM table WHERE table.column IN (SELECT table2.column FROM table2)
```

### notInArray[](#notinarray)

PostgreSQL

MySQL

SQLite

SingleStore

Value is not in array of values

```
import { notInArray } from "drizzle-orm";

db.select().from(table).where(notInArray(table.column, [1, 2, 3, 4]));
```

```
SELECT * FROM table WHERE table.column NOT in (1, 2, 3, 4)
```

```
import { notInArray } from "drizzle-orm";

const query = db.select({ data: table2.column }).from(table2);
db.select().from(table).where(notInArray(table.column, query));
```

```
SELECT * FROM table WHERE table.column NOT IN (SELECT table2.column FROM table2)
```

### between[](#between)

PostgreSQL

MySQL

SQLite

SingleStore

Value is between two values

```
import { between } from "drizzle-orm";

db.select().from(table).where(between(table.column, 2, 7));
```

```
SELECT * FROM table WHERE table.column BETWEEN 2 AND 7
```

### notBetween[](#notbetween)

PostgreSQL

MySQL

SQLite

SingleStore

Value is not between two value

```
import { notBetween } from "drizzle-orm";

db.select().from(table).where(notBetween(table.column, 2, 7));
```

```
SELECT * FROM table WHERE table.column NOT BETWEEN 2 AND 7
```

### like[](#like)

PostgreSQL

MySQL

SQLite

SingleStore

Value is like other value, case sensitive

```
import { like } from "drizzle-orm";

db.select().from(table).where(like(table.column, "%llo wor%"));
```

```
SELECT * FROM table  WHERE table.column LIKE '%llo wor%'
```

### ilike[](#ilike)

PostgreSQL

MySQL

SQLite

SingleStore

Value is like some other value, case insensitive

```
import { ilike } from "drizzle-orm";

db.select().from(table).where(ilike(table.column, "%llo wor%"));
```

```
SELECT * FROM table WHERE table.column ILIKE '%llo wor%'
```

### notIlike[](#notilike)

PostgreSQL

MySQL

SQLite

SingleStore

Value is not like some other value, case insensitive

```
import { notIlike } from "drizzle-orm";

db.select().from(table).where(notIlike(table.column, "%llo wor%"));
```

```
SELECT * FROM table WHERE table.column NOT ILIKE '%llo wor%'
```

### not[](#not)

PostgreSQL

MySQL

SQLite

SingleStore

All conditions must return `false`.

```
import { eq, not } from "drizzle-orm";

db.select().from(table).where(not(eq(table.column, 5)));
```

```
SELECT * FROM table WHERE NOT (table.column = 5)
```

### and[](#and)

PostgreSQL

MySQL

SQLite

SingleStore

All conditions must return `true`.

```
import { gt, lt, and } from "drizzle-orm";

db.select().from(table).where(and(gt(table.column, 5), lt(table.column, 7)));
```

```
SELECT * FROM table WHERE (table.column > 5 AND table.column < 7)
```

### or[](#or)

PostgreSQL

MySQL

SQLite

SingleStore

One or more conditions must return `true`.

```
import { gt, lt, or } from "drizzle-orm";

db.select().from(table).where(or(gt(table.column, 5), lt(table.column, 7)));
```

```
SELECT * FROM table WHERE (table.column > 5 OR table.column < 7)
```

### arrayContains[](#arraycontains)

PostgreSQL

MySQL

SQLite

SingleStore

Test that a column or expression contains all elements of the list passed as the second argument

```
import { arrayContains } from "drizzle-orm";

const contains = await db.select({ id: posts.id }).from(posts)
  .where(arrayContains(posts.tags, ['Typescript', 'ORM']));

const withSubQuery = await db.select({ id: posts.id }).from(posts)
  .where(arrayContains(
    posts.tags,
    db.select({ tags: posts.tags }).from(posts).where(eq(posts.id, 1)),
  ));
```

```
select "id" from "posts" where "posts"."tags" @> {Typescript,ORM};
select "id" from "posts" where "posts"."tags" @> (select "tags" from "posts" where "posts"."id" = 1);
```

### arrayContained[](#arraycontained)

PostgreSQL

MySQL

SQLite

SingleStore

Test that the list passed as the second argument contains all elements of a column or expression

```
import { arrayContained } from "drizzle-orm";

const contained = await db.select({ id: posts.id }).from(posts)
  .where(arrayContained(posts.tags, ['Typescript', 'ORM']));
```

```
select "id" from "posts" where "posts"."tags" <@ {Typescript,ORM};
```

### arrayOverlaps[](#arrayoverlaps)

PostgreSQL

MySQL

SQLite

SingleStore

Test that a column or expression contains any elements of the list passed as the second argument.

```
import { arrayOverlaps } from "drizzle-orm";

const overlaps = await db.select({ id: posts.id }).from(posts)
  .where(arrayOverlaps(posts.tags, ['Typescript', 'ORM']));
```

```
select "id" from "posts" where "posts"."tags" && {Typescript,ORM}
```

