---
title: "Select first row for each group in Postgres"
source: "https://supabase.com/docs/guides/database/postgres/first-row-in-group"
canonical_url: "https://supabase.com/docs/guides/database/postgres/first-row-in-group"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:34.804Z"
content_hash: "7f453bed38ad36f4a87ccb4b2e8efa150824cd002fcdbc73e16f9b4ca82d0f46"
menu_path: ["Database","Database","Examples","Examples","Select First Row per Group","Select First Row per Group"]
section_path: ["Database","Database","Examples","Examples","Select First Row per Group","Select First Row per Group"]
nav_prev: {"path": "supabase/docs/guides/database/postgres/event-triggers/index.md", "title": "Event Triggers"}
nav_next: {"path": "supabase/docs/guides/database/postgres/indexes/index.md", "title": "Managing Indexes in Postgres"}
---

# 

Select first row for each group in Postgres

* * *

Given a table `seasons`:

id

team

points

1

Liverpool

82

2

Liverpool

84

3

Brighton

34

4

Brighton

28

5

Liverpool

79

We want to find the rows containing the maximum number of points _per team_.

The expected output we want is:

id

team

points

3

Brighton

34

2

Liverpool

84

From the [SQL Editor](/dashboard/project/_/sql), you can run a query like:

```
1select distinct2  on (team) id,3  team,4  points5from6  seasons7order BY8  id,9  points desc,10  team;
```

The important bits here are:

*   The `desc` keyword to order the `points` from highest to lowest.
*   The `distinct` keyword that tells Postgres to only return a single row per team.

This query can also be executed via `psql` or any other query editor if you prefer to [connect directly to the database](/docs/guides/database/connecting-to-postgres#direct-connections).
