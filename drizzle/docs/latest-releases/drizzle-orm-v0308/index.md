---
title: "Drizzle ORM - DrizzleORM v0.30.8 release"
source: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0308"
canonical_url: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0308"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:14:20.694Z"
content_hash: "ff7a929c260ee0c7bcdcb8e93f1f5ff37476fa791c440806fc71daed2e32786e"
menu_path: ["Drizzle ORM - DrizzleORM v0.30.8 release"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0307/index.md", "title": "Drizzle ORM - DrizzleORM v0.30.7 release"}
nav_next: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0309/index.md", "title": "Drizzle ORM - DrizzleORM v0.30.9 release"}
---

DrizzleORM v0.30.8 release

Apr 11, 2024

## New Features

-   Added custom schema support to enums in Postgres (fixes [#669](https://github.com/drizzle-team/drizzle-orm/issues/669) via [#2048](https://github.com/drizzle-team/drizzle-orm/pull/2048)):

```ts
import { pgSchema } from 'drizzle-orm/pg-core';

const mySchema = pgSchema('mySchema');
const colors = mySchema.enum('colors', ['red', 'green', 'blue']);
```

Learn more about Postgres [schemas](drizzle/docs/schemas/index.md) and [enums](drizzle/docs/column-types/pg/index.md#enum).

## Fixes

-   Changed D1 `migrate()` function to use batch API ([#2137](https://github.com/drizzle-team/drizzle-orm/pull/2137))

To get started with Drizzle and D1 follow the [documentation](drizzle/docs/get-started-sqlite/index.md#cloudflare-d1).

-   Split `where` clause in Postgres `.onConflictDoUpdate` method into `setWhere` and `targetWhere` clauses, to support both `where` cases in `on conflict ...` clause (fixes [#1628](https://github.com/drizzle-team/drizzle-orm/issues/1628), [#1302](https://github.com/drizzle-team/drizzle-orm/issues/1302) via [#2056](https://github.com/drizzle-team/drizzle-orm/pull/2056)).

```ts
await db.insert(employees)
  .values({ employeeId: 123, name: 'John Doe' })
  .onConflictDoUpdate({
    target: employees.employeeId,
    targetWhere: sql`name <> 'John Doe'`,
    set: { name: sql`excluded.name` }
  });
  
await db.insert(employees)
  .values({ employeeId: 123, name: 'John Doe' })
  .onConflictDoUpdate({
    target: employees.employeeId,
    set: { name: 'John Doe' },
    setWhere: sql`name <> 'John Doe'`
  });
```

Learn more about `.onConflictDoUpdate` method [here](drizzle/docs/insert/index.md#on-conflict-do-update).

-   Fixed query generation for `where` clause in Postgres `.onConflictDoNothing` method, as it was placed in a wrong spot (fixes [#1628](https://github.com/drizzle-team/drizzle-orm/issues/1628) via [#2056](https://github.com/drizzle-team/drizzle-orm/pull/2056)).

Learn more about `.onConflictDoNothing` method [here](drizzle/docs/insert/index.md#on-conflict-do-nothing).

-   Fixed multiple issues with AWS Data API driver (fixes [#1931](https://github.com/drizzle-team/drizzle-orm/pull/1931), [#1932](https://github.com/drizzle-team/drizzle-orm/issues/1932), [#1934](https://github.com/drizzle-team/drizzle-orm/issues/1934), [#1936](https://github.com/drizzle-team/drizzle-orm/issues/1936) via [#2119](https://github.com/drizzle-team/drizzle-orm/pull/2119))
-   Fix inserting and updating array values in AWS Data API (fixes [#1912](https://github.com/drizzle-team/drizzle-orm/issues/1912) via [#1911](https://github.com/drizzle-team/drizzle-orm/pull/1911))

To get started with Drizzle and AWS Data API follow the [documentation](drizzle/docs/get-started-postgresql/index.md#aws-data-api).
