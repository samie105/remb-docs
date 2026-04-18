---
title: "Identity Linking"
source: "https://supabase.com/docs/guides/auth/auth-identity-linking"
canonical_url: "https://supabase.com/docs/guides/auth/auth-identity-linking"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:46.850Z"
content_hash: "98bb8aca2042651e3eb4bdbda63fa8aa8a865f3da9c0771967661a74181bbdc5"
menu_path: ["Auth","Auth","Flows (How-tos)","Flows (How-tos)","Identity Linking","Identity Linking"]
section_path: ["Auth","Auth","Flows (How-tos)","Flows (How-tos)","Identity Linking","Identity Linking"]
nav_prev: {"path": "supabase/docs/guides/auth/auth-hooks/send-sms-hook/index.md", "title": "Send SMS Hook"}
nav_next: {"path": "supabase/docs/guides/auth/auth-mfa/index.md", "title": "Multi-Factor Authentication"}
---

# 

Identity Linking

## 

Manage the identities associated with your user

* * *

## Identity linking strategies[#](#identity-linking-strategies)

Currently, Supabase Auth supports 2 strategies to link an identity to a user:

1.  [Automatic Linking](#automatic-linking)
2.  [Manual Linking](#manual-linking-beta)

### Automatic linking[#](#automatic-linking)

Supabase Auth automatically links identities with the same email address to a single user. This helps to improve the user experience when multiple OAuth login options are presented since the user does not need to remember which OAuth account they used to sign up with. When a new user signs in with OAuth, Supabase Auth will attempt to look for an existing user that uses the same email address. If a match is found, the new identity is linked to the user.

In order for automatic linking to correctly identify the user for linking, Supabase Auth needs to ensure that all user emails are unique. It would also be an insecure practice to automatically link an identity to a user with an unverified email address since that could lead to pre-account takeover attacks. To prevent this from happening, when a new identity can be linked to an existing user, Supabase Auth will remove any other unconfirmed identities linked to an existing user.

Users that signed up with [SAML SSO](/docs/guides/auth/sso/auth-sso-saml) will not be considered as targets for automatic linking.

### Manual linking (beta)[#](#manual-linking-beta)

Supabase Auth allows a user to initiate identity linking with a different email address when they are logged in. To link an OAuth identity to the user, call [`linkIdentity()`](/docs/reference/javascript/auth-linkidentity):

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6const { data, error } = await supabase.auth.linkIdentity({ provider: 'google' })
```

In the example above, the user will be redirected to Google to complete the OAuth2.0 flow. Once the OAuth2.0 flow has completed successfully, the user will be redirected back to the application and the Google identity will be linked to the user. You can enable manual linking from your project's authentication [configuration options](/dashboard/project/_/auth/providers) or by setting the environment variable `GOTRUE_SECURITY_MANUAL_LINKING_ENABLED: true` when self-hosting.

### Link identity with native OAuth (ID token)[#](#link-identity-with-native-oauth-id-token)

For native mobile applications, you can link an identity using an ID token obtained from a third-party OAuth provider. This is useful when you want to use native OAuth flows (like Google Sign-In or Sign in with Apple) rather than web-based OAuth redirects.

```
1// Example with Google Sign-In (using a native Google Sign-In library)2const idToken = 'ID_TOKEN_FROM_GOOGLE'3const accessToken = 'ACCESS_TOKEN_FROM_GOOGLE'45const { data, error } = await supabase.auth.linkIdentity({6  provider: 'google',7  token: idToken,8  access_token: accessToken,9})
```

## Unlink an identity[#](#unlink-an-identity)

You can use [`getUserIdentities()`](/docs/reference/javascript/auth-getuseridentities) to fetch all the identities linked to a user. Then, call [`unlinkIdentity()`](/docs/reference/javascript/auth-unlinkidentity) to unlink the identity. The user needs to be logged in and have at least 2 linked identities in order to unlink an existing identity.

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6// retrieve all identities linked to a user7const { data: identities, error: identitiesError } = await supabase.auth.getUserIdentities()89if (!identitiesError) {10  // find the google identity linked to the user11  const googleIdentity = identities.identities.find((identity) => identity.provider === 'google')1213  if (googleIdentity) {14    // unlink the google identity from the user15    const { data, error } = await supabase.auth.unlinkIdentity(googleIdentity)16  }17}
```

## Frequently asked questions[#](#frequently-asked-questions)

### How to add email/password login to an OAuth account?[#](#how-to-add-emailpassword-login-to-an-oauth-account)

Call the `updateUser({ password: 'validpassword'})` to add email with password authentication to an account created with an OAuth provider (Google, GitHub, etc.).

### Can you sign up with email if already using OAuth?[#](#can-you-sign-up-with-email-if-already-using-oauth)

If you try to create an email account after previously signing up with OAuth using the same email, you'll receive an obfuscated user response with no verification email sent. This prevents user enumeration attacks.
