---
title: "PostgreSQL: Documentation: 18: 68.6. BKI Example"
source: "https://www.postgresql.org/docs/current/bki-example.html"
canonical_url: "https://www.postgresql.org/docs/current/bki-example.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:44:30.320Z"
content_hash: "0402fca18862e4afe45500cf808e12fdc16230df312561e6b5e2081ddcc8650d"
menu_path: ["PostgreSQL: Documentation: 18: 68.6. BKI Example"]
section_path: []
content_language: "en"
---
| 68.6. BKI Example |
| --- |
| [Prev](https://www.postgresql.org/docs/current/bki-structure.html "68.5. Structure of the Bootstrap BKI File")  | [Up](https://www.postgresql.org/docs/current/bki.html "Chapter 68. System Catalog Declarations and Initial Contents") | Chapter 68. System Catalog Declarations and Initial Contents | [Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation") |  [Next](https://www.postgresql.org/docs/current/planner-stats-details.html "Chapter 69. How the Planner Uses Statistics") |

* * *

The following sequence of commands will create the table `test_table` with OID 420, having three columns `oid`, `cola` and `colb` of type `oid`, `int4` and `text`, respectively, and insert two rows into the table:

create test\_table 420 (oid = oid, cola = int4, colb = text)
open test\_table
insert ( 421 1 'value 1' )
insert ( 422 2 \_null\_ )
close test\_table
