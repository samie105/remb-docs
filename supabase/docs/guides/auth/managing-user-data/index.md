---
title: "User Management"
source: "https://supabase.com/docs/guides/auth/managing-user-data"
canonical_url: "https://supabase.com/docs/guides/auth/managing-user-data"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:08.442Z"
content_hash: "ae8d093fa049bffad87b29a6a7112e3d11f17a9dd251662c730af08a38a420b5"
menu_path: ["Auth","Auth","Configuration","Configuration","User Management","User Management"]
section_path: ["Auth","Auth","Configuration","Configuration","User Management","User Management"]
nav_prev: {"path": "supabase/docs/guides/auth/jwts/index.md", "title": "JSON Web Token (JWT)"}
nav_next: {"path": "supabase/docs/guides/auth/native-mobile-deep-linking/index.md", "title": "Native Mobile Deep Linking"}
---

# 

User Management

## 

View, delete, and export user information.

* * *

You can view your users on the [Users page](/dashboard/project/_/auth/users) of the Dashboard. You can also view the contents of the Auth schema in the [Table Editor](/dashboard/project/_/editor).

## Accessing user data via API[#](#accessing-user-data-via-api)

For security, the Auth schema is not exposed in the auto-generated API. If you want to access users data via the API, you can create your own user tables in the `public` schema.

Make sure to protect the table by enabling [Row Level Security](../../database/postgres/row-level-security/index.md). Reference the `auth.users` table to ensure data integrity. Specify `on delete cascade` in the reference. For example, a `public.profiles` table might look like this:

```
1create table public.profiles (2  id uuid not null references auth.users on delete cascade,3  first_name text,4  last_name text,56  primary key (id)7);89alter table public.profiles enable row level security;
```

Only use primary keys as [foreign key references](https://www.postgresql.org/docs/current/tutorial-fk.html) for schemas and tables like `auth.users` which are managed by Supabase. Postgres lets you specify a foreign key reference for columns backed by a unique index (not necessarily primary keys).

Primary keys are **guaranteed not to change**. Columns, indices, constraints or other database objects managed by Supabase **may change at any time** and you should be careful when referencing them directly.

To update your `public.profiles` table every time a user signs up, set up a trigger. If the trigger fails, it could block signups, so test your code thoroughly.

```
1-- inserts a row into public.profiles2create function public.handle_new_user()3returns trigger4language plpgsql5security definer set search_path = ''6as $$7begin8  insert into public.profiles (id, first_name, last_name)9  values (new.id, new.raw_user_meta_data ->> 'first_name', new.raw_user_meta_data ->> 'last_name');10  return new;11end;12$$;1314-- trigger the function every time a user is created15create trigger on_auth_user_created16  after insert on auth.users17  for each row execute procedure public.handle_new_user();
```

## Adding and retrieving user metadata[#](#adding-and-retrieving-user-metadata)

You can assign metadata to users on sign up:

```
1import { createClient } from '@supabase/supabase-js'2const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_KEY!)34// ---cut---5const { data, error } = await supabase.auth.signUp({6  email: 'valid.email@supabase.io',7  password: 'example-password',8  options: {9    data: {10      first_name: 'John',11      age: 27,12    },13  },14})
```

User metadata is stored on the `raw_user_meta_data` column of the `auth.users` table. To view the metadata:

```
1import { createClient } from '@supabase/supabase-js'2const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_KEY!)34// ---cut---5const {6  data: { user },7} = await supabase.auth.getUser()8let metadata = user?.user_metadata
```

## Deleting users[#](#deleting-users)

You may delete users directly or via the management console at Authentication > Users. Note that deleting a user from the `auth.users` table does not automatically sign out a user. As Supabase makes use of JSON Web Tokens (JWT), a user's JWT will remain "valid" until it has expired.

You cannot delete a user if they are the owner of any objects in Supabase Storage.

You will encounter an error when you try to delete an Auth user that owns any Storage objects. If this happens, try deleting all the objects for that user, or reassign ownership to another user.

## Exporting users[#](#exporting-users)

As Supabase is built on top of Postgres, you can query the `auth.users` and `auth.identities` table via the `SQL Editor` tab to extract all users:

```
1select * from auth.users;
```

You can then export the results as CSV.
