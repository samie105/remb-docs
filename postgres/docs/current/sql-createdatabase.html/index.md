---
title: "PostgreSQL: Documentation: 18: CREATE DATABASE"
source: "https://www.postgresql.org/docs/current/sql-createdatabase.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-createdatabase.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:48.416Z"
content_hash: "dc72bc932afa1ac9fc60ae2dff55029a5b3d5a1cf882884f6aa38446ee1b5e85"
menu_path: ["PostgreSQL: Documentation: 18: CREATE DATABASE"]
section_path: []
nav_prev: {"path": "../sql-createconversion.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE CONVERSION"}
nav_next: {"path": "../sql-createdomain.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE DOMAIN"}
---

CREATE DATABASE — create a new database

## Synopsis

CREATE DATABASE _`name`_
    \[ WITH \] \[ OWNER \[=\] _`user_name`_ \]
           \[ TEMPLATE \[=\] _`template`_ \]
           \[ ENCODING \[=\] _`encoding`_ \]
           \[ STRATEGY \[=\] _`strategy`_ \]
           \[ LOCALE \[=\] _`locale`_ \]
           \[ LC\_COLLATE \[=\] _`lc_collate`_ \]
           \[ LC\_CTYPE \[=\] _`lc_ctype`_ \]
           \[ BUILTIN\_LOCALE \[=\] _`builtin_locale`_ \]
           \[ ICU\_LOCALE \[=\] _`icu_locale`_ \]
           \[ ICU\_RULES \[=\] _`icu_rules`_ \]
           \[ LOCALE\_PROVIDER \[=\] _`locale_provider`_ \]
           \[ COLLATION\_VERSION = _`collation_version`_ \]
           \[ TABLESPACE \[=\] _`tablespace_name`_ \]
           \[ ALLOW\_CONNECTIONS \[=\] _`allowconn`_ \]
           \[ CONNECTION LIMIT \[=\] _`connlimit`_ \]
           \[ IS\_TEMPLATE \[=\] _`istemplate`_ \]
           \[ OID \[=\] _`oid`_ \]

## Description

`CREATE DATABASE` creates a new PostgreSQL database.

To create a database, you must be a superuser or have the special `CREATEDB` privilege. See [CREATE ROLE](https://www.postgresql.org/docs/current/sql-createrole.html "CREATE ROLE").

By default, the new database will be created by cloning the standard system database `template1`. A different template can be specified by writing ``TEMPLATE _`name`_``. In particular, by writing `TEMPLATE template0`, you can create a pristine database (one where no user-defined objects exist and where the system objects have not been altered) containing only the standard objects predefined by your version of PostgreSQL. This is useful if you wish to avoid copying any installation-local objects that might have been added to `template1`.

## Parameters

_`name`_ [#](#CREATE-DATABASE-NAME)

The name of a database to create.

_`user_name`_ [#](#CREATE-DATABASE-USER-NAME)

The role name of the user who will own the new database, or `DEFAULT` to use the default (namely, the user executing the command). To create a database owned by another role, you must be able to `SET ROLE` to that role.

_`template`_ [#](#CREATE-DATABASE-TEMPLATE)

The name of the template from which to create the new database, or `DEFAULT` to use the default template (`template1`).

_`encoding`_ [#](#CREATE-DATABASE-ENCODING)

Character set encoding to use in the new database. Specify a string constant (e.g., `'SQL_ASCII'`), or an integer encoding number, or `DEFAULT` to use the default encoding (namely, the encoding of the template database). The character sets supported by the PostgreSQL server are described in [Section 23.3.1](https://www.postgresql.org/docs/current/multibyte.html#MULTIBYTE-CHARSET-SUPPORTED "23.3.1. Supported Character Sets"). See below for additional restrictions.

_`strategy`_ [#](#CREATE-DATABASE-STRATEGY)

Strategy to be used in creating the new database. If the `WAL_LOG` strategy is used, the database will be copied block by block and each block will be separately written to the write-ahead log. This is the most efficient strategy in cases where the template database is small, and therefore it is the default. The older `FILE_COPY` strategy is also available. This strategy writes a small record to the write-ahead log for each tablespace used by the target database. Each such record represents copying an entire directory to a new location at the filesystem level. While this does reduce the write-ahead log volume substantially, especially if the template database is large, it also forces the system to perform a checkpoint both before and after the creation of the new database. In some situations, this may have a noticeable negative impact on overall system performance. The `FILE_COPY` strategy is affected by the [file\_copy\_method](../runtime-config-resource.html/index.md#GUC-FILE-COPY-METHOD) setting.

_`locale`_ [#](#CREATE-DATABASE-LOCALE)

Sets the default collation order and character classification in the new database. Collation affects the sort order applied to strings, e.g., in queries with `ORDER BY`, as well as the order used in indexes on text columns. Character classification affects the categorization of characters, e.g., lower, upper, and digit. Also sets the associated aspects of the operating system environment, `LC_COLLATE` and `LC_CTYPE`. The default is the same setting as the template database. See [Section 23.2.2.3.1](https://www.postgresql.org/docs/current/collation.html#COLLATION-MANAGING-CREATE-LIBC "23.2.2.3.1. libc Collations") and [Section 23.2.2.3.2](https://www.postgresql.org/docs/current/collation.html#COLLATION-MANAGING-CREATE-ICU "23.2.2.3.2. ICU Collations") for details.

Can be overridden by setting [_`lc_collate`_](index.md#CREATE-DATABASE-LC-COLLATE), [_`lc_ctype`_](index.md#CREATE-DATABASE-LC-CTYPE), [_`builtin_locale`_](index.md#CREATE-DATABASE-BUILTIN-LOCALE), or [_`icu_locale`_](index.md#CREATE-DATABASE-ICU-LOCALE) individually.

If [_`locale_provider`_](index.md#CREATE-DATABASE-LOCALE-PROVIDER) is `builtin`, then _`locale`_ or _`builtin_locale`_ must be specified and set to either `C`, `C.UTF-8`, or `PG_UNICODE_FAST`.

### Tip

The other locale settings [lc\_messages](../runtime-config-client.html/index.md#GUC-LC-MESSAGES), [lc\_monetary](../runtime-config-client.html/index.md#GUC-LC-MONETARY), [lc\_numeric](../runtime-config-client.html/index.md#GUC-LC-NUMERIC), and [lc\_time](../runtime-config-client.html/index.md#GUC-LC-TIME) are not fixed per database and are not set by this command. If you want to make them the default for a specific database, you can use `ALTER DATABASE ... SET`.

_`lc_collate`_ [#](#CREATE-DATABASE-LC-COLLATE)

Sets `LC_COLLATE` in the database server's operating system environment. The default is the setting of [_`locale`_](index.md#CREATE-DATABASE-LOCALE) if specified, otherwise the same setting as the template database. See below for additional restrictions.

If [_`locale_provider`_](index.md#CREATE-DATABASE-LOCALE-PROVIDER) is `libc`, also sets the default collation order to use in the new database, overriding the setting [_`locale`_](index.md#CREATE-DATABASE-LOCALE).

_`lc_ctype`_ [#](#CREATE-DATABASE-LC-CTYPE)

Sets `LC_CTYPE` in the database server's operating system environment. The default is the setting of [_`locale`_](index.md#CREATE-DATABASE-LOCALE) if specified, otherwise the same setting as the template database. See below for additional restrictions.

If [_`locale_provider`_](index.md#CREATE-DATABASE-LOCALE-PROVIDER) is `libc`, also sets the default character classification to use in the new database, overriding the setting [_`locale`_](index.md#CREATE-DATABASE-LOCALE).

_`builtin_locale`_ [#](#CREATE-DATABASE-BUILTIN-LOCALE)

Specifies the builtin provider locale for the database default collation order and character classification, overriding the setting [_`locale`_](index.md#CREATE-DATABASE-LOCALE). The [locale provider](index.md#CREATE-DATABASE-LOCALE-PROVIDER) must be `builtin`. The default is the setting of [_`locale`_](index.md#CREATE-DATABASE-LOCALE) if specified; otherwise the same setting as the template database.

The locales available for the `builtin` provider are `C`, `C.UTF-8` and `PG_UNICODE_FAST`.

_`icu_locale`_ [#](#CREATE-DATABASE-ICU-LOCALE)

Specifies the ICU locale (see [Section 23.2.2.3.2](https://www.postgresql.org/docs/current/collation.html#COLLATION-MANAGING-CREATE-ICU "23.2.2.3.2. ICU Collations")) for the database default collation order and character classification, overriding the setting [_`locale`_](index.md#CREATE-DATABASE-LOCALE). The [locale provider](index.md#CREATE-DATABASE-LOCALE-PROVIDER) must be ICU. The default is the setting of [_`locale`_](index.md#CREATE-DATABASE-LOCALE) if specified; otherwise the same setting as the template database.

_`icu_rules`_ [#](#CREATE-DATABASE-ICU-RULES)

Specifies additional collation rules to customize the behavior of the default collation of this database. This is supported for ICU only. See [Section 23.2.3.4](https://www.postgresql.org/docs/current/collation.html#ICU-TAILORING-RULES "23.2.3.4. ICU Tailoring Rules") for details.

_`locale_provider`_ [#](#CREATE-DATABASE-LOCALE-PROVIDER)

Specifies the provider to use for the default collation in this database. Possible values are `builtin`, `icu` (if the server was built with ICU support) or `libc`. By default, the provider is the same as that of the [_`template`_](index.md#CREATE-DATABASE-TEMPLATE). See [Section 23.1.4](https://www.postgresql.org/docs/current/locale.html#LOCALE-PROVIDERS "23.1.4. Locale Providers") for details.

_`collation_version`_ [#](#CREATE-DATABASE-COLLATION-VERSION)

Specifies the collation version string to store with the database. Normally, this should be omitted, which will cause the version to be computed from the actual version of the database collation as provided by the operating system. This option is intended to be used by `pg_upgrade` for copying the version from an existing installation.

See also [ALTER DATABASE](https://www.postgresql.org/docs/current/sql-alterdatabase.html "ALTER DATABASE") for how to handle database collation version mismatches.

_`tablespace_name`_ [#](#CREATE-DATABASE-TABLESPACE-NAME)

The name of the tablespace that will be associated with the new database, or `DEFAULT` to use the template database's tablespace. This tablespace will be the default tablespace used for objects created in this database. See [CREATE TABLESPACE](https://www.postgresql.org/docs/current/sql-createtablespace.html "CREATE TABLESPACE") for more information.

_`allowconn`_ [#](#CREATE-DATABASE-ALLOWCONN)

If false then no one can connect to this database. The default is true, allowing connections (except as restricted by other mechanisms, such as `GRANT`/`REVOKE CONNECT`).

_`connlimit`_ [#](#CREATE-DATABASE-CONNLIMIT)

How many concurrent connections can be made to this database. -1 (the default) means no limit.

_`istemplate`_ [#](#CREATE-DATABASE-ISTEMPLATE)

If true, then this database can be cloned by any user with `CREATEDB` privileges; if false (the default), then only superusers or the owner of the database can clone it.

_`oid`_ [#](#CREATE-DATABASE-OID)

The object identifier to be used for the new database. If this parameter is not specified, PostgreSQL will choose a suitable OID automatically. This parameter is primarily intended for internal use by pg\_upgrade, and only pg\_upgrade can specify a value less than 16384.

Optional parameters can be written in any order, not only the order illustrated above.

## Notes

`CREATE DATABASE` cannot be executed inside a transaction block.

Errors along the line of “could not initialize database directory” are most likely related to insufficient permissions on the data directory, a full disk, or other file system problems.

Use [`DROP DATABASE`](https://www.postgresql.org/docs/current/sql-dropdatabase.html "DROP DATABASE") to remove a database.

The program [createdb](https://www.postgresql.org/docs/current/app-createdb.html "createdb") is a wrapper program around this command, provided for convenience.

Database-level configuration parameters (set via [`ALTER DATABASE`](https://www.postgresql.org/docs/current/sql-alterdatabase.html "ALTER DATABASE")) and database-level permissions (set via [`GRANT`](https://www.postgresql.org/docs/current/sql-grant.html "GRANT")) are not copied from the template database.

Although it is possible to copy a database other than `template1` by specifying its name as the template, this is not (yet) intended as a general-purpose “`COPY DATABASE`” facility. The principal limitation is that no other sessions can be connected to the template database while it is being copied. `CREATE DATABASE` will fail if any other connection exists when it starts; otherwise, new connections to the template database are locked out until `CREATE DATABASE` completes. See [Section 22.3](https://www.postgresql.org/docs/current/manage-ag-templatedbs.html "22.3. Template Databases") for more information.

The character set encoding specified for the new database must be compatible with the chosen locale settings (`LC_COLLATE` and `LC_CTYPE`). If the locale is `C` (or equivalently `POSIX`), then all encodings are allowed, but for other locale settings there is only one encoding that will work properly. (On Windows, however, UTF-8 encoding can be used with any locale.) `CREATE DATABASE` will allow superusers to specify `SQL_ASCII` encoding regardless of the locale settings, but this choice is deprecated and may result in misbehavior of character-string functions if data that is not encoding-compatible with the locale is stored in the database.

The encoding and locale settings must match those of the template database, except when `template0` is used as template. This is because other databases might contain data that does not match the specified encoding, or might contain indexes whose sort ordering is affected by `LC_COLLATE` and `LC_CTYPE`. Copying such data would result in a database that is corrupt according to the new settings. `template0`, however, is known to not contain any data or indexes that would be affected.

There is currently no option to use a database locale with nondeterministic comparisons (see [`CREATE COLLATION`](https://www.postgresql.org/docs/current/sql-createcollation.html "CREATE COLLATION") for an explanation). If this is needed, then per-column collations would need to be used.

The `CONNECTION LIMIT` option is only enforced approximately; if two new sessions start at about the same time when just one connection “slot” remains for the database, it is possible that both will fail. Also, the limit is not enforced against superusers or background worker processes.

## Examples

To create a new database:

CREATE DATABASE lusiadas;

To create a database `sales` owned by user `salesapp` with a default tablespace of `salesspace`:

CREATE DATABASE sales OWNER salesapp TABLESPACE salesspace;

To create a database `music` with a different locale:

CREATE DATABASE music
    LOCALE 'sv\_SE.utf8'
    TEMPLATE template0;

In this example, the `TEMPLATE template0` clause is required if the specified locale is different from the one in `template1`. (If it is not, then specifying the locale explicitly is redundant.)

To create a database `music2` with a different locale and a different character set encoding:

CREATE DATABASE music2
    LOCALE 'sv\_SE.iso885915'
    ENCODING LATIN9
    TEMPLATE template0;

The specified locale and encoding settings must match, or an error will be reported.

Note that locale names are specific to the operating system, so that the above commands might not work in the same way everywhere.

## Compatibility

There is no `CREATE DATABASE` statement in the SQL standard. Databases are equivalent to catalogs, whose creation is implementation-defined.
