---
title: "Cache Metrics"
source: "https://supabase.com/docs/guides/storage/cdn/metrics"
canonical_url: "https://supabase.com/docs/guides/storage/cdn/metrics"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:11.989Z"
content_hash: "e238bb6a77a11ebeeec05dadf88a57eb075334931e213f0bc0c5672eca077e30"
menu_path: ["Storage","Storage","More","More","More","CDN","CDN","Metrics","Metrics"]
section_path: ["Storage","Storage","More","More","More","CDN","CDN","Metrics","Metrics"]
nav_prev: {"path": "supabase/docs/guides/storage/buckets/fundamentals/index.md", "title": "Storage Buckets"}
nav_next: {"path": "supabase/docs/guides/storage/cdn/fundamentals/index.md", "title": "Storage CDN"}
---

# 

Cache Metrics

* * *

Cache hits can be determined via the `metadata.response.headers.cf_cache_status` key in our [Logs Explorer](/docs/guides/platform/logs#logs-explorer). Any value that corresponds to either `HIT`, `STALE`, `REVALIDATED`, or `UPDATING` is categorized as a cache hit. The following example query will show the top cache misses from the `edge_logs`:

```
1select2  r.path as path,3  r.search as search,4  count(id) as count5from6  edge_logs as f7  cross join unnest(f.metadata) as m8  cross join unnest(m.request) as r9  cross join unnest(m.response) as res10  cross join unnest(res.headers) as h11where12  starts_with(r.path, '/storage/v1/object')13  and r.method = 'GET'14  and h.cf_cache_status in ('MISS', 'NONE/UNKNOWN', 'EXPIRED', 'BYPASS', 'DYNAMIC')15group by path, search16order by count desc17limit 50;
```

Try out [this query](/dashboard/project/_/logs/explorer?q=%0Aselect%0A++r.path+as+path%2C%0A++r.search+as+search%2C%0A++count%28id%29+as+count%0Afrom%0A++edge_logs+as+f%0A++cross+join+unnest%28f.metadata%29+as+m%0A++cross+join+unnest%28m.request%29+as+r%0A++cross+join+unnest%28m.response%29+as+res%0A++cross+join+unnest%28res.headers%29+as+h%0Awhere%0A++starts_with%28r.path%2C+%27%2Fstorage%2Fv1%2Fobject%27%29%0A++and+r.method+%3D+%27GET%27%0A++and+h.cf_cache_status+in+%28%27MISS%27%2C+%27NONE%2FUNKNOWN%27%2C+%27EXPIRED%27%2C+%27BYPASS%27%2C+%27DYNAMIC%27%29%0Agroup+by+path%2C+search%0Aorder+by+count+desc%0Alimit+50%3B) in the Logs Explorer.

Your cache hit ratio over time can then be determined using the following query:

```
1select2  timestamp_trunc(timestamp, hour) as timestamp,3  countif(h.cf_cache_status in ('HIT', 'STALE', 'REVALIDATED', 'UPDATING')) / count(f.id) as ratio4from5  edge_logs as f6  cross join unnest(f.metadata) as m7  cross join unnest(m.request) as r8  cross join unnest(m.response) as res9  cross join unnest(res.headers) as h10where starts_with(r.path, '/storage/v1/object') and r.method = 'GET'11group by timestamp12order by timestamp desc;
```

Try out [this query](/dashboard/project/_/logs/explorer?q=%0Aselect%0A++timestamp_trunc%28timestamp%2C+hour%29+as+timestamp%2C%0A++countif%28h.cf_cache_status+in+%28%27HIT%27%2C+%27STALE%27%2C+%27REVALIDATED%27%2C+%27UPDATING%27%29%29+%2F+count%28f.id%29+as+ratio%0Afrom%0A++edge_logs+as+f%0A++cross+join+unnest%28f.metadata%29+as+m%0A++cross+join+unnest%28m.request%29+as+r%0A++cross+join+unnest%28m.response%29+as+res%0A++cross+join+unnest%28res.headers%29+as+h%0Awhere+starts_with%28r.path%2C+%27%2Fstorage%2Fv1%2Fobject%27%29+and+r.method+%3D+%27GET%27%0Agroup+by+timestamp%0Aorder+by+timestamp+desc%3B) in the Logs Explorer.


