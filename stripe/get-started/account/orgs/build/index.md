---
title: "Build an organization"
source: "https://docs.stripe.com/get-started/account/orgs/build"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:41:35.898Z"
content_hash: "ba4f8f80eaaf3e8ea4f82b0ac3a543f5097a84b27720cabed37356882445cde8"
---

Create an organization, managing your accounts from a single location in the Stripe Dashboard. After you create an organization, you can invite additional team members to [access your organization](https://docs.stripe.com/get-started/account/orgs/team) by navigating to your [Team and security](https://dashboard.stripe.com/org/settings/team) settings.

## Before you begin

*   The person who creates the organization must be a [Super Administrator](https://docs.stripe.com/get-started/account/teams/roles) in each account added to the organization. Stripe automatically assigns this role to the account owner, who can assign the Super Administrator role to the organization creator, if it’s a different person. If an account’s owner leaves, you can [request an ownership transfer](https://support.stripe.com/questions/change-the-owner-of-a-stripe-account).
    
*   You must [Consolidate the IdPs](https://docs.stripe.com/get-started/account/orgs/sso) of any accounts with SSO enabled before you add them to the organization.
    

## Create an organization

To create an organization from one of your Stripe accounts:

1.  Navigate to the account picker in the Dashboard.
    
2.  Select **Create**, and then click [Create organization](https://dashboard.stripe.com/org-creation).
    
3.  Enter a name for your organization.
    
4.  Select the accounts you want to add to the organization. You can add up to 75 accounts.
    
5.  Agree to the [Terms of Service](https://stripe.com/legal/organizations).
    
6.  Click **Create**.
    

## Manage SSO behavior

After you create an organization, [SSO](https://docs.stripe.com/get-started/account/sso) configuration for all accounts transfers to the organization. You must update your identity provider (IdP) to assign roles through the organization and consolidate account SSO management under the organization’s IdP.

1.  Obtain your `org_id` from your [organization management settings](https://dashboard.stripe.com/org/settings/org) in the Dashboard.
2.  Add or update your IdP attribute statement to use `Stripe-Role-org_id` (instead of `Stripe-Role-acct_id`) so you can assign roles in the organization.

#### Common mistake

Failure to update your SSO integration can result in restricted user access.

## Add an existing account to an organization

After you create an organization, you can add an existing account. An organization can include up to 75 accounts, and each account can belong to only one organization.

1.  Click **Add account** next to **Business accounts** on the [homepage](https://dashboard.stripe.com/org/dashboard).
    
2.  Select **Choose from existing accounts**.
    
3.  Select the accounts you want to add. If you’re a Super Administrator of an account, you can add the account to your organization directly. If you’re an Administrator of an account, you can send an invite to the Super Administrator. If you’re not sure who the Super Administrator is, check the account’s [Team settings](https://dashboard.stripe.com/settings/team). The person who created an account is automatically made a Super Administrator. India Stripe Accounts aren’t eligible at this time.
    
4.  Click **Add**.
    

## Add a new account to an organization

To add a new account to an organization:

1.  Click the account picker, then select **Create new account**.
    
2.  Select **Create a new account in your organization**.
    
3.  Add the account name, then select the country of operation.
    
4.  (Optional) Select a legal entity, business details, or payout bank account information you want to copy from existing accounts within your organization.
    
5.  Click **Create account**.
    

## Add a new account outside of an organization

To add a new account outside of an organization:

1.  Click the account picker, then select **Create new account**.
    
2.  Select **Create an account outside of your organization**.
    
3.  Add the account name, then select the country of operation.
    
4.  Click **Create**.
    

## Remove an account from an organization

To remove an account from an organization:

1.  Click the account picker, and select your organization.
    
2.  Go to [Organization management](https://dashboard.stripe.com/org/settings/org), and click the overflow menu () next to the name of the account you want to remove.
    
3.  Click **Remove from organization**.
    
4.  Make sure you assign account-level roles to any users who inherited them from the organization if you want them to continue having those permissions in the removed account.
    

You must be a [Super Administrator](https://docs.stripe.com/get-started/account/teams/roles) of the organization to remove an account. If you remove every account from an organization, Stripe permanently closes it.

#### Data pipeline effects

If you remove an account from an organization, we automatically remove the account from all [data pipelines](https://docs.stripe.com/stripe-data/access-data-in-warehouse) in the organization.
