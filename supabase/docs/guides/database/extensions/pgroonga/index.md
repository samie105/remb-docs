---
title: "PGroonga: Multilingual Full Text Search"
source: "https://supabase.com/docs/guides/database/extensions/pgroonga"
canonical_url: "https://supabase.com/docs/guides/database/extensions/pgroonga"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:59.976Z"
content_hash: "098f66d6b8c144813cea8c958ac41c448c559a833baea058e677d792232c20ee"
menu_path: ["Database","Database","Extensions","Extensions","PGroonga: Multilingual Full Text Search","PGroonga: Multilingual Full Text Search"]
section_path: ["Database","Database","Extensions","Extensions","PGroonga: Multilingual Full Text Search","PGroonga: Multilingual Full Text Search"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/pgrouting/index.md", "title": "pgrouting: Geospatial Routing"}
nav_next: {"path": "supabase/docs/guides/database/extensions/pgvector/index.md", "title": "pgvector: Embeddings and vector similarity"}
---

# 

PGroonga: Multilingual Full Text Search

* * *

`PGroonga` is a Postgres extension adding a full text search indexing method based on [Groonga](https://groonga.org). While native Postgres supports full text indexing, it is limited to alphabet and digit based languages. `PGroonga` offers a wider range of character support making it viable for a superset of languages supported by Postgres including Japanese, Chinese, etc.

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for `pgroonga` and enable the extension.

## Creating a full text search index[#](#creating-a-full-text-search-index)

Given a table with a `text` column:

```
1create table memos (2  id serial primary key,3  content text4);
```

We can index the column for full text search with a `pgroonga` index:

```
1create index ix_memos_content ON memos USING pgroonga(content);
```

To test the full text index, we'll add some data.

```
1insert into memos(content)2values3  ('Postgres is a relational database management system.'),4  ('Groonga is a fast full text search engine that supports all languages.'),5  ('PGroonga is a Postgres extension that uses Groonga as index.'),6  ('There is groonga command.');
```

The Postgres query planner is smart enough to know that, for extremely small tables, it's faster to scan the whole table rather than loading an index. To force the index to be used, we can disable sequential scans:

```
1-- For testing only. Don't do this in production2set enable_seqscan = off;
```

Now if we run an explain plan on a query filtering on `memos.content`:

```
1explain select * from memos where content like '%engine%';23                               QUERY PLAN4-----------------------------------------------------------------------------5Index Scan using ix_memos_content on memos  (cost=0.00..1.11 rows=1 width=36)6  Index Cond: (content ~~ '%engine%'::text)7(2 rows)
```

The `pgroonga` index is used to retrieve the result set:

```
1| id  | content                                                                  |2| --- | ------------------------------------------------------------------------ |3| 2   | 'Groonga is a fast full text search engine that supports all languages.' |
```

## Full text search[#](#full-text-search)

The `&@~` operator performs full text search. It returns any matching results. Unlike `LIKE` operator, `pgroonga` can search any text that contains the keyword case insensitive.

Take the following example:

```
1select * from memos where content &@~ 'groonga';
```

And the result:

```
1id | content  2----+------------------------------------------------------------------------32 | Groonga is a fast full text search engine that supports all languages.43 | PGroonga is a Postgres extension that uses Groonga as index.54 | There is groonga command.6(3 rows)
```

### Match all search words[#](#match-all-search-words)

To find all memos where content contains BOTH of the words `postgres` and `pgroonga`, we can just use space to separate each words:

```
1select * from memos where content &@~ 'postgres pgroonga';
```

And the result:

```
1id | content  2----+----------------------------------------------------------------33 | PGroonga is a Postgres extension that uses Groonga as index.4(1 row)
```

### Match any search words[#](#match-any-search-words)

To find all memos where content contain ANY of the words `postgres` or `pgroonga`, use the upper case `OR`:

```
1select * from memos where content &@~ 'postgres OR pgroonga';
```

And the result:

```
1id | content  2----+----------------------------------------------------------------31 | Postgres is a relational database management system.43 | PGroonga is a Postgres extension that uses Groonga as index.5(2 rows)
```

### Search that matches words with negation[#](#search-that-matches-words-with-negation)

To find all memos where content contain the word `postgres` but not `pgroonga`, use `-` symbol:

```
1select * from memos where content &@~ 'postgres -pgroonga';
```

And the result:

```
1id | content  2----+--------------------------------------------------------31 | Postgres is a relational database management system.4(1 row)
```

## Resources[#](#resources)

*   Official [PGroonga documentation](https://pgroonga.github.io/tutorial/)

