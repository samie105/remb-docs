---
title: "PostgreSQL: Documentation: 18: H.1. Client Interfaces"
source: "https://www.postgresql.org/docs/current/external-interfaces.html"
canonical_url: "https://www.postgresql.org/docs/current/external-interfaces.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:49:27.846Z"
content_hash: "207dc7a806ed5af64bf151cc312c831225dce9790268e4354d71ace686887e4f"
menu_path: ["PostgreSQL: Documentation: 18: H.1. Client Interfaces"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/external-extensions.html/index.md", "title": "PostgreSQL: Documentation: 18: H.4.\u00a0Extensions"}
nav_next: {"path": "postgres/docs/current/external-pl.html/index.md", "title": "PostgreSQL: Documentation: 18: H.3.\u00a0Procedural Languages"}
---

There are only two client interfaces included in the base PostgreSQL distribution:

-   [libpq](https://www.postgresql.org/docs/current/libpq.html "Chapter 32. libpq — C Library") is included because it is the primary C language interface, and because many other client interfaces are built on top of it.
    
-   [ECPG](https://www.postgresql.org/docs/current/ecpg.html "Chapter 34. ECPG — Embedded SQL in C") is included because it depends on the server-side SQL grammar, and is therefore sensitive to changes in PostgreSQL itself.
    

All other language interfaces are external projects and are distributed separately. A [list of language interfaces](https://wiki.postgresql.org/wiki/List_of_drivers) is maintained on the PostgreSQL wiki. Note that some of these packages are not released under the same license as PostgreSQL. For more information on each language interface, including licensing terms, refer to its website and documentation.

[https://wiki.postgresql.org/wiki/List\_of\_drivers](https://wiki.postgresql.org/wiki/List_of_drivers)
