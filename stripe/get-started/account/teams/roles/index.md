---
title: "User roles"
source: "https://docs.stripe.com/get-started/account/teams/roles"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:43:33.836Z"
content_hash: "a84923dd383e2454cd3693eb0cdfc74511d3f364acb588363828aedc3d995646"
---

## Give team members controlled access to your Stripe account.

#### Note

If you assign a user multiple roles, they’re assigned all the permissions of each individual role. Be cautious of conflicts and unintended authority.

##### Administrator

This role is for anyone who needs similar access as the account owner—they can see and manage almost everything.

They can't delete the default bank account, or change the account owner.

##### IAM Administrator

The Identity and Access Management (IAM) Admin role is for people who need to invite team members and assign roles. They can also remove any user, including Administrators and Super Administrators.

They can't do anything beyond access management. They also can't assign a user to the Administrator or Super Administrator role.

##### Super Administrator

This role is assigned to the creator of a business account and should only be assigned to users who are allowed to perform all privileged actions. Only a Super Administrator can assign the Super Administrator role to other team members.

Change the account owner (only the owner can transfer ownership).

Important

These roles can invite additional users to your account, and if compromised by an attacker would allow them to invite users under their control.

Account owner

An Account Owner is a special type of Administrator that can perform all actions, including closing the account. There can only be one Owner for an account. To change the Account Owner, please refer to [this guide](https://support.stripe.com/questions/change-the-owner-of-a-stripe-account).

Connect roles

These roles are only available if you use [Connect](https://docs.stripe.com/connect)

##### Connect Onboarding Analyst

This role is for people who need to create connected accounts and edit their identity information.

They can't do anything on the platform account except view and edit connected accounts.

connect\_onboarding\_analyst

##### Transfer Analyst

Your account must require [two-step authentication](https://support.stripe.com/questions/two-step-authentication-requirement) in order to allow non-Administrators with this role to transfer funds.

This role is for people who need to transfer funds to connected accounts and view the platform’s balance and historical payouts. They can also view disputes and charges.

They can't resolve disputes, refund or create payments, pay out money to external bank accounts, add or edit bank accounts, or create new connected accounts.

##### Developer

This role is for developers who need to set up a Stripe integration. This role has access to the secret key, which grants access to almost all API resources.

They can't invite team members or change the account owner.

Identity roles

These roles are only available if you use [Identity](https://docs.stripe.com/identity)

##### Identity Analyst

This role is for Identity users who need to create, review, cancel, or redact verifications.

This role can’t edit verifications for connected accounts.

##### Identity View Only

This role is for Identity users who need to view verification data.

This role can’t create, review, cancel, or redact verifications.

##### Analyst

This role is for people who need to pay out money, refund payments, and export data.

They can't edit payout schedules or account settings.

##### Dispute Analyst

This role is for people who need need to view, submit evidence for, and accept disputes.

They can't do anything that's not related to disputes.

##### Refund Analyst

This role is for people who need to refund payments and issue credit notes on invoices.

They can’t create payments, view balance, or view connected accounts.

##### Data Migration Specialist

This role is for people who need to perform data migrations (copy, import, export) for their account.

They can't create connected accounts, transfer funds, payout money, or edit any account and product settings.

data\_migration\_specialist

##### Support Associate

This role is for people who need to refund payments and resolve disputes, but should not have the ability to edit products. It has administration permissions for connected accounts, where it can edit the payout schedule, update the legal entity, update the bank account, and more.

They can't create connected accounts, transfer funds, payout money, or edit any account or product settings.

##### Support Communications

This role is for people who need to authenticate email support cases, use Support Center to view and respond to support cases, or share files securely with Stripe.

They can’t access financial information, transfer funds, access or edit connected accounts, or edit any account and product settings.

##### Support Specialist

This role is for people who need to refund payments, resolve disputes, and may need to update products. It has administration permissions for connected accounts, where it can edit the payout schedule, update the legal entity, and more. This role can add, edit, and delete products.

They can't create connected accounts, transfer funds, payout money, or edit any account settings.

##### Terminal Specialist

This role is for people who need to manage their Terminal fleet. They can register readers, manage locations, place hardware orders, and deploy software to Terminal devices.

They can't view or manage payments, products, or customers. They also can't configure payment methods or other product settings.

Tax form roles

These roles are only available if you use [1099s](https://docs.stripe.com/connect/tax-reporting)

##### Tax Analyst

This role is for people who need to configure tax form settings, file tax forms for connected accounts, and export data.

They can't create connected accounts, transfer funds, payout money, or edit account and non-Tax product settings.

##### View Only

This role is for people who need to view payments, balance, and connected accounts, but can’t edit any of them. This role can also export data and download reports.

They can't create connected accounts, transfer funds, payout money, or edit any account and product settings.

##### Accountant

This role is for accountants who need to access Stripe Revenue Recognition and its features for monthly bookkeeping. The accountants can set up a custom chart of accounts, create accounting rules and modify revenue amortisation settings. They can also view payments, balance, invoices, customers, and connected accounts, etc., but can’t edit any of them.

They can't create connected accounts, transfer funds, payout money, choose pricing plans, or edit any account and other product settings including signing-up or canceling Stripe Revenue Recognition.

##### Top-up Specialist

This role gives access to the Top-ups feature, including creating, viewing, and updating top-ups, as well as viewing balance and payouts. Accountants or Financial employees may find this useful.

They can't access any other Stripe features.

##### Financial Connections Specialist

This role gives access to Financial Connections operations, including viewing and editing Financial Connections settings, registration and objects, with limited customer read access.

They can't access any other Stripe features.

financial\_connections\_specialist

##### Data Engineer

This role is for Stripe Data Pipeline users who need to setup and manage data pipelines.

They will not have access to other parts of the Dashboard other than Stripe Data Pipeline.
