---
title: "PostgreSQL: Documentation: 18: 51.4. The PostgreSQL Rule System"
source: "https://www.postgresql.org/docs/current/rule-system.html"
canonical_url: "https://www.postgresql.org/docs/current/rule-system.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:48:50.657Z"
content_hash: "10bf06c210041d6942c6b3131069c2bea088b25bca432546479ff57be074974c"
menu_path: ["PostgreSQL: Documentation: 18: 51.4. The PostgreSQL Rule System"]
section_path: []
content_language: "en"
nav_prev: {"path": "../rowtypes.html/index.md", "title": "PostgreSQL: Documentation: 18: 8.16.\u00a0Composite Types"}
nav_next: {"path": "../rules-privileges.html/index.md", "title": "PostgreSQL: Documentation: 18: 39.5.\u00a0Rules and Privileges"}
---

PostgreSQL supports a powerful _rule system_ for the specification of _views_ and ambiguous _view updates_. Originally the PostgreSQL rule system consisted of two implementations:

-   The first one worked using _row level_ processing and was implemented deep in the _executor_. The rule system was called whenever an individual row had been accessed. This implementation was removed in 1995 when the last official release of the Berkeley Postgres project was transformed into Postgres95.
    
-   The second implementation of the rule system is a technique called _query rewriting_. The _rewrite system_ is a module that exists between the _parser stage_ and the _planner/optimizer_. This technique is still implemented.
    

The query rewriter is discussed in some detail in [Chapter 39](https://www.postgresql.org/docs/current/rules.html "Chapter 39. The Rule System"), so there is no need to cover it here. We will only point out that both the input and the output of the rewriter are query trees, that is, there is no change in the representation or level of semantic detail in the trees. Rewriting can be thought of as a form of macro expansion.
