---
title: "API upgrades"
source: "https://docs.stripe.com/upgrades"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:55:39.241Z"
content_hash: "d6ba4da299f12c31f7bddd488669f94006a77130df6b5ae06f799877ade1b085"
---

#### Private preview

[Thin events](https://docs.stripe.com/event-destinations#thin-events) for API v1 resources are available in private preview. You can use them to streamline integration upgrades without changing your webhook configuration. Previously, thin events only supported API v2 resources. [Learn more and request access](https://docs.google.com/forms/d/e/1FAIpQLSeEkqzB02afvlklMkqwA6wsBH90eW8gxmc-hBOvqe2N6TRujQ/viewform?usp=dialog).

Your API version controls the API and webhook behavior you see (for example, what parameters you can include in requests, what properties you see in responses, and so on). Your version gets set the first time you make an API request. Each major release, such as [Acacia](https://docs.stripe.com/changelog/acacia), includes changes that aren’t backward-compatible with previous releases. Upgrading to a new major release can require updates to existing code. Each monthly release includes only backward-compatible changes, and uses the same name as the last major release. You can safely upgrade to a new monthly release without breaking any existing code. To upgrade your API version, follow [these steps](#how-can-i-upgrade-my-api).

When a [Connect](https://stripe.com/connect) platform makes requests on behalf of connected accounts without specifying an API version, Stripe always uses the platform’s API version. Regardless of a connected account’s API version, the platform’s requests on its behalf always return responses matching the API version of the request.

## Backward-compatible changes

Stripe considers the following changes to be backward-compatible:

*   Adding new API resources.
*   Adding new optional request parameters to existing API methods.
*   Adding new properties to existing API responses.
*   Changing the order of properties in existing API responses.
*   Changing the length or format of opaque strings, such as object IDs, error messages, and other human-readable strings.
    *   This includes adding or removing fixed prefixes (such as `ch_` on charge IDs).
    *   Make sure that your integration can handle Stripe-generated object IDs, which can contain up to 255 characters. For example, if you’re using MySQL, store the IDs in a `VARCHAR(255) COLLATE utf8_bin` column (the `COLLATE` configuration provides case-sensitivity during lookups).
*   Adding new event types.
    *   Make sure that your webhook listener gracefully handles unfamiliar event types.

## Upgrade your API version

If you’re running an older version of the API, upgrade to the latest version to take advantage of new features and enhanced functionality.

Upgrading your API version affects:

*   The API calls you make without a `Stripe-Version` header: the parameters you can send and the structure of objects returned.
*   The structure of objects received with [Stripe.js](https://docs.stripe.com/payments/elements) methods such as [confirmCardPayment](https://docs.stripe.com/js#stripe-confirm-card-payment).
*   The structure of objects sent to your webhook endpoints (both Account and [Connect](https://docs.stripe.com/connect/webhooks)). However, if an endpoint has an explicit version set, it always uses that version.
*   Automated Billing operations performed by Stripe (for example, generating an [invoice](https://docs.stripe.com/api/invoices) for a new subscription period) use your account’s default API version. See the API changelog for details about how your default API version impacts these operations.

### View your API version and the latest available upgrade in Workbench

See the [API version used by recent requests](https://docs.stripe.com/workbench/guides#view-api-versions) on your account and the latest available upgrade from the [Overview](https://dashboard.stripe.com/workbench/overview) tab in Workbench.

When performing an API upgrade, make sure that you specify the API version that you’re integrating against in your code instead of relying on your account’s default API version. To test a newer version for API calls, set the `Stripe-Version` header (in live or testing environments). Learn how to manage versioning in our [server-side SDKs](https://docs.stripe.com/sdks#server-side-libraries).

### Upgrade and test your webhooks

Read our guide on [how to handle webhook versioning](https://docs.stripe.com/webhooks/versioning).

### Perform the upgrade

When you’re confident that your code can handle the latest API version, perform the upgrade using Workbench:

1.  Open the [Overview](https://dashboard.stripe.com/workbench/overview) tab in Workbench.
2.  In the **API versions** section, click **Upgrade available**, which is visible if a newer API version is available.
3.  Review which API version will be assigned to your account, and click **Upgrade.**

This switches the version used by API calls that don’t have the `Stripe-Version` header and also switches the version used to render objects sent to your webhooks.

#### Caution

The shape of resources inside [events retrieved from the API](https://docs.stripe.com/api/events) is defined by the default API version of your account at the time the event occurred. If your code retrieves events created when your default API version was different, it must account for any differences in the event versions.

### Roll back your API version

For 72 hours after you’ve upgraded your API version, you can safely roll back to the version you were upgrading from in Workbench.

After you’ve rolled back, webhooks that were sent with the new object structure and failed will be retried with the old structure.

## Stay informed

We send information on new additions and changes to the Stripe API and language libraries in the Stripe Developer Digest. Make sure you [subscribe](https://go.stripe.global/dev-digest) to stay informed about additions and changes.

## API versions

#### Caution

This section is no longer being updated. To learn about updates to the Stripe API, visit the new [Changelog](https://docs.stripe.com/changelog).

Listed below are all the [breaking changes](#breaking-change) to the Stripe API. Each date corresponds with a new version of the Stripe API. If you’re looking for all API additions and updates, see the [API changelog](https://docs.stripe.com/changelog). If you’re looking for new product releases, see the [product changelog](https://stripe.com/blog/changelog).

### 2024-06-20

*   New values have been added to the [Issuing Authorization](https://docs.stripe.com/api/issuing/authorizations/object) `request_history.reason` enum:
    
    *   `card_canceled`
    *   `card_expired`
    *   `cardholder_blocked`
    *   `insecure_authorization_method`
    *   `pin_blocked`
    
*   On the [Issuing Authorization](https://docs.stripe.com/api/issuing/authorizations/object) resource and related `test_helper` APIs, `fuel.volume_decimal` has been renamed to `fuel.quantity_decimal`.
    
*   On the [Issuing Transaction](https://docs.stripe.com/api/issuing/transactions/object) resource and related `test_helper` APIs, `purchase_details.fuel.volume_decimal` has been renamed to `purchase_details.fuel.quantity_decimal`.
    
*   The following undocumented fuel fields have been removed from the [Issuing Transaction](https://docs.stripe.com/api/issuing/transactions/object) resource in favor of the `_decimal` equivalents:
    
    *   `purchase_details.fuel.unit_cost`
    *   `purchase_details.fuel.volume`
    
*   The following undocumented fleet fields have been removed from the [Issuing Transaction](https://docs.stripe.com/api/issuing/transactions/object) resource in favor of their corresponding `_decimal` equivalents:
    
    *   `purchase_details.fleet.reported_breakdown.fuel.gross_amount`
    *   `purchase_details.fleet.reported_breakdown.non_fuel.gross_amount`
    *   `purchase_details.fleet.reported_breakdown.tax.local_amount`
    *   `purchase_details.fleet.reported_breakdown.tax.national_amount`
    
*   New values have been added to the [Issuing Transaction](https://docs.stripe.com/api/issuing/transactions/object) `purchase_details.fuel.unit` enum:
    
    *   `imperial_gallon`
    *   `kilogram`
    *   `pound`
    *   `charging_minute`
    *   `kilowatt_hour`
    
*   The `fleet.cardholder_prompt_data.alphanumeric_id` property on the [Issuing Authorization](https://docs.stripe.com/api/issuing/authorizations/object) resource has been deprecated and will be removed in a future API version. Depending on the configuration of your card program, use `driver_id`, `vehicle_number`, `unspecified_id` or `user_id` instead.
    
*   In the Capabilities API, `paused.inactivity` and `other` have been added as new disabled reasons. See [Capability disabled reasons](https://docs.stripe.com/api/accounts/object#capability_object-requirements-disabled_reason) for more information.
    
*   In the Capabilities API, `bank_transfer_payments` capability type is being deprecated in favor of newer capability types per buyer’s location. The newer capability types are:
    
    *   `gb_bank_transfer_payments` for UK Bank Transfers (GBP customer balance payments)
    *   `jp_bank_transfer_payments` for JP Bank Transfers (JPY customer balance payments)
    *   `mx_bank_transfer_payments` for MX Bank Transfers (MXN customer balance payments)
    *   `sepa_bank_transfer_payments` for SEPA Bank Transfers (EUR customer balance payments)
    *   `us_bank_transfer_payments` for US Bank Transfers (USD customer balance payments)
    

### 2024-04-10

*   [PaymentIntents](https://docs.stripe.com/api/payment_intents) now has `automatic_async` as the default capture method when capture method is not specified during PaymentIntents creation. For more information about async capture, view the [asynchronous capture guide](https://docs.stripe.com/payments/payment-intents/asynchronous-capture).
    
*   Fields under `rendering_options` for invoices are now migrated under `rendering`.
    
*   Product ‘features’ has been renamed to `marketing_features`.
    

### 2023-10-16

*   In the Accounts API, the following error codes have been added as new error codes in the `requirements.errors` array. See [Account requirements errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors) for more information.
    
    *   `invalid_address_highway_contract_box`
    *   `invalid_address_private_mailbox`
    *   `invalid_business_profile_name`
    *   `invalid_business_profile_name_denylisted`
    *   `invalid_company_name_denylisted`
    *   `invalid_dob_age_over_maximum`
    *   `invalid_dob_age_under_minimum`
    *   `invalid_product_description_length`
    *   `invalid_product_description_url_match`
    *   `invalid_statement_descriptor_business_mismatch`
    *   `invalid_statement_descriptor_denylisted`
    *   `invalid_statement_descriptor_length`
    *   `invalid_statement_descriptor_prefix_denylisted`
    *   `invalid_statement_descriptor_prefix_mismatch`
    *   `invalid_tax_id_format`
    *   `invalid_url_denylisted`
    *   `invalid_url_format`
    *   `invalid_url_web_presence_detected`
    *   `invalid_url_website_business_information_mismatch`
    *   `invalid_url_website_empty`
    *   `invalid_url_website_inaccessible`
    *   `invalid_url_website_inaccessible_geoblocked`
    *   `invalid_url_website_inaccessible_password_protected`
    *   `invalid_url_website_incomplete`
    *   `invalid_url_website_incomplete_cancellation_policy`
    *   `invalid_url_website_incomplete_customer_service_details`
    *   `invalid_url_website_incomplete_legal_restrictions`
    *   `invalid_url_website_incomplete_refund_policy`
    *   `invalid_url_website_incomplete_return_policy`
    *   `invalid_url_website_incomplete_terms_and_conditions`
    *   `invalid_url_website_incomplete_under_construction`
    *   `invalid_url_website_other`
    
*   In the Accounts API, if no `settings.payments.statement_descriptor` is supplied, the statement descriptor is automatically set to the first supplied parameter of (in priority order):
    
    *   `business_profile.name`
    *   `business_profile.url`
    *   `company.name` or `individual.first_name` + `individual.last_name` (dependent on the `business_type`)
    
    The statement descriptor is only set automatically when one of the above fields is provided as a parameter, so existing accounts will not be impacted unless a dependent field is updated. Similarly, `settings.card_payments.statement_descriptor_prefix` will be defaulted to a shortened version of the `settings.payments.statement_descriptor`. This will take place whenever the statement descriptor is updated (either explicitly, or when defaulted).
    

### 2023-08-16

*   Major
    
    [PaymentIntents](https://docs.stripe.com/api/payment_intents) and [SetupIntents](https://docs.stripe.com/api/setup_intents) now have `automatic_payment_methods` enabled by default, which allows you to configure payment method settings from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods)—no code required. The previous default was to accept only card payments when both `payment_method_types` and `automatic_payment_methods` were not specified. For more information, view the [upgrade guide](https://docs.stripe.com/upgrades/manage-payment-methods).
    
    *   When confirming a PaymentIntent, you will be required to provide a `return_url` unless `off_session=true`.
    *   When confirming a PaymentIntent, you cannot use `error_on_requires_action`. Use `payment_method_types` with `error_on_requires_action` if you wish to fail payment attempts when PaymentIntents transition into `requires_action`.
    *   When confirming a SetupIntent, you will be required to provide a `return_url`.
    *   You can bypass the `return_url` requirement using `automatic_payment_methods[allow_redirects]=never`, this will automatically filter payment methods that [require redirect](https://docs.stripe.com/payments/payment-methods/integration-options#additional-api-supportability) even if they are enabled in the Dashboard.
    
*   [No-cost orders](https://docs.stripe.com/payments/checkout/no-cost-orders) are now enabled for one-time payments in Checkout Sessions. The value of `payment_method_collection` has changed from `always` to `if_required` accordingly.
    
*   When being viewed by a platform, PaymentMethod fingerprints of types `us_bank_account`, `acss_debit`, `sepa_debit`, `bacs_debit`, and `au_becs_debit` are rendered in platform scope, not the owning merchant (connected account) scope. This works similarly to the [2018-01-23](#2018-01-23) change for cards and bank accounts.
    
*   Added more specific error codes to the [PaymentIntent](https://docs.stripe.com/api/payment_intents) API for when a [Klarna](https://docs.stripe.com/payments/klarna) payment fails:
    
    *   `payment_method_customer_decline`
    *   `payment_method_not_available`
    *   `payment_method_provider_decline`
    *   `payment_intent_payment_attempt_expired`
    
*   In the Accounts API, `verification_missing_directors`, `verification_directors_mismatch`, `verification_document_directors_mismatch` and `verification_extraneous_directors` has been added as a new error code in the `requirements.errors` array. See [Account requirements errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors) for more information.
    

### 2022-11-15

*   [Charge](https://docs.stripe.com/api/charges/object) no longer auto-expands refunds by default. You can [expand the list](https://docs.stripe.com/api#expanding_objects) but for performance reasons we recommended against doing so unless needed.
    
*   The `charges` property on [PaymentIntent](https://docs.stripe.com/api/payment_intents/object) has been removed. You can use the `latest_charge` property instead.
    
*   Added more specific error codes for the following bank redirect payment methods: Bancontact, EPS, Giropay, iDEAL, Przelewy24, and Sofort.
    
    *   Added the following error codes to the [PaymentIntent](https://docs.stripe.com/api/payment_intents) and [PaymentMethod](https://docs.stripe.com/api/payment_methods) APIs:
        
        *   `payment_intent_payment_attempt_expired`
        *   `payment_method_customer_decline`
        *   `payment_method_provider_timeout`
        *   `payment_method_not_available`
        *   `payment_method_provider_decline`
    *   Added the following error codes to the [SetupIntent](https://docs.stripe.com/api/setup_intents) APIs:
        
        *   `setup_intent_setup_attempt_expired`
        *   `payment_method_customer_decline`
        *   `payment_method_provider_timeout`
        *   `payment_method_not_available`
        *   `payment_method_provider_decline`
    
*   In the Accounts API, `verification_legal_entity_structure_mismatch` has been added as a new error code in the `requirements.errors` array. See [Account requirements errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors) for more information.
    

### 2022-08-01

*   The `pending_invoice_items_behavior` parameter on [create Invoice](https://docs.stripe.com/api/invoices/create) no longer supports the `include_and_require` value. When the parameter is omitted the default value of `pending_invoice_items_behavior` is now `exclude`.
    
*   When creating a Checkout Session in payment mode, the default value of `customer_creation` has changed from `always` to `if_required`.
    
*   A PaymentIntent is no longer created during Checkout Session creation in payment mode. Instead, a PaymentIntent will be created when the Session is confirmed.
    
*   Checkout Sessions no longer return the `setup_intent` property in subscription mode.
    
*   The following parameters have been removed from [create Checkout Session](https://docs.stripe.com/api/checkout/sessions/create):
    
    *   `line_items[amount]`
    *   `line_items[currency]`
    *   `line_items[name]`
    *   `line_items[description]`
    *   `line_items[images]`
    
    You can use the `price` and `price_data` parameters instead.
    
*   The `subscription_data[coupon]` parameter has been removed from [create Checkout Session](https://docs.stripe.com/api/checkout/sessions/create). You can use the `discounts` parameter instead.
    
*   The `shipping_rates` parameter has been removed from [create Checkout Session](https://docs.stripe.com/api/checkout/sessions/create). You can use the `shipping_options` parameter instead.
    
*   On the Checkout Session resource, several shipping properties have changed.
    
    *   `shipping_rate` has been moved into the new `shipping_cost` hash.
    *   `shipping` has been renamed to `shipping_details`.
    
*   `exempted` now appears in the `three_d_secure` hash for card Charges. It indicates that a 3D Secure exemption was granted.
    
*   In the Accounts API, `invalid_tos_acceptance` has been added as a new error code in the `requirements.errors` array. See [Account requirements errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors) for more information.
    
*   When creating a `physical` Issuing card in testmode, its shipping [status](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-status) no longer automatically changes from `pending` to `delivered`. This functionality is now accessible via the following new endpoints:
    
    *   `/v1/test_helpers/issuing/cards/:card/shipping/ship`
    *   `/v1/test_helpers/issuing/cards/:card/shipping/deliver`
    *   `/v1/test_helpers/issuing/cards/:card/shipping/return`
    *   `/v1/test_helpers/issuing/cards/:card/shipping/fail`
    
*   `design_rejected` is now a possible value for the `cancellation_reason` field on the issued card object, indicating that the card’s design was rejected by Stripe.
    
*   The `default_currency` field on the Customer API resource has been removed.
    

### 2020-08-27

*   We have removed `tax_percent` from objects and requests in favor of [tax rates](https://docs.stripe.com/api/tax_rates).
    

*   On subscription schedules, `phases.plans` has been renamed to `phases.items`. This applies for the [subscription schedule](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases) object as well as [create](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases) and [update](https://docs.stripe.com/api/subscription_schedules/update#update_subscription_schedule-phases) requests.
    
*   Deprecate the `payment_method.card_automatically_updated` webhook in favor of `payment_method.automatically_updated`.
    
*   Checkout Sessions no longer include the `display_items` property. Use the includable `line_items` property instead.
    
*   The `requirements` hash on the Account and Capability objects, and the `verification_fields` hash on the Country Spec object have newly formatted strings for requirements that are related to key persons associated with an account:
    
    *   Fields that are required for persons with `representative`, `owner`, `director`, and `executive` roles will be prefixed with `representative`, `owners`, `directors`, and `executives`, respectively. Person requirements will be previewed as follows:
        *   When the representative’s phone number is required, it will appear as `representative.phone` instead of `relationship.representative`.
        *   When an owner’s full name is required, it will appear as `owners.first_name` and `owners.last_name` instead of `relationship.owner`.
        *   When an executive’s ID number is required, it will appear as `executives.id_number` instead of `relationship.executive`.
        *   When a director’s date of birth is required, it will appear as `directors.dob.day`, `directors.dob.month`, and `directors.dob.year` instead of `relationship.director`.
    *   The boolean values that indicate the associated owners, executives, or directors have been provided now appear as `company.owners_provided`, `company.executives_provided`, or `company.directors_provided` instead of `relationship.owner`, `relationship.executive`, or `relationship.director`, respectively.
    
*   In the Accounts/Persons/Capabilities API, several new error codes have been introduced in the `requirements.errors` array. See [Account requirements errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors) for more information. These error codes are:
    
    *   `verification_document_issue_or_expiry_date_missing`
    *   `verification_document_not_signed`
    *   `verification_failed_tax_id_not_issued`
    *   `verification_failed_tax_id_match`
    *   `invalid_address_po_boxes_disallowed`
    
*   The `payment_method_details.card.three_d_secure` fields on the Charge object have been updated. The `succeeded` and `authenticated` booleans have been removed; please use the `result` enum instead.
    
*   The `subscriptions` property on Customers is no longer included by default. You can [expand the list](https://stripe.com/docs/api#expanding_objects) but for performance reasons we recommended against doing so unless needed.
    
*   The `tiers` property on Plan is no longer included by default. You can [expand the list](https://stripe.com/docs/api#expanding_objects) but for performance reasons we recommended against doing so unless needed.
    
*   The `sources` property on Customers is no longer included by default. You can [expand the list](https://stripe.com/docs/api#expanding_objects) but for performance reasons we recommended against doing so unless needed.
    
*   The `tax_ids` property on Customers is no longer included by default. You can [expand the list](https://stripe.com/docs/api#expanding_objects) but for performance reasons we recommended against doing so unless needed.
    
*   The `prorate` and `subscription_prorate` parameters are deprecated in favor of `proration_behavior`.
    

### 2020-03-02

*   Major
    
    You can now optionally number invoices [sequentially across your account](https://stripe.com/docs/billing/invoices/customizing#invoice-prefix-number) instead of sequentially for each customer. To use this feature, enable [account level numbering](https://dashboard.stripe.com/settings/billing/invoice) in the Stripe Dashboard.
    
    *   To ensure invoices are numbered sequentially and without gaps, invoices that can be deleted (drafts) are only assigned numbers when finalized.
    

### 2019-12-03

*   Major
    
    The [`id`](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-id) field of all invoice line items have changed and are now prefixed with `il_`. The new id has consistent prefixes across all line items, is globally unique, and can be used for pagination. Old prefixes included `sub_`, `su_`, `item_`, `sli_`, and `ii_` and weren’t globally unique.
    
    *   You can no longer use the prefix of the id to determine the source of the line item. Instead use the `type` field for this purpose.
    *   For lines with `type=invoiceitem`, use the `invoice_item` field to reference or update the originating Invoice Item object.
    *   The Invoice Line Item object on earlier API versions also have a `unique_id` field to be used for migrating internal references before upgrading to this version.
    *   When [setting a tax rate to individual line items](https://docs.stripe.com/billing/invoices/tax-rates#setting-tax-rates-on-individual-items), use the new `id`. Users on earlier API versions can pass in either a line item `id` or `unique_id`.
    
*   When [creating](https://docs.stripe.com/api/credit_notes/create) a post-payment credit note on an invoice:
    
    *   [`out_of_band_amount`](https://docs.stripe.com/api/credit_notes/create#create_credit_note-out_of_band_amount) is required if the sum of `credit_amount` and (`refund` or `refund_amount`) is less than the credit note total.
    *   In previous API versions `out_of_band_amount` is optional and, in the case that the `credit_amount` and refund amounts are less than the credit note total, the difference will automatically be allocated to the `out_of_band_amount`.
    
*   Customer balances applied to all invoices are now debited or credited back to the customer when voided. Earlier, applied customer balances were not returned back to the customer and were consumed.
    
    *   To achieve this behavior in earlier API versions:
        *   Set `consume_applied_balance` to `false` when voiding invoices in [`/v1/invoices/:id/void`](https://docs.stripe.com/api/invoices/void).
        *   Set `invoice_customer_balance_settings[consume_applied_balance_on_void]` to `false` in `/v1/subscriptions` [create](https://docs.stripe.com/api/subscriptions/create) or [update](https://docs.stripe.com/api/subscriptions/update) to force this behavior for Invoices voided by a Subscription.
        *   Set `subscription_data[invoice_customer_balance_settings][consume_applied_balance_on_void]` to `false` in `/v1/checkout/sessions` [create](https://docs.stripe.com/api/checkout/sessions/create) to force this behavior for Invoices voided by Subscriptions created with Checkout.
    
*   Deprecated tax information for Customers have been removed.
    
    *   The deprecated `tax_info` and `tax_info_verification` fields on the `Customer` object are now removed in favor of `tax_ids`.
    *   The deprecated `tax_info` parameter on the `Customer` create and update methods are removed in favor of `tax_id_data`.
    *   For more information, view the [migration guide](https://docs.stripe.com/billing/taxes/tax-rates#migration).
    

### 2019-11-05

*   In the Accounts API, the `requested_capabilities` property is now required at creation time for Custom accounts in all countries. See [Account capabilities](https://docs.stripe.com/connect/account-capabilities) for more information.
    
*   On subscription schedules, `invoice_settings`, `default_payment_method`, `billing_thresholds` and `collection_method` are now nested under `default_settings`.
    

### 2019-10-17

*   There are changes to subscription schedules.
    
    *   Rename `renewal_behavior` to `end_behavior` with values `cancel` and `release`.
    *   Remove `renewal_interval`.
    *   A side effect of this change is that if you wrote a `renewal_behavior` of `none` on an old API version, `end_behavior` will be converted to `cancel` when reading the value back.
    *   In the event that you are upgrading your API and set `renewal_behavior` as `renew`, with this API version enabled you will see `end_behavior` as `renew` however you will not be able to update `renewal_interval`. Additionally you can not set `end_behavior` to `renew`, so it is in a read-only state.
    
*   The `start` field on a subscription resource has been removed and is replaced by a `start_date` field which represents when the entire subscription started as opposed to when the current plan configuration started.
    
*   The `due_date` property is always null on invoices with `billing=charge_automatically`.
    
*   The `billing` attribute on invoices, subscriptions, and subscription schedules is renamed to `collection_method`.
    
*   The [customer object](https://stripe.com/docs/api/customers)’s `account_balance` value has been renamed to `balance`. A new [customer balance transactions API](https://stripe.com/docs/api/customer_balance_transactions) is available:
    
    *   Update the customer’s `balance` by incrementing or decrementing its current value by a specified `amount` and attaching `metadata` to the change.
    *   Retrieve history of changes to the customer’s `balance`.
    

### 2019-10-08

*   The `relationship[account_opener]` field on a Person object has been renamed to `relationship[representative]`.
    

### 2019-09-09

*   In the Accounts API, the `requested_capabilities` property is now required at creation time for accounts in Australia, Austria, Belgium, Denmark, Finland, France, Germany, Ireland, Italy, Luxembourg, the Netherlands, New Zealand, Norway, Portugal, Spain, Sweden, Switzerland, and the United Kingdom. See [Account capabilities](https://docs.stripe.com/connect/account-capabilities) for more information.
    
*   Adds additional `details_code` values to the `verification[document]` hash on a Person object.
    

### 2019-08-14

*   Major
    
    The `platform_payments` capability has been renamed to `transfers`, to better indicate the Stripe primitives that this capability supports.
    
    *   The `card_payments` capability has been updated to no longer imply `transfers`. You’ll now need to additionally request the `transfers` capability when creating an account.
    
*   The `relationship[executive]` field on a Person object will no longer be automatically set to `true` when a Person object with `relationship[account_opener]` is created. The `requirements` hash on an Account object may require that you explicitly indicate that the `account_opener` is also an `executive`. If this is the case, you will need to indicate it by setting `relationship[executive]=true`.
    

### 2019-05-16

*   Bank pull payments no longer expose internal system refunds on failure.
    
    System refunds can still be accessed via the [list refunds](https://stripe.com/docs/api/refunds/list#list_refunds-charge) endpoint.
    

### 2019-03-14

*   The `application_fee` parameter on invoice API methods and the `application_fee` field on the invoice object have both been renamed to `application_fee_amount`.
    
*   Major
    
    Creating a subscription succeeds even when the first payment fails. The subscription will be created in an incomplete status, where it will remain for up to 23 hours. During that time period, it can be moved into an active state by paying the first invoice. If no successful payment is made, the subscription will move into a final incomplete\_expired state. Updates to a non-incomplete subscription that require a payment will also succeed regardless of the payment status. Prior to this version, all creations or updates would fail if the corresponding payment failed. For more details see [our guide](https://stripe.com/docs/billing/subscriptions/overview#subscription-lifecycle).
    
*   There are a few changes to the [invoice object](https://stripe.com/docs/api/invoices):
    
    *   A `status_transitions` hash now contains the timestamps when an invoice was finalized, paid, marked uncollectible, or voided.
    *   The `date` property has been renamed to `created`.
    *   The `finalized_at` property has been moved into the `status_transitions` hash.
    

### 2019-02-19

*   Major
    
    Statement descriptor behaviors for card payments [created via `/v1/charges`](https://docs.stripe.com/api/charges/create) have changed. See [our statement descriptor guide](https://docs.stripe.com/payments/charges-api#dynamic-statement-descriptor) for details.
    
    *   Instead of using the platform’s statement descriptor, charges created with `on_behalf_of` or `destination` will now use the descriptor of the connected account.
    *   The full statement descriptor for a card payment may no longer be provided at charge creation. Dynamic descriptors provided at charge time will now be prefixed by the descriptor prefix set in the dashboard or via the new `settings[card_payments][statement_descriptor_prefix]` parameter in the Accounts API.
    *   If an account has no `statement_descriptor` set, the account’s business or legal name will be used as statement descriptor.
    *   Statement descriptors may no longer contain `*`, `'`, and `"`.
    

*   `legal_entity[business_id_number]` has been renamed `legal_entity[business_registration_number]`.
    

*   Major
    
    Many properties on the Account API object have been reworked. To see a mapping of the old argument names to the new ones, see [Accounts API Argument Changes](https://docs.stripe.com/connect/updated-requirements/accounts-arguments).
    
    *   The `legal_entity` property on the Account API resource has been replaced with `individual`, `company`, and `business_type`.
    *   The `verification` hash has been replaced with a `requirements` hash.
        *   The `verification[fields_needed]` array has been replaced with three arrays to better represent when info is required: `requirements[eventually_due]`, `requirements[currently_due]`, and `requirements[past_due]`.
        *   `verification[due_by]` has been renamed to `requirements[current_deadline]`.
        *   The `disabled_reason` enum value of `fields_needed` has been renamed to `requirements.past_due`.
    *   Properties on the Account API object that configure behavior within Stripe have been moved into the new `settings` hash.
        *   The `payout_schedule`, `payout_statement_descriptor` and `debit_negative_balances` fields have been moved to `settings[payouts]` and renamed to `schedule`, `statement_descriptor` and `debit_negative_balances`.
        *   The `statement_descriptor` field has been moved to `settings[payments][statement_descriptor]`.
        *   The `decline_charge_on` fields have been moved to `settings[card_payments]` and renamed to `decline_on`.
        *   The `business_logo`, `business_logo_large` and `business_primary_color` fields have been moved to `settings[branding]` and renamed to `icon`, `logo` and `primary_color`. The `icon` field additionally requires the uploaded image file to be square.
        *   The `display_name` and `timezone` fields have been moved to `settings[dashboard]`.
    *   `business_name`, `business_url`, `product_description`, `support_address`, `support_email`, `support_phone` and `support_url` have been moved to the `business_profile` subhash.
    *   The `legal_entity[verification][document]` property (now located at `individual[verification]` and at `verification` in the Person API object) has been changed to a hash.
        *   The `front` and `back` fields support uploading both sides of documents.
        *   The `details_code` field has new error types: `document_corrupt`, `document_failed_copy`, `document_failed_greyscale`, `document_failed_other`, `document_failed_test_mode`, `document_fraudulent`, `document_id_country_not_supported`, `document_id_type_not_supported`, `document_invalid`, `document_manipulated`, `document_missing_back`, `document_missing_front`, `document_not_readable`, `document_not_uploaded`, `document_photo_mismatch`, and `document_too_large`.
    *   The `keys` property on Account creation has been removed. Platforms should now authenticate as their connected accounts with their own key via [the `Stripe-Account` header](https://stripe.com/docs/connect/authentication#stripe-account-header).
    *   Starting with the 2019-02-19 API, the `requested_capabilities` property is now required at creation time for accounts in the U.S. See [Account capabilities](https://docs.stripe.com/connect/account-capabilities) for more information.
    

### 2019-02-11

*   Some PaymentIntent statuses have been renamed
    
    *   `requires_source` is now `requires_payment_method`
    *   `requires_source_action` is now `requires_action`
    *   All other statuses are unchanged
    
*   `save_source_to_customer` has been renamed to `save_payment_method`.
    
*   `allowed_source_types` has been renamed to `payment_method_types`.
    
*   The `next_source_action` property on PaymentIntent has been renamed to `next_action`, and the `authorize_with_url` within has been renamed to `redirect_to_url`.
    

### 2018-11-08

*   The `closed` property on the [invoice object](https://stripe.com/docs/api/invoices) controls [automatic collection](https://docs.stripe.com/billing/invoices/workflow#auto_advance). `closed` has been deprecated in favor of the more specific `auto_advance` field. Where you might have set `closed=true` on invoices in the past, set `auto_advance=false`.
    
*   `auto_advance` now also defaults to false for one-off invoices, allowing you to control how long their [status](https://stripe.com/docs/billing/migration/invoice-states#status) stays a `draft`. A longer explanation of these series of changes is [in the documentation](https://stripe.com/docs/billing/migration/invoice-states#autoadvance).
    
*   Instead of checking the `forgiven` field on an invoice, check for the `uncollectible` status.
    
    *   Instead of setting the `forgiven` field on an invoice, [mark it as uncollectible.](https://docs.stripe.com/api/invoices/mark_uncollectible)
    
*   The `immutable_frozen_invoice` error code was renamed to `invoice_already_finalized`
    
*   The following changes only affect users of PaymentIntents as part of the private beta before November 15, 2018. If you did not use PaymentIntents before then, these don’t affect you.
    
    *   The `next_source_action` dictionary on PaymentIntents previously contained a key called `value`. This has been replaced with the `authorize_with_url` and `use_stripe_sdk` keys.
    *   When creating PaymentIntents, the `attempt_confirmation` parameter has been renamed to `confirm`.
    *   The PaymentIntent confirm endpoint no longer supports the `payment_intent` parameter. To update a PaymentIntent’s source, pass `source` or `source_data` as a top-level parameter.
    *   The `return_url` parameter is only allowed when confirming a PaymentIntent. Passing `return_url` when updating a PaymentIntent is no longer allowed.
    *   When creating a PaymentIntent with `transfer_data[destination]`, the `on_behalf_of` parameter must be provided and must match the account provided to `transfer_data[destination]`. This is because when you provide a destination, Stripe will [settle charges in the country of the destination account](https://stripe.com/docs/connect/separate-charges-and-transfers#settlement-merchant).
    *   The `next_source_action` dictionary on PaymentIntents no longer contains the `source_type` property. To view the source type when retrieving PaymentIntents, [expand](https://stripe.com/docs/api/expanding_objects) the `source` parameter.
    

### 2018-10-31

*   The `description` field on customer endpoints has a maximum character length limit of `350` now. The `name` field on product endpoints has a maximum character length limit of `250` now. The `description` field on invoice line items has a maximum character length limit of `500` now.
    
*   The `billing_reason` attribute of the invoice object now can take the value of `subscription_create`, indicating that it is the first invoice of a subscription. For older API versions, `billing_reason=subscription_create` is represented as `subscription_update`.
    

### 2018-09-24

*   `FileUpload` objects have been renamed to `File` objects. Additionally, the `url` attribute now contains an authenticated URL (i.e. you will need to use your secret API key to download the file’s contents.) You can [create a file link](https://docs.stripe.com/api#create_file_link) to obtain a publicly-accessible URL for the file.
    

### 2018-09-06

*   When creating or updating a SKU, its attribute values no longer need to be unique. It is now possible to create multiple SKUs without attributes or with identical attribute values.
    

### 2018-08-23

*   You can no longer set `at_period_end` in the subscription `DELETE` endpoints. The `DELETE` endpoint is reserved for immediate canceling going forward. Use `cancel_at_period_end` on the subscription update endpoints instead.
    
*   The [customer object](https://stripe.com/docs/api/customers)’s `business_vat_id` was changed from String to Hash called `tax_info`, consisting of `tax_id` and `type`, in both requests and responses.
    
*   The `amount` field field in the `tiers` configuration for `plans` was renamed to `unit_amount`.
    

### 2018-07-27

*   The subscription endpoints no longer support the `source` parameter. If you want to change the default source for a customer, instead use the [source creation API](https://stripe.com/docs/api#create_source) to add the new source and then the [customer update API](https://stripe.com/docs/api#update_customer) to set it as the default.
    
*   When ending a trial on a subscription using `trial_end=now` the updated subscription will now receive a `trial_end` timestamp from the time of the request rather than being unset.
    
*   The `percent_off` field of coupons was changed from Integer to Float, with a precision of two decimal places.
    
*   When creating or updating a customer the `email` parameter must contain an email address of valid shape.
    

### 2018-05-21

*   Products no longer have SKU lists embedded.
    
*   Major
    
    The `id` field of invoice line items of `type=subscription` no longer can be interpreted as a subscription ID, but instead is a unique invoice line item ID. It can be used for pagination.
    
*   Coupon, SKU, customer, product and plan `id`s may only contain alphanumeric and `_-` characters on creation.
    
*   Major
    
    When creating or updating subscriptions, the default value of `trial_from_plan` is now `false`, meaning that a subscription will not automatically inherit a plan’s `trial_period_days`. If a subscription is already trialing, switching to a new plan without specifying `trial_from_plan` will maintain the trial. We recommend setting an explicit trial per subscription instead of setting trials on plans.
    
*   When changing the plan on a subscription to a new plan with a trial (together with `trial_from_plan=true`), the new plan’s full trial period will be added to the subscription, without subtracting already-used time from previous trials.
    

### 2018-02-28

*   Updating a subscription set to cancel on a future date no longer clears the cancellation status. In order to clear the cancellation status, specify [`cancel_at_period_end=false`](https://docs.stripe.com/api#update_subscription-cancel_at_period_end) when updating a subscription.
    

### 2018-02-06

*   For a Source’s `card[three_d_secure]` property, adds `recommended` as a possible value. Previously, the only valid values were `not supported`, `optional`, and `required`.
    

### 2018-02-05

*   Major
    
    Each plan object is now linked to a product object with `type=service`. The plan object `statement_descriptor` and `name` attributes have been [moved to product](https://docs.stripe.com/api#product_object-statement_descriptor) objects, and plan objects now have a `nickname` attribute. Creating a plan now requires passing a [`product` attribute](https://docs.stripe.com/api#create_plan-product) to `POST /v1/plans`. This may be either an existing product ID or a dictionary of product fields, so that you may continue to create plans without separately creating products.
    
*   Products now have a required `type`: `good` for products used with Orders SKUs, or `service` for products used with Subscriptions and Plans.
    
    *   On API versions older than 2018-02-05, `type` is set to `good` by default, and `GET /v1/products` omits products with `type=service` from the list. (If you want to see products with `type=service` on API versions older than 2018-02-05, you can specify [`type=service`](https://docs.stripe.com/api/products/list#list_products-type) when listing products.)
    
*   Major
    
    Allows a new subscription’s first full invoice to be on a future date, by specifying `billing_cycle_anchor`, with an optional proration up to that date.`billing_cycle_anchor` on its own is available retroactively to past versions, and starting in this version, `billing_cycle_anchor` can be combined with a trial, enabling a free trial to be followed by a prorated period, followed by a fixed billing cycle.
    
*   Prorations on free plans now create $0 invoices. In past versions, these did not create invoices.
    

### 2018-01-23

*   When being viewed by a platform, cards and bank accounts created on behalf of connected accounts will have a fingerprint that is universal across all connected accounts. For accounts that are not connect platforms, there will be no change.
    

### 2017-12-14

*   Updates invoice payment attempts to return a `card_error` when the charge is declined. This aligns `/v1/invoices/{INVOICE_ID}/pay` with `/v1/charges`.
    
*   Updates invoice line items to always have a `description` set, including invoice line items generated from subscription items.
    

### 2017-08-15

*   Adds `not_required` as a possible `redirect[status]` value on the `Source` object. Previously, optional redirects were marked as `succeeded`.
    

### 2017-06-05

*   Adds `under_review` as a possible `verification[disabled_reason]` value on the `Account` object. Previously, an under review status used the value `other`.
    

### 2017-05-25

*   Replaces the `managed` Boolean property on `Account` objects with `type`, whose possible values are: `standard`, `express`, and `custom`. A `type` value is required when creating accounts. The `standard` type replaces `managed: false`, and the `custom` type replaces `managed: true`.
    
*   Updates the `previous_attributes` property on `Event` objects to show entire sub-arrays when those arrays have changes. Previously, those sub-arrays only showed the specific fields that changed.
    
*   Updates the `request` property on the `Event` object to be a hash containing the request ID and the idempotency key. Previously, `request` was just the ID.
    
*   Renames the `user_id` property on Connect-related event objects to `account`.
    

### 2017-04-06

*   Major
    
    Splits the `Transfer` object into `Payout` and `Transfer`. The `Payout` object represents money moving from a Stripe account to an external account (bank or debit card). The `Transfer` object now only represents money moving between Stripe accounts on a Connect platform. For more details, see [https://stripe.com/docs/transfer-payout-split](https://stripe.com/docs/transfer-payout-split).
    

### 2017-02-14

*   Updates the `dispute` property on the `Charge` object to contain the ID of an associated dispute. Previously, `dispute` contained the entire `Dispute` object. You can [expand this property](https://stripe.com/docs/api#expanding_objects) when retrieving charges to render the full `Dispute` object as before.
    
*   Updates the `outcome[rule]` property on the `Charge` object to contain the ID of the rule that blocked the charge. Previously, `outcome[rule]` contained the entire `Rule` object. You can [expand this property](https://stripe.com/docs/api#expanding_objects) when retrieving charges to render the full `Rule` object as before.
    

### 2017-01-27

*   Removes the `sourced_transfers` property from the `Balance Transaction` object.
    

### 2016-10-19

*   Returns the status code 403 when an API request is made with insufficient permission. Previously, the API returned a 401 status code.
    

### 2016-07-06

*   Updates the list all subscriptions call to also return canceled subscriptions. The endpoint now supports fetching only canceled subscriptions by specifying `status=canceled`. You can now retrieve a single canceled subscription by providing its ID.
    

### 2016-06-15

*   Updates the `active` property on the `Product` object so that setting `active` to false no longer marks the product’s SKUs as inactive.
    

### 2016-03-07

*   Removes the `currencies_supported` property from the `Account` object. You can find a list of supported currencies by retrieving a `Country Spec` object for the country of the account.
    

### 2016-02-29

*   Adds postal code validation for legal entity addresses when creating and updating accounts.
    

### 2016-02-23

*   Updates the behavior of orders so that changing an order from `paid` or `fulfilled` to `canceled` or `returned` automatically refunds the associated charge. Previously, attempting to change an order from `paid` or `fulfilled` to `canceled` or `returned` raised an error if the associated charge had not already been refunded.
    

### 2016-02-22

*   Returns an error on attempts to add more than 250 invoice items to an invoice.
    

### 2016-02-19

*   Renames the `name` property on the `Bank Account` object to `account_holder_name`.
    

### 2016-02-03

*   Updates the returned `Account` object to only show sub-properties of `legal_entity` that are applicable to the account’s country, or that were previously provided.
    

### 2015-10-16

*   Returns an error if a `tax_percent` is provided without a `plan` during a customer update or creation.
    

### 2015-10-12

*   Major
    
    Returns an error when invalid parameters are passed in the card or bank account hash during token, source, or external account creation. Changes the error code returned for missing required parameters in the card or bank account hash to 400. Previously, a 402 code was returned.
    

### 2015-10-01

*   Replaces the `bank_accounts` property on the `Account` object with `external_accounts`. Replaces the `bank_account` value in the `fields_needed` property with `external_account`.
    

### 2015-09-23

*   Updates the `charge` property on the `Invoice` object to always show the invoice’s latest charge, regardless of the charge’s source (e.g, a card or a bank account). Removes the `payment` property, which previously reflected a non-card charge.
    
*   Major
    
    Updates the list all charges call to return all charges, including those made to bank accounts and other non-card sources. Previously, it only returned charges made to cards. Updates the deprecated `offset` parameter to only be supported when filtering by source type.
    

### 2015-09-03

*   Returns an error if a request reuses an idempotency token with different parameters than the original request. Previously, errors were only returned for reusing the same idempotency token across different API endpoints.
    

### 2015-08-19

*   Updates the `Balance Transaction` object to provide the refund ID or dispute ID as the `source` value when the balance transaction is associated with a refund or dispute. Previously, the original charge ID was shown.
    

### 2015-08-07

*   Adds date validation to the `tos_acceptance[date]` property on the `Account` object. Accepted values are timestamps after 2009 and before the current moment.
    

### 2015-07-28

*   The `balance.available` event is now triggered when immediate transfers are processed.
    

### 2015-07-13

*   Replaces the `verification[contacted]` Boolean property on the `Account` object with a `verification[disabled_reason]` string that describes why the account is unable to make transfers or charges.
    

### 2015-07-07

*   Updates the `status` property on the `Transfer` object so that transfers not yet submitted to the bank are still `pending` and transfers submitted to the bank that have not yet arrived are `in_transit`. Previously, both states were described as `pending`.
    

### 2015-06-15

*   Updates the `payout_schedule[delay_days]` property on the `Account` object to return an error if provided when the `interval` is set to `manual`. Manual payouts always use the minimum `delay_days` value.
    

### 2015-04-07

*   Updates the `period[end]` property on proration invoice line items to reflect the subscription’s `current_period_end` property when the update and proration was made. A proration invoice line item’s `period[start]` and `period[end]` properties now represent the prorated adjustment interval. Previously, `period[end]` marked the time at which the proration was made, and was the same as `period[start]`.
    
*   Updates the `Invoice` object to change the order of the `lines` list: first invoice items in reverse chronological order, followed by the subscription, if applicable.
    

### 2015-03-24

*   Updates coupons so they no longer apply to negative invoice items by default. Previously, coupons applied to all non-proration invoice items. To allow a coupon to apply to a negative invoice item, pass `discountable=true` when creating or updating the invoice item.
    

### 2015-02-18

*   Updates the `status` property on the `Charge` object to have a value of `succeeded` for successful charges. Previously, the `status` property would be `paid` for successful charges.
    
*   Major
    
    Replaces the `card` property on the `Charge` object with `source`. Provide this parameter with a `Card` token, as before, or with a `Source` token that has an `object` value of `card`. Older API versions return both the `card` and `source` properties on `Charge`.
    
*   Major
    
    Replaces the `cards` and `default_card` properties on the `Customer` object with `sources` and `default_source`. Both properties can represent `Card` objects, as before, and `Source` objects with an `object` value of `card`. Older API versions return both the new and old properties on `Customer`. Replaces the `customer.card.*` and `customer.bank_account.*` events with `customer.source.*`.
    

### 2015-02-16

*   Renames the `transfer.canceled` event to `transfer.reversed`.
    

### 2015-02-10

*   Adds the value `warning_closed` to the `status` property on the `Dispute` object.
    
*   Updates test mode transfers to require sufficient funds in your available test mode balance (for consistency with live mode transfers). Add funds directly to your available test mode balance—bypassing the pending balance—by creating a charge using the special test card number **4000 0000 0000 0077**.
    

### 2015-01-26

*   Updates the presentation of nested hashes in the `previous_attributes` property of events to only show the difference. For example, a change from `{address: {line1: "Foo", line2: "Bar"}}` to `{address: {line1: "Foo", line2: "Baz"}}` is represented as `{previous_attributes: {address: {line2: "Baz"}}}`. Previously, it was represented as `{previous_attributes: {address: {line1: "Foo", line2: "Baz"}}}`.
    
*   Updates the `canceled_at` property on the `Subscription` object to always be the timestamp from the API call or invoice payment failure that canceled the subscription. Previously, `canceled_at` reflected “at period end” subscription cancellations, too. The `ended_at` property still reflects the time that the subscription actually stopped.
    

### 2015-01-11

*   Removes the `mimetype` property from the `File Upload` object. Returns simplified file types in the `type` property and uses simpler naming conventions than mimetypes (e.g., `type` contains **pdf** instead of **application/pdf**).
    

### 2014-12-22

*   Updates the `Card` object so a value of `unchecked` for the `address_line1_check`, `address_zip_check`, or `cvc_check` properties means the property has not been checked. Previously, it meant the issuing bank does not support the particular check. That state now shows as `unavailable`. Unchecked properties are checked when a card is charged or added to a `Customer` object.
    
*   Removes the `customer` property from the `Card` object that appears on the `Token` object.
    

### 2014-12-17

*   Replaces the `statement_description` property on the `Charge`, `Invoice`, `Plan`, and `Transfer` objects with `statement_descriptor`. To determine what appears on a customer’s transaction, `statement_description` is appended to your Stripe account’s statement descriptor while `statement_descriptor` sets the full statement value. If not on this API version or newer, providing a `statement_descriptor` still triggers the `statement_description` behavior. Regardless of API version, the `statement_description` behavior does not apply with PaymentIntents.
    
*   Updates the Accounts API to require API version 2014-12-17 or newer.
    

### 2014-12-08

*   Updates the `Dispute` object so evidence can be provided as a hash of typed fields rather than a single block of text. Replaces the `evidence_due_by` property with the `evidence_details` hash, which includes `due_by` and `submission_count` (for the number of times a dispute has been submitted).
    

### 2014-11-20

*   Updates disputes that are won to return the status `won` even if the charge was refunded. Previously, a dispute won that had a refunded charge would transition to `charge_refunded`.
    
*   Updates the `metadata` property of the `Invoice Item` object with a type of `subscription` to show the subscription’s metadata. Previously, it showed the plan’s metadata.
    

### 2014-11-05

*   Renames the `charge_enabled` and `transfer_enabled` properties on the `Account` object to `charges_enabled` and `transfers_enabled`.
    

### 2014-10-07

*   Prevents publishable keys from retrieving `Token` objects. When a card or bank account token is created with a publishable key, the `fingerprint` property is not included in the response.
    

### 2014-09-08

*   Replaces the `disabled`, `validated`, and `verified` properties on the `Bank Account` object with a `status` enum property.
    

### 2014-08-20

*   Adds three values to the `status` property on the `Dispute` object: `warning_needs_response`, `warning_under_review`, and `charge_refunded`. Replaces the `balance_transaction` property of the `Dispute` object with `balance_transactions` (this provides greater detail around funds withdrawn and reinstated as a result of disputes).
    

### 2014-08-04

*   Removes the `other_transfers`, `summary`, and `transactions` properties from automatic transfer responses in favor of the balance history endpoint (**/v1/balance/history**). _Update_: As of June 20, 2024, these properties are no longer available in any versions, including those prior to 2014-08-04.
    

### 2014-07-26

*   Changes the `refunds` property on the `Application Fee` object from an array to a sublist object, which contains the `data`, `has_more`, and `url` properties. This makes application fee refunds consistent with charge refunds.
    

### 2014-07-22

*   Updates proration line items on invoices to include the associated subscription’s plan and quantity.
    

### 2014-06-17

*   Changes the `refunds` property on the `Charge` object from an array to a sublist object, which contains the `data`, `has_more`, and `url` properties.
    

### 2014-06-13

*   Renames the `type` property on the `Card` object to `brand`.
    

### 2014-05-19

*   Replaces the `account` property on the `Transfer` object with `bank_account`. The `bank_account` property is only included when the transfer is made to a bank account.
    

### 2014-03-28

*   Major
    
    Removes the `count` property from list responses.
    
*   Update error message for old API versions which do not support include\[\]=total\_count but generate error message about it.
    

### 2014-03-13

*   Renames the `statement_descriptor` property on the `Transfer` object to `statement_description`.
    

### 2014-01-31

*   Major
    
    Replaces the `subscription` property on the `Customer` object with the `subscriptions` property, as customers can have multiple subscriptions.
    
*   Ignores trial dates on canceled subscriptions when automatically computing trial end dates for new subscriptions.
    

### 2013-12-03

*   Replaces the `user` and `user_email` properties on the `Application Fee` object with an expandable `account` property.
    
*   Updates the refunding of application fees to be proportional to the amount of the charge refunded (when setting `refund_application_fee=true`). Previously, the entire application fee was refunded even when only part of the charge was.
    

### 2013-10-29

*   Major
    
    Changes coupon behavior so that applying an amount-off coupon to an invoice does not increase the `Customer` account balance if the discount is greater than the invoice amount. Coupons are ignored—and not counted as redeemed—when applied to zero-cost invoices. This change does not apply to coupons created on earlier API version.
    

### 2013-08-13

*   Removes the `fee` and `fee_details` properties from the `Charge` and `Transfer` objects. Fee information is in the corresponding balance transaction.
    

### 2013-08-12

*   Allows the `description` property on `Customer`, `Charge`, `InvoiceItem`, and `Recipient` objects, and the `email` property on `Customer` and `Recipient` objects, to be set to null by providing empty string values in POST requests.
    

### 2013-07-05

*   Major
    
    Replaces the `active_card` property on the `Customer` object with a `cards` sublist and a `default_card` ID property.
    

### 2013-02-13

*   Updates the `Charge` object so disputed charges include another `stripe_fee` object in the `fee_details` array, representing the dispute fees. Includes the dispute fees in the fee total on the `Charge` object.
    

### 2013-02-11

*   Major
    
    Updates the pay invoice call to return an error when the charge is not successful. Previously, the API would return a 200 status and set the invoice’s `paid` property to false.
    

### 2012-11-07

*   Replaces the `disputed` property on the `Charge` object with `dispute`.
    

### 2012-10-26

*   Updates the `Invoice` object format. The `lines` property is now a _sublist_, a paginated list of all items that contribute to the invoice.
    

### 2012-09-24

*   Removes the extraneous `id` property from the `Discount` object.
    

### 2012-07-09

*   Removes the `uncaptured` property from the `Customer` object.
    

### 2012-06-18

*   Removes the `amount` and `currency` properties from the `Token` object.
    

### 2012-03-25

*   Removes the `next_recurring_charge` property from the `Customer` object. Use the upcoming invoice call instead.
    

### 2012-02-23

*   Shows all response fields, even those with null values. Previously, the API hid fields with null values.
    

### 2011-09-15

*   Updates the card validation behavior when creating tokens.
    

### 2011-08-01

*   Updates the list format. New list objects have a `data` property that represents an array of objects (by default, 10) and a `count` property that represents the total count.
    

### 2011-06-28

*   Removes the `identifier` property (duplicate of `id`) from the `Plan` object.
    

### 2011-06-21

*   Raises exceptions on unrecognized parameters passed to the API instead of silently allowing and ignoring them.
