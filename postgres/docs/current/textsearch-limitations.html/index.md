---
title: "PostgreSQL: Documentation: 18: 12.11. Limitations"
source: "https://www.postgresql.org/docs/current/textsearch-limitations.html"
canonical_url: "https://www.postgresql.org/docs/current/textsearch-limitations.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:37.525Z"
content_hash: "eac9273cfc9bc7deba4bef6da0cd24419cf56eff3491599effe7a2aeae4b40b5"
menu_path: ["PostgreSQL: Documentation: 18: 12.11. Limitations"]
section_path: []
nav_prev: {"path": "postgres/docs/current/runtime-config-wal.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.5.\u00a0Write Ahead Log"}
nav_next: {"path": "postgres/docs/current/infoschema-foreign-data-wrappers.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.27.\u00a0foreign_data_wrappers"}
---

The current limitations of PostgreSQL's text search features are:

*   The length of each lexeme must be less than 2 kilobytes
    
*   The length of a `tsvector` (lexemes + positions) must be less than 1 megabyte
    
*   The number of lexemes must be less than 264
    
*   Position values in `tsvector` must be greater than 0 and no more than 16,383
    
*   The match distance in a ``<_`N`_>`` (FOLLOWED BY) `tsquery` operator cannot be more than 16,384
    
*   No more than 256 positions per lexeme
    
*   The number of nodes (lexemes + operators) in a `tsquery` must be less than 32,768
    

For comparison, the PostgreSQL 8.1 documentation contained 10,441 unique words, a total of 335,420 words, and the most frequent word “postgresql” was mentioned 6,127 times in 655 documents.

Another example — the PostgreSQL mailing list archives contained 910,989 unique words with 57,491,343 lexemes in 461,020 messages.
