---
title: "Build a custom integration"
source: "https://docs.stripe.com/agentic-commerce/for-sellers/custom"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:47:14.091Z"
content_hash: "f858f5c4264afc950da8e492b73e8ea1cf06a4911686e95c150ecffd247e1d01"
---

### Receive an SPT

When the agent collects the buyer’s payment information and confirms the checkout, your confirmation hook receives an [SPT](https://docs.stripe.com/api/shared-payment/granted-token). The SPT is a scoped grant of the customer’s payment method from the agent to your [Stripe profile](https://docs.stripe.com/get-started/account/profile) with specific usage and expiration limits.

`POST api.seller.com/agentic/checkouts/:id/confirm {   payment_data: {     token: "spt_123",  // Stripe SharedPaymentToken ID     provider: "stripe",     billing_address?: {  // optional       line1?: string,       city?: string,       state?: string,       postal_code?: string,       country?: string     }   },   risk_details: {     client_device_metadata_details: {       user_agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"       ip_address: 1.2.3.4     }   } }`

### Use an SPT

Use [SPT resolve](https://docs.stripe.com/api/v1/shared_payment/granted_tokens/resolve) to retrieve network credentials and submit them to your payment processor.

`curl --request POST \   --url https://api.stripe.com/v1/shared_payment/granted_tokens/:id/resolve \   --header 'Authorization: Bearer sk_XXX' \   --header 'Content-Type: application/x-www-form-urlencoded'`

#### Note

The credential type appears in `payment_method_details.credentials.type` and is either `agentic_token` or `dpan`.

In collaboration with the card networks, Stripe provisions single-use `agentic_token` credentials on your behalf through Mastercard’s Agent Pay and Visa’s Intelligent Commerce programs.

`{   id: "spt_123",   object: "shared_payment.granted_token",   created: 1234567890,   deactivated_at: null,   deactivated_reason: null,   livemode: true,   shared_metadata: {},   payment_method_details: {     type: "card",     card: {       credentials?: {         type: "dpan" || "agentic_token",         // if type is agentic_token         agentic_token?: {           number?: string,           exp_month?: string,           exp_year?: string,           cryptogram?: {             value: string,             type: "CAVV" | "TAVV" | "DCVV",             eci?: string           },           encrypted?: {             encryption_type: "RSA",             encryption_block: string,             encryption_block_fields: string,             key_id: string           }         },         // if type is dpan         dpan?: {           number?: string,           exp_month?: string,           exp_year?: string,           cryptogram?: {             value: string,             type: "CAVV" | "TAVV" | "DCVV",             eci?: string           },           encrypted?: {             encryption_type: "RSA",             encryption_block: string,             encryption_block_fields: string,             key_id: string           }         }       },       brand: "visa",       country: "US",       display_brand: "visa",       exp_month: 9,       exp_year: 2029,       fingerprint: "dyRcYjZNxnHpC51l",       funding: "credit",       last4: "5627",       networks: {         available: ["visa"],         preferred: null       },       wallet: null     }   },   usage_details: {     amount_captured: {       value: 1000,       currency: "usd"     }   },   usage_limits: {     currency: "usd",     expires_at: 1234567890,     max_amount: 10000   },   agent_details: {     name: string,     network_business_profile: "profile_1234"   } }`

### Record a payment

After you capture the payment with your processor, record a [payment](https://docs.stripe.com/api/payment-record/report) and confirm the checkout flow.

`curl https://api.stripe.comv1/payment_records/report_payment \  -u "`

`sk_test_REDACTED`

`:" \  -d "payment_method_details[shared_payment_granted_token]=spt_123" \   -d "amount_requested[value]=1000" \   -d "amount_requested[currency]=usd" \   -d initiated_at=54646747 \  -d outcome=guaranteed \  -d "guaranteed[amount][value]=1000" \   -d "guaranteed[amount][currency]=usd" \   -d "guaranteed[final_capture]=true" \   -d "guaranteed[guaranteed_at]=54646747" \   -d "processor_details[type]=custom" \   -d "processor_details[custom][payment_reference]=auth_order_id_1"`

### Respond to confirm checkout and fulfill orders

`{     // status must be in_progress or completed, or you must return an error     status: "in_progress" | "completed",     order: {       id: string,       permalink_url: string,     },     metadata?: Hash }`
