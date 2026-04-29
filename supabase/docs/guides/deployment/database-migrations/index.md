---
title: "Database Migrations"
source: "https://supabase.com/docs/guides/deployment/database-migrations"
canonical_url: "https://supabase.com/docs/guides/deployment/database-migrations"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:04.592Z"
content_hash: "b15037d11ef6e10c67d045d1f7150d8719a3ec86e0a4642d847867f3419e068f"
menu_path: ["Deployment & Branching","Deployment & Branching","Environments","Environments","Database migrations","Database migrations"]
section_path: ["Deployment & Branching","Deployment & Branching","Environments","Environments","Database migrations","Database migrations"]
nav_prev: {"path": "../branching/working-with-branches/index.md", "title": "Working with branches"}
nav_next: {"path": "../going-into-prod/index.md", "title": "Production Checklist"}
---

# 

Database Migrations

## 

How to manage schema migrations for your Supabase project.

* * *

Database migrations are SQL statements that create, update, or delete your existing database schemas. They are a common way of tracking changes to your database over time.

## Schema migrations[#](#schema-migrations)

For this guide, we'll create a table called `employees` and see how we can make changes to it.

You will need to [install](/docs/guides/local-development#quickstart) the Supabase CLI and start the local development stack.

If a lock timeout error occurs, in your migration file, consider increasing your [`lock_timeout`](https://postgresqlco.nf/doc/en/param/lock_timeout/) setting.

1

### Create your first migration file

To get started, generate a [new migration](/docs/reference/cli/supabase-migration-new) to store the SQL needed to create our `employees` table.

###### Terminal

```
1supabase migration new create_employees_table
```

2

### Add the SQL to your migration file

This creates a new migration file in supabase/migrations directory.

To that file, add the SQL to create this `employees` table.

###### supabase/migrations/<timestamp>\_create\_employees\_table.sql

```
1create table if not exists employees (2  id bigint primary key generated always as identity,3  name text not null,4  email text,5  created_at timestamptz default now()6);
```

3

### Apply your first migration

Run this migration to create the `employees` table.

Now you can visit your new `employees` table in the local Dashboard.

###### Terminal

```
1supabase migration up
```

4

### Modify your employees table

Next, modify your `employees` table by adding a column for `department`.

###### Terminal

```
1supabase migration new add_department_column
```

5

### Add a new column to your table

To that new migration file, add the SQL to create a new `department` column.

###### supabase/migrations/<timestamp>\_add\_department\_column.sql

```
1alter table if exists public.employees2add department text default 'Hooli';
```

6

### Apply your second migration

Run this migration to update your existing `employees` table.

###### Terminal

```
1supabase migration up
```

Finally, you should see the `department` column added to your `employees` table in the local Dashboard.

View the [complete code](https://github.com/supabase/supabase/tree/master/examples/database/employees) for this example on GitHub.

### Seeding data[#](#seeding-data)

Now that you are managing your database with migrations scripts, it would be great have some seed data to use every time you reset the database.

1

### Populate your table

Create a seed script in supabase/seed.sql.

To that file, add the SQL to insert data into your `employees` table.

###### supabase/seed.sql

```
1insert into public.employees2  (name)3values4  ('Erlich Bachman'),5  ('Richard Hendricks'),6  ('Monica Hall');
```

2

### Reset your database

Reset your database to reapply migrations and populate with seed data.

###### Terminal

```
1supabase db reset
```

You should now see the `employees` table, along with your seed data in the Dashboard! All of your database changes are captured in code, and you can reset to a known state at any time, complete with seed data.

### Diffing changes[#](#diffing-changes)

This workflow is great if you know SQL and are comfortable creating tables and columns. If not, you can still use the Dashboard to create tables and columns, and then use the CLI to diff your changes and create migrations.

1

### Create your table from the Dashboard

Create a new table called `cities`, with columns `id`, `name` and `population`.

Then generate a [schema diff](/docs/reference/cli/supabase-db-diff).

###### Terminal

```
1supabase db diff -f create_cities_table
```

2

### Add schema diff as a migration

A new migration file is created for you.

Alternately, you can copy the table definitions directly from the Table Editor.

###### supabase/migrations/<timestamp>\_create\_cities\_table.sql

```
1create table "public"."cities" (2  "id" bigint primary key generated always as identity,3  "name" text,4  "population" bigint5);
```

3

### Test your migration

Test your new migration file by resetting your local database.

###### Terminal

```
1supabase db reset
```

The last step is deploying these changes to a live Supabase project.

## Deploy your project[#](#deploy-your-project)

You've been developing your project locally, making changes to your tables via migrations. It's time to deploy your project to the Supabase Platform and start scaling up to millions of users!

Head over to [Supabase](/dashboard) and create a new project to deploy to.

1

### Log in to the Supabase CLI

[Login](/docs/reference/cli/supabase-login) to the Supabase CLI using an auto-generated Personal Access Token.

###### Terminal

```
1supabase login
```

2

### Link your project

[Link](/docs/reference/cli/supabase-link) to your remote project by selecting from the on-screen prompt.

###### Terminal

```
1supabase link
```

3

### Deploy database migrations

[Push](/docs/reference/cli/supabase-db-push) your migrations to the remote database.

###### Terminal

```
1supabase db push
```

4

### Deploy database seed data (optional)

[Push](/docs/reference/cli/supabase-db-push) your migrations and seed the remote database.

###### Terminal

```
1supabase db push --include-seed
```

Visiting your live project on [Supabase](/dashboard/project/_), you'll see a new `employees` table, complete with the `department` column you added in the second migration above.
