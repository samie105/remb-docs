---
title: "Build an API route in less than 2 minutes."
source: "https://supabase.com/docs/guides/api/quickstart"
canonical_url: "https://supabase.com/docs/guides/api/quickstart"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:29.478Z"
content_hash: "4b13c17eb630ac376e6cf47ad163f02e19e646fa87af723040235af1201dcf28"
menu_path: ["Data REST API","Data REST API","Quickstart","Quickstart"]
section_path: ["Data REST API","Data REST API","Quickstart","Quickstart"]
nav_prev: {"path": "supabase/docs/guides/api/hardening-data-api/index.md", "title": "Hardening the Data API"}
nav_next: {"path": "supabase/docs/guides/api/rest/auto-generated-docs/index.md", "title": "Auto-generated documentation"}
---

# 

Build an API route in less than 2 minutes.

## 

Create your first API route by creating a table called `todos` to store tasks.

* * *

Let's create our first REST route which we can query using `cURL` or the browser.

We'll create a database table called `todos` for storing tasks. This creates a corresponding API route `/rest/v1/todos` which can accept `GET`, `POST`, `PATCH`, & `DELETE` requests.

1

### Set up a Supabase project with a 'todos' table

[Create a new project](/dashboard) in the Supabase Dashboard.

After your project is ready, create a table in your Supabase database. You can do this with either the Table interface or the [SQL Editor](/dashboard/project/_/sql).

```
1-- Create a table called "todos"2-- with a column to store tasks.3create table todos (4  id serial primary key,5  task text6);
```

2

### Allow public access

Let's turn on Row Level Security for this table and allow public access.

```
1-- Turn on security2alter table "todos"3enable row level security;45-- Allow anonymous access6create policy "Allow public access"7  on todos8  for select9  to anon10  using (true);
```

3

### Insert some dummy data

Now we can add some data to our table which we can access through our API.

```
1insert into todos (task)2values3  ('Create tables'),4  ('Enable security'),5  ('Add data'),6  ('Fetch data from the API');
```

4

### Fetch the data

Find your API URL and Keys in your Dashboard [API Settings](/dashboard/project/_/settings/api). You can now query your "todos" table by appending `/rest/v1/todos` to the API URL.

Copy this block of code, substitute `<PROJECT_REF>` and `<ANON_KEY>`, then run it from a terminal.

```
1curl 'https://<PROJECT_REF>.supabase.co/rest/v1/todos' \2-H "apikey: <ANON_KEY>" \3-H "Authorization: Bearer <ANON_KEY>"
```

## Bonus[#](#bonus)

There are several options for accessing your data:

### Browser[#](#browser)

You can query the route in your browser, by appending the `anon` key as a query parameter:

`https://<PROJECT_REF>.supabase.co/rest/v1/todos?apikey=<ANON_KEY>`

### Client libraries[#](#client-libraries)

We provide a number of [Client Libraries](https://github.com/supabase/supabase#client-libraries).

```
1const { data, error } = await supabase.from('todos').select()
```
