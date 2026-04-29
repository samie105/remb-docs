---
title: "Configure Phone Login & MFA"
source: "https://supabase.com/docs/guides/self-hosting/self-hosted-phone-mfa"
canonical_url: "https://supabase.com/docs/guides/self-hosting/self-hosted-phone-mfa"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:44.375Z"
content_hash: "742abcbd9ddb282675def0e9f0dce5d5803c2de47b621a83255f97522547e26e"
menu_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Configure Phone Login & MFA","Configure Phone Login & MFA"]
section_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Configure Phone Login & MFA","Configure Phone Login & MFA"]
nav_prev: {"path": "../self-hosted-oauth/index.md", "title": "Configure Social Login (OAuth) Providers"}
nav_next: {"path": "../self-hosted-proxy-https/index.md", "title": "Configure Reverse Proxy and HTTPS"}
---

# 

Configure Phone Login & MFA

## 

Set up phone login SMS providers, OTP settings, and multi-factor authentication for self-hosted Supabase with Docker.

* * *

This guide covers the **server-side configuration** for phone login and multi-factor authentication (MFA) on a self-hosted Supabase instance running with Docker Compose.

For client-side implementation, see [Phone Login](/docs/guides/auth/phone-login) and [Multi-Factor Authentication](/docs/guides/auth/auth-mfa).

## Before you begin[#](#before-you-begin)

You need:

*   A working self-hosted Supabase installation. See [Self-Hosting with Docker](/docs/guides/self-hosting/docker).
*   An account with an SMS provider (e.g., Twilio)

Phone auth is **enabled by default** in the Docker setup (`ENABLE_PHONE_SIGNUP=true` in `.env`). However, without an SMS provider configured, the Auth service has no way to deliver OTP codes.

## SMS provider configuration[#](#sms-provider-configuration)

The default `.env.example` and `docker-compose.yml` include commented-out SMS provider placeholders. The example below uses Twilio - you'll need a Twilio account with an account SID, auth token, and message service SID. See [Twilio's documentation](https://www.twilio.com/docs/messaging) for how to obtain these credentials.

To enable SMS delivery:

### Step 1: Uncomment and configure the environment variables[#](#step-1-uncomment-and-configure-the-environment-variables)

```
1SMS_PROVIDER=twilio2SMS_OTP_EXP=603SMS_OTP_LENGTH=64SMS_MAX_FREQUENCY=60s5SMS_TEMPLATE=Your code is {{ .Code }}67## Twilio credentials8SMS_TWILIO_ACCOUNT_SID=your-account-sid9SMS_TWILIO_AUTH_TOKEN=your-auth-token10SMS_TWILIO_MESSAGE_SERVICE_SID=your-message-service-sid
```

### Step 2: Uncomment the matching lines in Docker Compose configuration[#](#step-2-uncomment-the-matching-lines-in-docker-compose-configuration)

Uncomment the `GOTRUE_SMS_*` lines in the `auth` service's `environment` block:

```
1auth:2  environment:3    # ... existing variables ...4    GOTRUE_SMS_PROVIDER: ${SMS_PROVIDER}5    GOTRUE_SMS_OTP_EXP: ${SMS_OTP_EXP}6    GOTRUE_SMS_OTP_LENGTH: ${SMS_OTP_LENGTH}7    GOTRUE_SMS_MAX_FREQUENCY: ${SMS_MAX_FREQUENCY}8    GOTRUE_SMS_TEMPLATE: ${SMS_TEMPLATE}9    GOTRUE_SMS_TWILIO_ACCOUNT_SID: ${SMS_TWILIO_ACCOUNT_SID}10    GOTRUE_SMS_TWILIO_AUTH_TOKEN: ${SMS_TWILIO_AUTH_TOKEN}11    GOTRUE_SMS_TWILIO_MESSAGE_SERVICE_SID: ${SMS_TWILIO_MESSAGE_SERVICE_SID}
```

### Step 3: Restart the auth service[#](#step-3-restart-the-auth-service)

```
1docker compose up -d --force-recreate --no-deps auth
```

### Step 4: Verify[#](#step-4-verify)

```
1docker compose exec auth env | grep GOTRUE_SMS
```

Confirm your provider and credentials appear in the output.

For providers other than Twilio, add the provider-specific `GOTRUE_SMS_*` lines manually to `docker-compose.yml`.

## OTP settings[#](#otp-settings)

### Expiration[#](#expiration)

The default OTP expiration is **60 seconds**. This is often too short for production use, consider increasing it.

Set `SMS_OTP_EXP` in `.env` (value is in seconds):

```
1# Set expiration to 5 minutes2SMS_OTP_EXP=300
```

And ensure `GOTRUE_SMS_OTP_EXP: ${SMS_OTP_EXP}` is uncommented in `docker-compose.yml`.

### Length[#](#length)

The default OTP length is 6 digits. You can set it to any value between 6 and 10:

```
1SMS_OTP_LENGTH=8
```

### Rate limiting[#](#rate-limiting)

`SMS_MAX_FREQUENCY` controls the minimum interval between SMS sends to the same phone number. The default is 60 seconds:

```
1## Allow one SMS every 30 seconds2SMS_MAX_FREQUENCY=30s
```

## Test OTPs for development[#](#test-otps-for-development)

To avoid sending real SMS during development, use `SMS_TEST_OTP` to map phone numbers to fixed OTP codes:

```
1SMS_TEST_OTP=16505551234:123456,16505555678:654321
```

And uncomment `GOTRUE_SMS_TEST_OTP: ${SMS_TEST_OTP}` in `docker-compose.yml`.

When a test phone number requests an OTP, the Auth service skips SMS delivery and accepts only the mapped code. Other phone numbers continue to use the real SMS provider.

Remove test OTPs before deploying to production. You can also set an expiration with `SMS_TEST_OTP_VALID_UNTIL` (ISO 8601 datetime, e.g., `2026-12-31T23:59:59Z`) so they stop working automatically.

## Multi-factor authentication (MFA)[#](#multi-factor-authentication-mfa)

The Auth service supports three MFA factor types. Configure them by uncommenting variables in `.env` and the matching `GOTRUE_MFA_*` lines in `docker-compose.yml`.

### App authenticator (TOTP)[#](#app-authenticator-totp)

TOTP is **enabled by default** - users can enroll with apps like Google Authenticator or Authy without any additional configuration.

To disable TOTP:

```
1MFA_TOTP_ENROLL_ENABLED=false2MFA_TOTP_VERIFY_ENABLED=false
```

### Phone MFA[#](#phone-mfa)

Phone MFA is **disabled by default** (opt-in). It uses the same SMS provider configuration as phone login.

To enable:

```
1MFA_PHONE_ENROLL_ENABLED=true2MFA_PHONE_VERIFY_ENABLED=true
```

### Maximum enrolled factors[#](#maximum-enrolled-factors)

By default, a user can enroll up to 10 MFA factors. To change this:

```
1MFA_MAX_ENROLLED_FACTORS=5
```

## Troubleshooting[#](#troubleshooting)

### OTP expires too quickly[#](#otp-expires-too-quickly)

The default `SMS_OTP_EXP` is 60 seconds. Increase it in `.env`:

```
1SMS_OTP_EXP=300
```

Ensure `GOTRUE_SMS_OTP_EXP: ${SMS_OTP_EXP}` is uncommented in `docker-compose.yml`, then restart:

```
1docker compose up -d --force-recreate --no-deps auth
```

### SMS not being delivered[#](#sms-not-being-delivered)

Check the auth container logs for errors:

```
1docker compose logs auth --tail 50
```

Verify provider credentials reach the container:

```
1docker compose exec auth env | grep GOTRUE_SMS
```

Common causes:

*   Provider credentials are in `.env` but the matching `GOTRUE_SMS_*` line is still commented out in `docker-compose.yml`
*   Provider credentials are wrong
*   Phone number format is wrong (use E.164 format: `+1234567890`)

### Variables added to the environment but not working[#](#variables-added-to-the-environment-but-not-working)

Configuration variables from `.env` are **not** automatically available inside the container unless there's a matching passthrough definition in `docker-compose.yml`. Check, e.g., for:

```
1docker compose exec auth env | grep -E 'GOTRUE_SMS|GOTRUE_MFA'
```

After changing the configuration environment variables, recreate the Auth service container:

```
1docker compose up -d --force-recreate --no-deps auth
```

### Rate limit errors[#](#rate-limit-errors)

If users see "rate limit exceeded" errors, check `SMS_MAX_FREQUENCY` (minimum interval between sends) and the global rate limit `GOTRUE_RATE_LIMIT_SMS_SENT` (default: 30 per hour).

### Additional resources[#](#additional-resources)

*   [Multi-Factor Authentication (Phone)](/docs/guides/auth/auth-mfa/phone)
*   [Multi-Factor Authentication (TOTP)](/docs/guides/auth/auth-mfa/totp)
*   [Auth server on GitHub](https://github.com/supabase/auth) (check README and `example.env`)
