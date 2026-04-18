---
title: "Customizing email templates"
source: "https://supabase.com/docs/guides/local-development/customizing-email-templates"
canonical_url: "https://supabase.com/docs/guides/local-development/customizing-email-templates"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:36.833Z"
content_hash: "aaa210c85328a3a5a85b0710b498391045cb53c5c40856ad4dd7fc541e345347"
menu_path: ["Local Dev / CLI","Local Dev / CLI","Local development","Local development","Customizing email templates","Customizing email templates"]
section_path: ["Local Dev / CLI","Local Dev / CLI","Local development","Local development","Customizing email templates","Customizing email templates"]
nav_prev: {"path": "supabase/docs/guides/local-development/declarative-database-schemas/index.md", "title": "Declarative database schemas"}
nav_next: {"path": "supabase/docs/guides/local-development/managing-config/index.md", "title": "Managing config and secrets"}
---

# 

Customizing email templates

## 

Customize local email templates via the config file.

* * *

You can customize the email templates for local development by [editing the `config.toml` file](/docs/guides/local-development/cli/config#auth-config).

## Configuring templates[#](#configuring-templates)

You should provide a relative URL to the `content_path` parameter, pointing to an HTML file which contains the template. For example:

### Authentication email templates[#](#authentication-email-templates)

```
1[auth.email.template.invite]2subject = "You are invited to Acme Inc"3content_path = "./supabase/templates/invite.html"
```

### Security notification email templates[#](#security-notification-email-templates)

```
1[auth.email.notification.password_changed]2enabled = true3subject = "Your password has been changed"4content_path = "./templates/password_changed_notification.html"
```

## Available authentication email templates[#](#available-authentication-email-templates)

There are several authentication-related email templates which can be configured. Each template serves a specific authentication flow:

### `auth.email.template.invite`[#](#authemailtemplateinvite)

**Default subject**: "You have been invited" **When sent**: When a user is invited to join your application via email invitation **Purpose**: Invite users who don't yet have an account to sign up **Content**: Contains a link for the invited user to accept the invitation and create their account

### `auth.email.template.confirmation`[#](#authemailtemplateconfirmation)

**Default subject**: "Confirm Your Signup" **When sent**: When a user signs up and needs to verify their email address **Purpose**: Ask users to confirm their email address after signing up **Content**: Contains a confirmation link to verify the user's email address

### `auth.email.template.recovery`[#](#authemailtemplaterecovery)

**Default subject**: "Reset Your Password" **When sent**: When a user requests a password reset **Purpose**: Allow users to reset their password if they forget it **Content**: Contains a link to reset the user's password

### `auth.email.template.magic_link`[#](#authemailtemplatemagiclink)

**Default subject**: "Your Magic Link" **When sent**: When a user requests a magic link for passwordless authentication **Purpose**: Allow users to sign in via a one-time link sent to their email **Content**: Contains a secure link that automatically logs the user in when clicked

### `auth.email.template.email_change`[#](#authemailtemplateemailchange)

**Default subject**: "Confirm Email Change" **When sent**: When a user requests to change their email address **Purpose**: Ask users to verify their new email address after changing it **Content**: Contains a confirmation link to verify the new email address

### `auth.email.template.reauthentication`[#](#authemailtemplatereauthentication)

**Default subject**: "Confirm Reauthentication" **When sent**: When a user needs to re-authenticate for sensitive operations **Purpose**: Ask users to re-authenticate before performing a sensitive action **Content**: Contains a 6-digit OTP code for verification

## Available security notification email templates[#](#available-security-notification-email-templates)

There are several security notification email templates which can be configured. These emails are only sent to users if the respective security notifications have been enabled at the project-level:

### `auth.email.notification.password_changed`[#](#authemailnotificationpasswordchanged)

**Default subject**: "Your password has been changed" **When sent**: When a user's password is changed **Purpose**: Notify users when their password has changed **Content**: Confirms that the password for the account has been changed

### `auth.email.notification.email_changed`[#](#authemailnotificationemailchanged)

**Default subject**: "Your email address has been changed" **When sent**: When a user's email address is changed **Purpose**: Notify users when their email address has changed **Content**: Confirms the change from the old email to the new email address

### `auth.email.notification.phone_changed`[#](#authemailnotificationphonechanged)

**Default subject**: "Your phone number has been changed" **When sent**: When a user's phone number is changed **Purpose**: Notify users when their phone number has changed **Content**: Confirms the change from the old phone number to the new phone number

### `auth.email.notification.mfa_factor_enrolled`[#](#authemailnotificationmfafactorenrolled)

**Default subject**: "A new MFA factor has been enrolled" **When sent**: When a new MFA factor is added to the user's account **Purpose**: Notify users when a new multi-factor authentication method has been added to their account **Content**: Confirms that a new MFA factor type has been enrolled

### `auth.email.notification.mfa_factor_unenrolled`[#](#authemailnotificationmfafactorunenrolled)

**Default subject**: "An MFA factor has been unenrolled" **When sent**: When an MFA factor is removed from the user's account **Purpose**: Notify users when a multi-factor authentication method has been removed from their account **Content**: Confirms that an MFA factor type has been unenrolled

### `auth.email.notification.identity_linked`[#](#authemailnotificationidentitylinked)

**Default subject**: "A new identity has been linked" **When sent**: When a new identity is linked to the account **Purpose**: Notify users when a new identity has been linked to their account **Content**: Confirms that a new identity has been linked

### `auth.email.notification.identity_unlinked`[#](#authemailnotificationidentityunlinked)

**Default subject**: "An identity has been unlinked" **When sent**: When an identity has been unlinked from the account **Purpose**: Notify users when an identity has been unlinked from their account **Content**: Confirms that an identity has been unlinked

## Template variables[#](#template-variables)

The templating system provides the following variables for use:

### `ConfirmationURL`[#](#confirmationurl)

Contains the confirmation URL. For example, a signup confirmation URL would look like:

```
1https://project-ref.supabase.co/auth/v1/verify?token={{ .TokenHash }}&type=email&redirect_to=https://example.com/path
```

**Usage**

```
1<p>Click here to confirm: {{ .ConfirmationURL }}</p>
```

### `Token`[#](#token)

Contains a 6-digit One-Time-Password (OTP) that can be used instead of the `ConfirmationURL`.

**Usage**

```
1<p>Here is your one time password: {{ .Token }}</p>
```

### `TokenHash`[#](#tokenhash)

Contains a hashed version of the `Token`. This is useful for constructing your own email link in the email template.

**Usage**

```
1<p>Follow this link to confirm your user:</p>2<p>3  <a href="{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email"4    >Confirm your email</a5  >6</p>
```

### `SiteURL`[#](#siteurl)

Contains your application's Site URL. This can be configured in your project's [authentication settings](/dashboard/project/_/auth/url-configuration).

**Usage**

```
1<p>Visit <a href="{{ .SiteURL }}">here</a> to log in.</p>
```

### `Email`[#](#email)

Contains the user's email address.

**Usage**

```
1<p>A recovery request was sent to {{ .Email }}.</p>
```

### `NewEmail`[#](#newemail)

Contains the new user's email address. This is only available in the `email_change` email template.

**Usage**

```
1<p>You are requesting to update your email address to {{ .NewEmail }}.</p>
```

### `OldEmail`[#](#oldemail)

Contains the user's old email address. This is only available in the `email_changed_notification` email template.

**Usage**

```
1<p>The email address for your account has been changed from {{ .OldEmail }} to {{ .Email }}.</p>
```

### `Phone`[#](#phone)

Contains the user's new phone number. This is only available in the `phone_changed_notification` email template.

**Usage**

```
1<p>The phone number for your account has been changed from {{ .OldPhone }} to {{ .Phone }}.</p>
```

### `OldPhone`[#](#oldphone)

Contains the user's old phone number. This is only available in the `phone_changed_notification` email template.

**Usage**

```
1<p>The phone number for your account has been changed from {{ .OldPhone }} to {{ .Phone }}.</p>
```

### `Provider`[#](#provider)

Contains the provider of the newly linked/unlinked identity. This is only available in the `identity_linked_notification` and `identity_unlinked_notification` email templates.

**Usage**

```
1<p>A new identity ({{ .Provider }}) has been linked to your account.</p>
```

### `FactorType`[#](#factortype)

Contains the type of the newly enrolled/unenrolled MFA factor. This is only available in the `mfa_factor_enrolled_notification` and `mfa_factor_unenrolled_notification` email templates.

**Usage**

```
1<p>A new factor ({{ .FactorType }}) has been enrolled for your account.</p>
```

## Deploying email templates[#](#deploying-email-templates)

These settings are for local development. To apply the changes locally, stop and restart the Supabase containers:

```
1supabase stop && supabase start
```

For hosted projects managed by Supabase, copy the templates into the [Email Templates](/dashboard/project/_/auth/templates) section of the Dashboard.


