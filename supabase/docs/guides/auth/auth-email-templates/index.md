---
title: "Email Templates"
source: "https://supabase.com/docs/guides/auth/auth-email-templates"
canonical_url: "https://supabase.com/docs/guides/auth/auth-email-templates"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:42.423Z"
content_hash: "dcb0ee628597051c9c1dfea2c549e37522dce294359ed269a3f9e345336c4683"
menu_path: ["Auth","Auth","Configuration","Configuration","Email Templates","Email Templates"]
section_path: ["Auth","Auth","Configuration","Configuration","Email Templates","Email Templates"]
nav_prev: {"path": "../auth-email-passwordless/index.md", "title": "Passwordless email logins"}
nav_next: {"path": "../auth-hooks/index.md", "title": "Auth Hooks"}
---

# 

Email Templates

## 

Learn how to manage the email templates in Supabase.

* * *

Email templates in Supabase fall into two categories: authentication and security notifications.

Authentication emails:

*   Confirm sign up
*   Invite user
*   Magic link
*   Change email address
*   Reset password
*   Reauthentication

Security notification emails:

*   Password changed
*   Email address changed
*   Phone number changed
*   Identity linked
*   Identity unlinked
*   Multi-factor authentication (MFA) method added
*   Multi-factor authentication (MFA) method removed

Security emails are only sent to users if the respective security notifications have been enabled at a project-level.

## Terminology[#](#terminology)

The templating system provides the following variables for use:

Name

Description

`{{ .ConfirmationURL }}`

Contains the confirmation URL. For example, a signup confirmation URL would look like: `https://project-ref.supabase.co/auth/v1/verify?token={{ .TokenHash }}&type=email&redirect_to=https://example.com/path`.

`{{ .Token }}`

Contains a 6-digit One-Time-Password (OTP) that can be used instead of the `{{. ConfirmationURL }}`.

`{{ .TokenHash }}`

Contains a hashed version of the `{{ .Token }}`. This is useful for constructing your own email link in the email template.

`{{ .SiteURL }}`

Contains your application's Site URL. This can be configured in your project's [authentication settings](/dashboard/project/_/auth/url-configuration).

`{{ .RedirectTo }}`

Contains the redirect URL passed when `signUp`, `signInWithOtp`, `signInWithOAuth`, `resetPasswordForEmail` or `inviteUserByEmail` is called. The redirect URL allow list can be configured in your project's [authentication settings](/dashboard/project/_/auth/url-configuration).

`{{ .Data }}`

Contains metadata from `auth.users.user_metadata`. Use this to personalize the email message.

`{{ .Email }}`

Contains the original email address of the user. Empty when trying to [link an email address to an anonymous user](/docs/guides/auth/auth-anonymous#link-an-email--phone-identity).

`{{ .NewEmail }}`

Contains the new email address of the user. This variable is only supported in the "Change email address" template.

`{{ .OldEmail }}`

Contains the old email address of the user. This variable is only supported in the "Email address changed notification" template.

`{{ .Phone }}`

Contains the new phone number of the user. This variable is only supported in the "Phone number changed notification" template.

`{{ .OldPhone }}`

Contains the old phone address of the user. This variable is only supported in the "Phone number changed notification" template.

`{{ .Provider }}`

Contains the provider of the newly linked/unlinked identity. This variable is only supported in the "Identity linked notification" and "Identity unlinked notification" templates.

`{{ .FactorType }}`

Contains the type of the newly enrolled/unenrolled MFA method. This variable is only supported in the "MFA method added notification" and "MFA method removed notification" templates.

## Editing email templates[#](#editing-email-templates)

On hosted Supabase projects, edit your email templates on the [Email Templates](/dashboard/project/_/auth/templates) page. On self-hosted projects or in local development, edit your [configuration files](/docs/guides/local-development/customizing-email-templates).

You can also manage email templates using the Management API:

```
1# Get your access token from https://supabase.com/dashboard/account/tokens2export SUPABASE_ACCESS_TOKEN="your-access-token"3export PROJECT_REF="your-project-ref"45# Get current email templates6curl -X GET "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \7  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \8  | jq 'to_entries | map(select(.key | startswith("mailer_templates"))) | from_entries'910# Update email templates11curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \12  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \13  -H "Content-Type: application/json" \14  -d '{15      "mailer_subjects_confirmation": "Confirm your signup",16      "mailer_templates_confirmation_content": "<h2>Confirm your signup</h2><p>Follow this link to confirm your user:</p><p><a href=\"{{ .ConfirmationURL }}\">Confirm your email</a></p>",17      "mailer_subjects_magic_link": "Your Magic Link",18      "mailer_templates_magic_link_content": "<h2>Magic Link</h2><p>Follow this link to login:</p><p><a href=\"{{ .ConfirmationURL }}\">Log In</a></p>",19      "mailer_subjects_recovery": "Rest Your Password",20      "mailer_templates_recovery_content": "<h2>Reset Password</h2><p>Follow this link to reset the password for your user:</p><p><a href=\"{{ .ConfirmationURL }}\">Reset Password</a></p>",21      "mailer_subjects_invite": "You have been invited",22      "mailer_templates_invite_content": "<h2>You have been invited</h2><p>You have been invited to create a user on {{ .SiteURL }}. Follow this link to accept the invite:</p><p><a href=\"{{ .ConfirmationURL }}\">Accept the invite</a></p>",23      "mailer_subjects_reauthentication": "Confirm reauthentication",24      "mailer_templates_reauthentication_content": "<h2>Confirm reauthentication</h2><p>Enter the code: {{token}}</p>",25      "mailer_subjects_email_change": "Confirm email change",26      "mailer_templates_email_change_content": "<h2>Confirm email change</h2><p>Follow this link to confirm the update of your email:</p><p><a href=\"{{ .ConfirmationURL }}\">Change email</a></p>",27      "mailer_notifications_password_changed_enabled": true,28      "mailer_subjects_password_changed_notification": "Your password has been changed",29      "mailer_templates_password_changed_notification_content": "<h2>Your password has been changed</h2>\n\n<p>This is a confirmation that the password for your account {{ .Email }} has just been changed.</p>\n<p>If you did not make this change, please contact support.</p>",30      "mailer_notifications_email_changed_enabled": true,31      "mailer_subjects_email_changed_notification": "Your email address has been changed",32      "mailer_templates_email_changed_notification_content": "<h2>Your email address has been changed</h2>\n\n<p>The email address for your account has been changed from {{ .OldEmail }} to {{ .Email }}.</p>\n<p>If you did not make this change, please contact support.</p>",33      "mailer_notifications_phone_changed_enabled": true,34      "mailer_subjects_phone_changed_notification": "Your phone number has been changed",35      "mailer_templates_phone_changed_notification_content": "<h2>Your phone number has been changed</h2>\n\n<p>The phone number for your account {{ .Email }} has been changed from {{ .OldPhone }} to {{ .Phone }}.</p>\n<p>If you did not make this change, please contact support immediately.</p>",36      "mailer_notifications_mfa_factor_enrolled_enabled": true,37      "mailer_subjects_mfa_factor_enrolled_notification": "A new MFA factor has been enrolled",38      "mailer_templates_mfa_factor_enrolled_notification_content": "<h2>A new MFA factor has been enrolled</h2>\n\n<p>A new factor ({{ .FactorType }}) has been enrolled for your account {{ .Email }}.</p>\n<p>If you did not make this change, please contact support immediately.</p>",39      "mailer_notifications_mfa_factor_unenrolled_enabled": true,40      "mailer_subjects_mfa_factor_unenrolled_notification": "An MFA factor has been unenrolled",41      "mailer_templates_mfa_factor_unenrolled_notification_content": "<h2>An MFA factor has been unenrolled</h2>\n\n<p>A factor ({{ .FactorType }}) has been unenrolled for your account {{ .Email }}.</p>\n<p>If you did not make this change, please contact support immediately.</p>",42      "mailer_notifications_identity_linked_enabled": true,43      "mailer_subjects_identity_linked_notification": "A new identity has been linked",44      "mailer_templates_identity_linked_notification_content": "<h2>A new identity has been linked</h2>\n\n<p>A new identity ({{ .Provider }}) has been linked to your account {{ .Email }}.</p>\n<p>If you did not make this change, please contact support immediately.</p>",45      "mailer_notifications_identity_unlinked_enabled": true,46      "mailer_subjects_identity_unlinked_notification": "An identity has been unlinked",47      "mailer_templates_identity_unlinked_notification_content": "<h2>An identity has been unlinked</h2>\n\n<p>An identity ({{ .Provider }}) has been unlinked from your account {{ .Email }}.</p>\n<p>If you did not make this change, please contact support immediately.</p>"48  }'
```

## Mobile deep linking[#](#mobile-deep-linking)

For mobile applications, you might need to link or redirect to a specific page within your app. See the [Mobile Deep Linking guide](/docs/guides/auth/native-mobile-deep-linking) to set this up.

## Limitations[#](#limitations)

### Email prefetching[#](#email-prefetching)

Certain email providers may have spam detection or other security features that prefetch URL links from incoming emails (e.g. [Safe Links in Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/safe-links-about?view=o365-worldwide)). In this scenario, the `{{ .ConfirmationURL }}` sent will be consumed instantly which leads to a "Token has expired or is invalid" error. To guard against this there are the options below:

**Option 1**

*   Use an email OTP instead by including `{{ .Token }}` in the email template
*   Create your own custom email link to redirect the user to a page where they can enter with their email and token to login

```
1<a href="{{ .SiteURL }}/confirm-signup">Confirm your signup</a>
```

*   Log them in by verifying the OTP token value with their email e.g. with [`supabase.auth.verifyOtp`](/docs/reference/javascript/auth-verifyotp) show below

```
1const { data, error } = await supabase.auth.verifyOtp({ email, token, type: 'email' })
```

**Option 2**

*   Create your own custom email link to redirect the user to a page where they can click on a button to confirm the action

```
1<a href="{{ .SiteURL }}/confirm-signup?confirmation_url={{ .ConfirmationURL }}">2  Confirm your signup3</a>
```

*   The button should contain the actual confirmation link which can be obtained from parsing the `confirmation_url={{ .ConfirmationURL }}` query parameter in the URL.

### Email tracking[#](#email-tracking)

If you are using an external email provider that enables "email tracking", the links inside the Supabase email templates will be overwritten and won't perform as expected. We recommend disabling email tracking to ensure email links are not overwritten.

### Redirecting the user to a server-side endpoint[#](#redirecting-the-user-to-a-server-side-endpoint)

If you intend to use [Server-side rendering](/docs/guides/auth/server-side-rendering), you might want the email link to redirect the user to a server-side endpoint to check if they are authenticated before returning the page. However, the default email link will redirect the user after verification to the redirect URL with the session in the query fragments. Since the session is returned in the query fragments by default, you won't be able to access it on the server-side.

You can customize the email link in the email template to redirect the user to a server-side endpoint successfully. For example:

```
1<a2  href="https://api.example.com/v1/authenticate?token_hash={{ .TokenHash }}&type=invite&redirect_to={{ .RedirectTo }}"3>4  Accept the invite5</a>
```

When the user clicks on the link, the request will hit `https://api.example.com/v1/authenticate` and you can grab the `token_hash`, `type` and `redirect_to` query parameters from the URL. Then, you can call the [`verifyOtp`](/docs/reference/javascript/auth-verifyotp) method to get back an authenticated session before redirecting the user back to the client. Since the `verifyOtp` method makes a `POST` request to Supabase Auth to verify the user, the session will be returned in the response body, which can be read by the server. For example:

```
1import { createClient, type EmailOtpType } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6const { token_hash, type } = Object.fromEntries(new URLSearchParams(window.location.search))7const {8  data: { session },9  error,10} = await supabase.auth.verifyOtp({ token_hash, type: type as EmailOtpType })1112// subsequently redirect the user back to the client using the redirect_to param13// ...
```

## Customization[#](#customization)

Supabase Auth makes use of [Go Templates](https://pkg.go.dev/text/template). This means it is possible to conditionally render information based on template properties.

### Send different email to early access users[#](#send-different-email-to-early-access-users)

Send a different email to users who signed up via an early access domain (`https://www.earlyaccess.trial.com`).

```
1{{ if eq .Data.Domain "https://www.example.com" }}2<h1>Welcome to Our Database Service!</h1>3  <p>Dear Developer,</p>4  <p>Welcome to Billy, the scalable developer platform!</p>5  <p>Best Regards,<br>6Billy Team</p>7{{ else if eq .Data.Domain "https://www.earlyaccess.trial.com" }}8<h1>Welcome to Our Database Service!</h1>9  <p>Dear Developer,</p>10  <p>Welcome Billy, the scalable developer platform!</p>11  <p> As an early access member, you have access to select features like Point To Space Restoration.</p>12  <p>Best Regards,<br>13Billy Team</p>14{{ end }}
```
