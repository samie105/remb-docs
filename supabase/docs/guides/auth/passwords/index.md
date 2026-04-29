---
title: "Password-based Auth"
source: "https://supabase.com/docs/guides/auth/passwords"
canonical_url: "https://supabase.com/docs/guides/auth/passwords"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:37.337Z"
content_hash: "111f8f5b658e1630d85e5f793fb798eea4e6c9d2403ea2e442908dc4e1f65662"
menu_path: ["Auth","Auth","Flows (How-tos)","Flows (How-tos)","Password-based","Password-based"]
section_path: ["Auth","Auth","Flows (How-tos)","Flows (How-tos)","Password-based","Password-based"]
nav_prev: {"path": "supabase/docs/guides/auth/password-security/index.md", "title": "Password security"}
nav_next: {"path": "supabase/docs/guides/auth/phone-login/index.md", "title": "Phone Login"}
---

# 

Password-based Auth

## 

Allow users to sign in with a password connected to their email or phone number.

* * *

Users often expect to sign in to your site with a password. Supabase Auth helps you implement password-based auth safely, using secure configuration options and best practices for storing and verifying passwords.

Users can associate a password with their identity using their [email address](#with-email) or a [phone number](#with-phone).

## With email[#](#with-email)

### Enabling email and password-based authentication[#](#enabling-email-and-password-based-authentication)

Email authentication is enabled by default.

You can configure whether users need to verify their email to sign in. On hosted Supabase projects, this is true by default. On self-hosted projects or in local development, this is false by default.

Change this setting on the [Auth Providers page](/dashboard/project/_/auth/providers) for hosted projects, or in the [configuration file](/docs/guides/cli/config#auth.email.enable_confirmations) for self-hosted projects.

### Signing up with an email and password[#](#signing-up-with-an-email-and-password)

There are two possible flows for email signup: [implicit flow](../sessions/index.md#implicit-flow) and [PKCE flow](../sessions/index.md#pkce-flow). If you're using SSR, you're using the PKCE flow. If you're using client-only code, the default flow depends upon the client library. The implicit flow is the default in JavaScript and Dart, and the PKCE flow is the default in Swift.

The instructions in this section assume that email confirmations are enabled.

The implicit flow only works for client-only apps. Your site directly receives the access token after the user confirms their email.

To sign up the user, call [signUp()](/docs/reference/javascript/auth-signup) with their email address and password.

You can optionally specify a URL to redirect to after the user clicks the confirmation link. This URL must be configured as a [Redirect URL](../redirect-urls/index.md), which you can do in the [dashboard](/dashboard/project/_/auth/url-configuration) for hosted projects, or in the [configuration file](/docs/guides/cli/config#auth.additional_redirect_urls) for self-hosted projects.

If you don't specify a redirect URL, the user is automatically redirected to your site URL. This defaults to `localhost:3000`, but you can also configure this.

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6async function signUpNewUser() {7  const { data, error } = await supabase.auth.signUp({8    email: 'valid.email@supabase.io',9    password: 'example-password',10    options: {11      emailRedirectTo: 'https://example.com/welcome',12    },13  })14}
```

### Signing in with an email and password[#](#signing-in-with-an-email-and-password)

When your user signs in, call [`signInWithPassword()`](/docs/reference/javascript/auth-signinwithpassword) with their email address and password:

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6async function signInWithEmail() {7  const { data, error } = await supabase.auth.signInWithPassword({8    email: 'valid.email@supabase.io',9    password: 'example-password',10  })11}
```

### Resetting a password[#](#resetting-a-password)

#### Step 1: Create a reset password page[#](#step-1-create-a-reset-password-page)

Create a **reset password** page. This page should be publicly accessible.

Collect the user's email address and request a password reset email. Specify the redirect URL, which should point to the URL of a **change password** page. This URL needs to be configured in your [redirect URLs](../redirect-urls/index.md).

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6await supabase.auth.resetPasswordForEmail('valid.email@supabase.io', {7  redirectTo: 'http://example.com/account/update-password',8})
```

#### Step 2: Create a change password page[#](#step-2-create-a-change-password-page)

Create a **change password** page at the URL you specified in the previous step. This page should be accessible only to authenticated users.

Collect the user's new password and call `updateUser` to update their password.

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6await supabase.auth.updateUser({ password: 'new_password' })
```

#### Verifying the current password[#](#verifying-the-current-password)

If your app requires users to confirm their current password before setting a new one, you can pass `currentPassword` (available in `supabase-js` v2.102.0+ and `supabase-kt` 3.5.0+):

```
1await supabase.auth.updateUser({2  password: 'new_password',3  currentPassword: 'old_password',4})
```

### Email sending[#](#email-sending)

The signup confirmation and password reset flows require an SMTP server to send emails.

The Supabase platform comes with a default email-sending service for you to try out. The service has a rate limit of 2 emails per hour, and availability is on a best-effort basis. For production use, you should consider configuring a custom SMTP server.

Consider configuring a custom SMTP server for production.

See the [Custom SMTP guide](../auth-smtp/index.md) for instructions.

#### Local development with Mailpit[#](#local-development-with-mailpit)

You can test email flows on your local machine. The Supabase CLI automatically captures emails sent locally by using [Mailpit](https://github.com/axllent/mailpit).

In your terminal, run `supabase status` to get the Mailpit URL. Go to this URL in your browser, and follow the instructions to find your emails.

## With phone[#](#with-phone)

You can use a user's mobile phone number as an identifier, instead of an email address, when they sign up with a password.

This practice is usually discouraged because phone networks recycle mobile phone numbers. Anyone receiving a recycled phone number gets access to the original user's account. To mitigate this risk, [implement MFA](../auth-mfa/index.md).

Protect users who use a phone number as a password-based auth identifier by enabling MFA.

### Enabling phone and password-based authentication[#](#enabling-phone-and-password-based-authentication)

Enable phone authentication on the [Auth Providers page](/dashboard/project/_/auth/providers) for hosted Supabase projects.

For self-hosted projects or local development, use the [configuration file](/docs/guides/cli/config#auth.sms.enable_signup). See the configuration variables namespaced under `auth.sms`.

If you want users to confirm their phone number on signup, you need to set up an SMS provider. Each provider has its own configuration. Supported providers include MessageBird, Twilio, Vonage, and TextLocal (community-supported).

### Configuring SMS Providers

### Signing up with a phone number and password[#](#signing-up-with-a-phone-number-and-password)

To sign up the user, call [`signUp()`](/docs/reference/javascript/auth-signup) with their phone number and password:

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6const { data, error } = await supabase.auth.signUp({7  phone: '+13334445555',8  password: 'some-password',9})
```

If you have phone verification turned on, the user receives an SMS with a 6-digit pin that you must verify within 60 seconds:

You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to `verifyOtp`:

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6const {7  data: { session },8  error,9} = await supabase.auth.verifyOtp({10  phone: '+13334445555',11  token: '123456',12  type: 'sms',13})
```

### Signing in a with a phone number and password[#](#signing-in-a-with-a-phone-number-and-password)

Call the function to sign in with the user's phone number and password:

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6const { data, error } = await supabase.auth.signInWithPassword({7  phone: '+13334445555',8  password: 'some-password',9})
```
