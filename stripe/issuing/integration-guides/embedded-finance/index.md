---
title: "Embedded Finance integration guide"
source: "https://docs.stripe.com/issuing/integration-guides/embedded-finance"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:03:52.173Z"
content_hash: "66cf113f37d0bbef78bd448e7febcdf8b2c292b1df27809aecab15e3e0adc475"
---

Build a US embedded financial services offering using Stripe [Issuing](https://docs.stripe.com/issuing/how-issuing-works) and [Treasury for platforms](https://docs.stripe.com/treasury/connect). Use Issuing to create cards, and Treasury for platforms to store balances and fund card spend.

By the end of this guide, you’ll know how to:

*   Create verified connected accounts representing your business customers with relevant Issuing and Treasury for platforms capabilities
*   Create financial accounts that you can use as a wallet for your business customers and add funds to using an external bank account
*   Create virtual cards for your business customers and use these cards to spend funds from a wallet

## Before you begin

1.  Sign up for a [Stripe account](https://dashboard.stripe.com/register).
2.  [Activate Issuing and Treasury for platforms](https://dashboard.stripe.com/setup/treasury/activate) in a [sandbox](https://docs.stripe.com/sandboxes) environment from the Dashboard. For more information, see [API access to Issuing and Treasury for platforms](https://docs.stripe.com/treasury/connect/access).
3.  Configure your [Connect platform branding settings](https://dashboard.stripe.com/settings/connect/stripe-dashboard/branding) for your business and add an icon.

[](#set-up-connect)

### Create a connected account

Create a connected account to represent a business customer of your platform. For example, if your product is a SaaS platform for restaurants, each restaurant would be represented as a connected account.

#### Connect account types

Issuing only supports connected accounts that don’t use a Stripe-hosted Dashboard, and where your platform is responsible for requirements collection and loss liability, also known as a Custom connected account. Learn how to [create connected accounts](https://docs.stripe.com/connect/interactive-platform-guide?connect-charge-type=direct&connect-loss-liability-owner=platform) that work with Issuing. If your existing accounts don’t match this configuration, you must recreate them.

The following request creates a US-based connected account with the correct configuration and requests the requisite capabilities:

`curl https://api.stripe.com/v1/accounts \  -u "`

`sk_test_REDACTED`

`:" \  -d country=US \  -d "controller[stripe_dashboard][type]=none" \   -d "controller[fees][payer]=application" \   -d "controller[losses][payments]=application" \   -d "controller[requirement_collection]=application" \   -d "capabilities[transfers][requested]=true" \   -d "capabilities[card_issuing][requested]=true" \   -d "capabilities[treasury][requested]=true" \   -d "capabilities[us_bank_account_ach_payments][requested]=true"`

The user’s account information appears in the response:

`{     ...     "id":   "{{CONNECTED_ACCOUNT_ID}}",     "controller": {       "stripe_dashboard": {         "type": "none"       },       "fees": {         "payer": "application"       },       "losses": {         "payments": "application"       },       "is_controller": true,       "type": "application",       "requirement_collection": "application"     },     ... }`

Note the connected account’s `id`. You’ll provide this value to [authenticate](https://docs.stripe.com/connect/authentication) as the connected account by passing it into requests in the `Stripe-Account` header.

If a connected account already exists, you can add the requisite capabilities by specifying the connected account `id` in the request:

`curl https://api.stripe.com/v1/accounts/`

`{{CONNECTED_ACCOUNT_ID}}`

 `\  -u "  sk_test_REDACTED  :" \  -d "controller[stripe_dashboard][type]=none" \   -d "controller[fees][payer]=application" \   -d "controller[losses][payments]=application" \   -d "controller[requirement_collection]=application" \   -d country=US \   --data-urlencode "email=jenny.rosen@example.com" \   -d "capabilities[transfers][requested]=true" \   -d "capabilities[treasury][requested]=true" \   -d "capabilities[card_issuing][requested]=true"`

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

[](#create-financial-accounts-add-funds)

After you enable Financial Accounts on your platform, add [FinancialAccount](https://docs.stripe.com/api/treasury/financial_accounts) objects to your [platform architecture](https://docs.stripe.com/treasury/connect/account-management/accounts-structure) to enable the efficient storing, sending, and receiving of funds. Stripe attaches a financial account to your platform account after enablement, and lets you provision an individual financial account for each eligible connected account on your platform.

In the Stripe API, `FinancialAccount` objects serve as the source and destination of money movement API requests. You request `Features` through the API to assign to `FinancialAccounts` that provide additional functionality for the financial accounts on your platform.

A financial account operates a distinct [balance of funds](https://docs.stripe.com/treasury/connect/account-management/working-with-balances-and-transactions) from the connected account payments balance of the account it’s linked to. For example, the owner of a connected account on your platform might have a 100 USD connected account balance and a 200 USD financial account balance. In this scenario, the connected account owner has a sum of 300 USD spread between their financial account and connected account balances. These two balances remain separate, but the API provides the ability to move money from the connected account balance to the financial account balance.

### Create a Financial Account

After Stripe adds the `treasury` capability to an account and it’s marked `active`, you can create a `FinancialAccount` object for the connected account. To do this, call `FinancialAccounts` and request the `Features` you want to provide:

`curl https://api.stripe.com/v1/treasury/financial_accounts \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Account:   {{CONNECTED_ACCOUNT_ID}}  " \  -d "supported_currencies[]=usd" \   -d "features[card_issuing][requested]=true" \   -d "features[deposit_insurance][requested]=true" \   -d "features[financial_addresses][aba][requested]=true" \   -d "features[inbound_transfers][ach][requested]=true" \   -d "features[intra_stripe_flows][requested]=true" \   -d "features[outbound_payments][ach][requested]=true" \   -d "features[outbound_payments][us_domestic_wire][requested]=true" \   -d "features[outbound_transfers][ach][requested]=true" \   -d "features[outbound_transfers][us_domestic_wire][requested]=true"`

The response, when you request features on financial account creation, indicates their status in the `active_features`, `pending_features`, and `restricted_features` parameters:

`{   "object": "treasury.financial_account",   "created": 1612927106,   "id": "fa_123",   "country": "US",   "supported_currencies": ["usd"],   "active_features": ["card_issuing"],   "pending_features": ["financial_addresses.aba"],   "restricted_features": [],   // No FinancialAddress added as the financial_addresses.aba feature is not yet active   "financial_addresses": [],   "livemode": true,   "status": "open",   ... }`

Activation might be instantaneous for some features (for example, `card_issuing`). However, other features, like `financial_addresses.aba`, [activate asynchronously](https://docs.stripe.com/treasury/connect/account-management/financial-account-features#webhooks) and might stay `pending` for up to 30 minutes while Stripe communicates with external systems. After all of the relevant features are active, you get confirmation on the `treasury.financial_account.features_status_updated` webhook listener. See [Available features](https://docs.stripe.com/treasury/connect/account-management/financial-account-features#available-features) for more information on financial account features.

### Link a bank account

To let your customers transfer money to and from an external account, create a `SetupIntent` with the required parameters, and denote that your customer owns the external account by attaching it to `self`:

`curl https://api.stripe.com/v1/setup_intents \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Account:   {{CONNECTED_ACCOUNT_ID}}  " \  -d attach_to_self=true \  -d "flow_directions[]=inbound" \   -d "flow_directions[]=outbound" \   -d "payment_method_types[]=us_bank_account" \   -d "payment_method_data[type]=us_bank_account" \   -d "payment_method_data[us_bank_account][routing_number]=110000000" \   -d "payment_method_data[us_bank_account][account_number]=000123456789" \   -d "payment_method_data[us_bank_account][account_holder_type]=company" \   -d "payment_method_data[billing_details][name]=Company Corp" \  -d confirm=true \  -d "mandate_data[customer_acceptance][type]=online" \   -d "mandate_data[customer_acceptance][online][ip_address]=123.123.123.123" \   --data-urlencode "mandate_data[customer_acceptance][online][user_agent]=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"`

The API response includes a unique identifier for the `payment_method` that’s used to reference this bank account when making ACH transfers:

`{   "id": "{{SETUP_INTENT_ID}}",   "object": "setup_intent",   "next_action": {     "type": "verify_with_microdeposits",     "verify_with_microdeposits": {       "arrival_date": 1642579200,       "hosted_verification_url": "https://payments.stripe.com/microdeposit/sacs_test_xxx",       "microdeposit_type": "amounts"     }   },   ...   "payment_method": "{{PAYMENT_METHOD_ID}}",   "payment_method_types": [     "us_bank_account"   ] }`

Before you can use a bank account, it must be verified using microdeposits (which we focus on here) or the faster [financial connections](https://docs.stripe.com/financial-connections) option. The `SetupIntent` response from the previous step includes a `hosted_verification_url` which you must present to your customer for them to input the associated descriptor code of the microdeposit. Use the value `SM11AA` to verify the bank account, or test a variety of other cases by using the [test account numbers](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment?platform=web&payment-ui=stripe-hosted#test-account-numbers) Stripe provides.

![Microdeposit verification](https://b.stripecdn.com/docs-statics-srv/assets/microdeposit-verification.a9151fafd6f3582cb8a268bf7b1b306e.png)

Microdeposit verification

### Add funds to the financial account

Using the embedded [Financial account component](https://docs.stripe.com/connect/supported-embedded-components/financial-account) in your application, you can enable your Connected Accounts to transfer funds into the Financial account.

## Create an Account Session

When [creating an Account Session](https://docs.stripe.com/api/account_sessions/create), enable the financial account component by specifying `financial_account` in the `components` parameter. You can enable or disable individual features of the financial account component by specifying the `features` parameter under `financial_account`.

`curl https://api.stripe.com/v1/account_sessions \  -u "`

`sk_test_REDACTED`

`:" \  -d "account=  {{CONNECTED_ACCOUNT_ID}}  " \   -d "components[financial_account][enabled]=true" \   -d "components[financial_account][features][send_money]=true" \   -d "components[financial_account][features][transfer_balance]=true" \   -d "components[financial_account][features][external_account_collection]=true"`

After creating the account session and [initializing ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions), you can render the financial account component in the frontend:

`// Include this element in your HTML const financialAccount = stripeConnectInstance.create('financial-account'); financialAccount.setFinancialAccount('{{FINANCIAL_ACCOUNT_ID}}') container.appendChild(financialAccount);`

From here, users can click **Move money** to initiate a transfer.

At this point, the connected account has a `FinancialAccount` that has been loaded with funds received from an `InboundTransfer` that you can spend using cards or `OutboundPayments` like ACH or wires.

To learn more, see:

*   [Getting permissions for InboundTransfers](https://docs.stripe.com/treasury/connect/moving-money/working-with-bankaccount-objects#permissions)
*   [Working with Treasury for platforms](https://docs.stripe.com/treasury/connect/account-management/financial-accounts)
*   [Using Stripe Treasury to move money](https://docs.stripe.com/treasury/connect/examples/moving-money#microdeposits)
*   [Requesting features on a Financial Account](https://docs.stripe.com/treasury/connect/account-management/financial-account-features#available-features)
*   [Working with SetupIntents, PaymentMethods, and BankAccounts](https://docs.stripe.com/treasury/connect/moving-money/working-with-bankaccount-objects)
*   [Moving money using InboundTransfer objects](https://docs.stripe.com/treasury/connect/moving-money/into/inbound-transfers)
*   [Moving money using ReceivedCredit objects](https://docs.stripe.com/treasury/connect/moving-money/into/received-credits)

[](#create-cardholders-cards)

The [Cardholder](https://docs.stripe.com/api/issuing/cardholder/object) is the individual (that is, employee or contractor) that’s authorized by your business customer to use card funding by the associated balance. The `Cardholder` object includes relevant details, such as a [name](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-name) to display on cards and a [billing](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-billing) address, which is usually the business address of the connected account or your platform.

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

To observe the impact of card activity on the associated balance, generate a test authorization. You can do this in the **Issuing page** of the Dashboard for the connected account, or with the following call to the [Authorization API](https://docs.stripe.com/api/issuing/authorizations):

`curl https://api.stripe.com/v1/test_helpers/issuing/authorizations \  -u "`

`sk_test_REDACTED`

`:" \  -d "card=  {{CARD_ID}}  " \   -d amount=1000 \  -d authorization_method=chip \  -d "merchant_data[category]=taxicabs_limousines" \   -d "merchant_data[city]=San Francisco" \  -d "merchant_data[country]=US" \   -d "merchant_data[name]=Rocket Rides" \  -d "merchant_data[network_id]=1234567890" \   -d "merchant_data[postal_code]=94107" \   -d "merchant_data[state]=CA"`

After approval, Stripe creates an `Authorization` in a `pending` state while it waits for [capture](https://docs.stripe.com/issuing/purchases/transactions). Note the authorization `id` that you’ll use to capture the funds:

`{   "id": "iauth_1NvPyY2SSJdH5vn2xZQE8C7k",   "object": "issuing.authorization",   "amount": 1000,   ...   "status": "pending",   "transactions": [] }`

You can use retrieve the balance details of the financial account and see the impact of the authorization:

`curl https://api.stripe.com/v1/treasury/financial_accounts/`

`{{FINANCIAL_ACCOUNT_ID}}`

 `\  -u "  sk_test_REDACTED  :" \  -H "Stripe-Account:   {{CONNECTED_ACCOUNT_ID}}  "`

The API response is a `FinancialAccount` object with a `balance` hash that details the funds and their availability:

`{   "object": "treasury.financial_account",   "id": "{{FINANCIAL_ACCOUNT_ID}}",   ...   "balance": {     "cash": {"usd": 19000},     "inbound_pending": {"usd": 0},     "outbound_pending": {"usd": 1000}   } }`

The response indicates 190 USD is currently available for use with an additional 10 USD held in `outbound_pending` from the `pending` authorization. You can now simulate capture of the authorization with the API.

### Capture the funds

Capture the funds using the following code:

`curl -X POST https://api.stripe.com/v1/test_helpers/issuing/authorizations/`

`{{AUTHORIZATION_ID}}`

`/capture \  -u "  sk_test_REDACTED  :"`

After the authorization is captured, Stripe creates an Issuing [Transaction](https://docs.stripe.com/issuing/purchases/transactions), the `status` of the authorization is set to `closed`, and a `ReceivedDebit` webhook is created with these details. Retrieving the balance details of the financial account again shows the `outbound_pending` is now 0 USD while the available cash is remains 190 USD:

`{   "object": "treasury.financial_account",   "id": "{{FINANCIAL_ACCOUNT_ID}}",   ...   "balance": {     "cash": {"usd": 19000},     "inbound_pending": {"usd": 0},     "outbound_pending": {"usd": 0}   } }`

## See also

*   [Spending controls](https://docs.stripe.com/issuing/controls/spending-controls)
*   [Issuing authorizations](https://docs.stripe.com/issuing/purchases/authorizations)
*   [Issuing transactions](https://docs.stripe.com/issuing/purchases/transactions)
*   [Working with Issuing cards and Treasury for platforms](https://docs.stripe.com/treasury/connect/account-management/issuing-cards)
*   [Manage transaction fraud](https://docs.stripe.com/issuing/manage-fraud)
