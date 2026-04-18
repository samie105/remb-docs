---
title: "PostgreSQL: Documentation: 18: F.24. passwordcheck — verify password strength"
source: "https://www.postgresql.org/docs/current/passwordcheck.html"
canonical_url: "https://www.postgresql.org/docs/current/passwordcheck.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:47.905Z"
content_hash: "2453b2142f36dafa159e3a4ab9e9ee75fab68e02d65e31164dc42e132917b37e"
menu_path: ["PostgreSQL: Documentation: 18: F.24. passwordcheck — verify password strength"]
section_path: []
nav_prev: {"path": "postgres/docs/current/parser-stage.html/index.md", "title": "PostgreSQL: Documentation: 18: 51.3.\u00a0The Parser Stage"}
nav_next: {"path": "postgres/docs/current/perm-functions.html/index.md", "title": "PostgreSQL: Documentation: 18: 21.6.\u00a0Function Security"}
---

The `passwordcheck` module checks users' passwords whenever they are set with [CREATE ROLE](https://www.postgresql.org/docs/current/sql-createrole.html "CREATE ROLE") or [ALTER ROLE](https://www.postgresql.org/docs/current/sql-alterrole.html "ALTER ROLE"). If a password is considered too weak, it will be rejected and the command will terminate with an error.

To enable this module, add `'$libdir/passwordcheck'` to [shared\_preload\_libraries](postgres/docs/current/runtime-config-client.html/index.md#GUC-SHARED-PRELOAD-LIBRARIES) in `postgresql.conf`, then restart the server.

You can adapt this module to your needs by changing the source code. For example, you can use [CrackLib](https://github.com/cracklib/cracklib) to check passwords — this only requires uncommenting two lines in the `Makefile` and rebuilding the module. (We cannot include CrackLib by default for license reasons.) Without CrackLib, the module enforces a few simple rules for password strength, which you can modify or extend as you see fit.

### Caution

To prevent unencrypted passwords from being sent across the network, written to the server log or otherwise stolen by a database administrator, PostgreSQL allows the user to supply pre-encrypted passwords. Many client programs make use of this functionality and encrypt the password before sending it to the server.

This limits the usefulness of the `passwordcheck` module, because in that case it can only try to guess the password. For this reason, `passwordcheck` is not recommended if your security requirements are high. It is more secure to use an external authentication method such as GSSAPI (see [Chapter 20](https://www.postgresql.org/docs/current/client-authentication.html "Chapter 20. Client Authentication")) than to rely on passwords within the database.

Alternatively, you could modify `passwordcheck` to reject pre-encrypted passwords, but forcing users to set their passwords in clear text carries its own security risks.

### F.24.1. Configuration Parameters [#](#PASSWORDCHECK-CONFIGURATION-PARAMETERS)

`passwordcheck.min_password_length` (`integer`)

The minimum acceptable password length in bytes. The default is 8. Only superusers can change this setting.

### Note

This parameter has no effect if a user supplies a pre-encrypted password.

In ordinary usage, this parameter is set in `postgresql.conf`, but superusers can alter it on-the-fly within their own sessions. Typical usage might be:

\# postgresql.conf
passwordcheck.min\_password\_length = 12
