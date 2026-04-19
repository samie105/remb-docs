---
title: "Send Email Hook"
source: "https://supabase.com/docs/guides/auth/auth-hooks/send-email-hook"
canonical_url: "https://supabase.com/docs/guides/auth/auth-hooks/send-email-hook"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:58.057Z"
content_hash: "4ac68f014ddcea6bdb86b33ba85b2d962a22d403e63273a7ecec4fe4eaee2119"
menu_path: ["Auth","Auth","More","More","More","Auth Hooks","Auth Hooks","Send email hook","Send email hook"]
section_path: ["Auth","Auth","More","More","More","Auth Hooks","Auth Hooks","Send email hook","Send email hook"]
nav_prev: {"path": "supabase/docs/guides/auth/auth-hooks/password-verification-hook/index.md", "title": "Password Verification Hook"}
nav_next: {"path": "supabase/docs/guides/auth/auth-hooks/send-sms-hook/index.md", "title": "Send SMS Hook"}
---

# 

Send Email Hook

## 

Use your own email service to send authentication emails.

* * *

The Send Email Hook replaces Supabase's built-in email sending. You can use this hook to:

*   Send emails using your own email provider
*   Add internationalization or custom logic
*   Fall back to another provider if your primary one fails

**Inputs**

Field

Type

Description

`user`

[`User`](/docs/guides/auth/users#the-user-object)

The user account taking the action

`email`

`object`

Metadata specific to the email sending process

```
1{2  "user": {3    "id": "8484b834-f29e-4af2-bf42-80644d154f76",4    "aud": "authenticated",5    "role": "authenticated",6    "email": "valid.email@supabase.io",7    "phone": "",8    "app_metadata": {9      "provider": "email",10      "providers": ["email"]11    },12    "user_metadata": {13      "email": "valid.email@supabase.io",14      "email_verified": false,15      "phone_verified": false,16      "sub": "8484b834-f29e-4af2-bf42-80644d154f76"17    },18    "identities": [19      {20        "identity_id": "bc26d70b-517d-4826-bce4-413a5ff257e7",21        "id": "8484b834-f29e-4af2-bf42-80644d154f76",22        "user_id": "8484b834-f29e-4af2-bf42-80644d154f76",23        "identity_data": {24          "email": "valid.email@supabase.io",25          "email_verified": false,26          "phone_verified": false,27          "sub": "8484b834-f29e-4af2-bf42-80644d154f76"28        },29        "provider": "email",30        "last_sign_in_at": "2024-05-14T12:56:33.824231484Z",31        "created_at": "2024-05-14T12:56:33.824261Z",32        "updated_at": "2024-05-14T12:56:33.824261Z",33        "email": "valid.email@supabase.io"34      }35    ],36    "created_at": "2024-05-14T12:56:33.821567Z",37    "updated_at": "2024-05-14T12:56:33.825595Z",38    "is_anonymous": false39  },40  "email_data": {41    "token": "305805",42    "token_hash": "7d5b7b1964cf5d388340a7f04f1dbb5eeb6c7b52ef8270e1737a58d0",43    "redirect_to": "http://localhost:3000/",44    "email_action_type": "signup",45    "site_url": "http://localhost:9999",46    "token_new": "",47    "token_hash_new": "",48    "old_email": "",49    "old_phone": "",50    "provider": "",51    "factor_type": ""52  }53}
```

**Outputs**

*   No outputs are required. An empty response with a status code of 200 is taken as a successful response.

## Email sending behavior[#](#email-sending-behavior)

Email sending depends on two settings: Email Provider and Auth Hook status.

Email Provider

Auth Hook

Result

Enabled

Enabled

Auth Hook handles email sending (SMTP not used)

Enabled

Disabled

SMTP handles email sending (custom if configured, default otherwise)

Disabled

Enabled

Email signups disabled

Disabled

Disabled

Email signups disabled

## Email change behavior and token hash mapping[#](#email-change-behavior-and-token-hash-mapping)

When `email_action_type` is `email_change`, the hook payload can include one or two OTPs and their hashes. This depends on your [Secure Email Change](/dashboard/project/_/auth/providers?provider=Email) setting.

*   Secure Email Change enabled: two OTPs are generated, one for the current email (`user.email`) and one for the new email (`user.new_email`). You must send two emails.
*   Secure Email Change disabled: only one OTP is generated for the new email. You send a single email.

##### Counterintuitive field naming

The token hash field names are reversed due to backward compatibility. Pay careful attention to which token/hash pair goes with which email address:

*   `token_hash_new` → use with the **current** email address (`user.email`) and `token`
*   `token_hash` → use with the **new** email address (`user.new_email`) and `token_new`

Do not assume the `_new` suffix refers to the new email address.

### What to send[#](#what-to-send)

When Secure Email Change is enabled (both token/hash pairs present):

*   Send to **current** email address (`user.email`): use `token` with `token_hash_new`
*   Send to **new** email address (`user.new_email`): use `token_new` with `token_hash`

When Secure Email Change is **disabled** (only one token/hash pair present):

*   Send a single email to the **new** email address. Use `token` with `token_hash` or `token_new` with `token_hash`, depending on which fields are present in the payload.

You can configure [Resend](https://resend.com/) as the custom email provider through the "Send Email" hook. This allows you to take advantage of Resend's developer-friendly APIs to send emails and leverage [React Email](https://react.email/) for managing your email templates. For a more advanced React Email tutorial, refer to [this guide](/docs/guides/functions/examples/auth-send-email-hook-react-email-resend).

If you want to send emails through the Supabase Resend integration, which uses Resend's SMTP server, check out [this integration](/partners/integrations/resend) instead.

Create a `.env` file with the following environment variables:

```
1RESEND_API_KEY="your_resend_api_key"2SEND_EMAIL_HOOK_SECRET="v1,whsec_<base64_secret>"
```

You can generate the secret in the [Auth Hooks](/dashboard/project/_/auth/hooks) section of the Supabase dashboard.

Set the secrets in your Supabase project:

```
1supabase secrets set --env-file .env
```

Create a new edge function:

```
1supabase functions new send-email
```

Add the following code to your edge function:

```
1import { Webhook } from "https://esm.sh/standardwebhooks@1.0.0";2import { Resend } from "npm:resend";34const resend = new Resend(Deno.env.get("RESEND_API_KEY") as string);5const hookSecret = (Deno.env.get("SEND_EMAIL_HOOK_SECRET") as string).replace("v1,whsec_", "");67Deno.serve(async (req) => {8  if (req.method !== "POST") {9    return new Response("not allowed", { status: 400 });10  }1112  const payload = await req.text();13  const headers = Object.fromEntries(req.headers);14  const wh = new Webhook(hookSecret);15  try {16    const { user, email_data } = wh.verify(payload, headers) as {17      user: {18        email: string;19      };20      email_data: {21        token: string;22        token_hash: string;23        redirect_to: string;24        email_action_type: string;25        site_url: string;26        token_new: string;27        token_hash_new: string;28      };29    };3031    const { error } = await resend.emails.send({32      from: "welcome <onboarding@example.com>",33      to: [user.email],34      subject: "Welcome to my site!",35      text: `Confirm you signup with this code: ${email_data.token}`,36    });37    if (error) {38      throw error;39    }40  } catch (error) {41    return new Response(42      JSON.stringify({43        error: {44          http_code: error.code,45          message: error.message,46        },47      }),48      {49        status: 401,50        headers: { "Content-Type": "application/json" },51      },52    );53  }5455  const responseHeaders = new Headers();56  responseHeaders.set("Content-Type", "application/json");57  return new Response(JSON.stringify({}), {58    status: 200,59    headers: responseHeaders,60  });61});
```

Deploy your edge function and [configure it as a hook](/dashboard/project/_/auth/hooks):

```
1supabase functions deploy send-email --no-verify-jwt
```
