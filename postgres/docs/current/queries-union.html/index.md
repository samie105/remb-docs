---
title: "PostgreSQL: Documentation: 18: 7.4. Combining Queries (UNION, INTERSECT, EXCEPT)"
source: "https://www.postgresql.org/docs/current/queries-union.html"
canonical_url: "https://www.postgresql.org/docs/current/queries-union.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:49.829Z"
content_hash: "9a987f3dfb092e620dffb623b7b09d985d89977a3da668ede2c84205711a3f06"
menu_path: ["PostgreSQL: Documentation: 18: 7.4. Combining Queries (UNION, INTERSECT, EXCEPT)"]
section_path: []
---
The results of two queries can be combined using the set operations union, intersection, and difference. The syntax is

_`query1`_ UNION \[ALL\] _`query2`_
_`query1`_ INTERSECT \[ALL\] _`query2`_
_`query1`_ EXCEPT \[ALL\] _`query2`_

where _`query1`_ and _`query2`_ are queries that can use any of the features discussed up to this point.

`UNION` effectively appends the result of _`query2`_ to the result of _`query1`_ (although there is no guarantee that this is the order in which the rows are actually returned). Furthermore, it eliminates duplicate rows from its result, in the same way as `DISTINCT`, unless `UNION ALL` is used.

`INTERSECT` returns all rows that are both in the result of _`query1`_ and in the result of _`query2`_. Duplicate rows are eliminated unless `INTERSECT ALL` is used.

`EXCEPT` returns all rows that are in the result of _`query1`_ but not in the result of _`query2`_. (This is sometimes called the _difference_ between two queries.) Again, duplicates are eliminated unless `EXCEPT ALL` is used.

In order to calculate the union, intersection, or difference of two queries, the two queries must be “union compatible”, which means that they return the same number of columns and the corresponding columns have compatible data types, as described in [Section 10.5](https://www.postgresql.org/docs/current/typeconv-union-case.html "10.5. UNION, CASE, and Related Constructs").

Set operations can be combined, for example

_`query1`_ UNION _`query2`_ EXCEPT _`query3`_

which is equivalent to

(_`query1`_ UNION _`query2`_) EXCEPT _`query3`_

As shown here, you can use parentheses to control the order of evaluation. Without parentheses, `UNION` and `EXCEPT` associate left-to-right, but `INTERSECT` binds more tightly than those two operators. Thus

_`query1`_ UNION _`query2`_ INTERSECT _`query3`_

means

_`query1`_ UNION (_`query2`_ INTERSECT _`query3`_)

You can also surround an individual _`query`_ with parentheses. This is important if the _`query`_ needs to use any of the clauses discussed in following sections, such as `LIMIT`. Without parentheses, you'll get a syntax error, or else the clause will be understood as applying to the output of the set operation rather than one of its inputs. For example,

SELECT a FROM b UNION SELECT x FROM y LIMIT 10

is accepted, but it means

(SELECT a FROM b UNION SELECT x FROM y) LIMIT 10

not

SELECT a FROM b UNION (SELECT x FROM y LIMIT 10)
