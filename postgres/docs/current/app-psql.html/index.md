---
title: "PostgreSQL: Documentation: 18: psql"
source: "https://www.postgresql.org/docs/current/app-psql.html"
canonical_url: "https://www.postgresql.org/docs/current/app-psql.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:47.160Z"
content_hash: "38db55fe679f01678149c37cf4f679b114dbe98add5adf50c1ee376115752e4c"
menu_path: ["PostgreSQL: Documentation: 18: psql"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-createpolicy.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE POLICY"}
nav_next: {"path": "postgres/docs/current/runtime-config-client.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.11.\u00a0Client Connection Defaults"}
---

Anything you enter in psql that begins with an unquoted backslash is a psql meta-command that is processed by psql itself. These commands make psql more useful for administration or scripting. Meta-commands are often called slash or backslash commands.

The format of a psql command is the backslash, followed immediately by a command verb, then any arguments. The arguments are separated from the command verb and each other by any number of whitespace characters.

To include whitespace in an argument you can quote it with single quotes. To include a single quote in an argument, write two single quotes within single-quoted text. Anything contained in single quotes is furthermore subject to C-like substitutions for `\n` (new line), `\t` (tab), `\b` (backspace), `\r` (carriage return), `\f` (form feed), `\`_`digits`_ (octal), and `\x`_`digits`_ (hexadecimal). A backslash preceding any other character within single-quoted text quotes that single character, whatever it is.

If an unquoted colon (`:`) followed by a psql variable name appears within an argument, it is replaced by the variable's value, as described in [SQL Interpolation](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-INTERPOLATION "SQL Interpolation") below. The forms ``:'_`variable_name`_'`` and ``:"_`variable_name`_"`` described there work as well. The ``:{?_`variable_name`_}`` syntax allows testing whether a variable is defined. It is substituted by TRUE or FALSE. Escaping the colon with a backslash protects it from substitution.

Within an argument, text that is enclosed in backquotes (`` ` ``) is taken as a command line that is passed to the shell. The output of the command (with any trailing newline removed) replaces the backquoted text. Within the text enclosed in backquotes, no special quoting or other processing occurs, except that appearances of ``:_`variable_name`_`` where _`variable_name`_ is a psql variable name are replaced by the variable's value. Also, appearances of ``:'_`variable_name`_'`` are replaced by the variable's value suitably quoted to become a single shell command argument. (The latter form is almost always preferable, unless you are very sure of what is in the variable.) Because carriage return and line feed characters cannot be safely quoted on all platforms, the ``:'_`variable_name`_'`` form prints an error message and does not substitute the variable value when such characters appear in the value.

Some commands take an SQL identifier (such as a table name) as argument. These arguments follow the syntax rules of SQL: Unquoted letters are forced to lowercase, while double quotes (`"`) protect letters from case conversion and allow incorporation of whitespace into the identifier. Within double quotes, paired double quotes reduce to a single double quote in the resulting name. For example, `FOO"BAR"BAZ` is interpreted as `fooBARbaz`, and `"A weird"" name"` becomes `A weird" name`.

Parsing for arguments stops at the end of the line, or when another unquoted backslash is found. An unquoted backslash is taken as the beginning of a new meta-command. The special sequence `\\` (two backslashes) marks the end of arguments and continues parsing SQL commands, if any. That way SQL and psql commands can be freely mixed on a line. But in any case, the arguments of a meta-command cannot continue beyond the end of the line.

Many of the meta-commands act on the _current query buffer_. This is simply a buffer holding whatever SQL command text has been typed but not yet sent to the server for execution. This will include previous input lines as well as any text appearing before the meta-command on the same line.

Many of the meta-commands also allow `x` to be appended as an option. This will cause the results to be displayed in expanded mode, as if `\x` or `\pset expanded` had been used.

`\a` [#](#APP-PSQL-META-COMMAND-A)

If the current table output format is unaligned, it is switched to aligned. If it is not unaligned, it is set to unaligned. This command is kept for backwards compatibility. See `\pset` for a more general solution.

`\bind` \[ _`parameter`_ \] ... [#](#APP-PSQL-META-COMMAND-BIND)

Sets query parameters for the next query execution, with the specified parameters passed for any parameter placeholders (`$1` etc.).

Example:

INSERT INTO tbl1 VALUES ($1, $2) \\bind 'first value' 'second value' \\g

This also works for query-execution commands besides `\g`, such as `\gx` and `\gset`.

This command causes the extended query protocol (see [Section 54.1.2](https://www.postgresql.org/docs/current/protocol-overview.html#PROTOCOL-QUERY-CONCEPTS "54.1.2. Extended Query Overview")) to be used, unlike normal psql operation, which uses the simple query protocol. So this command can be useful to test the extended query protocol from psql. (The extended query protocol is used even if the query has no parameters and this command specifies zero parameters.) This command affects only the next query executed; all subsequent queries will use the simple query protocol by default.

`\bind_named` _`statement_name`_ \[ _`parameter`_ \] ... [#](#APP-PSQL-META-COMMAND-BIND-NAMED)

`\bind_named` is equivalent to `\bind`, except that it takes the name of an existing prepared statement as first parameter. An empty string denotes the unnamed prepared statement.

Example:

INSERT INTO tbls1 VALUES ($1, $2) \\parse stmt1
\\bind\_named stmt1 'first value' 'second value' \\g

This command causes the extended query protocol (see [Section 54.1.2](https://www.postgresql.org/docs/current/protocol-overview.html#PROTOCOL-QUERY-CONCEPTS "54.1.2. Extended Query Overview")) to be used, unlike normal psql operation, which uses the simple query protocol. So this command can be useful to test the extended query protocol from psql.

`\c` or ``\connect [ -reuse-previous=_`on|off`_ ] [ _`dbname`_ [ _`username`_ ] [ _`host`_ ] [ _`port`_ ] | _`conninfo`_ ]`` [#](#APP-PSQL-META-COMMAND-C-LC)

Establishes a new connection to a PostgreSQL server. The connection parameters to use can be specified either using a positional syntax (one or more of database name, user, host, and port), or using a _`conninfo`_ connection string as detailed in [Section 32.1.1](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING "32.1.1. Connection Strings"). If no arguments are given, a new connection is made using the same parameters as before.

Specifying any of _`dbname`_, _`username`_, _`host`_ or _`port`_ as `-` is equivalent to omitting that parameter.

The new connection can re-use connection parameters from the previous connection; not only database name, user, host, and port, but other settings such as _`sslmode`_. By default, parameters are re-used in the positional syntax, but not when a _`conninfo`_ string is given. Passing a first argument of `-reuse-previous=on` or `-reuse-previous=off` overrides that default. If parameters are re-used, then any parameter not explicitly specified as a positional parameter or in the _`conninfo`_ string is taken from the existing connection's parameters. An exception is that if the _`host`_ setting is changed from its previous value using the positional syntax, any _`hostaddr`_ setting present in the existing connection's parameters is dropped. Also, any password used for the existing connection will be re-used only if the user, host, and port settings are not changed. When the command neither specifies nor reuses a particular parameter, the libpq default is used.

If the new connection is successfully made, the previous connection is closed. If the connection attempt fails (wrong user name, access denied, etc.), the previous connection will be kept if psql is in interactive mode. But when executing a non-interactive script, the old connection is closed and an error is reported. That may or may not terminate the script; if it does not, all database-accessing commands will fail until another `\connect` command is successfully executed. This distinction was chosen as a user convenience against typos on the one hand, and a safety mechanism that scripts are not accidentally acting on the wrong database on the other hand. Note that whenever a `\connect` command attempts to re-use parameters, the values re-used are those of the last successful connection, not of any failed attempts made subsequently. However, in the case of a non-interactive `\connect` failure, no parameters are allowed to be re-used later, since the script would likely be expecting the values from the failed `\connect` to be re-used.

Examples:

\=> \\c mydb myuser host.dom 6432
=> \\c service=foo
=> \\c "host=localhost port=5432 dbname=mydb connect\_timeout=10 sslmode=disable"
=> \\c -reuse-previous=on sslmode=require    -- changes only sslmode
=> \\c postgresql://tom@localhost/mydb?application\_name=myapp

``\C [ _`title`_ ]`` [#](#APP-PSQL-META-COMMAND-C-UC)

Sets the title of any tables being printed as the result of a query or unset any such title. This command is equivalent to ``\pset title _`title`_``. (The name of this command derives from “caption”, as it was previously only used to set the caption in an HTML table.)

``\cd [ _`directory`_ ]`` [#](#APP-PSQL-META-COMMAND-CD)

Changes the current working directory to _`directory`_. Without argument, changes to the current user's home directory. For details on how home directories are found, see [Section 32.16](https://www.postgresql.org/docs/current/libpq-pgpass.html "32.16. The Password File").

### Tip

To print your current working directory, use `\! pwd`.

`\close_prepared` _`prepared_statement_name`_ [#](#APP-PSQL-META-COMMAND-CLOSE-PREPARED)

Closes the specified prepared statement. An empty string denotes the unnamed prepared statement. If no prepared statement exists with this name, the operation is a no-op.

Example:

SELECT $1 \\parse stmt1
\\close\_prepared stmt1

This command causes the extended query protocol to be used, unlike normal psql operation, which uses the simple query protocol. So this command can be useful to test the extended query protocol from psql.

`\conninfo` [#](#APP-PSQL-META-COMMAND-CONNINFO)

Outputs information about the current database connection, including SSL-related information if SSL is in use.

Note that the `Client User` field shows the user at the time of connection, while the `Superuser` field indicates whether the current user (in the current execution context) has superuser privileges. These users are usually the same, but they can differ, for example, if the current user was changed with the `SET ROLE` command.

``\copy { _`table`_ [ ( _`column_list`_ ) ] } `from` { _`'filename'`_ | program _`'command'`_ | stdin | pstdin } [ [ with ] ( _`option`_ [, ...] ) ] [ where _`condition`_ ]``  
``\copy { _`table`_ [ ( _`column_list`_ ) ] | ( _`query`_ ) } `to` { _`'filename'`_ | program _`'command'`_ | stdout | pstdout } [ [ with ] ( _`option`_ [, ...] ) ]`` [#](#APP-PSQL-META-COMMANDS-COPY)

Performs a frontend (client) copy. This is an operation that runs an SQL [`COPY`](https://www.postgresql.org/docs/current/sql-copy.html "COPY") command, but instead of the server reading or writing the specified file, psql reads or writes the file and routes the data between the server and the local file system. This means that file accessibility and privileges are those of the local user, not the server, and no SQL superuser privileges are required.

When `program` is specified, _`command`_ is executed by psql and the data passed from or to _`command`_ is routed between the server and the client. Again, the execution privileges are those of the local user, not the server, and no SQL superuser privileges are required.

For `\copy ... from stdin`, data rows are read from the same source that issued the command, continuing until a line containing only `\.` is read or the stream reaches EOF. This option is useful for populating tables in-line within an SQL script file. For `\copy ... to stdout`, output is sent to the same place as psql command output, and the ``COPY _`count`_`` command status is not printed (since it might be confused with a data row). To read/write psql's standard input or output regardless of the current command source or `\o` option, write `from pstdin` or `to pstdout`.

The syntax of this command is similar to that of the SQL [`COPY`](https://www.postgresql.org/docs/current/sql-copy.html "COPY") command. All options other than the data source/destination are as specified for `COPY`. Because of this, special parsing rules apply to the `\copy` meta-command. Unlike most other meta-commands, the entire remainder of the line is always taken to be the arguments of `\copy`, and neither variable interpolation nor backquote expansion are performed in the arguments.

### Tip

Another way to obtain the same result as `\copy ... to` is to use the SQL `COPY ... TO STDOUT` command and terminate it with ``\g _`filename`_`` or ``\g |_`program`_``. Unlike `\copy`, this method allows the command to span multiple lines; also, variable interpolation and backquote expansion can be used.

### Tip

These operations are not as efficient as the SQL `COPY` command with a file or program data source or destination, because all data must pass through the client/server connection. For large amounts of data the SQL command might be preferable.

`\copyright` [#](#APP-PSQL-META-COMMAND-COPYRIGHT)

Shows the copyright and distribution terms of PostgreSQL.

``\crosstabview [ _`colV`_ [ _`colH`_ [ _`colD`_ [ _`sortcolH`_ ] ] ] ]`` [#](#APP-PSQL-META-COMMANDS-CROSSTABVIEW)

Executes the current query buffer (like `\g`) and shows the results in a crosstab grid. The query must return at least three columns. The output column identified by _`colV`_ becomes a vertical header and the output column identified by _`colH`_ becomes a horizontal header. _`colD`_ identifies the output column to display within the grid. _`sortcolH`_ identifies an optional sort column for the horizontal header.

Each column specification can be a column number (starting at 1) or a column name. The usual SQL case folding and quoting rules apply to column names. If omitted, _`colV`_ is taken as column 1 and _`colH`_ as column 2. _`colH`_ must differ from _`colV`_. If _`colD`_ is not specified, then there must be exactly three columns in the query result, and the column that is neither _`colV`_ nor _`colH`_ is taken to be _`colD`_.

The vertical header, displayed as the leftmost column, contains the values found in column _`colV`_, in the same order as in the query results, but with duplicates removed.

The horizontal header, displayed as the first row, contains the values found in column _`colH`_, with duplicates removed. By default, these appear in the same order as in the query results. But if the optional _`sortcolH`_ argument is given, it identifies a column whose values must be integer numbers, and the values from _`colH`_ will appear in the horizontal header sorted according to the corresponding _`sortcolH`_ values.

Inside the crosstab grid, for each distinct value `x` of _`colH`_ and each distinct value `y` of _`colV`_, the cell located at the intersection `(x,y)` contains the value of the `colD` column in the query result row for which the value of _`colH`_ is `x` and the value of _`colV`_ is `y`. If there is no such row, the cell is empty. If there are multiple such rows, an error is reported.

``\d[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-D)

For each relation (table, view, materialized view, index, sequence, or foreign table) or composite type matching the _`pattern`_, show all columns, their types, the tablespace (if not the default) and any special attributes such as `NOT NULL` or defaults. Associated indexes, constraints, rules, and triggers are also shown. For foreign tables, the associated foreign server is shown as well. (“Matching the pattern” is defined in [Patterns](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") below.)

For some types of relation, `\d` shows additional information for each column: column values for sequences, indexed expressions for indexes, and foreign data wrapper options for foreign tables.

The command form `\d+` is identical, except that more information is displayed: any comments associated with the columns of the table are shown, as is the presence of OIDs in the table, the view definition if the relation is a view, a non-default [replica identity](https://www.postgresql.org/docs/current/sql-altertable.html#SQL-ALTERTABLE-REPLICA-IDENTITY) setting and the [access method](https://www.postgresql.org/docs/current/sql-create-access-method.html "CREATE ACCESS METHOD") name if the relation has an access method.

By default, only user-created objects are shown; supply a pattern or the `S` modifier to include system objects.

### Note

If `\d` is used without a _`pattern`_ argument, it is equivalent to `\dtvmsE` which will show a list of all visible tables, views, materialized views, sequences and foreign tables. This is purely a convenience measure.

As with many other commands, if `x` is appended to the command name, the results are displayed in expanded mode, but note that this only applies when `\d` is used without a _`pattern`_ argument, and the `x` modifier cannot appear immediately after the `\d` (because `\dx` is a different command); the `x` modifier may only appear after an `S` or `+` modifier. For example, `\d+x` is equivalent to `\dtvmsE+x` and will show a list of all relations in expanded mode.

``\da[Sx] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DA-LC)

Lists aggregate functions, together with their return type and the data types they operate on. If _`pattern`_ is specified, only aggregates whose names match the pattern are shown. By default, only user-created objects are shown; supply a pattern or the `S` modifier to include system objects. If `x` is appended to the command name, the results are displayed in expanded mode.

``\dA[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DA-UC)

Lists access methods. If _`pattern`_ is specified, only access methods whose names match the pattern are shown. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each access method is listed with its associated handler function and description.

``\dAc[x+] [[_`access-method-pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") [[_`input-type-pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns")]]`` [#](#APP-PSQL-META-COMMAND-DAC)

Lists operator classes (see [Section 36.16.1](https://www.postgresql.org/docs/current/xindex.html#XINDEX-OPCLASS "36.16.1. Index Methods and Operator Classes")). If _`access-method-pattern`_ is specified, only operator classes associated with access methods whose names match that pattern are listed. If _`input-type-pattern`_ is specified, only operator classes associated with input types whose names match that pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each operator class is listed with its associated operator family and owner.

``\dAf[x+] [[_`access-method-pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") [[_`input-type-pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns")]]`` [#](#APP-PSQL-META-COMMAND-DAF)

Lists operator families (see [Section 36.16.5](https://www.postgresql.org/docs/current/xindex.html#XINDEX-OPFAMILY "36.16.5. Operator Classes and Operator Families")). If _`access-method-pattern`_ is specified, only operator families associated with access methods whose names match that pattern are listed. If _`input-type-pattern`_ is specified, only operator families associated with input types whose names match that pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each operator family is listed with its owner.

``\dAo[x+] [[_`access-method-pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") [[_`operator-family-pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns")]]`` [#](#APP-PSQL-META-COMMAND-DAO)

Lists operators associated with operator families (see [Section 36.16.2](https://www.postgresql.org/docs/current/xindex.html#XINDEX-STRATEGIES "36.16.2. Index Method Strategies")). If _`access-method-pattern`_ is specified, only members of operator families associated with access methods whose names match that pattern are listed. If _`operator-family-pattern`_ is specified, only members of operator families whose names match that pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each operator is listed with its sort operator family (if it is an ordering operator), and whether its underlying function is leakproof.

``\dAp[x+] [[_`access-method-pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") [[_`operator-family-pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns")]]`` [#](#APP-PSQL-META-COMMAND-DAP)

Lists support functions associated with operator families (see [Section 36.16.3](https://www.postgresql.org/docs/current/xindex.html#XINDEX-SUPPORT "36.16.3. Index Method Support Routines")). If _`access-method-pattern`_ is specified, only functions of operator families associated with access methods whose names match that pattern are listed. If _`operator-family-pattern`_ is specified, only functions of operator families whose names match that pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, functions are displayed verbosely, with their actual parameter lists.

``\db[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DB)

Lists tablespaces. If _`pattern`_ is specified, only tablespaces whose names match the pattern are shown. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each tablespace is listed with its associated options, on-disk size, permissions and description.

``\dc[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DC-LC)

Lists conversions between character-set encodings. If _`pattern`_ is specified, only conversions whose names match the pattern are listed. By default, only user-created objects are shown; supply a pattern or the `S` modifier to include system objects. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each object is listed with its associated description.

``\dconfig[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DCONFIG)

Lists server configuration parameters and their values. If _`pattern`_ is specified, only parameters whose names match the pattern are listed. Without a _`pattern`_, only parameters that are set to non-default values are listed. (Use `\dconfig *` to see all parameters.) If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each parameter is listed with its data type, context in which the parameter can be set, and access privileges (if non-default access privileges have been granted).

``\dC[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DC-UC)

Lists type casts. If _`pattern`_ is specified, only casts whose source or target types match the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, additional information about each cast is shown, including whether its underlying function is leakproof, and the cast's description.

``\dd[Sx] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DD-LC)

Shows the descriptions of objects of type `constraint`, `operator class`, `operator family`, `rule`, and `trigger`. All other comments may be viewed by the respective backslash commands for those object types.

`\dd` displays descriptions for objects matching the _`pattern`_, or of visible objects of the appropriate type if no argument is given. But in either case, only objects that have a description are listed. By default, only user-created objects are shown; supply a pattern or the `S` modifier to include system objects. If `x` is appended to the command name, the results are displayed in expanded mode.

Descriptions for objects can be created with the [`COMMENT`](https://www.postgresql.org/docs/current/sql-comment.html "COMMENT") SQL command.

``\dD[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DD-UC)

Lists domains. If _`pattern`_ is specified, only domains whose names match the pattern are shown. By default, only user-created objects are shown; supply a pattern or the `S` modifier to include system objects. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each object is listed with its associated permissions and description.

``\ddp[x] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DDP)

Lists default access privilege settings. An entry is shown for each role (and schema, if applicable) for which the default privilege settings have been changed from the built-in defaults. If _`pattern`_ is specified, only entries whose role name or schema name matches the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode.

The [`ALTER DEFAULT PRIVILEGES`](https://www.postgresql.org/docs/current/sql-alterdefaultprivileges.html "ALTER DEFAULT PRIVILEGES") command is used to set default access privileges. The meaning of the privilege display is explained in [Section 5.8](https://www.postgresql.org/docs/current/ddl-priv.html "5.8. Privileges").

``\dE[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]``  
``\di[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]``  
``\dm[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]``  
``\ds[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]``  
``\dt[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]``  
``\dv[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DE)

In this group of commands, the letters `E`, `i`, `m`, `s`, `t`, and `v` stand for foreign table, index, materialized view, sequence, table, and view, respectively. You can specify any or all of these letters, in any order, to obtain a listing of objects of these types. For example, `\dti` lists tables and indexes. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each object is listed with its persistence status (permanent, temporary, or unlogged), physical size on disk, and associated description if any. If _`pattern`_ is specified, only objects whose names match the pattern are listed. By default, only user-created objects are shown; supply a pattern or the `S` modifier to include system objects.

``\des[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DES)

Lists foreign servers (mnemonic: “external servers”). If _`pattern`_ is specified, only those servers whose name matches the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, a full description of each server is shown, including the server's access privileges, type, version, options, and description.

``\det[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DET)

Lists foreign tables (mnemonic: “external tables”). If _`pattern`_ is specified, only entries whose table name or schema name matches the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, generic options and the foreign table description are also displayed.

``\deu[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DEU)

Lists user mappings (mnemonic: “external users”). If _`pattern`_ is specified, only those mappings whose user names match the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, additional information about each mapping is shown.

### Caution

`\deu+` might also display the user name and password of the remote user, so care should be taken not to disclose them.

``\dew[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DEW)

Lists foreign-data wrappers (mnemonic: “external wrappers”). If _`pattern`_ is specified, only those foreign-data wrappers whose name matches the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, the access privileges, options, and description of the foreign-data wrapper are also shown.

``\df[anptwSx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") [ _`arg_pattern`_ ... ] ]`` [#](#APP-PSQL-META-COMMAND-DF-LC)

Lists functions, together with their result data types, argument data types, and function types, which are classified as “agg” (aggregate), “normal”, “procedure”, “trigger”, or “window”. To display only functions of specific type(s), add the corresponding letters `a`, `n`, `p`, `t`, or `w` to the command. If _`pattern`_ is specified, only functions whose names match the pattern are shown. Any additional arguments are type-name patterns, which are matched to the type names of the first, second, and so on arguments of the function. (Matching functions can have more arguments than what you specify. To prevent that, write a dash `-` as the last _`arg_pattern`_.) By default, only user-created objects are shown; supply a pattern or the `S` modifier to include system objects. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, additional information about each function is shown, including volatility, parallel safety, owner, security classification, whether it is leakproof, access privileges, language, internal name (for C and internal functions only), and description. Source code for a specific function can be seen using `\sf`.

``\dF[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DF-UC)

Lists text search configurations. If _`pattern`_ is specified, only configurations whose names match the pattern are shown. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, a full description of each configuration is shown, including the underlying text search parser and the dictionary list for each parser token type.

``\dFd[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DFD)

Lists text search dictionaries. If _`pattern`_ is specified, only dictionaries whose names match the pattern are shown. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, additional information is shown about each selected dictionary, including the underlying text search template and the option values.

``\dFp[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DFP)

Lists text search parsers. If _`pattern`_ is specified, only parsers whose names match the pattern are shown. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, a full description of each parser is shown, including the underlying functions and the list of recognized token types.

``\dFt[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DFT)

Lists text search templates. If _`pattern`_ is specified, only templates whose names match the pattern are shown. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, additional information is shown about each template, including the underlying function names.

``\dg[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DG)

Lists database roles. (Since the concepts of “users” and “groups” have been unified into “roles”, this command is now equivalent to `\du`.) By default, only user-created roles are shown; supply the `S` modifier to include system roles. If _`pattern`_ is specified, only those roles whose names match the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, additional information is shown about each role; currently this adds the comment for each role.

`\dl[x+]` [#](#APP-PSQL-META-COMMAND-DL-LC)

This is an alias for `\lo_list`, which shows a list of large objects. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each large object is listed with its associated permissions, if any.

``\dL[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DL-UC)

Lists procedural languages. If _`pattern`_ is specified, only languages whose names match the pattern are listed. By default, only user-created languages are shown; supply the `S` modifier to include system objects. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each language is listed with its call handler, validator, access privileges, and whether it is a system object.

``\dn[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DN)

Lists schemas (namespaces). If _`pattern`_ is specified, only schemas whose names match the pattern are listed. By default, only user-created objects are shown; supply a pattern or the `S` modifier to include system objects. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each object is listed with its associated permissions and description, if any.

``\do[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") [ _`arg_pattern`_ [ _`arg_pattern`_ ] ] ]`` [#](#APP-PSQL-META-COMMAND-DO-LC)

Lists operators with their operand and result types. If _`pattern`_ is specified, only operators whose names match the pattern are listed. If one _`arg_pattern`_ is specified, only prefix operators whose right argument's type name matches that pattern are listed. If two _`arg_pattern`_s are specified, only binary operators whose argument type names match those patterns are listed. (Alternatively, write `-` for the unused argument of a unary operator.) By default, only user-created objects are shown; supply a pattern or the `S` modifier to include system objects. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, additional information about each operator is shown, including the name of the underlying function, and whether it is leakproof.

``\dO[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DO-UC)

Lists collations. If _`pattern`_ is specified, only collations whose names match the pattern are listed. By default, only user-created objects are shown; supply a pattern or the `S` modifier to include system objects. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each collation is listed with its associated description, if any. Note that only collations usable with the current database's encoding are shown, so the results may vary in different databases of the same installation.

``\dp[Sx] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DP-LC)

Lists tables, views and sequences with their associated access privileges. If _`pattern`_ is specified, only tables, views and sequences whose names match the pattern are listed. By default only user-created objects are shown; supply a pattern or the `S` modifier to include system objects. If `x` is appended to the command name, the results are displayed in expanded mode.

The [`GRANT`](https://www.postgresql.org/docs/current/sql-grant.html "GRANT") and [`REVOKE`](https://www.postgresql.org/docs/current/sql-revoke.html "REVOKE") commands are used to set access privileges. The meaning of the privilege display is explained in [Section 5.8](https://www.postgresql.org/docs/current/ddl-priv.html "5.8. Privileges").

``\dP[itnx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DP-UC)

Lists partitioned relations. If _`pattern`_ is specified, only entries whose name matches the pattern are listed. The modifiers `t` (tables) and `i` (indexes) can be appended to the command, filtering the kind of relations to list. By default, partitioned tables and indexes are listed.

If the modifier `n` (“nested”) is used, or a pattern is specified, then non-root partitioned relations are included, and a column is shown displaying the parent of each partitioned relation.

If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, the sum of the sizes of each relation's partitions is also displayed, along with the relation's description. If `n` is combined with `+`, two sizes are shown: one including the total size of directly-attached leaf partitions, and another showing the total size of all partitions, including indirectly attached sub-partitions.

``\drds[x] [ [_`role-pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") [ [_`database-pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ] ]`` [#](#APP-PSQL-META-COMMAND-DRDS)

Lists defined configuration settings. These settings can be role-specific, database-specific, or both. _`role-pattern`_ and _`database-pattern`_ are used to select specific roles and databases to list, respectively. If omitted, or if `*` is specified, all settings are listed, including those not role-specific or database-specific, respectively. If `x` is appended to the command name, the results are displayed in expanded mode.

The [`ALTER ROLE`](https://www.postgresql.org/docs/current/sql-alterrole.html "ALTER ROLE") and [`ALTER DATABASE`](https://www.postgresql.org/docs/current/sql-alterdatabase.html "ALTER DATABASE") commands are used to define per-role and per-database configuration settings.

``\drg[Sx] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DRG)

Lists information about each granted role membership, including assigned options (`ADMIN`, `INHERIT` and/or `SET`) and grantor. See the [`GRANT`](https://www.postgresql.org/docs/current/sql-grant.html "GRANT") command for information about role memberships.

By default, only grants to user-created roles are shown; supply the `S` modifier to include system roles. If _`pattern`_ is specified, only grants to those roles whose names match the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode.

``\dRp[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DRP)

Lists replication publications. If _`pattern`_ is specified, only those publications whose names match the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, the tables and schemas associated with each publication are shown as well.

``\dRs[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DRS)

Lists replication subscriptions. If _`pattern`_ is specified, only those subscriptions whose names match the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, additional properties of the subscriptions are shown.

``\dT[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DT)

Lists data types. If _`pattern`_ is specified, only types whose names match the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each type is listed with its internal name and size, its allowed values if it is an `enum` type, and its associated permissions. By default, only user-created objects are shown; supply a pattern or the `S` modifier to include system objects.

``\du[Sx+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DU)

Lists database roles. (Since the concepts of “users” and “groups” have been unified into “roles”, this command is now equivalent to `\dg`.) By default, only user-created roles are shown; supply the `S` modifier to include system roles. If _`pattern`_ is specified, only those roles whose names match the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, additional information is shown about each role; currently this adds the comment for each role.

``\dx[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DX-LC)

Lists installed extensions. If _`pattern`_ is specified, only those extensions whose names match the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, all the objects belonging to each matching extension are listed.

``\dX[x] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DX-UC)

Lists extended statistics. If _`pattern`_ is specified, only those extended statistics whose names match the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode.

The status of each kind of extended statistics is shown in a column named after its statistic kind (e.g. Ndistinct). `defined` means that it was requested when creating the statistics, and NULL means it wasn't requested. You can use `pg_stats_ext` if you'd like to know whether [`ANALYZE`](https://www.postgresql.org/docs/current/sql-analyze.html "ANALYZE") was run and statistics are available to the planner.

``\dy[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-DY)

Lists event triggers. If _`pattern`_ is specified, only those event triggers whose names match the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each object is listed with its associated description.

`\e` or `\edit` ``[ _`filename`_ ] [ _`line_number`_ ]`` [#](#APP-PSQL-META-COMMAND-EDIT)

If _`filename`_ is specified, the file is edited; after the editor exits, the file's content is copied into the current query buffer. If no _`filename`_ is given, the current query buffer is copied to a temporary file which is then edited in the same fashion. Or, if the current query buffer is empty, the most recently executed query is copied to a temporary file and edited in the same fashion.

If you edit a file or the previous query, and you quit the editor without modifying the file, the query buffer is cleared. Otherwise, the new contents of the query buffer are re-parsed according to the normal rules of psql, treating the whole buffer as a single line. Any complete queries are immediately executed; that is, if the query buffer contains or ends with a semicolon, everything up to that point is executed and removed from the query buffer. Whatever remains in the query buffer is redisplayed. Type semicolon or `\g` to send it, or `\r` to cancel it by clearing the query buffer.

Treating the buffer as a single line primarily affects meta-commands: whatever is in the buffer after a meta-command will be taken as argument(s) to the meta-command, even if it spans multiple lines. (Thus you cannot make meta-command-using scripts this way. Use `\i` for that.)

If a line number is specified, psql will position the cursor on the specified line of the file or query buffer. Note that if a single all-digits argument is given, psql assumes it is a line number, not a file name.

### Tip

See [Environment](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-ENVIRONMENT "Environment"), below, for how to configure and customize your editor.

``\echo _`text`_ [ ... ]`` [#](#APP-PSQL-META-COMMAND-ECHO)

Prints the evaluated arguments to standard output, separated by spaces and followed by a newline. This can be useful to intersperse information in the output of scripts. For example:

\=> **`` \echo `date` ``**
Tue Oct 26 21:40:57 CEST 1999

If the first argument is an unquoted `-n` the trailing newline is not written (nor is the first argument).

### Tip

If you use the `\o` command to redirect your query output you might wish to use `\qecho` instead of this command. See also `\warn`.

``\ef [ _`function_description`_ [ _`line_number`_ ] ]`` [#](#APP-PSQL-META-COMMAND-EF)

This command fetches and edits the definition of the named function or procedure, in the form of a `CREATE OR REPLACE FUNCTION` or `CREATE OR REPLACE PROCEDURE` command. Editing is done in the same way as for `\edit`. If you quit the editor without saving, the statement is discarded. If you save and exit the editor, the updated command is executed immediately if you added a semicolon to it. Otherwise it is redisplayed; type semicolon or `\g` to send it, or `\r` to cancel.

The target function can be specified by name alone, or by name and arguments, for example `foo(integer, text)`. The argument types must be given if there is more than one function of the same name.

If no function is specified, a blank `CREATE FUNCTION` template is presented for editing.

If a line number is specified, psql will position the cursor on the specified line of the function body. (Note that the function body typically does not begin on the first line of the file.)

Unlike most other meta-commands, the entire remainder of the line is always taken to be the argument(s) of `\ef`, and neither variable interpolation nor backquote expansion are performed in the arguments.

### Tip

See [Environment](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-ENVIRONMENT "Environment"), below, for how to configure and customize your editor.

``\encoding [ _`encoding`_ ]`` [#](#APP-PSQL-META-COMMAND-ENCODING)

Sets the client character set encoding. Without an argument, this command shows the current encoding.

`\errverbose` [#](#APP-PSQL-META-COMMAND-ERRVERBOSE)

Repeats the most recent server error message at maximum verbosity, as though `VERBOSITY` were set to `verbose` and `SHOW_CONTEXT` were set to `always`.

``\ev [ _`view_name`_ [ _`line_number`_ ] ]`` [#](#APP-PSQL-META-COMMAND-EV)

This command fetches and edits the definition of the named view, in the form of a `CREATE OR REPLACE VIEW` command. Editing is done in the same way as for `\edit`. If you quit the editor without saving, the statement is discarded. If you save and exit the editor, the updated command is executed immediately if you added a semicolon to it. Otherwise it is redisplayed; type semicolon or `\g` to send it, or `\r` to cancel.

If no view is specified, a blank `CREATE VIEW` template is presented for editing.

If a line number is specified, psql will position the cursor on the specified line of the view definition.

Unlike most other meta-commands, the entire remainder of the line is always taken to be the argument(s) of `\ev`, and neither variable interpolation nor backquote expansion are performed in the arguments.

``\f [ _`string`_ ]`` [#](#APP-PSQL-META-COMMAND-F)

Sets the field separator for unaligned query output. The default is the vertical bar (`|`). It is equivalent to `\pset fieldsep`.

``\g [ (_`option`_=_`value`_ [...]) ] [ _`filename`_ ]``  
``\g [ (_`option`_=_`value`_ [...]) ] [ |_`command`_ ]`` [#](#APP-PSQL-META-COMMAND-G)

Sends the current query buffer to the server for execution.

If parentheses appear after `\g`, they surround a space-separated list of _`option`_`=`_`value`_ formatting-option clauses, which are interpreted in the same way as `\pset` _`option`_ _`value`_ commands, but take effect only for the duration of this query. In this list, spaces are not allowed around `=` signs, but are required between option clauses. If `=`_`value`_ is omitted, the named _`option`_ is changed in the same way as for `\pset` _`option`_ with no explicit _`value`_.

If a _`filename`_ or `|`_`command`_ argument is given, the query's output is written to the named file or piped to the given shell command, instead of displaying it as usual. The file or command is written to only if the query successfully returns zero or more tuples, not if the query fails or is a non-data-returning SQL command.

If the current query buffer is empty, the most recently sent query is re-executed instead. Except for that behavior, `\g` without any arguments is essentially equivalent to a semicolon. With arguments, `\g` provides a “one-shot” alternative to the `\o` command, and additionally allows one-shot adjustments of the output formatting options normally set by `\pset`.

When the last argument begins with `|`, the entire remainder of the line is taken to be the _`command`_ to execute, and neither variable interpolation nor backquote expansion are performed in it. The rest of the line is simply passed literally to the shell.

`\gdesc` [#](#APP-PSQL-META-COMMAND-GDESC)

Shows the description (that is, the column names and data types) of the result of the current query buffer. The query is not actually executed; however, if it contains some type of syntax error, that error will be reported in the normal way.

If the current query buffer is empty, the most recently sent query is described instead.

``\getenv _`psql_var`_ _`env_var`_`` [#](#APP-PSQL-META-COMMAND-GETENV)

Gets the value of the environment variable _`env_var`_ and assigns it to the psql variable _`psql_var`_. If _`env_var`_ is not defined in the psql process's environment, _`psql_var`_ is not changed. Example:

\=> **`\getenv home HOME`**
=> **`\echo :home`**
/home/postgres

`\gexec` [#](#APP-PSQL-META-COMMAND-GEXEC)

Sends the current query buffer to the server, then treats each column of each row of the query's output (if any) as an SQL statement to be executed. For example, to create an index on each column of `my_table`:

\=> **`SELECT format('create index on my_table(%I)', attname)`**
-> **`FROM pg_attribute`**
-> **`WHERE attrelid = 'my_table'::regclass AND attnum > 0`**
-> **`ORDER BY attnum`**
-> **`\gexec`**
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX

The generated queries are executed in the order in which the rows are returned, and left-to-right within each row if there is more than one column. NULL fields are ignored. The generated queries are sent literally to the server for processing, so they cannot be psql meta-commands nor contain psql variable references. If any individual query fails, execution of the remaining queries continues unless `ON_ERROR_STOP` is set. Execution of each query is subject to `ECHO` processing. (Setting `ECHO` to `all` or `queries` is often advisable when using `\gexec`.) Query logging, single-step mode, timing, and other query execution features apply to each generated query as well.

If the current query buffer is empty, the most recently sent query is re-executed instead.

``\gset [ _`prefix`_ ]`` [#](#APP-PSQL-META-COMMAND-GSET)

Sends the current query buffer to the server and stores the query's output into psql variables (see [Variables](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-VARIABLES "Variables") below). The query to be executed must return exactly one row. Each column of the row is stored into a separate variable, named the same as the column. For example:

\=> **`SELECT 'hello' AS var1, 10 AS var2`**
-> **`\gset`**
=> **`\echo :var1 :var2`**
hello 10

If you specify a _`prefix`_, that string is prepended to the query's column names to create the variable names to use:

\=> **`SELECT 'hello' AS var1, 10 AS var2`**
-> **`\gset result_`**
=> **`\echo :result_var1 :result_var2`**
hello 10

If a column result is NULL, the corresponding variable is unset rather than being set.

If the query fails or does not return one row, no variables are changed.

If the current query buffer is empty, the most recently sent query is re-executed instead.

``\gx [ (_`option`_=_`value`_ [...]) ] [ _`filename`_ ]``  
``\gx [ (_`option`_=_`value`_ [...]) ] [ |_`command`_ ]`` [#](#APP-PSQL-META-COMMAND-GX)

`\gx` is equivalent to `\g`, except that it forces expanded output mode for this query, as if `expanded=on` were included in the list of `\pset` options. See also `\x`.

`\h` or `\help` ``[ _`command`_ ]`` [#](#APP-PSQL-META-COMMAND-HELP)

Gives syntax help on the specified SQL command. If _`command`_ is not specified, then psql will list all the commands for which syntax help is available. If _`command`_ is an asterisk (`*`), then syntax help on all SQL commands is shown.

Unlike most other meta-commands, the entire remainder of the line is always taken to be the argument(s) of `\help`, and neither variable interpolation nor backquote expansion are performed in the arguments.

### Note

To simplify typing, commands that consists of several words do not have to be quoted. Thus it is fine to type **`\help alter table`**.

`\H` or `\html` [#](#APP-PSQL-META-COMMAND-HTML)

Turns on HTML query output format. If the HTML format is already on, it is switched back to the default aligned text format. This command is for compatibility and convenience, but see `\pset` about setting other output options.

`\i` or `\include` _`filename`_ [#](#APP-PSQL-META-COMMAND-INCLUDE)

Reads input from the file _`filename`_ and executes it as though it had been typed on the keyboard.

If _`filename`_ is `-` (hyphen), then standard input is read until an EOF indication or `\q` meta-command. This can be used to intersperse interactive input with input from files. Note that Readline behavior will be used only if it is active at the outermost level.

### Note

If you want to see the lines on the screen as they are read you must set the variable `ECHO` to `all`.

`\if` _`expression`_  
`\elif` _`expression`_  
`\else`  
`\endif` [#](#PSQL-METACOMMAND-IF)

This group of commands implements nestable conditional blocks. A conditional block must begin with an `\if` and end with an `\endif`. In between there may be any number of `\elif` clauses, which may optionally be followed by a single `\else` clause. Ordinary queries and other types of backslash commands may (and usually do) appear between the commands forming a conditional block.

The `\if` and `\elif` commands read their argument(s) and evaluate them as a Boolean expression. If the expression yields `true` then processing continues normally; otherwise, lines are skipped until a matching `\elif`, `\else`, or `\endif` is reached. Once an `\if` or `\elif` test has succeeded, the arguments of later `\elif` commands in the same block are not evaluated but are treated as false. Lines following an `\else` are processed only if no earlier matching `\if` or `\elif` succeeded.

The _`expression`_ argument of an `\if` or `\elif` command is subject to variable interpolation and backquote expansion, just like any other backslash command argument. After that it is evaluated like the value of an on/off option variable. So a valid value is any unambiguous case-insensitive match for one of: `true`, `false`, `1`, `0`, `on`, `off`, `yes`, `no`. For example, `t`, `T`, and `tR` will all be considered to be `true`.

Expressions that do not properly evaluate to true or false will generate a warning and be treated as false.

Lines being skipped are parsed normally to identify queries and backslash commands, but queries are not sent to the server, and backslash commands other than conditionals (`\if`, `\elif`, `\else`, `\endif`) are ignored. Conditional commands are checked only for valid nesting. Variable references in skipped lines are not expanded, and backquote expansion is not performed either.

All the backslash commands of a given conditional block must appear in the same source file. If EOF is reached on the main input file or an `\include`\-ed file before all local `\if`\-blocks have been closed, then psql will raise an error.

Here is an example:

\-- check for the existence of two separate records in the database and store
-- the results in separate psql variables
SELECT
    EXISTS(SELECT 1 FROM customer WHERE customer\_id = 123) as is\_customer,
    EXISTS(SELECT 1 FROM employee WHERE employee\_id = 456) as is\_employee
\\gset
\\if :is\_customer
    SELECT \* FROM customer WHERE customer\_id = 123;
\\elif :is\_employee
    \\echo 'is not a customer but is an employee'
    SELECT \* FROM employee WHERE employee\_id = 456;
\\else
    \\if yes
        \\echo 'not a customer or employee'
    \\else
        \\echo 'this will never print'
    \\endif
\\endif

`\ir` or `\include_relative` _`filename`_ [#](#APP-PSQL-META-COMMAND-INCLUDE-RELATIVE)

The `\ir` command is similar to `\i`, but resolves relative file names differently. When executing in interactive mode, the two commands behave identically. However, when invoked from a script, `\ir` interprets file names relative to the directory in which the script is located, rather than the current working directory.

`\l[x+]` or ``\list[x+] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-LIST)

List the databases in the server and show their names, owners, character set encodings, and access privileges. If _`pattern`_ is specified, only databases whose names match the pattern are listed. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, database sizes, default tablespaces, and descriptions are also displayed. (Size information is only available for databases that the current user can connect to.)

``\lo_export _`loid`_ _`filename`_`` [#](#APP-PSQL-META-COMMAND-LO-EXPORT)

Reads the large object with OID _`loid`_ from the database and writes it to _`filename`_. Note that this is subtly different from the server function `lo_export`, which acts with the permissions of the user that the database server runs as and on the server's file system.

### Tip

Use `\lo_list` to find out the large object's OID.

``\lo_import _`filename`_ [ _`comment`_ ]`` [#](#APP-PSQL-META-COMMAND-LO-IMPORT)

Stores the file into a PostgreSQL large object. Optionally, it associates the given comment with the object. Example:

foo=> **`\lo_import '/home/peter/pictures/photo.xcf' 'a picture of me'`**
lo\_import 152801

The response indicates that the large object received object ID 152801, which can be used to access the newly-created large object in the future. For the sake of readability, it is recommended to always associate a human-readable comment with every object. Both OIDs and comments can be viewed with the `\lo_list` command.

Note that this command is subtly different from the server-side `lo_import` because it acts as the local user on the local file system, rather than the server's user and file system.

`\lo_list[x+]` [#](#APP-PSQL-META-COMMAND-LO-LIST)

Shows a list of all PostgreSQL large objects currently stored in the database, along with any comments provided for them. If `x` is appended to the command name, the results are displayed in expanded mode. If `+` is appended to the command name, each large object is listed with its associated permissions, if any.

``\lo_unlink _`loid`_`` [#](#APP-PSQL-META-COMMAND-LO-UNLINK)

Deletes the large object with OID _`loid`_ from the database.

### Tip

Use `\lo_list` to find out the large object's OID.

`\o` or ``\out [ _`filename`_ ]``  
`\o` or ``\out [ |_`command`_ ]`` [#](#APP-PSQL-META-COMMAND-OUT)

Arranges to save future query results to the file _`filename`_ or pipe future results to the shell command _`command`_. If no argument is specified, the query output is reset to the standard output.

If the argument begins with `|`, then the entire remainder of the line is taken to be the _`command`_ to execute, and neither variable interpolation nor backquote expansion are performed in it. The rest of the line is simply passed literally to the shell.

“Query results” includes all tables, command responses, and notices obtained from the database server, as well as output of various backslash commands that query the database (such as `\d`); but not error messages.

### Tip

To intersperse text output in between query results, use `\qecho`.

`\p` or `\print` [#](#APP-PSQL-META-COMMAND-PRINT)

Print the current query buffer to the standard output. If the current query buffer is empty, the most recently executed query is printed instead.

``\parse _`statement_name`_`` [#](#APP-PSQL-META-COMMAND-PARSE)

Creates a prepared statement from the current query buffer, based on the name of a destination prepared-statement object. An empty string denotes the unnamed prepared statement.

Example:

SELECT $1 \\parse stmt1

This command causes the extended query protocol to be used, unlike normal psql operation, which uses the simple query protocol. A [Parse (F)](https://www.postgresql.org/docs/current/protocol-message-formats.html#PROTOCOL-MESSAGE-FORMATS-PARSE) message will be issued by this command so it can be useful to test the extended query protocol from psql. This command affects only the next query executed; all subsequent queries will use the simple query protocol by default.

``\password [ _`username`_ ]`` [#](#APP-PSQL-META-COMMAND-PASSWORD)

Changes the password of the specified user (by default, the current user). This command prompts for the new password, encrypts it, and sends it to the server as an `ALTER ROLE` command. This makes sure that the new password does not appear in cleartext in the command history, the server log, or elsewhere.

``\prompt [ _`text`_ ] _`name`_`` [#](#APP-PSQL-META-COMMAND-PROMPT)

Prompts the user to supply text, which is assigned to the variable _`name`_. An optional prompt string, _`text`_, can be specified. (For multiword prompts, surround the text with single quotes.)

By default, `\prompt` uses the terminal for input and output. However, if the `-f` command line switch was used, `\prompt` uses standard input and standard output.

``\pset [ _`option`_ [ _`value`_ ] ]`` [#](#APP-PSQL-META-COMMAND-PSET)

This command sets options affecting the output of query result tables. _`option`_ indicates which option is to be set. The semantics of _`value`_ vary depending on the selected option. For some options, omitting _`value`_ causes the option to be toggled or unset, as described under the particular option. If no such behavior is mentioned, then omitting _`value`_ just results in the current setting being displayed.

`\pset` without any arguments displays the current status of all printing options.

Adjustable printing options are:

`border` [#](#APP-PSQL-META-COMMAND-PSET-BORDER)

The _`value`_ must be a number. In general, the higher the number the more borders and lines the tables will have, but details depend on the particular format. In HTML format, this will translate directly into the `border=...` attribute. In most other formats only values 0 (no border), 1 (internal dividing lines), and 2 (table frame) make sense, and values above 2 will be treated the same as `border = 2`. The `latex` and `latex-longtable` formats additionally allow a value of 3 to add dividing lines between data rows.

`columns` [#](#APP-PSQL-META-COMMAND-PSET-COLUMNS)

Sets the target width for the `wrapped` format, and also the width limit for determining whether output is wide enough to require the pager or switch to the vertical display in expanded auto mode. Zero (the default) causes the target width to be controlled by the environment variable `COLUMNS`, or the detected screen width if `COLUMNS` is not set. In addition, if `columns` is zero then the `wrapped` format only affects screen output. If `columns` is nonzero then file and pipe output is wrapped to that width as well.

`csv_fieldsep` [#](#APP-PSQL-META-COMMAND-PSET-CSV-FIELDSEP)

Specifies the field separator to be used in CSV output format. If the separator character appears in a field's value, that field is output within double quotes, following standard CSV rules. The default is a comma.

`expanded` (or `x`) [#](#APP-PSQL-META-COMMAND-PSET-EXPANDED)

If _`value`_ is specified it must be either `on` or `off`, which will enable or disable expanded mode, or `auto`. If _`value`_ is omitted the command toggles between the on and off settings. When expanded mode is enabled, query results are displayed in two columns, with the column name on the left and the data on the right. This mode is useful if the data wouldn't fit on the screen in the normal “horizontal” mode. In the auto setting, the expanded mode is used whenever the query output has more than one column and is wider than the screen; otherwise, the regular mode is used. The auto setting is only effective in the aligned and wrapped formats. In other formats, it always behaves as if the expanded mode is off.

`fieldsep` [#](#APP-PSQL-META-COMMAND-PSET-FIELDSEP)

Specifies the field separator to be used in unaligned output format. That way one can create, for example, tab-separated output, which other programs might prefer. To set a tab as field separator, type `\pset fieldsep '\t'`. The default field separator is `'|'` (a vertical bar).

`fieldsep_zero` [#](#APP-PSQL-META-COMMAND-PSET-FIELDSEP-ZERO)

Sets the field separator to use in unaligned output format to a zero byte.

`footer` [#](#APP-PSQL-META-COMMAND-PSET-FOOTER)

If _`value`_ is specified it must be either `on` or `off` which will enable or disable display of the table footer (the ``(_`n`_ rows)`` count). If _`value`_ is omitted the command toggles footer display on or off.

`format` [#](#APP-PSQL-META-COMMAND-PSET-FORMAT)

Sets the output format to one of `aligned`, `asciidoc`, `csv`, `html`, `latex`, `latex-longtable`, `troff-ms`, `unaligned`, or `wrapped`. Unique abbreviations are allowed.

`aligned` format is the standard, human-readable, nicely formatted text output; this is the default.

`unaligned` format writes all columns of a row on one line, separated by the currently active field separator. This is useful for creating output that might be intended to be read in by other programs, for example, tab-separated or comma-separated format. However, the field separator character is not treated specially if it appears in a column's value; so CSV format may be better suited for such purposes.

`csv` format writes column values separated by commas, applying the quoting rules described in [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180). This output is compatible with the CSV format of the server's `COPY` command. A header line with column names is generated unless the `tuples_only` parameter is `on`. Titles and footers are not printed. Each row is terminated by the system-dependent end-of-line character, which is typically a single newline (`\n`) for Unix-like systems or a carriage return and newline sequence (`\r\n`) for Microsoft Windows. Field separator characters other than comma can be selected with `\pset csv_fieldsep`.

`wrapped` format is like `aligned` but wraps wide data values across lines to make the output fit in the target column width. The target width is determined as described under the `columns` option. Note that psql will not attempt to wrap column header titles; therefore, `wrapped` format behaves the same as `aligned` if the total width needed for column headers exceeds the target.

The `asciidoc`, `html`, `latex`, `latex-longtable`, and `troff-ms` formats put out tables that are intended to be included in documents using the respective mark-up language. They are not complete documents! This might not be necessary in HTML, but in LaTeX you must have a complete document wrapper. The `latex` format uses LaTeX's `tabular` environment. The `latex-longtable` format requires the LaTeX `longtable` and `booktabs` packages.

`linestyle` [#](#APP-PSQL-META-COMMAND-PSET-LINESTYLE)

Sets the border line drawing style to one of `ascii`, `old-ascii`, or `unicode`. Unique abbreviations are allowed. (That would mean one letter is enough.) The default setting is `ascii`. This option only affects the `aligned` and `wrapped` output formats.

`ascii` style uses plain ASCII characters. Newlines in data are shown using a `+` symbol in the right-hand margin. When the `wrapped` format wraps data from one line to the next without a newline character, a dot (`.`) is shown in the right-hand margin of the first line, and again in the left-hand margin of the following line.

`old-ascii` style uses plain ASCII characters, using the formatting style used in PostgreSQL 8.4 and earlier. Newlines in data are shown using a `:` symbol in place of the left-hand column separator. When the data is wrapped from one line to the next without a newline character, a `;` symbol is used in place of the left-hand column separator.

`unicode` style uses Unicode box-drawing characters. Newlines in data are shown using a carriage return symbol in the right-hand margin. When the data is wrapped from one line to the next without a newline character, an ellipsis symbol is shown in the right-hand margin of the first line, and again in the left-hand margin of the following line.

When the `border` setting is greater than zero, the `linestyle` option also determines the characters with which the border lines are drawn. Plain ASCII characters work everywhere, but Unicode characters look nicer on displays that recognize them.

`null` [#](#APP-PSQL-META-COMMAND-PSET-NULL)

Sets the string to be printed in place of a null value. The default is to print nothing, which can easily be mistaken for an empty string. For example, one might prefer `\pset null '(null)'`.

`numericlocale` [#](#APP-PSQL-META-COMMAND-PSET-NUMERICLOCALE)

If _`value`_ is specified it must be either `on` or `off` which will enable or disable display of a locale-specific character to separate groups of digits to the left of the decimal marker. If _`value`_ is omitted the command toggles between regular and locale-specific numeric output.

`pager` [#](#APP-PSQL-META-COMMAND-PSET-PAGER)

Controls use of a pager program for query and psql help output. When the `pager` option is `off`, the pager program is not used. When the `pager` option is `on`, the pager is used when appropriate, i.e., when the output is to a terminal and will not fit on the screen. The `pager` option can also be set to `always`, which causes the pager to be used for all terminal output regardless of whether it fits on the screen. `\pset pager` without a _`value`_ toggles pager use on and off.

If the environment variable `PSQL_PAGER` or `PAGER` is set, output to be paged is piped to the specified program. Otherwise a platform-dependent default program (such as `more`) is used.

When using the `\watch` command to execute a query repeatedly, the environment variable `PSQL_WATCH_PAGER` is used to find the pager program instead, on Unix systems. This is configured separately because it may confuse traditional pagers, but can be used to send output to tools that understand psql's output format (such as `pspg --stream`).

`pager_min_lines` [#](#APP-PSQL-META-COMMAND-PSET-PAGER-MIN-LINES)

If `pager_min_lines` is set to a number greater than the page height, the pager program will not be called unless there are at least this many lines of output to show. The default setting is 0.

`recordsep` [#](#APP-PSQL-META-COMMAND-PSET-RECORDSEP)

Specifies the record (line) separator to use in unaligned output format. The default is a newline character.

`recordsep_zero` [#](#APP-PSQL-META-COMMAND-PSET-RECORDSEP-ZERO)

Sets the record separator to use in unaligned output format to a zero byte.

`tableattr` (or `T`) [#](#APP-PSQL-META-COMMAND-PSET-TABLEATTR)

In HTML format, this specifies attributes to be placed inside the `table` tag. This could for example be `cellpadding` or `bgcolor`. Note that you probably don't want to specify `border` here, as that is already taken care of by `\pset border`. If no _`value`_ is given, the table attributes are unset.

In `latex-longtable` format, this controls the proportional width of each column containing a left-aligned data type. It is specified as a whitespace-separated list of values, e.g., `'0.2 0.2 0.6'`. Unspecified output columns use the last specified value.

`title` (or `C`) [#](#APP-PSQL-META-COMMAND-PSET-TITLE)

Sets the table title for any subsequently printed tables. This can be used to give your output descriptive tags. If no _`value`_ is given, the title is unset.

`tuples_only` (or `t`) [#](#APP-PSQL-META-COMMAND-PSET-TUPLES-ONLY)

If _`value`_ is specified it must be either `on` or `off` which will enable or disable tuples-only mode. If _`value`_ is omitted the command toggles between regular and tuples-only output. Regular output includes extra information such as column headers, titles, and various footers. In tuples-only mode, only actual table data is shown.

`unicode_border_linestyle` [#](#APP-PSQL-META-COMMAND-PSET-UNICODE-BORDER-LINESTYLE)

Sets the border drawing style for the `unicode` line style to one of `single` or `double`.

`unicode_column_linestyle` [#](#APP-PSQL-META-COMMAND-PSET-UNICODE-COLUMN-LINESTYLE)

Sets the column drawing style for the `unicode` line style to one of `single` or `double`.

`unicode_header_linestyle` [#](#APP-PSQL-META-COMMAND-PSET-UNICODE-HEADER-LINESTYLE)

Sets the header drawing style for the `unicode` line style to one of `single` or `double`.

`xheader_width` [#](#APP-PSQL-META-COMMAND-PSET-XHEADER-WIDTH)

Sets the maximum width of the header for expanded output to one of `full` (the default value), `column`, `page`, or an _`integer value`_.

`full`: the expanded header is not truncated, and will be as wide as the widest output line.

`column`: truncate the header line to the width of the first column.

`page`: truncate the header line to the terminal width.

_`integer value`_: specify the exact maximum width of the header line.

Illustrations of how these different formats look can be seen in [Examples](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-EXAMPLES "Examples"), below.

### Tip

There are various shortcut commands for `\pset`. See `\a`, `\C`, `\f`, `\H`, `\t`, `\T`, and `\x`.

`\q` or `\quit` [#](#APP-PSQL-META-COMMAND-QUIT)

Quits the psql program. In a script file, only execution of that script is terminated.

``\qecho _`text`_ [ ... ]`` [#](#APP-PSQL-META-COMMAND-QECHO)

This command is identical to `\echo` except that the output will be written to the query output channel, as set by `\o`.

`\r` or `\reset` [#](#APP-PSQL-META-COMMAND-RESET)

Resets (clears) the query buffer.

``\restrict _`restrict_key`_`` [#](#APP-PSQL-META-COMMAND-RESTRICT)

Enter "restricted" mode with the provided key. In this mode, the only allowed meta-command is `\unrestrict`, to exit restricted mode. The key may contain only alphanumeric characters.

This command is primarily intended for use in plain-text dumps generated by pg\_dump, pg\_dumpall, and pg\_restore, but it may be useful elsewhere.

``\s [ _`filename`_ ]`` [#](#APP-PSQL-META-COMMAND-S)

Print psql's command line history to _`filename`_. If _`filename`_ is omitted, the history is written to the standard output (using the pager if appropriate). This command is not available if psql was built without Readline support.

``\set [ _`name`_ [ _`value`_ [ ... ] ] ]`` [#](#APP-PSQL-META-COMMAND-SET)

Sets the psql variable _`name`_ to _`value`_, or if more than one value is given, to the concatenation of all of them. If only one argument is given, the variable is set to an empty-string value. To unset a variable, use the `\unset` command.

`\set` without any arguments displays the names and values of all currently-set psql variables.

Valid variable names can contain letters, digits, and underscores. See [Variables](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-VARIABLES "Variables") below for details. Variable names are case-sensitive.

Certain variables are special, in that they control psql's behavior or are automatically set to reflect connection state. These variables are documented in [Variables](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-VARIABLES "Variables"), below.

### Note

This command is unrelated to the SQL command [`SET`](https://www.postgresql.org/docs/current/sql-set.html "SET").

``\setenv _`name`_ [ _`value`_ ]`` [#](#APP-PSQL-META-COMMAND-SETENV)

Sets the environment variable _`name`_ to _`value`_, or if the _`value`_ is not supplied, unsets the environment variable. Example:

testdb=> **`\setenv PAGER less`**
testdb=> **`\setenv LESS -imx4F`**

``\sf[+] _`function_description`_`` [#](#APP-PSQL-META-COMMAND-SF)

This command fetches and shows the definition of the named function or procedure, in the form of a `CREATE OR REPLACE FUNCTION` or `CREATE OR REPLACE PROCEDURE` command. The definition is printed to the current query output channel, as set by `\o`.

The target function can be specified by name alone, or by name and arguments, for example `foo(integer, text)`. The argument types must be given if there is more than one function of the same name.

If `+` is appended to the command name, then the output lines are numbered, with the first line of the function body being line 1.

Unlike most other meta-commands, the entire remainder of the line is always taken to be the argument(s) of `\sf`, and neither variable interpolation nor backquote expansion are performed in the arguments.

``\sv[+] _`view_name`_`` [#](#APP-PSQL-META-COMMAND-SV)

This command fetches and shows the definition of the named view, in the form of a `CREATE OR REPLACE VIEW` command. The definition is printed to the current query output channel, as set by `\o`.

If `+` is appended to the command name, then the output lines are numbered from 1.

Unlike most other meta-commands, the entire remainder of the line is always taken to be the argument(s) of `\sv`, and neither variable interpolation nor backquote expansion are performed in the arguments.

`\startpipeline`  
`\sendpipeline`  
`\syncpipeline`  
`\endpipeline`  
`\flushrequest`  
`\flush`  
``\getresults [ _`number_results`_ ]`` [#](#APP-PSQL-META-COMMAND-PIPELINE)

This group of commands implements pipelining of SQL statements. A pipeline must begin with a `\startpipeline` and end with an `\endpipeline`. In between there may be any number of `\syncpipeline` commands, which sends a [sync message](https://www.postgresql.org/docs/current/protocol-flow.html#PROTOCOL-FLOW-EXT-QUERY "54.2.3. Extended Query") without ending the ongoing pipeline and flushing the send buffer. In pipeline mode, statements are sent to the server without waiting for the results of previous statements. See [Section 32.5](https://www.postgresql.org/docs/current/libpq-pipeline-mode.html "32.5. Pipeline Mode") for more details.

All queries executed while a pipeline is ongoing use the extended query protocol. Queries are appended to the pipeline when ending with a semicolon. The meta-commands `\bind`, `\bind_named`, `\close_prepared` or `\parse` can be used in an ongoing pipeline. While a pipeline is ongoing, `\sendpipeline` will append the current query buffer to the pipeline. Other meta-commands like `\g`, `\gx` or `\gdesc` are not allowed in pipeline mode.

`\flushrequest` appends a flush command to the pipeline, allowing to read results with `\getresults` without issuing a sync or ending the pipeline. `\getresults` will automatically push unsent data to the server. `\flush` can be used to manually push unsent data.

`\getresults` accepts an optional _`number_results`_ parameter. If provided, only the first _`number_results`_ pending results will be read. If not provided or `0`, all pending results are read.

When pipeline mode is active, a dedicated prompt variable is available to report the pipeline status. See [`%P`](postgres/docs/current/app-psql.html/index.md#APP-PSQL-PROMPTING-P-UC) for more details

`COPY` is not supported while in pipeline mode.

Example:

\\startpipeline
SELECT \* FROM pg\_class;
SELECT 1 \\bind \\sendpipeline
\\flushrequest
\\getresults
\\endpipeline

`\t` [#](#APP-PSQL-META-COMMAND-T-LC)

Toggles the display of output column name headings and row count footer. This command is equivalent to `\pset tuples_only` and is provided for convenience.

``\T _`table_options`_`` [#](#APP-PSQL-META-COMMAND-T-UC)

Specifies attributes to be placed within the `table` tag in HTML output format. This command is equivalent to ``\pset tableattr _`table_options`_``.

``\timing [ _`on`_ | _`off`_ ]`` [#](#APP-PSQL-META-COMMAND-TIMING)

With a parameter, turns displaying of how long each SQL statement takes on or off. Without a parameter, toggles the display between on and off. The display is in milliseconds; intervals longer than 1 second are also shown in minutes:seconds format, with hours and days fields added if needed.

``\unrestrict _`restrict_key`_`` [#](#APP-PSQL-META-COMMAND-UNRESTRICT)

Exit "restricted" mode (i.e., where all other meta-commands are blocked), provided the specified key matches the one given to `\restrict` when restricted mode was entered.

This command is primarily intended for use in plain-text dumps generated by pg\_dump, pg\_dumpall, and pg\_restore, but it may be useful elsewhere.

``\unset _`name`_`` [#](#APP-PSQL-META-COMMAND-UNSET)

Unsets (deletes) the psql variable _`name`_.

Most variables that control psql's behavior cannot be unset; instead, an `\unset` command is interpreted as setting them to their default values. See [Variables](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-VARIABLES "Variables") below.

`\w` or `\write` _`filename`_  
`\w` or `\write` `|`_`command`_ [#](#APP-PSQL-META-COMMAND-WRITE)

Writes the current query buffer to the file _`filename`_ or pipes it to the shell command _`command`_. If the current query buffer is empty, the most recently executed query is written instead.

If the argument begins with `|`, then the entire remainder of the line is taken to be the _`command`_ to execute, and neither variable interpolation nor backquote expansion are performed in it. The rest of the line is simply passed literally to the shell.

``\warn _`text`_ [ ... ]`` [#](#APP-PSQL-META-COMMAND-WARN)

This command is identical to `\echo` except that the output will be written to psql's standard error channel, rather than standard output.

``\watch [ i[nterval]=_`seconds`_ ] [ c[ount]=_`times`_ ] [ m[in_rows]=_`rows`_ ] [ _`seconds`_ ]`` [#](#APP-PSQL-META-COMMAND-WATCH)

Repeatedly execute the current query buffer (as `\g` does) until interrupted, or the query fails, or the execution count limit (if given) is reached, or the query no longer returns the minimum number of rows. Wait the specified number of seconds (default 2) between executions. The default wait can be changed with the variable [`WATCH_INTERVAL`](postgres/docs/current/app-psql.html/index.md#APP-PSQL-VARIABLES-WATCH-INTERVAL). For backwards compatibility, _`seconds`_ can be specified with or without an `interval=` prefix. Each query result is displayed with a header that includes the `\pset title` string (if any), the time as of query start, and the delay interval.

If the current query buffer is empty, the most recently sent query is re-executed instead.

``\x [ _`on`_ | _`off`_ | _`auto`_ ]`` [#](#APP-PSQL-META-COMMAND-X)

Sets or toggles expanded table formatting mode. As such it is equivalent to `\pset expanded`.

``\z[Sx] [ [_`pattern`_](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-PATTERNS "Patterns") ]`` [#](#APP-PSQL-META-COMMAND-Z)

Lists tables, views and sequences with their associated access privileges. If a _`pattern`_ is specified, only tables, views and sequences whose names match the pattern are listed. By default only user-created objects are shown; supply a pattern or the `S` modifier to include system objects. If `x` is appended to the command name, the results are displayed in expanded mode.

This is an alias for `\dp` (“display privileges”).

``\! [ _`command`_ ]`` [#](#APP-PSQL-META-COMMAND-EXCLAMATION-MARK)

With no argument, escapes to a sub-shell; psql resumes when the sub-shell exits. With an argument, executes the shell command _`command`_.

Unlike most other meta-commands, the entire remainder of the line is always taken to be the argument(s) of `\!`, and neither variable interpolation nor backquote expansion are performed in the arguments. The rest of the line is simply passed literally to the shell.

``\? [ _`topic`_ ]`` [#](#APP-PSQL-META-COMMAND-QUESTION-MARK)

Shows help information. The optional _`topic`_ parameter (defaulting to `commands`) selects which part of psql is explained: `commands` describes psql's backslash commands; `options` describes the command-line options that can be passed to psql; and `variables` shows help about psql configuration variables.

`\;` [#](#APP-PSQL-META-COMMAND-SEMICOLON)

Backslash-semicolon is not a meta-command in the same way as the preceding commands; rather, it simply causes a semicolon to be added to the query buffer without any further processing.

Normally, psql will dispatch an SQL command to the server as soon as it reaches the command-ending semicolon, even if more input remains on the current line. Thus for example entering

select 1; select 2; select 3;

will result in the three SQL commands being individually sent to the server, with each one's results being displayed before continuing to the next command. However, a semicolon entered as `\;` will not trigger command processing, so that the command before it and the one after are effectively combined and sent to the server in one request. So for example

select 1\\; select 2\\; select 3;

results in sending the three SQL commands to the server in a single request, when the non-backslashed semicolon is reached. The server executes such a request as a single transaction, unless there are explicit `BEGIN`/`COMMIT` commands included in the string to divide it into multiple transactions. (See [Section 54.2.2.1](https://www.postgresql.org/docs/current/protocol-flow.html#PROTOCOL-FLOW-MULTI-STATEMENT "54.2.2.1. Multiple Statements in a Simple Query") for more details about how the server handles multi-query strings.)

#### Patterns

The various `\d` commands accept a _`pattern`_ parameter to specify the object name(s) to be displayed. In the simplest case, a pattern is just the exact name of the object. The characters within a pattern are normally folded to lower case, just as in SQL names; for example, `\dt FOO` will display the table named `foo`. As in SQL names, placing double quotes around a pattern stops folding to lower case. Should you need to include an actual double quote character in a pattern, write it as a pair of double quotes within a double-quote sequence; again this is in accord with the rules for SQL quoted identifiers. For example, `\dt "FOO""BAR"` will display the table named `FOO"BAR` (not `foo"bar`). Unlike the normal rules for SQL names, you can put double quotes around just part of a pattern, for instance `\dt FOO"FOO"BAR` will display the table named `fooFOObar`.

Whenever the _`pattern`_ parameter is omitted completely, the `\d` commands display all objects that are visible in the current schema search path — this is equivalent to using `*` as the pattern. (An object is said to be _visible_ if its containing schema is in the search path and no object of the same kind and name appears earlier in the search path. This is equivalent to the statement that the object can be referenced by name without explicit schema qualification.) To see all objects in the database regardless of visibility, use `*.*` as the pattern.

Within a pattern, `*` matches any sequence of characters (including no characters) and `?` matches any single character. (This notation is comparable to Unix shell file name patterns.) For example, `\dt int*` displays tables whose names begin with `int`. But within double quotes, `*` and `?` lose these special meanings and are just matched literally.

A relation pattern that contains a dot (`.`) is interpreted as a schema name pattern followed by an object name pattern. For example, `\dt foo*.*bar*` displays all tables whose table name includes `bar` that are in schemas whose schema name starts with `foo`. When no dot appears, then the pattern matches only objects that are visible in the current schema search path. Again, a dot within double quotes loses its special meaning and is matched literally. A relation pattern that contains two dots (`.`) is interpreted as a database name followed by a schema name pattern followed by an object name pattern. The database name portion will not be treated as a pattern and must match the name of the currently connected database, else an error will be raised.

A schema pattern that contains a dot (`.`) is interpreted as a database name followed by a schema name pattern. For example, `\dn mydb.*foo*` displays all schemas whose schema name includes `foo`. The database name portion will not be treated as a pattern and must match the name of the currently connected database, else an error will be raised.

Advanced users can use regular-expression notations such as character classes, for example `[0-9]` to match any digit. All regular expression special characters work as specified in [Section 9.7.3](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP "9.7.3. POSIX Regular Expressions"), except for `.` which is taken as a separator as mentioned above, `*` which is translated to the regular-expression notation `.*`, `?` which is translated to `.`, and `$` which is matched literally. You can emulate these pattern characters at need by writing `?` for `.`, ``(_`R`_+|)`` for ``_`R`_*``, or ``(_`R`_|)`` for ``_`R`_?``. `$` is not needed as a regular-expression character since the pattern must match the whole name, unlike the usual interpretation of regular expressions (in other words, `$` is automatically appended to your pattern). Write `*` at the beginning and/or end if you don't wish the pattern to be anchored. Note that within double quotes, all regular expression special characters lose their special meanings and are matched literally. Also, the regular expression special characters are matched literally in operator name patterns (i.e., the argument of `\do`).


