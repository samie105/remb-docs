---
title: "PostgreSQL extensions"
source: "https://www.prisma.io/docs/orm/prisma-schema/postgresql-extensions"
canonical_url: "https://www.prisma.io/docs/orm/prisma-schema/postgresql-extensions"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:34:34.756Z"
content_hash: "08446dbdc7f1a903dab29588ec6da5f868bb58fcf692313c1fed6cacd99cb085"
menu_path: ["PostgreSQL extensions"]
section_path: []
tab_variants: ["npm","pnpm","yarn","bun","npm","pnpm","yarn","bun"]
content_language: "en"
---
How to install and manage PostgreSQL extensions with Prisma ORM using customized migrations, and how to use them in Prisma Client

This page is about [PostgreSQL extensions](https://www.postgresql.org/docs/current/external-extensions.html) and explains how to use them with Prisma ORM.

## [What are PostgreSQL extensions?](#what-are-postgresql-extensions)

PostgreSQL allows you to extend your database functionality by installing and activating packages known as _extensions_. For example, the `citext` extension adds a case-insensitive string data type. Some extensions, such as `citext`, are supplied directly by PostgreSQL, while other extensions are developed externally. For more information on extensions, see [the PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-createextension.html).

To use an extension, it must first be _installed_ on the local file system of your database server. You then need to _activate_ the extension, which runs a script file that adds the new functionality.

## [Using a PostgreSQL extension with Prisma ORM](#using-a-postgresql-extension-with-prisma-orm)

Let's walk through an example of installing the `citext` extension.

### [1\. Create an empty migration](#1-create-an-empty-migration)

Run the following command to create an empty migration that you can [customize](https://www.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations):

### [2\. Add a SQL statement to install the extension](#2-add-a-sql-statement-to-install-the-extension)

In the new migration file that was created in the `migrations` directory, add the following statement:

```
CREATE EXTENSION IF NOT EXISTS citext;
```

### [3\. Deploy the migration](#3-deploy-the-migration)

Run the following command to deploy the migration and apply to your database:

### [4\. Use the extension](#4-use-the-extension)

You can now use the extension in your queries with Prisma Client. If the extension has special data types that currently can't be natively represented in the Prisma schema, you can still define fields of that type on your models using the [`Unsupported`](https://www.prisma.io/docs/orm/prisma-schema/data-model/models#unsupported-types) fallback type.

## [PostGIS extension for spatial data](#postgis-extension-for-spatial-data)

PostGIS enables spatial and geographic objects for PostgreSQL, allowing you to store and query location data, routes, boundaries, and other geographic features. Prisma ORM provides native support for PostGIS geometry types.

### [Prerequisites](#prerequisites)

1.  Install PostGIS on your PostgreSQL server
2.  Enable the extension in your database:

```
CREATE EXTENSION IF NOT EXISTS postgis;
```

### [Using the Geometry type](#using-the-geometry-type)

Once PostGIS is enabled, you can use the native `Geometry` type in your Prisma schema:

```
model Location {
  id       Int      @id @default(autoincrement())
  name     String
  position Geometry(Point, 4326)?
}

model Route {
  id   Int      @id @default(autoincrement())
  name String
  path Geometry(LineString, 4326)?
}

model Zone {
  id       Int      @id @default(autoincrement())
  name     String
  boundary Geometry(Polygon, 4326)?
}
```

The `Geometry` type supports various shapes:

-   `Point` - Single location (e.g., restaurant, store)
-   `LineString` - Path or route
-   `Polygon` - Area or boundary
-   `MultiPoint`, `MultiLineString`, `MultiPolygon` - Collections of geometries

### [Native spatial operations](#native-spatial-operations)

Prisma Client provides native filters and ordering for spatial queries:

```
// Find locations within 1km radius
const nearby = await prisma.location.findMany({
  where: {
    position: {
      near: {
        point: [13.4, 52.5],
        maxDistance: 1000,
      },
    },
  },
});

// Find points within a polygon boundary
const withinArea = await prisma.location.findMany({
  where: {
    position: {
      within: {
        polygon: [
          [0, 0],
          [0, 10],
          [10, 10],
          [10, 0],
          [0, 0],
        ],
      },
    },
  },
});

// Sort by distance from a reference point
const sorted = await prisma.location.findMany({
  orderBy: {
    position: {
      distanceFrom: {
        point: [13.4, 52.5],
        direction: "asc",
      },
    },
  },
  take: 10,
});
```

For detailed usage, examples, and real-world use cases, see [Working with geometry fields](https://www.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-geometry-fields).
