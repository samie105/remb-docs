---
title: "Drizzle ORM - DrizzleORM v0.30.8 release"
source: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0308"
canonical_url: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0308"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:14:37.726Z"
content_hash: "0e5a9896aa87fd20c1140310d59a15d447d0a4a89871817c02a8325a7dea0041"
menu_path: ["Drizzle ORM - DrizzleORM v0.30.8 release"]
section_path: []
---
DrizzleORM v0.30.8 release

Apr 11, 2024

## New Features

*   Added custom schema support to enums in Postgres (fixes [#669](https://github.com/drizzle-team/drizzle-orm/issues/669) via [#2048](https://github.com/drizzle-team/drizzle-orm/pull/2048)):

```
import { pgSchema } from 'drizzle-orm/pg-core';

const mySchema = pgSchema('mySchema');
const colors = mySchema.enum('colors', ['red', 'green', 'blue']);
```

Learn more about Postgres [schemas](https://orm.drizzle.team/docs/schemas) and [enums](https://orm.drizzle.team/docs/column-types/pg#enum).

## Fixes

*   Changed D1 `migrate()` function to use batch API ([#2137](https://github.com/drizzle-team/drizzle-orm/pull/2137))

To get started with Drizzle and D1 follow the [documentation](https://orm.drizzle.team/docs/get-started-sqlite#cloudflare-d1).

*   Split `where` clause in Postgres `.onConflictDoUpdate` method into `setWhere` and `targetWhere` clauses, to support both `where` cases in `on conflict ...` clause (fixes [#1628](https://github.com/drizzle-team/drizzle-orm/issues/1628), [#1302](https://github.com/drizzle-team/drizzle-orm/issues/1302) via [#2056](https://github.com/drizzle-team/drizzle-orm/pull/2056)).

```
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

Learn more about `.onConflictDoUpdate` method [here](https://orm.drizzle.team/docs/insert#on-conflict-do-update).

*   Fixed query generation for `where` clause in Postgres `.onConflictDoNothing` method, as it was placed in a wrong spot (fixes [#1628](https://github.com/drizzle-team/drizzle-orm/issues/1628) via [#2056](https://github.com/drizzle-team/drizzle-orm/pull/2056)).

Learn more about `.onConflictDoNothing` method [here](https://orm.drizzle.team/docs/insert#on-conflict-do-nothing).

*   Fixed multiple issues with AWS Data API driver (fixes [#1931](https://github.com/drizzle-team/drizzle-orm/pull/1931), [#1932](https://github.com/drizzle-team/drizzle-orm/issues/1932), [#1934](https://github.com/drizzle-team/drizzle-orm/issues/1934), [#1936](https://github.com/drizzle-team/drizzle-orm/issues/1936) via [#2119](https://github.com/drizzle-team/drizzle-orm/pull/2119))
*   Fix inserting and updating array values in AWS Data API (fixes [#1912](https://github.com/drizzle-team/drizzle-orm/issues/1912) via [#1911](https://github.com/drizzle-team/drizzle-orm/pull/1911))

To get started with Drizzle and AWS Data API follow the [documentation](https://orm.drizzle.team/docs/get-started-postgresql#aws-data-api).
