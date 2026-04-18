---
title: "PostgreSQL: Documentation: 18: 2.9. Deletions"
source: "https://www.postgresql.org/docs/current/tutorial-delete.html"
canonical_url: "https://www.postgresql.org/docs/current/tutorial-delete.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:32.995Z"
content_hash: "2783c693f8834254ec547da6842a247baaacf05e44096eef844232b010215e6d"
menu_path: ["PostgreSQL: Documentation: 18: 2.9. Deletions"]
section_path: []
nav_prev: {"path": "postgres/docs/current/upgrading.html/index.md", "title": "PostgreSQL: Documentation: 18: 18.6.\u00a0Upgrading a PostgreSQL Cluster"}
nav_next: {"path": "postgres/docs/current/sql-createtsparser.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE TEXT SEARCH PARSER"}
---

Rows can be removed from a table using the `DELETE` command. Suppose you are no longer interested in the weather of Hayward. Then you can do the following to delete those rows from the table:

DELETE FROM weather WHERE city = 'Hayward';

All weather records belonging to Hayward are removed.

SELECT \* FROM weather;

     city      | temp\_lo | temp\_hi | prcp |    date
---------------+---------+---------+------+------------
 San Francisco |      46 |      50 | 0.25 | 1994-11-27
 San Francisco |      41 |      55 |    0 | 1994-11-29
(2 rows)

One should be wary of statements of the form

DELETE FROM _`tablename`_;

Without a qualification, `DELETE` will remove _all_ rows from the given table, leaving it empty. The system will not request confirmation before doing this!


