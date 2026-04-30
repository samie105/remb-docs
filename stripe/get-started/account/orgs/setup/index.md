---
title: "Supported Organization setups"
source: "https://docs.stripe.com/get-started/account/orgs/setup"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:42:15.428Z"
content_hash: "b84491254355a4f2ba1db6d23aec6c06e945133b52f117d7500d7c3b0d4c69a0"
---

Organizations support the following account setups: multiple standalone accounts, platforms, and connected accounts.

## Organizations versus Connect platforms

Organizations and [Connect](https://docs.stripe.com/connect/how-connect-works) platforms both allow a Stripe user to manage multiple related accounts. However, they each serve distinct purposes.

*   **Ownership**: A Connect platform extends its Stripe integration to third parties, while an organization centralizes the management of multiple accounts under common ownership.
*   **Operation**: A Connect platform is itself an account—it processes payments and has balances, customers, subscriptions, and more. An organization doesn’t conduct its own business through Stripe. It acts as a container structure to view and manage the operation of its separate businesses.
*   **Structure**: A Connect platform can belong to an organization. For example, Rocket, Inc. might have separate Connect platforms operating in different global regions, all of which are accounts within the Rocket organization, as shown in the [Connect example setup](#connect-platforms).

## Multiple standalone accounts

It’s common to manage multiple Stripe accounts that represent different business lines, countries of operation, legal entities, and acquisitions.

## Rocket Deliveries

Account 2

Multiple standalone accounts representing different businsess lines.

After you [add these accounts to an organization](https://docs.stripe.com/get-started/account/orgs/build), you can search and download consolidated reports across your accounts without any changes to your Stripe integration. After you create an organization, you can add new business lines or add existing accounts.

## Rocket, Inc.

Organization

## Rocket Deliveries

Account 2

Organization with multiple accounts representing different business lines.

## Multiple platform accounts

If you have several Connect platforms that correspond to different countries of operation or business lines, you can add them to an organization.

## Rocket US

Platform account 1

## Rocket CA

Platform account 2

## Rocket MX

Platform account 3

## Rocket Rides

Connected account 1

## Rocket Repairs

Connected account 2

## Rocket Deliveries

Connected account 3

Multiple Connect platforms representing different business lines, each with connected accounts.

After you add your platforms to an organization, you can search for connected accounts and data within a specific platform or across all your platforms.

## Rocket, Inc.

Organization

## Rocket US

Platform account 1

## Rocket CA

Platform account 2

## Rocket MX

Platform account 3

## Rocket Rides

Connected account 1

## Rocket Repairs

Connected account 2

## Rocket Deliveries

Connected account 3

Organization with multiple Connect platforms representing different business lines, each with connected accounts.

## Multiple connected accounts under a Connect platform

In certain cases, you might own multiple connected accounts connected to the same platform. This commonly occurs in franchise groups where several franchises are under common ownership.

## Prime Motors

Platform account

## Rocket Dealer Seattle

Connected account 1

## Rocket Dealer Tacoma

Connected account 2

## Independent Dealer

Connected account 3

Multiple connected accounts with shared ownership in a platform.

You can add your connected accounts to an organization, independent of their platform. This allows you to use the unified search and reporting across your accounts.

## Prime Dealer Group

Organization

## Prime Motors

Platform account

## Rocket Dealer Seattle

Connected account 1

## Rocket Dealer Tacoma

Connected account 2

## Independent Dealer

Connected account 3

Organization containing a subset of a platform's connected accounts.

## Multiple business lines represented as connected accounts

In some cases, you might represent multiple business lines as a platform with connected accounts, even though your business isn’t a traditional platform or marketplace. This is common if you want to consolidate payment integrations or clone payment methods stored in the platform to connected accounts.

## Furever Grooming

Connected account 1

## Furever Boarding

Connected account 2

## Furever Supplies

Connected account 3

Platform with multiple connected accounts under shared ownership.

By creating an organization that encompasses the platform and connected accounts, you can use unified search and reporting across all the accounts without impacting your payment integrations.

## Furever Grooming

Connected account 1

## Furever Boarding

Connected account 2

## Furever Supplies

Connected account 3

Organization with platform and multiple connected accounts under shared ownership.
