---
title: "Running a batch job"
source: "https://docs.stripe.com/batch-api/create"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:05:51.990Z"
content_hash: "79e0abc764fbaae4fe45f240cbbc2a70b6834c5713196531dda8ca42e59567a2"
---

For the complete API reference, including all available parameters and response fields, see the [Batch Jobs API reference](https://docs.stripe.com/api/v2/core/batch-jobs?api-version=2026-03-25.preview).

To process a batch job, follow these steps:

1.  [Create a batch job](#create-a-batch-job) and specify the target API endpoint.
2.  [Upload the input file](#upload-the-input-file) with your batch requests.
3.  [Monitor job status](#monitor-job-status) through webhooks or polling.
4.  [Download the results](#download-the-results).

## Create a batch job

To start, create a batch job by sending a `POST` request to `/v2/core/batch_jobs`. Specify the target endpoint and any processing options:

`curl -X POST https://api.stripe.com/v2/core/batch_jobs \  -H "Authorization: Bearer` 

`sk_test_REDACTED`

`" \  -H "Stripe-Version: 2026-03-25.preview" \   --json '{     "endpoint": {         "path": "/v1/subscriptions/:id/migrate",         "http_method": "post"     },     "maximum_rps": 10,     "skip_validation": false   }'`

The content type for this request is a JSON file. This returns a batch job object with a `ready_for_upload` status. The upload URL and its expiration time are in the `status_details` field:

`{   "id": "batchv2_AbCdEfGhIjKlMnOpQrStUvWxYz",   "object": "v2.core.batch_job",   "created": "2026-03-09T20:55:31.000Z",   "maximum_rps": 10,   "skip_validation": false,   "status": "ready_for_upload",   "status_details": {     "ready_for_upload": {       "upload_url": {         "expires_at": "2026-03-09T21:00:31.000Z",         "url": "[https://stripeusercontent.com/files/upload/...](https://stripeusercontent.com/files/)"       }     }   } }`

The `status_details` object changes based on the current status. When the job is `ready_for_upload`, it contains the presigned upload URL and its expiration timestamp.

### Parameters

Parameter

Required

Description

`endpoint.path`

Yes

The API endpoint to target (for example, `/v1/subscriptions/:id/migrate`). See [Supported endpoints](https://docs.stripe.com/batch-api#supported-endpoints).

`endpoint.http_method`

Yes

The HTTP method for the endpoint. Currently only `post` is supported.

`maximum_rps`

No

Maximum requests processed per second (1–100). Defaults to 10.

`skip_validation`

No

Set to `true` to skip input file validation and start processing immediately. Defaults to `false`.

`notification_suppression`

No

Controls whether webhooks from the underlying API operations are delivered. Set `{"scope": "all"}` to suppress operation-level webhooks. Batch-level events are always delivered regardless of this setting. Defaults to `{"scope": "none"}`.

`metadata`

No

Key-value pairs for your internal tracking. Metadata is included in batch job events, including failure events.

## Upload the input file

After creating the batch job, upload your input file to the URL in `status_details.ready_for_upload.upload_url.url`. Use a `PUT` request with the file contents:

`curl {UPLOAD_URL} \   -X PUT \   -T input.jsonl \   -H "Content-Type: application/jsonlines"`

The input file for this request must be a JSONL file, and the content type must be `application/octet-stream`. After the upload completes, Stripe automatically starts processing. There’s no separate `start` step.

The upload URL expires 5 minutes after batch job creation. Check the `expires_at` field for the exact deadline. If the URL expires before you upload the file, the job status changes to `upload_timeout`, and you must create a new batch job. Generate the input file before you create the batch job so you can upload it promptly.

### Input file format

The file must be UTF-8 encoded and use JSONL format (newline-delimited JSON, one object per line). Each line represents a single API request to the target endpoint. CSV and other formats aren’t supported.

Each JSON object supports these fields:

Field

Required

Description

`id`

Yes

A unique identifier to correlate this request with its result. The IDs on the path parameters and the IDs on the endpoint must match, though the user is free to choose how to name them: must match `/^[A-Za-z0-9_-]+$/`.

`path_params`

Conditional

Path parameters for the endpoint. Required when the endpoint path includes placeholders (for example, `:id`). The keys in `path_params` must match the placeholders in the endpoint path exactly.

`params`

No

Request body parameters for the API call. Variations can occur based on the API method.

`context`

No

A Stripe account ID. Use this to execute the request against a specific account, such as a connected account.

### Example input file

For the `POST /v1/customers/:id` endpoint:

`{   "id": "req_001",   "path_params": {"id": "cus_1AbCdEfGhIjKlMn"},   "params": {"name": "Jenny Rosen", "email": "jenny@example.com"} } {   "id": "req_002",   "path_params": {"id": "cus_2BcDeFgHiJkLmNo"},   "params": {"name": "John Smith", "metadata": {"tier": "premium"}} } {   "id": "req_003",   "context": "acct_1234567890",   "path_params": {"id": "cus_3CdEfGhIjKlMnOp"},   "params": {"description": "Updated by batch"} }`

Each `id` must be unique within the file. Stripe uses it to correlate requests with results, because the results file isn’t ordered the same way as the input file.

## Monitor job status

You can track your batch job by polling the retrieve endpoint or by listening for [webhook events](#webhook-events). We recommend using webhook events for production integrations.

### Poll for status

`curl https://api.stripe.com/v2/core/batch_jobs/batchv2_AbCdEfGhIjKlMnOpQrStUvWxYz \  -H "Authorization: Bearer` 

`sk_test_REDACTED`

`" \  -H "Stripe-Version: 2026-03-25.preview"`

The content type for this request is a json file. While the job is running, `status_details` includes real-time progress counts:

`{   "status": "in_progress",   "status_details": {     "in_progress": {       "success_count": "1",       "failure_count": "0"     }   } }`

During the `validating` phase, `status_details` includes a `validated_count` field that shows how many rows Stripe has validated so far.

Batch job API calls appear in the Stripe Dashboard or Workbench request logs. The underlying API calls don’t appear in the request logs. Use the retrieve endpoint or webhook events to monitor progress. To debug individual request failures, check the results file.

### Job lifecycle

After you upload the input file, the batch job progresses through these statuses:

Status

Description

`ready_for_upload`

The batch job was created and is waiting for the input file.

`validating`

The input file was uploaded and Stripe is validating it. Skipped when `skip_validation` is `true`.

`in_progress`

Validation passed (or was skipped) and Stripe is processing requests.

`complete`

All requests have been processed. Results are available for download.

`cancelling`

A cancelation was requested. Stripe is finishing in-flight requests.

### Terminal statuses

Status

Description

`validation_failed`

The input file contains errors. No requests were processed. Check the batch job object for error details. This is only applicable when `skip_validation: false`.

`batch_failed`

An unexpected error occurred during processing.

`cancelled`

The batch job was canceled. Partial results might be available.

`upload_timeout`

The upload URL expired before the file was uploaded. Create a new batch job.

`timeout`

The batch job exceeded the maximum processing duration of 24 hours. Partial results might be available.

### Validation

When `skip_validation` is `false` (the default) Stripe validates the entire input file before processing any requests. This validation catches errors such as:

*   Invalid JSON in any row.
*   Missing or invalid `id` fields.
*   Duplicate IDs.
*   Missing required `path_params` for the target endpoint.
*   Malformed parameters.

If validation fails, the status changes to `validation_failed`, and Stripe doesn’t attempt any requests. The batch job object includes details about the first error it encounters.

When `skip_validation` is `true`, the job transitions directly from `ready_for_upload` to `in_progress` after upload. Errors in individual requests appear in the results file instead of blocking the entire batch.

### Webhook events

Batch jobs emit v2 thin events for every lifecycle transition. To receive these events, you must configure a [v2 event destination](https://docs.stripe.com/event-destinations).

Batch job events require v2 event destinations. They aren’t delivered to v1 webhook endpoints.

The following events are available:

Event type

Description

`v2.core.batch_job.created`

A batch job was created.

`v2.core.batch_job.ready_for_upload`

The batch job is ready for file upload.

`v2.core.batch_job.validating`

File upload complete, validation in progress.

`v2.core.batch_job.validation_failed`

Input file validation failed.

`v2.core.batch_job.completed`

All requests have been processed.

`v2.core.batch_job.batch_failed`

The batch job failed unexpectedly.

`v2.core.batch_job.canceled`

The batch job was canceled.

`v2.core.batch_job.timeout`

The batch job exceeded maximum processing duration.

`v2.core.batch_job.upload_timeout`

The upload URL expired before the file was uploaded.

`v2.core.batch_job.updated`

The batch job status or progress changed.

All batch job events include the metadata you provided when creating the job. Use this to correlate events with your internal systems.

When `notification_suppression` is set to `{"scope": "all"}`, webhooks from the underlying API operations (for example, subscription update events) are suppressed. Batch-level events listed above are always delivered regardless of this setting.

## Download the results

When the batch job reaches `complete` status, the `status_details` field includes a summary of successes and failures, along with a presigned download URL for the output file:

`{   "id": "batchv2_AbCdEfGhIjKlMnOpQrStUvWxYz",   "object": "v2.core.batch_job",   "created": "2026-03-09T20:55:31.000Z",   "maximum_rps": 10,   "skip_validation": true,   "status": "complete",   "status_details": {     "complete": {       "success_count": "2",       "failure_count": "0",       "output_file": {         "content_type": "application/jsonlines",         "size": "8514",         "download_url": {           "expires_at": "2026-03-09T22:05:31.000Z",           "url": "[https://stripeusercontent.com/files/download/...](https://stripeusercontent.com/files/)"         }       }     }   } }`

Download the file using the URL in `status_details.complete.output_file.download_url.url`. Stripe provides an output file when the batch job reaches any of these states:

*   `complete`
*   `cancelled`
*   `timeout`
*   `validation_failed`

To see when the download URL expires, check the `expires_at` field for the deadline.

The results file contains both successful and failed requests in a single file. To find failures, filter for rows where `status` isn’t `200`.

### Results file format

The output file uses JSONL format (one JSON object per line). Each line contains these fields:

Field

Description

`id`

The request ID from the input file. Use this to correlate results with requests.

`response`

The full API response object. Contains the resource on success, or an error object on failure.

`status`

The HTTP status code as an integer (for example, `200`, `402`).

### Example results file

Successful requests return the full API resource in the `response` field:

`{   "id": "req_001",   "response": {     "id": "sub_1AbCdEfGhIjKlMn",     "object": "subscription",     "status": "active",     "billing_cycle_anchor": 1710021331,     "current_period_end": 1712613331,     "current_period_start": 1710021331   },   "status": 200 } {   "id": "req_002",   "response": {     "id": "sub_2BcDeFgHiJkLmNo",     "object": "subscription",     "status": "active",     "billing_cycle_anchor": 1710021331,     "current_period_end": 1712613331,     "current_period_start": 1710021331   },   "status": 200 }`

Failed requests return an error object:

`{   "id": "req_003",   "response": {     "error": {       "message": "This subscription cannot be migrated because it is not active. Current status is canceled.",       "type": "invalid_request_error",       "code": "resource_invalid_state"     }   },   "status": 400 }`

Results aren’t returned in the same order as the input file. Use the `id` field to match each result to its corresponding request.

## Cancel a batch job

You can cancel a batch job that hasn’t completed yet by sending a `POST` request:

`curl -X POST https://api.stripe.com/v2/core/batch_jobs/batchv2_AbCdEfGhIjKlMnOpQrStUvWxYz/cancel \  -H "Authorization: Bearer` 

`sk_test_REDACTED`

`" \  -H "Stripe-Version: 2026-03-25.preview"`

Cancelation is asynchronous. The job first transitions to `cancelling` while in-flight requests finish, then to `cancelled`. Any partial results from requests processed before cancelation are available in the results file.
