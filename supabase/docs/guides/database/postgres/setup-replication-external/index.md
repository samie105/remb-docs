---
title: "Replicate to another Postgres database using Logical Replication"
source: "https://supabase.com/docs/guides/database/postgres/setup-replication-external"
canonical_url: "https://supabase.com/docs/guides/database/postgres/setup-replication-external"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:44.322Z"
content_hash: "d932092c592ece100a913b1df46ade3ee4f99c07432fc4d339bdf60aedd0556b"
menu_path: ["Database","Database","Examples","Examples","Replicating from Supabase to External Postgres","Replicating from Supabase to External Postgres"]
section_path: ["Database","Database","Examples","Examples","Replicating from Supabase to External Postgres","Replicating from Supabase to External Postgres"]
nav_prev: {"path": "supabase/docs/guides/database/postgres/roles/index.md", "title": "Postgres Roles"}
nav_next: {"path": "supabase/docs/guides/database/postgres/row-level-security/index.md", "title": "Row Level Security"}
---

# 

Replicate to another Postgres database using Logical Replication

* * *

For this example, you will need:

*   A Supabase project
*   A Postgres database (running v10 or newer)

You will be running commands on both of these databases to publish changes from the Supabase database to the external database.

1.  Create a `publication` on the **Supabase database**:

```
1CREATE PUBLICATION example_pub;
```

2.  Also on the **Supabase database**, create a `replication slot`:

```
1select pg_create_logical_replication_slot('example_slot', 'pgoutput');
```

3.  Now connect to your **external database** and subscribe to the `publication`

This needs a **direct** connection (not a Connection Pooler) to your database and you can find the connection info in the [**Connect** panel](/dashboard/project/_?showConnect=true) in the `Direct connection` section.

You will also need to ensure that IPv6 is supported by your replication destination (or you can enable the [IPv4 add-on](/docs/guides/platform/ipv4-address))

If you would prefer not to use the `postgres` user, then you can run `CREATE ROLE <user> WITH REPLICATION;` using the `postgres` user.

```
1CREATE SUBSCRIPTION example_sub2CONNECTION 'host=db.oaguxblfdassqxvvwtfe.supabase.co user=postgres password=YOUR_PASS dbname=postgres'3PUBLICATION example_pub4WITH (copy_data = true, create_slot=false, slot_name=example_slot);
```

For projects running Postgres 17+, it is possible to subscribe to a [Read Replica](/docs/guides/platform/read-replicas) by using your Read Replica's connection string.

`create_slot` is set to `false` because `slot_name` is provided and the slot was already created in Step 2. To copy data from before the slot was created, set `copy_data` to `true`.

4.  Now we'll go back to the Supabase DB and add all the tables that you want replicated to the publication.

```
1ALTER PUBLICATION example_pub ADD TABLE example_table;
```

5.  Check the replication status using `pg_stat_replication`

```
1select * from pg_stat_replication;
```

You can add more tables to the initial publication, but you're going to need to do a REFRESH on the subscribing database. See [https://www.postgresql.org/docs/current/sql-alterpublication.html](https://www.postgresql.org/docs/current/sql-alterpublication.html)

