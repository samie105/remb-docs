---
title: "Drizzle ORM - PostGIS geometry point"
source: "https://orm.drizzle.team/docs/guides/postgis-geometry-point"
canonical_url: "https://orm.drizzle.team/docs/guides/postgis-geometry-point"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:06:02.402Z"
content_hash: "64bcf7af7229ee24001b7dae2c7848a4c7479b30d51915c465510a2bb9ba0423"
menu_path: ["Drizzle ORM - PostGIS geometry point"]
section_path: []
nav_prev: {"path": "drizzle/docs/guides/point-datatype-psql/index.md", "title": "Drizzle ORM - Point datatype in PostgreSQL"}
nav_next: {"path": "drizzle/docs/guides/postgresql-full-text-search/index.md", "title": "Drizzle ORM - PostgreSQL full-text search"}
---

Drizzle | PostGIS geometry point

`PostGIS` extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data.

As for now, Drizzle doesn’t create extension automatically, so you need to create it manually. Create an empty migration file and add SQL query:

```
npx drizzle-kit generate --custom
```

```
CREATE EXTENSION postgis;
```

This is how you can create table with `geometry` datatype and spatial index in Drizzle:

schema.ts

migration.sql

```
import { geometry, index, pgTable, serial, text } from 'drizzle-orm/pg-core';

export const stores = pgTable(
  'stores',
  {
    id: serial('id').primaryKey(),
    name: text('name').notNull(),
    location: geometry('location', { type: 'point', mode: 'xy', srid: 4326 }).notNull(),
  },
  (t) => [
    index('spatial_index').using('gist', t.location),
  ]
);
```

```
CREATE TABLE IF NOT EXISTS "stores" (
    "id" serial PRIMARY KEY NOT NULL,
    "name" text NOT NULL,
    "location" geometry(point) NOT NULL
);
--> statement-breakpoint
CREATE INDEX IF NOT EXISTS "spatial_index" ON "stores" USING gist ("location");
```

This is how you can insert `geometry` data into the table in Drizzle. `ST_MakePoint()` in PostGIS creates a geometric object of type `point` using the specified coordinates. `ST_SetSRID()` sets the `SRID` (unique identifier associated with a specific coordinate system, tolerance, and resolution) on a geometry to a particular integer value:

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
  location: sql`ST_SetSRID(ST_MakePoint(-90.9, 18.7), 4326)`,
});
```

To compute the distance between the objects you can use `<->` operator and `ST_Distance()` function, which for `geometry types` returns the minimum planar distance between two geometries. This is how you can query for the nearest location by coordinates in Drizzle with PostGIS:

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

const sqlPoint = sql`ST_SetSRID(ST_MakePoint(${point.x}, ${point.y}), 4326)`;

await db
  .select({
    ...getColumns(stores),
    distance: sql`ST_Distance(${stores.location}, ${sqlPoint})`,
  })
  .from(stores)
  .orderBy(sql`${stores.location} <-> ${sqlPoint}`)
  .limit(1);
```

```
select *, ST_Distance(location, ST_SetSRID(ST_MakePoint(-73.935_242, 40.730_61), 4326))
from stores order by location <-> ST_SetSRID(ST_MakePoint(-73.935_242, 40.730_61), 4326)
limit 1;
```

To filter stores located within a specified rectangular area, you can use `ST_MakeEnvelope()` and `ST_Within()` functions. `ST_MakeEnvelope()` creates a rectangular Polygon from the minimum and maximum values for X and Y. `ST_Within()` Returns TRUE if geometry A is within geometry B.

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
    sql`ST_Within(
      ${stores.location}, ST_MakeEnvelope(${point.x1}, ${point.y1}, ${point.x2}, ${point.y2}, 4326)
    )`,
  );
```

```
select * from stores where ST_Within(location, ST_MakeEnvelope(-88, 40, -73, 43, 4326));
```


