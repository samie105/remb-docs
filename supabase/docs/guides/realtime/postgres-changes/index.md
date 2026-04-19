---
title: "Postgres Changes"
source: "https://supabase.com/docs/guides/realtime/postgres-changes"
canonical_url: "https://supabase.com/docs/guides/realtime/postgres-changes"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:29.751Z"
content_hash: "e22880ed4d85cf79acce5e1bfa2dadba4b21ecc96a8568d846749613b6d36a60"
menu_path: ["Realtime","Realtime","Usage","Usage","Postgres Changes","Postgres Changes"]
section_path: ["Realtime","Realtime","Usage","Usage","Postgres Changes","Postgres Changes"]
nav_prev: {"path": "supabase/docs/guides/realtime/limits/index.md", "title": "Realtime Limits"}
nav_next: {"path": "supabase/docs/guides/realtime/presence/index.md", "title": "Presence"}
---

# 

Postgres Changes

## 

Listen to Postgres changes using Supabase Realtime.

* * *

Let's explore how to use Realtime's Postgres Changes feature to listen to database events.

## Quick start[#](#quick-start)

In this example we'll set up a database table, secure it with Row Level Security, and subscribe to all changes using the Supabase client libraries.

1

### Set up a Supabase project with a 'todos' table

[Create a new project](https://app.supabase.com) in the Supabase Dashboard.

After your project is ready, create a table in your Supabase database. You can do this with either the Table interface or the [SQL Editor](https://app.supabase.com/project/_/sql).

```
1-- Create a table called "todos"2-- with a column to store tasks.3create table todos (4  id serial primary key,5  task text6);
```

2

### Allow anonymous access

In this example we'll turn on [Row Level Security](/docs/guides/database/postgres/row-level-security) for this table and allow anonymous access. In production, be sure to secure your application with the appropriate permissions.

```
1-- Turn on security2alter table "todos"3enable row level security;45-- Allow anonymous access6create policy "Allow anonymous access"7on todos8for select9to anon10using (true);
```

3

### Enable Postgres replication

Go to your project's [Publications settings](/dashboard/project/_/database/publications), and under `supabase_realtime`, toggle on the tables you want to listen to.

Alternatively, add tables to the `supabase_realtime` publication by running the given SQL:

```
1alter publication supabase_realtime2add table your_table_name;
```

4

### Install the client

Install the Supabase JavaScript client.

```
1npm install @supabase/supabase-js
```

5

### Create the client

This client will be used to listen to Postgres changes.

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient(4  'https://<project>.supabase.co',5  '<sb_publishable_... key>'6)
```

6

### Listen to changes by schema

Listen to changes on all tables in the `public` schema by setting the `schema` property to 'public' and event name to `*`. The event name can be one of:

*   `INSERT`
*   `UPDATE`
*   `DELETE`
*   `*`

The channel name can be any string except 'realtime'.

```
1import { createClient } from '@supabase/supabase-js'2const supabase = createClient('your_project_url', 'your_supabase_api_key')34// ---cut---5const channelA = supabase6  .channel('schema-db-changes')7  .on(8    'postgres_changes',9    {10      event: '*',11      schema: 'public',12    },13    (payload) => console.log(payload)14  )15  .subscribe()
```

7

### Insert dummy data

Now we can add some data to our table which will trigger the `channelA` event handler.

```
1insert into todos (task)2values3  ('Change!');
```

## Usage[#](#usage)

You can use the Supabase client libraries to subscribe to database changes.

### Listening to specific schemas[#](#listening-to-specific-schemas)

Subscribe to specific schema events using the `schema` parameter:

```
1const changes = supabase2  .channel('schema-db-changes')3  .on(4    'postgres_changes',5    {6      schema: 'public', // Subscribes to the "public" schema in Postgres7      event: '*',       // Listen to all changes8    },9    (payload) => console.log(payload)10  )11  .subscribe()
```

The channel name can be any string except 'realtime'.

### Listening to `INSERT` events[#](#listening-to-insert-events)

Use the `event` parameter to listen only to database `INSERT`s:

```
1const changes = supabase2  .channel('schema-db-changes')3  .on(4    'postgres_changes',5    {6      event: 'INSERT', // Listen only to INSERTs7      schema: 'public',8    },9    (payload) => console.log(payload)10  )11  .subscribe()
```

The channel name can be any string except 'realtime'.

### Listening to `UPDATE` events[#](#listening-to-update-events)

Use the `event` parameter to listen only to database `UPDATE`s:

```
1const changes = supabase2  .channel('schema-db-changes')3  .on(4    'postgres_changes',5    {6      event: 'UPDATE', // Listen only to UPDATEs7      schema: 'public',8    },9    (payload) => console.log(payload)10  )11  .subscribe()
```

The channel name can be any string except 'realtime'.

### Listening to `DELETE` events[#](#listening-to-delete-events)

Use the `event` parameter to listen only to database `DELETE`s:

```
1const changes = supabase2  .channel('schema-db-changes')3  .on(4    'postgres_changes',5    {6      event: 'DELETE', // Listen only to DELETEs7      schema: 'public',8    },9    (payload) => console.log(payload)10  )11  .subscribe()
```

The channel name can be any string except 'realtime'.

### Listening to specific tables[#](#listening-to-specific-tables)

Subscribe to specific table events using the `table` parameter:

```
1const changes = supabase2  .channel('table-db-changes')3  .on(4    'postgres_changes',5    {6      event: '*',7      schema: 'public',8      table: 'todos',9    },10    (payload) => console.log(payload)11  )12  .subscribe()
```

The channel name can be any string except 'realtime'.

### Listening to multiple changes[#](#listening-to-multiple-changes)

To listen to different events and schema/tables/filters combinations with the same channel:

```
1const channel = supabase2  .channel('db-changes')3  .on(4    'postgres_changes',5    {6      event: '*',7      schema: 'public',8      table: 'messages',9    },10    (payload) => console.log(payload)11  )12  .on(13    'postgres_changes',14    {15      event: 'INSERT',16      schema: 'public',17      table: 'users',18    },19    (payload) => console.log(payload)20  )21  .subscribe()
```

### Filtering for specific changes[#](#filtering-for-specific-changes)

Use the `filter` parameter for granular changes:

```
1const changes = supabase2  .channel('table-filter-changes')3  .on(4    'postgres_changes',5    {6      event: 'INSERT',7      schema: 'public',8      table: 'todos',9      filter: 'id=eq.1',10    },11    (payload) => console.log(payload)12  )13  .subscribe()
```

## Available filters[#](#available-filters)

Realtime offers filters so you can specify the data your client receives at a more granular level.

### Equal to (`eq`)[#](#equal-to--eq-)

To listen to changes when a column's value in a table equals a client-specified value:

```
1const channel = supabase2  .channel('changes')3  .on(4    'postgres_changes',5    {6      event: 'UPDATE',7      schema: 'public',8      table: 'messages',9      filter: 'body=eq.hey',10    },11    (payload) => console.log(payload)12  )13  .subscribe()
```

This filter uses Postgres's `=` filter.

### Not equal to (`neq`)[#](#not-equal-to--neq-)

To listen to changes when a column's value in a table does not equal a client-specified value:

```
1const channel = supabase2  .channel('changes')3  .on(4    'postgres_changes',5    {6      event: 'INSERT',7      schema: 'public',8      table: 'messages',9      filter: 'body=neq.bye',10    },11    (payload) => console.log(payload)12  )13  .subscribe()
```

This filter uses Postgres's `!=` filter.

### Less than (`lt`)[#](#less-than--lt-)

To listen to changes when a column's value in a table is less than a client-specified value:

```
1const channel = supabase2  .channel('changes')3  .on(4    'postgres_changes',5    {6      event: 'INSERT',7      schema: 'public',8      table: 'profiles',9      filter: 'age=lt.65',10    },11    (payload) => console.log(payload)12  )13  .subscribe()
```

This filter uses Postgres's `<` filter, so it works for non-numeric types. Make sure to check the expected behavior of the compared data's type.

### Less than or equal to (`lte`)[#](#less-than-or-equal-to--lte-)

To listen to changes when a column's value in a table is less than or equal to a client-specified value:

```
1const channel = supabase2  .channel('changes')3  .on(4    'postgres_changes',5    {6      event: 'UPDATE',7      schema: 'public',8      table: 'profiles',9      filter: 'age=lte.65',10    },11    (payload) => console.log(payload)12  )13  .subscribe()
```

This filter uses Postgres' `<=` filter, so it works for non-numeric types. Make sure to check the expected behavior of the compared data's type.

### Greater than (`gt`)[#](#greater-than--gt-)

To listen to changes when a column's value in a table is greater than a client-specified value:

```
1const channel = supabase2  .channel('changes')3  .on(4    'postgres_changes',5    {6      event: 'INSERT',7      schema: 'public',8      table: 'products',9      filter: 'quantity=gt.10',10    },11    (payload) => console.log(payload)12  )13  .subscribe()
```

This filter uses Postgres's `>` filter, so it works for non-numeric types. Make sure to check the expected behavior of the compared data's type.

### Greater than or equal to (`gte`)[#](#greater-than-or-equal-to--gte-)

To listen to changes when a column's value in a table is greater than or equal to a client-specified value:

```
1const channel = supabase2  .channel('changes')3  .on(4    'postgres_changes',5    {6      event: 'INSERT',7      schema: 'public',8      table: 'products',9      filter: 'quantity=gte.10',10    },11    (payload) => console.log(payload)12  )13  .subscribe()
```

This filter uses Postgres's `>=` filter, so it works for non-numeric types. Make sure to check the expected behavior of the compared data's type.

### Contained in list (in)[#](#contained-in-list-in)

To listen to changes when a column's value in a table equals any client-specified values:

```
1const channel = supabase2  .channel('changes')3  .on(4    'postgres_changes',5    {6      event: 'INSERT',7      schema: 'public',8      table: 'colors',9      filter: 'name=in.(red, blue, yellow)',10    },11    (payload) => console.log(payload)12  )13  .subscribe()
```

This filter uses Postgres's `= ANY`. Realtime allows a maximum of 100 values for this filter.

## Receiving `old` records[#](#receiving-old-records)

By default, only `new` record changes are sent but if you want to receive the `old` record (previous values) whenever you `UPDATE` or `DELETE` a record, you can set the `replica identity` of your table to `full`:

```
1alter table2  messages replica identity full;
```

RLS policies are not applied to `DELETE` statements, because there is no way for Postgres to verify that a user has access to a deleted record. When RLS is enabled and `replica identity` is set to `full` on a table, the `old` record contains only the primary key(s).

## Private schemas[#](#private-schemas)

Postgres Changes works out of the box for tables in the `public` schema. You can listen to tables in your private schemas by granting table `SELECT` permissions to the database role found in your access token. You can run a query similar to the following:

```
1grant select on "non_private_schema"."some_table" to authenticated;
```

We strongly encourage you to enable RLS and create policies for tables in private schemas. Otherwise, any role you grant access to will have unfettered read access to the table.

## Custom tokens[#](#custom-tokens)

You may choose to sign your own tokens to customize claims that can be checked in your RLS policies.

Your project JWT secret is found with your [Project API keys](https://app.supabase.com/project/_/settings/api) in your dashboard.

Do not expose the `service_role` token on the client because the role is authorized to bypass row-level security.

To use your own JWT with Realtime make sure to set the token after instantiating the Supabase client and before connecting to a Channel.

```
1const { createClient } = require('@supabase/supabase-js')23const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY, {})45// Set your custom JWT here6supabase.realtime.setAuth('your-custom-jwt')78const channel = supabase9  .channel('db-changes')10  .on(11    'postgres_changes',12    {13      event: '*',14      schema: 'public',15      table: 'messages',16      filter: 'body=eq.bye',17    },18    (payload) => console.log(payload)19  )20  .subscribe()
```

### Refreshed tokens[#](#refreshed-tokens)

You will need to refresh tokens on your own, but once generated, you can pass them to Realtime.

For example, if you're using the `supabase-js` `v2` client then you can pass your token like this:

```
1// Client setup23supabase.realtime.setAuth('fresh-token')
```

## Limitations[#](#limitations)

### Delete events are not filterable[#](#delete-events-are-not-filterable)

You can't filter Delete events when tracking Postgres Changes. This limitation is due to the way changes are pulled from Postgres.

### Spaces in table names[#](#spaces-in-table-names)

Realtime currently does not work when table names contain spaces.

### Database instance and realtime performance[#](#database-instance-and-realtime-performance)

Realtime systems usually require forethought because of their scaling dynamics. For the `Postgres Changes` feature, every change event must be checked to see if the subscribed user has access. For instance, if you have 100 users subscribed to a table where you make a single insert, it will then trigger 100 "reads": one for each user.

There can be a database bottleneck which limits message throughput. If your database cannot authorize the changes rapidly enough, the changes will be delayed until you receive a timeout.

Database changes are processed on a single thread to maintain the change order. That means compute upgrades don't have a large effect on the performance of Postgres change subscriptions. You can estimate the expected maximum throughput for your database below.

If you are using Postgres Changes at scale, you should consider using separate "public" table without RLS and filters. Alternatively, you can use Realtime server-side only and then re-stream the changes to your clients using a Realtime Broadcast.

Enter your database settings to estimate the maximum throughput for your instance:

#### Set your expected parameters

Compute:

MicroSmall to mediumLarge to 16XL

Filters:

NoYes

RLS:

NoYes

Connected clients:

5005,00010,00030,000

#### Current maximum possible throughput

Total DB changes /sec

Max messages per client /sec

Max total messages /sec

Latency p95

64

64

32,000

238ms

View raw throughput table

Don't forget to run your own benchmarks to make sure that the performance is acceptable for your use case.

We are making many improvements to Realtime's Postgres Changes. If you are uncertain about the performance of your use case, reach out using [Support Form](/dashboard/support/new) and we will be happy to help you. We have a team of engineers that can advise you on the best solution for your use-case.
