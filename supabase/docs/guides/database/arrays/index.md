---
title: "Working With Arrays"
source: "https://supabase.com/docs/guides/database/arrays"
canonical_url: "https://supabase.com/docs/guides/database/arrays"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:50.948Z"
content_hash: "d581ce3a17acdf27445bac09b78c92f8ebb07a35a4b8c053311d69c497b3527c"
menu_path: ["Database","Database","Working with your database (basics)","Working with your database (basics)","Working with arrays","Working with arrays"]
section_path: ["Database","Database","Working with your database (basics)","Working with your database (basics)","Working with arrays","Working with arrays"]
nav_prev: {"path": "../../cron/quickstart/index.md", "title": "Quickstart"}
nav_next: {"path": "../beekeeper-studio/index.md", "title": "Connecting with Beekeeper Studio"}
---

# 

Working With Arrays

* * *

Postgres supports flexible [array types](https://www.postgresql.org/docs/12/arrays.html). These arrays are also supported in the Supabase Dashboard and in the JavaScript API.

## Create a table with an array column[#](#create-a-table-with-an-array-column)

Create a test table with a text array (an array of strings):

1.  Go to the [Table editor](/dashboard/project/_/editor) page in the Dashboard.
2.  Click **New Table** and create a table with the name `arraytest`.
3.  Click **Save**.
4.  Click **New Column** and create a column with the name `textarray`, type `text`, and select **Define as array**.
5.  Click **Save**.

## Insert a record with an array value[#](#insert-a-record-with-an-array-value)

1.  Go to the [Table editor](/dashboard/project/_/editor) page in the Dashboard.
2.  Select the `arraytest` table.
3.  Click **Insert row** and add `["Harry", "Larry", "Moe"]`.
4.  Click **Save.**

## View the results[#](#view-the-results)

1.  Go to the [Table editor](/dashboard/project/_/editor) page in the Dashboard.
2.  Select the `arraytest` table.

You should see:

```
1| id  | textarray               |2| --- | ----------------------- |3| 1   | ["Harry","Larry","Moe"] |
```

## Query array data[#](#query-array-data)

Postgres uses 1-based indexing (e.g., `textarray[1]` is the first item in the array).

To select the first item from the array and get the total length of the array:

```
1SELECT textarray[1], array_length(textarray, 1) FROM arraytest;
```

returns:

```
1| textarray | array_length |2| --------- | ------------ |3| Harry     | 3            |
```

## Resources[#](#resources)

*   [Supabase JS Client](https://github.com/supabase/supabase-js)
*   [Supabase - Get started for free](https://supabase.com)
*   [Postgres Arrays](https://www.postgresql.org/docs/15/arrays.html)
