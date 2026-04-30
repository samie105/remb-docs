---
title: "Analytics"
source: "https://docs.stripe.com/billing/subscriptions/analytics"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:13:45.846Z"
content_hash: "da3ea34fec84c1c5370eac53006755a981efa7f8607422d5caea7d9e5e4d6e5c"
---

[Stripe Billing](https://dashboard.stripe.com/billing) analytics and [downloadable reports](#downloadable-reports) let you:

*   Monitor overall performance at a glance
*   Drill down into data to audit changes over time
*   Filter and group data to compare segment performance
*   Benchmark your metrics against similar businesses on Stripe

## Preview features

To get early access to a [preview](https://docs.stripe.com/release-phases) feature, enter your email.

Preview program

Description

Sign up

Usage MRR

Access usage-based MRR and reporting features

Click here to sign up for our preview.

## Downloadable reports

To build financial models and begin downstream reporting, download your billing metrics data. The export is in CSV format and includes the following reports:

Report

Description

MRR per subscriber per month

Includes the Monthly Recurring Revenue (MRR) for each subscriber at the end of each month.

Subscription metrics summary

A summary of your monthly subscription metrics. The report includes your MRR roll-forward report, active subscriber roll-forward report, trial conversion metrics, and lifetime value metrics.

Customer MRR changes

Includes a log of every MRR change for each customer, including new subscribers, upgrades, downgrades, reactivations, and churn.

## Configure your metrics definitions

You can configure metrics from the [Billing overview](https://dashboard.stripe.com/billing) page. Click **Configure** to change how Stripe calculates Monthly Recurring Revenue (MRR), Churn, and Active Subscribers. Changes take 24-48 hours to appear in your configuration.

### Discounts

You can configure whether to include or exclude discounts in your MRR calculation. Subtracting discounts from MRR is considered a more conservative approach to reporting MRR because it more closely reflects the present value of these customers.

You can adjust two settings to exclude discounts:

*   **Subtract recurring discounts from MRR**: Turn this on for your MRR to reflect any recurring discounts applied.
*   **Subtract one-time discounts from MRR**: Turn this on for your MRR to reflect any one-time discounts applied.

These settings apply the same way to all coupons you use on Stripe, including subscription-level coupons, line-item level coupons, and stacked coupons. Permanent recurring discounts, are always subtracted from MRR.

### Active subscribers

You can configure when Stripe considers a subscriber to be active:

*   **At the start of the subscription**: If you select this option, a subscription is considered active when the first billing period begins. This is the most common option.
*   **When the first payment is received**: If you select this, the subscription is considered active when the first payment is received. Use this if you don’t want to consider subscribers active until they’ve paid their first invoice.

## Audit your metrics with drill-downs

You can interact with billing charts using the **Explore** functionality.

Some charts, like **MRR growth** and **Churned revenue**, allow you to drill down into data points to see the underlying data. To do this, click **Explore** on a chart to see the chart and a table of related data points. If a cell in the table is clickable, you can click into it to reveal the underlying events for that data point. This is particularly helpful to understand things like which customers churned or expanded their subscription in a given period.

#### Public preview

This feature is currently available for a subset of billing metrics.

## Analyze your metrics with filtering and grouping

You can interact with billing charts using the **Explore** functionality.

Some charts, like **MRR growth** and **Churned revenue**, allow you to filter and group by **Product** or **Price**. To do this, click **Explore** on a chart to see the chart and a table of related data points below and options for filtering and grouping above.

#### Public preview

This feature is available for a subset of billing metrics. This feature isn’t available if you’re processing subscription volume in multiple currencies.

## Billing metric definitions

Expand the report names in this section to see descriptions of the analytics and downloadable reports from the Dashboard’s [Billing overview](https://dashboard.stripe.com/billing).

### Revenue

### Monthly Recurring Revenue (MRR)

### MRR growth

### Usage

### Aggregate usage

### Usage revenue

### Subscribers

### Active subscribers

### Active subscriber growth

### New subscribers

### Average revenue per user (ARPU)

### Subscriber lifetime value (LTV)

### Trials

### New trials

### Trial conversion rate

### Churn

### Subscriber churn rate

### Churned revenue

### Retention by cohort
