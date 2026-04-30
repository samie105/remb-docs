---
title: "Deep links in the customer portal"
source: "https://docs.stripe.com/customer-management/portal-deep-links"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:07:29.198Z"
content_hash: "43df0632fab5a8482ffd7651546ccfd934e27f8aa1690e7fbd44110ead7cfe0e"
---

After your customer successfully completes the flow, they see a localized confirmation page that shows the details of their completed update. You can customize the confirmation message on this page, redirect to a URL of your choice, or redirect them back to the customer portal homepage where their full account details are visible.

To customize this behavior, set [after\_completion](https://docs.stripe.com/api/customer_portal/sessions/create#create_portal_session-flow_data-after_completion) on `flow_data`.

The following example lets your customer cancel their subscription, and redirect back to your own site afterwards:

`curl https://api.stripe.com/v1/billing_portal/sessions \  -u "`

`sk_test_REDACTED`

`:" \  -d "customer=  {{CUSTOMER_ID}}  " \   --data-urlencode "return_url=[https://example.com/account/overview](https://example.com/account/overview)" \   -d "flow_data[type]=subscription_cancel" \   -d "flow_data[subscription_cancel][subscription]=  {{SUBSCRIPTION_ID}}  " \   -d "flow_data[after_completion][type]=redirect" \   --data-urlencode "flow_data[after_completion][redirect][return_url]=[https://example.com/account/subscription_canceled](https://example.com/account/subscription_canceled)"`

#### Note

The top level `return_url` is a link back to your website that the customer can click at any time (if they decide not to cancel, for example). The `flow_data[after_completion][redirect][return_url]` is a link back to your website after a customer successfully cancels their subscription.
