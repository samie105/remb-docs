---
title: "PostgreSQL: Documentation: 18: ALTER DEFAULT PRIVILEGES"
source: "https://www.postgresql.org/docs/current/sql-alterdefaultprivileges.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-alterdefaultprivileges.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:29.037Z"
content_hash: "94a4be5026b1efd47c27be0d84d0d3aa4d932f0c4a3c2ce9721b31b8b40973fa"
menu_path: ["PostgreSQL: Documentation: 18: ALTER DEFAULT PRIVILEGES"]
section_path: []
nav_prev: {"path": "postgres/docs/current/app-pgcontroldata.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_controldata"}
nav_next: {"path": "postgres/docs/current/event-trigger-table-rewrite-example.html/index.md", "title": "PostgreSQL: Documentation: 18: 38.4.\u00a0A Table Rewrite Event Trigger Example"}
---

ALTER DEFAULT PRIVILEGES — define default access privileges

## Synopsis

ALTER DEFAULT PRIVILEGES
    \[ FOR { ROLE | USER } _`target_role`_ \[, ...\] \]
    \[ IN SCHEMA _`schema_name`_ \[, ...\] \]
    _`abbreviated_grant_or_revoke`_

where _`abbreviated_grant_or_revoke`_ is one of:

GRANT { { SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | MAINTAIN }
    \[, ...\] | ALL \[ PRIVILEGES \] }
    ON TABLES
    TO { \[ GROUP \] _`role_name`_ | PUBLIC } \[, ...\] \[ WITH GRANT OPTION \]

GRANT { { USAGE | SELECT | UPDATE }
    \[, ...\] | ALL \[ PRIVILEGES \] }
    ON SEQUENCES
    TO { \[ GROUP \] _`role_name`_ | PUBLIC } \[, ...\] \[ WITH GRANT OPTION \]

GRANT { EXECUTE | ALL \[ PRIVILEGES \] }
    ON { FUNCTIONS | ROUTINES }
    TO { \[ GROUP \] _`role_name`_ | PUBLIC } \[, ...\] \[ WITH GRANT OPTION \]

GRANT { USAGE | ALL \[ PRIVILEGES \] }
    ON TYPES
    TO { \[ GROUP \] _`role_name`_ | PUBLIC } \[, ...\] \[ WITH GRANT OPTION \]

GRANT { { USAGE | CREATE }
    \[, ...\] | ALL \[ PRIVILEGES \] }
    ON SCHEMAS
    TO { \[ GROUP \] _`role_name`_ | PUBLIC } \[, ...\] \[ WITH GRANT OPTION \]

GRANT { { SELECT | UPDATE }
    \[, ...\] | ALL \[ PRIVILEGES \] }
    ON LARGE OBJECTS
    TO { \[ GROUP \] _`role_name`_ | PUBLIC } \[, ...\] \[ WITH GRANT OPTION \]

REVOKE \[ GRANT OPTION FOR \]
    { { SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | MAINTAIN }
    \[, ...\] | ALL \[ PRIVILEGES \] }
    ON TABLES
    FROM { \[ GROUP \] _`role_name`_ | PUBLIC } \[, ...\]
    \[ CASCADE | RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]
    { { USAGE | SELECT | UPDATE }
    \[, ...\] | ALL \[ PRIVILEGES \] }
    ON SEQUENCES
    FROM { \[ GROUP \] _`role_name`_ | PUBLIC } \[, ...\]
    \[ CASCADE | RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]
    { EXECUTE | ALL \[ PRIVILEGES \] }
    ON { FUNCTIONS | ROUTINES }
    FROM { \[ GROUP \] _`role_name`_ | PUBLIC } \[, ...\]
    \[ CASCADE | RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]
    { USAGE | ALL \[ PRIVILEGES \] }
    ON TYPES
    FROM { \[ GROUP \] _`role_name`_ | PUBLIC } \[, ...\]
    \[ CASCADE | RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]
    { { USAGE | CREATE }
    \[, ...\] | ALL \[ PRIVILEGES \] }
    ON SCHEMAS
    FROM { \[ GROUP \] _`role_name`_ | PUBLIC } \[, ...\]
    \[ CASCADE | RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]
    { { SELECT | UPDATE }
    \[, ...\] | ALL \[ PRIVILEGES \] }
    ON LARGE OBJECTS
    FROM { \[ GROUP \] _`role_name`_ | PUBLIC } \[, ...\]
    \[ CASCADE | RESTRICT \]

## Description

`ALTER DEFAULT PRIVILEGES` allows you to set the privileges that will be applied to objects created in the future. (It does not affect privileges assigned to already-existing objects.) Privileges can be set globally (i.e., for all objects created in the current database), or just for objects created in specified schemas.

While you can change your own default privileges and the defaults of roles that you are a member of, at object creation time, new object permissions are only affected by the default privileges of the current role, and are not inherited from any roles in which the current role is a member.

As explained in [Section 5.8](https://www.postgresql.org/docs/current/ddl-priv.html "5.8. Privileges"), the default privileges for any object type normally grant all grantable permissions to the object owner, and may grant some privileges to `PUBLIC` as well. However, this behavior can be changed by altering the global default privileges with `ALTER DEFAULT PRIVILEGES`.

Currently, only the privileges for schemas, tables (including views and foreign tables), sequences, functions, types (including domains), and large objects can be altered. For this command, functions include aggregates and procedures. The words `FUNCTIONS` and `ROUTINES` are equivalent in this command. (`ROUTINES` is preferred going forward as the standard term for functions and procedures taken together. In earlier PostgreSQL releases, only the word `FUNCTIONS` was allowed. It is not possible to set default privileges for functions and procedures separately.)

Default privileges that are specified per-schema are added to whatever the global default privileges are for the particular object type. This means you cannot revoke privileges per-schema if they are granted globally (either by default, or according to a previous `ALTER DEFAULT PRIVILEGES` command that did not specify a schema). Per-schema `REVOKE` is only useful to reverse the effects of a previous per-schema `GRANT`.

### Parameters

_`target_role`_

Change default privileges for objects created by the _`target_role`_, or the current role if unspecified.

_`schema_name`_

The name of an existing schema. If specified, the default privileges are altered for objects later created in that schema. If `IN SCHEMA` is omitted, the global default privileges are altered. `IN SCHEMA` is not allowed when setting privileges for schemas and large objects, since schemas can't be nested and large objects don't belong to a schema.

_`role_name`_

The name of an existing role to grant or revoke privileges for. This parameter, and all the other parameters in _`abbreviated_grant_or_revoke`_, act as described under [GRANT](https://www.postgresql.org/docs/current/sql-grant.html "GRANT") or [REVOKE](https://www.postgresql.org/docs/current/sql-revoke.html "REVOKE"), except that one is setting permissions for a whole class of objects rather than specific named objects.

## Notes

Use [psql](https://www.postgresql.org/docs/current/app-psql.html "psql")'s `\ddp` command to obtain information about existing assignments of default privileges. The meaning of the privilege display is the same as explained for `\dp` in [Section 5.8](https://www.postgresql.org/docs/current/ddl-priv.html "5.8. Privileges").

If you wish to drop a role for which the default privileges have been altered, it is necessary to reverse the changes in its default privileges or use `DROP OWNED BY` to get rid of the default privileges entry for the role.

## Examples

Grant SELECT privilege to everyone for all tables (and views) you subsequently create in schema `myschema`, and allow role `webuser` to INSERT into them too:

ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT SELECT ON TABLES TO PUBLIC;
ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT INSERT ON TABLES TO webuser;

Undo the above, so that subsequently-created tables won't have any more permissions than normal:

ALTER DEFAULT PRIVILEGES IN SCHEMA myschema REVOKE SELECT ON TABLES FROM PUBLIC;
ALTER DEFAULT PRIVILEGES IN SCHEMA myschema REVOKE INSERT ON TABLES FROM webuser;

Remove the public EXECUTE permission that is normally granted on functions, for all functions subsequently created by role `admin`:

ALTER DEFAULT PRIVILEGES FOR ROLE admin REVOKE EXECUTE ON FUNCTIONS FROM PUBLIC;

Note however that you _cannot_ accomplish that effect with a command limited to a single schema. This command has no effect, unless it is undoing a matching `GRANT`:

ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE EXECUTE ON FUNCTIONS FROM PUBLIC;

That's because per-schema default privileges can only add privileges to the global setting, not remove privileges granted by it.

## Compatibility

There is no `ALTER DEFAULT PRIVILEGES` statement in the SQL standard.

