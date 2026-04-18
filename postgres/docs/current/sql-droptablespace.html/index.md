---
title: "PostgreSQL: Documentation: 18: DROP TABLESPACE"
source: "https://www.postgresql.org/docs/current/sql-droptablespace.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-droptablespace.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:30.190Z"
content_hash: "8d9a21b0d02ff37a95c7b0d298f93d90e13773b47f6fc0edbf1e419ceafda953"
menu_path: ["PostgreSQL: Documentation: 18: DROP TABLESPACE"]
section_path: []
nav_prev: {"path": "postgres/docs/current/logicaldecoding-writer.html/index.md", "title": "PostgreSQL: Documentation: 18: 47.7.\u00a0Logical Decoding Output Writers"}
nav_next: {"path": "postgres/docs/current/sql-create-access-method.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE ACCESS METHOD"}
---

DROP TABLESPACE — remove a tablespace

## Synopsis

DROP TABLESPACE \[ IF EXISTS \] _`name`_

## Description

`DROP TABLESPACE` removes a tablespace from the system.

A tablespace can only be dropped by its owner or a superuser. The tablespace must be empty of all database objects before it can be dropped. It is possible that objects in other databases might still reside in the tablespace even if no objects in the current database are using the tablespace. Also, if the tablespace is listed in the [temp\_tablespaces](postgres/docs/current/runtime-config-client.html/index.md#GUC-TEMP-TABLESPACES) setting of any active session, the `DROP` might fail due to temporary files residing in the tablespace.

## Parameters

`IF EXISTS`

Do not throw an error if the tablespace does not exist. A notice is issued in this case.

_`name`_

The name of a tablespace.

## Notes

`DROP TABLESPACE` cannot be executed inside a transaction block.

## Examples

To remove tablespace `mystuff` from the system:

DROP TABLESPACE mystuff;

## Compatibility

`DROP TABLESPACE` is a PostgreSQL extension.
