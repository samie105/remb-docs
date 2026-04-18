---
title: "Search concepts"
source: "https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/"
canonical_url: "https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:11:29.135Z"
content_hash: "35a9af8ae4d3bfd4040c0146f2ad054b9feba7a6cb1905a23a4f9adf099bfee3"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Search concepts","→","Search concepts"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Search concepts","→","Search concepts"]
---
# Search concepts

Details about query syntax, aggregation, scoring, and other search and query options

Redis Open Source supports the following Redis Search features. This article provides you an overview.

## Indexing features

*   Secondary indexing
*   Vector indexing
*   Index on [JSON](/docs/latest/develop/data-types/json/) documents
*   Full-text indexing of multiple fields in a document
*   Incremental indexing without performance loss
*   Document deletion and updating with index garbage collection

## Query features

*   Multi-field queries
*   Query on [JSON](/docs/latest/develop/data-types/json/) documents
*   [Aggregation](/docs/latest/develop/ai/search-and-query/advanced-concepts/aggregations/)
*   Boolean queries with AND, OR, and NOT operators between subqueries
*   Optional query clauses
*   Retrieval of full document contents or only their IDs
*   Exact phrase search and slop-based search
*   Numeric filters and ranges
*   Geo-filtering using Redis [geo commands](/docs/latest/commands/?group=geo)
*   [Vector search](/docs/latest/develop/ai/search-and-query/vectors/)
*   [Key and field expiration behavior](/docs/latest/develop/ai/search-and-query/advanced-concepts/expiration/)

## Full-text search features

*   [Prefix-based searches](/docs/latest/develop/ai/search-and-query/query/#prefix-matching)
*   Field weights
*   [Auto-complete](/docs/latest/develop/ai/search-and-query/administration/overview/#auto-complete) and fuzzy prefix suggestions
*   [Stemming](/docs/latest/develop/ai/search-and-query/advanced-concepts/stemming/)\-based query expansion for [many languages](/docs/latest/develop/ai/search-and-query/advanced-concepts/stemming/#supported-languages) using [Snowball](http://snowballstem.org/)
*   Support for custom functions for query expansion and scoring (see [Extensions](/docs/latest/develop/ai/search-and-query/administration/extensions/))
*   Unicode support (UTF-8 input required)
*   Document ranking

## Cluster support

The Redis Search features of Redis Open Source are also available for distributed databases that can scale to billions of documents and hundreds of servers.

## Supported platforms

Redis Open Source is developed and tested on Linux and macOS on x86\_64 CPUs.

Atom CPUs are not supported.

  

## On this page
