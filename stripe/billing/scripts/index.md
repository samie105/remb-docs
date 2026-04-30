---
title: "Customize Billing with scripts"
source: "https://docs.stripe.com/billing/scripts"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:12:45.844Z"
content_hash: "bb463ca310fa14d43c001f236dc2d620d189ef14da7cf99cbee502b36c4eef18"
---

#### Interested in getting early access to scripts?

Script authoring is currently in private preview. [Sign up](#signup).

You can use [script extensions](https://docs.stripe.com/extensions/how-extensions-work#scripts) to customize how Stripe Billing behaves at specific steps in the billing flow. Scripts let you modify Stripe’s default behavior when it doesn’t match your business’s billing requirements. Add custom logic to change how to calculate proration amounts, control how to apply customer balances, or define how to route items across invoices. You can configure this and similar behavior through scripts, without building or maintaining anything outside of Stripe.

There are two types of scripts. Both run on Stripe’s infrastructure as part of the billing workflow, and Stripe packages both as apps.

Type

Description

When to use

**Stripe-authored scripts**

Prebuilt, ready to use scripts you can activate and configure in the Dashboard.

*   When you need to start quickly with a prebuilt solution.
*   You don’t want to write or maintain any code.

**User-authored scripts**

You create the scripts in TypeScript to support logic specific to your business.

*   Your use case requires custom logic to support business rules unique to your operations.
*   You need full control over the behavior.

## Get started
