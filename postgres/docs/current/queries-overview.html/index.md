---
title: "PostgreSQL: Documentation: 18: 7.1. Overview"
source: "https://www.postgresql.org/docs/current/queries-overview.html"
canonical_url: "https://www.postgresql.org/docs/current/queries-overview.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:07.368Z"
content_hash: "d86c95654f3b38635f21267b2f45b84923c0fdb9828de996677df963e7a82569"
menu_path: ["PostgreSQL: Documentation: 18: 7.1. Overview"]
section_path: []
---
The process of retrieving or the command to retrieve data from a database is called a _query_. In SQL the [`SELECT`](https://www.postgresql.org/docs/current/sql-select.html "SELECT") command is used to specify queries. The general syntax of the `SELECT` command is

\[WITH _`with_queries`_\] SELECT _`select_list`_ FROM _`table_expression`_ \[_`sort_specification`_\]

The following sections describe the details of the select list, the table expression, and the sort specification. `WITH` queries are treated last since they are an advanced feature.

A simple kind of query has the form:

SELECT \* FROM table1;

Assuming that there is a table called `table1`, this command would retrieve all rows and all user-defined columns from `table1`. (The method of retrieval depends on the client application. For example, the psql program will display an ASCII-art table on the screen, while client libraries will offer functions to extract individual values from the query result.) The select list specification `*` means all columns that the table expression happens to provide. A select list can also select a subset of the available columns or make calculations using the columns. For example, if `table1` has columns named `a`, `b`, and `c` (and perhaps others) you can make the following query:

SELECT a, b + c FROM table1;

(assuming that `b` and `c` are of a numerical data type). See [Section 7.3](https://www.postgresql.org/docs/current/queries-select-lists.html "7.3. Select Lists") for more details.

`FROM table1` is a simple kind of table expression: it reads just one table. In general, table expressions can be complex constructs of base tables, joins, and subqueries. But you can also omit the table expression entirely and use the `SELECT` command as a calculator:

SELECT 3 \* 4;

This is more useful if the expressions in the select list return varying results. For example, you could call a function this way:

SELECT random();
