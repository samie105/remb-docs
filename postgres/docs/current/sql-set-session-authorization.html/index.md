---
title: "PostgreSQL: Documentation: 18: SET SESSION AUTHORIZATION"
source: "https://www.postgresql.org/docs/current/sql-set-session-authorization.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-set-session-authorization.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:07.947Z"
content_hash: "3d07d67e4f1f091064dd569d793b069e59cc1d266fea50b771043a1c5c2d4550"
menu_path: ["PostgreSQL: Documentation: 18: SET SESSION AUTHORIZATION"]
section_path: []
nav_prev: {"path": "../sql-set-role.html/index.md", "title": "PostgreSQL: Documentation: 18: SET ROLE"}
nav_next: {"path": "../sql-set-transaction.html/index.md", "title": "PostgreSQL: Documentation: 18: SET TRANSACTION"}
---

SET SESSION AUTHORIZATION — set the session user identifier and the current user identifier of the current session

## Synopsis

SET \[ SESSION | LOCAL \] SESSION AUTHORIZATION _`user_name`_
SET \[ SESSION | LOCAL \] SESSION AUTHORIZATION DEFAULT
RESET SESSION AUTHORIZATION

## Description

This command sets the session user identifier and the current user identifier of the current SQL session to be _`user_name`_. The user name can be written as either an identifier or a string literal. Using this command, it is possible, for example, to temporarily become an unprivileged user and later switch back to being a superuser.

The session user identifier is initially set to be the (possibly authenticated) user name provided by the client. The current user identifier is normally equal to the session user identifier, but might change temporarily in the context of `SECURITY DEFINER` functions and similar mechanisms; it can also be changed by [`SET ROLE`](https://www.postgresql.org/docs/current/sql-set-role.html "SET ROLE"). The current user identifier is relevant for permission checking.

The session user identifier can be changed only if the initial session user (the _authenticated user_) has the superuser privilege. Otherwise, the command is accepted only if it specifies the authenticated user name.

The `SESSION` and `LOCAL` modifiers act the same as for the regular [`SET`](https://www.postgresql.org/docs/current/sql-set.html "SET") command.

The `DEFAULT` and `RESET` forms reset the session and current user identifiers to be the originally authenticated user name. These forms can be executed by any user.

## Notes

`SET SESSION AUTHORIZATION` cannot be used within a `SECURITY DEFINER` function.

## Examples

SELECT SESSION\_USER, CURRENT\_USER;

 session\_user | current\_user
--------------+--------------
 peter        | peter

SET SESSION AUTHORIZATION 'paul';

SELECT SESSION\_USER, CURRENT\_USER;

 session\_user | current\_user
--------------+--------------
 paul         | paul

## Compatibility

The SQL standard allows some other expressions to appear in place of the literal _`user_name`_, but these options are not important in practice. PostgreSQL allows identifier syntax (``"_`username`_"``), which SQL does not. SQL does not allow this command during a transaction; PostgreSQL does not make this restriction because there is no reason to. The `SESSION` and `LOCAL` modifiers are a PostgreSQL extension, as is the `RESET` syntax.

The privileges necessary to execute this command are left implementation-defined by the standard.
