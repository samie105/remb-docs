---
title: "Best practices"
source: "https://docs.stripe.com/batch-api/best-practices"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:05:31.615Z"
content_hash: "cb1d4d75cedb4088410e7ac882058dd0e290dbea3c315884ac7cbe44240f1051"
---

## Choose the right `maximum_rps`

The `maximum_rps` parameter controls how fast Stripe processes requests in your batch. Batch processing uses a separate rate limit pool from your main API requests, so batch jobs don’t affect your account’s regular API traffic.

*   **Lower values**: 1–10 are suitable for non-urgent bulk operations.
*   **Higher values**: 50–100 process batches faster and are suitable for independent operations across different resources.

## Use validation for critical operations

Keep `skip_validation` set to `false` (the default) for operations where partial processing would cause issues. Validation ensures your entire file is well-formed before any requests are executed.

Set `skip_validation` to `true` when you’ve already validated your input data and want faster job startup, or when processing partial results is acceptable.

## Split large workloads

If you have an input file larger than 5GB, split workloads into multiple batch jobs. You can run multiple batch jobs concurrently.

## Verify resource state before batching

Confirm that all target resources are in the required state before submitting a batch. For example, subscriptions must be active before they can be migrated with `/v1/subscriptions/:id/migrate`. Batch jobs execute the target operation directly and don’t change resource state as a prerequisite.

## Handle errors in results

Always check the `status` field in each result line. Individual requests within a successful batch can still fail (for example, because of insufficient funds or invalid parameters). Build your integration to filter the results file for non-`200` statuses and handle failures accordingly.

## Prepare your file before creating the job

The upload URL expires 5 minutes after batch job creation. Generate and validate your input file before calling the create endpoint. If you need to prepare data dynamically, complete all data retrieval and file generation first, then create the batch job and upload immediately.

## Common errors

### Upload URL expired

If you don’t upload the input file before the `expires_at` timestamp (5 minutes after job creation), the batch job transitions to `upload_timeout` status. Create a new batch job and upload the file promptly. Generate your input file before creating the batch job to avoid this.

### Invalid resource state

Individual requests can fail if the target resource isn’t in the expected state. For example, when using `/v1/subscriptions/:id/migrate`:

*   **Subscription isn’t active**: The subscription must be in an `active` state before you can migrate it. Canceled or incomplete subscriptions return a `400` error with `resource_invalid_state`.
*   **Subscription already migrated**: Attempting to migrate a subscription that has already been migrated returns an error.

These per-request errors appear in the results file with a non-`200` status code. The batch job itself still completes successfully (the batch continues processing if individual lines fail).

### Path parameter mismatches

The keys in `path_params` must exactly match the placeholders in the endpoint path. For example, if your endpoint path is `/v1/subscriptions/:id/migrate`, your `path_params` must use `{"id": "sub_..."}`. A mismatch between the placeholder name and the key causes a validation error or a `400` status in the results file.

### Upload content type

The upload `PUT` request must use `Content-Type: application/octet-stream`. Other content types are rejected.

### File format errors

When `skip_validation` is `false`, these errors cause the entire batch to fail with `validation_failed` status:

*   Rows that aren’t valid JSON
*   Missing `id` field on any row
*   Duplicate `id` values across rows
*   IDs containing characters outside `A-Za-z0-9_-`

When `skip_validation` is `true`, file-level format errors can cause individual rows to fail rather than blocking the entire batch.

### Job processing timeout

Batch jobs that run longer than 24 hours transition to `timeout` status. Partial results from requests that completed before the timeout are available in the results file.
