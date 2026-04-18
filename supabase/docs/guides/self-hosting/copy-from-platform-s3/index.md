---
title: "Copy Storage Objects from Platform"
source: "https://supabase.com/docs/guides/self-hosting/copy-from-platform-s3"
canonical_url: "https://supabase.com/docs/guides/self-hosting/copy-from-platform-s3"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:13.305Z"
content_hash: "c98662596920ed05acc403c2a2687c752ecd029cfe8967e354a349b081a8af9c"
menu_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Copy Storage from Platform","Copy Storage from Platform"]
section_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Copy Storage from Platform","Copy Storage from Platform"]
nav_prev: {"path": "supabase/docs/guides/security/security-testing/index.md", "title": "Security testing of your Supabase projects"}
nav_next: {"path": "supabase/docs/guides/security/soc-2-compliance/index.md", "title": "SOC 2 Compliance and Supabase"}
---

# 

Copy Storage Objects from Platform

## 

Copy storage objects from a managed Supabase project to a self-hosted instance using rclone.

* * *

This guide walks you through copying storage objects from a managed Supabase platform project to a self-hosted instance using [rclone](https://rclone.org/) with S3-to-S3 copy.

Direct file copy (e.g., downloading files and placing them into `volumes/storage/`) does not work. Self-hosted Storage uses an internal file structure that differs from what you get when downloading files from the platform. Use the S3 protocol to transfer objects so that Storage creates the correct metadata records.

## Before you begin[#](#before-you-begin)

You need:

*   A working self-hosted Supabase instance with the S3 protocol endpoint enabled - see [Configure S3 Storage](/docs/guides/self-hosting/self-hosted-s3#enable-the-s3-protocol-endpoint)
*   Your platform project's S3 credentials - generated from the [S3 Configuration](/dashboard/project/_/storage/s3) page
*   Matching buckets created on your self-hosted instance
*   [rclone](https://rclone.org/install/) installed on the machine running the copy

## Step 1: Get platform S3 credentials[#](#step-1-get-platform-s3-credentials)

In your managed Supabase project dashboard, go to **Storage** > **S3 Configuration** > **Access keys**. Generate a new access key pair and copy:

*   **Endpoint**: `https://<project-ref>.supabase.co/storage/v1/s3`
*   **Region**: your project's region (e.g., `us-east-1`)
*   **Access Key ID** and **Secret access key**

For better performance with large files, use the direct storage hostname: `https://<project-ref>.storage.supabase.co/storage/v1/s3`

## Step 2: Create buckets on self-hosted[#](#step-2-create-buckets-on-self-hosted)

Buckets must exist on the destination before you can copy objects into them. You can create them through dashboard UI, or with **SQL Editor**.

If you already restored your platform database to self-hosted using the [restore guide](/docs/guides/self-hosting/restore-from-platform), your bucket definitions are already present. You can skip this step.

To list your platform buckets, connect to your platform database and run:

```
1select id, name, public from storage.buckets order by name;
```

Then create matching buckets on your self-hosted instance. Connect to your self-hosted database and run:

```
1insert into storage.buckets (id, name, public)2values3  ('your-storage-bucket', 'your-storage-bucket', false)4on conflict (id) do nothing;
```

Repeat for each bucket, setting `public` to `true` or `false` as appropriate.

## Step 3: Configure rclone[#](#step-3-configure-rclone)

Create or edit your rclone configuration file (`~/.config/rclone/rclone.conf`):

```
1[platform]2type = s33provider = Other4access_key_id = your-platform-access-key-id5secret_access_key = your-platform-secret-access-key6endpoint = https://your-project-ref.supabase.co/storage/v1/s37region = your-project-region89[self-hosted]10type = s311provider = Other12access_key_id = your-self-hosted-access-key-id13secret_access_key = your-self-hosted-secret-access-key14endpoint = http://your-domain:8000/storage/v1/s315region = your-self-hosted-region
```

Replace the credentials with your actual values. For self-hosted, use the `REGION`, `S3_PROTOCOL_ACCESS_KEY_ID` and `S3_PROTOCOL_ACCESS_KEY_SECRET` you configured in [Configure S3 Storage](/docs/guides/self-hosting/self-hosted-s3#enable-the-s3-protocol-endpoint).

Verify both remotes connect:

```
1rclone lsd platform:2rclone lsd self-hosted:
```

Both commands should list your buckets.

## Step 4: Copy objects[#](#step-4-copy-objects)

Copy a single bucket:

```
1rclone copy platform:your-storage-bucket self-hosted:your-storage-bucket --progress
```

To copy all buckets:

```
1for bucket in $(rclone lsf platform: | tr -d '/'); do2  echo "Copying bucket: $bucket"3  rclone copy "platform:$bucket" "self-hosted:$bucket" --progress4done
```

For large migrations, consider adding `--transfers 4` to increase parallelism, or `--checkers 8` to speed up the comparison phase. See the [flags documentation](https://rclone.org/flags/) for all options.

## Verify[#](#verify)

Compare object counts between source and destination:

```
1rclone size platform:your-storage-bucket && \2rclone size self-hosted:your-storage-bucket
```

Open Studio on your self-hosted instance and browse the storage buckets to confirm files are accessible.

## Troubleshooting[#](#troubleshooting)

### Signature errors[#](#signature-errors)

If you see `SignatureDoesNotMatch` when connecting to either remote:

*   **Platform**: Regenerate S3 access keys from your project's Storage Settings. Ensure the endpoint URL includes `/storage/v1/s3`.
*   **Self-hosted**: Verify that `REGION`, `S3_PROTOCOL_ACCESS_KEY_ID` and `S3_PROTOCOL_ACCESS_KEY_SECRET` in `.env` file match your rclone config.

### Bucket not found[#](#bucket-not-found)

If rclone reports that a bucket doesn't exist on the self-hosted side, create it first - see [Step 2](#step-2-create-buckets-on-self-hosted). The S3 protocol does not auto-create buckets on copy.

### Timeouts on large files[#](#timeouts-on-large-files)

For very large files, increase rclone's timeout:

```
1rclone copy platform:your-storage-bucket self-hosted:your-storage-bucket --timeout 30m
```

### Empty listing on platform[#](#empty-listing-on-platform)

If `rclone lsd platform:` returns nothing, verify the endpoint URL ends with `/storage/v1/s3` and that the S3 access keys have not expired. Regenerate them from the dashboard if needed.
