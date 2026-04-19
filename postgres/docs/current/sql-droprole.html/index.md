---
title: "PostgreSQL: Documentation: 18: DROP ROLE"
source: "https://www.postgresql.org/docs/current/sql-droprole.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-droprole.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:56.267Z"
content_hash: "136787bb7c33c51032e6b3d8ec0f6e72e22ab593c61ae1456f90d0c4c7fa116e"
menu_path: ["PostgreSQL: Documentation: 18: DROP ROLE"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-dropprocedure.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP PROCEDURE"}
nav_next: {"path": "postgres/docs/current/sql-droprule.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP RULE"}
---

DROP ROLE — remove a database role

## Synopsis

DROP ROLE \[ IF EXISTS \] _`name`_ \[, ...\]

## Description

`DROP ROLE` removes the specified role(s). To drop a superuser role, you must be a superuser yourself; to drop non-superuser roles, you must have `CREATEROLE` privilege and have been granted `ADMIN OPTION` on the role.

A role cannot be removed if it is still referenced in any database of the cluster; an error will be raised if so. Before dropping the role, you must drop all the objects it owns (or reassign their ownership) and revoke any privileges the role has been granted on other objects. The [`REASSIGN OWNED`](https://www.postgresql.org/docs/current/sql-reassign-owned.html "REASSIGN OWNED") and [`DROP OWNED`](https://www.postgresql.org/docs/current/sql-drop-owned.html "DROP OWNED") commands can be useful for this purpose; see [Section 21.4](https://www.postgresql.org/docs/current/role-removal.html "21.4. Dropping Roles") for more discussion.

However, it is not necessary to remove role memberships involving the role; `DROP ROLE` automatically revokes any memberships of the target role in other roles, and of other roles in the target role. The other roles are not dropped nor otherwise affected.

## Parameters

`IF EXISTS`

Do not throw an error if the role does not exist. A notice is issued in this case.

_`name`_

The name of the role to remove.

## Notes

PostgreSQL includes a program [dropuser](https://www.postgresql.org/docs/current/app-dropuser.html "dropuser") that has the same functionality as this command (in fact, it calls this command) but can be run from the command shell.

## Examples

To drop a role:

DROP ROLE jonathan;

## Compatibility

The SQL standard defines `DROP ROLE`, but it allows only one role to be dropped at a time, and it specifies different privilege requirements than PostgreSQL uses.
