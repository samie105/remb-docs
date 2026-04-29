---
title: "PostgreSQL: Documentation: 18: CHECKPOINT"
source: "https://www.postgresql.org/docs/current/sql-checkpoint.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-checkpoint.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:51:26.108Z"
content_hash: "2879916b0a2052089e66fdbe85ebc86a209ea14f0462a1e59b938369482f8a79"
menu_path: ["PostgreSQL: Documentation: 18: CHECKPOINT"]
section_path: []
content_language: "en"
nav_prev: {"path": "../sql-call.html/index.md", "title": "PostgreSQL: Documentation: 18: CALL"}
nav_next: {"path": "../sql-close.html/index.md", "title": "PostgreSQL: Documentation: 18: CLOSE"}
---

CHECKPOINT — force a write-ahead log checkpoint

## Description

A checkpoint is a point in the write-ahead log sequence at which all data files have been updated to reflect the information in the log. All data files will be flushed to disk. Refer to [Section 28.5](https://www.postgresql.org/docs/current/wal-configuration.html "28.5. WAL Configuration") for more details about what happens during a checkpoint.

The `CHECKPOINT` command forces an immediate checkpoint when the command is issued, without waiting for a regular checkpoint scheduled by the system (controlled by the settings in [Section 19.5.2](https://www.postgresql.org/docs/current/runtime-config-wal.html#RUNTIME-CONFIG-WAL-CHECKPOINTS "19.5.2. Checkpoints")). `CHECKPOINT` is not intended for use during normal operation.

If executed during recovery, the `CHECKPOINT` command will force a restartpoint (see [Section 28.5](https://www.postgresql.org/docs/current/wal-configuration.html "28.5. WAL Configuration")) rather than writing a new checkpoint.

Only superusers or users with the privileges of the [pg\_checkpoint](../predefined-roles.html/index.md#PREDEFINED-ROLE-PG-CHECKPOINT) role can call `CHECKPOINT`.

## Compatibility

The `CHECKPOINT` command is a PostgreSQL language extension.
