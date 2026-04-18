---
title: "index_advisor: query optimization"
source: "https://supabase.com/docs/guides/database/extensions/index_advisor"
canonical_url: "https://supabase.com/docs/guides/database/extensions/index_advisor"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:28.783Z"
content_hash: "6af9ee2a5fb38b3ba568a4408c1b4386c3adb2f1c4e408e245aa2379f567454c"
menu_path: ["Database","Database","Extensions","Extensions","index_advisor: Query optimization","index_advisor: Query optimization"]
section_path: ["Database","Database","Extensions","Extensions","index_advisor: Query optimization","index_advisor: Query optimization"]
nav_prev: {"path": "supabase/docs/guides/database/connecting-to-postgres/serverless-drivers/index.md", "title": "Connect to your database"}
nav_next: {"path": "supabase/docs/guides/database/extensions/pg_cron/index.md", "title": "pg_cron: Schedule Recurring Jobs with Cron Syntax in Postgres"}
---

# 

index\_advisor: query optimization

* * *

[Index advisor](https://github.com/supabase/index_advisor) is a Postgres extension for recommending indexes to improve query performance.

Features:

*   Supports generic parameters e.g. `$1`, `$2`
*   Supports materialized views
*   Identifies tables/columns obfuscated by views
*   Skips duplicate indexes

`index_advisor` is accessible directly through Supabase Studio by navigating to the [Query Performance Report](/dashboard/project/_/advisors/query-performance) and selecting a query and then the "indexes" tab.

![Supabase Studio index\_advisor integration.](/docs/img/index_advisor_studio.png)

Alternatively, you can use index\_advisor directly via SQL.

For example:

```
1select2    *3from4  index_advisor('select book.id from book where title = $1');56 startup_cost_before | startup_cost_after | total_cost_before | total_cost_after |                  index_statements                   | errors7---------------------+--------------------+-------------------+------------------+-----------------------------------------------------+--------8 0.00                | 1.17               | 25.88             | 6.40             | {"CREATE INDEX ON public.book USING btree (title)"},| {}9(1 row)
```

## Installation[#](#installation)

To get started, enable index\_advisor by running

```
1create extension index_advisor;
```

## API[#](#api)

Index advisor exposes a single function `index_advisor(query text)` that accepts a query and searches for a set of SQL DDL `create index` statements that improve the query's execution time.

The function's signature is:

```
1index_advisor(query text)2returns3    table  (4        startup_cost_before jsonb,5        startup_cost_after jsonb,6        total_cost_before jsonb,7        total_cost_after jsonb,8        index_statements text[],9        errors text[]10    )
```

## Usage[#](#usage)

As a minimal example, the `index_advisor` function can be given a single table query with a filter on an unindexed column.

```
1create extension if not exists index_advisor cascade;23create table book(4  id int primary key,5  title text not null6);78select9  *10from11  index_advisor('select book.id from book where title = $1');1213 startup_cost_before | startup_cost_after | total_cost_before | total_cost_after |                  index_statements                   | errors14---------------------+--------------------+-------------------+------------------+-----------------------------------------------------+--------15 0.00                | 1.17               | 25.88             | 6.40             | {"CREATE INDEX ON public.book USING btree (title)"},| {}16(1 row)
```

and will return a row recommending an index on the unindexed column.

More complex queries may generate additional suggested indexes:

```
1create extension if not exists index_advisor cascade;23create table author(4    id serial primary key,5    name text not null6);78create table publisher(9    id serial primary key,10    name text not null,11    corporate_address text12);1314create table book(15    id serial primary key,16    author_id int not null references author(id),17    publisher_id int not null references publisher(id),18    title text19);2021create table review(22    id serial primary key,23    book_id int references book(id),24    body text not null25);2627select28    *29from30    index_advisor('31        select32            book.id,33            book.title,34            publisher.name as publisher_name,35            author.name as author_name,36            review.body review_body37        from38            book39            join publisher40                on book.publisher_id = publisher.id41            join author42                on book.author_id = author.id43            join review44                on book.id = review.book_id45        where46            author.id = $147            and publisher.id = $248    ');4950 startup_cost_before | startup_cost_after | total_cost_before | total_cost_after |                  index_statements                         | errors51---------------------+--------------------+-------------------+------------------+-----------------------------------------------------------+--------52 27.26               | 12.77              | 68.48             | 42.37            | {"CREATE INDEX ON public.book USING btree (author_id)",   | {}53                                                                                    "CREATE INDEX ON public.book USING btree (publisher_id)",54                                                                                    "CREATE INDEX ON public.review USING btree (book_id)"}55(3 rows)
```

## Limitations[#](#limitations)

*   index\_advisor will only recommend single column, B-tree indexes. More complex indexes will be supported in future releases.
*   when a generic argument's type is not discernible from context, an error is returned in the `errors` field. To resolve those errors, add explicit type casting to the argument. e.g. `$1::int`.

## Resources[#](#resources)

*   [`index_advisor`](https://github.com/supabase/index_advisor) repo
