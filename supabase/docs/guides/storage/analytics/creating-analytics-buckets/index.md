---
title: "Creating Analytics Buckets"
source: "https://supabase.com/docs/guides/storage/analytics/creating-analytics-buckets"
canonical_url: "https://supabase.com/docs/guides/storage/analytics/creating-analytics-buckets"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:59.769Z"
content_hash: "60a110ecea480c39dc83b05bb124da86a8799fa2b36f054c27072f18e80ce877"
menu_path: ["Storage","Storage","Analytics Buckets","Analytics Buckets","Creating Buckets","Creating Buckets"]
section_path: ["Storage","Storage","Analytics Buckets","Analytics Buckets","Creating Buckets","Creating Buckets"]
nav_prev: {"path": "supabase/docs/guides/storage/analytics/connecting-to-analytics-bucket/index.md", "title": "Iceberg Catalog"}
nav_next: {"path": "supabase/docs/guides/storage/analytics/introduction/index.md", "title": "Analytics Buckets"}
---

# 

Creating Analytics Buckets

## 

Set up your first analytics bucket using the SDK or dashboard.

* * *

This feature is in **Private Alpha**. API stability and backward compatibility are not guaranteed at this stage. Request access through this [form](https://forms.supabase.com/analytics-buckets).

Analytics buckets use [Apache Iceberg](https://iceberg.apache.org/), an open-table format for efficient management of large analytical datasets. You can interact with analytics buckets using tools such as [PyIceberg](https://py.iceberg.apache.org/), [Apache Spark](https://spark.apache.org/), or any client supporting the [Iceberg REST Catalog API](https://editor-next.swagger.io/?url=https://raw.githubusercontent.com/apache/iceberg/main/open-api/rest-catalog-open-api.yaml).

##### About replication

Analytics Buckets are still available, but managed replication into Analytics Buckets through Supabase ETL is no longer supported. If you need managed replication today, use [Database Replication](/docs/guides/database/replication/replication-setup) with **BigQuery**. If you want to use Analytics Buckets, bring your own ingestion pipeline.

## Creating an Analytics bucket[#](#creating-an-analytics-bucket)

You can create an analytics bucket using either the Supabase SDK or the Supabase Dashboard.

### Using the Supabase SDK[#](#using-the-supabase-sdk)

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'your-service-key')45const { data, error } = await supabase.storage.analytics.createBucket('analytics-data')67if (error) {8  console.error('Failed to create analytics bucket:', error)9} else {10  console.log('Analytics bucket created:', data)11}
```

### Using the Supabase Dashboard[#](#using-the-supabase-dashboard)

1.  Navigate to the **Storage** section in the Supabase Dashboard.
2.  Click **Create Bucket**.
3.  Enter a name for your bucket (e.g., `my-analytics-bucket`).
4.  Select **Analytics Bucket** as the bucket type.
5.  Click **Create**.

![Create Analytics Bucket in Dashboard](/docs/img/storage/iceberg-bucket.png)

## Next steps[#](#next-steps)

Once you've created your analytics bucket, you can:

*   [Connect with Iceberg clients](/docs/guides/storage/analytics/connecting-to-analytics-bucket) like PyIceberg or Apache Spark
*   [Query data with Postgres](/docs/guides/storage/analytics/query-with-postgres) using the Iceberg Foreign Data Wrapper


