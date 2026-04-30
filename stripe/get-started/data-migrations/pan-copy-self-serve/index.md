---
title: "Copy PAN data across Stripe accounts"
source: "https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:39:21.015Z"
content_hash: "d8db286954416d18be0edf93d08ba3213be2ac8e0ebd8d7330c1e7879c77e72b"
---

The Stripe self-serve data copy service allows you to copy customer and payment data from one Stripe account to another Stripe account in the Dashboard.

A data copy involves two parties: the sender account and the recipient account.

*   **Sender account**: The Stripe account currently storing the customer data. This is the account to copy the data from.
*   **Recipient account**: The Stripe account where you want to store the customer data. This is the account to copy the data to.

Before beginning the copying process, the sender and the recipient must provide their account IDs to each other. If you’re the sender account, work with a user of the recipient account to share account IDs. If you’re the recipient account, work with a user of the sender account to share account IDs. Find your account ID by going to the [User settings](https://dashboard.stripe.com/settings/user) in the Dashboard while logged into your account.

## Data copying considerations

Consider the following when copying data to a new account:

*   We can only copy data from one account to another. We can’t merge or move the data. After it’s complete, the copied data exists on both the destination and source accounts.
    
*   We only copy the raw [Customer](https://docs.stripe.com/api/customers/object) objects and associated payment data objects. The supported payment methods include:
    
    *   Cards stored as [Card](https://docs.stripe.com/api/cards/object) objects
    *   Cards stored as [Source](https://docs.stripe.com/api/sources/object) objects
    *   Cards stored as [Payment method](https://docs.stripe.com/api/payment_methods/object) objects
    *   US ACH records stored as [Bank account](https://docs.stripe.com/api/customer_bank_accounts/object) objects
    *   US ACH records stored as [Payment method](https://docs.stripe.com/api/payment_methods/object) objects
    *   SEPA mandates stored as [Payment method](https://docs.stripe.com/api/payment_methods/object) objects
*   We can’t copy Single Euro Payments Area (SEPA) stored as source objects, Bacs Direct Debit, or pre-authorized debit payments (PADs) that use the Automated Clearing Settlement System (ACSS).
    
*   We can’t copy individual [Charges](https://docs.stripe.com/api/charges/object), [PaymentIntents](https://docs.stripe.com/api/payment_intents/object), [Invoices](https://docs.stripe.com/api/invoices/object), [Plans](https://docs.stripe.com/api/plans/object), [Subscriptions](https://docs.stripe.com/api/subscriptions/object), [Coupons](https://docs.stripe.com/api/coupons/object), [Events](https://docs.stripe.com/api/events/object), Logs, [Guest customers](https://support.stripe.com/questions/guest-customer-faq), or any other Stripe objects.
    
*   The copy operation doesn’t change customer IDs, resulting in the same IDs for customers in both the destination and source account data.
    
*   The copy process assigns new object IDs of the same payment type to payment data. For example, the process assigns a new card object ID to all card objects and new payment method object IDs to all payment method objects. After the copy process is complete, Stripe creates and uploads a CSV mapping file to the **Documents** section of the recipient’s Dashboard. The mapping file is available to the recipient only. The mapping file contains the following headers:
    
    *   `customer_id_old`
    *   `source_id_old`
    *   `customer_id_new`
    *   `source_id_new`
    
    Customer IDs don’t change during the copying process, so `customer_id_old` and `customer_id_new` have the same value after the copy finishes. `source_id_old` is the old payment method ID from the sharing account, and `source_id_new` is the new payment method ID from the recipient account.
    
*   Source account data remains intact. We recommend keeping the original source account as a backup for your data.
    
*   The recipient account must be an activated account. To activate the account, log in to the Dashboard and follow the prompts at the top-left of the home screen to activate payments.
    
*   You can’t copy deleted customers from the sharing account to the recipient account. After you delete a `Customer`, there’s no way to restore that object.
    
*   If you delete a `Customer` in the recipient account, a second copy doesn’t restore that customer.
    
*   During a second copy involving the same accounts and same customers, previously-copied `Customer` objects aren’t duplicated. The second copy copies over brand new Stripe `Customer` objects or new payment methods only for previously-copied `Customer` objects. If you delete a customer in the account, re-copying that customer from the sharing account doesn’t restore the deleted customer.
    
*   The copy includes only Stripe `Customer` objects (`cus_xxx`). We can’t copy Guest (`gcus_xxxx`) customers—see [Guest customers](https://support.stripe.com/questions/guest-customer-faq) to learn more. Sender accounts must have `Customer` objects stored to process a data copy.
    
*   Accounts are limited on the number of copies they can perform in a given period. If you need to send additional copies, you can [contact the Data Migration team](https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve?copy-method=full#get-stripe-support). Stripe can limit copies at any time, depending on certain account characteristics.
    
*   Stripe limits copies to one copy per unique recipient until the recipient account authorizes and accepts the first copy request.
    
*   If any expired cards are included in the records that you copy over to the destination account, there’s the possibility that [Card Account Updater](https://stripe.com/guides/optimizing-authorization-rates#card-account-updater) (CAU)—if turned on for the destination account—will communicate with the card networks to automatically update these cards. This can result in additional CAU fees for the destination account. To avoid the possibility of CAU fees related to a self-serve copy, the destination account team must work with the source account team to make sure that no expired cards are included in the copy data set.
    

## Full or partial copy

You can perform a full or partial copy. A full copy sends all customers from the sender account. A partial copy sends a subset of customers from the sender account.

A partial copy entails sending a subset of customers from the sender account to the recipient account. There are two ways to complete a partial copy:

*   **Select customers in the Dashboard**: Recommended for copying fewer than 15 customers
*   **Upload a CSV file with a list of customer IDs**: Recommended for copying more than 15 customers

You need to complete three steps for a full data copy:

1.  The sender shares their customer data with the recipient.
2.  The recipient authorizes and accepts the customer data from the sender.
3.  The copying process finishes.

1.  The sender logs into their [Stripe account](https://dashboard.stripe.com/login) and navigates to the [Customers](https://dashboard.stripe.com/customers) page.
2.  They click **Copy customers**.
3.  In the **Copy Method** field, they click **Copy all customers**.
4.  They enter the account ID (`acct_xxxx`) of the recipient account and click **Continue**. If they haven’t previously shared customers with this recipient account, they receive a message stating that the recipient needs to authorize your request before the copy occurs.
5.  They click **Confirm**.
6.  After successfully sharing the data with the recipient, the sender can see the pending copy request on the [copy status page](https://dashboard.stripe.com/copy-status/shared).

The recipient logs into their [Stripe account](https://dashboard.stripe.com/login) and navigates to the [Customers](https://dashboard.stripe.com/customers) page. They see a pending copy request at the top that says the sender wants to share their data. The recipient clicks **Authorize and Accept**.

## The copying process finishes

After the sender completes the previous steps, the copy begins processing. The sender and recipient can see the in-progress copy on the [copy status page](https://dashboard.stripe.com/copy-status) in the Dashboard.

Most data copies finish within 72 hours, after the sender shares the customer data with the recipient and the recipient authorizes and accepts the customer data from the sender. Copies of fewer than 10,000 customers typically complete within a couple of hours.

When the copying process is complete, the sender and recipient can see the completed copy on the [Customers](https://dashboard.stripe.com/customers) page and the [copy status page](https://dashboard.stripe.com/copy-status) in the Dashboard. The recipient has the option to download the mapping file.

## Copy into or out of a Connect account

If the sender account is a Connect account without access to the Stripe Dashboard, reach out to your contact at the platform to let them know you need a data copy. The platform account owner or Data Migration Specialist needs to follow these steps:

Partial copy with customer selection isn’t available for Connect accounts.

1.  The platform account owner or Data Migration Specialist logs into their Stripe account and navigates to the [Connect](https://dashboard.stripe.com/connect/accounts/overview) page.
2.  The sender locates and selects the correct Connect account where the customers are stored.
3.  They navigate to the **Customers** section within the Connect account.
4.  They click **Copy customers**.
5.  In the **Copy Method** field, they click **Copy all customers**.
6.  They enter the account ID (format: acct\_xxxx) of the recipient account and click **Continue**. If they haven’t previously shared customers with this recipient account, they receive a message stating that the recipient needs to authorize your request before the copy occurs.
7.  They click **Confirm**. After successfully sharing their data with the recipient, they can see the pending copy request on the [copy status page](https://dashboard.stripe.com/copy-status/received).
8.  The recipient follows standard steps for authorizing and accepting customer data.

If the recipient account is a Connect account that doesn’t have access to the Stripe Dashboard, reach out to your contact at the platform to let them know you need a data copy.

The platform account owner, admin, or Data Migration Specialist need to authorize and accept customer data from the sender after the sender shares it.

To authorize the data, the recipient logs into the platform Stripe account, goes to the [copy status page](https://dashboard.stripe.com/copy-status/received), and clicks **Authorize and Accept** on the relevant pending copy request.

If your customers are stored in a platform account that you don’t own, inform your contact at the platform that you need a data copy. Direct them to follow the steps to share your customers with the recipient account. Platform accounts typically store customers for several unrelated Connected accounts. Make sure the platform account shares only your customers, by following the steps to do a partial copy.

## Status page

If you’re an account owner or Data Migration Specialist, you can view in-progress and completed copies by going to the **Customers** page and selecting **Copy customers** > **Status page**. You can toggle between **Shared** data and **Received** data.

For all other roles, you can view in-progress and complete copies on the [copy status page](https://dashboard.stripe.com/copy-status).

### Shared

On the **Shared** tab, you can see copies where your account was the sender account, sharing your customers with other accounts.

`In progress` copies are copies that are currently processing or where the sender account has initiated the copy, but the recipient hasn’t authorized and accepted it. For `Pending*` copies, the recipient needs to authorize and accept the copy to proceed. Most `In progress` copies finish within 72 hours. Copies of fewer than 10,000 customers typically complete within a couple of hours.

`Previously shared` copies are copies that were successful or canceled from your account to another.

### Received

On the **Received** tab, you can see copies where your account was the recipient account, receiving customers from other accounts.

`In progress` copies are copies that are currently processing or where the sender account has initiated the copy, but you as the recipient haven’t authorized and accepted it. For `Pending` copies, you need to authorize and accept the copy to proceed. Most `In progress` copies in this state finish within 72 hours. Copies of fewer than 10,000 customers typically complete within a couple of hours.

`Previously shared with you` copies are copies that were successful or canceled from another account to your account.

`Authorized senders` navigates to the Authorized accounts page, which shows the accounts authorized to send you their data. You need to accept the data copy requests from these accounts. After you accept, these accounts can see your business name when they enter your account ID during the sharing step. You can revoke permission from any accounts in this list, which prevents them from seeing your business name during the sharing process. When you revoke permission, future copy requests must be authorized and accepted. Only account owners, admins, and Data Migration Specialists can add and revoke authorized accounts.

## Permissions restrictions

Only the account owner or a Data Migration Specialist can perform actions from the sender account. Only the account owner, an account admin, or a Data Migration Specialist can perform actions from the recipient account and download the mapping file.

Learn how to [add a team member as a Data Migration Specialist](https://docs.stripe.com/get-started/account/teams/roles).

## Payment method considerations

### ACH bank account payment data

If you copy ACH bank accounts, you must hold your customer’s authorization to debit or credit their bank account and initiate a transaction over these networks. You’re responsible for making sure the authorizations are in a form and manner that complies with the Nacha Operating Rules. You must retain data sufficient to provide or reconstruct any ACH authorization and provide Stripe with evidence of that authorization upon request.

### ACH payment method payment data

If you copy ACH payment methods, you must hold your customer’s authorization to debit or credit their bank account and initiate a transaction over these networks. You’re responsible for making sure the authorizations are in a form and manner that complies with the Nacha Operating Rules. You must retain data sufficient to provide or reconstruct any ACH authorization and provide Stripe with evidence of that authorization upon request.

Before the copy process begins, the receiving account must acknowledge and agree that they have the [collected mandates](https://support.stripe.com/questions/collecting-ach-direct-debit-mandates-from-customers). If the receiving side doesn’t agree to this when the copy request is accepted, the copy process skips ACH payment methods during the copy process.

### SEPA payment data

If you copy SEPA payment methods, you must hold your customer’s authorization to debit or credit their bank account and initiate a transaction over these networks. You’re responsible for making sure the authorizations are in a form and manner that complies with the European Payments Council. You must retain data sufficient to provide or reconstruct SEPA authorization and provide Stripe with evidence of that authorization upon request.

Before the copy process begins, the receiving account must acknowledge that they’ve [collected mandates](https://support.stripe.com/questions/collecting-sepa-dd-mandates-from-customers). If the receiving side doesn’t agree to this when the copy request is accepted, the copy process skips SEPA payment methods during the copy process.

The [creditor IDs](https://support.stripe.com/questions/sepa-creditor-identifier-\(creditor-id\)) of the sender account and recipient account must be the same to copy SEPA payment methods.

Only SEPA Direct Debits stored as Payment Methods are supported in the copy process. SEPA Direct Debits stored as Sources aren’t included in the copy, because non-card payment methods are no longer supported by the Sources API. If you have SEPA Source objects you want to migrate, do the following:

1.  Migrate your SEPA Direct Debits from `src_` objects to `pm_` objects by following the [steps provided by Stripe Support](https://support.stripe.com/questions/reusable-object-migration-from-sources-to-payment-intents).
2.  Perform the copy, which migrates the SEPA `pm_` objects to the new account.

## India account considerations

You can’t copy data between India Stripe accounts and accounts outside of India. Regulations in India require local storage of certain payments data. If you attempt to complete a copy between an India Stripe account and an account outside of India, you receive an error message that says copying is prohibited.

#### Note

## Get Stripe support

If you run into issues or have any questions when completing the data copy, contact the Data Migration Team with this [intake form](https://support.stripe.com/contact/email?topic=migrations). You must be logged in to your Stripe account before clicking this link.

In the intake form, for migration type, select **Tell us about your other data migration use case**, and fill out the form accordingly. If you’ve already initiated a data copy, provide the migration request ID associated with the copy request. The migration request ID is in the pending banner or the status page.
