---
title: "Storage Optimizations"
source: "https://supabase.com/docs/guides/storage/production/scaling"
canonical_url: "https://supabase.com/docs/guides/storage/production/scaling"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:23.831Z"
content_hash: "516908f9ab3d35278f64158f25d9e450904edfcb377a02ee13639760ea6da609"
menu_path: ["Storage","Storage","More","More","More","Going to production","Going to production","Scaling","Scaling"]
section_path: ["Storage","Storage","More","More","More","Going to production","Going to production","Scaling","Scaling"]
nav_prev: {"path": "supabase/docs/guides/storage/pricing/index.md", "title": "Pricing"}
nav_next: {"path": "supabase/docs/guides/storage/quickstart/index.md", "title": "Storage Quickstart"}
---

# 

Storage Optimizations

## 

Scaling Storage

* * *

Here are some optimizations that you can consider to improve performance and reduce costs as you start scaling Storage.

## Egress[#](#egress)

If your project has high egress, these optimizations can help reducing it.

#### Resize images[#](#resize-images)

Images typically make up most of your egress. By keeping them as small as possible, you can cut down on egress and boost your application's performance. You can take advantage of our [Image Transformation](/docs/guides/storage/serving/image-transformations) service to optimize any image on the fly.

#### Set a high cache-control value[#](#set-a-high-cache-control-value)

Using the browser cache can effectively lower your egress since the asset remains stored in the user's browser after the initial download. Setting a high `cache-control` value ensures the asset stays in the user's browser for an extended period, decreasing the need to download it from the server repeatedly. Read more [here](../../cdn/smart-cdn/index.md#cache-duration)

#### Limit the upload size[#](#limit-the-upload-size)

You have the option to set a maximum upload size for your bucket. Doing this can prevent users from uploading and then downloading excessively large files. You can control the maximum file size by configuring this option at the [bucket level](../../buckets/creating-buckets/index.md).

#### Smart CDN[#](#smart-cdn)

By leveraging our [Smart CDN](../../cdn/smart-cdn/index.md), you can achieve a higher cache hit rate and therefore lower your egress cached, as we charge less for cached egress (see [egress pricing](../../../platform/manage-your-usage/egress/index.md#pricing)).

## Optimize listing objects[#](#optimize-listing-objects)

Once you have a substantial number of objects, you might observe that the `supabase.storage.list()` method starts to slow down. This occurs because the endpoint is quite generic and attempts to retrieve both folders and objects in a single query. While this approach is very useful for building features like the Storage viewer on the Supabase dashboard, it can impact performance with a large number of objects.

If your application doesn't need the entire hierarchy computed you can speed up drastically the query execution for listing your objects by creating a Postgres function as following:

```
1create or replace function list_objects(2    bucketid text,3    prefix text,4    limits int default 100,5    offsets int default 06) returns table (7    name text,8    id uuid,9    updated_at timestamptz,10    created_at timestamptz,11    last_accessed_at timestamptz,12    metadata jsonb13) as $$14begin15    return query SELECT16        objects.name,17        objects.id,18        objects.updated_at,19        objects.created_at,20        objects.last_accessed_at,21        objects.metadata22    FROM storage.objects23    WHERE objects.name like prefix || '%'24    AND bucket_id = bucketid25    ORDER BY name ASC26    LIMIT limits27    OFFSET offsets;28end;29$$ language plpgsql stable;
```

You can then use the your Postgres function as following:

Using SQL:

```
1select * from list_objects('bucket_id', '', 100, 0);
```

Using the SDK:

```
1const { data, error } = await supabase.rpc('list_objects', {2  bucketid: 'yourbucket',3  prefix: '',4  limit: 100,5  offset: 0,6})
```

## Optimizing RLS[#](#optimizing-rls)

When creating RLS policies against the storage tables you can add indexes to the interested columns to speed up the lookup
