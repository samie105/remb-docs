---
title: "Working with geometry fields"
source: "https://www.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-geometry-fields"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-geometry-fields"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:47.908Z"
content_hash: "b2e1d715814ddea34990c1654f0f96d2c3c2f0796c37ef6f3b7cb2ce3eaa318d"
menu_path: ["Working with geometry fields"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields/index.md", "title": "Working with Json fields"}
nav_next: {"path": "prisma/docs/orm/prisma-client/testing/integration-testing/index.md", "title": "Integration testing"}
---

# Create an empty migration
npx prisma migrate dev --create-only

# Add the CREATE INDEX statement to the generated SQL file
# Then apply the migration
npx prisma migrate dev
```

### [PostgreSQL 16 query planner issue](#postgresql-16-query-planner-issue)

:::warning PostgreSQL 16 users with large datasets

If you're using **PostgreSQL 16** with datasets containing thousands of records, you may encounter slow spatial queries (3-5 seconds instead of `<100ms`) due to a query planner bug that was fixed in PostgreSQL 17+. **Symptom:** Queries with `near`, `within`, or `intersects` are unexpectedly slow despite having GIST indexes.

**Cause:** PostgreSQL 16 underestimates the number of rows returned by spatial Common Table Expressions (CTEs), causing it to choose Nested Loop joins instead of Hash Joins. This results in thousands of unnecessary loop iterations.

**Workaround:** Use the `withSpatialOptimization` helper from `@prisma/adapter-pg`:

```
import { PrismaClient } from '@prisma/client'
import { withSpatialOptimization } from '@prisma/adapter-pg'

const userLocation = [13.4, 52.5] as [number, number]

// The helper automatically detects PostgreSQL 16 and applies optimization only when needed
const nearby = await withSpatialOptimization(
  prisma,
  (client) => client.location.findMany({
    where: {
      position: {
        near: {
          point: userLocation,
          maxDistance: 5000,
        },
      },
    },
    orderBy: {
      position: {
        distanceFrom: userLocation,
      },
    },
    take: 20,
  })
)

// Works with all spatial filters:
const zonesContaining = await withSpatialOptimization(
  prisma,
  (client) => client.deliveryZone.findMany({
    where: {
      boundary: {
        intersects: {
          type: 'Point',
          coordinates: userLocation,
        },
      },
    },
  })
)
```

The helper:

*   **Automatically detects** PostgreSQL version (cached for performance)
*   **Only applies optimization** on PostgreSQL 16
*   **Skips optimization** on PostgreSQL 17+ (where the bug is fixed)
*   **Handles errors gracefully** if version detection fails

**Important notes:**

*   The helper is **safe to use on all PostgreSQL versions**—it automatically detects PostgreSQL 16 and only applies the optimization when needed.
*   On PostgreSQL 17+, the helper runs queries normally without any optimization (the bug is already fixed).
*   The optimization uses `SET LOCAL` which only affects the current transaction and is automatically reverted.
*   While the helper is safe, only use it for spatial queries that you've confirmed are slow—it adds a small version-detection overhead on first use (cached afterward).
*   Always ensure you have **GIST indexes** on your geometry columns—this optimization does not replace proper indexing.

**Best practice:** If you can upgrade to PostgreSQL 17+, the bug is fixed natively and you won't need this workaround at all.

:::

### [Choose the right SRID](#choose-the-right-srid)

The SRID affects both coordinate interpretation and distance calculations. Choosing the wrong SRID can lead to inaccurate results or slow queries:

*   **SRID 4326 (WGS 84)**: Best for worldwide GPS data with lat/long coordinates. Distance calculations use spherical geometry (accurate for Earth's curvature). This is the recommended choice for most applications.
    
*   **SRID 3857 (Web Mercator)**: Optimized for web mapping and visualization. Uses planar geometry (faster but less accurate for distance calculations, especially near poles). Use for display purposes, not distance measurements.
    
*   **Local SRIDs**: Use region-specific SRIDs (e.g., 2154 for France, 27700 for UK) for highly accurate local measurements within a specific country or region. These provide the most accurate distance calculations for their area.
    

### [Query optimization tips](#query-optimization-tips)

*   **Limit results**: Combine `near` filters with `take` to avoid fetching too many records:
    
    ```
    const nearby = await prisma.location.findMany({
      where: { position: { near: { point: [13.4, 52.5], maxDistance: 5000 } } },
      take: 20, // Only return 20 closest results
    });
    ```
    
*   **Server-side filtering**: Use native geometry filters instead of fetching all data and filtering in JavaScript:
    
    ```
    // ❌ Bad: Fetch all and filter in JavaScript
    const all = await prisma.location.findMany();
    const nearby = all.filter((loc) => calculateDistance(loc.position, myPoint) < 1000);
    
    // ✅ Good: Filter in database
    const nearby = await prisma.location.findMany({
      where: { position: { near: { point: myPoint, maxDistance: 1000 } } },
    });
    ```
    
*   **Combine filters**: Use multiple conditions to narrow down results before distance calculations:
    
    ```
    const results = await prisma.restaurant.findMany({
      where: {
        AND: [
          { isOpen: true }, // Regular filter first
          { rating: { gte: 4 } }, // Filter by rating
          { location: { near: { point: [13.4, 52.5], maxDistance: 2000 } } }, // Then spatial filter
        ],
      },
    });
    ```
    

Before Prisma added native `Geometry` support, developers had to use the `Unsupported` type to work with PostGIS columns. If you have an existing schema using `Unsupported("geometry(...)")`, you can migrate to the native `Geometry` type to gain access to native filters and ordering without any breaking changes to your data or application code.

### [Before](#before)

```
model Location {
  id       Int                                 @id @default(autoincrement())
  position Unsupported("geometry(Point,4326)")?
}
```

### [After](#after)

```
model Location {
  id       Int               @id @default(autoincrement())
  position Geometry(Point, 4326)?
}
```

### [Migration steps](#migration-steps)

1.  Update your Prisma schema to use `Geometry(...)` instead of `Unsupported(...)`
2.  Run `npx prisma generate` to regenerate Prisma Client
3.  No changes to your application code are required - the GeoJSON format remains identical

When working with geometry fields, there are several important details to keep in mind to avoid common mistakes and unexpected behavior.

### [Coordinate order](#coordinate-order)

One of the most common mistakes when working with geographic data is using the wrong coordinate order. GeoJSON and PostGIS use `[longitude, latitude]` order, which is opposite to how we typically say addresses ("Paris is at 48.85° latitude, 2.35° longitude"):

```
// ✅ Correct: [longitude, latitude]
const berlin = { type: "Point", coordinates: [13.4, 52.5], srid: 4326 };

// ❌ Wrong: [latitude, longitude]
const wrong = { type: "Point", coordinates: [52.5, 13.4], srid: 4326 };
```

### [Closing polygon rings](#closing-polygon-rings)

Polygons in PostGIS must have closed rings, meaning the first and last coordinate pairs must be identical. This is a requirement of the GeoJSON specification and PostGIS will reject polygons with unclosed rings:

```
// ✅ Correct: Closed ring
const polygon = [
  [0, 0],
  [0, 10],
  [10, 10],
  [10, 0],
  [0, 0],
];

// ❌ Wrong: Unclosed ring
const unclosed = [
  [0, 0],
  [0, 10],
  [10, 10],
  [10, 0],
]; // Missing closing point
```

### [Distance units](#distance-units)

Understanding distance units is crucial for setting correct `maxDistance` values and interpreting distance calculations. The units depend on your SRID:

*   **SRID 4326 (WGS 84)**: Distances are in **meters** when using spherical calculations (which Prisma does automatically). For example, `maxDistance: 1000` means 1 kilometer.
    
*   **SRID 3857 (Web Mercator)**: Distances are in the projection's units (typically meters for local areas, but accuracy degrades with distance). Not recommended for distance measurements.
    
*   **Local SRIDs**: Distances are typically in meters or feet depending on the specific projection. Check the SRID documentation at [epsg.io](https://epsg.io/).
    

Always use consistent units across your application and document which SRID you're using.

### [Null handling](#null-handling)

By default, geometry filters only match records where the geometry field is not `NULL`. This is usually what you want, but can be surprising if you're not expecting it. For example, a `near` filter won't include locations where the position is `NULL`, even if you have an optional geometry field in your schema.

To include records with null geometry in your results, you need to explicitly handle them with separate queries or combine with null checks:

```
// Find locations either within area OR with no position set
const locationsWithinOrNull = await prisma.location.findMany({
  where: {
    OR: [
      { position: null },
      { position: { within: { polygon: [...] } } },
    ],
  },
});
```

*   [CRUD operations](prisma/docs/orm/prisma-client/queries/crud/index.md) for general query patterns
*   [Filtering and sorting](https://www.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting) for more filter options
*   [PostgreSQL extensions](prisma/docs/orm/prisma-schema/postgresql-extensions/index.md) for enabling PostGIS
*   [PostGIS documentation](https://postgis.net/documentation/) for advanced spatial operations
*   [GeoJSON specification](https://geojson.org/) for geometry format details

