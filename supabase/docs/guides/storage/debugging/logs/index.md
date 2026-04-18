---
title: "Logs"
source: "https://supabase.com/docs/guides/storage/debugging/logs"
canonical_url: "https://supabase.com/docs/guides/storage/debugging/logs"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:16.458Z"
content_hash: "4be0166db4576e327f87b6d4981da7f7c7bc47728d50f3f2761c9248cf7542a3"
menu_path: ["Storage","Storage","More","More","More","Debugging","Debugging","Logs","Logs"]
section_path: ["Storage","Storage","More","More","More","Debugging","Debugging","Logs","Logs"]
nav_prev: {"path": "supabase/docs/guides/storage/cdn/smart-cdn/index.md", "title": "Smart CDN"}
nav_next: {"path": "supabase/docs/guides/storage/debugging/error-codes/index.md", "title": "Error Codes"}
---

# 

Logs

* * *

The [Storage Logs](/dashboard/project/_/logs/storage-logs) provide a convenient way to examine all incoming request logs to your Storage service. You can filter by time and keyword searches.

For more advanced filtering needs, use the [Logs Explorer](/dashboard/project/_/logs/explorer) to query the Storage logs dataset directly. The Logs Explorer is separate from the SQL Editor and uses a subset of the BigQuery SQL syntax rather than traditional SQL.

For more details on filtering the log tables, see [Advanced Log Filtering](/docs/guides/telemetry/advanced-log-filtering)

### Example Storage queries for the Logs Explorer[#](#example-storage-queries-for-the-logs-explorer)

#### Filter by status 5XX error[#](#filter-by-status-5xx-error)

```
1select2  id,3  storage_logs.timestamp,4  event_message,5  r.statusCode,6  e.message as errorMessage,7  e.raw as rawError8from9  storage_logs10  cross join unnest(metadata) as m11  cross join unnest(m.res) as r12  cross join unnest(m.error) as e13where r.statusCode >= 50014order by timestamp desc15limit 100;
```

#### Filter by status 4XX error[#](#filter-by-status-4xx-error)

```
1select2  id,3  storage_logs.timestamp,4  event_message,5  r.statusCode,6  e.message as errorMessage,7  e.raw as rawError8from9  storage_logs10  cross join unnest(metadata) as m11  cross join unnest(m.res) as r12  cross join unnest(m.error) as e13where r.statusCode >= 400 and r.statusCode < 50014order by timestamp desc15limit 100;
```

#### Filter by method[#](#filter-by-method)

```
1select id, storage_logs.timestamp, event_message, r.method2from3  storage_logs4  cross join unnest(metadata) as m5  cross join unnest(m.req) as r6where r.method in ("POST")7order by timestamp desc8limit 100;
```

#### Filter by IP address[#](#filter-by-ip-address)

```
1select id, storage_logs.timestamp, event_message, r.remoteAddress2from3  storage_logs4  cross join unnest(metadata) as m5  cross join unnest(m.req) as r6where r.remoteAddress in ("IP_ADDRESS")7order by timestamp desc8limit 100;
```
