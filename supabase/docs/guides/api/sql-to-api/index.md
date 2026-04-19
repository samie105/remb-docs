---
title: "Converting SQL to JavaScript API"
source: "https://supabase.com/docs/guides/api/sql-to-api"
canonical_url: "https://supabase.com/docs/guides/api/sql-to-api"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:44.830Z"
content_hash: "e77a294a0d58e02b2c1b216526255f3a68fb5ff9a7eeae85e168955e58e2df1e"
menu_path: ["Data REST API","Data REST API","Using the Data APIs","Using the Data APIs","Converting from SQL to JavaScript API","Converting from SQL to JavaScript API"]
section_path: ["Data REST API","Data REST API","Using the Data APIs","Using the Data APIs","Converting from SQL to JavaScript API","Converting from SQL to JavaScript API"]
nav_prev: {"path": "supabase/docs/guides/api/securing-your-api/index.md", "title": "Securing your API"}
nav_next: {"path": "supabase/docs/guides/api/sql-to-rest/index.md", "title": "SQL to REST API Translator"}
---

# 

Converting SQL to JavaScript API

* * *

Many common SQL queries can be written using the JavaScript API, provided by the SDK to wrap Data API calls. Below are a few examples of conversions between SQL and JavaScript patterns.

## Select statement with basic clauses[#](#select-statement-with-basic-clauses)

Select a set of columns from a single table with where, order by, and limit clauses.

```
1select first_name, last_name, team_id, age2from players3where age between 20 and 24 and team_id != 'STL'4order by last_name, first_name desc5limit 20;
```

```
1const { data, error } = await supabase2  .from('players')3  .select('first_name,last_name,team_id,age')4  .gte('age', 20)5  .lte('age', 24)6  .not('team_id', 'eq', 'STL')7  .order('last_name', { ascending: true }) // or just .order('last_name')8  .order('first_name', { ascending: false })9  .limit(20)
```

## Select statement with complex Boolean logic clause[#](#select-statement-with-complex-boolean-logic-clause)

Select all columns from a single table with a complex where clause: OR AND OR

```
1select *2from players3where ((team_id = 'CHN' or team_id is null) and (age > 35 or age is null));
```

```
1const { data, error } = await supabase2  .from('players')3  .select() // or .select('*')4  .or('team_id.eq.CHN,team_id.is.null')5  .or('age.gt.35,age.is.null') // additional filters imply "AND"
```

Select all columns from a single table with a complex where clause: AND OR AND

```
1select *2from players3where ((team_id = 'CHN' and age > 35) or (team_id != 'CHN' and age is not null));
```

```
1const { data, error } = await supabase2  .from('players')3  .select() // or .select('*')4  .or('and(team_id.eq.CHN,age.gt.35),and(team_id.neq.CHN,.not.age.is.null)')
```

## Resources[#](#resources)

*   [Supabase - Get started for free](https://supabase.com)
*   [PostgREST Operators](https://postgrest.org/en/stable/api.html#operators)
*   [Supabase API: JavaScript select](/docs/reference/javascript/select)
*   [Supabase API: JavaScript modifiers](/docs/reference/javascript/using-modifiers)
*   [Supabase API: JavaScript filters](/docs/reference/javascript/using-filters)
