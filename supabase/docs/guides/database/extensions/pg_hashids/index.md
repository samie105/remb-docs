---
title: "pg_hashids: Short UIDs"
source: "https://supabase.com/docs/guides/database/extensions/pg_hashids"
canonical_url: "https://supabase.com/docs/guides/database/extensions/pg_hashids"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:38.799Z"
content_hash: "5407f9a17b2a257990aaebba2cebe744ac882246005f0b99ee31eb4285c58dbf"
menu_path: ["Database","Database","Extensions","Extensions","pg_hashids: Short UIDs","pg_hashids: Short UIDs"]
section_path: ["Database","Database","Extensions","Extensions","pg_hashids: Short UIDs","pg_hashids: Short UIDs"]
nav_prev: {"path": "../pg_graphql/index.md", "title": "pg_graphql: GraphQL for Postgres"}
nav_next: {"path": "../pg_jsonschema/index.md", "title": "pg_jsonschema: JSON Schema Validation"}
---

# 

pg\_hashids: Short UIDs

* * *

[pg\_hashids](https://github.com/iCyberon/pg_hashids) provides a secure way to generate short, unique, non-sequential ids from numbers. The hashes are intended to be small, easy-to-remember identifiers that can be used to obfuscate data (optionally) with a password, alphabet, and salt. For example, you may wish to hide data like user IDs, order numbers, or tracking codes in favor of `pg_hashid`'s unique identifiers.

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for "pg\_hashids" and enable the extension.

## Usage[#](#usage)

Suppose we have a table that stores order information, and we want to give customers a unique identifier without exposing the sequential `id` column. To do this, we can use `pg_hashid`'s `id_encode` function.

```
1create table orders (2  id serial primary key,3  description text,4  price_cents bigint5);67insert into orders (description, price_cents)8values ('a book', 9095);910select11  id,12  id_encode(id) as short_id,13  description,14  price_cents15from16  orders;1718  id | short_id | description | price_cents19----+----------+-------------+-------------20  1 | jR       | a book      |        909521(1 row)
```

To reverse the `short_id` back into an `id`, there is an equivalent function named `id_decode`.

## Resources[#](#resources)

*   Official [pg\_hashids documentation](https://github.com/iCyberon/pg_hashids)
