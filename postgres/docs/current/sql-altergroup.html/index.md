---
title: "PostgreSQL: Documentation: 18: ALTER GROUP"
source: "https://www.postgresql.org/docs/current/sql-altergroup.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-altergroup.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:43.864Z"
content_hash: "9a3149877160ff8f835860e90491893eb1779e9fcdb43e53b22f1e877d571e37"
menu_path: ["PostgreSQL: Documentation: 18: ALTER GROUP"]
section_path: []
nav_prev: {"path": "postgres/docs/current/spi-spi-getrelname.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_getrelname"}
nav_next: {"path": "postgres/docs/current/rules-triggers.html/index.md", "title": "PostgreSQL: Documentation: 18: 39.7.\u00a0Rules Versus Triggers"}
---

ALTER GROUP — change role name or membership

## Synopsis

ALTER GROUP _`role_specification`_ ADD USER _`user_name`_ \[, ... \]
ALTER GROUP _`role_specification`_ DROP USER _`user_name`_ \[, ... \]

where _`role_specification`_ can be:

    _`role_name`_
  | CURRENT\_ROLE
  | CURRENT\_USER
  | SESSION\_USER

ALTER GROUP _`group_name`_ RENAME TO _`new_name`_

## Description

`ALTER GROUP` changes the attributes of a user group. This is an obsolete command, though still accepted for backwards compatibility, because groups (and users too) have been superseded by the more general concept of roles.

The first two variants add users to a group or remove them from a group. (Any role can play the part of either a “user” or a “group” for this purpose.) These variants are effectively equivalent to granting or revoking membership in the role named as the “group”; so the preferred way to do this is to use [`GRANT`](https://www.postgresql.org/docs/current/sql-grant.html "GRANT") or [`REVOKE`](https://www.postgresql.org/docs/current/sql-revoke.html "REVOKE"). Note that `GRANT` and `REVOKE` have additional options which are not available with this command, such as the ability to grant and revoke `ADMIN OPTION`, and the ability to specify the grantor.

The third variant changes the name of the group. This is exactly equivalent to renaming the role with [`ALTER ROLE`](https://www.postgresql.org/docs/current/sql-alterrole.html "ALTER ROLE").

## Parameters

_`group_name`_

The name of the group (role) to modify.

_`user_name`_

Users (roles) that are to be added to or removed from the group. The users must already exist; `ALTER GROUP` does not create or drop users.

_`new_name`_

The new name of the group.

## Examples

Add users to a group:

ALTER GROUP staff ADD USER karl, john;

Remove a user from a group:

ALTER GROUP workers DROP USER beth;

## Compatibility

There is no `ALTER GROUP` statement in the SQL standard.
