---
title: "Access management"
source: "https://redis.io/docs/latest/operate/rc/security/access-control/access-management/"
canonical_url: "https://redis.io/docs/latest/operate/rc/security/access-control/access-management/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:11.703Z"
content_hash: "6789499d3ef1e5acdf5f81e041cab1cf79f20e5be3f449692ef67b21cd2e198c"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Security","→","Security","→\n      \n        Access control","→","Access control","→\n      \n        Access management","→","Access management"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Security","→","Security","→\n      \n        Access control","→","Access control","→\n      \n        Access management","→","Access management"]
nav_prev: {"path": "../index.md", "title": "Access control"}
nav_next: {"path": "../data-access-control/default-user/index.md", "title": "Default user"}
---

# Access management

Control who can make changes to your databases using the Redis Cloud console.

Redis Cloud

The **Access management** screen helps you manage:

*   The team of users allowed to access your subscription and its databases.
*   The API keys that authenticate application access to your account.
*   [Single sign-on (SSO) with SAML](/docs/latest/operate/rc/security/access-control/saml-sso/).

Here, you learn how to manage your team's users and control their level of access.

For help managing API keys, see [Manage API keys](/docs/latest/operate/rc/api/get-started/manage-api-keys/).

## Manage team access

The **Team** tab lets you manage the people allowed to access your account. Each authorized person is assigned to a role that specifies their privileges.

[![The Access management tab helps you manage the people allowed to access your subscription.](/docs/latest/images/rc/access-management-team-tab.png)](/docs/latest/images/rc/access-management-team-tab.png)

The list contains one entry summarizing the team settings for each user in your team. By default, the list includes the account owner.

The list includes several buttons and icons to help you manage the list:

Icon

Description

[![Use the Add button to add members to your team.](/docs/latest/images/rc/icon-add.png#no-click)](/docs/latest/images/rc/icon-add.png#no-click)

The **Add** button lets you add members to your team

[![Use the Edit button change details for a team member.](/docs/latest/images/rc/icon-edit.png#no-click)](/docs/latest/images/rc/icon-edit.png#no-click)

The **Edit** button lets you edit the settings for the selected team member

[![Use the Delete button to remove a member from your team.](/docs/latest/images/rc/icon-delete-teal.png#no-click)](/docs/latest/images/rc/icon-delete-teal.png#no-click)

The **Delete** button lets you remove members from your team

 [![The Sort ascending button displays members in ascending order according to the values of the selected field.](/docs/latest/images/rc/icon-list-sort-asc.png#no-click)](/docs/latest/images/rc/icon-list-sort-asc.png#no-click)[![The Sort descending button displays members in descending order according to the values of the selected field.](/docs/latest/images/rc/icon-list-sort-desc.png#no-click)](/docs/latest/images/rc/icon-list-sort-desc.png#no-click)

The **Sort ascending** and **Sort descending** icons display the list according to the selected order

You can also use the list search to find a specific user or filter by **Role**, **User Type**, or **Options**.

### Add user

When you add a member to your team, the **Add user** dialog appears.

[![Use the Add User dialog to specify the details for your new user.](/docs/latest/images/rc/access-mgmt-add-user-dialog.png)](/docs/latest/images/rc/access-mgmt-add-user-dialog.png)

Use the dialog to specify these values.

Setting

Description

**First name**

First name of the user displayed in the Redis Cloud console and in email messages

**Last name**

Last name of the user displayed in the Redis Cloud console and in email messages

**Role**

The role identifies their subscription and account privileges. For details, see [Team management roles](#team-management-roles).

**Email**

The address used for alerts and other email messages regarding the account

**Alert emails**

Enable to be notified when subscription databases cross certain thresholds, such as exceeding memory limits or latency requirements

**Operational emails**

Notifications about subscription and database changes, such as creating or deleting a database, and [subscription and database maintenance](/docs/latest/operate/rc/subscriptions/maintenance/)

**Billing emails**

Notifications about billing, such as when bills are issued and paid

**Multi-factor authentication**

Whether MFA is enabled for the member. This is deactivated when members have not enabled or confirmed MFA in their user profile settings.

Use the **Add user** button to save your new team member details.

Redis will send an activation email to the user once their details are saved. After following the activation link, they can sign in.

### Edit user

To edit user team details, select the user from the list and then select the **Edit** button. The **Edit user** dialog displays the details you can change.

[![Use the Edit User dialog to change the details for a user](/docs/latest/images/rc/access-mgmt-edit-user-dialog.png)](/docs/latest/images/rc/access-mgmt-edit-user-dialog.png)

You can change any detail except the team member's email address.

Select **Save user** to save your changes.

### Delete user

To remove a member from your team, select them from the list and then select the **Delete** button. A confirmation dialog appears.

[![Confirm that you want to remove a user from your team](/docs/latest/images/rc/access-management-delete-user-dialog.png)](/docs/latest/images/rc/access-management-delete-user-dialog.png)

Select **Delete user** to confirm removal. This is a permanent action that cannot be undone.

## Team management roles

Each team member is assigned a role that identifies their privileges and limits their activities in the Redis Cloud console.

Roles and responsibilities are:

*   **Owner** can view, create, and edit any settings in the account.
    
    Each subscription must have at least one account owner. Accounts can have multiple owners.
    
    Owners can also manage subscriptions, databases, and API keys.
    
*   **Billing Admin** can view and edit settings related to billing and payments.
    
    Billing Admins can add and remove payment methods and change the payment method for a subscription, but they cannot change any other subscription or database settings.
    
*   **Manager** can view, create, and edit any setting in the subscription.
    
    Managers can change subscription costs and change payment methods associated with a subscription, but they cannot add or remove available payment methods.
    
*   **Member** can view, create, and edit databases in ways that do not impact costs.
    
    Members cannot create databases or edit databases in ways that impact costs.
    
*   **Viewer** can view all databases and their configurations, including database secrets.
    
*   **Logs viewer** can not access the Redis Cloud console. They are only allowed access to the [Redis Cloud API](/docs/latest/operate/rc/api/) [`GET logs/`](/docs/latest/operate/rc/api/api-reference/#tag/Account/operation/getAccountSystemLogs) endpoint.
    

This table shows each role's ability to perform common tasks.

**Task**

**Owner**

**Billing Admin**

**Manager**

**Member**

**Viewer**

**Logs Viewer**

Access management

✅ Yes

❌ No

❌ No

❌ No

❌ No

❌ No

Account settings

✅ Yes

✅ Yes[1](#table-note-1)

❌ No

❌ No

❌ No

❌ No

Billing & payments

✅ Yes

✅ Yes

❌ No[4](#table-note-4)

❌ No

❌ No

❌ No

Create subscription

✅ Yes

❌ No

✅ Yes

❌ No

❌ No

❌ No

Edit subscription

✅ Yes

✅ Yes[2](#table-note-2)

✅ Yes

❌ No

❌ No

❌ No

Create database (affects cost)

✅ Yes

❌ No

✅ Yes

❌ No

❌ No

❌ No

Edit database (affects cost)

✅ Yes

❌ No

✅ Yes

❌ No

❌ No

❌ No

Create database (no cost impact)

✅ Yes

❌ No

✅ Yes

❌ No

❌ No

❌ No

Edit database (no cost impact)

✅ Yes

❌ No

✅ Yes

✅ Yes

❌ No

❌ No

View subscription

✅ Yes

✅ Yes

✅ Yes

✅ Yes

✅ Yes

❌ No

View database

✅ Yes

✅ Yes[3](#table-note-3)

✅ Yes

✅ Yes

✅ Yes

❌ No

Use the [REST API](/docs/latest/operate/rc/api/)

✅ Yes

❌ No

❌ No

❌ No

✅ Yes[5](#table-note-5)

✅ Yes[6](#table-note-6)

1.  Billing Admins can only edit the account billing address in Account Settings.
    
2.  Billing Admins can only change the payment method when editing a subscription.
    
3.  Billing Admins can see the list of databases, but can not see database details, including connection details.
    
4.  Managers are able to view existing payment methods and assign them as payment methods for subscriptions, but they cannot add or remove payment methods.
    
5.  Viewers can use the REST API for GET requests, but cannot modify subscription or database details.
    
6.  Logs viewers can only use the [`GET logs/`](/docs/latest/operate/rc/api/api-reference/#tag/Account/operation/getAccountSystemLogs) endpoint of the REST API.
    

## On this page
