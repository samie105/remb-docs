---
title: "PostgreSQL: Documentation: 18: LOCK"
source: "https://www.postgresql.org/docs/current/sql-lock.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-lock.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:43:50.208Z"
content_hash: "3ac6f2065f6c8296f8cc51cea12a220827f61d1b9d55657798ee9af48bc02db2"
menu_path: ["PostgreSQL: Documentation: 18: LOCK"]
section_path: []
content_language: "en"
nav_prev: {"path": "../sql-listen.html/index.md", "title": "PostgreSQL: Documentation: 18: LISTEN"}
nav_next: {"path": "../sql-merge.html/index.md", "title": "PostgreSQL: Documentation: 18: MERGE"}
---

## Synopsis

LOCK \[ TABLE \] \[ ONLY \] _`name`_ \[ \* \] \[, ...\] \[ IN _`lockmode`_ MODE \] \[ NOWAIT \]

where _`lockmode`_ is one of:

    ACCESS SHARE | ROW SHARE | ROW EXCLUSIVE | SHARE UPDATE EXCLUSIVE
    | SHARE | SHARE ROW EXCLUSIVE | EXCLUSIVE | ACCESS EXCLUSIVE

## Description

`LOCK TABLE` obtains a table-level lock, waiting if necessary for any conflicting locks to be released. If `NOWAIT` is specified, `LOCK TABLE` does not wait to acquire the desired lock: if it cannot be acquired immediately, the command is aborted and an error is emitted. Once obtained, the lock is held for the remainder of the current transaction. (There is no `UNLOCK TABLE` command; locks are always released at transaction end.)

When a view is locked, all relations appearing in the view definition query are also locked recursively with the same lock mode.

When acquiring locks automatically for commands that reference tables, PostgreSQL always uses the least restrictive lock mode possible. `LOCK TABLE` provides for cases when you might need more restrictive locking. For example, suppose an application runs a transaction at the `READ COMMITTED` isolation level and needs to ensure that data in a table remains stable for the duration of the transaction. To achieve this you could obtain `SHARE` lock mode over the table before querying. This will prevent concurrent data changes and ensure subsequent reads of the table see a stable view of committed data, because `SHARE` lock mode conflicts with the `ROW EXCLUSIVE` lock acquired by writers, and your ``LOCK TABLE _`name`_ IN SHARE MODE`` statement will wait until any concurrent holders of `ROW EXCLUSIVE` mode locks commit or roll back. Thus, once you obtain the lock, there are no uncommitted writes outstanding; furthermore none can begin until you release the lock.

To achieve a similar effect when running a transaction at the `REPEATABLE READ` or `SERIALIZABLE` isolation level, you have to execute the `LOCK TABLE` statement before executing any `SELECT` or data modification statement. A `REPEATABLE READ` or `SERIALIZABLE` transaction's view of data will be frozen when its first `SELECT` or data modification statement begins. A `LOCK TABLE` later in the transaction will still prevent concurrent writes — but it won't ensure that what the transaction reads corresponds to the latest committed values.

If a transaction of this sort is going to change the data in the table, then it should use `SHARE ROW EXCLUSIVE` lock mode instead of `SHARE` mode. This ensures that only one transaction of this type runs at a time. Without this, a deadlock is possible: two transactions might both acquire `SHARE` mode, and then be unable to also acquire `ROW EXCLUSIVE` mode to actually perform their updates. (Note that a transaction's own locks never conflict, so a transaction can acquire `ROW EXCLUSIVE` mode when it holds `SHARE` mode — but not if anyone else holds `SHARE` mode.) To avoid deadlocks, make sure all transactions acquire locks on the same objects in the same order, and if multiple lock modes are involved for a single object, then transactions should always acquire the most restrictive mode first.

More information about the lock modes and locking strategies can be found in [Section 13.3](https://www.postgresql.org/docs/current/explicit-locking.html "13.3. Explicit Locking").

## Parameters

_`name`_

The name (optionally schema-qualified) of an existing table to lock. If `ONLY` is specified before the table name, only that table is locked. If `ONLY` is not specified, the table and all its descendant tables (if any) are locked. Optionally, `*` can be specified after the table name to explicitly indicate that descendant tables are included.

The command `LOCK TABLE a, b;` is equivalent to `LOCK TABLE a; LOCK TABLE b;`. The tables are locked one-by-one in the order specified in the `LOCK TABLE` command.

_`lockmode`_

The lock mode specifies which locks this lock conflicts with. Lock modes are described in [Section 13.3](https://www.postgresql.org/docs/current/explicit-locking.html "13.3. Explicit Locking").

If no lock mode is specified, then `ACCESS EXCLUSIVE`, the most restrictive mode, is used.

`NOWAIT`

Specifies that `LOCK TABLE` should not wait for any conflicting locks to be released: if the specified lock(s) cannot be acquired immediately without waiting, the transaction is aborted.

## Notes

To lock a table, the user must have the right privilege for the specified _`lockmode`_. If the user has `MAINTAIN`, `UPDATE`, `DELETE`, or `TRUNCATE` privileges on the table, any _`lockmode`_ is permitted. If the user has `INSERT` privileges on the table, `ROW EXCLUSIVE MODE` (or a less-conflicting mode as described in [Section 13.3](https://www.postgresql.org/docs/current/explicit-locking.html "13.3. Explicit Locking")) is permitted. If a user has `SELECT` privileges on the table, `ACCESS SHARE MODE` is permitted.

The user performing the lock on the view must have the corresponding privilege on the view. In addition, by default, the view's owner must have the relevant privileges on the underlying base relations, whereas the user performing the lock does not need any permissions on the underlying base relations. However, if the view has `security_invoker` set to `true` (see [`CREATE VIEW`](https://www.postgresql.org/docs/current/sql-createview.html "CREATE VIEW")), the user performing the lock, rather than the view owner, must have the relevant privileges on the underlying base relations.

`LOCK TABLE` is useless outside a transaction block: the lock would remain held only to the completion of the statement. Therefore PostgreSQL reports an error if `LOCK` is used outside a transaction block. Use [`BEGIN`](https://www.postgresql.org/docs/current/sql-begin.html "BEGIN") and [`COMMIT`](https://www.postgresql.org/docs/current/sql-commit.html "COMMIT") (or [`ROLLBACK`](https://www.postgresql.org/docs/current/sql-rollback.html "ROLLBACK")) to define a transaction block.

`LOCK TABLE` only deals with table-level locks, and so the mode names involving `ROW` are all misnomers. These mode names should generally be read as indicating the intention of the user to acquire row-level locks within the locked table. Also, `ROW EXCLUSIVE` mode is a shareable table lock. Keep in mind that all the lock modes have identical semantics so far as `LOCK TABLE` is concerned, differing only in the rules about which modes conflict with which. For information on how to acquire an actual row-level lock, see [Section 13.3.2](https://www.postgresql.org/docs/current/explicit-locking.html#LOCKING-ROWS "13.3.2. Row-Level Locks") and [The Locking Clause](https://www.postgresql.org/docs/current/sql-select.html#SQL-FOR-UPDATE-SHARE "The Locking Clause") in the [SELECT](https://www.postgresql.org/docs/current/sql-select.html "SELECT") documentation.

## Examples

Obtain a `SHARE` lock on a primary key table when going to perform inserts into a foreign key table:

BEGIN WORK;
LOCK TABLE films IN SHARE MODE;
SELECT id FROM films
    WHERE name = 'Star Wars: Episode I - The Phantom Menace';
-- Do ROLLBACK if record was not returned
INSERT INTO films\_user\_comments VALUES
    (\_id\_, 'GREAT! I was waiting for it for so long!');
COMMIT WORK;

Take a `SHARE ROW EXCLUSIVE` lock on a primary key table when going to perform a delete operation:

BEGIN WORK;
LOCK TABLE films IN SHARE ROW EXCLUSIVE MODE;
DELETE FROM films\_user\_comments WHERE id IN
    (SELECT id FROM films WHERE rating < 5);
DELETE FROM films WHERE rating < 5;
COMMIT WORK;

## Compatibility

There is no `LOCK TABLE` in the SQL standard, which instead uses `SET TRANSACTION` to specify concurrency levels on transactions. PostgreSQL supports that too; see [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION") for details.

Except for `ACCESS SHARE`, `ACCESS EXCLUSIVE`, and `SHARE UPDATE EXCLUSIVE` lock modes, the PostgreSQL lock modes and the `LOCK TABLE` syntax are compatible with those present in Oracle.
