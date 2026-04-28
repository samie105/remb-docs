---
title: "TypedSQL"
source: "https://www.prisma.io/docs/orm/prisma-client/using-raw-sql/typedsql"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/using-raw-sql/typedsql"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:40:44.625Z"
content_hash: "d5c2e45cdbbf4ad8274b1e9cb007351b003cedb6fb029b57cc9328bcdf50bcc3"
menu_path: ["TypedSQL"]
section_path: []
tab_variants: ["npm","pnpm","yarn","bun","PostgreSQL","MySQL","SQLite"]
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-client/using-raw-sql/safeql/index.md", "title": "SafeQL & Prisma Client"}
nav_next: {"path": "prisma/docs/orm/prisma-migrate/workflows/baselining/index.md", "title": "Baselining a database"}
---

Learn how to use TypedSQL to write fully type-safe SQL queries that are compatible with any SQL console and Prisma Client

To start using TypedSQL in your Prisma project, follow these steps:

1.  Ensure you have `@prisma/client` and `prisma` installed:
    
2.  Add the `typedSql` preview feature flag to your `schema.prisma` file:
    
    ```
    generator client {
     provider = "prisma-client"
     previewFeatures = ["typedSql"]
     output = "../src/generated/prisma"
    }
    ```
    
3.  Create a `sql` directory inside your `prisma` directory. This is where you'll write your SQL queries.
    
    ```
    mkdir -p prisma/sql
    ```
    
4.  Create a new `.sql` file in your `prisma/sql` directory. For example, `getUsersWithPosts.sql`. Note that the file name must be a valid JS identifier and cannot start with a `$`.
    
5.  Write your SQL queries in your new `.sql` file. For example:
    
    prisma/sql/getUsersWithPosts.sql
    
    ```
    SELECT u.id, u.name, COUNT(p.id) as "postCount"
    FROM "User" u
    LEFT JOIN "Post" p ON u.id = p."authorId"
    GROUP BY u.id, u.name
    ```
    
6.  Generate Prisma Client with the `sql` flag to ensure TypeScript functions and types for your SQL queries are created:
    
    ```
    prisma generate --sql
    ```
    
    If you don't want to regenerate the client after every change, this command also works with the existing `--watch` flag:
    
    ```
    prisma generate --sql --watch
    ```
    
7.  Now you can import and use your SQL queries in your TypeScript code:
    

/src/index.ts

```
import { PrismaClient } from "./generated/prisma/client";
import { getUsersWithPosts } from "./generated/prisma/sql";

const prisma = new PrismaClient();

const usersWithPostCounts = await prisma.$queryRawTyped(getUsersWithPosts());
console.log(usersWithPostCounts);
```

To pass arguments to your TypedSQL queries, you can use parameterized queries. This allows you to write flexible and reusable SQL statements while maintaining type safety. Here's how to do it:

1.  In your SQL file, use placeholders for the parameters you want to pass. The syntax for placeholders depends on your database engine:

For PostgreSQL, use the positional placeholders `$1`, `$2`, etc. For MySQL, use `?`. In SQLite, you can use positional (`$1`, `$2`), general (`?`), or named placeholders (`:minAge`, `:maxAge`):

1.  When using the generated function in your TypeScript code, pass the arguments as additional parameters to `$queryRawTyped`:

/src/index.ts

```
import { PrismaClient } from "./generated/prisma/client";
import { getUsersByAge } from "./generated/prisma/sql";

const prisma = new PrismaClient();

const minAge = 18;
const maxAge = 30;
const users = await prisma.$queryRawTyped(getUsersByAge(minAge, maxAge));
console.log(users);
```

By using parameterized queries, you ensure type safety and protect against SQL injection vulnerabilities. The TypedSQL generator will create the appropriate TypeScript types for the parameters based on your SQL query, providing full type checking for both the query results and the input parameters.

### [Passing array arguments to TypedSQL](#passing-array-arguments-to-typedsql)

TypedSQL supports passing arrays as arguments for PostgreSQL. Use PostgreSQL's `ANY` operator with an array parameter.

prisma/sql/getUsersByIds.sql

```
SELECT id, name, email
FROM users
WHERE id = ANY($1)
```

/src/index.ts

```
import { PrismaClient } from "./generated/prisma/client";
import { getUsersByIds } from "./generated/prisma/sql";

const prisma = new PrismaClient();

const userIds = [1, 2, 3];
const users = await prisma.$queryRawTyped(getUsersByIds(userIds));
console.log(users);
```

TypedSQL will generate the appropriate TypeScript types for the array parameter, ensuring type safety for both the input and the query results.

### [Defining argument types in your SQL files](#defining-argument-types-in-your-sql-files)

Argument typing in TypedSQL is accomplished via specific comments in your SQL files. These comments are of the form:

```
-- @param {Type} $N:alias optional description
```

Where `Type` is a valid database type, `N` is the position of the argument in the query, and `alias` is an optional alias for the argument that is used in the TypeScript type.

As an example, if you needed to type a single string argument with the alias `name` and the description "The name of the user", you would add the following comment to your SQL file:

```
-- @param {String} $1:name The name of the user
```

To indicate that a parameter is nullable, add a question mark after the alias:

```
-- @param {String} $1:name? The name of the user (optional)
```

Currently accepted types are `Int`, `BigInt`, `Float`, `Boolean`, `String`, `DateTime`, `Json`, `Bytes`, `null`, and `Decimal`.

Taking the [example from above](#passing-arguments-to-typedsql-queries), the SQL file would look like this:

```
-- @param {Int} $1:minAge
-- @param {Int} $2:maxAge
SELECT id, name, age
FROM users
WHERE age > $1 AND age < $2
```

The format of argument type definitions is the same regardless of the database engine.

For practical examples of how to use TypedSQL, please refer to the [TypedSQL example in the Prisma Examples repo](https://github.com/prisma/prisma-examples/tree/latest/generator-prisma-client/basic-typedsql).

### [Supported Databases](#supported-databases)

TypedSQL supports modern versions of MySQL and PostgreSQL without any further configuration. For MySQL versions older than 8.0 and all SQLite versions, you will need to manually [describe argument types](#defining-argument-types-in-your-sql-files) in your SQL files. The types of inputs are inferred in all supported versions of PostgreSQL and MySQL 8.0 and later.

TypedSQL does not work with MongoDB, as it is specifically designed for SQL databases.

### [Active Database Connection Required](#active-database-connection-required)

TypedSQL requires an active database connection to function properly. This means you need to have a running database instance that Prisma can connect to when generating the client with the `--sql` flag. TypedSQL uses the connection string defined in `prisma.config.ts` (`datasource.url`) to establish this connection.

### [Dynamic SQL Queries with Dynamic Columns](#dynamic-sql-queries-with-dynamic-columns)

TypedSQL does not natively support constructing SQL queries with dynamically added columns. When you need to create a query where the columns are determined at runtime, you must use the `$queryRaw` and `$executeRaw` methods. These methods allow for the execution of raw SQL, which can include dynamic column selections.

**Example of a query using dynamic column selection:**

```
const columns = "name, email, age"; // Columns determined at runtime
const result = await prisma.$queryRawUnsafe(`SELECT ${columns} FROM Users WHERE active = true`);
```

In this example, the columns to be selected are defined dynamically and included in the SQL query. While this approach provides flexibility, it requires careful attention to security, particularly to [avoid SQL injection vulnerabilities](prisma/docs/orm/prisma-client/using-raw-sql/raw-queries/index.md#sql-injection-prevention). Additionally, using raw SQL queries means foregoing the type-safety and DX of TypedSQL.

This feature was heavily inspired by [PgTyped](https://github.com/adelsz/pgtyped) and [SQLx](https://github.com/launchbadge/sqlx). Additionally, SQLite parsing is handled by SQLx.
