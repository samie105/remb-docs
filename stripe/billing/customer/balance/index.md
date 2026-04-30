---
title: "Customer invoice balance"
source: "https://docs.stripe.com/billing/customer/balance"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:09:07.208Z"
content_hash: "2d00295e63877ef8c4ca4c592a99568bbe0851c9ec6172061c6d65fc3a399d1a"
---

Every customer in Stripe Billing has an invoice balance that you can issue credit and debit adjustments against. Adjustments in the invoice balance could be a credit (meaning you owe them money) or a debit (meaning they owe you money). These adjustments sum up to a balance on the customer that you can apply to future [invoices](https://docs.stripe.com/api/invoices).

Because the invoice balance is computed from a ledger — an immutable list of debit and credit transactions — it provides an audit trail of transactions for the customer. These [Customer Balance Transactions](https://docs.stripe.com/api/customer_balance_transactions/object) can refer to the object related to the adjustment (such as a [Credit Note](https://docs.stripe.com/invoicing/dashboard/credit-notes) or [Customer](https://docs.stripe.com/invoicing/customer)), or even [metadata](https://docs.stripe.com/api/metadata) for your own reference.

#### Use the Accounts v2 API to represent customers

## Example use cases

Some common use cases for customer invoice balances include:

*   [Issuing a Credit Note](https://docs.stripe.com/invoicing/dashboard/credit-notes) to create a credit that reduces the amount due on the next invoice.
*   Prorations from [downgrading a subscription](https://docs.stripe.com/billing/subscriptions/change-price) can indirectly create credits to reduce the amount due on the next invoice.
*   When the amount due on an invoice is less than the [minimum chargeable amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts) the invoice is marked as paid and the amount owed moved to the invoice balance as a debit. This functionality only occurs for customers without a [cash\_balance](#cash-balances).

## Customer invoice balance details

Keep the following details in mind when using customer invoice balances:

*   The invoice balance automatically applies toward the next invoice finalized to a customer.
*   You can’t choose a specific invoice to apply the invoice balance to.
*   You can’t choose to not apply the invoice balance to an invoice.
*   The invoice balance is in the customer’s currency.
*   Customers with a [cash balance](https://docs.stripe.com/api/customers/object#customer_object-cash_balance) can’t keep a positive balance. In other words, they can’t increase the amount due on the next invoice.
*   The invoice balance doesn’t apply to invoices created by Checkout Sessions with [`invoice_creation`](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-invoice_creation) enabled.
*   You can’t apply invoice balances to previously created invoices that are still open. However, [editing an open invoice](https://docs.stripe.com/invoicing/invoice-edits) applies any invoice balance to the invoice revision.

## Debits and credits

**Negative values** are treated as a _credit_ (a reduction in the amount owed by the customer) that you can apply to the next invoice.

**Positive values** are treated as a _debit_ (an increase in the amount owed by the customer to you) that you can apply to the next invoice.

## Transactions

All modifications to the invoice balance are recorded as [Transactions](https://docs.stripe.com/api/customer_balance_transactions/object). After it’s been created, you can only update its `description` or `metadata`—you can’t edit other properties or delete a transaction.

### Undo a transaction

You can only undo a transaction by creating a corresponding, reversing transaction. For example, if you credit the customer 10 USD, you must debit the customer 10 USD in a new transaction, each canceling the other out.

### Transaction types

All [Transactions](https://docs.stripe.com/api/customer_balance_transactions/object) created with the API or in the Dashboard have a [type](https://docs.stripe.com/api/customer_balance_transactions/object#customer_balance_transaction_object-type) value of `adjustment`, representing a debit or credit manually created by you for the customer.

The `type` property has many more possible values to represent the creation source and reason for the transaction. The following table outlines and describes each of these `type` values:

Type

Description

`adjustment`

An explicitly created adjustment transaction to debit or credit the invoice balance. This is the only type of transaction that you can create using API integrations and the Dashboard.

`applied_to_invoice`

Traces the application of credit against a linked [Invoice](https://docs.stripe.com/invoicing/overview).

`credit_note`

Traces the creation of credit to a [Credit Note](https://docs.stripe.com/invoicing/dashboard/credit-notes) and the associated [Invoice](https://docs.stripe.com/invoicing/overview).

`invoice_too_small`

When the amount due on an invoice is less than our [minimum chargeable amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts) and the customer doesn’t have a cash balance, we debit the invoice to the invoice balance and add it to the amount due of the next issued invoice.

`invoice_too_large`

When the amount due on an invoice is greater than our [maximum chargeable amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts) and the customer doesn’t have a cash balance, we debit the invoice to the invoice balance and add it to the amount due of the next issued invoice.

`unapplied_from_invoice`

Traces the reversal of an applied invoice balance from a linked [Invoice](https://docs.stripe.com/invoicing). Paired with an earlier `applied_to_invoice` transaction.

`unspent_receiver_credit`

When unspent funds in [receiver Sources](https://docs.stripe.com/sources#flow-for-customer-action) attached to a customer without a cash balance aren’t fully charged after 60 days, Stripe automatically charges them on your behalf and credits your balance. When this happens, Stripe also creates a corresponding credit transaction.

`initial`

Represents the starting value of the customer invoice balance when a customer is created using the API with a non-zero invoice balance.

## Modify the invoice balance

You can modify a customer invoice balance in the Dashboard by creating a new [Customer Balance Transaction](https://docs.stripe.com/api/customer_balance_transactions/object) adjustment from the customer details page.

Under **Customer invoice balance**, click **Adjust balance** to display the **Credit balance adjustment** modal.

You can set information about the adjustment, such as:

*   **Adjustment type**: Choose credit or debit
*   **Currency**: Available only if the customer doesn’t have a currency set
*   **Amount**
*   **Internal note**: Visible to Dashboard users, but not to the customer

![How to adjust a customer's subscription balance.](https://b.stripecdn.com/docs-statics-srv/assets/2-Customer-balance.ed7d6df96ba2b8595461e1091e4da7a9.png)

## Invoice balance transaction history

Audit adjustments to a customer invoice balance in the Dashboard on their customer details page, under **Customer invoice balance**.

This section displays the current value of the invoice balance. Click **View details** to see the transaction history used to calculate that value. Each transaction line displays information relevant to the [transaction type](#types), such as a link to the invoice that applied the invoice balance, or the credit note that credited the balance.

![Viewing the invoice balance transaction history](https://b.stripecdn.com/docs-statics-srv/assets/3-Balance-history.446845092bb178c7924a9cbee2538f94.png)

## Customer cash balances

Customers using the [bank transfers](https://docs.stripe.com/payments/bank-transfers) payment method have a [cash balance object](https://docs.stripe.com/api/customers/object#customer_object-cash_balance) with one or more currencies in the `available` object. You can use the funds to [make payments](https://docs.stripe.com/payments/customer-balance#make-cash-payment) or pay invoices.

#### Manage cash balances for customer-configured Accounts

If you use customer-configured [Accounts](https://docs.stripe.com/api/v2/core/accounts/object#v2_account_object-configuration-customer) to represent your customers, you can access an `Account`’s cash balance by passing its ID instead of the `Customer` ID (for example, `v1/customers/acct_xxxxx/balance_transactions`).

Customers with available balances have the following behavior:

*   You can’t create a negative customer cash balance since it represents money sent from the `Customer`.
*   You can’t finalize a too-small or too-large invoice with the cash balance (for example, creating a subscription for 0.01 USD). Learn more about [minimum and maximum amounts](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts).
*   You can delete `Customers` that have a cash balance, but only if their cash balance is 0.
*   You can’t remove a `Customer`’s available balance.
