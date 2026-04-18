---
title: "PostgreSQL: Documentation: 18: 7.7. VALUES Lists"
source: "https://www.postgresql.org/docs/current/queries-values.html"
canonical_url: "https://www.postgresql.org/docs/current/queries-values.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:10.843Z"
content_hash: "545b6b7f550a579ddb62ee48a4eaaba2520949ed4df700e850e026afdee77380"
menu_path: ["PostgreSQL: Documentation: 18: 7.7. VALUES Lists"]
section_path: []
nav_prev: {"path": "postgres/docs/current/bki-example.html/index.md", "title": "PostgreSQL: Documentation: 18: 68.6.\u00a0BKI Example"}
nav_next: {"path": "postgres/docs/current/logical-replication-col-lists.html/index.md", "title": "PostgreSQL: Documentation: 18: 29.5.\u00a0Column Lists"}
---

`VALUES` provides a way to generate a “constant table” that can be used in a query without having to actually create and populate a table on-disk. The syntax is

VALUES ( _`expression`_ \[, ...\] ) \[, ...\]

Each parenthesized list of expressions generates a row in the table. The lists must all have the same number of elements (i.e., the number of columns in the table), and corresponding entries in each list must have compatible data types. The actual data type assigned to each column of the result is determined using the same rules as for `UNION` (see [Section 10.5](https://www.postgresql.org/docs/current/typeconv-union-case.html "10.5. UNION, CASE, and Related Constructs")).

As an example:

VALUES (1, 'one'), (2, 'two'), (3, 'three');

will return a table of two columns and three rows. It's effectively equivalent to:

SELECT 1 AS column1, 'one' AS column2
UNION ALL
SELECT 2, 'two'
UNION ALL
SELECT 3, 'three';

By default, PostgreSQL assigns the names `column1`, `column2`, etc. to the columns of a `VALUES` table. The column names are not specified by the SQL standard and different database systems do it differently, so it's usually better to override the default names with a table alias list, like this:

\=> SELECT \* FROM (VALUES (1, 'one'), (2, 'two'), (3, 'three')) AS t (num,letter);
 num | letter
-----+--------
   1 | one
   2 | two
   3 | three
(3 rows)

Syntactically, `VALUES` followed by expression lists is treated as equivalent to:

SELECT _`select_list`_ FROM _`table_expression`_

and can appear anywhere a `SELECT` can. For example, you can use it as part of a `UNION`, or attach a _`sort_specification`_ (`ORDER BY`, `LIMIT`, and/or `OFFSET`) to it. `VALUES` is most commonly used as the data source in an `INSERT` command, and next most commonly as a subquery.

For more information see [VALUES](https://www.postgresql.org/docs/current/sql-values.html "VALUES").


