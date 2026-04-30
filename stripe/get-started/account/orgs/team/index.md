---
title: "Manage access to your organization"
source: "https://docs.stripe.com/get-started/account/orgs/team"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:42:54.339Z"
content_hash: "ca601ef5411e013ac0fd15e3842103c5558bc8c74252a51f86f2e229540d2520"
---

You can manage your organization’s team member permission levels from your [Team and security](https://dashboard.stripe.com/org/settings/team) settings. Administrators can:

*   Add members to or remove them from an organization or its accounts.
*   View all members across an organization or account.
*   Change the [user roles](https://docs.stripe.com/get-started/account/teams/roles) assigned to any member.
*   Invite up to ten users to a given role.
*   Manage two-factor (2FA) authentication settings for a member or the entire account.
*   View the security history of all members.

## Organization versus account roles

You can assign users access to your entire organization or individual accounts within your organization. Organization-level roles grant users access to all accounts within the organization, including the organization itself. Account-level roles let users access a specific account with the assigned role.

A user can have roles at both the organization and account levels. However, organization-level roles are automatically inherited at the account level. For example, you can’t give someone admin rights for the organization but view-only access for an account within that organization. Conversely, you can assign admin rights for a specific account without granting organization-level admin access.

*   **Manage your organization’s team members**: Manage user access and roles for specific accounts under the organization’s [Team](https://dashboard.stripe.com/org/settings/team) tab. You can also manage team members by granting access to multiple accounts simultaneously or providing access to the entire organization. You can only access this page if you have an organization-level role.
    
*   **Manage an account’s team members**: Add, remove, and edit team members of an account, and update the roles of users associated with that account under the account’s [Team](https://dashboard.stripe.com/settings/team) tab.
    

For example, assume you have three accounts: Banking, Finance, and Consulting. In this case, organization- and account-level roles work as follows:

*   **Organization-level role**: Assign a user the IAM Administrator role to grant that role in all three accounts and the organization itself. This provides access to team management for all three accounts and organization-level team management.
    
*   **Account-level role**: Assign a user the IAM Administrator role in the Banking account to limit their access to the IAM role within that account. They can manage account-level teams only within the Banking account. This role doesn’t grant access to other accounts or organization-level team management.
    

## Create API keys

Configure [organization API keys](https://docs.stripe.com/keys#organization-api-keys) so your team members can make API requests for any account within the organization.

## Update your organization

You can view all of your organization’s team members under the [Team](https://dashboard.stripe.com/org/settings/team) tab. Additionally, you can:

*   Invite new members.
*   Edit members.
*   Grant members access to one or more additional accounts.
*   Remove members from your organization.

You add, remove, and edit team members using the following processes from either the organization or account Dashboard. The only difference is that the account Dashboard only shows actions available for that specific account.

### Add a team member

To add new team members:

1.  Navigate to the [Team](https://dashboard.stripe.com/org/settings/team) tab.
    
2.  Click **Add member**.
    
3.  Add one or more email addresses, separated by space or comma. Adding users together allows you to assign them all the same roles and access simultaneously.
    
4.  Select which roles to assign. Users can hold multiple roles within the same account.
    
5.  Select which accounts to apply the selected roles to.
    
    *   Select one or more accounts to grant the role permissions only in those accounts.
    *   Select the organization to grant the role permissions for the organization and all accounts within the organization. Grant the lowest permission required by the user because you can still grant different roles at the individual account level.
6.  Click **Assign additional roles** to choose different roles to assign for other accounts.
    
7.  After completing the role assignment for all the accounts, review the configuration, and click **Send invites** to email the specified users with the steps to accept the invitation.
    

### Remove a team member

To remove an existing team member:

1.  Navigate to the [Team](https://dashboard.stripe.com/org/settings/team) tab.
    
2.  Click the overflow menu () in the user’s row to remove them. You can also click **Remove member** in the user’s profile.
    
3.  After you remove a user, they immediately lose access to the organization.
    

### Edit a team member’s access

To edit an existing team member’s access:

1.  Navigate to the [Team](https://dashboard.stripe.com/org/settings/team) tab.
    
2.  Click the user’s profile from the list of team members.
    
3.  Click **Manage roles**.
    
4.  In the overflow menu () next to the user’s role, click **Edit**. In the **Manage roles** drawer, you can also remove or add user roles.
    
5.  Select the accounts where you want this user to have these new roles. You can add new accounts, remove accounts, or grant organization-level access.
    

### View all team members

To view all team members within an organization, go to the [Team](https://dashboard.stripe.com/org/settings/team) tab. From here, you can also export the entire user table as a **CSV** file, and filter by:

*   Account
*   Roles
*   Status
*   Name
*   Email

## Authenticate team members

Stripe supports 2FA through passkeys, security keys (including TouchID), authenticator apps, and SMS. We recommend passkeys or security keys because they’re resistant to phishing. SMS-based 2FA is vulnerable to SIM-swapping and interception, so use it only as a last resort. Require all team members to register for 2FA. If you use [single sign-on (SSO)](https://docs.stripe.com/get-started/account/sso), you can enforce authentication policies centrally through your identity provider.

### Require 2FA for all users

Only an organization Administrator or Super Administrator can require 2FA for all team members.

1.  Navigate to the [User authentication](https://dashboard.stripe.com/org/settings/security/authentication) tab.
    
2.  Enable **Require two-step authentication for all team members**.
    

After you enable this option, all users must register a 2FA device during their next login. This requires them to complete a 2FA challenge during subsequent login attempts.

### Reset 2FA for a single user

If a single user loses access to their 2FA devices, an Administrator or Super Administrator must reset that user’s 2FA settings from the account level:

1.  Navigate to the account’s [Team](https://dashboard.stripe.com/settings/team) tab.
    
2.  Click the affected user’s profile.
    
3.  Click **Reset two-factor authentication**.
    

Stripe sends an email to the affected user’s registered email address with instructions on how they can reset their 2FA devices. You can’t do this by going to the user’s profile at the organization level.

## View your security history

To view your organization’s security history, go to the [Security history](https://dashboard.stripe.com/settings/org/security/history) tab. Here, you can filter your security history by date or action. The **Action** filter includes hundreds of actions across different categories, including **User security**, **Team**, **API**, and a number of Stripe products. You can also export your entire security history as a **CSV** file.
