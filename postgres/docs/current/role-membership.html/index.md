---
title: "PostgreSQL: Documentation: 18: 21.3. Role Membership"
source: "https://www.postgresql.org/docs/current/role-membership.html"
canonical_url: "https://www.postgresql.org/docs/current/role-membership.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:16.781Z"
content_hash: "86882d317efe1b9041b3e644775c10878126b2e82c2393f89ddf3c232af4fb1c"
menu_path: ["PostgreSQL: Documentation: 18: 21.3. Role Membership"]
section_path: []
nav_prev: {"path": "../release-prior.html/index.md", "title": "PostgreSQL: Documentation: 18: E.5.\u00a0Prior Releases"}
nav_next: {"path": "../role-removal.html/index.md", "title": "PostgreSQL: Documentation: 18: 21.4.\u00a0Dropping Roles"}
---

It is frequently convenient to group users together to ease management of privileges: that way, privileges can be granted to, or revoked from, a group as a whole. In PostgreSQL this is done by creating a role that represents the group, and then granting _membership_ in the group role to individual user roles.

To set up a group role, first create the role:

CREATE ROLE _`name`_;

Typically a role being used as a group would not have the `LOGIN` attribute, though you can set it if you wish.

Once the group role exists, you can add and remove members using the [`GRANT`](https://www.postgresql.org/docs/current/sql-grant.html "GRANT") and [`REVOKE`](https://www.postgresql.org/docs/current/sql-revoke.html "REVOKE") commands:

GRANT _`group_role`_ TO _`role1`_, ... ;
REVOKE _`group_role`_ FROM _`role1`_, ... ;

You can grant membership to other group roles, too (since there isn't really any distinction between group roles and non-group roles). The database will not let you set up circular membership loops. Also, it is not permitted to grant membership in a role to `PUBLIC`.

The members of a group role can use the privileges of the role in two ways. First, member roles that have been granted membership with the `SET` option can do [`SET ROLE`](https://www.postgresql.org/docs/current/sql-set-role.html "SET ROLE") to temporarily “become” the group role. In this state, the database session has access to the privileges of the group role rather than the original login role, and any database objects created are considered owned by the group role, not the login role. Second, member roles that have been granted membership with the `INHERIT` option automatically have use of the privileges of those directly or indirectly a member of, though the chain stops at memberships lacking the inherit option. As an example, suppose we have done:

CREATE ROLE joe LOGIN;
CREATE ROLE admin;
CREATE ROLE wheel;
CREATE ROLE island;
GRANT admin TO joe WITH INHERIT TRUE;
GRANT wheel TO admin WITH INHERIT FALSE;
GRANT island TO joe WITH INHERIT TRUE, SET FALSE;

Immediately after connecting as role `joe`, a database session will have use of privileges granted directly to `joe` plus any privileges granted to `admin` and `island`, because `joe` “inherits” those privileges. However, privileges granted to `wheel` are not available, because even though `joe` is indirectly a member of `wheel`, the membership is via `admin` which was granted using `WITH INHERIT FALSE`. After:

SET ROLE admin;

the session would have use of only those privileges granted to `admin`, and not those granted to `joe` or `island`. After:

SET ROLE wheel;

the session would have use of only those privileges granted to `wheel`, and not those granted to either `joe` or `admin`. The original privilege state can be restored with any of:

SET ROLE joe;
SET ROLE NONE;
RESET ROLE;

### Note

The `SET ROLE` command always allows selecting any role that the original login role is directly or indirectly a member of, provided that there is a chain of membership grants each of which has `SET TRUE` (which is the default). Thus, in the above example, it is not necessary to become `admin` before becoming `wheel`. On the other hand, it is not possible to become `island` at all; `joe` can only access those privileges via inheritance.

### Note

In the SQL standard, there is a clear distinction between users and roles, and users do not automatically inherit privileges while roles do. This behavior can be obtained in PostgreSQL by giving roles being used as SQL roles the `INHERIT` attribute, while giving roles being used as SQL users the `NOINHERIT` attribute. However, PostgreSQL defaults to giving all roles the `INHERIT` attribute, for backward compatibility with pre-8.1 releases in which users always had use of permissions granted to groups they were members of.

The role attributes `LOGIN`, `SUPERUSER`, `CREATEDB`, and `CREATEROLE` can be thought of as special privileges, but they are never inherited as ordinary privileges on database objects are. You must actually `SET ROLE` to a specific role having one of these attributes in order to make use of the attribute. Continuing the above example, we might choose to grant `CREATEDB` and `CREATEROLE` to the `admin` role. Then a session connecting as role `joe` would not have these privileges immediately, only after doing `SET ROLE admin`.

To destroy a group role, use [`DROP ROLE`](https://www.postgresql.org/docs/current/sql-droprole.html "DROP ROLE"):

DROP ROLE _`name`_;

Any memberships in the group role are automatically revoked (but the member roles are not otherwise affected).
