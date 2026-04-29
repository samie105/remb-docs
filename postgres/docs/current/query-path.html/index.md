---
title: "PostgreSQL: Documentation: 18: 51.1. The Path of a Query"
source: "https://www.postgresql.org/docs/current/query-path.html"
canonical_url: "https://www.postgresql.org/docs/current/query-path.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:42.669Z"
content_hash: "838a1f1a0d245d89abd2b0c212cb100efb7542edb8a36ec6f3e0b3d643a20102"
menu_path: ["PostgreSQL: Documentation: 18: 51.1. The Path of a Query"]
section_path: []
nav_prev: {"path": "../queries-values.html/index.md", "title": "PostgreSQL: Documentation: 18: 7.7.\u00a0VALUES Lists"}
nav_next: {"path": "../rangetypes.html/index.md", "title": "PostgreSQL: Documentation: 18: 8.17.\u00a0Range Types"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/query-path.html "PostgreSQL 18 - 51.1. The Path of a Query") ([18](/docs/18/query-path.html "PostgreSQL 18 - 51.1. The Path of a Query")) / [17](/docs/17/query-path.html "PostgreSQL 17 - 51.1. The Path of a Query") / [16](/docs/16/query-path.html "PostgreSQL 16 - 51.1. The Path of a Query") / [15](/docs/15/query-path.html "PostgreSQL 15 - 51.1. The Path of a Query") / [14](/docs/14/query-path.html "PostgreSQL 14 - 51.1. The Path of a Query")

Development Versions: [devel](/docs/devel/query-path.html "PostgreSQL devel - 51.1. The Path of a Query")

Unsupported versions: [13](/docs/13/query-path.html "PostgreSQL 13 - 51.1. The Path of a Query") / [12](/docs/12/query-path.html "PostgreSQL 12 - 51.1. The Path of a Query") / [11](/docs/11/query-path.html "PostgreSQL 11 - 51.1. The Path of a Query") / [10](/docs/10/query-path.html "PostgreSQL 10 - 51.1. The Path of a Query") / [9.6](/docs/9.6/query-path.html "PostgreSQL 9.6 - 51.1. The Path of a Query") / [9.5](/docs/9.5/query-path.html "PostgreSQL 9.5 - 51.1. The Path of a Query") / [9.4](/docs/9.4/query-path.html "PostgreSQL 9.4 - 51.1. The Path of a Query") / [9.3](/docs/9.3/query-path.html "PostgreSQL 9.3 - 51.1. The Path of a Query") / [9.2](/docs/9.2/query-path.html "PostgreSQL 9.2 - 51.1. The Path of a Query") / [9.1](/docs/9.1/query-path.html "PostgreSQL 9.1 - 51.1. The Path of a Query") / [9.0](/docs/9.0/query-path.html "PostgreSQL 9.0 - 51.1. The Path of a Query") / [8.4](/docs/8.4/query-path.html "PostgreSQL 8.4 - 51.1. The Path of a Query") / [8.3](/docs/8.3/query-path.html "PostgreSQL 8.3 - 51.1. The Path of a Query") / [8.2](/docs/8.2/query-path.html "PostgreSQL 8.2 - 51.1. The Path of a Query")

## 51.1. The Path of a Query [#](#QUERY-PATH)

Here we give a short overview of the stages a query has to pass to obtain a result.

1.  A connection from an application program to the PostgreSQL server has to be established. The application program transmits a query to the server and waits to receive the results sent back by the server.
    
2.  The _parser stage_ checks the query transmitted by the application program for correct syntax and creates a _query tree_.
    
3.  The _rewrite system_ takes the query tree created by the parser stage and looks for any _rules_ (stored in the _system catalogs_) to apply to the query tree. It performs the transformations given in the _rule bodies_.
    
    One application of the rewrite system is in the realization of _views_. Whenever a query against a view (i.e., a _virtual table_) is made, the rewrite system rewrites the user's query to a query that accesses the _base tables_ given in the _view definition_ instead.
    
4.  The _planner/optimizer_ takes the (rewritten) query tree and creates a _query plan_ that will be the input to the _executor_.
    
    It does so by first creating all possible _paths_ leading to the same result. For example if there is an index on a relation to be scanned, there are two paths for the scan. One possibility is a simple sequential scan and the other possibility is to use the index. Next the cost for the execution of each path is estimated and the cheapest path is chosen. The cheapest path is expanded into a complete plan that the executor can use.
    
5.  The executor recursively steps through the _plan tree_ and retrieves rows in the way represented by the plan. The executor makes use of the _storage system_ while scanning relations, performs _sorts_ and _joins_, evaluates _qualifications_ and finally hands back the rows derived.
    

In the following sections we will cover each of the above listed items in more detail to give a better understanding of PostgreSQL's internal control and data structures.

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/query-path.html/) to report a documentation issue.
