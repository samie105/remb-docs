---
title: "Fleet integration guide"
source: "https://docs.stripe.com/issuing/integration-guides/fleet"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:04:13.386Z"
content_hash: "d875160cee8fad141fcb477ad6be418cf2db19b8543c35a52dd594e126565126"
---

Build a fleet offering by using Stripe [Issuing](https://docs.stripe.com/issuing) to create cards and process transactions for your customers’ business.

By the end of this guide, you’ll know how to:

*   Create verified connected accounts representing your business customers.
*   Create cards for your business customers and use these cards to spend funds.
*   Understand the additional fleet specific fields collected at the pump or point of sale.

## Before you begin

1.  Sign up for a [Stripe account](https://dashboard.stripe.com/register).
2.  [Activate Issuing](https://dashboard.stripe.com/issuing/activate) in a [sandbox](https://docs.stripe.com/sandboxes) environment from the Dashboard.
3.  Configure your [Connect platform branding settings](https://dashboard.stripe.com/settings/connect/stripe-dashboard/branding) for your business and add an icon.

## Overview

Stripe Issuing enables fleet management platforms and operators to create and manage customized fleet card programs with physical or virtual payment cards. Issuing allows users to efficiently control, manage, and reconcile expenses related to their clients’ electric or traditional fuel vehicle fleets.

Stripe’s platform provides advanced capabilities with open-loop cards accepted anywhere, real-time spend controls at the point of purchase, advanced fraud protection leveraging Stripe’s fraud tools and authorization signals, and the ability to define card benefits unique to your program, such as 1% cashback on fuel spend. Fleet providers can also issue cards tied to individual or groups of vehicles, facilitating precise expense tracking (including odometer readings) and limiting spend to authorized drivers, merchants, or certain purchase categories.

Stripe’s platform provides data access to identify insights in spend patterns, mileage, maintenance, and transaction details, allowing businesses to customize their fleet program. This approach provides greater operational efficiency with realized cost savings, as well as an oversight of card-based expenditure across fuel, repairs, food, accommodation, and more.

[](#set-up-connect)

### Create a connected account

Create a connected account to represent a business customer of your platform. For your platform, each fleet operator would be represented as a connected account.

#### Connect account types

Issuing only supports connected accounts that don’t use a Stripe-hosted Dashboard, and where your platform is responsible for requirements collection and loss liability, also known as a Custom connected account. Learn how to [create connected accounts](https://docs.stripe.com/connect/interactive-platform-guide?connect-charge-type=direct&connect-loss-liability-owner=platform) that work with Issuing. If your existing accounts don’t match this configuration, you must recreate them.

The following request creates a US-based connected account with the correct configuration and requests the requisite capabilities:

`curl https://api.stripe.com/v1/accounts \  -u "`

`sk_test_REDACTED`

`:" \  -d country=US \  -d "controller[stripe_dashboard][type]=none" \   -d "controller[fees][payer]=application" \   -d "controller[losses][payments]=application" \   -d "controller[requirement_collection]=application" \   -d "capabilities[transfers][requested]=true" \   -d "capabilities[card_issuing][requested]=true" \   -d "capabilities[us_bank_account_ach_payments][requested]=true"`

The user’s account information appears in the response:

`{     ...     "id":   "{{CONNECTED_ACCOUNT_ID}}",     "controller": {       "stripe_dashboard": {         "type": "none"       },       "fees": {         "payer": "application"       },       "losses": {         "payments": "application"       },       "is_controller": true,       "type": "application",       "requirement_collection": "application"     },     ... }`

Note the connected account’s `id`. You’ll provide this value to [authenticate](https://docs.stripe.com/connect/authentication) as the connected account by passing it into requests in the `Stripe-Account` header.

If a connected account already exists, you can add the requisite capabilities by specifying the connected account `id` in the request:

`curl https://api.stripe.com/v1/accounts/`

`{{CONNECTED_ACCOUNT_ID}}`

 `\  -u "  sk_test_REDACTED  :" \  -d "controller[stripe_dashboard][type]=none" \   -d "controller[fees][payer]=application" \   -d "controller[losses][payments]=application" \   -d "controller[requirement_collection]=application" \   -d country=US \   --data-urlencode "email=jenny.rosen@example.com" \   -d "capabilities[transfers][requested]=true" \   -d "capabilities[card_issuing][requested]=true"`

### Verify the connected account

Choose one of the following onboarding options:

[Stripe-hosted onboarding](https://docs.stripe.com/connect/hosted-onboarding) is a web form hosted by Stripe with your brand’s name, color, and icon. Stripe-hosted onboarding uses the [Accounts API](https://docs.stripe.com/api/accounts) to read the requirements and generate an onboarding form with robust data validation and is localized for all Stripe-supported countries.

Before using Connect Onboarding, you must provide the name, color, and icon of your brand in the Branding section of your [Connect settings page](https://dashboard.stripe.com/test/settings/connect).

You can use hosted onboarding to allow connected accounts to link an `external_account` (which is required for payouts) by enabling it through your [Connect Onboarding settings](https://dashboard.stripe.com/settings/connect).

To create an onboarding link for the connected account, use the [Account Links API](https://docs.stripe.com/api/account_links/create).

`curl https://api.stripe.com/v1/account_links \  -u "`

`sk_test_REDACTED`

`:" \  -d account={{CONNECTED_ACCOUNT_ID}} \   --data-urlencode "refresh_url=https://example.com/reauth" \   --data-urlencode "return_url=https://example.com/return" \   -d type=account_onboarding`

#### Caution

For security reasons, don’t email, text, or send account link URLs directly to your connected account. We recommend that you distribute the account link URL from within your platform’s application, where their account is authenticated.

The response you receive includes the `url` parameter containing the link for your connected account to onboard to your platform.

At this point, Stripe has created and verified the connected account with `active` relevant capabilities to use Issuing and Treasury for platforms.

To learn more, see:

*   [Set up an Issuing and Connect integration](https://docs.stripe.com/issuing/connect)
*   [Stripe hosted onboarding for connected accounts](https://docs.stripe.com/connect/custom/hosted-onboarding)
*   [Creating and using connected accounts](https://docs.stripe.com/connect/interactive-platform-guide?connect-charge-type=direct&connect-loss-liability-owner=platform)
*   [Identify verification for connected accounts](https://docs.stripe.com/connect/identity-verification)

[](#create-cardholders-cards)

The [Cardholder](https://docs.stripe.com/api/issuing/cardholder/object) is the individual driver (that is, employee or contractor) that’s authorized by your business customer to use card funding by the associated balance. The `Cardholder` object includes relevant details, such as a [name](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-name) to display on cards and a [billing](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-billing) address, which is usually the business address of the connected account or your platform.

Use the embedded [Issuing cards list component](https://docs.stripe.com/connect/supported-embedded-components/issuing-cards-list) to enable your connected accounts to create a [Card](https://docs.stripe.com/api/issuing/cards/object) for a Cardholder and associate it with the Financial Account.

This demo is read-only with limited functionality. Visit [furever.dev](https://furever.dev/) for a fully functional demo.

When [creating an Account Session](https://docs.stripe.com/api/account_sessions/create), enable the Issuing cards list component by specifying `issuing_cards_list` in the `components` parameter. You can enable or disable individual features of the Issuing cards list component by specifying the `features` parameter under `issuing_cards_list`.

`curl https://api.stripe.com/v1/account_sessions \  -u "`

`sk_test_REDACTED`

`:" \  -d "account=  {{CONNECTED_ACCOUNT_ID}}  " \   -d "components[issuing_cards_list][enabled]=true" \   -d "components[issuing_cards_list][features][card_management]=true" \   -d "components[issuing_cards_list][features][cardholder_management]=true" \   -d "components[issuing_cards_list][features][card_spend_dispute_management]=true" \   -d "components[issuing_cards_list][features][spend_control_management]=true"`

After creating the account session and [initializing ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions), you can render the Issuing cards list component in the front end:

`// Include this element in your HTML const issuingCardsList = stripeConnectInstance.create('issuing-cards-list'); issuingCardsList.setShowSpendControls(true); container.appendChild(issuingCardsList);`

From here, users can click **Create card** to begin creating a new Cardholder and Card. The user can also activate the card during creation, or do so afterwards.

At this point, there’s an active card attached to a cardholder and financial account. See the [Issuing page](https://dashboard.stripe.com/issuing/overview) for the connected account to view the card and cardholder information.

To learn more, see:

*   [Virtual cards with Issuing](https://docs.stripe.com/issuing/cards/virtual)
*   [Physical cards](https://docs.stripe.com/issuing/cards/physical)
*   [Use the Dashboard for Issuing with Connect](https://docs.stripe.com/issuing/connect#using-dashboard-issuing)
*   [Create cards with the API](https://docs.stripe.com/api/issuing/cards)

[](#use-card)

When a card is used to make a purchase, it generates an authorization request, which can be approved or declined in real-time.

Card network notifies Stripe

Request real-time decision

Approve and set max `amount`

Return result to card network

Fueling completes up to `amount`

Card network notifies Stripe

With a configured fleet card program, you’ll access additional fleet-specific fields gathered at the pump or point of sale. This includes odometer reading, driver identification, fuel type, gallons pumped, and itemized non-fuel product details, enabled by a fleet-specific chip configuration on the card. This data becomes available at the point of purchase during authorization, and later when the transaction is processed. Some fuel dispensers allow [partial authorization](https://docs.stripe.com/issuing/purchases/authorizations#handling-other-authorizations).

To observe the impact of card activity on the associated balance, generate a test authorization.

As a user with a Commercial Fleet card program, you receive specific fleet-related data on the [Authorization](https://docs.stripe.com/api/issuing/authorizations/object) object.

You can create a test authorization on the Issuing page of the Dashboard for the connected account, or with the following call to the [Authorizations API](https://docs.stripe.com/api/issuing/authorizations):

`curl https://api.stripe.com/v1/test_helpers/issuing/authorizations \  -u "`

`sk_test_REDACTED`

`:" \  -d "card=  {{CARD_ID}}  " \   -d amount=100 \  -d authorization_method=chip \  -d "fleet[cardholder_prompt_data][odometer]=42424" \   -d "fleet[purchase_type]=fuel_purchase" \   -d "fleet[service_type]=self_service" \   -d "merchant_data[category]=automated_fuel_dispensers" \   -d is_amount_controllable=true`

After approval, Stripe creates an `Authorization` in a `pending` state while it waits for [capture](https://docs.stripe.com/issuing/purchases/transactions).

The authorized `amount` is the default amount held for a [fuel dispenser transaction](https://docs.stripe.com/issuing/purchases/authorizations#fuel-dispenser-authorizations) unless you’ve provided a different partial authorization amount in your response to the `issuing_authorization.request` webhook.

Make note of the authorization `id` that you’ll use to capture the funds:

`{   "id": "iauth_1NvPyY2SSJdH5vn2xZQE8C7k",   "object": "issuing.authorization",   "amount": 10000,   ...   "fleet": {     "cardholder_prompt_data": {       "odometer": 42424     },     "purchase_type": "fuel_purchase",     "service_type": "self_service"   },   "status": "pending",   "transactions": [] }`

### Simulate fuel dispenser completion

In testing environments, you can simulate the completion of fuel being dispensed using the following code:

`curl https://api.stripe.com/v1/test_helpers/issuing/authorizations/`

`{{AUTHORIZATION_ID}}`

`/finalize_amount \  -u "  sk_test_REDACTED  :" \  -d final_amount=1000 \  -d "fleet[cardholder_prompt_data][odometer]=42424" \   -d "fleet[purchase_type]=fuel_purchase" \   -d "fleet[reported_breakdown][fuel][gross_amount_decimal]=10.0" \   -d "fleet[reported_breakdown][non_fuel][gross_amount_decimal]=0" \   -d "fleet[reported_breakdown][tax][local_amount_decimal]=0.03" \   -d "fleet[service_type]=self_service" \   -d "fuel[industry_product_code]=001" \   -d "fuel[quantity_decimal]=5.0" \   -d "fuel[type]=unleaded_regular" \   -d "fuel[unit]=us_gallon" \   -d "fuel[unit_cost_decimal]=200"`

The `Authorization` remains in a `pending` state until it’s [captured](https://docs.stripe.com/issuing/purchases/transactions). The amount is updated to reflect the total amount of fuel dispensed, and additional fleet-specific fields are now available:

`{   "id": "iauth_1NvPyY2SSJdH5vn2xZQE8C7k",   "object": "issuing.authorization",   "amount": 1000,   ...   "fleet": {     "cardholder_prompt_data": {       "odometer": 42424     },     "purchase_type": "fuel_purchase",     "reported_breakdown": {       "fuel": {         "gross_amount_decimal": "10.0"       },       "non_fuel": {         "gross_amount_decimal": "0"       },       "tax": {         "local_amount_decimal": "0.03",         "national_amount_decimal": null       }     },     "service_type": "self_service"   },   "fuel": {     "industry_product_code": "001",     "quantity_decimal": "5.0",     "type": "unleaded_regular",     "unit": "us_gallon",     "unit_cost_decimal": "200"   },   "status": "pending",   "transactions": [] }`

### Capture the funds

In testing environments, you can capture the funds using the following code:

`curl https://api.stripe.com/v1/test_helpers/issuing/authorizations/`

`{{AUTHORIZATION_ID}}`

`/capture \  -u "  sk_test_REDACTED  :" \  -d "purchase_details[fleet][cardholder_prompt_data][odometer]=42424" \   -d "purchase_details[fleet][purchase_type]=fuel_purchase" \   -d "purchase_details[fleet][reported_breakdown][fuel][gross_amount_decimal]=10.0" \   -d "purchase_details[fleet][reported_breakdown][non_fuel][gross_amount_decimal]=0" \   -d "purchase_details[fleet][reported_breakdown][tax][local_amount_decimal]=0.03" \   -d "purchase_details[fleet][service_type]=self_service" \   -d "purchase_details[fuel][industry_product_code]=001" \   -d "purchase_details[fuel][quantity_decimal]=5.0" \   -d "purchase_details[fuel][type]=unleaded_regular" \   -d "purchase_details[fuel][unit]=us_gallon" \   -d "purchase_details[fuel][unit_cost_decimal]=200"`

After the authorization is captured, Stripe creates an Issuing [Transaction](https://docs.stripe.com/issuing/purchases/transactions), the `status` of the authorization is set to `closed`.

As a user with a Commercial Fleet card program, you receive specific fleet-related data on the [Transaction](https://docs.stripe.com/api/issuing/transactions), (for example, to reconcile purchases).

`{   "id": "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ",   "object": "issuing.transaction",   "amount": 1000,   ...   "purchase_details": {     "fleet": {       "cardholder_prompt_data": {         "odometer": 42424       },       "purchase_type": "fuel_purchase",       "reported_breakdown": {         "fuel": {           "gross_amount_decimal": "10.0"         },         "non_fuel": {           "gross_amount_decimal": "0"         },         "tax": {           "local_amount_decimal": "0.03",           "national_amount_decimal": null         }       },       "service_type": "self_service"     },     "fuel": {       "industry_product_code": "001",       "quantity_decimal": "5.0",       "type": "unleaded_regular",       "unit": "us_gallon",       "unit_cost_decimal": "200"     }   } }`

## See also

*   [Spending controls](https://docs.stripe.com/issuing/controls/spending-controls)
*   [Issuing authorizations](https://docs.stripe.com/issuing/purchases/authorizations)
*   [Issuing transactions](https://docs.stripe.com/issuing/purchases/transactions)
*   [Working with Issuing cards and Treasury for platforms](https://docs.stripe.com/treasury/connect/account-management/issuing-cards)
*   [Manage transaction fraud](https://docs.stripe.com/issuing/manage-fraud)
