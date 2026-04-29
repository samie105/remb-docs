---
title: "PostgreSQL: Documentation: 18: 9.26. Set Returning Functions"
source: "https://www.postgresql.org/docs/current/functions-srf.html"
canonical_url: "https://www.postgresql.org/docs/current/functions-srf.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:49:59.031Z"
content_hash: "d2be562521fdf4d3cf73180f874e8be1c648dba5415fdb9bdf395f2d2d2ae153"
menu_path: ["PostgreSQL: Documentation: 18: 9.26. Set Returning Functions"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/functions-matching.html/index.md", "title": "PostgreSQL: Documentation: 18: 9.7.\u00a0Pattern Matching"}
nav_next: {"path": "postgres/docs/current/functions-statistics.html/index.md", "title": "PostgreSQL: Documentation: 18: 9.31.\u00a0Statistics Information Functions"}
---

This section describes functions that possibly return more than one row. The most widely used functions in this class are series generating functions, as detailed in [Table 9.69](https://www.postgresql.org/docs/current/functions-srf.html#FUNCTIONS-SRF-SERIES "Table 9.69. Series Generating Functions") and [Table 9.70](https://www.postgresql.org/docs/current/functions-srf.html#FUNCTIONS-SRF-SUBSCRIPTS "Table 9.70. Subscript Generating Functions"). Other, more specialized set-returning functions are described elsewhere in this manual. See [Section 7.2.1.4](https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-TABLEFUNCTIONS "7.2.1.4. Table Functions") for ways to combine multiple set-returning functions.

**Table 9.69. Series Generating Functions**

| 
Function

Description

 |
| --- |
| 

`generate_series` ( _`start`_ `integer`, _`stop`_ `integer` \[, _`step`_ `integer` \] ) → `setof integer`

`generate_series` ( _`start`_ `bigint`, _`stop`_ `bigint` \[, _`step`_ `bigint` \] ) → `setof bigint`

`generate_series` ( _`start`_ `numeric`, _`stop`_ `numeric` \[, _`step`_ `numeric` \] ) → `setof numeric`

Generates a series of values from _`start`_ to _`stop`_, with a step size of _`step`_. _`step`_ defaults to 1.

 |
| 

`generate_series` ( _`start`_ `timestamp`, _`stop`_ `timestamp`, _`step`_ `interval` ) → `setof timestamp`

`generate_series` ( _`start`_ `timestamp with time zone`, _`stop`_ `timestamp with time zone`, _`step`_ `interval` \[, _`timezone`_ `text` \] ) → `setof timestamp with time zone`

Generates a series of values from _`start`_ to _`stop`_, with a step size of _`step`_. In the timezone-aware form, times of day and daylight-savings adjustments are computed according to the time zone named by the _`timezone`_ argument, or the current [TimeZone](../runtime-config-client.html/index.md#GUC-TIMEZONE) setting if that is omitted.

 |

When _`step`_ is positive, zero rows are returned if _`start`_ is greater than _`stop`_. Conversely, when _`step`_ is negative, zero rows are returned if _`start`_ is less than _`stop`_. Zero rows are also returned if any input is `NULL`. It is an error for _`step`_ to be zero. Some examples follow:

SELECT \* FROM generate\_series(2,4);
 generate\_series
-----------------
               2
               3
               4
(3 rows)

SELECT \* FROM generate\_series(5,1,-2);
 generate\_series
-----------------
               5
               3
               1
(3 rows)

SELECT \* FROM generate\_series(4,3);
 generate\_series
-----------------
(0 rows)

SELECT generate\_series(1.1, 4, 1.3);
 generate\_series
-----------------
             1.1
             2.4
             3.7
(3 rows)

-- this example relies on the date-plus-integer operator:
SELECT current\_date + s.a AS dates FROM generate\_series(0,14,7) AS s(a);
   dates
------------
 2004-02-05
 2004-02-12
 2004-02-19
(3 rows)

SELECT \* FROM generate\_series('2008-03-01 00:00'::timestamp,
                              '2008-03-04 12:00', '10 hours');
   generate\_series
---------------------
 2008-03-01 00:00:00
 2008-03-01 10:00:00
 2008-03-01 20:00:00
 2008-03-02 06:00:00
 2008-03-02 16:00:00
 2008-03-03 02:00:00
 2008-03-03 12:00:00
 2008-03-03 22:00:00
 2008-03-04 08:00:00
(9 rows)

-- this example assumes that TimeZone is set to UTC; note the DST transition:
SELECT \* FROM generate\_series('2001-10-22 00:00 -04:00'::timestamptz,
                              '2001-11-01 00:00 -05:00'::timestamptz,
                              '1 day'::interval, 'America/New\_York');
    generate\_series
------------------------
 2001-10-22 04:00:00+00
 2001-10-23 04:00:00+00
 2001-10-24 04:00:00+00
 2001-10-25 04:00:00+00
 2001-10-26 04:00:00+00
 2001-10-27 04:00:00+00
 2001-10-28 04:00:00+00
 2001-10-29 05:00:00+00
 2001-10-30 05:00:00+00
 2001-10-31 05:00:00+00
 2001-11-01 05:00:00+00
(11 rows)

**Table 9.70. Subscript Generating Functions**

| 
Function

Description

 |
| --- |
| 

`generate_subscripts` ( _`array`_ `anyarray`, _`dim`_ `integer` ) → `setof integer`

Generates a series comprising the valid subscripts of the _`dim`_'th dimension of the given array.

 |
| 

`generate_subscripts` ( _`array`_ `anyarray`, _`dim`_ `integer`, _`reverse`_ `boolean` ) → `setof integer`

Generates a series comprising the valid subscripts of the _`dim`_'th dimension of the given array. When _`reverse`_ is true, returns the series in reverse order.

 |

`generate_subscripts` is a convenience function that generates the set of valid subscripts for the specified dimension of the given array. Zero rows are returned for arrays that do not have the requested dimension, or if any input is `NULL`. Some examples follow:

\-- basic usage:
SELECT generate\_subscripts('{NULL,1,NULL,2}'::int\[\], 1) AS s;
 s
---
 1
 2
 3
 4
(4 rows)

-- presenting an array, the subscript and the subscripted
-- value requires a subquery:
SELECT \* FROM arrays;
         a
--------------------
 {-1,-2}
 {100,200,300}
(2 rows)

SELECT a AS array, s AS subscript, a\[s\] AS value
FROM (SELECT generate\_subscripts(a, 1) AS s, a FROM arrays) foo;
     array     | subscript | value
---------------+-----------+-------
 {-1,-2}       |         1 |    -1
 {-1,-2}       |         2 |    -2
 {100,200,300} |         1 |   100
 {100,200,300} |         2 |   200
 {100,200,300} |         3 |   300
(5 rows)

-- unnest a 2D array:
CREATE OR REPLACE FUNCTION unnest2(anyarray)
RETURNS SETOF anyelement AS $$
select $1\[i\]\[j\]
   from generate\_subscripts($1,1) g1(i),
        generate\_subscripts($1,2) g2(j);
$$ LANGUAGE sql IMMUTABLE;
CREATE FUNCTION
SELECT \* FROM unnest2(ARRAY\[\[1,2\],\[3,4\]\]);
 unnest2
---------
       1
       2
       3
       4
(4 rows)

When a function in the `FROM` clause is suffixed by `WITH ORDINALITY`, a `bigint` column is appended to the function's output column(s), which starts from 1 and increments by 1 for each row of the function's output. This is most useful in the case of set returning functions such as `unnest()`.

\-- set returning function WITH ORDINALITY:
SELECT \* FROM pg\_ls\_dir('.') WITH ORDINALITY AS t(ls,n);
       ls        | n
-----------------+----
 pg\_serial       |  1
 pg\_twophase     |  2
 postmaster.opts |  3
 pg\_notify       |  4
 postgresql.conf |  5
 pg\_tblspc       |  6
 logfile         |  7
 base            |  8
 postmaster.pid  |  9
 pg\_ident.conf   | 10
 global          | 11
 pg\_xact         | 12
 pg\_snapshots    | 13
 pg\_multixact    | 14
 PG\_VERSION      | 15
 pg\_wal          | 16
 pg\_hba.conf     | 17
 pg\_stat\_tmp     | 18
 pg\_subtrans     | 19
(19 rows)
