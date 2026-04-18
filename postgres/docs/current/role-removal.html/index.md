---
title: "PostgreSQL: Documentation: 18: 21.4. Dropping Roles"
source: "https://www.postgresql.org/docs/current/role-removal.html"
canonical_url: "https://www.postgresql.org/docs/current/role-removal.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:45.748Z"
content_hash: "1d939a031333fc9b01eb050fd1e1d6a42a921cae30f08dc42c8205d9810eeabe"
menu_path: ["PostgreSQL: Documentation: 18: 21.4. Dropping Roles"]
section_path: []
nav_prev: {"path": "postgres/docs/current/release-18-3.html/index.md", "title": "PostgreSQL: Documentation: 18: E.1.\u00a0Release 18.3"}
nav_next: {"path": "postgres/docs/current/ddl-foreign-data.html/index.md", "title": "PostgreSQL: Documentation: 18: 5.13.\u00a0Foreign Data"}
---

Because roles can own database objects and can hold privileges to access other objects, dropping a role is often not just a matter of a quick [`DROP ROLE`](https://www.postgresql.org/docs/current/sql-droprole.html "DROP ROLE"). Any objects owned by the role must first be dropped or reassigned to other owners; and any permissions granted to the role must be revoked.

Ownership of objects can be transferred one at a time using `ALTER` commands, for example:

ALTER TABLE bobs\_table OWNER TO alice;

Alternatively, the [`REASSIGN OWNED`](https://www.postgresql.org/docs/current/sql-reassign-owned.html "REASSIGN OWNED") command can be used to reassign ownership of all objects owned by the role-to-be-dropped to a single other role. Because `REASSIGN OWNED` cannot access objects in other databases, it is necessary to run it in each database that contains objects owned by the role. (Note that the first such `REASSIGN OWNED` will change the ownership of any shared-across-databases objects, that is databases or tablespaces, that are owned by the role-to-be-dropped.)

Once any valuable objects have been transferred to new owners, any remaining objects owned by the role-to-be-dropped can be dropped with the [`DROP OWNED`](https://www.postgresql.org/docs/current/sql-drop-owned.html "DROP OWNED") command. Again, this command cannot access objects in other databases, so it is necessary to run it in each database that contains objects owned by the role. Also, `DROP OWNED` will not drop entire databases or tablespaces, so it is necessary to do that manually if the role owns any databases or tablespaces that have not been transferred to new owners.

`DROP OWNED` also takes care of removing any privileges granted to the target role for objects that do not belong to it. Because `REASSIGN OWNED` does not touch such objects, it's typically necessary to run both `REASSIGN OWNED` and `DROP OWNED` (in that order!) to fully remove the dependencies of a role to be dropped.

In short then, the most general recipe for removing a role that has been used to own objects is:

REASSIGN OWNED BY doomed\_role TO successor\_role;
DROP OWNED BY doomed\_role;
-- repeat the above commands in each database of the cluster
DROP ROLE doomed\_role;

When not all owned objects are to be transferred to the same successor owner, it's best to handle the exceptions manually and then perform the above steps to mop up.

If `DROP ROLE` is attempted while dependent objects still remain, it will issue messages identifying which objects need to be reassigned or dropped.
