---
title: "PostgreSQL: Documentation: 18: Chapter 61. Genetic Query Optimizer"
source: "https://www.postgresql.org/docs/current/geqo.html"
canonical_url: "https://www.postgresql.org/docs/current/geqo.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:15.011Z"
content_hash: "3e1f97b8dac0add9f9537b3da279e2ee0849ed37a0c71523ba2a28c674b7af4d"
menu_path: ["PostgreSQL: Documentation: 18: Chapter 61. Genetic Query Optimizer"]
section_path: []
nav_prev: {"path": "postgres/docs/current/source.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a055.\u00a0PostgreSQL Coding Conventions"}
nav_next: {"path": "postgres/docs/current/wal-for-extensions.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a064.\u00a0Write Ahead Logging for Extensions"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/geqo.html "PostgreSQL 18 - Chapter 61. Genetic Query Optimizer") ([18](/docs/18/geqo.html "PostgreSQL 18 - Chapter 61. Genetic Query Optimizer")) / [17](/docs/17/geqo.html "PostgreSQL 17 - Chapter 61. Genetic Query Optimizer") / [16](/docs/16/geqo.html "PostgreSQL 16 - Chapter 61. Genetic Query Optimizer") / [15](/docs/15/geqo.html "PostgreSQL 15 - Chapter 61. Genetic Query Optimizer") / [14](/docs/14/geqo.html "PostgreSQL 14 - Chapter 61. Genetic Query Optimizer")

Development Versions: [devel](/docs/devel/geqo.html "PostgreSQL devel - Chapter 61. Genetic Query Optimizer")

Unsupported versions: [13](/docs/13/geqo.html "PostgreSQL 13 - Chapter 61. Genetic Query Optimizer") / [12](/docs/12/geqo.html "PostgreSQL 12 - Chapter 61. Genetic Query Optimizer") / [11](/docs/11/geqo.html "PostgreSQL 11 - Chapter 61. Genetic Query Optimizer") / [10](/docs/10/geqo.html "PostgreSQL 10 - Chapter 61. Genetic Query Optimizer") / [9.6](/docs/9.6/geqo.html "PostgreSQL 9.6 - Chapter 61. Genetic Query Optimizer") / [9.5](/docs/9.5/geqo.html "PostgreSQL 9.5 - Chapter 61. Genetic Query Optimizer") / [9.4](/docs/9.4/geqo.html "PostgreSQL 9.4 - Chapter 61. Genetic Query Optimizer") / [9.3](/docs/9.3/geqo.html "PostgreSQL 9.3 - Chapter 61. Genetic Query Optimizer") / [9.2](/docs/9.2/geqo.html "PostgreSQL 9.2 - Chapter 61. Genetic Query Optimizer") / [9.1](/docs/9.1/geqo.html "PostgreSQL 9.1 - Chapter 61. Genetic Query Optimizer") / [9.0](/docs/9.0/geqo.html "PostgreSQL 9.0 - Chapter 61. Genetic Query Optimizer") / [8.4](/docs/8.4/geqo.html "PostgreSQL 8.4 - Chapter 61. Genetic Query Optimizer") / [8.3](/docs/8.3/geqo.html "PostgreSQL 8.3 - Chapter 61. Genetic Query Optimizer") / [8.2](/docs/8.2/geqo.html "PostgreSQL 8.2 - Chapter 61. Genetic Query Optimizer") / [8.1](/docs/8.1/geqo.html "PostgreSQL 8.1 - Chapter 61. Genetic Query Optimizer") / [8.0](/docs/8.0/geqo.html "PostgreSQL 8.0 - Chapter 61. Genetic Query Optimizer") / [7.4](/docs/7.4/geqo.html "PostgreSQL 7.4 - Chapter 61. Genetic Query Optimizer") / [7.3](/docs/7.3/geqo.html "PostgreSQL 7.3 - Chapter 61. Genetic Query Optimizer") / [7.2](/docs/7.2/geqo.html "PostgreSQL 7.2 - Chapter 61. Genetic Query Optimizer") / [7.1](/docs/7.1/geqo.html "PostgreSQL 7.1 - Chapter 61. Genetic Query Optimizer")

## Chapter 61. Genetic Query Optimizer

### Author

Written by Martin Utesch (`<[utesch@aut.tu-freiberg.de](mailto:utesch@aut.tu-freiberg.de)>`) for the Institute of Automatic Control at the University of Mining and Technology in Freiberg, Germany.

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/geqo.html/) to report a documentation issue.


