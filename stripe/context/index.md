---
title: "Stripe-Context header"
source: "https://docs.stripe.com/context"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:50:12.498Z"
content_hash: "310c6a08b5110afbb55e2acaba73a5a7679cc0e23ebf9df582937b2bbe13741f"
---

## Perform API operations on related accounts.

By default, API requests execute on the Stripe account that generated the accompanying [API key](https://docs.stripe.com/keys). However, you can use the `Stripe-Context` header to perform an API request in the context of a related account.

## API request scope

You can make API requests to operate within different scopes:

*   Your own account
*   Any connected account in your platform
*   Any v2 account with at least the merchant or recipient configuration
*   Any account in your organization

When you make an API request targeting an account other than that of the API key, you must identify the intended account by including the `Stripe-Context` header. The value depends on the relative relationship of the intended account to the [API key](https://docs.stripe.com/keys) used to make the request.

For example, consider an organization with multiple platform accounts representing different business lines. Each platform has connected accounts and one connected account has a recipient account.

## Rocket, Inc.

Organization org\_1234

## Rocket Rides

Platform acct\_111

## Rocket Repairs

Platform acct\_222

## Rocket Deliveries

Platform acct\_333

## Driver Smith

Connected account acct\_111a

## Mechanic Jones

Connected account acct\_222a

## Courier Vega

Connected account acct\_333a

## Fuel City

Recipient account acct\_111b

Organization with multiple standalone platform accounts representing different business lines, each with connected accounts.

Given this business structure, it’s possible to perform API requests using several different scopes. The following table shows the `Stripe-Context` format for each different scope that requires context based on its relationship to the account the requesting API key belongs to.

Requesting API key owner

Scope account

Stripe-Context format

Rocket, Inc.

Rocket Rides

Platform ID: `acct_111`

Rocket, Inc.

Driver Smith

Platform ID/Connected account ID: `acct_111/acct_111a`

Rocket Rides

Driver Smith

Connected account ID: `acct_111a`

Rocket Deliveries

Courier Vega

Connected account ID: `acct_333a`

Rocket Rides

Fuel City

Connected account ID/Recipient ID: `acct_111a/acct_111b`
