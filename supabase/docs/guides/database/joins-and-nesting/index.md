---
title: "Querying Joins and Nested tables"
source: "https://supabase.com/docs/guides/database/joins-and-nesting"
canonical_url: "https://supabase.com/docs/guides/database/joins-and-nesting"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:21.892Z"
content_hash: "b783f92842c6d10bf39afce84204dbe8e1d052fbf6adee628e48202153c29d22"
menu_path: ["Database","Database","Working with your database (basics)","Working with your database (basics)","Querying joins and nested tables","Querying joins and nested tables"]
section_path: ["Database","Database","Working with your database (basics)","Working with your database (basics)","Querying joins and nested tables","Querying joins and nested tables"]
---
# 

Querying Joins and Nested tables

* * *

The data APIs automatically detect relationships between Postgres tables. Since Postgres is a relational database, this is a very common scenario.

## One-to-many joins[#](#one-to-many-joins)

Let's use an example database that stores `orchestral_sections` and `instruments`:

**Orchestral sections**

`id`

`name`

1

strings

2

woodwinds

**Instruments**

`id`

`name`

`section_id`

1

violin

1

2

viola

1

3

flute

2

4

oboe

2

The APIs will automatically detect relationships based on the foreign keys:

```
1const { data, error } = await supabase.from('orchestral_sections').select(`2  id,3  name,4  instruments ( id, name )5`)
```

### TypeScript types for joins[#](#typescript-types-for-joins)

`supabase-js` always returns a `data` object (for success), and an `error` object (for unsuccessful requests).

These helper types provide the result types from any query, including nested types for database joins.

Given the following schema with a relation between orchestral sections and instruments:

```
1create table orchestral_sections (2  "id" serial primary key,3  "name" text4);56create table instruments (7  "id" serial primary key,8  "name" text,9  "section_id" int references "orchestral_sections"10);
```

We can get the nested `SectionsWithInstruments` type like this:

```
1import { QueryResult, QueryData, QueryError } from '@supabase/supabase-js'23const sectionsWithInstrumentsQuery = supabase.from('orchestral_sections').select(`4  id,5  name,6  instruments (7    id,8    name9  )10`)11type SectionsWithInstruments = QueryData<typeof sectionsWithInstrumentsQuery>1213const { data, error } = await sectionsWithInstrumentsQuery14if (error) throw error15const sectionsWithInstruments: SectionsWithInstruments = data
```

## Join types and join modifiers[#](#join-types-and-join-modifiers)

By default, embedded relations use **left join** semantics from the parent table:

*   Parent rows are returned even if no related rows match.
*   The embedded relation is `[]` for one-to-many joins and `null` for many-to-one joins when nothing matches.

To filter out parent rows that do not match the related table, use `!inner` on the embedded relation.

### What `:` and `!` mean in join syntax[#](#what--and--mean-in-join-syntax)

Syntax

Meaning

Example

`alias:relation(columns)`

Rename the embedded relation in the response.

`start_scan:scans(id, badge_scan_time)`

`relation!inner(columns)`

Use `inner join` behavior for that embedded relation.

`instruments!inner(id, name)`

`relation!foreign_key(columns)`

Choose which foreign key relationship to use when multiple foreign keys match the join.

`scans!scan_id_start(id)`

### Example data for join types[#](#example-data-for-join-types)

#### Orchestral sections[#](#orchestral-sections)

`id`

`name`

1

strings

2

woodwinds

3

percussion

#### Instruments[#](#instruments)

`id`

`name`

`section_id`

1

violin

1

2

viola

1

3

flute

2

4

oboe

2

### Left join (default)[#](#left-join-default)

This query filters on a joined field (`instruments.name`) but still returns all parent rows:

```
1const { data, error } = await supabase2  .from('orchestral_sections')3  .select(4    `5    id,6    name,7    instruments ( id, name )8  `9  )10  .eq('instruments.name', 'flute')
```

#### Result[#](#result)

```
1[2  {3    "id": 1,4    "name": "strings",5    "instruments": []6  },7  {8    "id": 2,9    "name": "woodwinds",10    "instruments": [{ "id": 3, "name": "flute" }]11  },12  {13    "id": 3,14    "name": "percussion",15    "instruments": []16  }17]
```

### Inner join (`!inner`)[#](#inner-join--inner-)

Adding `!inner` filters out parent rows that don't match the joined filter:

```
1const { data, error } = await supabase2  .from('orchestral_sections')3  .select(4    `5    id,6    name,7    instruments!inner ( id, name )8  `9  )10  .eq('instruments.name', 'flute')
```

#### Result[#](#result)

```
1[2  {3    "id": 2,4    "name": "woodwinds",5    "instruments": [{ "id": 3, "name": "flute" }]6  }7]
```

### Filtering using joined fields[#](#filtering-using-joined-fields)

Use `joined_table.column` in filters (for example `eq`, `neq`, and `in`):

```
1const { data, error } = await supabase2  .from('instruments')3  .select(4    `5    id,6    name,7    orchestral_sections!inner ( id, name )8  `9  )10  .eq('orchestral_sections.name', 'woodwinds')
```

#### Result[#](#result)

```
1[2  {3    "id": 3,4    "name": "flute",5    "orchestral_sections": {6      "id": 2,7      "name": "woodwinds"8    }9  },10  {11    "id": 4,12    "name": "oboe",13    "orchestral_sections": {14      "id": 2,15      "name": "woodwinds"16    }17  }18]
```

## Many-to-many joins[#](#many-to-many-joins)

The data APIs will detect many-to-many joins. For example, if you have a database which stored teams of users (where each user could belong to many teams):

```
1create table users (2  "id" serial primary key,3  "name" text4);56create table teams (7  "id" serial primary key,8  "team_name" text9);1011create table members (12  "user_id" int references users,13  "team_id" int references teams,14  primary key (user_id, team_id)15);
```

In these cases you don't need to explicitly define the joining table (members). If we wanted to fetch all the teams and the members in each team:

```
1const { data, error } = await supabase.from('teams').select(`2  id,3  team_name,4  users ( id, name )5`)
```

## Specifying the `ON` clause for joins with multiple foreign keys[#](#specifying-the-on-clause-for-joins-with-multiple-foreign-keys)

For example, if you have a project that tracks when employees check in and out of work shifts:

```
1-- Employees2create table users (3  "id" serial primary key,4  "name" text5);67-- Badge scans8create table scans (9  "id" serial primary key,10  "user_id" int references users,11  "badge_scan_time" timestamp12);1314-- Work shifts15create table shifts (16  "id" serial primary key,17  "user_id" int references users,18  "scan_id_start" int references scans, -- clocking in19  "scan_id_end" int references scans, -- clocking out20  "attendance_status" text21);
```

In this case, you need to explicitly define the join because the joining column on `shifts` is ambiguous as they are both referencing the `scans` table.

To fetch all the `shifts` with `scan_id_start` and `scan_id_end` related to a specific `scan`, use the following syntax:

```
1const { data, error } = await supabase.from('shifts').select(2  `3    *,4    start_scan:scans!scan_id_start (5      id,6      user_id,7      badge_scan_time8    ),9   end_scan:scans!scan_id_end (10     id,11     user_id,12     badge_scan_time13    )14  `15)
```
