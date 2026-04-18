---
title: "PostgreSQL: Documentation: 18: dblink_connect_u"
source: "https://www.postgresql.org/docs/current/contrib-dblink-connect-u.html"
canonical_url: "https://www.postgresql.org/docs/current/contrib-dblink-connect-u.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:43.052Z"
content_hash: "2499f0e36865bb700cf19a9b2e59c127d6d87f08e4d0ee72559f76279c3d710e"
menu_path: ["PostgreSQL: Documentation: 18: dblink_connect_u"]
section_path: []
nav_prev: {"path": "postgres/docs/current/ddl-identity-columns.html/index.md", "title": "PostgreSQL: Documentation: 18: 5.3.\u00a0Identity Columns"}
nav_next: {"path": "postgres/docs/current/bloom.html/index.md", "title": "PostgreSQL: Documentation: 18: F.6.\u00a0bloom \u2014 bloom filter index access method"}
---

dblink\_connect\_u — opens a persistent connection to a remote database, insecurely

## Synopsis

dblink\_connect\_u(text connstr) returns text
dblink\_connect\_u(text connname, text connstr) returns text

## Description

`dblink_connect_u()` is identical to `dblink_connect()`, except that it will allow non-superusers to connect using any authentication method.

If the remote server selects an authentication method that does not involve a password, then impersonation and subsequent escalation of privileges can occur, because the session will appear to have originated from the user as which the local PostgreSQL server runs. Also, even if the remote server does demand a password, it is possible for the password to be supplied from the server environment, such as a `~/.pgpass` file belonging to the server's user. This opens not only a risk of impersonation, but the possibility of exposing a password to an untrustworthy remote server. Therefore, `dblink_connect_u()` is initially installed with all privileges revoked from `PUBLIC`, making it un-callable except by superusers. In some situations it may be appropriate to grant `EXECUTE` permission for `dblink_connect_u()` to specific users who are considered trustworthy, but this should be done with care. It is also recommended that any `~/.pgpass` file belonging to the server's user _not_ contain any records specifying a wildcard host name.

For further details see `dblink_connect()`.


