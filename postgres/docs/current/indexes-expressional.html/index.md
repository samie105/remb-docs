---
title: "PostgreSQL: Documentation: 18: 11.7. Indexes on Expressions"
source: "https://www.postgresql.org/docs/current/indexes-expressional.html"
canonical_url: "https://www.postgresql.org/docs/current/indexes-expressional.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:54.333Z"
content_hash: "b53f5bc0ff213b31b6e66ce329160053019bd0b226ed83d7915526ed18cc6dae"
menu_path: ["PostgreSQL: Documentation: 18: 11.7. Indexes on Expressions"]
section_path: []
nav_prev: {"path": "postgres/docs/current/spi-spi-gettype.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_gettype"}
nav_next: {"path": "postgres/docs/current/indexes-partial.html/index.md", "title": "PostgreSQL: Documentation: 18: 11.8.\u00a0Partial Indexes"}
---

An index column need not be just a column of the underlying table, but can be a function or scalar expression computed from one or more columns of the table. This feature is useful to obtain fast access to tables based on the results of computations.

For example, a common way to do case-insensitive comparisons is to use the `lower` function:

SELECT \* FROM test1 WHERE lower(col1) = 'value';

This query can use an index if one has been defined on the result of the `lower(col1)` function:

CREATE INDEX test1\_lower\_col1\_idx ON test1 (lower(col1));

If we were to declare this index `UNIQUE`, it would prevent creation of rows whose `col1` values differ only in case, as well as rows whose `col1` values are actually identical. Thus, indexes on expressions can be used to enforce constraints that are not definable as simple unique constraints.

As another example, if one often does queries like:

SELECT \* FROM people WHERE (first\_name || ' ' || last\_name) = 'John Smith';

then it might be worth creating an index like this:

CREATE INDEX people\_names ON people ((first\_name || ' ' || last\_name));

The syntax of the `CREATE INDEX` command normally requires writing parentheses around index expressions, as shown in the second example. The parentheses can be omitted when the expression is just a function call, as in the first example.

Index expressions are relatively expensive to maintain, because the derived expression(s) must be computed for each row insertion and [non-HOT update](https://www.postgresql.org/docs/current/storage-hot.html "66.7. Heap-Only Tuples (HOT)"). However, the index expressions are _not_ recomputed during an indexed search, since they are already stored in the index. In both examples above, the system sees the query as just `WHERE indexedcolumn = 'constant'` and so the speed of the search is equivalent to any other simple index query. Thus, indexes on expressions are useful when retrieval speed is more important than insertion and update speed.

