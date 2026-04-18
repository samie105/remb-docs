---
title: "pg_plan_filter: Restrict Total Cost"
source: "https://supabase.com/docs/guides/database/extensions/pg_plan_filter"
canonical_url: "https://supabase.com/docs/guides/database/extensions/pg_plan_filter"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:45.209Z"
content_hash: "3f926e9fcc966978c445e96a0bfd48fde3f2efa4d97fd495cde546f5ee16c4a9"
menu_path: ["Database","Database","Extensions","Extensions","pg_plan_filter: Restrict Total Cost","pg_plan_filter: Restrict Total Cost"]
section_path: ["Database","Database","Extensions","Extensions","pg_plan_filter: Restrict Total Cost","pg_plan_filter: Restrict Total Cost"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/pg_net/index.md", "title": "pg_net: Async Networking"}
nav_next: {"path": "supabase/docs/guides/database/extensions/pg_partman/index.md", "title": "Postgres Extensions Overview"}
---

# 

pg\_plan\_filter: Restrict Total Cost

* * *

[`pg_plan_filter`](https://github.com/pgexperts/pg_plan_filter) is Postgres extension to block execution of statements where query planner's estimate of the total cost exceeds a threshold. This is intended to give database administrators a way to restrict the contribution an individual query has on database load.

## Enable the extension[#](#enable-the-extension)

The extension is already enabled by default via `shared_preload_libraries` setting.

You can follow the instructions below.

## API[#](#api)

`plan_filter.statement_cost_limit`: restricts the maximum total cost for executed statements `plan_filter.limit_select_only`: restricts to `select` statements

Note that `limit_select_only = true` is not the same as read-only because `select` statements may modify data, for example, through a function call.

## Example[#](#example)

To demonstrate total cost filtering, we'll compare how `plan_filter.statement_cost_limit` treats queries that are under and over its cost limit. First, we set up a table with some data:

```
1create table book(2  id int primary key3);4-- CREATE TABLE56insert into book(id) select * from generate_series(1, 10000);7-- INSERT 0 10000
```

Next, we can review the explain plans for a single record select, and a whole table select.

```
1explain select * from book where id =1;2                                QUERY PLAN3---------------------------------------------------------------------------4 Index Only Scan using book_pkey on book  (cost=0.28..2.49 rows=1 width=4)5   Index Cond: (id = 1)6(2 rows)78explain select * from book;9                       QUERY PLAN10---------------------------------------------------------11 Seq Scan on book  (cost=0.00..135.00 rows=10000 width=4)12(1 row)
```

Now we can choose a `statement_cost_filter` value between the total cost for the single select (2.49) and the whole table select (135.0) so one statement will succeed and one will fail.

```
1set plan_filter.statement_cost_limit = 50; -- between 2.49 and 135.023select * from book where id = 1;4 id5----6  17(1 row)8-- SUCCESS
```

```
1select * from book;23ERROR:  plan cost limit exceeded4HINT:  The plan for your query shows that it would probably have an excessive run time. This may be due to a logic error in the SQL, or it maybe just a very costly query. Rewrite your query or increase the configuration parameter "plan_filter.statement_cost_limit".5-- FAILURE
```

## Resources[#](#resources)

*   Official [`pg_plan_filter` documentation](https://github.com/pgexperts/pg_plan_filter)

