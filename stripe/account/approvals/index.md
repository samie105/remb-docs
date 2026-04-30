---
title: "Set up two-party approvals"
source: "https://docs.stripe.com/account/approvals"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:38:02.777Z"
content_hash: "b82ad1d5c24b1b85558e737b8aa5a9376b491941e6315dd2735b9a9df2b79945"
---

Approvals lets admins require a second person to review sensitive actions before they take effect. Rules apply to human users acting through the Dashboard, CLI, or MCP, and to autonomous agents using [agent-tagged API keys](https://docs.stripe.com/keys#agent-keys) through the API, CLI, or MCP.

When an action triggers an approval rule, it’s paused and an approval request is created. A designated reviewer approves or denies the request. Approved actions are completed automatically; denied actions are discarded with no changes made.

## Interested in two-party approvals?

Enter your email and we'll reach out if you're eligible for the private preview.

## Supported actions

You can require approval for the following actions:

*   Bank account is added or updated
*   Bank account is deleted
*   Payment intent is created
*   Invoice is created
*   Refund is created
*   Subscription is created
*   Subscription is cancelled

## Create an approval rule

1.  Go to **Settings** > [Approvals](https://dashboard.stripe.com/settings/approvals/rules).
2.  Click **Create rule**, then select the action that triggers the approval.
3.  Optionally, click **Add condition** to add one or more trigger conditions. For example, require approval for a refund only if the amount exceeds a threshold. If you add multiple conditions, you can choose whether to combine them with `and` or `or`.
4.  Set the control:
    *   **Require approval**: The action is paused until a reviewer approves it.
    *   **Block**: The action is rejected outright.
5.  Choose **who can review requests**: specific team members, or anyone with the Administrator or Super Administrator role.
6.  Optionally, enter a **name** for the rule.
7.  Click **Activate** to save and enable the rule immediately, or **Save changes** to save it as inactive.

You can activate, deactivate, or delete rules at any time from the Approvals settings page. Only one active rule can apply to a given action.

## Handle API requests that require two-party approval

When an agent-tagged API key attempts an action that triggers an approval rule, Stripe blocks the request and returns an `approval_required` error containing a pending `approval_request` object. The agent must decide how to proceed.

### Receive the error

`stripe refunds create \   --charge=ch_1NirD82eZvKYlo2CIvbtLWuY`

`{   "error": {     "code": "approval_required",     "type": "invalid_request_error",     "message": "This action requires approval before it can be completed. An approval request (apreq_test_61UTlnIc6qlJSHVBD16TkRqlEkSQ55yeUApuueFJIDCS) has been automatically generated but has not been submitted. To proceed, submit the request for review via POST /v2/core/approval_requests/apreq_test_61UTlnIc6qlJSHVBD16TkRqlEkSQ55yeUApuueFJIDCS/submit — if approved, it will automatically execute.",     "approval_request": {       "id": "apreq_test_61UTlnIc6qlJSHVBD16TkRqlEkSQ55yeUApuueFJIDCS",       "object": "approval_request",       "action": "create_refund",       "status": "pending",       "dashboard_url": "[https://dashboard.stripe.com/approval_requests/apreq_test_61UTlnIc6qlJSHVBD16TkRqlEkSQ55yeUApuueFJIDCS](https://dashboard.stripe.com/approval_requests/apreq_test_61UTlnIc6qlJSHVBD16TkRqlEkSQ55yeUApuueFJIDCS)",       "expires_at": "2026-03-10T19:00:00Z"     }   } }`

### Respond to the request

The agent can either submit the request for manual review, or, if the action isn’t required, ignore it. Submitted requests appear in the Dashboard under **Settings > Approvals > [Requests](https://dashboard.stripe.com/settings/approvals/requests)**. Unsubmitted approval requests expire automatically after 24 hours.

#### Note

Agent-tagged API keys must have the `approval_requests.write` permission to submit an approval request.

To submit a request:

`curl -X POST https://api.stripe.com/v2/core/approval_requests/apreq_1R4kXn2eZvKYlo2C/submit \  -H "Authorization: Bearer` 

`sk_test_REDACTED`

`" \  -H "Stripe-Version: 2026-04-22.preview" \   --json '{     "reason": "Customer support request for Jenny Rosen"   }'`

## Review approval requests

Designated reviewers can approve or deny requests [on the Requests page](https://dashboard.stripe.com/settings/approvals/requests) in the Dashboard. Use the filters to view requests by status, then click a request to view its details and respond.

When a request is approved, the action completes automatically. When a request is denied, no changes are made. A user can’t approve their own request.

## Monitor approval activity

Approval events appear in [Security history](https://dashboard.stripe.com/settings/security_history) under **Settings** > **Team and security**. The following events are logged:

*   Approval rule created, updated, activated, deactivated, or deleted
*   Approval request created
*   Approval request approved or denied

You can also view API requests where approval was required from [Logs in Workbench](https://dashboard.stripe.com/workbench/logs). Click an API request to view it.

## Webhooks and events

Because approval requests are reviewed asynchronously, you might want to create a webhook to listen for an event once an approval request is approved (`v2.core.approval_request.approved`) or rejected (`v2.core.approval_request.rejected`). If you no longer need an approval request to be reviewed, you can cancel it, which generates a `v2.core.approval_request.canceled` event.

After approval, requests are auto-executed, and emit either `v2.core.approval_request.succeeded` or `v2.core.approval_request.failed`.
