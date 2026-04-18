---
title: "Connection URLs"
source: "https://www.prisma.io/docs/orm/reference/connection-urls"
canonical_url: "https://www.prisma.io/docs/orm/reference/connection-urls"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:21.127Z"
content_hash: "160454ed59b21e7ea34817d0bf55c18182700a6d5314048ebbc31460ecf6b0e7"
menu_path: ["Connection URLs"]
section_path: []
---
Learn about the format and syntax Prisma ORM uses for defining database connection URLs for PostgreSQL, MySQL and SQLite

Prisma ORM needs a connection URL to be able to connect to your database, e.g. when sending queries with [Prisma Client](https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction) or when changing the database schema with [Prisma Migrate](https://www.prisma.io/docs/orm/prisma-migrate).

The connection URL is provided via the `url` field of a `datasource` block in your Prisma config (or Prisma schema if on version 6). It usually consists of the following components (except for SQLite and [Prisma Postgres](https://www.prisma.io/docs/postgres)):

*   **User**: The name of your database user
*   **Password**: The password for your database user
*   **Host**: The IP or domain name of the machine where your database server is running
*   **Port**: The port on which your database server is running
*   **Database name**: The name of the database you want to use

Make sure you have this information at hand when getting started with Prisma ORM. If you don't have a database server running yet, you can either use a local SQLite database file (see the [Quickstart](https://www.prisma.io/docs/prisma-orm/quickstart/sqlite)) or [setup a free PostgreSQL database with Prisma Postgres](https://www.prisma.io/docs/postgres).

The format of the connection URL depends on the _database connector_ you're using. Prisma ORM generally supports the standard formats for each database. You can find out more about the connection URL of your database on the dedicated docs page:

*   [PostgreSQL](https://www.prisma.io/docs/orm/core-concepts/supported-databases/postgresql)
*   [MySQL](https://www.prisma.io/docs/orm/core-concepts/supported-databases/mysql)
*   [SQLite](https://www.prisma.io/docs/orm/core-concepts/supported-databases/sqlite)
*   [MongoDB](https://www.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)
*   [Microsoft SQL Server](https://www.prisma.io/docs/orm/core-concepts/supported-databases/sql-server)
*   [CockroachDB](https://www.prisma.io/docs/orm/core-concepts/supported-databases/postgresql#cockroachdb)

### [Special characters](#special-characters)

For MySQL, PostgreSQL and CockroachDB you must [percentage-encode special characters](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding) in any part of your connection URL - including passwords. For example, `p@$$w0rd` becomes `p%40%24%24w0rd`.

For Microsoft SQL Server, you must [escape special characters](https://www.prisma.io/docs/orm/core-concepts/supported-databases/sql-server#connection-details) in any part of your connection string.

Here are examples for the connection URLs of the databases Prisma ORM supports:

### [Prisma Postgres](#prisma-postgres)

[Prisma Postgres](https://www.prisma.io/docs/postgres) is a managed PostgreSQL service running on unikernels. There are several ways to connect to Prisma Postgres:

*   via direct TCP connections (lets you connect via any ORM or database tool)
*   via pooled TCP connections (recommended for serverless and high-concurrency workloads)
*   via [Prisma Accelerate](https://www.prisma.io/docs/accelerate) (only supported with Prisma ORM)
*   locally

The connection string formats of these are covered below.

#### [Direct TCP](#direct-tcp)

When you connect to Prisma Postgres via direct TCP, your connection string looks as follows:

```
DATABASE_URL="postgres://USER:PASSWORD@db.prisma.io:5432/?sslmode=require"
```

The `USER` and `PASSWORD` values are provided when you generate credentials for your Prisma Postgres instance in the [Prisma Console](https://console.prisma.io/?utm_source=docs&utm_medium=content&utm_content=orm). Here is an example with sample values:

```
DATABASE_URL="postgres://2f9881cc7eef46f094ac913df34c1fb441502fe66cbe28cc48998d4e6b20336b:sk_QZ3u8fMPFfBzOID4ol-mV@db.prisma.io:5432/?sslmode=require"
```

#### [Pooled TCP](#pooled-tcp)

When you connect to Prisma Postgres via pooled TCP, your connection string looks as follows:

```
DATABASE_URL="postgres://USER:PASSWORD@pooled.db.prisma.io:5432/?sslmode=require"
```

Use a pooled TCP connection string for serverless, bursty, or high-concurrency workloads. Learn more in [Connection pooling](https://www.prisma.io/docs/postgres/database/connection-pooling).

#### [Via Prisma Accelerate (HTTP)](#via-prisma-accelerate-http)

When connecting via Prisma Accelerate, the connection string doesn't require a user/password like a conventional connection string does. Instead, authentication works via an API key:

```
export default defineConfig({
  datasource: {
    url: "prisma+postgres://accelerate.prisma-data.net/?api_key=API_KEY"
  },
});
```

In this snippet, `API_KEY` is a placeholder for the API key you are receiving when setting up a new Prismas Postgres instance via the [Prisma Console](https://console.prisma.io/?utm_source=docs&utm_medium=content&utm_content=orm). Here is an example for what a real connection URL to Prisma Postgres may look like:

```
export default defineConfig({
  datasource: {
    url: "prisma+postgres://accelerate.prisma-data.net/?api_key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGlfa2V5IjoiMGNkZTFlMjQtNzhiYi00NTY4LTkyM2EtNWUwOTEzZWUyNjU1IiwidGVuYW50X2lkIjoiNzEyZWRlZTc1Y2U2MDk2ZjI4NDg3YjE4NWMyYzA2OTNhNGMxNzJkMjhhOWFlNGUwZTYxNWE4NWIxZWY1YjBkMCIsImludGVybmFsX3NlY3JldCI6IjA4MzQ2Y2RlLWI5ZjktNDQ4Yy04NThmLTMxNjg4ODEzNmEzZCJ9.N1Za6q6NfInzHvRkud6Ojt_-RFg18a0601vdYWGKOrk"
  },
});
```

#### [Local Prisma Postgres](#local-prisma-postgres)

The connection string for connecting to a [local Prisma Postgres](https://www.prisma.io/docs/postgres/database/local-development) instance mirrors the structure of a remote instance via Accelerate:

```
export default defineConfig({
  datasource: {
    url: "prisma+postgres://accelerate.prisma-data.net/?api_key=API_KEY"
  },
});
```

However, in this case the `API_KEY` doesn't provide authentication details. Instead, it encodes information about the local Prisma Postgres instance. You can obtain a local connection string via the [`prisma dev`](https://www.prisma.io/docs/orm/reference/prisma-cli-reference#dev) command.

### [PostgreSQL](#postgresql)

```
export default defineConfig({
  datasource: {
    url: "postgresql://janedoe:mypassword@localhost:5432/mydb?schema=sample"
  },
});
```

### [MySQL](#mysql)

```
export default defineConfig({
  datasource: {
    url: "mysql://janedoe:mypassword@localhost:3306/mydb"
  },
});
```

### [Microsoft SQL Server](#microsoft-sql-server)

```
export default defineConfig({
  datasource: {
    url: "sqlserver://localhost:1433;initial catalog=sample;user=sa;password=mypassword;"
  },
});
```

### [SQLite](#sqlite)

```
export default defineConfig({
  datasource: {
    url: "file:./dev.db"
  },
});
```

### [CockroachDB](#cockroachdb)

```
export default defineConfig({
  datasource: {
    url: "postgresql://janedoe:mypassword@localhost:26257/mydb?schema=public"
  },
});
```

### [MongoDB](#mongodb)

_Support for MongoDB is limited to [Prisma 6](https://www.prisma.io/docs/v6/orm/reference/connection-urls#mongodb) as of now. We're working on support for MongoDB in Prisma v7_

You can also provide the connection URL as an environment variable:

```
datasource db {
  provider = "postgresql"
}
```

You can then either set the environment variable in your terminal or by providing a [dotenv](https://github.com/motdotla/dotenv) file named `.env`. This will automatically be picked up by the Prisma CLI.

Prisma ORM reads the connection URL from the dotenv file in the following situations:

*   When it updates the schema during build time
*   When it connects to the database during run time

```
DATABASE_URL=postgresql://janedoe:mypassword@localhost:5432/mydb
```

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/reference/connection-urls.mdx)
