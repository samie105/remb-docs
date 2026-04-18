---
title: "PostgreSQL: Documentation: 18: pg_restore"
source: "https://www.postgresql.org/docs/current/app-pgrestore.html"
canonical_url: "https://www.postgresql.org/docs/current/app-pgrestore.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:54.281Z"
content_hash: "036cdbf1f579ffcd17c790a3e9d4a5af99dd8fb4a3bfab52ccab641777d6883b"
menu_path: ["PostgreSQL: Documentation: 18: pg_restore"]
section_path: []
---
pg\_restore accepts the following command line arguments.

_`filename`_

Specifies the location of the archive file (or directory, for a directory-format archive) to be restored. If not specified, the standard input is used.

`-a`  
`--data-only`

Restore only the data, not the schema (data definitions) or statistics. Table data, large objects, and sequence values are restored, if present in the archive.

This option is similar to, but for historical reasons not identical to, specifying `--section=data`.

`-c`  
`--clean`

Before restoring database objects, issue commands to `DROP` all the objects that will be restored. This option is useful for overwriting an existing database. If any of the objects do not exist in the destination database, ignorable error messages will be reported, unless `--if-exists` is also specified.

`-C`  
`--create`

Create the database before restoring into it. If `--clean` is also specified, drop and recreate the target database before connecting to it.

With `--create`, pg\_restore also restores the database's comment if any, and any configuration variable settings that are specific to this database, that is, any `ALTER DATABASE ... SET ...` and `ALTER ROLE ... IN DATABASE ... SET ...` commands that mention this database. Access privileges for the database itself are also restored, unless `--no-acl` is specified.

When this option is used, the database named with `-d` is used only to issue the initial `DROP DATABASE` and `CREATE DATABASE` commands. All data is restored into the database name that appears in the archive.

``-d _`dbname`_``  
``--dbname=_`dbname`_``

Connect to database _`dbname`_ and restore directly into the database. The _`dbname`_ can be a [connection string](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING "32.1.1. Connection Strings"). If so, connection string parameters will override any conflicting command line options.

`-e`  
`--exit-on-error`

Exit if an error is encountered while sending SQL commands to the database. The default is to continue and to display a count of errors at the end of the restoration.

``-f _`filename`_``  
``--file=_`filename`_``

Specify output file for generated script, or for the listing when used with `-l`. Use `-` for stdout.

``-F _`format`_``  
``--format=_`format`_``

Specify format of the archive. It is not necessary to specify the format, since pg\_restore will determine the format automatically. If specified, it can be one of the following:

`c`  
`custom`

The archive is in the custom format of pg\_dump.

`d`  
`directory`

The archive is a directory archive.

`t`  
`tar`

The archive is a `tar` archive.

``-I _`index`_``  
``--index=_`index`_``

Restore definition of named index only. Multiple indexes may be specified with multiple `-I` switches.

``-j _`number-of-jobs`_``  
``--jobs=_`number-of-jobs`_``

Run the most time-consuming steps of pg\_restore — those that load data, create indexes, or create constraints — concurrently, using up to _`number-of-jobs`_ concurrent sessions. This option can dramatically reduce the time to restore a large database to a server running on a multiprocessor machine. This option is ignored when emitting a script rather than connecting directly to a database server.

Each job is one process or one thread, depending on the operating system, and uses a separate connection to the server.

The optimal value for this option depends on the hardware setup of the server, of the client, and of the network. Factors include the number of CPU cores and the disk setup. A good place to start is the number of CPU cores on the server, but values larger than that can also lead to faster restore times in many cases. Of course, values that are too high will lead to decreased performance because of thrashing.

Only the custom and directory archive formats are supported with this option. The input must be a regular file or directory (not, for example, a pipe or standard input). Also, multiple jobs cannot be used together with the option `--single-transaction`.

`-l`  
`--list`

List the table of contents of the archive. The output of this operation can be used as input to the `-L` option. Note that if filtering switches such as `-n` or `-t` are used with `-l`, they will restrict the items listed.

``-L _`list-file`_``  
``--use-list=_`list-file`_``

Restore only those archive elements that are listed in _`list-file`_, and restore them in the order they appear in the file. Note that if filtering switches such as `-n` or `-t` are used with `-L`, they will further restrict the items restored.

_`list-file`_ is normally created by editing the output of a previous `-l` operation. Lines can be moved or removed, and can also be commented out by placing a semicolon (`;`) at the start of the line. See below for examples.

``-n _`schema`_``  
``--schema=_`schema`_``

Restore only objects that are in the named schema. Multiple schemas may be specified with multiple `-n` switches. This can be combined with the `-t` option to restore just a specific table.

``-N _`schema`_``  
``--exclude-schema=_`schema`_``

Do not restore objects that are in the named schema. Multiple schemas to be excluded may be specified with multiple `-N` switches.

When both `-n` and `-N` are given for the same schema name, the `-N` switch wins and the schema is excluded.

`-O`  
`--no-owner`

Do not output commands to set ownership of objects to match the original database. By default, pg\_restore issues `ALTER OWNER` or `SET SESSION AUTHORIZATION` statements to set ownership of created schema elements. These statements will fail unless the initial connection to the database is made by a superuser (or the same user that owns all of the objects in the script). With `-O`, any user name can be used for the initial connection, and this user will own all the created objects.

``-P _`function-name(argtype [, ...])`_``  
``--function=_`function-name(argtype [, ...])`_``

Restore the named function only. Be careful to spell the function name and arguments exactly as they appear in the dump file's table of contents. Multiple functions may be specified with multiple `-P` switches.

`-R`  
`--no-reconnect`

This option is obsolete but still accepted for backwards compatibility.

`-s`  
`--schema-only`

Restore only the schema (data definitions), not data, to the extent that schema entries are present in the archive.

This option cannot be used with `--data-only` or `--statistics-only`. It is similar to, but for historical reasons not identical to, specifying `--section=pre-data --section=post-data --no-statistics`.

(Do not confuse this with the `--schema` option, which uses the word “schema” in a different meaning.)

``-S _`username`_``  
``--superuser=_`username`_``

Specify the superuser user name to use when disabling triggers. This is relevant only if `--disable-triggers` is used.

``-t _`table`_``  
``--table=_`table`_``

Restore definition and/or data of only the named table. For this purpose, “table” includes views, materialized views, sequences, and foreign tables. Multiple tables can be selected by writing multiple `-t` switches. This option can be combined with the `-n` option to specify table(s) in a particular schema.

### Note

When `-t` is specified, pg\_restore makes no attempt to restore any other database objects that the selected table(s) might depend upon. Therefore, there is no guarantee that a specific-table restore into a clean database will succeed.

### Note

This flag does not behave identically to the `-t` flag of pg\_dump. There is not currently any provision for wild-card matching in pg\_restore, nor can you include a schema name within its `-t`. And, while pg\_dump's `-t` flag will also dump subsidiary objects (such as indexes) of the selected table(s), pg\_restore's `-t` flag does not include such subsidiary objects.

### Note

In versions prior to PostgreSQL 9.6, this flag matched only tables, not any other type of relation.

``-T _`trigger`_``  
``--trigger=_`trigger`_``

Restore named trigger only. Multiple triggers may be specified with multiple `-T` switches.

`-v`  
`--verbose`

Specifies verbose mode. This will cause pg\_restore to output detailed object comments and start/stop times to the output file, and progress messages to standard error. Repeating the option causes additional debug-level messages to appear on standard error.

`-V`  
`--version`

Print the pg\_restore version and exit.

`-x`  
`--no-privileges`  
`--no-acl`

Prevent restoration of access privileges (grant/revoke commands).

`-1`  
`--single-transaction`

Execute the restore as a single transaction (that is, wrap the emitted commands in `BEGIN`/`COMMIT`). This ensures that either all the commands complete successfully, or no changes are applied. This option implies `--exit-on-error`.

`--disable-triggers`

This option is relevant only when performing a restore without schema. It instructs pg\_restore to execute commands to temporarily disable triggers on the target tables while the data is restored. Use this if you have referential integrity checks or other triggers on the tables that you do not want to invoke during data restore.

Presently, the commands emitted for `--disable-triggers` must be done as superuser. So you should also specify a superuser name with `-S` or, preferably, run pg\_restore as a PostgreSQL superuser.

`--enable-row-security`

This option is relevant only when restoring the contents of a table which has row security. By default, pg\_restore will set [row\_security](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-ROW-SECURITY) to off, to ensure that all data is restored in to the table. If the user does not have sufficient privileges to bypass row security, then an error is thrown. This parameter instructs pg\_restore to set [row\_security](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-ROW-SECURITY) to on instead, allowing the user to attempt to restore the contents of the table with row security enabled. This might still fail if the user does not have the right to insert the rows from the dump into the table.

Note that this option currently also requires the dump be in `INSERT` format, as `COPY FROM` does not support row security.

``--filter=_`filename`_``

Specify a filename from which to read patterns for objects excluded or included from restore. The patterns are interpreted according to the same rules as `-n`/`--schema` for including objects in schemas, `-N`/`--exclude-schema` for excluding objects in schemas, `-P`/`--function` for restoring named functions, `-I`/`--index` for restoring named indexes, `-t`/`--table` for restoring named tables or `-T`/`--trigger` for restoring triggers. To read from `STDIN`, use `-` as the filename. The `--filter` option can be specified in conjunction with the above listed options for including or excluding objects, and can also be specified more than once for multiple filter files.

The file lists one database pattern per row, with the following format:

{ include | exclude } { function | index | schema | table | trigger } _`PATTERN`_

The first keyword specifies whether the objects matched by the pattern are to be included or excluded. The second keyword specifies the type of object to be filtered using the pattern:

*   `function`: functions, works like the `-P`/`--function` option. This keyword can only be used with the `include` keyword.
    
*   `index`: indexes, works like the `-I`/`--indexes` option. This keyword can only be used with the `include` keyword.
    
*   `schema`: schemas, works like the `-n`/`--schema` and `-N`/`--exclude-schema` options.
    
*   `table`: tables, works like the `-t`/`--table` option. This keyword can only be used with the `include` keyword.
    
*   `trigger`: triggers, works like the `-T`/`--trigger` option. This keyword can only be used with the `include` keyword.
    

Lines starting with `#` are considered comments and ignored. Comments can be placed after an object pattern row as well. Blank lines are also ignored. See [Patterns](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") for how to perform quoting in patterns.

`--if-exists`

Use `DROP ... IF EXISTS` commands to drop objects in `--clean` mode. This suppresses “does not exist” errors that might otherwise be reported. This option is not valid unless `--clean` is also specified.

`--no-comments`

Do not output commands to restore comments, even if the archive contains them.

`--no-data`

Do not output commands to restore data, even if the archive contains them.

`--no-data-for-failed-tables`

By default, table data is restored even if the creation command for the table failed (e.g., because it already exists). With this option, data for such a table is skipped. This behavior is useful if the target database already contains the desired table contents. For example, auxiliary tables for PostgreSQL extensions such as PostGIS might already be loaded in the target database; specifying this option prevents duplicate or obsolete data from being loaded into them.

This option is effective only when restoring directly into a database, not when producing SQL script output.

`--no-policies`

Do not output commands to restore row security policies, even if the archive contains them.

`--no-publications`

Do not output commands to restore publications, even if the archive contains them.

`--no-schema`

Do not output commands to restore schema (data definitions), even if the archive contains them.

`--no-security-labels`

Do not output commands to restore security labels, even if the archive contains them.

`--no-statistics`

Do not output commands to restore statistics, even if the archive contains them.

`--no-subscriptions`

Do not output commands to restore subscriptions, even if the archive contains them.

`--no-table-access-method`

Do not output commands to select table access methods. With this option, all objects will be created with whichever table access method is the default during restore.

`--no-tablespaces`

Do not output commands to select tablespaces. With this option, all objects will be created in whichever tablespace is the default during restore.

``--restrict-key=_`restrict_key`_``

Use the provided string as the psql `\restrict` key in the dump output. This can only be specified for SQL script output, i.e., when the `--file` option is used. If no restrict key is specified, pg\_restore will generate a random one as needed. Keys may contain only alphanumeric characters.

This option is primarily intended for testing purposes and other scenarios that require repeatable output (e.g., comparing dump files). It is not recommended for general use, as a malicious server with advance knowledge of the key may be able to inject arbitrary code that will be executed on the machine that runs psql with the dump output.

``--section=_`sectionname`_``

Only restore the named section. The section name can be `pre-data`, `data`, or `post-data`. This option can be specified more than once to select multiple sections. The default is to restore all sections.

The data section contains actual table data as well as large-object definitions. Post-data items consist of definitions of indexes, triggers, rules and constraints other than validated check constraints. Pre-data items consist of all other data definition items.

`--statistics`

Output commands to restore statistics, if the archive contains them. This is the default.

`--statistics-only`

Restore only the statistics, not schema (data definitions) or data.

`--strict-names`

Require that each schema (`-n`/`--schema`) and table (`-t`/`--table`) qualifier match at least one schema/table in the file to be restored.

``--transaction-size=_`N`_``

Execute the restore as a series of transactions, each processing up to _`N`_ database objects. This option implies `--exit-on-error`.

`--transaction-size` offers an intermediate choice between the default behavior (one transaction per SQL command) and `-1`/`--single-transaction` (one transaction for all restored objects). While `--single-transaction` has the least overhead, it may be impractical for large databases because the transaction will take a lock on each restored object, possibly exhausting the server's lock table space. Using `--transaction-size` with a size of a few thousand objects offers nearly the same performance benefits while capping the amount of lock table space needed.

`--use-set-session-authorization`

Output SQL-standard `SET SESSION AUTHORIZATION` commands instead of `ALTER OWNER` commands to determine object ownership. This makes the dump more standards-compatible, but depending on the history of the objects in the dump, might not restore properly.

`-?`  
`--help`

Show help about pg\_restore command line arguments, and exit.

pg\_restore also accepts the following command line arguments for connection parameters:

``-h _`host`_``  
``--host=_`host`_``

Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket. The default is taken from the `PGHOST` environment variable, if set, else a Unix domain socket connection is attempted.

``-p _`port`_``  
``--port=_`port`_``

Specifies the TCP port or local Unix domain socket file extension on which the server is listening for connections. Defaults to the `PGPORT` environment variable, if set, or a compiled-in default.

``-U _`username`_``  
``--username=_`username`_``

User name to connect as.

`-w`  
`--no-password`

Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a `.pgpass` file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.

`-W`  
`--password`

Force pg\_restore to prompt for a password before connecting to a database.

This option is never essential, since pg\_restore will automatically prompt for a password if the server demands password authentication. However, pg\_restore will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing `-W` to avoid the extra connection attempt.

``--role=_`rolename`_``

Specifies a role name to be used to perform the restore. This option causes pg\_restore to issue a `SET ROLE` _`rolename`_ command after connecting to the database. It is useful when the authenticated user (specified by `-U`) lacks privileges needed by pg\_restore, but can switch to a role with the required rights. Some installations have a policy against logging in directly as a superuser, and use of this option allows restores to be performed without violating the policy.
