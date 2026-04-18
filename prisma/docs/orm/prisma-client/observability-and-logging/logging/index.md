---
title: "Logging"
source: "https://www.prisma.io/docs/orm/prisma-client/observability-and-logging/logging"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/observability-and-logging/logging"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:08.643Z"
content_hash: "14ef923b7ea0cbf75fde659fe4f349a978d97ef747493f01fcee188d53248547"
menu_path: ["Logging"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/deployment/deploy-prisma/index.md", "title": "Deploy Prisma ORM"}
nav_next: {"path": "prisma/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing/index.md", "title": "OpenTelemetry tracing"}
---

Observability and Logging

Learn how to configure Prisma Client to log the raw SQL queries it sends to the database and other information

Use the `PrismaClient` [`log`](prisma/docs/orm/reference/prisma-client-reference/index.md#log) parameter to configure [log levels](prisma/docs/orm/reference/prisma-client-reference/index.md#log-levels) , including warnings, errors, and information about the queries sent to the database.

Prisma Client supports two types of logging:

*   Logging to [stdout](https://en.wikipedia.org/wiki/Standard_streams) (default)
*   Event-based logging (use [`$on()`](prisma/docs/orm/reference/prisma-client-reference/index.md#on) method to [subscribe to events](#event-based-logging))

The simplest way to print _all_ log levels to stdout is to pass in an array `LogLevel` objects:

```
const prisma = new PrismaClient({
  log: ["query", "info", "warn", "error"],
});
```

This is the short form of passing in an array of `LogDefinition` objects where the value of `emit` is always `stdout`:

```
const prisma = new PrismaClient({
  log: [
    {
      emit: "stdout",
      level: "query",
    },
    {
      emit: "stdout",
      level: "error",
    },
    {
      emit: "stdout",
      level: "info",
    },
    {
      emit: "stdout",
      level: "warn",
    },
  ],
});
```

To use event-based logging:

1.  Set `emit` to `event` for a specific log level, such as query
2.  Use the `$on()` method to subscribe to the event

The following example subscribes to all `query` events and write the `duration` and `query` to console:

```
Query: SELECT "public"."User"."id", "public"."User"."email", "public"."User"."name" FROM "public"."User" WHERE 1=1 OFFSET $1
Params: [0]
Duration: 3ms
Query: SELECT "public"."Post"."id", "public"."Post"."title", "public"."Post"."authorId" FROM "public"."Post" WHERE "public"."Post"."authorId" IN ($1,$2,$3,$4) OFFSET $5
Params: [2, 7, 18, 29]
Duration: 2ms
```

```
Query: db.User.aggregate([ { $project: { _id: 1, email: 1, name: 1, }, }, ])
Query: db.Post.aggregate([ { $match: { userId: { $in: [ "622f0bbbdf635a42016ee325", ], }, }, }, { $project: { _id: 1, slug: 1, title: 1, body: 1, userId: 1, }, }, ])
```

The exact [event (`e`) type and the properties available](prisma/docs/orm/reference/prisma-client-reference/index.md#event-types) depends on the log level.

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/observability-and-logging/logging.mdx)


