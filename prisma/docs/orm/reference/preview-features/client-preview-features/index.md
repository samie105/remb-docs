---
title: "Prisma Client & Prisma schema"
source: "https://www.prisma.io/docs/orm/reference/preview-features/client-preview-features"
canonical_url: "https://www.prisma.io/docs/orm/reference/preview-features/client-preview-features"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:19.475Z"
content_hash: "a35c63919621da4c9d34434b6f926a32b2367daa6db569a8a077a8630306b6f9"
menu_path: ["Prisma Client & Prisma schema"]
section_path: []
---
Prisma Client and Prisma schema features that are currently in Preview

When we release a new Prisma Client or Prisma schema feature, it often starts in Preview so that you can test it and submit your feedback. After we improve the feature with your feedback and are satisfied with the internal test results, we promote the feature to general availability.

For more information, see [ORM releases and maturity levels](https://www.prisma.io/docs/orm/more/releases).

The following [Preview](https://www.prisma.io/docs/orm/more/releases#preview) feature flags are available for Prisma Client and Prisma schema:

Feature

Released into Preview

Feedback issue

[`views`](https://www.prisma.io/docs/orm/prisma-schema/data-model/views)

[4.9.0](https://github.com/prisma/prisma/releases/tag/4.9.0)

[Submit feedback](https://github.com/prisma/prisma/issues/17335)

`relationJoins`

[5.7.0](https://github.com/prisma/prisma/releases/tag/5.7.0)

[Submit feedback](https://github.com/prisma/prisma/discussions/22288)

`nativeDistinct`

[5.7.0](https://github.com/prisma/prisma/releases/tag/5.7.0)

[Submit feedback](https://github.com/prisma/prisma/discussions/22287)

`typedSql`

[5.19.0](https://github.com/prisma/prisma/releases/tag/5.19.0)

[Submit feedback](https://github.com/prisma/prisma/discussions/25106)

`strictUndefinedChecks`

[5.20.0](https://github.com/prisma/prisma/releases/tag/5.20.0)

[Submit feedback](https://github.com/prisma/prisma/discussions/25271)

[`fullTextSearchPostgres`](https://www.prisma.io/docs/v6/orm/prisma-client/queries/full-text-search)

[6.0.0](https://github.com/prisma/prisma/releases/tag/6.0.0)

[Submit feedback](https://github.com/prisma/prisma/issues/25773)

`shardKeys`

[6.10.0](https://pris.ly/release/6.10.0)

[Submit feedback](https://github.com/prisma/prisma/issues/)

[`partialIndexes`](https://www.prisma.io/docs/orm/prisma-schema/data-model/indexes)

[7.4.0](https://pris.ly/release/7.4.0)

[Submit feedback](https://github.com/prisma/prisma/issues/6974)

To enable a Preview feature, [add the feature flag to the `generator` block](#enabling-a-prisma-client-preview-feature) in your `schema.prisma` file. [Share your feedback on all Preview features on GitHub](https://github.com/prisma/prisma/issues/3108).

To enable a Prisma Client Preview feature:

1.  Add the Preview feature flag to the `generator` block:
    
    ```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
      previewFeatures = ["relationJoins"]
    }
    ```
    
2.  Re-generate Prisma Client:
    
3.  If you are using Visual Studio Code and the Preview feature is not available in your `.ts` file after generating Prisma Client, run the **TypeScript: Restart TS server** command.
    

In the list below, you can find a history of Prisma Client and Prisma schema features that were in Preview and are now in general availability. The features are sorted by the most recent version in which they were promoted to general availability.

Feature

Released into Preview

Released into General Availability

[`driverAdapters`](https://www.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers#driver-adapters)

[5.4.0](https://github.com/prisma/prisma/releases/tag/5.4.0)

[6.16.0](https://github.com/prisma/prisma/releases/tag/6.16.0)

[`multiSchema`](https://www.prisma.io/docs/orm/prisma-schema/data-model/multi-schema)

[4.3.0](https://github.com/prisma/prisma/releases/tag/4.3.0)

[6.13.0](https://github.com/prisma/prisma/releases/tag/6.13.0)

[`prismaSchemaFolder`](https://www.prisma.io/docs/orm/prisma-schema/overview/location#multi-file-prisma-schema)

[5.15.0](https://github.com/prisma/prisma/releases/tag/5.15.0)

[6.7.0](https://pris.ly/release/6.7.0)

`omitApi`

[5.13.0](https://github.com/prisma/prisma/releases/tag/5.13.0)

[6.2.0](https://github.com/prisma/prisma/releases/tag/6.2.0)

`jsonProtocol`

[4.11.0](https://github.com/prisma/prisma/releases/tag/4.11.0)

[5.0.0](https://github.com/prisma/prisma/releases/tag/5.0.0)

[`extendedWhereUnique`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#filter-on-non-unique-fields-with-userwhereuniqueinput)

[4.5.0](https://github.com/prisma/prisma/releases/tag/4.5.0)

[5.0.0](https://github.com/prisma/prisma/releases/tag/5.0.0)

[`fieldReference`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#compare-columns-in-the-same-table)

[4.3.0](https://github.com/prisma/prisma/releases/tag/4.3.0)

[5.0.0](https://github.com/prisma/prisma/releases/tag/5.0.0)

[`clientExtensions`](https://www.prisma.io/docs/orm/prisma-client/client-extensions)

[4.7.0](https://github.com/prisma/prisma/releases/tag/4.7.0)

[4.16.0](https://github.com/prisma/prisma/releases/tag/4.16.0)

[`filteredRelationCount`](https://www.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#filter-the-relation-count)

[4.3.0](https://github.com/prisma/prisma/releases/tag/4.3.0)

[4.16.0](https://github.com/prisma/prisma/releases/tag/4.16.0)

[`tracing`](https://www.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing)

[4.2.0](https://github.com/prisma/prisma/releases/tag/4.2.0)

[6.1.0](https://github.com/prisma/prisma/releases/tag/6.1.0)

[`orderByNulls`](https://www.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting#sort-with-null-records-first-or-last)

[4.1.0](https://github.com/prisma/prisma/releases/tag/4.1.0)

[4.16.0](https://github.com/prisma/prisma/releases/tag/4.16.0)

[`referentialIntegrity`](https://www.prisma.io/docs/orm/prisma-schema/data-model/relations/relation-mode)

[3.1.1](https://github.com/prisma/prisma/releases/tag/3.1.1)

[4.7.0](https://github.com/prisma/prisma/releases/tag/4.7.0)

[`interactiveTransactions`](https://www.prisma.io/docs/orm/prisma-client/queries/transactions#interactive-transactions)

[2.29.0](https://github.com/prisma/prisma/releases/tag/2.29.0)

[4.7.0](https://github.com/prisma/prisma/releases/tag/4.7.0)  
with Prisma Accelerate [5.1.1](https://github.com/prisma/prisma/releases/tag/5.1.1)

[`extendedIndexes`](https://www.prisma.io/docs/orm/prisma-schema/data-model/indexes)

[3.5.0](https://github.com/prisma/prisma/releases/tag/3.5.0)

[4.0.0](https://github.com/prisma/prisma/releases/tag/4.0.0)

[`filterJson`](https://www.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields#filter-on-a-json-field-simple)

[2.23.0](https://github.com/prisma/prisma/releases/tag/2.23.0)

[4.0.0](https://github.com/prisma/prisma/releases/tag/4.0.0)

[`improvedQueryRaw`](https://www.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#raw-query-type-mapping)

[3.14.0](https://github.com/prisma/prisma/releases/tag/3.14.0)

[4.0.0](https://github.com/prisma/prisma/releases/tag/4.0.0)

[`cockroachdb`](https://www.prisma.io/docs/orm/core-concepts/supported-databases/postgresql#cockroachdb)

[3.9.0](https://github.com/prisma/prisma/releases/tag/3.9.0)  
migrations in [3.11.0](https://github.com/prisma/prisma/releases/tag/3.11.0)

[3.14.0](https://github.com/prisma/prisma/releases/tag/3.14.0)

[`mongodb`](https://www.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)

[2.27.0](https://github.com/prisma/prisma/releases/tag/2.27.0)  
introspection in [3.2.0](https://github.com/prisma/prisma/releases/tag/3.2.0)  
embedded docs in [3.4.0](https://github.com/prisma/prisma/releases/tag/3.4.0)  
raw queries in [3.9.0](https://github.com/prisma/prisma/releases/tag/3.9.0)  
filters/ordering in embedded docs in [3.11.0](https://github.com/prisma/prisma/releases/tag/3.11.0)

[3.12.0](https://github.com/prisma/prisma/releases/tag/3.12.0)

[`microsoftSqlServer`](https://www.prisma.io/docs/orm/core-concepts/supported-databases/sql-server)

[2.10.0](https://github.com/prisma/prisma/releases/tag/2.10.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

[`namedConstraints`](https://www.prisma.io/docs/orm/prisma-schema/data-model/database-mapping#constraint-and-index-names)

[2.29.0](https://github.com/prisma/prisma/releases/tag/2.29.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

[`referentialActions`](https://www.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions)

[2.26.0](https://github.com/prisma/prisma/releases/tag/2.26.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

[`orderByAggregateGroup`](https://www.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#order-by-aggregate-group)

[2.21.0](https://github.com/prisma/prisma/releases/tag/2.21.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

[`orderByRelation`](https://www.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting#sort-by-relation)

[2.16.0](https://github.com/prisma/prisma/releases/tag/2.16.0)  
aggregates in [2.19.0](https://github.com/prisma/prisma/releases/tag/2.19.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

[`selectRelationCount`](https://www.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#count-relations)

[2.20.0](https://github.com/prisma/prisma/releases/tag/2.20.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

`napi`

[2.20.0](https://github.com/prisma/prisma/releases/tag/2.20.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

[`groupBy`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#groupby)

[2.14.0](https://github.com/prisma/prisma/releases/tag/2.14.0)

[2.20.0](https://github.com/prisma/prisma/releases/tag/2.20.0)

[`createMany`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#createmany)

[2.16.0](https://github.com/prisma/prisma/releases/tag/2.16.0)

[2.20.0](https://github.com/prisma/prisma/releases/tag/2.20.0)

[`nativeTypes`](https://www.prisma.io/docs/orm/prisma-schema/data-model/models#native-types-mapping)

[2.11.0](https://github.com/prisma/prisma/releases/tag/2.11.0)

[2.17.0](https://github.com/prisma/prisma/releases/tag/2.17.0)

[`uncheckedScalarInputs`](https://www.prisma.io/docs/orm/prisma-client/queries/relation-queries#create-a-single-record-and-multiple-related-records)

[2.11.0](https://github.com/prisma/prisma/releases/tag/2.11.0)

[2.15.0](https://github.com/prisma/prisma/releases/tag/2.15.0)

[`transactionApi`](https://www.prisma.io/docs/orm/prisma-client/queries/transactions#the-transaction-api)

[2.1.0](https://github.com/prisma/prisma/releases/tag/2.1.0)

[2.11.0](https://github.com/prisma/prisma/releases/tag/2.11.0)

[`connectOrCreate`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#connectorcreate)

[2.1.0](https://github.com/prisma/prisma/releases/tag/2.1.0)

[2.11.0](https://github.com/prisma/prisma/releases/tag/2.11.0)

[`atomicNumberOperations`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#atomic-number-operations)

[2.6.0](https://github.com/prisma/prisma/releases/tag/2.6.0)

[2.10.0](https://github.com/prisma/prisma/releases/tag/2.10.0)

[`insensitiveFilters` (PostgreSQL)](https://www.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting#case-insensitive-filtering)

[2.5.0](https://github.com/prisma/prisma/releases/tag/2.5.0)

[2.8.0](https://github.com/prisma/prisma/releases/tag/2.8.0)

[`aggregateApi`](https://www.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#aggregate)

[2.2.0](https://github.com/prisma/prisma/releases/tag/2.2.0)

[2.5.0](https://github.com/prisma/prisma/releases/tag/2.5.0)

[`distinct`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#distinct)

[2.3.0](https://github.com/prisma/prisma/releases/tag/2.3.0)

[2.5.0](https://github.com/prisma/prisma/releases/tag/2.5.0)

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/reference/preview-features/client-preview-features.mdx)
