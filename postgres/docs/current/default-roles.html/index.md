---
title: "PostgreSQL: Documentation: 18: O.2. Default Roles Renamed to Predefined Roles"
source: "https://www.postgresql.org/docs/current/default-roles.html"
canonical_url: "https://www.postgresql.org/docs/current/default-roles.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:42:54.391Z"
content_hash: "d047d14d596cdf33b668d2334a7f99ce3c419d948ccfb2f22d534ac05b3c3c1f"
menu_path: ["PostgreSQL: Documentation: 18: O.2. Default Roles Renamed to Predefined Roles"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/ddl-system-columns.html/index.md", "title": "PostgreSQL: Documentation: 18: 5.6.\u00a0System Columns"}
nav_next: {"path": "postgres/docs/current/dict-int.html/index.md", "title": "PostgreSQL: Documentation: 18: F.12.\u00a0dict_int \u2014 example full-text search dictionary for integers"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/default-roles.html "PostgreSQL devel - O.2. Default Roles Renamed to Predefined Roles")

| O.2. Default Roles Renamed to Predefined Roles |
| --- |
| [Prev](https://www.postgresql.org/docs/current/recovery-config.html "O.1. recovery.conf file merged into postgresql.conf")  | [Up](https://www.postgresql.org/docs/current/appendix-obsolete.html "Appendix O. Obsolete or Renamed Features") | Appendix O. Obsolete or Renamed Features | [Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation") |  [Next](https://www.postgresql.org/docs/current/pgxlogdump.html "O.3. pg_xlogdump renamed to pg_waldump") |

* * *

PostgreSQL 13 and below used the term “Default Roles”. However, as these roles are not able to actually be changed and are installed as part of the system at initialization time, the more appropriate term to use is “Predefined Roles”. See [Section 21.5](https://www.postgresql.org/docs/current/predefined-roles.html "21.5. Predefined Roles") for current documentation regarding Predefined Roles, and [the release notes for PostgreSQL 14](https://www.postgresql.org/docs/current/release-prior.html "E.5. Prior Releases") for details on this change.

* * *

<table summary="Navigation footer"><tbody><tr><td><a accesskey="p" href="https://www.postgresql.org/docs/current/recovery-config.html" title="O.1.&nbsp;recovery.conf file merged into postgresql.conf">Prev</a>&nbsp;</td><td><a accesskey="u" href="https://www.postgresql.org/docs/current/appendix-obsolete.html" title="Appendix&nbsp;O.&nbsp;Obsolete or Renamed Features">Up</a></td><td>&nbsp;<a accesskey="n" href="https://www.postgresql.org/docs/current/pgxlogdump.html" title="O.3.&nbsp;pg_xlogdump renamed to pg_waldump">Next</a></td></tr><tr><td>O.1.&nbsp;<code>recovery.conf</code> file merged into <code>postgresql.conf</code>&nbsp;</td><td><a accesskey="h" href="https://www.postgresql.org/docs/current/index.html" title="PostgreSQL 18.3 Documentation">Home</a></td><td>&nbsp;O.3.&nbsp;<code>pg_xlogdump</code> renamed to <code>pg_waldump</code></td></tr></tbody></table>

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](https://www.postgresql.org/account/comments/new/18/default-roles.html/) to report a documentation issue.
