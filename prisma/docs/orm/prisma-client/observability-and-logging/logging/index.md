---
title: "Logging"
source: "https://www.prisma.io/docs/orm/prisma-client/observability-and-logging/logging"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/observability-and-logging/logging"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:38:41.031Z"
content_hash: "6678736b376f9291b19229b6287559e7b1a132b19a12728d18dcd4032bdc7ac3"
menu_path: ["Logging"]
section_path: []
content_language: "en"
nav_prev: {"path": "../../deployment/traditional/deploy-to-sevalla/index.md", "title": "Deploy to Sevalla"}
nav_next: {"path": "../opentelemetry-tracing/index.md", "title": "OpenTelemetry tracing"}
---

Observability and Logging

Learn how to configure Prisma Client to log the raw SQL queries it sends to the database and other information

Use the `PrismaClient` [`log`](../../../reference/prisma-client-reference/index.md#log) parameter to configure [log levels](../../../reference/prisma-client-reference/index.md#log-levels) , including warnings, errors, and information about the queries sent to the database.

Prisma Client supports two types of logging:

-   Logging to [stdout](https://en.wikipedia.org/wiki/Standard_streams) (default)
-   Event-based logging (use [`$on()`](../../../reference/prisma-client-reference/index.md#on) method to [subscribe to events](#event-based-logging))

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

The exact [event (`e`) type and the properties available](../../../reference/prisma-client-reference/index.md#event-types) depends on the log level.
