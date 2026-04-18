---
title: "Customizing migrations"
source: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:37.180Z"
content_hash: "39d5fe6479e64215cf429205f56ac4076c832f4f70b683bdaca3902642624fd5"
menu_path: ["Customizing migrations"]
section_path: []
---
Workflows

How to edit a migration file before applying it to avoid data loss in production.

In some scenarios, you need to edit a migration file before you apply it. For example, to [change the direction of a 1-1 relation](#example-change-the-direction-of-a-1-1-relation) (moving the foreign key from one side to another) without data loss, you need to move data as part of the migration - this SQL is not part of the default migration, and must be written by hand.

This guide explains how to edit migration files and gives some examples of use cases where you may want to do this.

To edit a migration file before applying it, the general procedure is the following:

*   Make a schema change that requires custom SQL (for example, to preserve existing data)
*   Create a draft migration using:

*   Modify the generated SQL file.
*   Apply the modified SQL by running:

### [Example: Rename a field](#example-rename-a-field)

By default, renaming a field in the schema results in a migration that will:

*   `CREATE` a new column (for example, `fullname`)
*   `DROP` the existing column (for example, `name`) and the data in that column

To actually **rename** a field and avoid data loss when you run the migration in production, you need to modify the generated migration SQL before applying it to the database. Consider the following schema fragment - the `biograpy` field is spelled wrong.

```
model Profile {
  id       Int    @id @default(autoincrement())
  biograpy String
  userId   Int    @unique
  user     User   @relation(fields: [userId], references: [id])
}
```

To rename the `biograpy` field to `biography`:

Rename the field in the schema:

```
model Profile {
  id        Int    @id @default(autoincrement())
  biograpy  String
  biography String
  userId    Int    @unique
  user      User   @relation(fields: [userId], references: [id])
}
```

*   Run the following command to create a **draft migration** that you can edit before applying to the database:

*   Edit the draft migration as shown, changing `DROP` / `DELETE` to a single `RENAME COLUMN`:

*   Save and apply the migration:

You can use the same technique to rename a `model` - edit the generated SQL to _rename_ the table rather than drop and re-create it.

### [Example: Use the expand and contract pattern to evolve the schema without downtime](#example-use-the-expand-and-contract-pattern-to-evolve-the-schema-without-downtime)

Making schema changes to existing fields, e.g., renaming a field can lead to downtime. It happens in the time frame between applying a migration that modifies an existing field, and deploying a new version of the application code which uses the modified field.

You can prevent downtime by breaking down the steps required to alter a field into a series of discrete steps designed to introduce the change gradually. This pattern is known as the _expand and contract pattern_.

The pattern involves two components: your application code accessing the database and the database schema you intend to alter.

With the _expand and contract_ pattern, renaming the field `bio` to `biography` would look as follows with Prisma:

*   Add the new `biography` field to your Prisma schema and create a migration

```
model Profile {
 id        Int    @id @default(autoincrement())
 bio       String
 biography String
 userId    Int    @unique
 user      User   @relation(fields: [userId], references: [id])
}
```

*   _Expand_: update the application code and write to both the `bio` and `biography` fields, but continue reading from the `bio` field, and deploy the code
*   Create an empty migration and copy existing data from the `bio` to the `biography` field

```
UPDATE "Profile" SET biography = bio;
```

4.  Verify the integrity of the `biography` field in the database
5.  Update application code to **read** from the new `biography` field
6.  Update application code to **stop writing** to the `bio` field
7.  _Contract_: remove the `bio` from the Prisma schema, and create a migration to remove the `bio` field

```
model Profile {
 id        Int    @id @default(autoincrement())
 bio       String
 biography String
 userId    Int    @unique
 user      User   @relation(fields: [userId], references: [id])
}
```

By using this approach, you avoid potential downtime that altering existing fields that are used in the application code are prone to, and reduce the amount of coordination required between applying the migration and deploying the updated application code.

Note that this pattern is applicable in any situation involving a change to a column that has data and is in use by the application code. Examples include combining two fields into one, or transforming a `1:n` relation to a `m:n` relation.

To learn more, check out the Data Guide article on [the expand and contract pattern](https://www.prisma.io/dataguide/types/relational/expand-and-contract-pattern)

### [Example: Change the direction of a 1-1 relation](#example-change-the-direction-of-a-1-1-relation)

To change the direction of a 1-1 relation:

*   Make the change in the schema:

```
model User {
 id        Int      @id @default(autoincrement())
 name      String
 posts     Post[]
 profile   Profile? @relation(fields: [profileId], references: [id])
 profileId Int      @unique
}

model Profile {
 id        Int    @id @default(autoincrement())
 biography String
 user      User
}
```

*   Run the following command to create a **draft migration** that you can edit before applying to the database:

```
⚠️  There will be data loss when applying the migration:

• The migration will add a unique constraint covering the columns `[profileId]` on the table `User`. If there are existing duplicate values, the migration will fail.
```

*   Edit the draft migration as shown:

*   Save and apply the migration:

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-migrate/workflows/customizing-migrations.mdx)
