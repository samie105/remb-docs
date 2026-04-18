---
title: "Storage Buckets"
source: "https://supabase.com/docs/guides/storage/buckets/fundamentals"
canonical_url: "https://supabase.com/docs/guides/storage/buckets/fundamentals"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:08.919Z"
content_hash: "f15c4a3b8c2470c3343ef8a50502ad444c8e47d91833f37e8dfa493b57ab60a6"
menu_path: ["Storage","Storage","File Buckets","File Buckets","Fundamentals","Fundamentals"]
section_path: ["Storage","Storage","File Buckets","File Buckets","Fundamentals","Fundamentals"]
nav_prev: {"path": "supabase/docs/guides/storage/analytics/query-with-postgres/index.md", "title": "Query with Postgres"}
nav_next: {"path": "supabase/docs/guides/storage/cdn/metrics/index.md", "title": "Cache Metrics"}
---

# 

Storage Buckets

* * *

Buckets allow you to keep your files organized and determines the [Access Model](#access-model) for your assets. [Upload restrictions](/docs/guides/storage/buckets/creating-buckets#restricting-uploads) like max file size and allowed content types are also defined at the bucket level.

## Access model[#](#access-model)

There are 2 access models for buckets, **public** and **private** buckets.

### Private buckets[#](#private-buckets)

When a bucket is set to **Private** all operations are subject to access control via [RLS policies](/docs/guides/storage/security/access-control). This also applies when downloading assets. Buckets are private by default.

The only ways to download assets within a private bucket is to:

*   Use the [download method](/docs/reference/javascript/storage-from-download) by providing an authorization header containing your user's JWT. The RLS policy you create on the `storage.objects` table will use this user to determine if they have access.
*   Create a signed URL with the [`createSignedUrl` method](/docs/reference/javascript/storage-from-createsignedurl) that can be accessed for a limited time.

#### Example use cases:[#](#example-use-cases)

*   Uploading users' sensitive documents
*   Securing private assets by using RLS to set up fine-grain access controls

### Public buckets[#](#public-buckets)

When a bucket is designated as 'Public,' it effectively bypasses access controls for both retrieving and serving files within the bucket. This means that anyone who possesses the asset URL can readily access the file.

Access control is still enforced for other types of operations including uploading, deleting, moving, and copying.

#### Example use cases:[#](#example-use-cases)

*   User profile pictures
*   User public media
*   Blog post content

Public buckets are more performant than private buckets since they are [cached differently](/docs/guides/storage/cdn/fundamentals#public-vs-private-buckets).


