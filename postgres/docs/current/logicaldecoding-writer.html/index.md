---
title: "PostgreSQL: Documentation: 18: 47.7. Logical Decoding Output Writers"
source: "https://www.postgresql.org/docs/current/logicaldecoding-writer.html"
canonical_url: "https://www.postgresql.org/docs/current/logicaldecoding-writer.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:28.683Z"
content_hash: "1f12079225becb07f2bbd07a8bc042c762f54dbcd4bb15a754a37fa17e351c04"
menu_path: ["PostgreSQL: Documentation: 18: 47.7. Logical Decoding Output Writers"]
section_path: []
nav_prev: {"path": "postgres/docs/current/pgstatstatements.html/index.md", "title": "PostgreSQL: Documentation: 18: F.32.\u00a0pg_stat_statements \u2014 track statistics of SQL planning and execution"}
nav_next: {"path": "postgres/docs/current/sql-droptablespace.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP TABLESPACE"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/logicaldecoding-writer.html "PostgreSQL devel - 47.7. Logical Decoding Output Writers")

47.7. Logical Decoding Output Writers

[Prev](https://www.postgresql.org/docs/current/logicaldecoding-output-plugin.html "47.6. Logical Decoding Output Plugins") 

[Up](https://www.postgresql.org/docs/current/logicaldecoding.html "Chapter 47. Logical Decoding")

Chapter 47. Logical Decoding

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 [Next](https://www.postgresql.org/docs/current/logicaldecoding-synchronous.html "47.8. Synchronous Replication Support for Logical Decoding")

* * *

It is possible to add more output methods for logical decoding. For details, see `src/backend/replication/logical/logicalfuncs.c`. Essentially, three functions need to be provided: one to read WAL, one to prepare writing output, and one to write the output (see [Section 47.6.5](https://www.postgresql.org/docs/current/logicaldecoding-output-plugin.html#LOGICALDECODING-OUTPUT-PLUGIN-OUTPUT "47.6.5. Functions for Producing Output")).

* * *

[Prev](https://www.postgresql.org/docs/current/logicaldecoding-output-plugin.html "47.6. Logical Decoding Output Plugins") 

[Up](https://www.postgresql.org/docs/current/logicaldecoding.html "Chapter 47. Logical Decoding")

 [Next](https://www.postgresql.org/docs/current/logicaldecoding-synchronous.html "47.8. Synchronous Replication Support for Logical Decoding")

47.6. Logical Decoding Output Plugins 

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 47.8. Synchronous Replication Support for Logical Decoding

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](https://www.postgresql.org/account/comments/new/18/logicaldecoding-writer.html/) to report a documentation issue.
