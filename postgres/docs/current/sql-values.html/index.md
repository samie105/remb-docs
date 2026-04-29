---
title: "PostgreSQL: Documentation: 18: VALUES"
source: "https://www.postgresql.org/docs/current/sql-values.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-values.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:21.218Z"
content_hash: "10fd1dd724ff52373449c4ea9126ff6dacc77c7313327bec927a6389b6b3acf5"
menu_path: ["PostgreSQL: Documentation: 18: VALUES"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-vacuum.html/index.md", "title": "PostgreSQL: Documentation: 18: VACUUM"}
nav_next: {"path": "postgres/docs/current/ssh-tunnels.html/index.md", "title": "PostgreSQL: Documentation: 18: 18.11.\u00a0Secure TCP/IP Connections with SSH Tunnels"}
---

## Description

`VALUES` computes a row value or set of row values specified by value expressions. It is most commonly used to generate a “constant table” within a larger command, but it can be used on its own.

When more than one row is specified, all the rows must have the same number of elements. The data types of the resulting table's columns are determined by combining the explicit or inferred types of the expressions appearing in that column, using the same rules as for `UNION` (see [Section 10.5](https://www.postgresql.org/docs/current/typeconv-union-case.html "10.5. UNION, CASE, and Related Constructs")).

Within larger commands, `VALUES` is syntactically allowed anywhere that `SELECT` is. Because it is treated like a `SELECT` by the grammar, it is possible to use the `ORDER BY`, `LIMIT` (or equivalently `FETCH FIRST`), and `OFFSET` clauses with a `VALUES` command.

## Parameters

_`expression`_

A constant or expression to compute and insert at the indicated place in the resulting table (set of rows). In a `VALUES` list appearing at the top level of an `INSERT`, an _`expression`_ can be replaced by `DEFAULT` to indicate that the destination column's default value should be inserted. `DEFAULT` cannot be used when `VALUES` appears in other contexts.

_`sort_expression`_

An expression or integer constant indicating how to sort the result rows. This expression can refer to the columns of the `VALUES` result as `column1`, `column2`, etc. For more details see [ORDER BY Clause](https://www.postgresql.org/docs/current/sql-select.html#SQL-ORDERBY "ORDER BY Clause") in the [SELECT](https://www.postgresql.org/docs/current/sql-select.html "SELECT") documentation.

_`operator`_

A sorting operator. For details see [ORDER BY Clause](https://www.postgresql.org/docs/current/sql-select.html#SQL-ORDERBY "ORDER BY Clause") in the [SELECT](https://www.postgresql.org/docs/current/sql-select.html "SELECT") documentation.

_`count`_

The maximum number of rows to return. For details see [LIMIT Clause](https://www.postgresql.org/docs/current/sql-select.html#SQL-LIMIT "LIMIT Clause") in the [SELECT](https://www.postgresql.org/docs/current/sql-select.html "SELECT") documentation.

_`start`_

The number of rows to skip before starting to return rows. For details see [LIMIT Clause](https://www.postgresql.org/docs/current/sql-select.html#SQL-LIMIT "LIMIT Clause") in the [SELECT](https://www.postgresql.org/docs/current/sql-select.html "SELECT") documentation.

## Notes

`VALUES` lists with very large numbers of rows should be avoided, as you might encounter out-of-memory failures or poor performance. `VALUES` appearing within `INSERT` is a special case (because the desired column types are known from the `INSERT`'s target table, and need not be inferred by scanning the `VALUES` list), so it can handle larger lists than are practical in other contexts.

## Examples

A bare `VALUES` command:

VALUES (1, 'one'), (2, 'two'), (3, 'three');

This will return a table of two columns and three rows. It's effectively equivalent to:

SELECT 1 AS column1, 'one' AS column2
UNION ALL
SELECT 2, 'two'
UNION ALL
SELECT 3, 'three';

More usually, `VALUES` is used within a larger SQL command. The most common use is in `INSERT`:

INSERT INTO films (code, title, did, date\_prod, kind)
    VALUES ('T\_601', 'Yojimbo', 106, '1961-06-16', 'Drama');

In the context of `INSERT`, entries of a `VALUES` list can be `DEFAULT` to indicate that the column default should be used here instead of specifying a value:

INSERT INTO films VALUES
    ('UA502', 'Bananas', 105, DEFAULT, 'Comedy', '82 minutes'),
    ('T\_601', 'Yojimbo', 106, DEFAULT, 'Drama', DEFAULT);

`VALUES` can also be used where a sub-`SELECT` might be written, for example in a `FROM` clause:

SELECT f.\*
  FROM films f, (VALUES('MGM', 'Horror'), ('UA', 'Sci-Fi')) AS t (studio, kind)
  WHERE f.studio = t.studio AND f.kind = t.kind;

UPDATE employees SET salary = salary \* v.increase
  FROM (VALUES(1, 200000, 1.2), (2, 400000, 1.4)) AS v (depno, target, increase)
  WHERE employees.depno = v.depno AND employees.sales >= v.target;

Note that an `AS` clause is required when `VALUES` is used in a `FROM` clause, just as is true for `SELECT`. It is not required that the `AS` clause specify names for all the columns, but it's good practice to do so. (The default column names for `VALUES` are `column1`, `column2`, etc. in PostgreSQL, but these names might be different in other database systems.)

When `VALUES` is used in `INSERT`, the values are all automatically coerced to the data type of the corresponding destination column. When it's used in other contexts, it might be necessary to specify the correct data type. If the entries are all quoted literal constants, coercing the first is sufficient to determine the assumed type for all:

SELECT \* FROM machines
WHERE ip\_address IN (VALUES('192.168.0.1'::inet), ('192.168.0.10'), ('192.168.1.43'));

### Tip

For simple `IN` tests, it's better to rely on the [list-of-scalars](https://www.postgresql.org/docs/current/functions-comparisons.html#FUNCTIONS-COMPARISONS-IN-SCALAR "9.25.1. IN") form of `IN` than to write a `VALUES` query as shown above. The list of scalars method requires less writing and is often more efficient.

## Compatibility

`VALUES` conforms to the SQL standard. `LIMIT` and `OFFSET` are PostgreSQL extensions; see also under [SELECT](https://www.postgresql.org/docs/current/sql-select.html "SELECT").
