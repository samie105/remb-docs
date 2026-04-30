---
title: "Import payment method data"
source: "https://docs.stripe.com/get-started/data-migrations/payment-method-imports"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:38:22.449Z"
content_hash: "ad2f1a39540070f24b09278d5b019cd0eac99f70e44056f8a2e4713114370747"
---

When you migrate card data from your previous processor, you can import the data in Stripe as the default payment method card (`pm_`) object or a legacy card (`card_`) object. The Payment Intents API supports all Stripe products for both card payment types, but your integration might favor one based on the following considerations.

*   If you’re using a third-party subscription platform with Stripe, check with the platform or your developer to see if they prefer one or the other.
    
*   If you have existing payment data in your Stripe account, try to match the type you’re already using:
    
    *   `pm_`: Use the [Payment Methods API](https://docs.stripe.com/api/payment-methods) in conjunction with the Payment Intents API.
    *   `card_`: Use the [Card API](https://docs.stripe.com/api/cards) in conjunction with the Payment Intents API.
    *   `src_`: You can still use the deprecated Sources API, but we recommend [migrating to the Payment Intents API](https://docs.stripe.com/payments/payment-intents/migration/charges) for access to more features.

## Default cards

A _default card_ is the primary card a customer sets or chooses for recurring payments, subscriptions, or as the default payment method for future transactions. When you mark a card as `default`, it automatically becomes the payment method for the next transaction unless you specify otherwise. Use this feature for subscription-based services that require automatic recurring payments. You can set a new card as the new default payment method, or add it as an additional payment method without changing the current default.

Type

Object prefix

Migration behavior

Card

`card_`

Sets a default card on import. If unspecified in the data file, the first card imported becomes the default.

Payment Method

`pm_`

Doesn’t require a default card. If unspecified in the data file, no card is the default.

Source

`src_`

Doesn’t require a default card. If unspecified in the data file, no card is the default.

### Provide default card data

*   Include default card information in a separate column of your data file, ideally using `TRUE` and `FALSE` values to identify the default and non-default cards.
*   Marking a card as default during import overrides an existing customer’s current default payment method, if set.

## Current limitations

You can work with your Stripe representative to request Apple Pay DPAN migration to Stripe. Your previous processor must export the device primary account number (DPAN), expiration date, and network transaction ID.

Stripe can’t migrate other cards stored by digital wallets such as Google Pay because those services (not the previous provider) tokenize the stored values for security. You must add any cards associated with digital wallets as new payment methods in Stripe.

## Address validation for Stripe Tax

When you migrate customer data to an account using Stripe Tax, include customer address fields for the following reasons:

*   **Tax calculation accuracy**: Addresses help calculate taxes correctly in different jurisdictions.
*   **Compliance with tax laws**: Local tax laws require addresses for tax invoice accuracy.
*   **Audits and reporting**: Precise address data aids compliance in tax audits and enhances internal analytics by recording transaction locations.
*   **Enhanced customer checkout**: Starting with accurate addresses improves the checkout process for repeat customers by enabling precise, automatic tax calculation.
*   **Adaptability to tax law changes**: A full set of customer address data allows a business to adjust to tax regulation changes, preventing compliance issues.

## Card Account Updater (CAU)

Files from processors often contain expired cards. The Stripe Card Account Updater (CAU) automatically updates stored card information by retrieving and applying new card details from the issuing bank.

CAU maximizes continuity of service and improves authorization rates, but might incur fees for each updated card in your account. You can specify how we handle expired cards during import.

*   **Skip expired cards**: Don’t import expired card data. CAU might still update non-expired cards (such as stolen or replacement cards), triggering post-migration charges.
*   **Import expired cards**: Allow CAU to update as many cards as possible and charge CAU fees to your account.

### How it works

![How card updating on import works](https://b.stripecdn.com/docs-statics-srv/assets/dm-cau.376a7292d021463b18118595e4e20e79.jpg)

## Migrate proof of Strong Customer Authentication (SCA)

For European users, PSD2 (Second Payment Services Directive) mandates [Strong Customer Authentication (SCA)](https://docs.stripe.com/strong-customer-authentication) to enhance electronic payment security. SCA requires two out of three independent authentication factors for transactions:

*   Something the customer knows (such as a password)
*   Something the customer possesses (such as a mobile device)
*   Something the customer is (such as biometric data)

Network transaction IDs from your previous processor show that a customer authenticated a transaction using SCA with the previous processor, enabling Stripe to apply for SCA exemptions for future transactions. This makes your migration to Stripe seamless for your customers, removing their need to re-authenticate.

If your previous provider can’t supply transaction IDs, let us know in your [import request form](https://docs.stripe.com/get-started/data-migrations/pan-import#request-migration) so we can offer alternative options.

## 3DS mandate for Japanese Stripe accounts

Japan’s revised [Credit Card Security Guidelines](https://www.meti.go.jp/press/2022/03/20230315001/20230315001.html) require Japanese businesses to enable 3D Secure 2 (3DS) by the end of March 2025.

If you’re a Japanese business not using 3DS, report this in the **Additional Details** section of the [migration request form](https://docs.stripe.com/get-started/data-migrations/pan-import#request-migration). By default, we interpret this to mean you set the card up to be exempt from the [3DS Mandate in Japan requirement after migration](https://support.stripe.com/questions/3ds-mandate-in-japan).

Stripe adjusts our support and services to help you comply with industry standards without disruption to your operations and security.

Learn more about the [3DS Mandate in Japan](https://support.stripe.com/questions/3ds-mandate-in-japan).

## Card file guidance

*   A processor can provide a number of different fields.
*   We advise your processor to provide a full export of all customer and payment method data to Stripe.
*   Stripe can filter out any unnecessary fields from the previous processor’s data as needed.
*   Stripe can merge multiple received files if either the old customer ID or the old source ID is present in both files.

### File formatting requirements

Export data files must meet the following data standards for us to proceed with an import:

*   The file must be in CSV format.
*   The file must be UTF-8 encoded.
*   Delimit rows by a single newline character `\n` (not `\r\n`).
*   Delimit columns by `,`.
*   You must wrap all fields containing commas in double quotes `"`. We recommend wrapping all fields in double quotes.
*   Leave empty fields entirely empty (no character in between delimiters). You must _not_ denote a missing field with `NULL`, `N/A`, or any other value.
*   Escape any double quotes that are part of the content with another double quote per the CSV RFC. For example, format `William "Bard of Avon" Shakespeare` as `"William ""Bard of Avon"" Shakespeare"`.
*   Fields can’t contain newline characters (`\r` or `\n`) within a field. Example of what to avoid: `101 1st Ave\nApt 1`
*   All rows must have the same number of columns.
*   Columns support any order.
*   You must encrypt sensitive data files with our [PGP key](https://docs.stripe.com/get-started/data-migrations/pan-import#migration-pgp-key) before submitting through SFTP.

## Card data fields

Field

Required

Additional info

Old customer ID

Required

We create a customer ID for each unique old customer ID provided.

Card number

Required

Each customer imported must have at least one Card.

Card expiry

Required

You can provide this option as one or two (separate month and year values) columns.

Network Transaction IDs

Required\*

\*Mandatory for [SCA impacted merchants](https://support.stripe.com/questions/countries-in-the-european-economic-area-\(eea\)-impacted-by-strong-customer-authentication-\(sca\)-regulation).

Address line 1

Required\*

\*Recommended for address validation. Mandatory for Stripe Tax.

City

Required\*

\*Recommended for address validation. Mandatory for Stripe Tax.

State

Required\*

\*Recommended for address validation. Mandatory for Stripe Tax.

Postal

Required\*

\*Recommended for address validation. Mandatory for Stripe Tax.

Country

Required\*

\*Recommended for address validation. Mandatory for Stripe Tax. Format as the ISO 2 letter country code.

Stripe customer ID

Optional

Provide in the processor file or a supplementary file to map to existing Stripe customers.

Old card ID

Optional

Recommended if you have one customer with multiple cards in your old processor.

Description

Optional

Additional metadata

Email

Optional

Additional metadata

Phone

Optional

Additional metadata

Is default

Optional

Indicate `TRUE` or `FALSE` to specify whether the card is the default.

Name

Optional

Additional metadata

Address line 2

Optional

Additional metadata

Customer/Card Metadata

Optional

Any additional metadata
