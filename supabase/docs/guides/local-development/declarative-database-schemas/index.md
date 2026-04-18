---
title: "Declarative database schemas"
source: "https://supabase.com/docs/guides/local-development/declarative-database-schemas"
canonical_url: "https://supabase.com/docs/guides/local-development/declarative-database-schemas"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:36.348Z"
content_hash: "4e810444ca1d325f798dc9e662f6f19cc3f6fa78f5a1d4cac4e042cde5928251"
menu_path: ["Local Dev / CLI","Local Dev / CLI","Local development","Local development","Declarative database schemas","Declarative database schemas"]
section_path: ["Local Dev / CLI","Local Dev / CLI","Local development","Local development","Declarative database schemas","Declarative database schemas"]
nav_prev: {"path": "supabase/docs/guides/integrations/supabase-for-platforms/index.md", "title": "Supabase for Platforms"}
nav_next: {"path": "supabase/docs/guides/local-development/customizing-email-templates/index.md", "title": "Customizing email templates"}
---

# 

Declarative database schemas

## 

Manage your database schemas in one place and generate versioned migrations.

* * *

## Overview[#](#overview)

Declarative schemas provide a developer-friendly way to maintain schema migrations.

[Migrations](/docs/guides/deployment/database-migrations) are traditionally managed imperatively (you provide the instructions on how exactly to change the database). This can lead to related information being scattered over multiple migration files. With declarative schemas, you instead declare the state you want your database to be in, and the instructions are generated for you.

## Schema migrations[#](#schema-migrations)

Schema migrations are SQL statements written in Data Definition Language. They are versioned in your `supabase/migrations` directory to ensure schema consistency between local and remote environments.

### Declaring your schema[#](#declaring-your-schema)

1

### Create your first schema file

Create a SQL file in `supabase/schemas` directory that defines an `employees` table.

```
1create table "employees" (2  "id" integer not null,3  "name" text4);
```

2

### Generate a migration file

Generate a migration file by diffing against your declared schema.

```
1supabase db diff -f create_employees_table
```

3

### Start the local database and apply migrations

Start the local database first. Then, apply the migration manually to see your schema changes in the local Dashboard.

```
1supabase start2supabase migration up
```

### Updating your schema[#](#updating-your-schema)

1

### Add a new column

Edit `supabase/schemas/employees.sql` file to add a new column to `employees` table.

```
1create table "employees" (2  "id" integer not null,3  "name" text,4  "age" smallint not null5);
```

Some entities like views and enums expect columns to be declared in a specific order. To avoid messy diffs, always append new columns to the end of the table.

2

### Generate a new migration

Diff existing migrations against your declared schema.

```
1supabase db diff -f add_age
```

3

### Review the generated migration

Verify that the generated migration contain a single incremental change.

```
1alter table "public"."employees" add column "age" smallint not null;
```

4

### Apply the pending migration

Start the database locally and apply the pending migration.

```
1supabase migration up
```

### Deploying your schema changes[#](#deploying-your-schema-changes)

1

### Log in to the Supabase CLI

[Log in](/docs/reference/cli/supabase-login) via the Supabase CLI.

```
1supabase login
```

2

### Link your remote project

Follow the on-screen prompts to [link](/docs/reference/cli/supabase-link) your remote project.

```
1supabase link
```

3

### Deploy database changes

[Push](/docs/reference/cli/supabase-db-push) your changes to the remote database.

```
1supabase db push
```

### Managing dependencies[#](#managing-dependencies)

As your database schema evolves, you will probably start using more advanced entities like views and functions. These entities are notoriously verbose to manage using plain migrations because the entire body must be recreated whenever there is a change. Using declarative schema, you can now edit them in-place so it’s much easier to review.

```
1create table "employees" (2  "id" integer not null,3  "name" text,4  "age" smallint not null5);67create view "profiles" as8  select id, name from "employees";910create function "get_age"(employee_id integer) RETURNS smallint11  LANGUAGE "sql"12AS $$13  select age14  from employees15  where id = employee_id;16$$;
```

Your schema files are run in lexicographic order by default. The order is important when you have foreign keys between multiple tables as the parent table must be created first. For example, your `supabase` directory may end up with the following structure.

```
1.2└── supabase/3    ├── schemas/4    │   ├── employees.sql5    │   └── managers.sql6    └── migrations/7        ├── 20241004112233_create_employees_table.sql8        ├── 20241005112233_add_employee_age.sql9        └── 20241006112233_add_managers_table.sql
```

For small projects with only a few tables, the default schema order may be sufficient. However, as your project grows, you might need more control over the order in which schemas are applied. To specify a custom order for applying the schemas, you can declare them explicitly in `config.toml`. Any glob patterns will evaluated, deduplicated, and sorted in lexicographic order. For example, the following pattern ensures `employees.sql` is always executed first.

```
1[db.migrations]2schema_paths = [3  "./schemas/employees.sql",4  "./schemas/*.sql",5]
```

### Pulling in your production schema[#](#pulling-in-your-production-schema)

To set up declarative schemas on a existing project, you can pull in your production schema by running:

```
1supabase db dump > supabase/schemas/prod.sql
```

From there, you can start breaking down your schema into smaller files and generate migrations. You can do this all at once, or incrementally as you make changes to your schema.

### Rolling back a schema change[#](#rolling-back-a-schema-change)

During development, you may want to rollback a migration to keep your new schema changes in a single migration file. This can be done by resetting your local database to a previous version.

```
1supabase db reset --version 20241005112233
```

After a reset, you can [edit the schema](#updating-your-schema) and regenerate a new migration file. Note that you should not reset a version that's already deployed to production.

If you need to rollback a migration that's already deployed, you should first revert changes to the schema files. Then you can generate a new migration file containing the down migration. This ensures your production migrations are always rolling forward.

SQL statements generated in a down migration are usually destructive. You must review them carefully to avoid unintentional data loss.

## Known caveats[#](#known-caveats)

The `migra` diff tool used for generating schema diff is capable of tracking most database changes. However, there are edge cases where it can fail.

If you need to use any of the entities below, remember to add them through [versioned migrations](/docs/guides/deployment/database-migrations) instead.

### Data manipulation language[#](#data-manipulation-language)

*   DML statements such as `insert`, `update`, `delete`, etc., are not captured by schema diff

### View ownership[#](#view-ownership)

*   [view owner and grants](https://github.com/djrobstep/migra/issues/160#issuecomment-1702983833)
*   [security invoker on views](https://github.com/djrobstep/migra/issues/234)
*   [materialized views](https://github.com/djrobstep/migra/issues/194)
*   doesn’t recreate views when altering column type

### RLS policies[#](#rls-policies)

*   [alter policy statements](https://github.com/djrobstep/schemainspect/blob/master/schemainspect/pg/obj.py#L228)
*   [column privileges](https://github.com/djrobstep/schemainspect/pull/67)

### Other entities[#](#other-entities)

*   schema privileges are not tracked because each schema is diffed separately
*   [comments are not tracked](https://github.com/djrobstep/migra/issues/69)
*   [partitions are not tracked](https://github.com/djrobstep/migra/issues/186)
*   [`alter publication ... add table ...`](https://github.com/supabase/cli/issues/883)
*   [create domain statements are ignored](https://github.com/supabase/cli/issues/2137)
*   [grant statements are duplicated from default privileges](https://github.com/supabase/cli/issues/1864)
