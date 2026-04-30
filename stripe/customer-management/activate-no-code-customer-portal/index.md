---
title: "Activate the no-code customer portal"
source: "https://docs.stripe.com/customer-management/activate-no-code-customer-portal"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:08:08.445Z"
content_hash: "e3a883c7369e79cfebafef4cd871f02abe3292014ca6c70d7ed94a88bf701b49"
---

## Set up Stripe's customer portal with a no-code configuration.

First, you need a Stripe account. [Login or register now](https://dashboard.stripe.com/register/).

Activate a link that you add to your website or share with your customers, allowing them to manage their payment details, invoices, and subscriptions. We’ll also add the link to your customer emails. You can set up the customer portal in a few minutes, without writing any code.

See how your customers can log in with the portal login link

[](#set-up-customer-portal)

1.  **Activate a customer portal link**
    
    On the [customer portal configuration](https://dashboard.stripe.com/settings/billing/portal) page, click **Activate link** in the **Ways to get started** section.
    
2.  **Configure the portal**
    
    Go to the [customer portal configuration](https://dashboard.stripe.com/settings/billing/portal) page and select your configuration options. Learn more about [configuration options](https://docs.stripe.com/customer-management/configure-portal).
    
3.  Add the link you activated to your site, or send it directly to your customers. They can log in to the portal with their email address and a one-time passcode.
    
    Make sure your customers have an email address set, using [contact\_email](https://docs.stripe.com/api/v2/core/accounts/object##v2_account_object-contact_email) with the Accounts v2 API or [email](https://docs.stripe.com/api/customers/object#customer_object-email) with the Customers v1 API. If multiple customers have the same email address, Stripe selects the most recently created customer that has both that email and an active subscription.
    
    For security purposes:
    
    *   Customers can’t update their email address through this link.
    *   If a customer doesn’t receive a one-time passcode after clicking the login link, make sure their email address matches the email address of an existing customer. To check, enter the email address in the search bar of the [Dashboard](https://dashboard.stripe.com/).
