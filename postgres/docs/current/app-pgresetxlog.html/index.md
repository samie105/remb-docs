---
title: "PostgreSQL: Documentation: 18: O.4. pg_resetxlog renamed to pg_resetwal"
source: "https://www.postgresql.org/docs/current/app-pgresetxlog.html"
canonical_url: "https://www.postgresql.org/docs/current/app-pgresetxlog.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:45:05.014Z"
content_hash: "f11a47937f7b91eef4343ef4fad2dff59b517fa60aaaff05a0772163b714abd5"
menu_path: ["PostgreSQL: Documentation: 18: O.4. pg_resetxlog renamed to pg_resetwal"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/app-pgresetwal.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_resetwal"}
nav_next: {"path": "postgres/docs/current/app-pgrestore.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_restore"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/app-pgresetxlog.html "PostgreSQL devel - O.4. pg_resetxlog renamed to pg_resetwal")

| O.4. `pg_resetxlog` renamed to `pg_resetwal` |
| --- |
| [Prev](https://www.postgresql.org/docs/current/pgxlogdump.html "O.3. pg_xlogdump renamed to pg_waldump")  | [Up](https://www.postgresql.org/docs/current/appendix-obsolete.html "Appendix O. Obsolete or Renamed Features") | Appendix O. Obsolete or Renamed Features | [Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation") |  [Next](https://www.postgresql.org/docs/current/app-pgreceivexlog.html "O.5. pg_receivexlog renamed to pg_receivewal") |

* * *

PostgreSQL 9.6 and below provided a command named `pg_resetxlog` to reset the write-ahead-log (WAL) files. This command was renamed to `pg_resetwal`, see [pg\_resetwal](https://www.postgresql.org/docs/current/app-pgresetwal.html "pg_resetwal") for documentation of `pg_resetwal` and see [the release notes for PostgreSQL 10](https://www.postgresql.org/docs/current/release-prior.html "E.5. Prior Releases") for details on this change.
