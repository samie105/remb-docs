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
nav_prev: {"path": "prisma/docs/orm/reference/errors/index.md", "title": "Prisma Error Reference"}
nav_next: {"path": "prisma/docs/orm/reference/preview-features/cli-preview-features/index.md", "title": "Prisma CLI Preview features"}
---

Prisma Client and Prisma schema features that are currently in Preview

When we release a new Prisma Client or Prisma schema feature, it often starts in Preview so that you can test it and submit your feedback. After we improve the feature with your feedback and are satisfied with the internal test results, we promote the feature to general availability.

For more information, see [ORM releases and maturity levels](prisma/docs/orm/more/releases/index.md).

The following [Preview](prisma/docs/orm/more/releases/index.md#preview) feature flags are available for Prisma Client and Prisma schema:

Feature

Released into Preview

Feedback issue

[`views`](prisma/docs/orm/prisma-schema/data-model/views/index.md)

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

[`partialIndexes`](prisma/docs/orm/prisma-schema/data-model/indexes/index.md)

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

[`driverAdapters`](prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md#driver-adapters)

[5.4.0](https://github.com/prisma/prisma/releases/tag/5.4.0)

[6.16.0](https://github.com/prisma/prisma/releases/tag/6.16.0)

[`multiSchema`](prisma/docs/orm/prisma-schema/data-model/multi-schema/index.md)

[4.3.0](https://github.com/prisma/prisma/releases/tag/4.3.0)

[6.13.0](https://github.com/prisma/prisma/releases/tag/6.13.0)

[`prismaSchemaFolder`](prisma/docs/orm/prisma-schema/overview/location/index.md#multi-file-prisma-schema)

[5.15.0](https://github.com/prisma/prisma/releases/tag/5.15.0)

[6.7.0](https://pris.ly/release/6.7.0)

`omitApi`

[5.13.0](https://github.com/prisma/prisma/releases/tag/5.13.0)

[6.2.0](https://github.com/prisma/prisma/releases/tag/6.2.0)

`jsonProtocol`

[4.11.0](https://github.com/prisma/prisma/releases/tag/4.11.0)

[5.0.0](https://github.com/prisma/prisma/releases/tag/5.0.0)

[`extendedWhereUnique`](prisma/docs/orm/reference/prisma-client-reference/index.md#filter-on-non-unique-fields-with-userwhereuniqueinput)

[4.5.0](https://github.com/prisma/prisma/releases/tag/4.5.0)

[5.0.0](https://github.com/prisma/prisma/releases/tag/5.0.0)

[`fieldReference`](prisma/docs/orm/reference/prisma-client-reference/index.md#compare-columns-in-the-same-table)

[4.3.0](https://github.com/prisma/prisma/releases/tag/4.3.0)

[5.0.0](https://github.com/prisma/prisma/releases/tag/5.0.0)

[`clientExtensions`](prisma/docs/orm/prisma-client/client-extensions/index.md)

[4.7.0](https://github.com/prisma/prisma/releases/tag/4.7.0)

[4.16.0](https://github.com/prisma/prisma/releases/tag/4.16.0)

[`filteredRelationCount`](prisma/docs/orm/prisma-client/queries/aggregation-grouping-summarizing/index.md#filter-the-relation-count)

[4.3.0](https://github.com/prisma/prisma/releases/tag/4.3.0)

[4.16.0](https://github.com/prisma/prisma/releases/tag/4.16.0)

[`tracing`](prisma/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing/index.md)

[4.2.0](https://github.com/prisma/prisma/releases/tag/4.2.0)

[6.1.0](https://github.com/prisma/prisma/releases/tag/6.1.0)

[`orderByNulls`](https://www.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting#sort-with-null-records-first-or-last)

[4.1.0](https://github.com/prisma/prisma/releases/tag/4.1.0)

[4.16.0](https://github.com/prisma/prisma/releases/tag/4.16.0)

[`referentialIntegrity`](prisma/docs/orm/prisma-schema/data-model/relations/relation-mode/index.md)

[3.1.1](https://github.com/prisma/prisma/releases/tag/3.1.1)

[4.7.0](https://github.com/prisma/prisma/releases/tag/4.7.0)

[`interactiveTransactions`](prisma/docs/orm/prisma-client/queries/transactions/index.md#interactive-transactions)

[2.29.0](https://github.com/prisma/prisma/releases/tag/2.29.0)

[4.7.0](https://github.com/prisma/prisma/releases/tag/4.7.0)  
with Prisma Accelerate [5.1.1](https://github.com/prisma/prisma/releases/tag/5.1.1)

[`extendedIndexes`](prisma/docs/orm/prisma-schema/data-model/indexes/index.md)

[3.5.0](https://github.com/prisma/prisma/releases/tag/3.5.0)

[4.0.0](https://github.com/prisma/prisma/releases/tag/4.0.0)

[`filterJson`](prisma/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields/index.md#filter-on-a-json-field-simple)

[2.23.0](https://github.com/prisma/prisma/releases/tag/2.23.0)

[4.0.0](https://github.com/prisma/prisma/releases/tag/4.0.0)

[`improvedQueryRaw`](prisma/docs/orm/prisma-client/using-raw-sql/raw-queries/index.md#raw-query-type-mapping)

[3.14.0](https://github.com/prisma/prisma/releases/tag/3.14.0)

[4.0.0](https://github.com/prisma/prisma/releases/tag/4.0.0)

[`cockroachdb`](prisma/docs/orm/core-concepts/supported-databases/postgresql/index.md#cockroachdb)

[3.9.0](https://github.com/prisma/prisma/releases/tag/3.9.0)  
migrations in [3.11.0](https://github.com/prisma/prisma/releases/tag/3.11.0)

[3.14.0](https://github.com/prisma/prisma/releases/tag/3.14.0)

[`mongodb`](prisma/docs/orm/core-concepts/supported-databases/mongodb/index.md)

[2.27.0](https://github.com/prisma/prisma/releases/tag/2.27.0)  
introspection in [3.2.0](https://github.com/prisma/prisma/releases/tag/3.2.0)  
embedded docs in [3.4.0](https://github.com/prisma/prisma/releases/tag/3.4.0)  
raw queries in [3.9.0](https://github.com/prisma/prisma/releases/tag/3.9.0)  
filters/ordering in embedded docs in [3.11.0](https://github.com/prisma/prisma/releases/tag/3.11.0)

[3.12.0](https://github.com/prisma/prisma/releases/tag/3.12.0)

[`microsoftSqlServer`](prisma/docs/orm/core-concepts/supported-databases/sql-server/index.md)

[2.10.0](https://github.com/prisma/prisma/releases/tag/2.10.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

[`namedConstraints`](prisma/docs/orm/prisma-schema/data-model/database-mapping/index.md#constraint-and-index-names)

[2.29.0](https://github.com/prisma/prisma/releases/tag/2.29.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

[`referentialActions`](prisma/docs/orm/prisma-schema/data-model/relations/referential-actions/index.md)

[2.26.0](https://github.com/prisma/prisma/releases/tag/2.26.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

[`orderByAggregateGroup`](prisma/docs/orm/prisma-client/queries/aggregation-grouping-summarizing/index.md#order-by-aggregate-group)

[2.21.0](https://github.com/prisma/prisma/releases/tag/2.21.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

[`orderByRelation`](https://www.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting#sort-by-relation)

[2.16.0](https://github.com/prisma/prisma/releases/tag/2.16.0)  
aggregates in [2.19.0](https://github.com/prisma/prisma/releases/tag/2.19.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

[`selectRelationCount`](prisma/docs/orm/prisma-client/queries/aggregation-grouping-summarizing/index.md#count-relations)

[2.20.0](https://github.com/prisma/prisma/releases/tag/2.20.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

`napi`

[2.20.0](https://github.com/prisma/prisma/releases/tag/2.20.0)

[3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)

[`groupBy`](prisma/docs/orm/reference/prisma-client-reference/index.md#groupby)

[2.14.0](https://github.com/prisma/prisma/releases/tag/2.14.0)

[2.20.0](https://github.com/prisma/prisma/releases/tag/2.20.0)

[`createMany`](prisma/docs/orm/reference/prisma-client-reference/index.md#createmany)

[2.16.0](https://github.com/prisma/prisma/releases/tag/2.16.0)

[2.20.0](https://github.com/prisma/prisma/releases/tag/2.20.0)

[`nativeTypes`](prisma/docs/orm/prisma-schema/data-model/models/index.md#native-types-mapping)

[2.11.0](https://github.com/prisma/prisma/releases/tag/2.11.0)

[2.17.0](https://github.com/prisma/prisma/releases/tag/2.17.0)

[`uncheckedScalarInputs`](prisma/docs/orm/prisma-client/queries/relation-queries/index.md#create-a-single-record-and-multiple-related-records)

[2.11.0](https://github.com/prisma/prisma/releases/tag/2.11.0)

[2.15.0](https://github.com/prisma/prisma/releases/tag/2.15.0)

[`transactionApi`](prisma/docs/orm/prisma-client/queries/transactions/index.md#the-transaction-api)

[2.1.0](https://github.com/prisma/prisma/releases/tag/2.1.0)

[2.11.0](https://github.com/prisma/prisma/releases/tag/2.11.0)

[`connectOrCreate`](prisma/docs/orm/reference/prisma-client-reference/index.md#connectorcreate)

[2.1.0](https://github.com/prisma/prisma/releases/tag/2.1.0)

[2.11.0](https://github.com/prisma/prisma/releases/tag/2.11.0)

[`atomicNumberOperations`](prisma/docs/orm/reference/prisma-client-reference/index.md#atomic-number-operations)

[2.6.0](https://github.com/prisma/prisma/releases/tag/2.6.0)

[2.10.0](https://github.com/prisma/prisma/releases/tag/2.10.0)

[`insensitiveFilters` (PostgreSQL)](https://www.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting#case-insensitive-filtering)

[2.5.0](https://github.com/prisma/prisma/releases/tag/2.5.0)

[2.8.0](https://github.com/prisma/prisma/releases/tag/2.8.0)

[`aggregateApi`](prisma/docs/orm/prisma-client/queries/aggregation-grouping-summarizing/index.md#aggregate)

[2.2.0](https://github.com/prisma/prisma/releases/tag/2.2.0)

[2.5.0](https://github.com/prisma/prisma/releases/tag/2.5.0)

[`distinct`](prisma/docs/orm/reference/prisma-client-reference/index.md#distinct)

[2.3.0](https://github.com/prisma/prisma/releases/tag/2.3.0)

[2.5.0](https://github.com/prisma/prisma/releases/tag/2.5.0)

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/reference/preview-features/client-preview-features.mdx)

