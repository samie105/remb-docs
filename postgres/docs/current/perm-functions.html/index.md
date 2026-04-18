---
title: "PostgreSQL: Documentation: 18: 21.6. Function Security"
source: "https://www.postgresql.org/docs/current/perm-functions.html"
canonical_url: "https://www.postgresql.org/docs/current/perm-functions.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:12.062Z"
content_hash: "d0c09cbe240bc80996bb7e1627da0df8b2ea6b764be3895bde46c666cd093cf4"
menu_path: ["PostgreSQL: Documentation: 18: 21.6. Function Security"]
section_path: []
nav_prev: {"path": "postgres/docs/current/infoschema-routine-column-usage.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.40.\u00a0routine_column_usage"}
nav_next: {"path": "postgres/docs/current/rowtypes.html/index.md", "title": "PostgreSQL: Documentation: 18: 8.16.\u00a0Composite Types"}
---

Functions, triggers and row-level security policies allow users to insert code into the backend server that other users might execute unintentionally. Hence, these mechanisms permit users to “Trojan horse” others with relative ease. The strongest protection is tight control over who can define objects. Where that is infeasible, write queries referring only to objects having trusted owners. Remove from `search_path` any schemas that permit untrusted users to create objects.

Functions run inside the backend server process with the operating system permissions of the database server daemon. If the programming language used for the function allows unchecked memory accesses, it is possible to change the server's internal data structures. Hence, among many other things, such functions can circumvent any system access controls. Function languages that allow such access are considered “untrusted”, and PostgreSQL allows only superusers to create functions written in those languages.
