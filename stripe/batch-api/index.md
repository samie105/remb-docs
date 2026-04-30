---
title: "Batch jobs"
source: "https://docs.stripe.com/batch-api"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:06:11.411Z"
content_hash: "95e40986a5b19a39e86d30a6118c6b755bbbf4f2823857b4504444da3457d1ad"
---

The Batch Jobs API allows you to perform bulk operations on Stripe resources. Instead of making individual API calls for each operation that could trigger rate limits, you can upload a file with all of your operations and let Stripe process them asynchronously. Use this for one-time migrations, bulk updates, or any operation that requires processing many resources.

## When to use batch jobs

Batch jobs work well for:

*   **Bulk migrations**: Move large numbers of subscriptions to new billing modes.
*   **Mass updates**: Update many accounts or subscriptions at once.

Batch jobs don’t work well for:

*   Operations that require an immediate synchronous response.
*   Real-time processing with tight timing requirements.
*   A single asynchronous call.

To process a batch job, follow these steps:

1.  [Create a batch job](https://docs.stripe.com/batch-api/create#create-a-batch-job) and specify the target API endpoint.
2.  [Upload the input file](https://docs.stripe.com/batch-api/create#upload-the-input-file) with your batch requests.
3.  [Monitor job status](https://docs.stripe.com/batch-api/create#monitor-job-status) through webhooks or polling.
4.  [Download the results](https://docs.stripe.com/batch-api/create#download-the-results).

## Supported endpoints

The Batch Jobs API supports the following endpoints. Each batch job targets a single endpoint, and all requests in the batch go to that endpoint.

## Limitations

Review the following limitations:

*   Batch files are limited to 5 GB. If you need to process a larger file for a higher volume of requests, split it into multiple batches.
    
*   Batch jobs only support JSONL (newline-delimited JSON) files. Batch jobs don’t accept CSV or other formats.
    
*   Requests in a batch can only use `POST` or `DELETE`. Batch jobs don’t support `GET`.
    
*   All requests in a batch must target the same API endpoint.
    
*   Batch jobs don’t guarantee the order of request processing.
    
*   Batch jobs have a maximum processing duration of 24 hours. Jobs that exceed this limit transition to `timeout` status, with partial results available.
    
*   Results are available for download for 7 days after the job completes.
    
*   The upload URL expires 5 minutes after job creation. After that period, the job transitions to `upload_timeout` and you need to create a new one.
    
*   Upload the file with a direct HTTP `PUT` request to the presigned URL.
