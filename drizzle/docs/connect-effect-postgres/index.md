---
title: "Drizzle <> Effect Postgres"
source: "https://orm.drizzle.team/docs/connect-effect-postgres"
canonical_url: "https://orm.drizzle.team/docs/connect-effect-postgres"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:41.095Z"
content_hash: "d122230831f62526b9d3dfc7d8867bfe155f07f4e756f182e153cf083cdf69ae"
menu_path: ["Drizzle <> Effect Postgres"]
section_path: []
nav_prev: {"path": "drizzle/docs/connect-bun-sql/index.md", "title": "Drizzle <> Bun SQL"}
nav_next: {"path": "drizzle/docs/connect-planetscale/index.md", "title": "Drizzle <> PlanetScale MySQL"}
---

WARNING

This page explains concepts available on drizzle versions `1.0.0-beta.9` and higher.

Effect is only available for PostgreSQL right now and soon be implemented for all other dialects

On how to upgrade (read more [here](drizzle/docs/upgrade-v1/index.md))

Drizzle has native support for Effect PostgreSQL connections with the `@effect/sql-pg` driver.

#### Step 1 - Install packages[](#step-1---install-packages)

npm

yarn

pnpm

bun

```
npm i drizzle-orm effect @effect/sql-pg pg
npm i -D drizzle-kit @types/pg
```

```
yarn add drizzle-orm effect @effect/sql-pg pg
yarn add -D drizzle-kit @types/pg
```

```
pnpm add drizzle-orm effect @effect/sql-pg pg
pnpm add -D drizzle-kit @types/pg
```

```
bun add drizzle-orm effect @effect/sql-pg pg
bun add -D drizzle-kit @types/pg
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

Drizzle provides an Effect-native API that integrates with Effect’s service pattern. Use `PgDrizzle.makeWithDefaults()` to quickly create a Drizzle database instance with sensible defaults (no logging, no caching).

```
import 'dotenv/config';
import * as PgDrizzle from 'drizzle-orm/effect-postgres';
import { PgClient } from '@effect/sql-pg';
import * as Effect from 'effect/Effect';
import * as Redacted from 'effect/Redacted';
import { sql } from 'drizzle-orm';
import { types } from 'pg';

// Configure the PgClient layer with type parsers
const PgClientLive = PgClient.layer({
  url: Redacted.make(process.env.DATABASE_URL!),
  types: {
    getTypeParser: (typeId, format) => {
      // Return raw values for date/time types to let Drizzle handle parsing
      if ([1184, 1114, 1082, 1186, 1231, 1115, 1185, 1187, 1182].includes(typeId)) {
        return (val: any) => val;
      }
      return types.getTypeParser(typeId, format);
    },
  },
});

const program = Effect.gen(function*() {
  // Create the database with default services (no logging, no caching)
  const db = yield* PgDrizzle.makeWithDefaults();

  // Execute queries
  const result = yield* db.execute<{ id: number }>(sql`SELECT 1 as id`);
  console.log(result);
});

// Run the program with the PgClient layer
Effect.runPromise(program.pipe(Effect.provide(PgClientLive)));
```

#### Step 3 - Create a DB Layer for dependency injection[](#step-3---create-a-db-layer-for-dependency-injection)

For larger applications, create a reusable DB layer that can be composed with other services. This follows Effect’s recommended pattern for dependency injection:

```
import * as PgDrizzle from 'drizzle-orm/effect-postgres';
import { PgClient } from '@effect/sql-pg';
import * as Context from 'effect/Context';
import * as Effect from 'effect/Effect';
import * as Layer from 'effect/Layer';
import * as Redacted from 'effect/Redacted';
import { types } from 'pg';
import * as relations from './schema/relations';

// Configure the PgClient layer
const PgClientLive = PgClient.layer({
  url: Redacted.make(process.env.DATABASE_URL!),
  types: {
    getTypeParser: (typeId, format) => {
      if ([1184, 1114, 1082, 1186, 1231, 1115, 1185, 1187, 1182].includes(typeId)) {
        return (val: any) => val;
      }
      return types.getTypeParser(typeId, format);
    },
  },
});

// Create the DB effect with default services
const dbEffect = PgDrizzle.make({ relations }).pipe(
  Effect.provide(PgDrizzle.DefaultServices)
);

// Define a DB service tag for dependency injection
class DB extends Context.Tag('DB')<DB, Effect.Effect.Success<typeof dbEffect>>() {}

// Create a layer that provides the DB service
const DBLive = Layer.effect(
  DB,
  Effect.gen(function*() {
    return yield* dbEffect;
  }),
);

// Compose all layers together
const AppLive = Layer.provideMerge(DBLive, PgClientLive);

// Use the DB service in your application
const program = Effect.gen(function*() {
  const db = yield* DB;
  const users = yield* db.select().from(usersTable);
  return users;
});

// Run with all dependencies provided
Effect.runPromise(program.pipe(Effect.provide(AppLive)));
```

#### Advanced: Custom logger and cache configuration[](#advanced-custom-logger-and-cache-configuration)

For more control over logging and caching, use `PgDrizzle.make()` directly and provide your own service implementations.

##### Logger configuration[](#logger-configuration)

By default, `makeWithDefaults()` uses a no-op logger (no logging). You can enable logging by providing a different `EffectLogger` implementation:

```
import * as PgDrizzle from 'drizzle-orm/effect-postgres';
import { EffectLogger } from 'drizzle-orm/effect-postgres';
import * as Effect from 'effect/Effect';

const program = Effect.gen(function*() {
  const db = yield* PgDrizzle.make({ /* schema, relations, casing */ }).pipe(
    // Enable Effect-based logging (uses Effect.log with annotations)
    Effect.provide(EffectLogger.layer),
    // Provide remaining default services (cache)
    Effect.provide(PgDrizzle.DefaultServices),
  );

  const users = yield* db.select().from(usersTable);
  return users;
});
```

**Available logger options:**

*   `EffectLogger.Default` - No-op logger (no logging occurs) - this is the default
*   `EffectLogger.layer` - Logs queries using Effect’s `Effect.log()` with annotations for query SQL and parameters. Integrates with Effect’s logging infrastructure.
*   `EffectLogger.fromDrizzle(logger)` - Wraps a Drizzle `Logger` instance for use with Effect
*   `EffectLogger.layerFromDrizzle(logger)` - Creates an Effect Layer from a Drizzle logger

When using `EffectLogger.layer`, queries are logged via Effect’s logging system. You can configure the output format by providing a different Effect logger layer (e.g., `Logger.pretty` for development, `Logger.json` for production).

**Using a Drizzle logger:**

```
import * as PgDrizzle from 'drizzle-orm/effect-postgres';
import { EffectLogger } from 'drizzle-orm/effect-postgres';
import * as Effect from 'effect/Effect';
import { DefaultLogger } from 'drizzle-orm';

const program = Effect.gen(function*() {
  const db = yield* PgDrizzle.make({ /* schema, relations, casing */ }).pipe(
    // Use a Drizzle logger wrapped for Effect
    Effect.provide(EffectLogger.layerFromDrizzle(new DefaultLogger())),
    // Provide remaining default services (cache)
    Effect.provide(PgDrizzle.DefaultServices),
  );

  const users = yield* db.select().from(usersTable);
  return users;
});
```

##### Cache configuration[](#cache-configuration)

Similarly, you can provide a custom cache implementation:

```
import * as PgDrizzle from 'drizzle-orm/effect-postgres';
import { EffectLogger } from 'drizzle-orm/effect-postgres';
import { EffectCache } from 'drizzle-orm/cache/core/cache-effect';
import * as Effect from 'effect/Effect';
import { MyCustomCache } from './cache';

const program = Effect.gen(function*() {
  const db = yield* PgDrizzle.make({ /* schema, relations, casing */ }).pipe(
    // Provide a custom cache wrapped for Effect
    Effect.provide(EffectCache.layerFromDrizzle(new MyCustomCache())),
    // Provide remaining default services (logger)
    Effect.provide(PgDrizzle.DefaultServices),
  );

  const users = yield* db.select().from(usersTable);
  return users;
});
```

**Available cache options:**

*   `EffectCache.Default` - No-op cache (no caching occurs) - this is the default
*   `EffectCache.fromDrizzle(cache)` - Wraps a Drizzle `Cache` instance for use with Effect
*   `EffectCache.layerFromDrizzle(cache)` - Creates an Effect Layer from a Drizzle cache (useful for composing with other layers)

#### What’s next?[](#whats-next)

