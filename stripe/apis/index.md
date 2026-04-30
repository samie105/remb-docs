---
title: "Stripe APIs"
source: "https://docs.stripe.com/apis"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:52:16.130Z"
content_hash: "79dfd229454f1980f792ef55e3fd19a50bf8e83da29dcf18c2dd246ba0585fdd"
---

[Skip to content](#main-content)

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fapis)

[

](https://docs.stripe.com/)

Search

/Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fapis)

[

Get started



](https://docs.stripe.com/get-started)

[

Payments



](https://docs.stripe.com/payments)

[

Revenue



](https://docs.stripe.com/revenue)

[

Platforms and marketplaces



](https://docs.stripe.com/connect)

[

Money management



](https://docs.stripe.com/money-management)

[

Developer resources



](https://docs.stripe.com/development)

APIs & SDKsHelp

[Overview](https://docs.stripe.com/development)

Versioning

Changelog

[Upgrade your API version](https://docs.stripe.com/upgrades)

Upgrade your SDK version

Essentials

SDKs

API

Overview

[API v2](https://docs.stripe.com/api-v2-overview)

[Rate limits](https://docs.stripe.com/rate-limits)

Authentication

[API keys](https://docs.stripe.com/keys)

[Specify request context](https://docs.stripe.com/context)

[Domains and IP addresses](https://docs.stripe.com/ips)

Make requests

[Expand responses](https://docs.stripe.com/expand)

[Pagination](https://docs.stripe.com/pagination)

[Search objects](https://docs.stripe.com/search)

[Localize content](https://docs.stripe.com/localization)

Testing and data

[Metadata](https://docs.stripe.com/metadata)

[Test your application](https://docs.stripe.com/automated-testing)

Error handling

[Handle errors](https://docs.stripe.com/error-handling)

[Error codes](https://docs.stripe.com/error-codes)

Testing

Stripe CLI

Sample projects

Tools

Stripe Dashboard

Workbench

Developers Dashboard

[Stripe for Visual Studio Code](https://docs.stripe.com/stripe-vscode)

Terraform

[Stripe Discord server](https://docs.stripe.com/discord)

Features

Workflows

Batch jobs

Event destinations

[Stripe health alerts](https://docs.stripe.com/health-alerts)[Stripe Signals](https://docs.stripe.com/signals)[File uploads](https://docs.stripe.com/file-upload)

AI solutions

Agent toolkit

[Model Context Protocol](https://docs.stripe.com/mcp)[Build agentic AI SaaS Billing workflows](https://docs.stripe.com/agents-billing-workflows)

Security and privacy

Security

[Stripebot web crawler](https://docs.stripe.com/stripebot-crawler)

Privacy

Extend Stripe

[Overview](https://docs.stripe.com/extensibility)

Build Stripe apps

Use apps from Stripe

Build extensions

[Custom objects](https://docs.stripe.com/custom-objects)

Partners

Partner ecosystem

[Partner certification](https://docs.stripe.com/partners/training-and-certification)

United KingdomEnglish (United States)

## Learn about Stripe APIs.

Stripe provides a unified set of [REST APIs](https://docs.stripe.com/api), comprised of [two namespaces](https://docs.stripe.com/api-v2-overview#key-differences-between-the-v1-and-v2-namespace), for accepting payments, managing billing and subscriptions, sending payouts, and building financial workflows. You can authenticate requests, shape responses, localize data, test integrations, and handle errors consistently across Stripe products.

## Overview

[](https://docs.stripe.com/api-v2-overview "Compare the API v1 and v2 namespaces")

[Compare the API v1 and v2 namespaces](https://docs.stripe.com/api-v2-overview "Compare the API v1 and v2 namespaces")

[

Learn about Stripe API v2, its response model, and how it compares to API v1.

](https://docs.stripe.com/api-v2-overview "Compare the API v1 and v2 namespaces")

[](https://docs.stripe.com/api-includable-response-values "Manage null API v2 responses")

[Manage null API v2 responses](https://docs.stripe.com/api-includable-response-values "Manage null API v2 responses")

[

Request dependent values in a single response.

](https://docs.stripe.com/api-includable-response-values "Manage null API v2 responses")

[](https://docs.stripe.com/rate-limits "Rate limits")

[Rate limits](https://docs.stripe.com/rate-limits "Rate limits")

[

Understand throttling and throughput behavior.

](https://docs.stripe.com/rate-limits "Rate limits")

## Authentication and security

[](https://docs.stripe.com/keys "API keys")

[API keys](https://docs.stripe.com/keys "API keys")

[

Authenticate requests with secret and restricted keys.

](https://docs.stripe.com/keys "API keys")

[](https://docs.stripe.com/keys-best-practices "Manage secret API keys")

[Manage secret API keys](https://docs.stripe.com/keys-best-practices "Manage secret API keys")

[

Best practices for creating, rotating, and securing keys.

](https://docs.stripe.com/keys-best-practices "Manage secret API keys")

[](https://docs.stripe.com/context "Specify request context")

[Specify request context](https://docs.stripe.com/context "Specify request context")

[

Pass account and idempotency context with requests.

](https://docs.stripe.com/context "Specify request context")

[](https://docs.stripe.com/ips "Domains and IP addresses")

[Domains and IP addresses](https://docs.stripe.com/ips "Domains and IP addresses")

[

Allowlist domains and IP ranges used by Stripe.

](https://docs.stripe.com/ips "Domains and IP addresses")

## Make requests

[](https://docs.stripe.com/expand "Expand responses")

[Expand responses](https://docs.stripe.com/expand "Expand responses")

[

Return nested objects in a single request.

](https://docs.stripe.com/expand "Expand responses")

[](https://docs.stripe.com/pagination "Pagination")

[Pagination](https://docs.stripe.com/pagination "Pagination")

[

Iterate through large lists of resources.

](https://docs.stripe.com/pagination "Pagination")

[](https://docs.stripe.com/search "Search objects")

[Search objects](https://docs.stripe.com/search "Search objects")

[

Look up objects in your Stripe data.

](https://docs.stripe.com/search "Search objects")

## Testing and data

[](https://docs.stripe.com/metadata "Metadata")

[Metadata](https://docs.stripe.com/metadata "Metadata")

[

Attach custom key-value pairs to objects.

](https://docs.stripe.com/metadata "Metadata")

[](https://docs.stripe.com/metadata/use-cases "Use cases")

[Use cases](https://docs.stripe.com/metadata/use-cases "Use cases")

[

Common patterns for modeling data with metadata.

](https://docs.stripe.com/metadata/use-cases "Use cases")

[](https://docs.stripe.com/automated-testing "Automated testing")

[Automated testing](https://docs.stripe.com/automated-testing "Automated testing")

[

Test your application’s behavior and ability to handle errors.

](https://docs.stripe.com/automated-testing "Automated testing")

## Error handling

[](https://docs.stripe.com/error-handling "Error handling")

[Error handling](https://docs.stripe.com/error-handling "Error handling")

[

Interpret errors and display them to users.

](https://docs.stripe.com/error-handling "Error handling")

[](https://docs.stripe.com/error-low-level "Advanced error handling")

[Advanced error handling](https://docs.stripe.com/error-low-level "Advanced error handling")

[

Work with low-level error details.

](https://docs.stripe.com/error-low-level "Advanced error handling")

[](https://docs.stripe.com/error-codes "Error codes")

[Error codes](https://docs.stripe.com/error-codes "Error codes")

[

Browse common error types and parameters.

](https://docs.stripe.com/error-codes "Error codes")

We use cookies to improve your experience and for marketing. Read our [cookie policy](https://stripe.com/cookies-policy/legal) or [manage cookies](https://stripe.com/cookie-settings).
