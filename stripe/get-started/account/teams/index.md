---
title: "Start a team"
source: "https://docs.stripe.com/get-started/account/teams"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:43:52.932Z"
content_hash: "a4d5ca51ef3990a218fa0d88b1de7cb48c70640227a8ce9fb29f0d12487e6562"
---

## Learn how to invite and interact with team members.

To invite new team members:

1.  Go to the [Team](https://dashboard.stripe.com/settings/team) tab in the Dashboard.
2.  Click **Add member**.
3.  Add one or more email addresses, separated by a space or comma. Adding users together allows you to assign them all the same roles and access simultaneously.
4.  Select which roles to assign. Users can hold multiple roles within the same account. Review the [list of actions](https://docs.stripe.com/get-started/account/teams/roles) that each role can and can’t perform before assigning the role to a team member. Grant the lowest permission required by the user to perform their job.
5.  After completing the role assignment for all the accounts, review the configuration, and click **Send invites** to email the specified users with the steps to accept the invitation.

Invites to your Stripe account expire after 10 days.

After a team member accepts their invite, you can edit their role at any time from your [Team](https://dashboard.stripe.com/settings/team) settings. To edit a team member’s role, click the overflow menu (), then click **Edit**.

## Mention team members

You can mention team members when you add a note to a payment. If you mention a team member, they receive an email notification with the note and a link to the associated payment.

## Receive email notifications

You can configure email notifications under **Communication preferences** in your [Personal details](https://dashboard.stripe.com/settings/user) settings, and apply them on a per-user basis. If your team members also want to receive notifications, they must customize their own settings. Stripe sends email notifications to you when any of the following events occur:

*   A successful payment is received.
*   An [application fee](https://docs.stripe.com/connect/direct-charges#collect-fees) is collected from a connected account.
*   A payment is [disputed](https://docs.stripe.com/disputes) by a customer.
*   A payment is marked as [elevated risk](https://docs.stripe.com/radar/risk-evaluation#elevated-risk) by Stripe or a custom [Stripe Radar](https://docs.stripe.com/radar) rule.
*   You’re mentioned in a note.
*   A customer sends an incorrect amount to pay their [invoice](https://docs.stripe.com/invoicing).
*   A [webhook](https://docs.stripe.com/webhooks) delivery fails.

For a full list of notification events, go to your **Communication preferences** under **Profile**.

### Automate email notifications

Use [Stripe Workflows](https://docs.stripe.com/workflows) to automate sending emails to your team. Workflows allows you to use a visual builder in the Stripe Dashboard to automate tasks that require multi-step processes that depend on conditional logic.

Workflows is also compatible with most Stripe products such as, but not limited to:

*   [Online payments](https://docs.stripe.com/payments/online-payments)
*   [Disputes](https://docs.stripe.com/disputes)
*   [Invoicing](https://docs.stripe.com/invoicing)
*   [Billing](https://docs.stripe.com/billing)
*   [Radar](https://docs.stripe.com/radar)

To learn how it works, [set up a test workflow](https://docs.stripe.com/workflows/set-up) and review our [example use cases](https://docs.stripe.com/workflows/use-cases).
