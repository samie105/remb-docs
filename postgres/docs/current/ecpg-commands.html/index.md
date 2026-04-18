---
title: "PostgreSQL: Documentation: 18: 34.3. Running SQL Commands"
source: "https://www.postgresql.org/docs/current/ecpg-commands.html"
canonical_url: "https://www.postgresql.org/docs/current/ecpg-commands.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:11.637Z"
content_hash: "cc530570a118a69bc32d4ef7d088621cca4d74e3a4285bc5a0d562b5a4baa61c"
menu_path: ["PostgreSQL: Documentation: 18: 34.3. Running SQL Commands"]
section_path: []
nav_prev: {"path": "postgres/docs/current/predefined-roles.html/index.md", "title": "PostgreSQL: Documentation: 18: 21.5.\u00a0Predefined Roles"}
nav_next: {"path": "postgres/docs/current/infoschema-parameters.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.33.\u00a0parameters"}
---

Any SQL command can be run from within an embedded SQL application. Below are some examples of how to do that.

### 34.3.1. Executing SQL Statements [#](#ECPG-EXECUTING)

Creating a table:

EXEC SQL CREATE TABLE foo (number integer, ascii char(16));
EXEC SQL CREATE UNIQUE INDEX num1 ON foo(number);
EXEC SQL COMMIT;

Inserting rows:

EXEC SQL INSERT INTO foo (number, ascii) VALUES (9999, 'doodad');
EXEC SQL COMMIT;

Deleting rows:

EXEC SQL DELETE FROM foo WHERE number = 9999;
EXEC SQL COMMIT;

Updates:

EXEC SQL UPDATE foo
    SET ascii = 'foobar'
    WHERE number = 9999;
EXEC SQL COMMIT;

`SELECT` statements that return a single result row can also be executed using `EXEC SQL` directly. To handle result sets with multiple rows, an application has to use a cursor; see [Section 34.3.2](https://www.postgresql.org/docs/current/ecpg-commands.html#ECPG-CURSORS "34.3.2. Using Cursors") below. (As a special case, an application can fetch multiple rows at once into an array host variable; see [Section 34.4.4.3.1](https://www.postgresql.org/docs/current/ecpg-variables.html#ECPG-VARIABLES-ARRAYS "34.4.4.3.1. Arrays").)

Single-row select:

EXEC SQL SELECT foo INTO :FooBar FROM table1 WHERE ascii = 'doodad';

Also, a configuration parameter can be retrieved with the `SHOW` command:

EXEC SQL SHOW search\_path INTO :var;

The tokens of the form ``:_`something`_`` are _host variables_, that is, they refer to variables in the C program. They are explained in [Section 34.4](https://www.postgresql.org/docs/current/ecpg-variables.html "34.4. Using Host Variables").

### 34.3.2. Using Cursors [#](#ECPG-CURSORS)

To retrieve a result set holding multiple rows, an application has to declare a cursor and fetch each row from the cursor. The steps to use a cursor are the following: declare a cursor, open it, fetch a row from the cursor, repeat, and finally close it.

Select using cursors:

EXEC SQL DECLARE foo\_bar CURSOR FOR
    SELECT number, ascii FROM foo
    ORDER BY ascii;
EXEC SQL OPEN foo\_bar;
EXEC SQL FETCH foo\_bar INTO :FooBar, DooDad;
...
EXEC SQL CLOSE foo\_bar;
EXEC SQL COMMIT;

For more details about declaring a cursor, see [DECLARE](https://www.postgresql.org/docs/current/ecpg-sql-declare.html "DECLARE"); for more details about fetching rows from a cursor, see [FETCH](https://www.postgresql.org/docs/current/sql-fetch.html "FETCH").

### Note

The ECPG `DECLARE` command does not actually cause a statement to be sent to the PostgreSQL backend. The cursor is opened in the backend (using the backend's `DECLARE` command) at the point when the `OPEN` command is executed.

### 34.3.3. Managing Transactions [#](#ECPG-TRANSACTIONS)

In the default mode, statements are committed only when `EXEC SQL COMMIT` is issued. The embedded SQL interface also supports autocommit of transactions (similar to psql's default behavior) via the `-t` command-line option to `ecpg` (see [ecpg](https://www.postgresql.org/docs/current/app-ecpg.html "ecpg")) or via the `EXEC SQL SET AUTOCOMMIT TO ON` statement. In autocommit mode, each command is automatically committed unless it is inside an explicit transaction block. This mode can be explicitly turned off using `EXEC SQL SET AUTOCOMMIT TO OFF`.

The following transaction management commands are available:

`EXEC SQL COMMIT` [#](#ECPG-TRANSACTIONS-EXEC-SQL-COMMIT)

Commit an in-progress transaction.

`EXEC SQL ROLLBACK` [#](#ECPG-TRANSACTIONS-EXEC-SQL-ROLLBACK)

Roll back an in-progress transaction.

`EXEC SQL PREPARE TRANSACTION` _`transaction_id`_ [#](#ECPG-TRANSACTIONS-EXEC-SQL-PREPARE-TRANSACTION)

Prepare the current transaction for two-phase commit.

`EXEC SQL COMMIT PREPARED` _`transaction_id`_ [#](#ECPG-TRANSACTIONS-EXEC-SQL-COMMIT-PREPARED)

Commit a transaction that is in prepared state.

`EXEC SQL ROLLBACK PREPARED` _`transaction_id`_ [#](#ECPG-TRANSACTIONS-EXEC-SQL-ROLLBACK-PREPARED)

Roll back a transaction that is in prepared state.

`EXEC SQL SET AUTOCOMMIT TO ON` [#](#ECPG-TRANSACTIONS-EXEC-SQL-AUTOCOMMIT-ON)

Enable autocommit mode.

`EXEC SQL SET AUTOCOMMIT TO OFF` [#](#ECPG-TRANSACTIONS-EXEC-SQL-AUTOCOMMIT-OFF)

Disable autocommit mode. This is the default.

### 34.3.4. Prepared Statements [#](#ECPG-PREPARED)

When the values to be passed to an SQL statement are not known at compile time, or the same statement is going to be used many times, then prepared statements can be useful.

The statement is prepared using the command `PREPARE`. For the values that are not known yet, use the placeholder “`?`”:

EXEC SQL PREPARE stmt1 FROM "SELECT oid, datname FROM pg\_database WHERE oid = ?";

If a statement returns a single row, the application can call `EXECUTE` after `PREPARE` to execute the statement, supplying the actual values for the placeholders with a `USING` clause:

EXEC SQL EXECUTE stmt1 INTO :dboid, :dbname USING 1;

If a statement returns multiple rows, the application can use a cursor declared based on the prepared statement. To bind input parameters, the cursor must be opened with a `USING` clause:

EXEC SQL PREPARE stmt1 FROM "SELECT oid,datname FROM pg\_database WHERE oid > ?";
EXEC SQL DECLARE foo\_bar CURSOR FOR stmt1;

/\* when end of result set reached, break out of while loop \*/
EXEC SQL WHENEVER NOT FOUND DO BREAK;

EXEC SQL OPEN foo\_bar USING 100;
...
while (1)
{
    EXEC SQL FETCH NEXT FROM foo\_bar INTO :dboid, :dbname;
    ...
}
EXEC SQL CLOSE foo\_bar;

When you don't need the prepared statement anymore, you should deallocate it:

EXEC SQL DEALLOCATE PREPARE _`name`_;

For more details about `PREPARE`, see [PREPARE](https://www.postgresql.org/docs/current/ecpg-sql-prepare.html "PREPARE"). Also see [Section 34.5](https://www.postgresql.org/docs/current/ecpg-dynamic.html "34.5. Dynamic SQL") for more details about using placeholders and input parameters.


