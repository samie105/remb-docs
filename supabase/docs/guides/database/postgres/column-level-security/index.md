---
title: "Column Level Security"
source: "https://supabase.com/docs/guides/database/postgres/column-level-security"
canonical_url: "https://supabase.com/docs/guides/database/postgres/column-level-security"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:23.019Z"
content_hash: "bf4082c54fe8ebd02856eaf0fc6602ad87f90678b543e2b5b81849b8b92d3264"
menu_path: ["Database","Database","Access and security","Access and security","Column Level Security","Column Level Security"]
section_path: ["Database","Database","Access and security","Access and security","Column Level Security","Column Level Security"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/uuid-ossp/index.md", "title": "uuid-ossp: Unique Identifiers"}
nav_next: {"path": "supabase/docs/guides/database/postgres/cascade-deletes/index.md", "title": "Cascade Deletes"}
---

# 

Column Level Security

* * *

Postgres's [Row Level Security (RLS)](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) gives you granular control over who can access rows of data. However, it doesn't give you control over which columns they can access within rows. Sometimes you want to restrict access to specific columns in your database. Column Level Privileges allows you to do just that.

This is an advanced feature. We do not recommend using column-level privileges for most users. Instead, we recommend using RLS policies in combination with a dedicated table for handling user roles.

Restricted roles cannot use the wildcard operator (`*`) on the affected table. Instead of using `SELECT * FROM <restricted_table>;` or its API equivalent, you must specify the column names explicitly.

## Policies at the row level[#](#policies-at-the-row-level)

Policies in Row Level Security (RLS) are used to restrict access to rows in a table. Think of them like adding a `WHERE` clause to every query.

For example, let's assume you have a `posts` table with the following columns:

*   `id`
*   `user_id`
*   `title`
*   `content`
*   `created_at`
*   `updated_at`

You can restrict updates to just the user who created it using [RLS](/docs/guides/auth#row-level-security), with the following policy:

```
1create policy "Allow update for owners" on posts for2update3  using ((select auth.uid()) = user_id);
```

However, this gives the post owner full access to update the row, including all of the columns.

## Privileges at the column level[#](#privileges-at-the-column-level)

To restrict access to columns, you can use [Privileges](https://www.postgresql.org/docs/current/ddl-priv.html).

There are two types of privileges in Postgres:

1.  **table-level**: Grants the privilege on all columns in the table.
2.  **column-level** Grants the privilege on a specific column in the table.

You can have both types of privileges on the same table. If you have both, and you revoke the column-level privilege, the table-level privilege will still be in effect.

By default, our table will have a table-level `UPDATE` privilege, which means that the `authenticated` role can update all the columns in the table.

```
1revoke2update3  on table public.posts4from5  authenticated;67grant8update9  (title, content) on table public.posts to authenticated;
```

In the above example, we are revoking the table-level `UPDATE` privilege from the `authenticated` role and granting a column-level `UPDATE` privilege on just the `title` and `content` columns.

If we want to restrict access to updating the `title` column:

```
1revoke2update3  (title) on table public.posts4from5  authenticated;
```

This time, we are revoking the column-level `UPDATE` privilege of the `title` column from the `authenticated` role. We didn't need to revoke the table-level `UPDATE` privilege because it's already revoked.

## Manage column privileges in the Dashboard[#](#manage-column-privileges-in-the-dashboard)

Column-level privileges are a powerful tool, but they're also quite advanced and in many cases, not the best fit for common access control needs. For that reason, we've intentionally moved the UI for this feature under the Feature Preview section in the dashboard.

You can view and edit the privileges in the [Supabase Studio](/dashboard/project/_/database/column-privileges).

![Column level privileges](/docs/img/guides/privileges/column-level-privileges-2.png)

## Manage column privileges in migrations[#](#manage-column-privileges-in-migrations)

While you can manage privileges directly from the Dashboard, as your project grows you may want to manage them in your migrations. Read about database migrations in the [Local Development](/docs/guides/deployment/database-migrations) guide.

1

### Create a migration file

To get started, generate a [new migration](/docs/reference/cli/supabase-migration-new) to store the SQL needed to create your table along with row and column-level privileges.

```
1supabase migration new create_posts_table
```

2

### Add the SQL to your migration file

This creates a new migration: supabase/migrations/<timestamp> \_create\_posts\_table.sql.

To that file, add the SQL to create this `posts` table with row and column-level privileges.

```
1create table2posts (3id bigint primary key generated always as identity,4user_id text,5title text,6content text,7created_at timestamptz default now()8updated_at timestamptz default now()9);1011-- Add row-level security12create policy "Allow update for owners" on posts for13update14using ((select auth.uid()) = user_id);1516-- Add column-level security17revoke18update19(title) on table public.posts20from21authenticated;
```

## Considerations when using column-level privileges[#](#considerations-when-using-column-level-privileges)

*   If you turn off a column privilege you won't be able to use that column at all.
*   All operations (insert, update, delete) as well as using `select *` will fail.


