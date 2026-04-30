---
title: "Catalog feed"
source: "https://docs.stripe.com/agentic-commerce/product-feed"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:45:14.491Z"
content_hash: "e9dd58022cdb3717aac9dedc72e9aa33ce79bd2f3e0036311741a897e60c5964"
---

Use the product feed specification to provide your complete structured product data (for example, titles, descriptions, identifiers, pricing, fulfillment, and media). Each row represents a product or variant.

1.  Format your product data using the field reference in this document. Each field includes sample values, validation rules, and whether it’s required, recommended, or optional.
2.  Send your product data securely using the [Stripe Product Catalog Import API](https://docs.stripe.com/api/v2/commerce/product-catalog-imports) in CSV format. Each row represents one product or variant. Submit a full initial feed to the sandbox endpoint to confirm your data parses correctly and meets all field requirements before you push to production.
3.  Keep your data current and refresh your feed frequently. Update changes to product attributes, pricing, or fulfillment details when they occur to maintain customer trust and prevent stale listings. We validate and clean your data, index it into the Stripe product feed, and convert it to the format each agent requires.

### Feed processing mode

Product feed uploads support two processing modes: `upsert` (default) and `replace`.

Upsert mode treats each row as an insert or update for a product identified by its `id`.

*   If the `id` doesn’t exist, we create the product.
*   If the `id` already exists, we update the product with the values provided in that row.
*   Products not included in the file remain unchanged.

Replace mode treats the uploaded file as the complete, authoritative product catalog.

*   If the `id` doesn’t exist, we create the product.
*   If the `id` already exists, we update the product with the values provided in that row.
*   Products that exist in your catalog but aren’t present in the uploaded file are permanently deleted.
*   Replace mode is only supported for the product feed.

Use replace mode when you want the uploaded file to fully define your catalog. Use upsert mode when you want to apply partial updates without affecting products you didn’t include.

### Deletion behavior

To remove a product or variant through the feed, include the optional `delete` column in your CSV. Set it to `true` for any products you want to delete. For products you want to keep, set it to `false` or leave the field blank.

When `delete=true`, Stripe only reads the `id` and `delete` columns for that row and ignores every other column.

### Discovery-only products

Products with `disable_checkout=true` are syndicated to AI agents for discovery, but they aren’t eligible for in-agent checkout. When an agent displays a discovery-only product, it redirects the user to the product’s `link` URL to complete the purchase on your website.

Discovery-only products follow the same feed processing rules as other products. Agents can index, search, and rank them. The only difference is that the purchase action redirects to your site instead of starting an in-agent checkout session.

To learn more about setting this field, see [Feed processing instructions](#feed-processing-instructions).

## Product feed field reference

Review the full schema used by the Stripe product feed in the following sections. Each table lists data types, examples, and requirements.

### Basic product data

### Product identifiers

### Media

### Item information

### Variants

### Custom variant options

### Availability and inventory

### Price and promotions

### Fulfillment

### Performance and review signals

### Product relationships

### Compliance

### Custom labels

### Feed processing instructions
