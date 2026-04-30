---
title: "Linked external accounts"
source: "https://docs.stripe.com/get-started/account/linked-external-accounts"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:40:57.598Z"
content_hash: "c32a866c04b91ec0b6ba2fba76f8323d876fe6de32ab41964dde568579bc2e6a"
---

To pay out from your Stripe balances, you need to connect one or more external bank accounts. You can also choose to give Stripe access to additional financial information required for credit and risk reviews, or other Stripe products, reducing the need for us to collect additional financial information in the future.

Stripe might use your financial account information to:

*   Link your financial account for [payouts](https://docs.stripe.com/payouts).
*   Evaluate eligibility for loans or other Stripe products.
*   Enable additional Stripe product features.
*   Re-evaluate reserve balances during risk reviews.

#### Note

## Financial account data

With your consent, we can access your linked account to retrieve the following information:

*   **Account details**: Account type, account number, current balance, and historical balances.
*   **Contact information**: Your name, email address, phone number, physical address, and other details held by your financial account.
*   **Account transactions**: Each transaction’s amount, date, and description.

Here are a few Stripe products and services that rely on your financial account information:

*   **Payouts**: Stripe uses your financial account information (specifically, the account number and routing number) to verify your account to enable [payouts](https://docs.stripe.com/payouts). You can link this account during onboarding, or at a later time by using your **Linked external accounts** settings in the Stripe Dashboard.
*   **Risk**: We analyze your financial account information to ascertain if a [reserve](https://support.stripe.com/topics/reserves) is required, and decide the appropriate amount for that reserve. Linking your financial account allows Stripe to continually reassess your risk profile, which could help reduce or eliminate the need for a reserve.
*   **Capital**: Stripe Capital uses your financial account information to evaluate your loan eligibility and the details of your loan offer.

The type of data available to Stripe might vary based on your financial account or our technology partner. Go to your [Linked external accounts settings](https://dashboard.stripe.com/settings/linked-accounts) to see the accounts you’ve linked to Stripe and what information you’ve shared with different Stripe products.

#### Note

We have organizational, technical, and administrative measures in place to protect your financial account data from unauthorized access, destruction, loss, alteration, or misuse within our organization. Should you believe that your interaction with us is no longer secure (for instance, if you feel that the security of your account has been compromised), please [contact us](https://support.stripe.com/contact) immediately.

## Link a financial account

If your Dashboard prompts you to **Link your bank account to Stripe**, follow these steps:

1.  Click **Link bank account** in the **Link your bank account to Stripe** banner in your Dashboard.
2.  Click **Link your account**.
3.  Choose your bank account provider and enter your bank account login details.
4.  Select all accounts or specific accounts (such as checking or savings accounts) and click **Link accounts**.
5.  To add multiple bank accounts, click **Link another account**. If not, click **Done**.
6.  You can verify the successful linking of bank accounts on the [Linked external accounts settings](https://dashboard.stripe.com/settings/linked-accounts).

You can also link your financial accounts directly from the Dashboard by following these steps:

1.  Visit the [Linked external accounts settings](https://dashboard.stripe.com/settings/linked-accounts) in your Dashboard.
2.  Click **\+ Add account**.
3.  Choose your bank account provider and enter your bank account login credentials.
4.  Select all or specific accounts (such as checking or savings accounts) and click **Link Accounts**.
5.  To add multiple bank accounts, click **Link another account**. If not, click **Done**.
6.  Check the **Linked external accounts** page to verify that the bank accounts were successfully linked.

## Data management

Learn how Stripe manages your data.

### Data retrieval frequency

How often Stripe accesses your data depends on the products you use. For instance, when assessing a risk reserve on your account, we might access your financial account information as often as daily because understanding your business’s risk profile continuously requires this information. For other products, such as Capital, we might get your financial account data once a week or once a month.

### Data retention duration

We retain your financial account information for as long as we’re providing services to you. We also keep this information to comply with our tax, accounting, and financial reporting obligations, to meet our contractual commitments to our financial partners, and where data retention is mandated by the payment methods we support. Even if you close your Stripe account, we might still need to retain your financial account information for a certain period following any limitation periods and record-keeping requirements imposed by applicable law.

### Data sharing

We use your financial account information as outlined in the [Stripe Privacy Policy](https://stripe.com/privacy). We only use your data for internal purposes, such as offering additional products, services, or features. Stripe doesn’t sell or rent your financial account information to marketers or unaffiliated third parties. We might share your data with trusted entities (like service providers, business partners, third parties authorized by you to access this information, and for compliance purposes) as stated in our privacy policy.

### Revoke consent

At any time, you can revoke your consent by visiting your [Link external accounts settings](https://dashboard.stripe.com/settings/linked-accounts) and clicking **Remove account** on any account you want to unlink. After you revoke your consent, we stop obtaining your account data. You can learn more about what happens when you [disconnect an account](https://support.stripe.com/questions/what-happens-when-i-disconnect-a-linked-financial-account).

Choosing not to link a financial account, or unlinking one, might make you ineligible to access or receive offers for additional products or services, enhancements to current products, or services. In some cases, we might request alternative information, such as financial statements.

### Consent duration and revoking process

We ask for consent every 90 days or as required by law. You can revoke your consent anytime by going to your [Linked external accounts settings](https://dashboard.stripe.com/settings/linked-accounts) and disconnecting any of the connected accounts by clicking **Remove account**. Learn more about what happens when you [disconnect an account](https://support.stripe.com/questions/what-happens-when-i-disconnect-a-linked-financial-account). Disconnecting your bank account doesn’t impact payouts.

### Renew expired consent

In your [Link external accounts settings](https://dashboard.stripe.com/settings/linked-accounts), if your consent has expired, you’ll see an option to relink your bank account. Complete the reauthorization to renew your consent.

## Trusted entity identification

When you link a financial account with Stripe, we become the primary recipient of your account data. Depending on the purpose for linking your account, we might also share this data with certain financial institutions or service providers involved in offering Stripe Capital and other financial services. For example, if you obtain a loan through Stripe Capital, we might share your account data with service providers that help manage your loan. Stripe only shares your data as set out in the [Stripe Privacy Policy](https://stripe.com/privacy).

## Stripe technology partners

We work with a third-party data aggregator, Truelayer, to get the data you’ve agreed to share with us and other trusted entities. When you enter your login information in the credential dialog, you might be sharing this information with both Stripe and Truelayer, or otherwise granting Stripe and Truelayer permission to access your accounts. Stripe and Truelayer use your login information or authorization to regularly access your account data.
