---
title: "Access Control"
source: "https://supabase.com/docs/guides/platform/access-control"
canonical_url: "https://supabase.com/docs/guides/platform/access-control"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:56.986Z"
content_hash: "c0efa5582dbb2af2e1a6753867ba8c67004435c68f484e41f110ad5f9c70914d"
menu_path: ["Platform","Platform","Project & Account Management","Project & Account Management","Access Control","Access Control"]
section_path: ["Platform","Platform","Project & Account Management","Project & Account Management","Access Control","Access Control"]
nav_prev: {"path": "supabase/docs/guides/local-development/seeding-your-database/index.md", "title": "Seeding your database"}
nav_next: {"path": "supabase/docs/guides/platform/aws-marketplace/index.md", "title": "AWS Marketplace"}
---

# 

Access Control

* * *

Supabase provides granular access controls to manage permissions across your organizations and projects.

For each organization and project, a member can have one of the following roles:

*   **Owner**: full access to everything in organization and project resources.
*   **Administrator**: full access to everything in organization and project resources **except** updating organization settings, transferring projects outside of the organization, and adding new owners.
*   **Developer**: read-only access to organization resources and content access to project resources but cannot change any project settings.
*   **Read-Only**: read-only access to organization and project resources.

Read-Only role is only available on the [Team and Enterprise plans](/pricing).

When you first create an account, a default organization is created for you and you'll be assigned as the **Owner**. Any organizations you create will assign you as **Owner** as well.

## Manage organization members[#](#manage-organization-members)

To invite others to collaborate, visit your organization's team [settings](/dashboard/org/_/team) to send an invite link to another user's email. The invite is valid for 24 hours. For project scoped roles, you may only assign a role to a single project for the user when sending the invite. You can assign roles to multiple projects after the user accepts the invite.

Invites sent from a SAML SSO account can only be accepted by another SAML SSO account from the same identity provider.

This is a security measure to prevent accidental invites to accounts not managed by your enterprise's identity provider.

### Viewing organization members using the Management API[#](#viewing-organization-members-using-the-management-api)

You can also view organization members using the Management API:

```
1# Get your access token from https://supabase.com/dashboard/account/tokens2export SUPABASE_ACCESS_TOKEN="your-access-token"3export ORG_ID="your-organization-id"45# List organization members6curl "https://api.supabase.com/v1/organizations/$ORG_ID/members" \7  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN"
```

### Transferring ownership of an organization[#](#transferring-ownership-of-an-organization)

Each Supabase organization must have at least one owner. If your organization has other owners then you can relinquish ownership and leave the organization by clicking **Leave team** in your organization's team [settings](/dashboard/org/_/team).

Otherwise, you'll need to invite a user as **Owner**, and they need to accept the invitation, or promote an existing organization member to **Owner** before you can leave the organization.

### Organization scoped roles vs project scoped roles[#](#organization-scoped-roles-vs-project-scoped-roles)

Project scoped roles are only available on the [Team and Enterprise plans](/pricing).

Each member in the organization can be assigned a role that is scoped either to the entire organization or to specific projects.

*   If a member has an organization-level role, they will have the corresponding permissions across all current and future projects within that organization.
*   If a member is assigned a project-scoped role, they will only have access to the specific projects they've been assigned to. They will not be able to view, access, or even see other projects within the organization on the Supabase Dashboard.

This allows for more granular control, ensuring that users only have visibility and access to the projects relevant to their role.

### Organization permissions across roles[#](#organization-permissions-across-roles)

The table below shows the actions each role can take on the resources belonging to the organization.

Resource

Action

Owner

Administrator

Developer

Read-Only[1](#user-content-fn-1)

[**Organization**](#org-permissions)

Organization Management

Update

Delete

OpenAI Telemetry Configuration[2](#user-content-fn-2)

Update

[**Members**](#member-permissions)

Organization Members

List

Owner

Add

Remove

Administrator

Add

Remove

Developer

Add

Remove

Owner (Project-Scoped)

Add

Remove

Administrator (Project-Scoped)

Add

Remove

Developer (Project-Scoped)

Add

Remove

Invite

Revoke

Resend

Accept[3](#user-content-fn-3)

[**Billing**](#billing-permissions)

Invoices

List

Billing Email

View

Update

Subscription

View

Update

Billing Address

View

Update

Tax Codes

View

Update

Payment Methods

View

Update

Usage

View

[**Integrations (Org Settings)**](#org-integration-permissions)

Authorize GitHub

\-

Add GitHub Repositories

\-

GitHub Connections

Create

Update

Delete

View

Vercel Connections

Create

Update

Delete

View

[**OAuth Apps**](#oauth-permissions)

OAuth Apps

Create

Update

Delete

List

[**Audit Logs**](#audit-permissions)

View Audit logs

\-

[**Legal Documents**](#legal-docs-permissions)

SOC2 Type 2 Report

Download

Security Questionnaire

Download

### Project permissions across roles[#](#project-permissions-across-roles)

The table below shows the actions each role can take on the resources belonging to the project.

Resource

Action

Owner

Admin

Developer

Read-Only[4](#user-content-fn-4)[5](#user-content-fn-6)

[**Project**](#project-permissions)

Project Management

Transfer

Create

Delete

Update (Name)

Pause

Restore

Restart

Custom Domains

View

Update

Data (Database)

View

Manage

[**Infrastructure**](#infrastructure-permissions)

Read Replicas

List

Create

Delete

Add-ons

Update

[**Integrations**](#proj-integrations-permissions)

Authorize GitHub

\-

Add GitHub Repositories

\-

GitHub Connections

Create

Update

Delete

View

Vercel Connections

Create

Update

Delete

View

[**Database Configuration**](#database-config-permissions)

Reset Password

\-

Pooling Settings

View

Update

SSL Configuration

View

Update

Disk Size Configuration

View

Update

Network Restrictions

View

Create

Delete

Network Bans

View

Unban

[**API Configuration**](#api-config-permissions)

API Keys

Read service key

Read anon key

JWT Secret

View

Generate new

API settings

View

Update

[**Auth Configuration**](#auth-config-permissions)

Auth Settings

View

Update

SMTP Settings

View

Update

Advanced Settings

View

Update

[**Storage Configuration**](#storage-config-permissions)

Upload Limit

View

Update

S3 Access Keys

View

Create

Delete

[**Edge Functions Configuration**](#edge-config-permissions)

Secrets

View

[6](#user-content-fn-5)

Create

Delete

[**SQL Editor**](#sql-editor-permissions)

Queries

Create

Update

Delete

View

List

Run

[7](#user-content-fn-7)

[**Database**](#database-permissions)

Scheduled Backups

View

Download

Restore

Physical backups (PITR)

View

Restore

[**Authentication**](#auth-permissions)

Users

Create

Delete

List

Send OTP

Send password recovery

Send magic link

Remove MFA factors

Providers

View

Update

Rate Limits

View

Update

Email Templates

View

Update

URL Configuration

View

Update

Hooks

View

Create

Delete

[**Storage**](#storage-permissions)

Buckets

Create

Update

Delete

View

List

Files

Create (Upload)

Update

Delete

List

[**Edge Functions**](#edge-permissions)

Edge Functions

Update

Delete

View

List

[**Reports**](#proj-reports-permissions)

Custom Report

Create

Update

Delete

View

List

[**Logs & Analytics**](#proj-logs-permissions)

Queries

Create

Update

Delete

View

List

Run

[**Branching**](#branching-permissions)

Production Branch

Read

Write

Development Branches

List

Create

Update

Delete

## Footnotes[#](#footnote-label)

1.  Available on the Team and Enterprise Plans. [↩](#user-content-fnref-1)
    
2.  Sending anonymous data to OpenAI is opt in and can improve Studio AI Assistant's responses. [↩](#user-content-fnref-2)
    
3.  Invites sent from a SSO account can only be accepted by another SSO account coming from the same identity provider. This is a security measure that prevents accidental invites to accounts not managed by your company's enterprise systems. [↩](#user-content-fnref-3)
    
4.  Available on the Team and Enterprise Plans. [↩](#user-content-fnref-4)
    
5.  Listed permissions are for the API and Dashboard. [↩](#user-content-fnref-6)
    
6.  Read-Only role is able to access secrets. [↩](#user-content-fnref-5)
    
7.  Limited to executing SELECT queries. SQL Query Snippets run by the Read-Only role are run against the database using the **supabase\_read\_only\_user**. This role has the [predefined Postgres role pg\_read\_all\_data](https://www.postgresql.org/docs/current/predefined-roles.html). [↩](#user-content-fnref-7)

