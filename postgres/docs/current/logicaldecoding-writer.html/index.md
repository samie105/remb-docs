---
title: "PostgreSQL: Documentation: 18: 47.7. Logical Decoding Output Writers"
source: "https://www.postgresql.org/docs/current/logicaldecoding-writer.html"
canonical_url: "https://www.postgresql.org/docs/current/logicaldecoding-writer.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:46:09.964Z"
content_hash: "bb5a198a6691cf2935c5b5f96e2654705c1080ccba3ac0fb5880e1c042519079"
menu_path: ["PostgreSQL: Documentation: 18: 47.7. Logical Decoding Output Writers"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/logicaldecoding-walsender.html/index.md", "title": "PostgreSQL: Documentation: 18: 47.3.\u00a0Streaming Replication Protocol Interface"}
nav_next: {"path": "postgres/docs/current/pageinspect.html/index.md", "title": "PostgreSQL: Documentation: 18: F.23.\u00a0pageinspect \u2014 low-level inspection of database pages"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/logicaldecoding-writer.html "PostgreSQL devel - 47.7. Logical Decoding Output Writers")

| 47.7. Logical Decoding Output Writers |
| --- |
| [Prev](https://www.postgresql.org/docs/current/logicaldecoding-output-plugin.html "47.6. Logical Decoding Output Plugins")  | [Up](https://www.postgresql.org/docs/current/logicaldecoding.html "Chapter 47. Logical Decoding") | Chapter 47. Logical Decoding | [Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation") |  [Next](https://www.postgresql.org/docs/current/logicaldecoding-synchronous.html "47.8. Synchronous Replication Support for Logical Decoding") |

* * *

It is possible to add more output methods for logical decoding. For details, see `src/backend/replication/logical/logicalfuncs.c`. Essentially, three functions need to be provided: one to read WAL, one to prepare writing output, and one to write the output (see [Section 47.6.5](https://www.postgresql.org/docs/current/logicaldecoding-output-plugin.html#LOGICALDECODING-OUTPUT-PLUGIN-OUTPUT "47.6.5. Functions for Producing Output")).

* * *

<table summary="Navigation footer"><tbody><tr><td><a accesskey="p" href="https://www.postgresql.org/docs/current/logicaldecoding-output-plugin.html" title="47.6.&nbsp;Logical Decoding Output Plugins">Prev</a>&nbsp;</td><td><a accesskey="u" href="https://www.postgresql.org/docs/current/logicaldecoding.html" title="Chapter&nbsp;47.&nbsp;Logical Decoding">Up</a></td><td>&nbsp;<a accesskey="n" href="https://www.postgresql.org/docs/current/logicaldecoding-synchronous.html" title="47.8.&nbsp;Synchronous Replication Support for Logical Decoding">Next</a></td></tr><tr><td>47.6.&nbsp;Logical Decoding Output Plugins&nbsp;</td><td><a accesskey="h" href="https://www.postgresql.org/docs/current/index.html" title="PostgreSQL 18.3 Documentation">Home</a></td><td>&nbsp;47.8.&nbsp;Synchronous Replication Support for Logical Decoding</td></tr></tbody></table>

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](https://www.postgresql.org/account/comments/new/18/logicaldecoding-writer.html/) to report a documentation issue.
