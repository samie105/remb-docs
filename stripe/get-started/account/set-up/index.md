---
title: "Set up your account"
source: "https://docs.stripe.com/get-started/account/set-up"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:37:42.994Z"
content_hash: "de0cd6292d759ae1efa6026ee4bd46f875f736adceef856daab162362aced592"
---

After you create a Stripe account, you can use your account in testing environments. In a [sandbox](https://docs.stripe.com/sandboxes), you can simulate transactions and use all Stripe services without moving any real money. To use Stripe services outside of a sandbox, you must verify your business and complete any requirements needed to activate the applicable Stripe service on a live account.

If you haven’t already, [create a Stripe account](https://dashboard.stripe.com/register).

To securely set up your account:

*   [Complete the account checklist](https://docs.stripe.com/get-started/account/checklist).
*   [Verify your business](https://dashboard.stripe.com/account/onboarding) in the Dashboard. You must answer some information about your business, product, and your personal relationship to your business. As you expand your use of Stripe services, we might ask you to add or verify additional information over time.

Stripe “Know Your Customer” (KYC) obligations require that we collect and maintain this information on all Stripe users. These requirements come from our regulators and financial partners, and are intended to prevent abuse of the financial system. We review the information you provide internally to make sure that it complies with [our services agreement](https://stripe.com/legal/ssa). We’ll contact you if we need any further information.

After you activate a Stripe service on a live account, you can’t change the business origin country. If you need to set your primary business location in a different country that we support, you must create a new account.

#### Caution

Privacy and security are priorities for Stripe. Our [privacy policy](https://stripe.com/privacy) explains how and for what purposes we collect, use, retain, disclose, and safeguard any personal data you provide to us.

## Public business information

Your customers see the following details on either their card statements or in [email receipts](https://docs.stripe.com/receipts) sent by Stripe.

*   Business name and website URL
*   Support email address, phone number, and address
*   Support site URL
*   Statement descriptor text

You provide this information when you verify your business, and can update it any time in your [Account settings](https://dashboard.stripe.com/settings/public). Make sure that your statement descriptor text and business information are clearly associated with you. If your customer can’t recognize one of your payments, they might [dispute](https://docs.stripe.com/disputes) it.

Statement descriptors are limited to between 5 and 22 characters. They must contain at least 5 letters and can’t use the special characters `<`, `>`, `'`, `"`, or `*`.

You can also use dynamic statement descriptors when creating a charge so that each payment has a custom statement descriptor. This dynamic text is appended to the [shortened descriptor](https://dashboard.stripe.com/settings/public) set in the Stripe Dashboard. Statement descriptor prefixes are limited to between 2 and 10 characters. For detailed information, see the documentation on [statement descriptors](https://docs.stripe.com/get-started/account/statement-descriptors).

## Keep your account safe

After you set up your account, you’ll want to keep it safe. Here are our recommendations:

*   **Keep private information private**: Don’t share your password and keep your secret [API keys](https://docs.stripe.com/keys) confidential on your own servers. Store secret keys in a secrets vault, not in source code. Use [restricted API keys](https://docs.stripe.com/keys#secret-and-restricted-keys) instead of secret keys wherever possible. As a reminder, Stripe employees never ask you for your keys.
    
*   **Don’t reuse your Stripe password**: Use a password that’s unique to Stripe. If you use your password on another site and that site is compromised, an attacker could use those stolen credentials to take over your account. If you need to reset your password, click **Edit** > **Change password** in your [Personal details](https://dashboard.stripe.com/settings/user) settings, and enter a new password.
    
*   **Use team members to provide others with access to your account**: You can [invite others](https://docs.stripe.com/get-started/account/teams) (with limited access) to your Stripe account so that they can log in and take certain actions.
    
*   **Update your computer and browser regularly**: We recommend configuring your computer to automatically download and install updates (for example, [macOS](https://support.apple.com/en-us/HT201541) or [Windows](https://support.microsoft.com/en-us/kb/306525)). This helps protect your system against automated attacks and malware.
    
*   **Beware of phishing**: All [genuine Stripe sites](https://support.stripe.com/questions/verify-you-are-on-an-official-stripe-webpage) use the `stripe.com` domain and HTTPS. If you get an email from us that you don’t expect, go directly to our site to log in. Don’t enter your password after clicking a link in an email. If you’re ever not sure it’s really us, review [Verified Stripe domains](https://support.stripe.com/questions/verified-stripe-domains) on Stripe Support.
    
*   **Enable two-factor authentication with a passkey or security key**: When you enable two-factor authentication (2FA), you need to provide an additional verification step to complete the login process. Stripe supports passkeys, security keys, authenticator apps, and SMS. We recommend passkeys or security keys because they’re resistant to phishing. SMS-based 2FA is vulnerable to SIM-swapping and interception, so use it only as a last resort. To enable this feature, go to your [user settings](https://dashboard.stripe.com/settings/user).
