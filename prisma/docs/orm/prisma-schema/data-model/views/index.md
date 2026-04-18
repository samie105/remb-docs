---
title: "Views"
source: "https://www.prisma.io/docs/orm/prisma-schema/data-model/views"
canonical_url: "https://www.prisma.io/docs/orm/prisma-schema/data-model/views"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:36.766Z"
content_hash: "d12384f18505fbeacaa81312d51263009e66b8fad14be31cb3ab286406aba538"
menu_path: ["Views"]
section_path: []
---
Database views allow you to name and store queries. In relational databases, views are [stored SQL queries](https://www.postgresql.org/docs/current/sql-createview.html) that might include columns in multiple tables, or calculated values such as aggregates. In MongoDB, views are queryable objects where the contents are defined by an [aggregation pipeline](https://www.mongodb.com/docs/manual/core/aggregation-pipeline) on other collections.

The `views` preview feature allows you to represent views in your Prisma schema with the `view` keyword. To use views in Prisma ORM, follow these steps:

1.  [Enable the `views` preview feature](#enable-the-views-preview-feature)
2.  [Create a view in the underlying database](#create-a-view-in-the-underlying-database), either directly or as a [manual addition to a Prisma Migrate migration file](#use-views-with-prisma-migrate-and-db-push), or use an existing view
3.  [Represent the view in your Prisma schema](#add-views-to-your-prisma-schema)
4.  [Query the view in Prisma Client](#query-views-in-prisma-client)

Support for views is currently in an early preview. To enable the `views` preview feature, add the `views` feature flag to the `previewFeatures` field of the `generator` block in your Prisma Schema:

```
generator client {
  provider        = "prisma-client"
  output          = "./generated"
  previewFeatures = ["views"] 
}
```

Please leave feedback about this preview feature in our dedicated preview feature [feedback issue](https://github.com/prisma/prisma/issues/17335) for `views`.

Currently, you cannot apply views that you define in your Prisma schema to your database with Prisma Migrate or `db push`. Instead, you must first create the view in the underlying database, either manually or [as part of a migration](#use-views-with-prisma-migrate-and-db-push).

For example, take the following Prisma schema with a `User` model and a related `Profile` model:

Next, take a `UserInfo` view in the underlying database that combines the `email` and `name` fields from the `User` model and the `bio` field from the `Profile` model.

For a relational database, the SQL statement to create this view is:

```
CREATE VIEW "UserInfo" AS
    SELECT u.id, email, name, bio
    FROM "User" u
    LEFT JOIN "Profile" p ON u.id = p."userId";
```

For MongoDB, you can [create a view](https://www.mongodb.com/docs/manual/core/views/join-collections-with-view/) with the following command:

```
db.createView("UserInfo", "User", [
  {
    $lookup: {
      from: "Profile",
      localField: "_id",
      foreignField: "userId",
      as: "ProfileData",
    },
  },
  {
    $project: {
      _id: 1,
      email: 1,
      name: 1,
      bio: "$ProfileData.bio",
    },
  },
  { $unwind: "$bio" },
]);
```

If you apply changes to your Prisma schema with Prisma Migrate or `db push`, Prisma ORM does not create or run any SQL related to views.

To include views in a migration, run `migrate dev --create-only` and then manually add the SQL for views to your migration file. Alternatively, you can create views manually in the database.

To add a view to your Prisma schema, use the `view` keyword.

You can represent the `UserInfo` view from the example above in your Prisma schema as follows:

### [Write by hand](#write-by-hand)

A `view` block is comprised of two main pieces:

*   The `view` block definition
*   The view's field definitions

These two pieces allow you to define the name of your view in the generated Prisma Client and the columns present in your view's query results.

#### [Define a `view` block](#define-a-view-block)

To define the `UserInfo` view from the example above, begin by using the `view` keyword to define a `view` block in your schema named `UserInfo`:

```
view UserInfo {
  // Fields
}
```

#### [Define fields](#define-fields)

The properties of a view are called _fields_, which consist of:

*   A field name
*   A field type

The fields of the `UserInfo` example view can be defined as follows:

Each _field_ of a `view` block represents a column in the query results of the view in the underlying database.

### [Use introspection](#use-introspection)

If you have an existing view or views defined in your database, [introspection](https://www.prisma.io/docs/orm/prisma-schema/introspection) will automatically generate `view` blocks in your Prisma schema that represent those views.

Assuming the example `UserInfo` view exists in your underlying database, running the following command will generate a `view` block in your Prisma schema representing that view:

The resulting `view` block will be defined as follows:

```
view UserInfo {
  id    Int?
  email String?
  name  String?
  bio   String?
}
```

#### [The `views` directory](#the-views-directory)

Introspection of a database with one or more existing views will also create a new `views` directory within your `prisma` directory. This directory will contain a subdirectory named after your database's schema which contains a `.sql` file for each view that was introspected in that schema. Each file will be named after an individual view and will contain the query the related view defines.

For example, after introspecting a database with the default `public` schema using the model used above you will find a `prisma/views/public/UserInfo.sql` file was created with the following contents:

```
SELECT
  u.id,
  u.email,
  u.name,
  p.bio
FROM
  (
    "User" u
    LEFT JOIN "Profile" p ON ((u.id = p."userId"))
  );
```

You can query views in Prisma Client in the same way that you query models. For example, the following query finds all users with a `name` of `'Alice'` in the `UserInfo` view defined above.

```
const userinfo = await prisma.userInfo.findMany({
  where: {
    name: "Alice",
  },
});
```

This section describes how to use Prisma ORM with updatable and materialized views in your database.

### [Updatable views](#updatable-views)

Some databases support _updatable views_ (e.g. [PostgreSQL](https://www.postgresql.org/docs/current/sql-createview.html#SQL-CREATEVIEW-UPDATABLE-VIEWS), [MySQL](https://dev.mysql.com/doc/refman/8.0/en/view-updatability.html), and [SQL Server](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-view-transact-sql?view=sql-server-ver16#updatable-views)). Updatable views allow creating, updating, or deleting entries if the underlying database supports such operations.

Prisma ORM does not allow any mutations (create, update, delete) on views, regardless of the database's capabilities. This change provides guardrails to ensure that views are treated consistently as read-only entities within Prisma Client. As a result, methods to perform writes such as `create`, `update`, `delete`, or `upsert` are not generated for `view` blocks in your Prisma Client API.

If you need to modify data represented by a view, you must perform the write operations directly on the underlying tables or use raw SQL queries.

### [Materialized views](#materialized-views)

Some databases support materialized views, e.g. [PostgreSQL](https://www.postgresql.org/docs/current/rules-materializedviews.html), [CockroachDB](https://www.cockroachlabs.com/docs/stable/views.html#materialized-views), [MongoDB](https://www.mongodb.com/docs/manual/core/materialized-views/), and [SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/views/create-indexed-views?view=sql-server-ver16) (where they're called "indexed views").

Materialized views persist the result of the view query for faster access and only update it on demand.

Currently, Prisma ORM does not support materialized views. However, when you [manually create a view](#create-a-view-in-the-underlying-database), you can also create a materialized view with the corresponding command in the underlying database. You can then use Prisma Client's [TypedSQL functionality](https://www.prisma.io/docs/orm/prisma-client/using-raw-sql) to execute the command and refresh the view manually.

In the future Prisma Client might support marking individual views as materialized and add a Prisma Client method to refresh the materialized view. Please comment on our [`views` feedback issue](https://github.com/prisma/prisma/issues/17335) with your use case.

Prisma ORM treats all `view` blocks as _read-only_ representations of database queries rather than true tables. Because of this, several limitations apply to ensure Prisma Client remains consistent with the behavior of the underlying database.

### [No identifiers](#no-identifiers)

Views are virtual tables and do not have inherent primary keys. Hence, you cannot define `@id`, `@@id` attributes on a `view` block.

### [No indexes](#no-indexes)

Because views are virtual tables, they cannot have indexes. Therefore, `@index` and `@@index` cannot be defined on `view` blocks.

### [Unsafe `@unique` attributes](#unsafe-unique-attributes)

While Prisma ORM lets you place `@unique` and `@@unique` attributes on views, the underlying database and Prisma do not enforce those constraints. Multiple rows can therefore share the same value for a supposedly unique field.

Neither the database nor Prisma ORM enforce the unique constraint expressed by that attribute.

The purpose of the `@unique` attribute in this case is only to enable relationships across views as well as `findUnique` queries and cursor-based pagination in Prisma Client.

### [Disabled write queries](#disabled-write-queries)

All write operations (`create`, `update`, `delete`, `upsert`) are disabled and not generated in the Prisma Client.
