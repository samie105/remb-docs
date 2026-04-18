---
title: "PostgreSQL: Documentation: 18: 47.10. Two-phase Commit Support for Logical Decoding"
source: "https://www.postgresql.org/docs/current/logicaldecoding-two-phase-commits.html"
canonical_url: "https://www.postgresql.org/docs/current/logicaldecoding-two-phase-commits.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:06.801Z"
content_hash: "8b56eae60744aaa66ca1b44fe215b839c2bc1826fc1d480a260f43799c666d2e"
menu_path: ["PostgreSQL: Documentation: 18: 47.10. Two-phase Commit Support for Logical Decoding"]
section_path: []
nav_prev: {"path": "postgres/docs/current/view-pg-timezone-names.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.34.\u00a0pg_timezone_names"}
nav_next: {"path": "postgres/docs/current/sql-listen.html/index.md", "title": "PostgreSQL: Documentation: 18: LISTEN"}
---

With the basic output plugin callbacks (eg., `begin_cb`, `change_cb`, `commit_cb` and `message_cb`) two-phase commit commands like `PREPARE TRANSACTION`, `COMMIT PREPARED` and `ROLLBACK PREPARED` are not decoded. While the `PREPARE TRANSACTION` is ignored, `COMMIT PREPARED` is decoded as a `COMMIT` and `ROLLBACK PREPARED` is decoded as a `ROLLBACK`.

To support the streaming of two-phase commands, an output plugin needs to provide additional callbacks. There are multiple two-phase commit callbacks that are required, (`begin_prepare_cb`, `prepare_cb`, `commit_prepared_cb`, `rollback_prepared_cb` and `stream_prepare_cb`) and an optional callback (`filter_prepare_cb`).

If the output plugin callbacks for decoding two-phase commit commands are provided, then on `PREPARE TRANSACTION`, the changes of that transaction are decoded, passed to the output plugin, and the `prepare_cb` callback is invoked. This differs from the basic decoding setup where changes are only passed to the output plugin when a transaction is committed. The start of a prepared transaction is indicated by the `begin_prepare_cb` callback.

When a prepared transaction is rolled back using the `ROLLBACK PREPARED`, then the `rollback_prepared_cb` callback is invoked and when the prepared transaction is committed using `COMMIT PREPARED`, then the `commit_prepared_cb` callback is invoked.

Optionally the output plugin can define filtering rules via `filter_prepare_cb` to decode only specific transaction in two phases. This can be achieved by pattern matching on the _`gid`_ or via lookups using the _`xid`_.

The users that want to decode prepared transactions need to be careful about below mentioned points:

*   If the prepared transaction has locked \[user\] catalog tables exclusively then decoding prepare can block till the main transaction is committed.
    
*   The logical replication solution that builds distributed two phase commit using this feature can deadlock if the prepared transaction has locked \[user\] catalog tables exclusively. To avoid this users must refrain from having locks on catalog tables (e.g. explicit `LOCK` command) in such transactions. See [Section 47.8.2](https://www.postgresql.org/docs/current/logicaldecoding-synchronous.html#LOGICALDECODING-SYNCHRONOUS-CAVEATS "47.8.2. Caveats") for the details.
