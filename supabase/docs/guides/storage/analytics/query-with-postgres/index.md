---
title: "Query with Postgres"
source: "https://supabase.com/docs/guides/storage/analytics/query-with-postgres"
canonical_url: "https://supabase.com/docs/guides/storage/analytics/query-with-postgres"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:07.842Z"
content_hash: "8d19c18e1b8d51d0de1d81674e5de2622b1152b52fa1aee0f476a9f563b77f6e"
menu_path: ["Storage","Storage","Analytics Buckets","Analytics Buckets","Query with Postgres","Query with Postgres"]
section_path: ["Storage","Storage","Analytics Buckets","Analytics Buckets","Query with Postgres","Query with Postgres"]
nav_prev: {"path": "supabase/docs/guides/storage/buckets/creating-buckets/index.md", "title": "Creating Buckets"}
nav_next: {"path": "supabase/docs/guides/storage/buckets/fundamentals/index.md", "title": "Storage Buckets"}
---

# 

Query with Postgres

## 

Query analytics bucket data directly from Postgres using SQL.

* * *

Once your data flows into an analytics bucket through your own ingestion pipeline, you can query it directly from Postgres using standard SQL.

This is made possible by the [Iceberg Foreign Data Wrapper](/docs/guides/database/extensions/wrappers/iceberg), which creates a bridge between your Postgres database and Iceberg tables.

##### About ingestion

Managed replication into Analytics Buckets through Supabase ETL is no longer supported. This guide assumes your Analytics Bucket is being populated by your own ingestion pipeline.

## Setup overview[#](#setup-overview)

You have two options to enable querying:

1.  **Dashboard UI** (recommended) - Streamlined setup through the Supabase Dashboard
2.  **Manual installation** - Install the wrapper using SQL and configuration

## Installing via Dashboard UI[#](#installing-via-dashboard-ui)

The dashboard provides the easiest setup experience:

1.  Navigate to your **Analytics Bucket** page in the Supabase Dashboard.
2.  Locate the namespace you want to query and click **Query with Postgres**.

![Query with Postgres button on analytics bucket page](/docs/img/storage/query-analytics-with-postgres.png)

3.  Enter the **Postgres schema** where you want to create the foreign tables.

![Select destination Postgres schema](/docs/img/storage/query-analytics-schema-name.png)

4.  Click **Connect**. The wrapper is now configured.

## Querying your data[#](#querying-your-data)

Once the foreign data wrapper is installed, you can query your Iceberg tables using standard SQL:

```
1select *2from schema_name.table_name3limit 100;
```

### Common query examples[#](#common-query-examples)

Get the latest events:

```
1select event_id, event_name, event_timestamp2from analytics.events3order by event_timestamp desc4limit 1000;
```

Join with transactional data:

```
1SELECT2  e.event_id,3  e.event_name,4  u.user_email5FROM analytics.events e6JOIN public.users u ON e.user_id = u.id7WHERE e.event_timestamp > NOW() - INTERVAL '7 days'8LIMIT 100;
```

## Manual installation[#](#manual-installation)

For advanced use cases, you can manually install and configure the Iceberg Foreign Data Wrapper. See the [Iceberg Foreign Data Wrapper documentation](/docs/guides/database/extensions/wrappers/iceberg) for detailed instructions.
