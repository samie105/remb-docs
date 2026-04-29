---
title: "Configure S3 Storage"
source: "https://supabase.com/docs/guides/self-hosting/self-hosted-s3"
canonical_url: "https://supabase.com/docs/guides/self-hosting/self-hosted-s3"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:53.171Z"
content_hash: "b94fdf83ff350dd1eb821ab623d4aa314ed41c9efbe3e476dd866a0a004f6b43"
menu_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Configure S3 Storage","Configure S3 Storage"]
section_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Configure S3 Storage","Configure S3 Storage"]
nav_prev: {"path": "../self-hosted-proxy-https/index.md", "title": "Configure Reverse Proxy and HTTPS"}
nav_next: {"path": "../self-hosted-saml-sso/index.md", "title": "Configure SAML SSO"}
---

# 

Configure S3 Storage

## 

Enable S3-compatible client endpoint and set up an S3 backend for self-hosted Supabase Storage.

* * *

Self-hosted Supabase Storage has two independent S3-related features:

*   **S3 protocol endpoint** - an S3-compatible API that Storage exposes at `/storage/v1/s3`. This allows standard S3 tools like `rclone` and the AWS CLI to interact with your Storage instance.
*   **S3 backend** - where Storage keeps data. By default, files are stored on the local filesystem. You can switch to an S3-compatible service (AWS S3, MinIO, etc.) for durability, scalability, or to use existing infrastructure.

You can configure either feature independently. For example, you can enable the S3 protocol endpoint to use `rclone` while keeping the default file-based storage, or switch to an S3 backend without enabling the S3 protocol endpoint.

## Enable the S3 protocol endpoint[#](#enable-the-s3-protocol-endpoint)

The S3 protocol endpoint at `/storage/v1/s3` allows standard S3 clients to interact with your self-hosted Storage instance. It works with any storage backend, including the default file-based storage - you do not need to configure an S3 backend first. The Supabase REST API and SDK do not use the S3 protocol.

Make sure to check that `REGION`, `S3_PROTOCOL_ACCESS_KEY_ID` and `S3_PROTOCOL_ACCESS_KEY_SECRET` are properly configured in you `.env` file. Read more about the secrets and passwords in [Configuring and securing Supabase](/docs/guides/self-hosting/docker#configuring-and-securing-supabase).

```
1storage:2  environment:3    # ... existing variables ...4    REGION: ${REGION}5    S3_PROTOCOL_ACCESS_KEY_ID: ${S3_PROTOCOL_ACCESS_KEY_ID}6    S3_PROTOCOL_ACCESS_KEY_SECRET: ${S3_PROTOCOL_ACCESS_KEY_SECRET}
```

### Test with the AWS CLI[#](#test-with-the-aws-cli)

```
1( set -a && \2source .env > /dev/null 2>&1 && \3echo "" && \4AWS_ACCESS_KEY_ID=$S3_PROTOCOL_ACCESS_KEY_ID \5AWS_SECRET_ACCESS_KEY=$S3_PROTOCOL_ACCESS_KEY_SECRET \6aws s3 ls \7--endpoint-url http://localhost:8000/storage/v1/s3 \8--region $REGION \9s3://your-storage-bucket )
```

### Test with rclone[#](#test-with-rclone)

```
1( set -a && \2source .env > /dev/null 2>&1 && \3echo "" && \4rclone ls \5--s3-endpoint http://localhost:8000/storage/v1/s3 \6--s3-region $REGION \7--s3-provider Other \8--s3-access-key-id "$S3_PROTOCOL_ACCESS_KEY_ID" \9--s3-secret-access-key "$S3_PROTOCOL_ACCESS_KEY_SECRET" \10:s3:your-storage-bucket )
```

Use `aws login` and `rclone config` for persistent configuration.

## How to configure an S3 backend[#](#how-to-configure-an-s3-backend)

In general, the following configuration variables define S3 backend configuration for Storage in `docker-compose.yml`:

```
1storage:2  environment:3    # ... existing variables ...4    STORAGE_BACKEND: s35    GLOBAL_S3_BUCKET: your-s3-bucket-or-dirname6    GLOBAL_S3_ENDPOINT: https://your-s3-endpoint7    GLOBAL_S3_PROTOCOL: https8    GLOBAL_S3_FORCE_PATH_STYLE: 'true'9    AWS_ACCESS_KEY_ID: your-access-key-id10    AWS_SECRET_ACCESS_KEY: your-secret-access-key11    REGION: your-region
```

Depending on your setup, you may need to adjust these values - for example, to use a local S3-compatible service like MinIO or a cloud provider like AWS.

### Using MinIO[#](#using-minio)

An overlay `docker-compose.s3.yml` configuration can be added to enable MinIO container and provide an S3-compatible API for Storage backend:

```
1docker compose -f docker-compose.yml -f docker-compose.s3.yml up -d
```

Make sure to review the Storage section in your `.env` file for related configuration options.

### Using AWS S3[#](#using-aws-s3)

Create an S3 bucket and an IAM user with access to it. Then configure the storage service:

```
1storage:2  environment:3    # ... existing variables ...4    STORAGE_BACKEND: s35    GLOBAL_S3_BUCKET: your-aws-bucket-name6    AWS_ACCESS_KEY_ID: your-aws-access-key7    AWS_SECRET_ACCESS_KEY: your-aws-secret-key8    REGION: your-aws-region
```

For AWS S3, you do not need `GLOBAL_S3_ENDPOINT` or `GLOBAL_S3_FORCE_PATH_STYLE` - the Storage S3 client automatically resolves the endpoint from the region and uses virtual-hosted-style URLs, which is what AWS S3 expects. These variables are only needed for non-AWS S3-compatible providers.

### S3-compatible providers[#](#s3-compatible-providers)

Use the same configuration as MinIO, but point to your provider's endpoint, e.g.:

```
1storage:2  environment:3    # ... existing variables ...4    STORAGE_BACKEND: s35    GLOBAL_S3_BUCKET: your-bucket-name6    GLOBAL_S3_ENDPOINT: https://your-account-id.r2.cloudflarestorage.com
```

## Verify[#](#verify)

*   Open Studio and upload a file to a bucket. List the file using the AWS CLI or `rclone` to confirm the S3 endpoint works.
*   If using an S3 backend: confirm the file appears in your S3 provider's console.

## Session token[#](#session-token)

You can authenticate to Supabase's S3-compatible storage using a user’s JWT to enforce Row-Level Security (RLS) across S3 operations. This is useful when initializing the S3 client on the server for a specific user session, or when using the client directly from the frontend.

All operations performed with a session token are scoped to the authenticated user, and any RLS policies defined in the storage schema will be applied.

To authenticate with S3 using a session token, provide the following credentials:

*   **region:** value from the `REGION` environment variable in your `.env` file
*   **access\_key\_id:** value from the `STORAGE_TENANT_ID` environment variable in your `.env` file
*   **secret\_access\_key:** value from the `ANON_KEY` environment variable
*   **session\_token:** a valid user JWT

Example using the `aws-sdk` library:

```
1import { S3Client } from '@aws-sdk/client-s3'23const {4  data: { session },5} = await supabase.auth.getSession()67const client = new S3Client({8  forcePathStyle: true,9  region: 'stub', // REGION in .env10  endpoint: 'http://<your-domain>/storage/v1/s3', // Edit <your-domain>11  credentials: {12    accessKeyId: 'stub', // STORAGE_TENANT_ID in .env13    secretAccessKey: 'your-anon-key', // ANON_KEY in .env14    sessionToken: session.access_token,15  },16})
```

## Troubleshooting[#](#troubleshooting)

### Signature mismatch errors[#](#signature-mismatch-errors)

S3 clients sign requests using the access key ID and secret. If you see `SignatureDoesNotMatch`, verify that the `REGION`, `S3_PROTOCOL_ACCESS_KEY_ID` and `S3_PROTOCOL_ACCESS_KEY_SECRET` in your `.env` file match what your S3 client is using.

### TUS upload errors on Cloudflare R2[#](#tus-upload-errors-on-cloudflare-r2)

If resumable (TUS) uploads fail with HTTP 500 and a message about `x-amz-tagging`, add `TUS_ALLOW_S3_TAGS: "false"` to the storage service environment. Cloudflare R2 does not implement this S3 feature.

### Permission denied on uploads[#](#permission-denied-on-uploads)

Setting a bucket to "Public" only allows unauthenticated **downloads**. Uploads are always blocked unless you create an RLS policy on the `storage.objects` table. Go to **Storage** > **Files** > **Policies** in Studio and create a policy that allows `INSERT` for the appropriate roles.

### Upload URLs point to localhost[#](#upload-urls-point-to-localhost)

If uploads from a browser fail (CORS or mixed content errors), check that `API_EXTERNAL_URL` and `SUPABASE_PUBLIC_URL` in your `.env` file match your actual domain and protocol - not `http://localhost:8000`.

### Additional resources[#](#additional-resources)

*   [Storage repository `.env.sample`](https://github.com/supabase/storage/blob/master/.env.sample)
*   [S3 Authentication](/docs/guides/storage/s3/authentication)
