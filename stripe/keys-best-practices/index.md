---
title: "Best practices for managing secret API keys"
source: "https://docs.stripe.com/keys-best-practices"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:52:55.717Z"
content_hash: "f9c92a0311bdff6c5a1eee5b424cf59f82c309676f8ffdaa03012a9f9cc147df"
---

Secret API keys are a form of account credentials, like a username and password. Unlike publishable keys, which are safe to include in webpages and apps, secret keys must stay in your server environment. If an unauthorized party obtains your secret API key, they can make unauthorized charges, access customer data, or disrupt your integration.

This guide is about specific ways to protect keys in your server environment. For an overview of the different types of keys Stripe supports, see [API keys](https://docs.stripe.com/keys).

## Protect secret API keys

You must handle and store your secret API keys safely at every phase of development to protect them from exposure or compromise.

*   **Never put secret API keys in source code**: Bad actors continuously scan public repositories for Stripe API keys. Even private repositories can be exposed through development environments.
    *   Use your platform’s secrets management tools (such as a secrets vault) or environment variables to supply API keys to your integration code.
    *   Periodically audit your source code, configuration files, and CI/CD pipelines for sensitive keys by searching for `sk_live_` and `rk_live_`. If you find a sensitive key, assume it has been [exposed and compromised](#handling-compromised-keys).
    *   Use a pre-commit hook in your version control system to reject commits that contain strings matching these patterns.
    *   Code snippets in Stripe documentation sometimes include keys for illustration purposes only. Don’t include real keys in your code.
*   **Never embed secret API keys in applications**: Unauthorized parties can unpack applications to search for embedded keys. For client-side use cases such as client tools, SDKs, and mobile apps, embed [publishable keys](https://docs.stripe.com/keys#obtain-api-keys) instead.
*   **Follow the principle of least privilege**: People and systems must have _only the privileges required to perform their jobs_.
    *   Define a clear policy about which team members have permission to create, update, or read secret API keys. Limit access to those who need it and audit key permissions periodically.
    *   Maintain up-to-date documentation about how to handle secret API keys within your organization. Host regular training sessions to reinforce best practices.
*   **Handle secret API keys carefully**: When you create a secret API key in the Stripe Dashboard, you see it one time. Immediately store the key in your platform’s secret-management tool or an environment variable, and don’t store it anywhere else.
    *   Share secret API keys through your platform’s secret-management tools—not in emails, chat messages, or customer support messages. **Stripe never asks you for your secret API key.**
    *   Use [restricted API keys](#limit-access) with limited permissions instead of unrestricted secret API keys.
*   **Rotate secret API keys periodically**: Define and practice a process for [rotating your Stripe API keys](https://docs.stripe.com/keys#rolling-keys). Periodic rotation confirms that you know where each key is used and that your team can replace a key on short notice. Write down a contingency plan so that if a key is exposed or compromised, your team can respond with minimum impact on your business.
*   **Audit API request logs to monitor suspicious activities**: Regularly audit or monitor API [request logs](https://docs.stripe.com/development/dashboard/request-logs) to proactively identify misused API keys. Make sure your developers aren’t using live keys when a [Sandbox](https://docs.stripe.com/sandboxes) key is appropriate. See [Sandbox versus live mode](https://docs.stripe.com/keys#test-live-modes).

## Store API keys securely

Don’t put any keys in code. Use secrets management tools (such as a secrets vault) to supply keys to your integration. You can store keys in environment variables to test code samples.

### Set an API key as an environment variable

When you run code examples, set a temporary variable for your current terminal session. The environment variable clears when you close the terminal.

`export STRIPE_API_KEY=sk_test_REDACTED`

### Reference the API key in your code

`client = Stripe::StripeClient.new(ENV["STRIPE_API_KEY"])`

## Customize API access with restricted API keys

Instead of using secret API keys with broad access, you can create [restricted API keys](https://docs.stripe.com/keys#create-restricted-api-secret-key) to assign specific privileges to people and systems. For example, you can give your invoicing system the ability to manage invoices and nothing else.

Restricted API keys help you limit the potential impact of a compromise. For example, if you need to give a Stripe API key to a third party that monitors disputes, you can create a restricted API key that grants read-only access to dispute-related resources in your Stripe account and blocks everything else. If the third party were compromised, an attacker who stole your restricted API key would be limited to those API calls.

## Limit the IP addresses that can send API requests

If your service sends API requests from stable IP addresses, you can restrict your secret or restricted API keys to those addresses. For example, if your platform offers a dedicated NAT gateway or another way to reserve an IP address or range, you can configure Stripe to block API requests with your keys from anywhere else.

For instructions about how to restrict a key to one or more IP addresses, see [how to limit secret or restricted keys](https://docs.stripe.com/keys#limit-api-secret-keys-ip-address).

## Handle compromised secret API keys

If a secret API key is exposed or compromised, rotate it immediately—even if you aren’t sure anyone saw it. Treat any exposure as a potential compromise.

*   _Exposure_ means the key became visible somewhere it shouldn’t have been, such as a public repository, a log file, or an email.
*   _Compromise_ means there’s evidence of unauthorized use of the key.

### Respond to a key exposure or compromise

Follow these steps when you discover that a secret API key has been exposed or compromised:

1.  **Rotate the affected key immediately.** [Rotate the key](https://docs.stripe.com/keys#rolling-keys) in the [Stripe Dashboard](https://dashboard.stripe.com/apikeys) and replace it in your integration. If you set a delayed expiration on the old key to avoid downtime, keep the window as short as possible.
2.  **Determine which keys to rotate.** At a minimum, rotate the specific key that was exposed. If the scope of the exposure is unclear—for example, if a server or credential store was compromised—rotate all secret and restricted API keys on your account.
3.  **Review your API request logs.** Check the [API request logs](https://docs.stripe.com/development/dashboard/request-logs) for the affected key. Look for requests you don’t recognize, unexpected IP addresses, or unusual patterns such as spikes in volume or calls to Stripe APIs your integration doesn’t normally use.
4.  **Contact Stripe support if you see unrecognized activity.** If your request logs show activity you can’t account for, contact [Stripe support](https://support.stripe.com/) for help investigating and mitigating the impact.

### Proactive protection for Stripe keys

If Stripe detects an exposed secret or restricted API key, we notify you and request that you rotate the key. In some cases, Stripe deactivates the key proactively and notifies you about any actions we take.

Stripe doesn’t guarantee detection of all exposed or compromised keys. Following these best practices helps you prevent key exposure and keep your integration with Stripe secure.

### Managed API keys

Some server platforms or hosting providers can [manage Stripe API keys](https://docs.stripe.com/keys#managed-api-keys) on behalf of their customers, including provisioning and rotation steps. Managed API keys remain on the server platform, which supplies them to your server-side code. The [Stripe Dashboard](https://dashboard.stripe.com/apikeys) lists your managed API keys but doesn’t expose complete keys.

Managed API keys are secret keys, not restricted API keys. You can’t assign these keys limited permissions, and you can’t constrain managed API keys to specific IP address ranges.

Because managed API keys are sensitive secrets in a server environment, follow the best practices in this guide to protect them. Never hard-code managed API keys in your server-side code, and never expose environment variables directly from your application.

If your server platform provides managed Stripe API keys to your application as environment variables and supports marking certain environment variables as _sensitive_ to trigger extra protections, make sure to mark any Stripe keys as sensitive.

If you suspect that a managed API key has been exposed or compromised, [rotate it from the Stripe Dashboard](https://dashboard.stripe.com/apikeys) or on the server platform. If you rotate a managed API key in the Stripe Dashboard, or if Stripe detects that your key has been compromised and expires it to protect your Stripe account, we synchronize with your server platform automatically on your behalf—you don’t need to change the key in two places.

When your managed API keys change, you generally need to redeploy the corresponding server-side applications unless your server platform redeploys them automatically.
