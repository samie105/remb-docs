---
title: "PostgreSQL: Documentation: 18: O.1. recovery.conf file merged into postgresql.conf"
source: "https://www.postgresql.org/docs/current/recovery-config.html"
canonical_url: "https://www.postgresql.org/docs/current/recovery-config.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:03.279Z"
content_hash: "c64dca6a80ee8e2cd92af9c28c39ad730ac380590378cd41d1a3f923877c1604"
menu_path: ["PostgreSQL: Documentation: 18: O.1. recovery.conf file merged into postgresql.conf"]
section_path: []
nav_prev: {"path": "postgres/docs/current/rangetypes.html/index.md", "title": "PostgreSQL: Documentation: 18: 8.17.\u00a0Range Types"}
nav_next: {"path": "postgres/docs/current/regress-variant.html/index.md", "title": "PostgreSQL: Documentation: 18: 31.3.\u00a0Variant Comparison Files"}
---

PostgreSQL 11 and below used a configuration file named `recovery.conf` to manage replicas and standbys. Support for this file was removed in PostgreSQL 12. See [the release notes for PostgreSQL 12](https://www.postgresql.org/docs/current/release-prior.html "E.5. Prior Releases") for details on this change.

On PostgreSQL 12 and above, [archive recovery, streaming replication, and PITR](https://www.postgresql.org/docs/current/continuous-archiving.html "25.3. Continuous Archiving and Point-in-Time Recovery (PITR)") are configured using [normal server configuration parameters](https://www.postgresql.org/docs/current/runtime-config-replication.html#RUNTIME-CONFIG-REPLICATION-STANDBY "19.6.3. Standby Servers"). These are set in `postgresql.conf` or via [ALTER SYSTEM](https://www.postgresql.org/docs/current/sql-altersystem.html "ALTER SYSTEM") like any other parameter.

The server will not start if a `recovery.conf` exists.

PostgreSQL 15 and below had a setting `promote_trigger_file`, or `trigger_file` before 12. Use `pg_ctl promote` or call `pg_promote()` to promote a standby instead.

The `standby_mode` setting has been removed. A `standby.signal` file in the data directory is used instead. See [Standby Server Operation](https://www.postgresql.org/docs/current/warm-standby.html#STANDBY-SERVER-OPERATION "26.2.2. Standby Server Operation") for details.
