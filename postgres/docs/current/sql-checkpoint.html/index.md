---
title: "PostgreSQL: Documentation: 18: CHECKPOINT"
source: "https://www.postgresql.org/docs/current/sql-checkpoint.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-checkpoint.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:50.813Z"
content_hash: "4f1aae90fe8f8ad39f281a7878237316ecb25256698a2b36b8f618de0e92c342"
menu_path: ["PostgreSQL: Documentation: 18: CHECKPOINT"]
section_path: []
---
CHECKPOINT — force a write-ahead log checkpoint

## Synopsis

CHECKPOINT

## Description

A checkpoint is a point in the write-ahead log sequence at which all data files have been updated to reflect the information in the log. All data files will be flushed to disk. Refer to [Section 28.5](https://www.postgresql.org/docs/current/wal-configuration.html "28.5. WAL Configuration") for more details about what happens during a checkpoint.

The `CHECKPOINT` command forces an immediate checkpoint when the command is issued, without waiting for a regular checkpoint scheduled by the system (controlled by the settings in [Section 19.5.2](https://www.postgresql.org/docs/current/runtime-config-wal.html#RUNTIME-CONFIG-WAL-CHECKPOINTS "19.5.2. Checkpoints")). `CHECKPOINT` is not intended for use during normal operation.

If executed during recovery, the `CHECKPOINT` command will force a restartpoint (see [Section 28.5](https://www.postgresql.org/docs/current/wal-configuration.html "28.5. WAL Configuration")) rather than writing a new checkpoint.

Only superusers or users with the privileges of the [pg\_checkpoint](https://www.postgresql.org/docs/current/predefined-roles.html#PREDEFINED-ROLE-PG-CHECKPOINT) role can call `CHECKPOINT`.

## Compatibility

The `CHECKPOINT` command is a PostgreSQL language extension.
