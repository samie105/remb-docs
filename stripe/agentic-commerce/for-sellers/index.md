---
title: "Sell through agents"
source: "https://docs.stripe.com/agentic-commerce/for-sellers"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:48:13.710Z"
content_hash: "8a5e6d4993ce30a47273646e3459b2d92f4e7dbf235be2ef93924d078496aad4"
---

Create a [catalog feed](https://docs.stripe.com/agentic-commerce/product-feed) to share your product and inventory data with agents. You can send your data using the Stripe Dashboard or API. To keep data current, we recommend uploading product data once per day and send more frequent incremental updates for inventory and pricing.

#### Note

Feed uploads are processed as independent, asynchronous tasks. We don’t guarantee uploads are processed or completed in the order you submit them. If you upload multiple files in quick succession, a later upload can finish before an earlier one.

Use Stripe APIs to upload your product data CSV. We recommend using the sandbox to validate parsing, field mappings, and data quality before enabling live updates.

### Create an import

Create a `ProductCatalogImport` object using the [Product Catalog Import API](https://docs.stripe.com/api/v2/commerce/product-catalog-imports). A successful request returns a [ProductCatalogImport object](https://docs.stripe.com/api/v2/commerce/product-catalog-imports/object) in the `awaiting_upload` state. The `status_details.awaiting_upload.upload_url.url` field in the response contains the presigned URL for your file upload.

`curl -X POST https://api.stripe.com/v2/commerce/product_catalog/imports \  -H "Authorization: Bearer` 

`sk_test_REDACTED`

`" \  -H "Stripe-Version: 2026-04-22.preview" \   --json '{     "feed_type": "product",     "mode": "upsert",     "metadata": {         "file_name": "march_11_2026_product_upload.csv"     }   }'`

`{   "id": "pcimprt_xxx",   "object": "v2.commerce.product_catalog_import",   "created": "2026-03-26T00:35:01.000Z",   "feed_type": "product",   "status": "awaiting_upload",   "status_details": {     "awaiting_upload": {       "upload_url": {         "expires_at": "2026-03-26T00:40:02.000Z",         "url": "[https://stripeusercontent.com/files/us-west-2/upload/wksp_xxx](https://stripeusercontent.com/files/us-west-2/upload/wksp_xxx)"       }     }   },   "livemode": true }`

### Upload your CSV

Upload your CSV to the presigned URL. The file must be in CSV or TSV format, where each row represents one product or variant. The maximum file size is 4 GB.

`curl -X PUT \  -H "Content-Type: text/csv" \   --data-binary @"/path/to/your/file.csv" \   "{{PRESIGNED_URL}}"`

After Stripe receives the file, the import transitions from `awaiting_upload` to `processing`. Stripe validates the file and ingests the items.

### Monitor feed status and resolve errors

Stripe processes your product data, validates and cleans it, then indexes it in a format you can send to AI agents. You can monitor indexing progress in two ways:

Use a `GET` request to poll the import object and check the `status` field. Continue polling until the object reaches a terminal state: `succeeded`, `succeeded_with_errors`, or `failed`.

`curl https://api.stripe.com/v2/commerce/product_catalog/imports/`

`{{PRODUCT_CATALOG_IMPORT_ID}}`

 `\  -H "Authorization: Bearer   sk_test_REDACTED  " \  -H "Stripe-Version: 2026-04-22.preview"`

If the import completes without errors, it reaches `succeeded`. If the file is structurally valid but contains row-level errors, it reaches `succeeded_with_errors`. If the import can’t complete (for example, because the file was never uploaded, is unreadable, or an internal error occurs), it reaches `failed`.

If your import status is `succeeded_with_errors`, you can download the error file:

1.  Look for the `status_details.succeeded_with_errors.error_file.url` field in the response.
2.  Download the CSV directly from that URL before it expires.
3.  The CSV contains only the rows that failed, with a leading `stripe_error_message` column describing each error.

#### Note

Error file URLs expire after 5 minutes. To get a new URL, call the [retrieve endpoint](https://docs.stripe.com/api/v2/commerce/product-catalog-imports/retrieve) again.
