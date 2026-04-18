---
title: "PostgreSQL: Documentation: 18: 68.5. Structure of the Bootstrap BKI File"
source: "https://www.postgresql.org/docs/current/bki-structure.html"
canonical_url: "https://www.postgresql.org/docs/current/bki-structure.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:25.343Z"
content_hash: "917ef1c74950f3a84795372c9d920aa2aeb814f9cc42bfdd1c179b1d3df25d05"
menu_path: ["PostgreSQL: Documentation: 18: 68.5. Structure of the Bootstrap BKI File"]
section_path: []
nav_prev: {"path": "postgres/docs/current/routine-vacuuming.html/index.md", "title": "PostgreSQL: Documentation: 18: 24.1.\u00a0Routine Vacuuming"}
nav_next: {"path": "postgres/docs/current/protocol-changes.html/index.md", "title": "PostgreSQL: Documentation: 18: 54.10.\u00a0Summary of Changes since Protocol 2.0"}
---

The `open` command cannot be used until the tables it uses exist and have entries for the table that is to be opened. (These minimum tables are `pg_class`, `pg_attribute`, `pg_proc`, and `pg_type`.) To allow those tables themselves to be filled, `create` with the `bootstrap` option implicitly opens the created table for data insertion.

Also, the `declare index` and `declare toast` commands cannot be used until the system catalogs they need have been created and filled in.

Thus, the structure of the `postgres.bki` file has to be:

1.  `create bootstrap` one of the critical tables
    
2.  `insert` data describing at least the critical tables
    
3.  `close`
    
4.  Repeat for the other critical tables.
    
5.  `create` (without `bootstrap`) a noncritical table
    
6.  `open`
    
7.  `insert` desired data
    
8.  `close`
    
9.  Repeat for the other noncritical tables.
    
10.  Define indexes and toast tables.
     
11.  `build indices`
     

There are doubtless other, undocumented ordering dependencies.
