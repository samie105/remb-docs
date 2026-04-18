---
title: "When to use RDI"
source: "https://redis.io/docs/latest/integrate/redis-data-integration/when-to-use/"
canonical_url: "https://redis.io/docs/latest/integrate/redis-data-integration/when-to-use/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:06:54.602Z"
content_hash: "99b8e7aa9e69a8189611d7260d6692b56a60ad3c8ba84fd21c1b9fce23f4ff05"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        When to use RDI","→","When to use RDI"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        When to use RDI","→","When to use RDI"]
---
# When to use RDI

Understand when (and when not) to use RDI.

RDI is designed to support apps that must use a disk-based database as the system of record but must also be fast and scalable. This is a common requirement for mobile and web apps with a rapidly-growing number of users; the performance of the main database is fine at first but it will soon struggle to handle the increasing demand without a cache.

## Guidelines for using RDI

Use the information in the sections below to determine whether RDI is a good fit for your architecture.

### When to use RDI

RDI is a good fit when:

*   You want your app/micro-services to read from Redis to scale reads at speed.
*   You want to transfer data to Redis from a _single_ source database.
*   You must use a slow database as the system of record for the app.
*   The app must always _write_ its data to the slow database.
*   Your app can tolerate _eventual_ consistency of data in the Redis cache.
*   You want a self-managed solution or AWS based solution.
*   The source data changes frequently in small increments.
*   There are no more than 10K changes per second in the source database.
*   RDI throughput during [full sync](/docs/latest/integrate/redis-data-integration/data-pipelines/#pipeline-lifecycle) would not exceed 30K records per second (for an average 1KB record size) and during [CDC](/docs/latest/integrate/redis-data-integration/data-pipelines/#pipeline-lifecycle) would not exceed 10K records per second (for an average 1KB record size).
*   The total data size is not larger than 100GB (since this would typically exceed the throughput limits just mentioned for full sync).
*   You don’t need to perform join operations on the data from several tables into a [nested Redis JSON object](/docs/latest/integrate/redis-data-integration/data-pipelines/data-denormalization/#joining-one-to-many-relationships).
*   RDI supports the [data transformations](/docs/latest/integrate/redis-data-integration/data-pipelines/transform-examples/) you need for your app.
*   Your data caching needs are too complex or demanding to implement and maintain yourself.
*   Your database administrator has reviewed RDI's requirements for the source database and confirmed that they are acceptable.

### When not to use RDI

RDI is not a good fit when:

*   You are migrating an existing data set into Redis only once.
*   Your app needs _immediate_ cache consistency (or a hard limit on latency) rather than _eventual_ consistency.
*   You need _transactional_ consistency between the source and target databases.
*   The data is ingested from two replicas of Active-Active at the same time.
*   The app must _write_ data to the Redis cache, which then updates the source database (write-behind/write-through patterns).
*   Your data set will only ever be small.
*   Your data is updated by some batch or ETL process with long and large transactions - RDI will fail processing these changes.
*   You need complex stream processing of data (aggregations, sliding window processing, complex custom logic).
*   You need to write data to multiple targets from the same pipeline (Redis supports other ways to replicate data across Redis databases such as replicaOf and Active Active).
*   Your database administrator has rejected RDI's requirements for the source database.

### Decision tree for using RDI

Use the decision tree below to determine whether RDI is a good fit for your architecture:

id: when-to-use-rdi
scope: rdi
indentWidth: 25
rootQuestion: cacheTarget
questions:
    cacheTarget:
        text: |
            Do you want to use Redis as the target database?
        whyAsk: |
            RDI is specifically designed to keep Redis in sync with a primary database. If you don't need Redis as a cache, RDI is not the right tool.
        answers:
            no:
                value: "No"
                outcome:
                    label: "❌ RDI only works with Redis as the target database"
                    id: noRedisCache
                    sentiment: "negative"
            yes:
                value: "Yes"
                nextQuestion: deployment
    deployment:
        text: |
            Do you want a self-managed solution or an AWS-based solution?
        whyAsk: |
            RDI is available as a self-managed solution or as an AWS-based managed service. If you need a different deployment model, RDI may not be suitable.
        answers:
            no:
                value: "No"
                outcome:
                    label: "⚠️ Check deployment options to see if RDI is suitable for your needs before proceeding"
                    id: deploymentMismatch
                    sentiment: "indeterminate"
            yes:
                value: "Yes"
                nextQuestion: singleSource
    singleSource:
        text: |
            Are you transferring data from a single source database?
        whyAsk: |
            RDI is designed to work with a single source database. Multiple sources or Active-Active replicas create conflicting change events.
        answers:
            no:
                value: "No"
                outcome:
                    label: "❌ RDI won't work with multiple source databases"
                    id: multipleSourcesOrActiveActive
                    sentiment: "negative"
            yes:
                value: "Yes"
                nextQuestion: consistency
    consistency:
        text: |
            Can your app tolerate eventual consistency in the Redis cache?
        whyAsk: |
            RDI provides eventual consistency, not immediate consistency. If your app needs real-time cache consistency or hard latency limits, RDI is not suitable.
        answers:
            no:
                value: "No"
                outcome:
                    label: "⚠️ Check that RDI's performance meets your latency requirements before proceeding (RDI can't guarantee \*immediate\* consistency)"
                    id: needsImmediate
                    sentiment: "indeterminate"
            yes:
                value: "Yes"
                nextQuestion: systemOfRecord
    systemOfRecord:
        text: |
            Does your app always \*write\* to the source database and not to Redis?
        whyAsk: |
            RDI requires the source database to be the authoritative source of truth. If your app writes to Redis first, RDI won't work.
        answers:
            no:
                value: "No"
                outcome:
                    label: "❌ RDI doesn't support syncing data from Redis back to the source database"
                    id: notSystemOfRecord
                    sentiment: "negative"
            yes:
                value: "Yes"
                nextQuestion: dataChangePattern
    dataChangePattern:
        text: |
            Does your source data change frequently in small increments?
        whyAsk: |
            RDI captures changes from the database transaction log. Large batch transactions or ETL processes can cause RDI to fail.
        answers:
            no:
                value: "No"
                outcome:
                    label: "⚠️ Check that RDI can handle your data change pattern before proceeding (RDI will fail with batch/ETL processes and transactions beyond a certain size)"
                    id: batchProcessing
                    sentiment: "indeterminate"
            yes:
                value: "Yes"
                nextQuestion: changeRate
    changeRate:
        text: |
            Are there fewer than 10K changes per second in the source database?
        whyAsk: |
            RDI has throughput limits. Exceeding these limits will cause processing failures and data loss.
        answers:
            no:
                value: "No"
                outcome:
                    label: "⚠️ RDI is fast but there are practical limits on throughput - check that RDI can handle your change rate before proceeding"
                    id: exceedsChangeRate
                    sentiment: "indeterminate"
            yes:
                value: "Yes"
                nextQuestion: dataSize
    dataSize:
        text: |
            Is your total data size smaller than 100GB?
        whyAsk: |
            RDI has practical limits on the total data size it can manage, based
            on the throughput requirements for full sync.
        answers:
            no:
                value: "No"
                outcome:
                    label: "⚠️ RDI might be unacceptably slow during the full-sync phase. Check that performance will be acceptable for your needs"
                    id: dataTooLarge
                    sentiment: "indeterminate"
            yes:
                value: "Yes"
                nextQuestion: joins
    joins:
        text: |
            Do you need to perform join operations on data from several tables into a nested Redis JSON object?
        whyAsk: |
            RDI has limitations with complex join operations. If you need to combine data from multiple tables into nested structures, you may need custom transformations.
        answers:
            yes:
                value: "Yes"
                outcome:
                    label: "⚠️ RDI may not be suitable - complex joins are not well supported, so check that RDI's data transformations will meet your needs"
                    id: complexJoins
                    sentiment: "indeterminate"
            no:
                value: "No"
                nextQuestion: transformations
    transformations:
        text: |
            Does RDI support the data transformations you need for your app?
        whyAsk: |
            RDI provides built-in transformations, but if you need custom logic beyond what RDI supports, you may need a different approach.
        answers:
            no:
                value: "No"
                outcome:
                    label: "⚠️ RDI supports a wide range of data transformations, but doesn't support free-form code execution. Check that RDI's data transformations will meet your needs"
                    id: unsupportedTransformations
                    sentiment: "indeterminate"
            yes:
                value: "Yes"
                nextQuestion: adminReview
    adminReview:
        text: |
            Has your database administrator reviewed RDI's requirements for the source database
            and confirmed they are acceptable?
        whyAsk: |
            RDI has specific requirements for the source database (binary logging, permissions, etc.). Your DBA must confirm these are acceptable before proceeding.
        answers:
            no:
                value: "No"
                outcome:
                    label: "⚠️ RDI has requirements that might conflict with practical considerations for your database (such as security policies). Check with your DBA before proceeding"
                    id: adminReviewNeeded
                    sentiment: "indeterminate"
            yes:
                value: "Yes"
                outcome:
                    label: "✅ RDI is a good fit for your use case"
                    id: goodFit
                    sentiment: "positive"

## On this page
