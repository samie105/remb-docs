---
title: "HypoPG: Hypothetical indexes"
source: "https://supabase.com/docs/guides/database/extensions/hypopg"
canonical_url: "https://supabase.com/docs/guides/database/extensions/hypopg"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:22.248Z"
content_hash: "7ec912274de28afdb34457eba41b4cd169bc9e2fb5f3152b351b63f465066fc8"
menu_path: ["Database","Database","Extensions","Extensions","HypoPG: Hypothetical indexes","HypoPG: Hypothetical indexes"]
section_path: ["Database","Database","Extensions","Extensions","HypoPG: Hypothetical indexes","HypoPG: Hypothetical indexes"]
---
# 

HypoPG: Hypothetical indexes

* * *

`HypoPG` is Postgres extension for creating hypothetical/virtual indexes. HypoPG allows users to rapidly create hypothetical/virtual indexes that have no resource cost (CPU, disk, memory) that are visible to the Postgres query planner.

The motivation for HypoPG is to allow users to quickly search for an index to improve a slow query without consuming server resources or waiting for them to build.

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for `hypopg` and enable the extension.

### Speeding up a query[#](#speeding-up-a-query)

Given the following table and a simple query to select from the table by `id`:

```
1create table account (2  id int,3  address text4);56insert into account(id, address)7select8  id,9  id || ' main street'10from11  generate_series(1, 10000) id;
```

We can generate an explain plan for a description of how the Postgres query planner intends to execute the query.

```
1explain select * from account where id=1;23                      QUERY PLAN4-------------------------------------------------------5 Seq Scan on account  (cost=0.00..180.00 rows=1 width=13)6   Filter: (id = 1)7(2 rows)
```

Using HypoPG, we can create a hypothetical index on the `account(id)` column to check if it would be useful to the query planner and then re-run the explain plan.

Note that the virtual indexes created by HypoPG are only visible in the Postgres connection that they were created in. Supabase connects to Postgres through a connection pooler so the `hypopg_create_index` statement and the `explain` statement should be executed in a single query.

```
1select * from hypopg_create_index('create index on account(id)');23explain select * from account where id=1;45                                     QUERY PLAN6------------------------------------------------------------------------------------7 Index Scan using <13504>btree_account_id on hypo  (cost=0.29..8.30 rows=1 width=13)8   Index Cond: (id = 1)9(2 rows)
```

The query plan has changed from a `Seq Scan` to an `Index Scan` using the newly created virtual index, so we may choose to create a real version of the index to improve performance on the target query:

```
1create index on account(id);
```

## Functions[#](#functions)

*   [`hypo_create_index(text)`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#create-a-hypothetical-index): A function to create a hypothetical index.
*   [`hypopg_list_indexes`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#manipulate-hypothetical-indexes): A View that lists all hypothetical indexes that have been created.
*   [`hypopg()`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#manipulate-hypothetical-indexes): A function that lists all hypothetical indexes that have been created with the same format as `pg_index`.
*   [`hypopg_get_index_def(oid)`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#manipulate-hypothetical-indexes): A function to display the `create index` statement that would create the index.
*   [`hypopg_get_relation_size(oid)`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#manipulate-hypothetical-indexes): A function to estimate how large a hypothetical index would be.
*   [`hypopg_drop_index(oid)`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#manipulate-hypothetical-indexes): A function to remove a given hypothetical index by `oid`.
*   [`hypopg_reset()`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#manipulate-hypothetical-indexes): A function to remove all hypothetical indexes.

## Resources[#](#resources)

*   Official [HypoPG documentation](https://hypopg.readthedocs.io/en/rel1_stable/)
