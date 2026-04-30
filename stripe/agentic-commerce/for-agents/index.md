---
title: "Embed commerce into your AI interface"
source: "https://docs.stripe.com/agentic-commerce/for-agents"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:46:53.760Z"
content_hash: "75d2e59371864f79cac2cd1521a4d76bf1827eb11afadb32bd291c404db4950c"
---

Use Agentic Commerce Suite (ACS) to embed commerce capabilities into your AI interface. ACS works across multiple commerce protocols, so your AI interface can discover products, collect payment information, and complete purchases on behalf of sellers. Use the embedded integration for an end-to-end agentic commerce flow.

Use the embedded integration to manage the full checkout lifecycle through Stripe, including product feed ingestion, cart management, fulfillment, and payment collection. Stripe handles routing, authentication, error retries, and shared payment token (SPT) creation so you don’t need to integrate directly with each seller.

Agents that enable both product discovery and purchase capabilities directly within their interface might be considered marketplace facilitators (MPFs) with tax collection and remittance obligations-consult a tax advisor to understand if this applies to you.

Return cart details (for example, pricing, items, and so on)

Return updated cart details (for example, fulfillment options)

Return updated `RequestedSession`

Create `SharedPaymentToken`

Process `SharedPaymentToken`

Return completed `RequestedSession`

Checkout lifecycle

[](#get-started)

### Set up your Stripe account

[Create a Stripe account](https://stripe.com/register) if you don’t already have one. After you verify your email, activate payments by providing business and personal information, linking a bank account for payouts, and setting up two-step authentication.

### Begin agent configuration

Go to the [Agentic commerce](https://dashboard.stripe.com/agentic-commerce) page and select **Onboard as an agent** to configure your account as an agent. If you don’t already have a [Stripe profile](https://docs.stripe.com/get-started/account/profile), Stripe prompts you to create one.

### (Optional) Upload terms of service and privacy policy

You can require sellers to accept your terms of service and privacy policy before they proceed. During onboarding, upload a link for each document. Stripe shows these links to sellers when they initiate an agreement. This step is optional.

### Configure product feed acceptance

Set up SSH File Transfer Protocol (SFTP) to ingest seller product feeds from Stripe. You must provide the host name, port, and user name. Stripe generates a public and private key pair that you add to the server’s authorized keys. The public key is available as you complete agent onboarding in the Stripe Dashboard. Stripe rotates the public and private keys every 365 days and notifies the agent when it’s time to rotate.

During onboarding, Stripe also presents you with a unique challenge token. You must upload this token to your SFTP host in a file called `stripe-verification.txt`. Once Stripe verifies the presence of this file with the expected token, Stripe begins uploading product catalogs for your sellers to your SFTP server.

### Complete verification

After you complete all onboarding steps, your account might enter a pending state while Stripe completes final verification checks. Stripe might ask you to complete additional identity verification, which you can access in your [Account settings](https://dashboard.stripe.com/settings/account). Stripe sends you an email when your agent configuration becomes active.

[](#manage-seller-relationships)

### Set up an orchestrated commerce agreement

After you complete agent onboarding, all Agentic Commerce Suite (ACS) sellers can discover your account name and business profile in the Dashboard.

Before you can connect with a seller, you need an orchestrated commerce agreement (OCA). An OCA is a required connection between your agent and a seller that enables agentic commerce flows. Only a seller can initiate an OCA request.

After a seller requests an OCA, the seller appears on the Agentic commerce page in the Dashboard. You can approve or reject the OCA for that seller.

### Terminate an orchestrated commerce agreement

Either party can terminate an OCA at any time. After termination, only the party that terminated the OCA can request a new one. You can terminate an OCA on the Agentic commerce page in the Dashboard.

### Manage an OCA with webhooks

[](#product-feed-ingestion)

Seller product feeds are sent to the SFTP server you set up during onboarding. For details on the SFTP directory layout, feed schemas, and manifest handling, see [SFTP catalog ingestion](https://docs.stripe.com/agentic-commerce/product-feed/sftp-catalog-ingestion).

### Disable checkout

Each product in the feed includes a `disable_checkout` field that indicates whether the product supports checkout:

*   `false`: The product is available for checkout. You can create a `RequestedSession` to complete the purchase through Stripe.
*   `true`: The product is for discovery only. Don’t include it in checkout flows. Instead, redirect your customer to the seller’s site to complete the purchase.

[](#agent-checkout)

After you establish a valid OCA with the seller, use the Delegated Checkout API to:

*   Route requests to the correct seller automatically by using Stripe profiles.
*   Manage the checkout lifecycle with the `RequestedSession` object.
*   Handle seller errors with Stripe-defined error codes and messages.
*   Create and send shared payment tokens (SPTs) automatically.

### Create a requested session

After a customer selects items through your agent, create a `RequestedSession` with the seller’s Stripe profile and the products the customer wants to purchase:

`curl https://api.stripe.com/v1/delegated_checkout/requested_sessions \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2026-04-22.preview" \  -d "seller_details[network_profile]=profile_123" \   -d currency=usd \  -d "line_item_details[0][sku_id]={{PRODUCT_SKU}}" \   -d "line_item_details[0][quantity]=1"`

### Update requested session details

Update a `RequestedSession` as the customer provides more information during checkout.

#### Update quantity

When a customer changes an item quantity in your agent interface, update the `quantity` in `line_item_details`:

`curl https://api.stripe.com/v1/delegated_checkout/requested_sessions/{{SESSION_ID}} \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2026-04-22.preview" \  -d "line_item_details[0][key]={{LINE_ITEM_KEY}}" \   -d "line_item_details[0][quantity]=2"`

#### Add fulfillment information

When the customer provides a fulfillment address, update the `address` in `fulfillment_details` to receive a list of fulfillment options that the seller supports:

`curl https://api.stripe.com/v1/delegated_checkout/requested_sessions/{{SESSION_ID}} \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2026-04-22.preview" \  -d "fulfillment_details[name]=Jenny Rosen" \   --data-urlencode "fulfillment_details[email]=jenny@example.com" \   -d "fulfillment_details[phone]=5555551234" \   -d "fulfillment_details[address][line1]=123 Main St" \  -d "fulfillment_details[address][city]=San Francisco" \  -d "fulfillment_details[address][state]=CA" \   -d "fulfillment_details[address][postal_code]=94111" \   -d "fulfillment_details[address][country]=US"`

#### Select a fulfillment option

After you render the available fulfillment options in your agent interface and the customer selects one, update the `selected_fulfillment_option` in `fulfillment_details`:

`curl https://api.stripe.com/v1/delegated_checkout/requested_sessions/{{SESSION_ID}} \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2026-04-22.preview" \  -d "fulfillment_details[selected_fulfillment_option][type]=shipping" \   -d "fulfillment_details[selected_fulfillment_option][shipping][shipping_option]={{SHIPPING_OPTION_KEY}}"`

### Collect a payment method

Collect the customer’s payment method before you confirm the `RequestedSession`. Use Stripe Elements to securely collect payment details on web, or the [mobile SDK](#mobile-integration) for native apps.

### Collect payment method with Elements

### Confirm the requested session

After the customer provides the required information, confirm the `RequestedSession` with a `PaymentMethod`.

When you confirm a `RequestedSession`, Stripe creates an [SPT](https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens) from the `PaymentMethod` and sets usage limits and seller details. Stripe routes the token to the seller for payment processing, so you don’t need to manage the token’s lifecycle.

You must provide risk details when you confirm a `RequestedSession`. You can use a [RadarSession](https://docs.stripe.com/radar/radar-session#create-radar-session) to capture these details automatically, or you can pass the risk signals directly in the API. Stripe uses risk signals for Radar models and scoring.

`curl https://api.stripe.com/v1/delegated_checkout/requested_sessions/{{SESSION_ID}}/confirm \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2026-04-22.preview" \  -d payment_method={{PAYMENT_METHOD_ID}} \   --data-urlencode "return_url=https://example.com/agent-checkout/return" \   -d "risk_details[client_device_metadata_details][radar_session]={{RADAR_SESSION_ID}}"`

### Handle next actions

When you confirm a `RequestedSession`, the seller might complete the payment immediately, or the underlying SPT might transition to `requires_action`. This usually happens for redirect payment methods such as Klarna and Affirm, and it might happen when card payments require 3D Secure authentication.

If the payment requires additional customer action (for example, because the payment method uses a redirect or the card issuer requires 3D Secure authentication), you must handle that action because the buyer is interacting with your interface, not the seller’s. Provide a `return_url` when you confirm the `RequestedSession` and listen for the `shared_payment.issued_token.requires_action` event. You can access the `next_action` on the expandable `shared_payment_issued_token` property of the `RequestedSession`. For more information about the SPT `next_action`, see [Handle the next action](https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens?agent-seller=agent#handle-next-actions).

After the customer completes the required action, Stripe sends the `shared_payment.issued_token.active` event unless the SPT was deactivated first. Stripe then continues processing the checkout and sends `delegated_checkout.requested_session.completed` when the order is complete.

#### Get order information

If the payment doesn’t require additional customer action, or after the customer completes any required next action, the response includes order information:

`{   "id": "{{SESSION_ID}}",   "status": "completed",   "payment_method": "{{PAYMENT_METHOD_ID}}",   "shared_payment_issued_token": "{{SHARED_PAYMENT_TOKEN_ID}}",   "order_details": {     "order_status_url": "https://seller.com/orders/{{ORDER_ID}}"   },   // ... }`

Use `order_status_url` to provide customers with order tracking.

#### Retry failed payments

When configured, Stripe calls the seller’s API endpoints for real-time inventory checks or shipping quotes. Stripe returns a `424` status code if the seller’s API endpoint returns a non-`2xx` status code. You can retry payments that fail with a `424` status code if the error is transient (for example, a seller API timeout).

### Listen for webhooks

Listen for webhook events to track the `RequestedSession` lifecycle and any SPT next action that the buyer must complete to finish the payment:

Event

Description

`delegated_checkout.requested_session.created`

Stripe created a new `RequestedSession`.

`delegated_checkout.requested_session.updated`

Stripe updated the `RequestedSession` details.

`delegated_checkout.requested_session.completed`

Stripe processed the payment successfully.

`delegated_checkout.requested_session.expired`

The `RequestedSession` expired or was manually closed.

`shared_payment.issued_token.requires_action`

The SPT requires buyer action in your interface before the seller can complete the payment.

`shared_payment.issued_token.active`

The buyer completed the required action and the SPT can proceed through the rest of the checkout flow.

[](#testing)

To test your integration, enable **Test Seller** in the Agentic commerce page in the Dashboard. The test seller simulates a real seller so you can verify your checkout flow end-to-end without a live seller connection.

After you enable the test seller:

1.  Ingest the test product feed through SSH File Transfer Protocol (SFTP).
2.  Use the items from the product feed as `line_item_details` when you create a `RequestedSession` with the test seller’s Stripe profile.
3.  Complete the full checkout flow—update fulfillment details, collect a payment method, and confirm the `RequestedSession`—to verify your integration works as expected.
