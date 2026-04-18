---
title: "Prototyping your schema"
source: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:11.153Z"
content_hash: "ffa2d6126f13c791e406552def3d7de5a6dcec560fed6c0b0ebfc4d4a206c708"
menu_path: ["Prototyping your schema"]
section_path: []
---
Workflows

Rapidly prototype your Prisma schema using db push without migrations

The Prisma CLI has a dedicated command for prototyping schemas: [`db push`](https://www.prisma.io/docs/orm/reference/prisma-cli-reference#db-push)

`db push` uses the same engine as Prisma Migrate to synchronize your Prisma schema with your database schema. The `db push` command:

*   Introspects the database to infer and executes the changes required to make your database schema reflect the state of your Prisma schema.
*   Does not automatically trigger generators (for example, Prisma Client). You need to manually invoke `prisma generate` after making schema changes.
*   If `db push` anticipates that the changes could result in data loss, it will:
    *   Throw an error
    *   Require the `--accept-data-loss` option if you still want to make the changes

`db push` works well if:

*   You want to **quickly prototype and iterate** on schema design locally without the need to deploy these changes to other environments such as other developers, or staging and production environments.
*   You are prioritizing reaching a **desired end-state** and not the changes or steps executed to reach that end-state (there is no way to preview changes made by `db push`)
*   You do not need to control how schema changes impact data. There is no way to orchestrate schema and data migrations—if `db push` anticipates that changes will result in data loss, you can either accept data loss with the `--accept-data-loss` option or stop the process. There is no way to customize the changes.

See [Schema prototyping with `db push`](https://www.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema) for an example of how to use `db push` in this way.

`db push` is **not recommended** if:

*   You want to replicate your schema changes in other environments without losing data. You can use `db push` for prototyping, but you should use migrations to commit the schema changes and apply these in your other environments.
*   You want fine-grained control over how the schema changes are executed - for example, [renaming a column instead of dropping it and creating a new one](https://www.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations#example-rename-a-field).
*   You want to keep track of changes made to the database schema over time. `db push` does not create any artifacts that allow you to keep track of these changes.
*   You want the schema changes to be reversible. You can use `db push` again to revert to the original state, but this might result in data loss.

Yes, you can [use `db push` and Prisma Migrate together in your development workflow](https://www.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema) . For example, you can:

*   Use `db push` to prototype a schema at the start of a project and initialize a migration history when you are happy with the first draft
*   Use `db push` to prototype a change to an existing schema, then run `prisma migrate dev` to generate a migration from your changes (you will be asked to reset)

The following scenario demonstrates how to use `db push` to synchronize a new schema with an empty database, and evolve that schema - including what happens when `db push` detects that a change will result in data loss.

*   Create a first draft of your schema:
    
    ```
    generator client {
      provider = "prisma-client"
      output   = "./generated"
    }
    
    datasource db {
      provider = "postgresql"
    }
    
    model User {
      id       Int      @id @default(autoincrement())
      name     String
      jobTitle String
      posts    Post[]
      profile  Profile?
    }
    
    model Profile {
      id       Int    @id @default(autoincrement())
      biograpy String // Intentional typo!
      userId   Int    @unique
      user     User   @relation(fields: [userId], references: [id])
    }
    
    model Post {
      id         Int        @id @default(autoincrement())
      title      String
      published  Boolean    @default(true)
      content    String     @db.VarChar(500)
      authorId   Int
      author     User       @relation(fields: [authorId], references: [id])
      categories Category[]
    }
    
    model Category {
      id    Int    @id @default(autoincrement())
      name  String @db.VarChar(50)
      posts Post[]
    
      @@unique([name])
    }
    ```
    
*   Use `db push` to push the initial schema to the database:
    
*   Create some example content:
    
    ```
    const add = await prisma.user.create({
      data: {
        name: "Eloise",
        jobTitle: "Programmer",
        posts: {
          create: {
            title: "How to create a MySQL database",
            content: "Some content",
          },
        },
      },
    });
    ```
    
*   Make an additive change - for example, create a new required field:
    
    ```
    model Post {
      id          Int        @id @default(autoincrement())
      title       String
      description String
      published   Boolean    @default(true)
      content     String     @db.VarChar(500)
      authorId    Int
      author      User       @relation(fields: [authorId], references: [id])
      categories  Category[]
    }
    ```
    
*   Push the changes:
    
    `db push` will fail because you cannot add a required field to a table with existing content unless you provide a default value.
    
*   Reset **all data** in your database and re-apply migrations.
    

*   Continue to evolve your schema until it reaches a relatively stable state.
    
*   Initialize a migration history:
    
    The steps taken to reach the initial prototype are not preserved - `db push` does not generate a history.
    
*   Push your migration history and Prisma schema to source control (e.g. Git).
    

At this point, the final draft of your prototyping is preserved in a migration and can be pushed to other environments (testing, production, or other members of your team).

## [Prototyping with an existing migration history](#prototyping-with-an-existing-migration-history)

The following scenario demonstrates how to use `db push` to prototype a change to a Prisma schema where a migration history already exists.

*   Check out the latest Prisma schema and migration history:
    
    ```
    generator client {
      provider = "prisma-client"
      output   = "./generated"
    }
    
    datasource db {
      provider = "postgresql"
    }
    
    model User {
      id       Int      @id @default(autoincrement())
      name     String
      jobTitle String
      posts    Post[]
      profile  Profile?
    }
    
    model Profile {
      id       Int    @id @default(autoincrement())
      biograpy String // Intentional typo!
      userId   Int    @unique
      user     User   @relation(fields: [userId], references: [id])
    }
    
    model Post {
      id         Int        @id @default(autoincrement())
      title      String
      published  Boolean    @default(true)
      content    String     @db.VarChar(500)
      authorId   Int
      author     User       @relation(fields: [authorId], references: [id])
      categories Category[]
    }
    
    model Category {
      id    Int    @id @default(autoincrement())
      name  String @db.VarChar(50)
      posts Post[]
    
      @@unique([name])
    }
    ```
    
*   Prototype your new feature, which can involve any number of steps. For example, you might:
    
    *   Create a `tags String[]` field, then run `db push`
    *   Change the field type to `tags Tag[]` and add a new model named `Tag`, then run `db push`
    *   Change your mind and restore the original `tags String[]` field, then call `db push`
    *   Make a manual change to the `tags` field in the database - for example, adding a constraint
    
    After experimenting with several solutions, the final schema change looks like this:
    
    ```
    model Post {
      id          Int        @id @default(autoincrement())
      title       String
      description String
      published   Boolean    @default(true)
      content     String     @db.VarChar(500)
      authorId    Int
      author      User       @relation(fields: [authorId], references: [id])
      categories  Category[]
      tags        String[]
    }
    ```
    
*   To create a migration that adds the new `tags` field, run the `migrate dev` command:
    
    Prisma Migrate will prompt you to reset because the changes you made manually and with `db push` while prototyping are not part of the migration history:
    
    ```
    √ Drift detected: Your database schema is not in sync with your migration history.
    
    We need to reset the PostgreSQL database "prototyping" at "localhost:5432".
    ```
    

*   Prisma Migrate replays the existing migration history, generates a new migration based on your schema changes, and applies those changes to the database.

At this point, the final result of your prototyping is preserved in a migration, and can be pushed to other environments (testing, production, or other members of your team).

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-migrate/workflows/prototyping-your-schema.mdx)
