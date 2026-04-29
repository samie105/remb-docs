---
title: "Write your own SQL"
source: "https://www.prisma.io/docs/orm/prisma-client/using-raw-sql"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/using-raw-sql"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:40:24.843Z"
content_hash: "a7fa99db2e9e00bf5de1d2ebaad9adeecc81822c719dec0bf9384fadc869b9c9"
menu_path: ["Write your own SQL"]
section_path: []
content_language: "en"
nav_prev: {"path": "../type-safety/prisma-type-system/index.md", "title": "How to use Prisma ORM's type system"}
nav_next: {"path": "raw-queries/index.md", "title": "Raw queries"}
---

Using Raw SQL

Learn how to use raw SQL queries in Prisma Client

While the Prisma Client API aims to make all your database queries intuitive, type-safe, and convenient, there may still be situations where raw SQL is the best tool for the job.

This can happen for various reasons, such as the need to optimize the performance of a specific query or because your data requirements can't be fully expressed by Prisma Client's query API.

In most cases, [TypedSQL](#writing-type-safe-queries-with-prisma-client-and-typedsql) allows you to express your query in SQL while still benefiting from Prisma Client's excellent user experience. However, since TypedSQL is statically typed, it may not handle certain scenarios, such as dynamically generated `WHERE` clauses. In these cases, you will need to use [`$queryRaw`](raw-queries/index.md#queryraw) or [`$executeRaw`](raw-queries/index.md#executeraw), or their unsafe counterparts.

### [What is TypedSQL?](#what-is-typedsql)

TypedSQL is a new feature of Prisma ORM that allows you to write your queries in `.sql` files while still enjoying the great developer experience of Prisma Client. You can write the code you're comfortable with and benefit from fully-typed inputs and outputs.

With TypedSQL, you can:

1.  Write complex SQL queries using familiar syntax
2.  Benefit from full IDE support and syntax highlighting for SQL
3.  Import your SQL queries as fully typed functions in your TypeScript code
4.  Maintain the flexibility of raw SQL with the safety of Prisma's type system

TypedSQL is particularly useful for:

-   Complex reporting queries that are difficult to express using Prisma's query API
-   Performance-critical operations that require fine-tuned SQL
-   Leveraging database-specific features not yet supported in Prisma's API

By using TypedSQL, you can write efficient, type-safe database queries without sacrificing the power and flexibility of raw SQL. This feature allows you to seamlessly integrate custom SQL queries into your Prisma-powered applications, ensuring type safety and improving developer productivity.

For a detailed guide on how to get started with TypedSQL, including setup instructions and usage examples, please refer to our [TypedSQL documentation](typedsql/index.md).

While not as ergonomic as [TypedSQL](#writing-type-safe-queries-with-prisma-client-and-typedsql), raw queries are still supported and useful when TypedSQL queries are not possible due to features not yet supported in TypedSQL or when the query is dynamically generated.

### [Alternative approaches to raw SQL queries in relational databases](#alternative-approaches-to-raw-sql-queries-in-relational-databases)

Prisma ORM supports four methods to execute raw SQL queries in relational databases:

-   [`$queryRaw`](raw-queries/index.md#queryraw)
-   [`$executeRaw`](raw-queries/index.md#executeraw)
-   [`$queryRawUnsafe`](raw-queries/index.md#queryrawunsafe)
-   [`$executeRawUnsafe`](raw-queries/index.md#executerawunsafe)

These commands are similar to using TypedSQL, but they are not type-safe and are written as strings in your code rather than in dedicated `.sql` files.

### [Alternative approaches to raw queries in document databases](#alternative-approaches-to-raw-queries-in-document-databases)

For MongoDB, Prisma ORM supports three methods to execute raw queries:

-   [`$runCommandRaw`](raw-queries/index.md#runcommandraw)
-   [`<model>.findRaw`](raw-queries/index.md#findraw)
-   [`<model>.aggregateRaw`](raw-queries/index.md#aggregateraw)

These methods allow you to execute raw MongoDB commands and queries, providing flexibility when you need to use MongoDB-specific features or optimizations.

`$runCommandRaw` is used to execute database commands, `<model>.findRaw` is used to find documents that match a filter, and `<model>.aggregateRaw` is used for aggregation operations.

Similar to raw queries in relational databases, these methods are not type-safe and require manual handling of the query results.
