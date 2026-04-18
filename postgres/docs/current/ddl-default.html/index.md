---
title: "PostgreSQL: Documentation: 18: 5.2. Default Values"
source: "https://www.postgresql.org/docs/current/ddl-default.html"
canonical_url: "https://www.postgresql.org/docs/current/ddl-default.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:12.842Z"
content_hash: "182348e97af213f9a226e3e86f705d464a8c544dcda7712a1f7852e64eada49a"
menu_path: ["PostgreSQL: Documentation: 18: 5.2. Default Values"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-syntax-lexical.html/index.md", "title": "PostgreSQL: Documentation: 18: 4.1.\u00a0Lexical Structure"}
nav_next: {"path": "postgres/docs/current/app-pgwalsummary.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_walsummary"}
---

A column can be assigned a default value. When a new row is created and no values are specified for some of the columns, those columns will be filled with their respective default values. A data manipulation command can also request explicitly that a column be set to its default value, without having to know what that value is. (Details about data manipulation commands are in [Chapter 6](https://www.postgresql.org/docs/current/dml.html "Chapter 6. Data Manipulation").)

If no default value is declared explicitly, the default value is the null value. This usually makes sense because a null value can be considered to represent unknown data.

In a table definition, default values are listed after the column data type. For example:

CREATE TABLE products (
    product\_no integer,
    name text,
    price numeric **DEFAULT 9.99**
);

The default value can be an expression, which will be evaluated whenever the default value is inserted (_not_ when the table is created). A common example is for a `timestamp` column to have a default of `CURRENT_TIMESTAMP`, so that it gets set to the time of row insertion. Another common example is generating a “serial number” for each row. In PostgreSQL this is typically done by something like:

CREATE TABLE products (
    product\_no integer **DEFAULT nextval('products\_product\_no\_seq')**,
    ...
);

where the `nextval()` function supplies successive values from a _sequence object_ (see [Section 9.17](https://www.postgresql.org/docs/current/functions-sequence.html "9.17. Sequence Manipulation Functions")). This arrangement is sufficiently common that there's a special shorthand for it:

CREATE TABLE products (
    product\_no **SERIAL**,
    ...
);

The `SERIAL` shorthand is discussed further in [Section 8.1.4](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-SERIAL "8.1.4. Serial Types").

