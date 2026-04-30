---
title: "Restricted API keys"
source: "https://docs.stripe.com/keys/restricted-api-keys"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:55:17.567Z"
content_hash: "0274cb1791b5658d6843ac3e0f63c9f21023e828aa1d2ea6cbc941eacc7e9148"
---

You can use a restricted API key (RAK) to assign specific Stripe API permissions to your API keys, including API keys you give to AI agents. Using a RAK like this limits the potential damage to your business if an API key is exposed to a bad actor. If a restricted API key doesn’t have the correct permissions to complete an API request, Stripe returns an [invalid request error](https://docs.stripe.com/error-handling#invalid-request-errors).

## What is a restricted API key?

When you sign up for Stripe, you get a [secret API key](https://docs.stripe.com/keys#obtain-api-keys) (starts with `sk_live_` or `sk_test_`). Any person, agent, or system with your secret key can do _anything_ in your Stripe account: create charges, issue refunds, read customer data, trigger payouts, and more.

A restricted API key (RAK) starts with `rk_live_` or `rk_test_` and can do only what you choose. When you create a RAK in the Stripe Dashboard, you select which Stripe resources the key can access and the permissions for each resource: **Read**, **Write**, or **None**. All Stripe APIs support restricted API keys.

You can use RAKs as a defensive measure to protect your Stripe account in case your keys are exposed or compromised. If a bad actor obtains a RAK, they’re limited to that key’s permissions. For example, you could create a RAK that can only read dispute data and nothing else. If a bad actor obtained that key, they could only read dispute data. They couldn’t create charges, access customer payment methods, or trigger payouts.

Stripe recommends always using RAKs instead of unrestricted secret keys, especially when giving a key to an AI agent. Use RAK permissions to limit what an agent can do in your account.

Always follow [best practices](https://docs.stripe.com/keys-best-practices) when using RAKs to avoid accidental exposure or compromise. Treat RAKs with the same caution as secret API keys.

## Why use restricted keys instead of secret keys?

Secret key (`sk_`)

Restricted key (`rk_`)

**Scope of access**

Full access to every API resource

Only the permissions you assign

**Impact if compromised**

A bad actor can do anything in your account

A bad actor can do only what the key allows

**Suitability for AI agents**

An agent might do things you don’t want in your account

You explicitly control the agent’s permissions

**Third-party sharing**

Dangerous: gives full control to the third party

Safer: you hand out only the access the third party needs

**Principle of least privilege**

Not possible to achieve with unrestricted keys

You can give keys minimal permissions

**Stripe recommendation**

Use sparingly and protect aggressively

**Preferred**: Use restricted keys wherever possible

### Reasons to switch to restricted API keys

*   **Limit the impact of a potential key takeover**: If a restricted key is compromised, a bad actor can access only the specific resources you allowed that key to access.
    
*   **Safely share keys with third parties**: Stripe discourages sharing keys in most circumstances, but for certain third-party integrations, you might need to share a key. For example, if a vendor needs to monitor your disputes, give them a restricted key with read-only dispute access, not your unrestricted secret key. If you’re working with a third party, make sure they follow [best practices](https://docs.stripe.com/keys-best-practices) to handle the key safely, like using an IP allowlist if possible to mitigate the risk of the key being compromised and expiring the key if the relationship ends.
    
*   **Meet compliance expectations**: Many security audits and compliance frameworks expect you to follow the principle of least privilege. Restricted keys make that straightforward.
    
*   **Combine with IP restrictions**: You can lock any restricted key to a specific set of IP addresses for an additional layer of defense.
    

## Migrate from a secret key to a restricted key

Restricted API keys are drop-in replacements for secret API keys. To use a restricted API key, provide it to your code in the same way you provide your secret key, following [best practices](https://docs.stripe.com/keys-best-practices) to avoid accidentally exposing the key. Every Stripe API supports restricted API keys. You need to configure each restricted key’s permissions to get the benefits.

Here’s a step-by-step approach to migrate from a secret key to a restricted key. See [Assign permissions to a restricted API key](#assign-permissions) to understand how to reduce a restricted key’s permissions.

### Review the secret key’s API usage

Review your code and any third-party integrations to catalog the Stripe products you use and the API calls you currently make with your secret key.

Review the secret key’s [request logs in Workbench](https://dashboard.stripe.com/workbench/logs). You can use the table below to map successful API requests to the RAK permissions they need.

HTTP method

RAK permission type

GET

read

POST

write

DELETE

write

For example, if you see successful calls to `GET /v1/customers`, you need to add read permissions for the [Customer](https://docs.stripe.com/api/customers) resource to a replacement RAK’s permissions.

### Create a restricted key in a sandbox

Stripe recommends creating a restricted key in a Stripe sandbox before creating a live-mode key.

1.  Go to the [API keys page](https://dashboard.stripe.com/apikeys) in the Stripe Dashboard.
2.  Click **Create restricted key**.
3.  Give it a descriptive name, such as `billing-service-test`.
4.  For each resource, set the permission to **None**, **Read**, or **Write** based on the API usage you observed earlier.

### Configure your staging environment to use the restricted key

In your test or staging application, replace the secret key with the restricted key in your server environment (for example, in an environment variable or secrets vault). The Stripe SDK and HTTP calls that use your key work identically. The only difference is the key value.

### Review the restricted key’s request logs for errors and adjust permissions

Review the restricted key’s logs in test mode from the [key list](https://dashboard.stripe.com/apikeys) by clicking the overflow menu () next to the key and selecting **View request logs**.

If you find any error messages such as `403 ERR`, edit the restricted key’s permissions to add the actions that failed:

1.  Click the overflow menu () next to the key.
2.  Select **Edit key**.
3.  Repeat your tests in a sandbox to confirm that you have assigned the restricted key the correct permissions.

Check your application logs for Stripe API errors. If the restricted key sent with a request doesn’t have the correct permissions, the response body includes an error message explaining which permissions to add.

### Create a live-mode restricted key

Create a new restricted key in live mode with permissions that match the test-mode key you tested.

### Configure your production environment to use the restricted key

Use the new key in your production environment in the same way you configured the test key in your staging environment.

### Retire the old secret key

When you’re confident everything works in test mode, [rotate](https://docs.stripe.com/keys#rolling-keys) or [expire](https://docs.stripe.com/keys#delete-secret-key) your old secret key in the Dashboard. This ensures that no one can use it in the future. You can set a delayed expiration (up to 7 days) if you want a safety window during which you can still revert to the secret key.

## Assign permissions to a restricted API key

You can configure restricted keys to fit your specific use cases in line with the principle of least privilege: a key should have the minimum permissions necessary to do its job, and no more. Here are several practical approaches to assign permissions.

### Audit request logs to determine permissions

1.  Go to the [API Keys](https://dashboard.stripe.com/apikeys) page in the Dashboard.
2.  Find the restricted key you are configuring.
3.  Click the overflow menu () next to the key.
4.  Click **View request logs** to see all of the requests made with that key.

Review the API endpoints your application used during your testing with the restricted key to see exactly which resources your application used and whether you read or wrote to them:

*   `GET` requests are reads
*   `POST` and `DELETE` requests are writes

If your application worked properly in your testing, make a list of the successful calls in the request logs, then compare the list to the permissions you granted to the restricted key. You can remove any permissions your key did not use. To edit the key’s permissions:

1.  Click the overflow menu ().
2.  Click **Edit key**.

If your application doesn’t work properly, you can filter the key’s request logs to show unsuccessful requests, then edit the key’s permissions in the keys menu to add the corresponding Stripe API permissions.

### Review your code

You can build a list of required permissions by searching your codebase for Stripe SDK calls. Map each call to the corresponding permission in the Dashboard. For example:

*   `PaymentIntent.create(...)` → **PaymentIntents: Write**
*   `Customer.retrieve(...)` → **Customers: Read**
*   `Dispute.list(...)` → **Disputes: Read**

Then configure your restricted key’s permissions to match only what you found.

### Start with broad permissions, then remove what you don’t need

You can initially give a restricted key broad permissions, then remove any excess permissions after reviewing how the key is used.

In a sandbox, create a restricted key from the API keys menu. The available permissions are grouped into categories. If you know your Stripe API usage doesn’t include a particular category, like Stripe Billing, you can select **None** for that category. Otherwise, select **Write** for categories that are relevant to your Stripe API usage. **Write** permissions include **Read** permissions: if a key can write an API resource, it can also read that resource.

Test your application with the test-mode restricted key as described above so that your application uses the key to make Stripe API requests. Test every component of your application that uses Stripe APIs.

## Use one restricted key per service or use case

If you have multiple services that use Stripe APIs (for example, a billing service, a reporting service, and a webhook handler), create a separate restricted key for each service, and give each key only the Stripe API permissions that each service needs. Granting separate permissions allows you to limit the potential impact of a key takeover if any one of your services is compromised.
