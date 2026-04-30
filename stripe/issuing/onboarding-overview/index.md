---
title: "Onboarding overview"
source: "https://docs.stripe.com/issuing/onboarding-overview"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:04:52.779Z"
content_hash: "b2f5f2259e858450de95a30197ef2c04c8be256590b532324fe681a98f0e3bf8"
---

Use this guide to develop and launch an integration using [Issuing](https://docs.stripe.com/issuing) (in the US, EU, or UK) or [Treasury for platforms](https://docs.stripe.com/treasury/connect) (US only). To successfully go live, your offering must be a business we support, and you must integrate systems and establish business processes.

Create cards and financial accounts for your customers (US only).

**Example segments**: SaaS platforms, e-commerce businesses, and corporate benefits providers.

## Milestone 1: Get your use case approved

Start by submitting an [intake form](https://stripe.com/contact/sales) that includes a high-level overview of what you’re looking to use Stripe Issuing and Stripe Treasury for platforms for. If you’re a funded business with a dedicated team of developers, or simply working with a single developer, include those details in the form.

After you submit the form, our team will reach out within 5 days to let you know if your use case is a good fit. We also let you know if we think your desired product or products don’t [serve your use case](https://support.stripe.com/questions/supported-business-use-cases-for-stripe-issuing) well. During the call, an assigned Stripe account representative asks you more about your use case and motivation as part of our supportability assessment. We also advise you on best practices and how to build a [compelling financial services offering](https://stripe.com/guides/building-a-fintech-company).

Following the call, we’ll inform you whether we can support your business within 5 business days (certain use cases can take longer). While you wait, you can build a test integration in a [sandbox](https://docs.stripe.com/sandboxes) environment to explore the product’s capabilities, and familiarize yourself with our compliance requirements. If we deem your use case supportable, your account representative provides you with any necessary agreements, and once signed, configures your program.

## Milestone 2: Obtain live access

To obtain live mode access, you must complete the required compliance tasks. In parallel, we recommend you build your integration in a production environment and operationalize required processes.

### Build your integration

At any time, you can explore an integration in a [sandbox](https://docs.stripe.com/sandboxes) environment using our [sample app](https://docs.stripe.com/issuing/sample-app). After you sign the legal agreement, Stripe configures your program to the capabilities required for your business model. After you receive approval, you can begin submitting live transactions.

Sandbox

Live

Usage limits

With no permissions necessary, explore a broad set of platform use cases by using the sample app or the [Issuing](https://docs.stripe.com/api/issuing/authorizations) or [Treasury for platforms](https://docs.stripe.com/api/treasury/financial_accounts) APIs

Limited to what you’re approved for

Immediate access

Yes

No, you’re granted access after you receive bank partner approval

Use real funds

No

Yes

### Manage operational responsibilities

Prior to go-live, you need to take care of various operational responsibilities:

*   **Customer support:** Understand what types of customer inquiries you need to handle and [equip your support team](https://docs.stripe.com/issuing/customer-support) with the appropriate information and tools.
*   **Compliance management:** Set up the necessary compliance processes outlined in the [compliance section](#complete-compliance-tasks).
*   **Physical cards:** If your use case requires [physical cards](https://docs.stripe.com/issuing/cards/physical), you can order [standard cards](https://docs.stripe.com/issuing/cards/physical) if you want to go to market quickly. Or you can [fully customize](https://docs.stripe.com/issuing/cards/physical/order-custom-bundle) your cards with unique artwork and materials, if physical cards are a core part of your business.
*   **Mobile wallets:** If your use case necessitates Apple Pay, [review the steps](https://docs.stripe.com/issuing/cards/digital-wallets) required for approval.

### Complete compliance tasks

You need to complete a set of compliance tasks before you can launch your integration. Stripe must also review and approve your fees, terms of service, marketing material, and user interfaces. To help in this process, we provide a workflow tool to manage compliance submissions and feedback as well as to help you stay organized.

1.  **Implement all requirements for a public launch**
    
    You must submit screenshots of your marketing, onboarding, and account servicing flows using the [compliance intake form](https://form.asana.com/?k=8K51UWmWhttehNFD5qBLdg&d=974470123217835) to demonstrate compliance. Before you build user-facing marketing, onboarding, and account servicing pages, review the following content guidelines:
    
    *   [Unfair and Deceptive Acts or Practices (UDAP):](https://docs.stripe.com/treasury/connect/compliance#udap-and-correct-messaging) Keep your advertising clear and honest.
    *   [Controlling the Assault of Non-Solicited Pornography And Marketing (CAN-SPAM):](https://docs.stripe.com/treasury/connect/compliance#can-spam) Comply with commercial email messaging.
    *   [Messaging and marketing:](https://docs.stripe.com/treasury/connect/compliance#issuing-messaging-guidelines) Use the right terms to accurately reflect the account structure and benefits, including [Treasury for platforms-specific messaging](https://docs.stripe.com/treasury/connect/marketing-financial-accounts).
    *   [Prohibition on international marketing:](https://docs.stripe.com/treasury/connect/compliance#prohibition-on-international-marketing) Limit to US-based merchants.
    *   Required agreements and disclosures for [Financial Account for platforms](https://docs.stripe.com/treasury/connect/compliance#treasury-terms), [Issuing](https://docs.stripe.com/treasury/connect/compliance#issuing-terms), and [other features](https://docs.stripe.com/treasury/connect/compliance#fees-credits-rewards-terms): Appropriately disclose fees and required identifying information.
    
    Stripe requires that you submit screenshots to demonstrate the following:
    
    *   You include all required agreements and disclosures in your onboarding flow, and make them available outside of onboarding.
    *   Customers have a channel to [submit complaints](https://docs.stripe.com/treasury/connect/handling-complaints) to you and to [initiate transaction disputes](https://docs.stripe.com/issuing/purchases/disputes).
    *   [Regulatory emails](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices) are sent when required for Issuing accounts.
    *   [Regulatory receipts](https://docs.stripe.com/treasury/connect/moving-money/regulatory-receipts) are provided when required for transactions in your financial account.
    *   If you choose to provide [account statements](https://docs.stripe.com/treasury/connect/compliance#statements), you must submit evidence they meet statement requirements.
2.  **Get approved to launch to the public**
    
    After you submit your screenshots, Stripe reviews and approves within two weeks or requests additional revisions. If there are any adjustments that need to be made to your submissions, we let you know, so that you can resubmit with the needed adjustments.
    

## Milestone 3: Get ready to launch your offering

Now you’re ready to request your first virtual or physical card. Using real funds, test the program out by having designated employees complete initial transactions.

### Operationalize ongoing activities to remain compliant

Once live, you need to dedicate resources to ongoing operational requirements:

*   **Marketing reviews:** Learn how to [submit new marketing material or user interfaces](https://docs.stripe.com/treasury/connect/compliance#going-live) for approval.
*   **Customer complaints:** Receive and resolve customer complaints, and [report them to Stripe](https://docs.stripe.com/treasury/connect/handling-complaints#complaints-tracking) each month.
*   **Dispute handling:** Set up [dispute handling](https://docs.stripe.com/issuing/purchases/disputes) processes for your card program.
*   **Lost or stolen cards:** Allow customers to report lost or stolen cards so you can cancel them immediately and (optionally) [request replacements](https://docs.stripe.com/issuing/cards/replacements#replacements-for-lost-or-stolen-cards).
*   **Recordkeeping:** [Record](https://docs.stripe.com/treasury/connect/compliance#recordkeeping) all marketing materials, customer data, and [regulatory receipts](https://docs.stripe.com/treasury/connect/moving-money/regulatory-receipts), and disclosures you make for at least 5 years.
