---
title: "SFTP catalog ingestion"
source: "https://docs.stripe.com/agentic-commerce/product-feed/sftp-catalog-ingestion"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:45:34.116Z"
content_hash: "7cdbe68dcd77cb753803fafdf920b3af720380c1a3437f3d842aac72ea94891c"
---

Stripe provides business product catalogs to your SFTP (SSH File Transfer Protocol) server as daily full-catalog snapshots. Use this guide to set up your ingestion pipeline and validate incoming data.

[

## Connectivity and directory structure



](#connectivity-and-directory-structure)

Stripe connects to your server using the following configuration:

*   **Protocol**: SFTP (SSH File Transfer Protocol) over port `22`
*   **Authentication**: SSH key-based using Ed25519
*   **Password authentication**: Disabled

### Metadata

Each business directory contains a `merchant_metadata.json` file. Read this file before you ingest catalog data to verify that you’re importing data for the correct business.

### Directory structure

Stripe assigns each business a unique top-level directory. Stripe organizes the SFTP root by business Stripe profile ID and separates data by feed type within each business directory.

`/root   stripe-verification.txt      # Uploaded by agent during onboarding   /[stripe_profile_id]/     merchant_metadata.json     /catalog/                  # Full daily snapshots       full_catalog_part1_of_2.csv.gz       full_catalog_part2_of_2.csv.gz       manifest.json     /updates/                  # High-frequency deltas (opt-in)       delta_part1_of_1.csv.gz       manifest.json`

### SFTP server verification

During agent onboarding in the Stripe Dashboard, you provide your SFTP host details and Stripe generates a unique challenge token. You must upload this token to the root of your SFTP server in a file named `stripe-verification.txt`.

After Stripe receives your SFTP host details and a seller enables your agent, Stripe starts syndicating that seller’s product catalog to your SFTP host. Syndication begins only after Stripe verifies that the challenge token in `stripe-verification.txt` matches the token generated during onboarding. Keep this file in place—removing it can affect your ability to receive feeds.

[](#hybrid-feed-model)

Stripe delivers data in two distinct streams to optimize bandwidth and processing.

Feed

Frequency

Primary purpose

File name pattern

Product Master Feed

Every 24 hours

Stable metadata: descriptions, images, brand, and taxonomy

`full_catalog_part[N]_of_[Total].csv.gz`

Delta Feed (opt-in)

Hourly

Real-time price, sale price, availability, and inventory changes

`delta_part[N]_of_[Total].csv.gz`

[

## Sharding and manifest



](#sharding-and-manifest)

For catalogs larger than 100,000 rows, Stripe might split the data into multiple shard files. Stripe uploads `manifest.json` last. Treat it as the signal that the batch is complete and ready to ingest. Don’t begin ingestion until `manifest.json` is present. If data files appear in `catalog/` or `updates/` but `manifest.json` doesn’t arrive, [contact Stripe Support](https://support.stripe.com/contact).

### Manifest structure

The manifest includes the Stripe profile ID, batch metadata, feed type, total shard count, and the full list of shard file names.

`{   "stripe_profile_id": "profile_12345",   "batch_timestamp": "2026-03-25T14:30:00Z",   "feed_type": "product_master",   "total_shards": 2,   "files": [     {"name": "full_catalog_part1_of_2.csv.gz"},     {"name": "full_catalog_part2_of_2.csv.gz"}   ] }`

[](#csv-encoding)

All data files use gzip compression with a `.csv.gz` extension. The uncompressed content is UTF-8 encoded, comma-separated, includes a header row, and follows standard CSV quoting rules for commas, quotes, and embedded line breaks.

For all fields:

*   An empty value means the field is unset.
*   Each row has a unique `id`.
*   Multi-value fields such as `additional_image_link` are serialized as comma-separated URLs within a single quoted CSV field.

[](#product-master-feed-schema)

The Product Master Feed contains the full catalog snapshot for stable product metadata. Each row represents a product or variant. Required fields are always present. Recommended fields are typically present but might be absent for some products. Optional fields might or might not be populated, depending on the business’s data.

### Required and recommended fields

### Optional fields

[](#synchronization-rules)

The contents of the SFTP directory are the current source of truth.

### How Stripe delivers data

Use the following delivery behaviors to design your ingestion process.

*   Stripe overwrites the contents of `catalog` and `updates` each cycle. The SFTP directory always reflects the latest batch. Stripe doesn’t retain prior batches.
*   Stripe uploads data files first and uploads `manifest.json` last so you don’t ingest a partial batch.

### Process feeds

Use these guidelines to process each feed batch correctly.

*   Use `batch_timestamp` to determine whether you already processed a batch.
*   Treat the latest full Product Master Feed as authoritative for the complete catalog state.

### Deletion behavior

Support both explicit and implicit deletion:

*   **Explicit deletion**: If a row in the Product Master Feed includes `delete=true`, remove the product or mark it inactive.
*   **Implicit deletion**: If a product was previously known but is absent from the latest full Product Master Feed, remove the product or mark it inactive.
*   **Reappearance**: If a previously deleted or omitted product appears again in a later full Product Master Feed, treat it as active unless `delete=true` is set.

[](#ingestion-rules)

Apply these rules to make your ingestion pipeline reliable and auditable:

*   **Timestamp validation**: Only update local records if the incoming record is newer than the stored record when record-level timestamps are available.
*   **Idempotency**: Reprocessing the same successfully processed batch must not create duplicate products or duplicate updates.
*   **Auditability**: Retain your own record of processed `batch_timestamp` values.
