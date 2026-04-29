---
title: "PostgreSQL: Documentation: 18: REASSIGN OWNED"
source: "https://www.postgresql.org/docs/current/sql-reassign-owned.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-reassign-owned.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:49.543Z"
content_hash: "ba60872e1929dc0420c09c3f58f738704ff25e2cae42efd72a2fce5879386629"
menu_path: ["PostgreSQL: Documentation: 18: REASSIGN OWNED"]
section_path: []
nav_prev: {"path": "../sql-prepare.html/index.md", "title": "PostgreSQL: Documentation: 18: PREPARE"}
nav_next: {"path": "../sql-refreshmaterializedview.html/index.md", "title": "PostgreSQL: Documentation: 18: REFRESH MATERIALIZED VIEW"}
---

REASSIGN OWNED — change the ownership of database objects owned by a database role

## Synopsis

REASSIGN OWNED BY { _`old_role`_ | CURRENT\_ROLE | CURRENT\_USER | SESSION\_USER } \[, ...\]
               TO { _`new_role`_ | CURRENT\_ROLE | CURRENT\_USER | SESSION\_USER }

## Description

`REASSIGN OWNED` instructs the system to change the ownership of database objects owned by any of the _`old_roles`_ to _`new_role`_.

## Parameters

_`old_role`_

The name of a role. The ownership of all the objects within the current database, and of all shared objects (databases, tablespaces), owned by this role will be reassigned to _`new_role`_.

_`new_role`_

The name of the role that will be made the new owner of the affected objects.

## Notes

`REASSIGN OWNED` is often used to prepare for the removal of one or more roles. Because `REASSIGN OWNED` does not affect objects within other databases, it is usually necessary to execute this command in each database that contains objects owned by a role that is to be removed.

`REASSIGN OWNED` requires membership on both the source role(s) and the target role.

The [`DROP OWNED`](https://www.postgresql.org/docs/current/sql-drop-owned.html "DROP OWNED") command is an alternative that simply drops all the database objects owned by one or more roles.

The `REASSIGN OWNED` command does not affect any privileges granted to the _`old_roles`_ on objects that are not owned by them. Likewise, it does not affect default privileges created with `ALTER DEFAULT PRIVILEGES`. Use `DROP OWNED` to revoke such privileges.

See [Section 21.4](https://www.postgresql.org/docs/current/role-removal.html "21.4. Dropping Roles") for more discussion.

## Compatibility

The `REASSIGN OWNED` command is a PostgreSQL extension.
