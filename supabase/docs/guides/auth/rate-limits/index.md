---
title: "Rate limits"
source: "https://supabase.com/docs/guides/auth/rate-limits"
canonical_url: "https://supabase.com/docs/guides/auth/rate-limits"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:45.375Z"
content_hash: "9ae7d80641178f11ecce350613199a1ff2abb0e9230b31a89deeae2b2f152a0f"
menu_path: ["Auth","Auth","Security","Security","Rate Limits","Rate Limits"]
section_path: ["Auth","Auth","Security","Security","Rate Limits","Rate Limits"]
nav_prev: {"path": "supabase/docs/guides/auth/quickstarts/with-expo-react-native-social-auth/index.md", "title": "Build a Social Auth App with Expo React Native"}
nav_next: {"path": "supabase/docs/guides/auth/redirect-urls/index.md", "title": "Redirect URLs"}
---

# 

Rate limits

## 

Rate limits protect your services from abuse

* * *

Supabase Auth enforces rate limits on authentication endpoints to prevent abuse. Some rate limits are customizable, and you can configure them in your project [**Authentication** > **Rate Limits**](/dashboard/project/_/auth/rate-limits).

You can also manage rate limits using the Management API:

```
1# Get your access token from https://supabase.com/dashboard/account/tokens2export SUPABASE_ACCESS_TOKEN="your-access-token"3export PROJECT_REF="your-project-ref"45# Get current rate limits6curl -X GET "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \7  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \8  | jq 'to_entries | map(select(.key | startswith("rate_limit_"))) | from_entries'910# Update rate limits11curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \12  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \13  -H "Content-Type: application/json" \14  -d '{15    "rate_limit_anonymous_users": 10,16    "rate_limit_email_sent": 10,17    "rate_limit_sms_sent": 10,18    "rate_limit_verify": 10,19    "rate_limit_token_refresh": 10,20    "rate_limit_otp": 10,21    "rate_limit_web3": 1022  }'
```

## Rate limit behavior[#](#rate-limit-behavior)

Supabase Auth uses a token bucket algorithm for endpoint operations that are limited by IP address.

Each bucket has a maximum capacity of 30 requests. When the bucket is full, brief bursts of up to 30 requests can be allowed in a short period. Once the bucket empties, requests are rate limited until tokens refill. The rate limit defines the rate at which the bucket is refilled.

This means a client that has been idle will tolerate a brief spike in traffic, but sustained request above the rate limit are denied. When rate limits are exceeded, a **429 Too Many Requests** error is returned.

The table below shows the rate limit quotas and additional details for authentication endpoints.

Operation

Path

Limited By

Customizable

Limit

Endpoints that trigger email sends

`/auth/v1/signup` `/auth/v1/recover` `/auth/v1/user`

Sum of combined requests project-wide

Custom SMTP Only

2 emails per hour with the built-in email provider. You can only change this with a custom SMTP setup. The rate limit is only applied on `/auth/v1/user` if this endpoint is called to update the user's email address.

Send One-Time-Passwords (OTP)

`/auth/v1/otp`

Sum of combined requests project-wide

Yes

Defaults to 30 OTPs per hour.

Send OTPs or magic links

`/auth/v1/otp`

Last request of the user

Yes

Defaults to 60 seconds window before a new request is allowed to the same user.

Signup confirmation request

`/auth/v1/signup`

Last request of the user

Yes

Defaults to 60 seconds window before a new request is allowed to the same user.

Password Reset Request

`/auth/v1/recover`

Last request of the user

Yes

Defaults to 60 seconds window before a new request is allowed to the same user.

Verification requests

`/auth/v1/verify`

IP Address

No

360 requests per hour (with bursts up to 30 requests)

Token refresh requests

`/auth/v1/token`

IP Address

No

1800 requests per hour (with bursts up to 30 requests)

Create or Verify an MFA challenge

`/auth/v1/factors/:id/challenge` `/auth/v1/factors/:id/verify`

IP Address

No

15 requests per hour (with bursts up to requests)

Anonymous sign-ins

`/auth/v1/signup`

IP Address

No

30 requests per hour (with bursts up to 30 requests). Rate limit only applies if this endpoint is called without passing in an email or phone number in the request body.

## IP address forwarding[#](#ip-address-forwarding)

By default, Supabase Auth uses the IP address of the client for rate limiting. In certain cases, such as when using server-side frameworks or proxies in front of a project, it may be necessary to forward the end-user IP address to avoid being rate limited based on the address of the server-side client. To use a forwarded IP address for rate limiting in Supabase Auth, set the `Sb-Forwarded-For` header to the end-user IP address and make a request with a [secret API key](../../api/api-keys/index.md). Publishable API keys and legacy `anon`/`service_role` API keys are not supported.

IP address forwarding must be explicitly enabled for new projects. You can enable this feature in your project under the **IP Address Forwarding** section of your project's rate limit settings at [**Authentication** > **Rate Limits**](/dashboard/project/_/auth/rate-limits).

You can also enable IP address forwarding using the management API:

```
1# Get your access token from https://supabase.com/dashboard/account/tokens2export SUPABASE_ACCESS_TOKEN="your-access-token"3export PROJECT_REF="your-project-ref"45# Update IP address forwarding settings6curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \7     -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \8     -H "Content-Type: application/json" \9     -d '{10      "security_sb_forwarded_for_enabled": true11        }' \12    | jq '.security_sb_forwarded_for_enabled'
```

Once IP address forwarding is enabled, set the `Sb-Forwarded-For` header using the Supabase SDK:

```
1import { createServerClient } from '@supabase/ssr'23const supabase = createServerClient(4  'https://<your-project-id>.supabase.co',5  '<your-secret-key>', // Key should start with sb_secret6  {7    global: {8      headers: {9        'sb-forwarded-for': request.headers.get('x-forwarded-for'),10      },11    },12  }13)
```
