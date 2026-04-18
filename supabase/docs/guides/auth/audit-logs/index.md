---
title: "Auth Audit Logs"
source: "https://supabase.com/docs/guides/auth/audit-logs"
canonical_url: "https://supabase.com/docs/guides/auth/audit-logs"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:07.828Z"
content_hash: "963d78d8c0ae1118c9a6b8cc7416303c0dba9d5b659cde19644d15dd528100cf"
menu_path: ["Auth","Auth","Security","Security","Audit Logs","Audit Logs"]
section_path: ["Auth","Auth","Security","Security","Audit Logs","Audit Logs"]
nav_prev: {"path": "supabase/docs/guides/auth/architecture/index.md", "title": "Auth architecture"}
nav_next: {"path": "supabase/docs/guides/auth/auth-anonymous/index.md", "title": "Anonymous Sign-Ins"}
---

# 

Auth Audit Logs

## 

Monitor and track authentication events with audit logging.

* * *

Auth audit logs provide comprehensive tracking of authentication events in your Supabase project. Audit logs are automatically captured for all authentication events and help you monitor user authentication activities, detect suspicious behavior, and maintain compliance with security requirements.

## What gets logged[#](#what-gets-logged)

Supabase auth audit logs automatically capture all authentication events including:

*   User signups and logins
*   Password changes and resets
*   Email verification events
*   Token refresh and logout events

## Storage options[#](#storage-options)

By default, audit logs are stored in two places:

1.  **Your project's Postgres database** - Stored in the `auth.audit_log_entries` table, searchable via SQL but uses database storage
2.  **External log storage** - Cost-efficient storage accessible through the dashboard

You can disable Postgres storage to reduce database storage costs while keeping the external log storage.

### Configuring audit log storage[#](#configuring-audit-log-storage)

1.  Navigate to your project’s dashboard
2.  Go to **Authentication**
3.  Find the **Audit Logs** under **Configuration** section
4.  Toggle on "Disable writing auth audit logs to project database" to disable database storage

Disabling Postgres storage reduces your database storage costs. Audit logs will still be available through the dashboard.

## Log format[#](#log-format)

Audit logs contain detailed information about each authentication event:

```
1{2  "timestamp": "2025-08-01T10:30:00Z",3  "user_id": "uuid",4  "action": "user_signedup",5  "ip_address": "192.168.1.1",6  "user_agent": "Mozilla/5.0...",7  "metadata": {8    "provider": "email"9  }10}
```

### Log actions reference[#](#log-actions-reference)

Action

Description

`login`

User login attempt

`logout`

User logout

`invite_accepted`

Team invitation accepted

`user_signedup`

New user registration

`user_invited`

User invitation sent

`user_deleted`

User account deleted

`user_modified`

User profile updated

`user_recovery_requested`

Password reset request

`user_reauthenticate_requested`

User reauthentication required

`user_confirmation_requested`

Email/phone confirmation requested

`user_repeated_signup`

Duplicate signup attempt

`user_updated_password`

Password change completed

`token_revoked`

Refresh token revoked

`token_refreshed`

Refresh token used to obtain new tokens

`generate_recovery_codes`

MFA recovery codes generated

`factor_in_progress`

MFA factor enrollment started

`factor_unenrolled`

MFA factor removed

`challenge_created`

MFA challenge initiated

`verification_attempted`

MFA verification attempt

`factor_deleted`

MFA factor deleted

`recovery_codes_deleted`

MFA recovery codes deleted

`factor_updated`

MFA factor settings updated

`mfa_code_login`

Login with MFA code

`identity_unlinked`

An identity unlinked from account

## Limitations[#](#limitations)

*   There may be a short delay before logs appear
*   Query capabilities are limited to the dashboard interface


