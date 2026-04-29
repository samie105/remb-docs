---
title: "PostgreSQL: Documentation: 18: 19.11. Client Connection Defaults"
source: "https://www.postgresql.org/docs/current/runtime-config-client.html"
canonical_url: "https://www.postgresql.org/docs/current/runtime-config-client.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:49.522Z"
content_hash: "0961fd1d8adedab1a5f2ff2bf4e4418c4bfdf70f4560e9d8cbd26ca6d7c40b6d"
menu_path: ["PostgreSQL: Documentation: 18: 19.11. Client Connection Defaults"]
section_path: []
nav_prev: {"path": "../rules-views.html/index.md", "title": "PostgreSQL: Documentation: 18: 39.2.\u00a0Views and the Rule System"}
nav_next: {"path": "../runtime-config-compatible.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.13.\u00a0Version and Platform Compatibility"}
---

### 19.11.1. Statement Behavior [#](#RUNTIME-CONFIG-CLIENT-STATEMENT)

`client_min_messages` (`enum`) [#](#GUC-CLIENT-MIN-MESSAGES)

Controls which [message levels](https://www.postgresql.org/docs/current/runtime-config-logging.html#RUNTIME-CONFIG-SEVERITY-LEVELS "Table 19.2. Message Severity Levels") are sent to the client. Valid values are `DEBUG5`, `DEBUG4`, `DEBUG3`, `DEBUG2`, `DEBUG1`, `LOG`, `NOTICE`, `WARNING`, and `ERROR`. Each level includes all the levels that follow it. The later the level, the fewer messages are sent. The default is `NOTICE`. Note that `LOG` has a different rank here than in [log\_min\_messages](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-MIN-MESSAGES).

`INFO` level messages are always sent to the client.

`search_path` (`string`) [#](#GUC-SEARCH-PATH)

This variable specifies the order in which schemas are searched when an object (table, data type, function, etc.) is referenced by a simple name with no schema specified. When there are objects of identical names in different schemas, the one found first in the search path is used. An object that is not in any of the schemas in the search path can only be referenced by specifying its containing schema with a qualified (dotted) name.

The value for `search_path` must be a comma-separated list of schema names. Any name that is not an existing schema, or is a schema for which the user does not have `USAGE` permission, is silently ignored.

If one of the list items is the special name `$user`, then the schema having the name returned by `CURRENT_USER` is substituted, if there is such a schema and the user has `USAGE` permission for it. (If not, `$user` is ignored.)

The system catalog schema, `pg_catalog`, is always searched, whether it is mentioned in the path or not. If it is mentioned in the path then it will be searched in the specified order. If `pg_catalog` is not in the path then it will be searched _before_ searching any of the path items.

Likewise, the current session's temporary-table schema, ``pg_temp__`nnn`_``, is always searched if it exists. It can be explicitly listed in the path by using the alias `pg_temp`. If it is not listed in the path then it is searched first (even before `pg_catalog`). However, the temporary schema is only searched for relation (table, view, sequence, etc.) and data type names. It is never searched for function or operator names.

When objects are created without specifying a particular target schema, they will be placed in the first valid schema named in `search_path`. An error is reported if the search path is empty.

The default value for this parameter is `"$user", public`. This setting supports shared use of a database (where no users have private schemas, and all share use of `public`), private per-user schemas, and combinations of these. Other effects can be obtained by altering the default search path setting, either globally or per-user.

For more information on schema handling, see [Section 5.10](https://www.postgresql.org/docs/current/ddl-schemas.html "5.10. Schemas"). In particular, the default configuration is suitable only when the database has a single user or a few mutually-trusting users.

The current effective value of the search path can be examined via the SQL function `current_schemas` (see [Section 9.27](https://www.postgresql.org/docs/current/functions-info.html "9.27. System Information Functions and Operators")). This is not quite the same as examining the value of `search_path`, since `current_schemas` shows how the items appearing in `search_path` were resolved.

`row_security` (`boolean`) [#](#GUC-ROW-SECURITY)

This variable controls whether to raise an error in lieu of applying a row security policy. When set to `on`, policies apply normally. When set to `off`, queries fail which would otherwise apply at least one policy. The default is `on`. Change to `off` where limited row visibility could cause incorrect results; for example, pg\_dump makes that change by default. This variable has no effect on roles which bypass every row security policy, to wit, superusers and roles with the `BYPASSRLS` attribute.

For more information on row security policies, see [CREATE POLICY](https://www.postgresql.org/docs/current/sql-createpolicy.html "CREATE POLICY").

`default_table_access_method` (`string`) [#](#GUC-DEFAULT-TABLE-ACCESS-METHOD)

This parameter specifies the default table access method to use when creating tables or materialized views if the `CREATE` command does not explicitly specify an access method, or when `SELECT ... INTO` is used, which does not allow specifying a table access method. The default is `heap`.

`default_tablespace` (`string`) [#](#GUC-DEFAULT-TABLESPACE)

This variable specifies the default tablespace in which to create objects (tables and indexes) when a `CREATE` command does not explicitly specify a tablespace.

The value is either the name of a tablespace, or an empty string to specify using the default tablespace of the current database. If the value does not match the name of any existing tablespace, PostgreSQL will automatically use the default tablespace of the current database. If a nondefault tablespace is specified, the user must have `CREATE` privilege for it, or creation attempts will fail.

This variable is not used for temporary tables; for them, [temp\_tablespaces](index.md#GUC-TEMP-TABLESPACES) is consulted instead.

This variable is also not used when creating databases. By default, a new database inherits its tablespace setting from the template database it is copied from.

If this parameter is set to a value other than the empty string when a partitioned table is created, the partitioned table's tablespace will be set to that value, which will be used as the default tablespace for partitions created in the future, even if `default_tablespace` has changed since then.

For more information on tablespaces, see [Section 22.6](https://www.postgresql.org/docs/current/manage-ag-tablespaces.html "22.6. Tablespaces").

`default_toast_compression` (`enum`) [#](#GUC-DEFAULT-TOAST-COMPRESSION)

This variable sets the default [TOAST](https://www.postgresql.org/docs/current/storage-toast.html "66.2. TOAST") compression method for values of compressible columns. (This can be overridden for individual columns by setting the `COMPRESSION` column option in `CREATE TABLE` or `ALTER TABLE`.) The supported compression methods are `pglz` and (if PostgreSQL was compiled with `--with-lz4`) `lz4`. The default is `pglz`.

`temp_tablespaces` (`string`) [#](#GUC-TEMP-TABLESPACES)

This variable specifies tablespaces in which to create temporary objects (temp tables and indexes on temp tables) when a `CREATE` command does not explicitly specify a tablespace. Temporary files for purposes such as sorting large data sets are also created in these tablespaces.

The value is a list of names of tablespaces. When there is more than one name in the list, PostgreSQL chooses a random member of the list each time a temporary object is to be created; except that within a transaction, successively created temporary objects are placed in successive tablespaces from the list. If the selected element of the list is an empty string, PostgreSQL will automatically use the default tablespace of the current database instead.

When `temp_tablespaces` is set interactively, specifying a nonexistent tablespace is an error, as is specifying a tablespace for which the user does not have `CREATE` privilege. However, when using a previously set value, nonexistent tablespaces are ignored, as are tablespaces for which the user lacks `CREATE` privilege. In particular, this rule applies when using a value set in `postgresql.conf`.

The default value is an empty string, which results in all temporary objects being created in the default tablespace of the current database.

See also [default\_tablespace](index.md#GUC-DEFAULT-TABLESPACE).

`check_function_bodies` (`boolean`) [#](#GUC-CHECK-FUNCTION-BODIES)

This parameter is normally on. When set to `off`, it disables validation of the routine body string during [CREATE FUNCTION](https://www.postgresql.org/docs/current/sql-createfunction.html "CREATE FUNCTION") and [CREATE PROCEDURE](https://www.postgresql.org/docs/current/sql-createprocedure.html "CREATE PROCEDURE"). Disabling validation avoids side effects of the validation process, in particular preventing false positives due to problems such as forward references. Set this parameter to `off` before loading functions on behalf of other users; pg\_dump does so automatically.

`default_transaction_isolation` (`enum`) [#](#GUC-DEFAULT-TRANSACTION-ISOLATION)

Each SQL transaction has an isolation level, which can be either “read uncommitted”, “read committed”, “repeatable read”, or “serializable”. This parameter controls the default isolation level of each new transaction. The default is “read committed”.

Consult [Chapter 13](https://www.postgresql.org/docs/current/mvcc.html "Chapter 13. Concurrency Control") and [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION") for more information.

`default_transaction_read_only` (`boolean`) [#](#GUC-DEFAULT-TRANSACTION-READ-ONLY)

A read-only SQL transaction cannot alter non-temporary tables. This parameter controls the default read-only status of each new transaction. The default is `off` (read/write).

Consult [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION") for more information.

`default_transaction_deferrable` (`boolean`) [#](#GUC-DEFAULT-TRANSACTION-DEFERRABLE)

When running at the `serializable` isolation level, a deferrable read-only SQL transaction may be delayed before it is allowed to proceed. However, once it begins executing it does not incur any of the overhead required to ensure serializability; so serialization code will have no reason to force it to abort because of concurrent updates, making this option suitable for long-running read-only transactions.

This parameter controls the default deferrable status of each new transaction. It currently has no effect on read-write transactions or those operating at isolation levels lower than `serializable`. The default is `off`.

Consult [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION") for more information.

`transaction_isolation` (`enum`) [#](#GUC-TRANSACTION-ISOLATION)

This parameter reflects the current transaction's isolation level. At the beginning of each transaction, it is set to the current value of [default\_transaction\_isolation](index.md#GUC-DEFAULT-TRANSACTION-ISOLATION). Any subsequent attempt to change it is equivalent to a [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION") command.

`transaction_read_only` (`boolean`) [#](#GUC-TRANSACTION-READ-ONLY)

This parameter reflects the current transaction's read-only status. At the beginning of each transaction, it is set to the current value of [default\_transaction\_read\_only](index.md#GUC-DEFAULT-TRANSACTION-READ-ONLY). Any subsequent attempt to change it is equivalent to a [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION") command.

`transaction_deferrable` (`boolean`) [#](#GUC-TRANSACTION-DEFERRABLE)

This parameter reflects the current transaction's deferrability status. At the beginning of each transaction, it is set to the current value of [default\_transaction\_deferrable](index.md#GUC-DEFAULT-TRANSACTION-DEFERRABLE). Any subsequent attempt to change it is equivalent to a [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION") command.

`session_replication_role` (`enum`) [#](#GUC-SESSION-REPLICATION-ROLE)

Controls firing of replication-related triggers and rules for the current session. Possible values are `origin` (the default), `replica` and `local`. Setting this parameter results in discarding any previously cached query plans. Only superusers and users with the appropriate `SET` privilege can change this setting.

The intended use of this setting is that logical replication systems set it to `replica` when they are applying replicated changes. The effect of that will be that triggers and rules (that have not been altered from their default configuration) will not fire on the replica. See the [`ALTER TABLE`](https://www.postgresql.org/docs/current/sql-altertable.html "ALTER TABLE") clauses `ENABLE TRIGGER` and `ENABLE RULE` for more information.

PostgreSQL treats the settings `origin` and `local` the same internally. Third-party replication systems may use these two values for their internal purposes, for example using `local` to designate a session whose changes should not be replicated.

Since foreign keys are implemented as triggers, setting this parameter to `replica` also disables all foreign key checks, which can leave data in an inconsistent state if improperly used.

`statement_timeout` (`integer`) [#](#GUC-STATEMENT-TIMEOUT)

Abort any statement that takes more than the specified amount of time. If `log_min_error_statement` is set to `ERROR` or lower, the statement that timed out will also be logged. If this value is specified without units, it is taken as milliseconds. A value of zero (the default) disables the timeout.

The timeout is measured from the time a command arrives at the server until it is completed by the server. If multiple SQL statements appear in a single simple-query message, the timeout is applied to each statement separately. (PostgreSQL versions before 13 usually treated the timeout as applying to the whole query string.) In extended query protocol, the timeout starts running when any query-related message (Parse, Bind, Execute, Describe) arrives, and it is canceled by completion of an Execute or Sync message.

Setting `statement_timeout` in `postgresql.conf` is not recommended because it would affect all sessions.

`transaction_timeout` (`integer`) [#](#GUC-TRANSACTION-TIMEOUT)

Terminate any session that spans longer than the specified amount of time in a transaction. The limit applies both to explicit transactions (started with `BEGIN`) and to an implicitly started transaction corresponding to a single statement. If this value is specified without units, it is taken as milliseconds. A value of zero (the default) disables the timeout.

If `transaction_timeout` is shorter or equal to `idle_in_transaction_session_timeout` or `statement_timeout` then the longer timeout is ignored.

Setting `transaction_timeout` in `postgresql.conf` is not recommended because it would affect all sessions.

### Note

Prepared transactions are not subject to this timeout.

`lock_timeout` (`integer`) [#](#GUC-LOCK-TIMEOUT)

Abort any statement that waits longer than the specified amount of time while attempting to acquire a lock on a table, index, row, or other database object. The time limit applies separately to each lock acquisition attempt. The limit applies both to explicit locking requests (such as `LOCK TABLE`, or `SELECT FOR UPDATE` without `NOWAIT`) and to implicitly-acquired locks. If this value is specified without units, it is taken as milliseconds. A value of zero (the default) disables the timeout.

Unlike `statement_timeout`, this timeout can only occur while waiting for locks. Note that if `statement_timeout` is nonzero, it is rather pointless to set `lock_timeout` to the same or larger value, since the statement timeout would always trigger first. If `log_min_error_statement` is set to `ERROR` or lower, the statement that timed out will be logged.

Setting `lock_timeout` in `postgresql.conf` is not recommended because it would affect all sessions.

`idle_in_transaction_session_timeout` (`integer`) [#](#GUC-IDLE-IN-TRANSACTION-SESSION-TIMEOUT)

Terminate any session that has been idle (that is, waiting for a client query) within an open transaction for longer than the specified amount of time. If this value is specified without units, it is taken as milliseconds. A value of zero (the default) disables the timeout.

This option can be used to ensure that idle sessions do not hold locks for an unreasonable amount of time. Even when no significant locks are held, an open transaction prevents vacuuming away recently-dead tuples that may be visible only to this transaction; so remaining idle for a long time can contribute to table bloat. See [Section 24.1](https://www.postgresql.org/docs/current/routine-vacuuming.html "24.1. Routine Vacuuming") for more details.

`idle_session_timeout` (`integer`) [#](#GUC-IDLE-SESSION-TIMEOUT)

Terminate any session that has been idle (that is, waiting for a client query), but not within an open transaction, for longer than the specified amount of time. If this value is specified without units, it is taken as milliseconds. A value of zero (the default) disables the timeout.

Unlike the case with an open transaction, an idle session without a transaction imposes no large costs on the server, so there is less need to enable this timeout than `idle_in_transaction_session_timeout`.

Be wary of enforcing this timeout on connections made through connection-pooling software or other middleware, as such a layer may not react well to unexpected connection closure. It may be helpful to enable this timeout only for interactive sessions, perhaps by applying it only to particular users.

`bytea_output` (`enum`) [#](#GUC-BYTEA-OUTPUT)

Sets the output format for values of type `bytea`. Valid values are `hex` (the default) and `escape` (the traditional PostgreSQL format). See [Section 8.4](https://www.postgresql.org/docs/current/datatype-binary.html "8.4. Binary Data Types") for more information. The `bytea` type always accepts both formats on input, regardless of this setting.

`xmlbinary` (`enum`) [#](#GUC-XMLBINARY)

Sets how binary values are to be encoded in XML. This applies for example when `bytea` values are converted to XML by the functions `xmlelement` or `xmlforest`. Possible values are `base64` and `hex`, which are both defined in the XML Schema standard. The default is `base64`. For further information about XML-related functions, see [Section 9.15](https://www.postgresql.org/docs/current/functions-xml.html "9.15. XML Functions").

The actual choice here is mostly a matter of taste, constrained only by possible restrictions in client applications. Both methods support all possible values, although the hex encoding will be somewhat larger than the base64 encoding.

`xmloption` (`enum`) [#](#GUC-XMLOPTION)

Sets whether `DOCUMENT` or `CONTENT` is implicit when converting between XML and character string values. See [Section 8.13](https://www.postgresql.org/docs/current/datatype-xml.html "8.13. XML Type") for a description of this. Valid values are `DOCUMENT` and `CONTENT`. The default is `CONTENT`.

According to the SQL standard, the command to set this option is

SET XML OPTION { DOCUMENT | CONTENT };

This syntax is also available in PostgreSQL.

`gin_pending_list_limit` (`integer`) [#](#GUC-GIN-PENDING-LIST-LIMIT)

Sets the maximum size of a GIN index's pending list, which is used when `fastupdate` is enabled. If the list grows larger than this maximum size, it is cleaned up by moving the entries in it to the index's main GIN data structure in bulk. If this value is specified without units, it is taken as kilobytes. The default is four megabytes (`4MB`). This setting can be overridden for individual GIN indexes by changing index storage parameters. See [Section 65.4.4.1](https://www.postgresql.org/docs/current/gin.html#GIN-FAST-UPDATE "65.4.4.1. GIN Fast Update Technique") and [Section 65.4.5](https://www.postgresql.org/docs/current/gin.html#GIN-TIPS "65.4.5. GIN Tips and Tricks") for more information.

`createrole_self_grant` (`string`) [#](#GUC-CREATEROLE-SELF-GRANT)

If a user who has `CREATEROLE` but not `SUPERUSER` creates a role, and if this is set to a non-empty value, the newly-created role will be granted to the creating user with the options specified. The value must be `set`, `inherit`, or a comma-separated list of these. The default value is an empty string, which disables the feature.

The purpose of this option is to allow a `CREATEROLE` user who is not a superuser to automatically inherit, or automatically gain the ability to `SET ROLE` to, any created users. Since a `CREATEROLE` user is always implicitly granted `ADMIN OPTION` on created roles, that user could always execute a `GRANT` statement that would achieve the same effect as this setting. However, it can be convenient for usability reasons if the grant happens automatically. A superuser automatically inherits the privileges of every role and can always `SET ROLE` to any role, and this setting can be used to produce a similar behavior for `CREATEROLE` users for users which they create.

`event_triggers` (`boolean`) [#](#GUC-EVENT-TRIGGERS)

Allow temporarily disabling execution of event triggers in order to troubleshoot and repair faulty event triggers. All event triggers will be disabled by setting it to `false`. Setting the value to `true` allows all event triggers to fire, this is the default value. Only superusers and users with the appropriate `SET` privilege can change this setting.

`restrict_nonsystem_relation_kind` (`string`) [#](#GUC-RESTRICT-NONSYSTEM-RELATION-KIND)

Set relation kinds for which access to non-system relations is prohibited. The value takes the form of a comma-separated list of relation kinds. Currently, the supported relation kinds are `view` and `foreign-table`.
