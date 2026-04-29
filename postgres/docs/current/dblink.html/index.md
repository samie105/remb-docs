---
title: "PostgreSQL: Documentation: 18: F.11. dblink — connect to other PostgreSQL databases"
source: "https://www.postgresql.org/docs/current/dblink.html"
canonical_url: "https://www.postgresql.org/docs/current/dblink.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:58.080Z"
content_hash: "e1455aef7bd7642652f44380288b8eb1123fd80e18e5b8e3dc413c27a93c17c9"
menu_path: ["PostgreSQL: Documentation: 18: F.11. dblink — connect to other PostgreSQL databases"]
section_path: []
nav_prev: {"path": "postgres/docs/current/datetime-units-history.html/index.md", "title": "PostgreSQL: Documentation: 18: B.6.\u00a0History of Units"}
nav_next: {"path": "postgres/docs/current/ddl-alter.html/index.md", "title": "PostgreSQL: Documentation: 18: 5.7.\u00a0Modifying Tables"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/dblink.html "PostgreSQL 18 - F.11. dblink — connect to other PostgreSQL databases") ([18](/docs/18/dblink.html "PostgreSQL 18 - F.11. dblink — connect to other PostgreSQL databases")) / [17](/docs/17/dblink.html "PostgreSQL 17 - F.11. dblink — connect to other PostgreSQL databases") / [16](/docs/16/dblink.html "PostgreSQL 16 - F.11. dblink — connect to other PostgreSQL databases") / [15](/docs/15/dblink.html "PostgreSQL 15 - F.11. dblink — connect to other PostgreSQL databases") / [14](/docs/14/dblink.html "PostgreSQL 14 - F.11. dblink — connect to other PostgreSQL databases")

Development Versions: [devel](/docs/devel/dblink.html "PostgreSQL devel - F.11. dblink — connect to other PostgreSQL databases")

Unsupported versions: [13](/docs/13/dblink.html "PostgreSQL 13 - F.11. dblink — connect to other PostgreSQL databases") / [12](/docs/12/dblink.html "PostgreSQL 12 - F.11. dblink — connect to other PostgreSQL databases") / [11](/docs/11/dblink.html "PostgreSQL 11 - F.11. dblink — connect to other PostgreSQL databases") / [10](/docs/10/dblink.html "PostgreSQL 10 - F.11. dblink — connect to other PostgreSQL databases") / [9.6](/docs/9.6/dblink.html "PostgreSQL 9.6 - F.11. dblink — connect to other PostgreSQL databases") / [9.5](/docs/9.5/dblink.html "PostgreSQL 9.5 - F.11. dblink — connect to other PostgreSQL databases") / [9.4](/docs/9.4/dblink.html "PostgreSQL 9.4 - F.11. dblink — connect to other PostgreSQL databases") / [9.3](/docs/9.3/dblink.html "PostgreSQL 9.3 - F.11. dblink — connect to other PostgreSQL databases") / [9.2](/docs/9.2/dblink.html "PostgreSQL 9.2 - F.11. dblink — connect to other PostgreSQL databases") / [9.1](/docs/9.1/dblink.html "PostgreSQL 9.1 - F.11. dblink — connect to other PostgreSQL databases") / [9.0](/docs/9.0/dblink.html "PostgreSQL 9.0 - F.11. dblink — connect to other PostgreSQL databases") / [8.4](/docs/8.4/dblink.html "PostgreSQL 8.4 - F.11. dblink — connect to other PostgreSQL databases") / [8.3](/docs/8.3/dblink.html "PostgreSQL 8.3 - F.11. dblink — connect to other PostgreSQL databases")

## F.11. dblink — connect to other PostgreSQL databases [#](#DBLINK)

`dblink` is a module that supports connections to other PostgreSQL databases from within a database session.

`dblink` can report the following wait events under the wait event type `Extension`.

`DblinkConnect`

Waiting to establish a connection to a remote server.

`DblinkGetConnect`

Waiting to establish a connection to a remote server when it could not be found in the list of already-opened connections.

`DblinkGetResult`

Waiting to receive the results of a query from a remote server.

See also [postgres\_fdw](postgres-fdw.html "F.38. postgres_fdw — access data stored in external PostgreSQL servers"), which provides roughly the same functionality using a more modern and standards-compliant infrastructure.

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/dblink.html/) to report a documentation issue.
