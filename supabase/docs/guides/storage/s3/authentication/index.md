---
title: "S3 Authentication"
source: "https://supabase.com/docs/guides/storage/s3/authentication"
canonical_url: "https://supabase.com/docs/guides/storage/s3/authentication"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:24.745Z"
content_hash: "e92c8c94fbe67e09ae6ccf8016d85e6b9c0cdf436ab854e41554b48aa299b42c"
menu_path: ["Storage","Storage","More","More","More","S3","S3","Authentication","Authentication"]
section_path: ["Storage","Storage","More","More","More","S3","S3","Authentication","Authentication"]
nav_prev: {"path": "supabase/docs/guides/storage/quickstart/index.md", "title": "Storage Quickstart"}
nav_next: {"path": "supabase/docs/guides/storage/s3/compatibility/index.md", "title": "S3 Compatibility"}
---

# 

S3 Authentication

## 

Learn about authenticating with Supabase Storage S3.

* * *

You have two options to authenticate with Supabase Storage S3:

*   Using the generated S3 access keys from your [project settings](/dashboard/project/_/storage/settings) (Intended exclusively for server-side use)
*   Using a Session Token, which will allow you to authenticate with a user JWT token and provide limited access via Row Level Security (RLS).

## S3 access keys[#](#s3-access-keys)

##### Keep these credentials secure

S3 access keys provide full access to all S3 operations across all buckets and bypass RLS policies. These are meant to be used only on the server.

To authenticate with S3, generate a pair of credentials (Access Key ID and Secret Access Key), copy the endpoint and region from the [project settings page](/dashboard/project/_/storage/settings).

This is all the information you need to connect to Supabase Storage using any S3-compatible service.

![Storage S3 Access keys](/docs/img/storage/s3-credentials.png)

For optimal performance when uploading large files you should always use the direct storage hostname. This provides several performance enhancements that will greatly improve performance when uploading large files.

Instead of `https://project-id.supabase.co` use `https://project-id.storage.supabase.co`

```
1import { S3Client } from '@aws-sdk/client-s3';23const client = new S3Client({4  forcePathStyle: true,5  region: 'project_region',6  endpoint: 'https://project_ref.storage.supabase.co/storage/v1/s3',7  credentials: {8    accessKeyId: 'your_access_key_id',9    secretAccessKey: 'your_secret_access_key',10  }11})
```

## Session token[#](#session-token)

You can authenticate to Supabase S3 with a user JWT token to provide limited access via RLS to all S3 operations. This is useful when you want initialize the S3 client on the server scoped to a specific user, or use the S3 client directly from the client side.

All S3 operations performed with the Session Token are scoped to the authenticated user. RLS policies on the Storage Schema are respected.

To authenticate with S3 using a Session Token, use the following credentials:

*   access\_key\_id: `project_ref`
*   secret\_access\_key: `anonKey`
*   session\_token: `valid jwt token`

For example, using the `aws-sdk` library:

Typically we advise against using `getSession`, because the session is read from local storage and you can't trust its claims for auth decisions. In this case however, the code only needs the raw access token string to forward as a credential to the S3 service, which validates the token server-side. Since no client-side auth decision is made based on the session data, `getSession` is appropriate here.

```
1import { S3Client } from '@aws-sdk/client-s3'23const {4  data: { session },5} = await supabase.auth.getSession()67const client = new S3Client({8  forcePathStyle: true,9  region: 'project_region',10  endpoint: 'https://project_ref.storage.supabase.co/storage/v1/s3',11  credentials: {12    accessKeyId: 'project_ref',13    secretAccessKey: 'anonKey',14    sessionToken: session.access_token,15  },16})
```

On self-hosted Supabase, the `accessKeyId` is the `STORAGE_TENANT_ID` environment variable defined in the `.env` file. Refer to the [self-hosted S3 guide](../../../self-hosting/self-hosted-s3/index.md#session-token) for more details.
