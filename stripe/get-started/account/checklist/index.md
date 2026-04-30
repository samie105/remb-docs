---
title: "Account checklist"
source: "https://docs.stripe.com/get-started/account/checklist"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:37:23.769Z"
content_hash: "c9396a3c0f66a3d863f18a46bc5c1686c96d3e7eb28a130eaf612ed2cc69dd43"
---

## Complete this checklist before taking your Stripe account live.

The items in this checklist apply to all Stripe accounts, regardless of how or where you signed up for Stripe. We also have checklists for [taking your integration live](https://docs.stripe.com/get-started/checklist/go-live) and adhering to [website payment best practices](https://docs.stripe.com/get-started/checklist/website). For the safety and security of your Stripe account, follow these steps:

*   Enable two-step authentication
    
    For security purposes, [enable two-factor authentication (2FA)](https://support.stripe.com/questions/how-do-i-enable-two-step-verification) on your Stripe account. Two-factor authentication requires that you log in with both your username and password, then verify your identity through a second factor. Stripe supports passkeys, security keys, authenticator apps, and SMS. We recommend passkeys or security keys because they’re resistant to phishing. SMS-based 2FA is vulnerable to SIM-swapping and interception, so use it only as a last resort.
    
*   Confirm your statement descriptor and public information
    
    The [statement descriptor](https://docs.stripe.com/get-started/account/set-up#public-business-information) appears on customer statements when you charge their card. Missing or incorrect information can result in confused customers creating disputes, so make sure to review your statement descriptor in the [Dashboard](https://dashboard.stripe.com/settings/public). Statement descriptors are limited to between 5 and 22 characters. They must contain at least 5 letters and can’t use the following special characters: `<`, `>`, `'`, or `"`. Stripe also recommends that you add text to your site that tells your users what they’ll see on their statements.
    
    The card issuer can automatically include other account information—for example, business name, address, email, or phone number—to show on your customer’s statements. Check that all of this information in your Stripe account is acceptable for your customers to see.
    
*   Set up email notifications
    
    Stripe can notify you of account activity by email. You can choose events to be notified of in your [Communication preferences](https://dashboard.stripe.com/settings/communication-preferences). If multiple [team members](https://docs.stripe.com/get-started/account/teams) have access to your account, each one can set their own notification preferences. At a minimum, we recommend turning on emails for successful charges and disputes.
    
*   Set up SMS from Stripe for critical account health updates
    
    Choose the events to receive notification of in your [Communication preferences](https://dashboard.stripe.com/settings/communication-preferences). Any [team member](https://docs.stripe.com/get-started/account/teams) with account access can set their own notification preferences.
    
*   Prevent and manage fraud and disputes
    
    [Fraud and disputes](https://docs.stripe.com/disputes/prevention) are unfortunate realities in all commerce. While Stripe is constantly improving its tools to help reduce these incidents, we recommend that you’re set up to:
    
    *   Regularly review [payments in the Dashboard](https://dashboard.stripe.com/test/payments).
    *   [Report charges](https://docs.stripe.com/radar/risk-evaluation) that appear suspicious using the Dashboard or API.
    *   Have [evidence](https://docs.stripe.com/disputes/responding#respond) at the ready for disputes.
    *   Prevent and mitigate [card testing](https://docs.stripe.com/disputes/prevention/card-testing).
*   Review your bank account information
    
    Incorrect bank information is a common cause of [payout delays](https://docs.stripe.com/payouts#payout-failures). Before accepting live charges, confirm [your bank details](https://dashboard.stripe.com/settings/payouts) are correct. If you process charges in [multiple currencies](https://docs.stripe.com/currencies) and have multiple bank accounts, also confirm you’ve established the correct default currency. Multiple bank accounts for additional currencies are optional as Stripe can convert any payments into your default currency.
    
    When reviewing your bank information, set your preferred [payout schedule](https://docs.stripe.com/payouts#payout-schedule). The recommended and default option is daily—as funds become available—but you can change this to best suit your business and reporting needs.
    
*   Give your team members access to your Stripe account
    
    You can give your [team members](https://docs.stripe.com/get-started/account/teams) access to your Stripe account. Stripe even lets you give different team members different permissions depending on their [roles](https://docs.stripe.com/get-started/account/teams/roles).
    
    Whenever you give a team member access to your Stripe account, don’t give them your login credentials. Require all team members to enable 2FA, ideally using passkeys or security keys. If you use [single sign-on (SSO)](https://docs.stripe.com/get-started/account/sso), you can enforce authentication policies centrally.
    
    If a team member no longer needs access to your Stripe account, remove them from your account.
    
*   Understand industry-specific restrictions
    
    Review our [Prohibited & Restricted businesses list](https://stripe.com/legal/restricted-businesses) to determine if your business operates in an industry that Stripe restricts or prohibits.
    
    If your business operates in a restricted industry, you might need to provide additional documentation before you can use Stripe as your payment processor. If your business operates in a prohibited industry, you won’t be able to use Stripe.
    
    If you have any questions about onboarding requirements or restrictions applicable to your business, [contact us](https://stripe.com/contact).
