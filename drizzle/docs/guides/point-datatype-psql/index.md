---
title: "Drizzle ORM - Point datatype in PostgreSQL"
source: "https://orm.drizzle.team/docs/guides/point-datatype-psql"
canonical_url: "https://orm.drizzle.team/docs/guides/point-datatype-psql"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:05:49.343Z"
content_hash: "6444d59251786d452eea0b8cc75a12ccf3766e6bc454c215bcab85d5d3f6564b"
menu_path: ["Drizzle ORM - Point datatype in PostgreSQL"]
section_path: []
nav_prev: {"path": "drizzle/docs/guides/mysql-local-setup/index.md", "title": "Drizzle ORM - How to setup MySQL locally"}
nav_next: {"path": "drizzle/docs/guides/postgis-geometry-point/index.md", "title": "Drizzle ORM - PostGIS geometry point"}
---

Drizzle | Point datatype in PostgreSQL

PostgreSQL has a special datatype to store geometric data called `point`. It is used to represent a point in a two-dimensional space. The point datatype is represented as a pair of `(x, y)` coordinates. The point expects to receive longitude first, followed by latitude.

```
import { sql } from 'drizzle-orm';

const db = drizzle(...);

await db.execute(
  sql`select point(-90.9, 18.7)`,
);
```

```
[ 
  { 
    point: '(-90.9,18.7)' 
  }
]
```

This is how you can create table with `point` datatype in Drizzle:

```
import { pgTable, point, serial, text } from 'drizzle-orm/pg-core';

export const stores = pgTable('stores', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  location: point('location', { mode: 'xy' }).notNull(),
});
```

This is how you can insert point data into the table in Drizzle:

```
// mode: 'xy'
await db.insert(stores).values({
  name: 'Test',
  location: { x: -90.9, y: 18.7 },
});

// mode: 'tuple'
await db.insert(stores).values({
  name: 'Test',
  location: [-90.9, 18.7],
});

// sql raw
await db.insert(stores).values({
  name: 'Test',
  location: sql`point(-90.9, 18.7)`,
});
```

To compute the distance between the objects you can use `<->` operator. This is how you can query for the nearest location by coordinates in Drizzle:

IMPORTANT

`getColumns` available starting from `drizzle-orm@1.0.0-beta.2`(read more [here](drizzle/docs/upgrade-v1/index.md))

If you are on pre-1 version(like `0.45.1`) then use `getTableColumns`

```
import { getColumns, sql } from 'drizzle-orm';
import { stores } from './schema';

const point = {
  x: -73.935_242,
  y: 40.730_61,
};

const sqlDistance = sql`location <-> point(${point.x}, ${point.y})`;

await db
  .select({
    ...getColumns(stores),
    distance: sql`round((${sqlDistance})::numeric, 2)`,
  })
  .from(stores)
  .orderBy(sqlDistance)
  .limit(1);
```

```
select *, round((location <-> point(-73.935242, 40.73061))::numeric, 2)
from stores order by location <-> point(-73.935242, 40.73061)
limit 1;
```

To filter rows to include only those where a `point` type `location` falls within a specified rectangular boundary defined by two diagonal points you can user `<@` operator. It checks if the first object is contained in or on the second object:

```
const point = {
  x1: -88,
  x2: -73,
  y1: 40,
  y2: 43,
};

await db
  .select()
  .from(stores)
  .where(
    sql`${stores.location} <@ box(point(${point.x1}, ${point.y1}), point(${point.x2}, ${point.y2}))`
  );
```

```
select * from stores where location <@ box(point(-88, 40), point(-73, 43));
```
