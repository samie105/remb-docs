---
title: "New API Keys and Asymmetric Authentication"
source: "https://supabase.com/docs/guides/self-hosting/self-hosted-auth-keys"
canonical_url: "https://supabase.com/docs/guides/self-hosting/self-hosted-auth-keys"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:36.868Z"
content_hash: "9511a3b517eaa0539a3467e66f582f8eea7f3476a0e6de4c5e144b700e648d5c"
menu_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Configure new API keys","Configure new API keys"]
section_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Configure new API keys","Configure new API keys"]
nav_prev: {"path": "supabase/docs/guides/self-hosting/restore-from-platform/index.md", "title": "Restore a Platform Project to Self-Hosted"}
nav_next: {"path": "supabase/docs/guides/self-hosting/self-hosted-oauth/index.md", "title": "Configure Social Login (OAuth) Providers"}
---

# 

New API Keys and Asymmetric Authentication

## 

Configure new API keys and ES256 asymmetric authentication for self-hosted Supabase.

* * *

You can configure self-hosted Supabase to use the [new API keys](/docs/guides/api/api-keys) alongside the legacy API keys (`ANON_KEY` and `SERVICE_ROLE_KEY` HS256-signed JWTs).

## Before you begin[#](#before-you-begin)

*   Complete the [Docker setup guide](/docs/guides/self-hosting/docker), including running `generate-keys.sh` so that `JWT_SECRET`, `ANON_KEY`, and `SERVICE_ROLE_KEY` are set in your `.env` file.
*   Ensure `openssl` and `node` version 16 or newer are available on the machine where you will generate new keys.
*   If you are upgrading an existing self-hosted Supabase environment, make sure to check the [changelog](https://github.com/supabase/supabase/blob/master/docker/CHANGELOG.md) and add/update the following files:
    *   `.env.example` (merge new sections into your `.env` file)
    *   `docker-compose.yml`
    *   `utils/add-new-auth-keys.sh`
    *   `utils/rotate-new-api-keys.sh`
    *   `volumes/api/kong-entrypoint.sh`
    *   `volumes/api/kong.yml`

## Adding the new keys[#](#adding-the-new-keys)

From your project directory where you have `docker-compose.yml`:

```
1sh utils/add-new-auth-keys.sh --update-env
```

This generates new configuration environment variables and writes them to `.env`. Without `--update-env`, the script prints the values and prompts you interactively.

The script reads `JWT_SECRET` from `.env` and includes it as a symmetric key inside both `JWT_KEYS` and `JWT_JWKS`. If you later change `JWT_SECRET`, you must regenerate the JWKS as well.

After updating `.env`, enable new authentication by uncommenting these lines in `docker-compose.yml`:

```
1auth:2  environment:3    # JSON array of signing JWKs (EC private + legacy symmetric)4    GOTRUE_JWT_KEYS: ${JWT_KEYS:-[]}56realtime:7  environment:8    # JWKS for token verification (EC public + legacy symmetric)9    API_JWT_JWKS: ${JWT_JWKS:-{"keys":[]}}1011storage:12  environment:13    # JWKS for token verification (EC public + legacy symmetric)14    JWT_JWKS: ${JWT_JWKS:-{"keys":[]}}
```

PostgREST does not need uncommenting - it already uses `PGRST_JWT_SECRET: ${JWT_JWKS:-${JWT_SECRET}}` which automatically picks up `JWT_JWKS` when set.

Then restart all services:

```
1docker compose down && docker compose up -d
```

### New API keys format[#](#new-api-keys-format)

The new API keys use the [same format](/docs/guides/api/api-keys) as the Supabase platform:

```
1sb_publishable_<22-char-random>_<8-char-checksum>2sb_secret_<22-char-random>_<8-char-checksum>
```

### Verifying the setup[#](#verifying-the-setup)

Test with the new publishable key:

```
1curl http://<your-domain>/rest/v1/ \2-H "apikey: your-supabase-publishable-key"
```

You should receive a valid response from PostgREST. Then verify that the legacy key still works:

```
1curl http://<your-domain>/rest/v1/ \2-H "apikey: your-anon-key"
```

Both should work and return the same result.

You can also verify the public JWKS endpoint:

```
1curl http://<your-domain>/auth/v1/.well-known/jwks.json
```

This should return the EC public key (the symmetric key is excluded). Third-party services can use this endpoint to obtain the public key and verify asymmetric user session JWTs without needing the private key.

### Environment variables configuration[#](#environment-variables-configuration)

New variables default to empty values in `.env.example`. When empty, the API gateway and all services operate in legacy-only mode: `sb_publishable` and `sb_secret` API keys are not configured.

Environment variable (existing and new)

Type

Description

`JWT_SECRET`

Symmetric secret

**Existing:** Shared secret for signing and verifying HS256 JWTs. Used by multiple services.

`ANON_KEY`

HS256 JWT

**Existing:** Legacy client-side API key. Embedded JWT with `role: "anon"`.

`SERVICE_ROLE_KEY`

HS256 JWT

**Existing:** Legacy server-side API key. Embedded JWT with `role: "service_role"`.

`SUPABASE_PUBLISHABLE_KEY`

Opaque

**New:** Short random key with checksum. Replaces `ANON_KEY` for **client-side** use.

`SUPABASE_SECRET_KEY`

Opaque

**New:** Short random key with checksum. Replaces `SERVICE_ROLE_KEY` for **server-side** use.

`JWT_KEYS`

JSON array

**New:** JSON array of signing JWKs containing the new asymmetric key pair and the legacy symmetric key. Used by Auth to sign tokens.

`JWT_JWKS`

JWKS (JSON)

**New:** Contains the new public key and the legacy symmetric key. Used by PostgREST, Realtime, and Storage to verify tokens.

### Differences from the Supabase platform[#](#differences-from-the-supabase-platform)

*   **One key per role.** Self-hosted Supabase supports a single `sb_publishable` and a single `sb_secret`. The platform allows creating multiple `sb_` keys per project.
*   **No checksum validation.** The opaque keys use the same format as the platform (`sb_publishable_<random>_<checksum>`), but the API gateway does not validate the checksum. Keys are matched as opaque strings by the API gateway.

### Backward compatibility[#](#backward-compatibility)

The new authentication configuration is fully backward compatible:

*   **All new variables are optional.** If left with empty values, the API gateway (Kong) and all services behave exactly as before.
*   **Kong accepts both key types simultaneously.** You can migrate clients incrementally - some using legacy API keys, others using the new ones.
*   **JWKS includes the symmetric key.** `JWT_JWKS` contains both the EC public key (for verifying new ES256 tokens) and the legacy `JWT_SECRET` as a symmetric JWK (for verifying old HS256 tokens). Services that receive `JWT_JWKS` can verify both token types.
*   **Services fall back gracefully.** PostgREST uses `${JWT_JWKS:-${JWT_SECRET}}` - if `JWT_JWKS` is empty, it uses `JWT_SECRET` directly.
*   **No database changes required.** The asymmetric key system operates entirely at the API gateway and service configuration layer.

When `JWT_KEYS` is set, Auth will start signing new user session JWTs with the new asymmetric ES256 key pair. Make sure all services that verify tokens (PostgREST, Realtime, Storage) are configured with `JWT_JWKS` so they can verify both the new ES256 and legacy HS256 tokens.

## Rotating the new API keys[#](#rotating-the-new-api-keys)

If your new API keys are compromised or you want to rotate them periodically, you can regenerate `sb_publishable` and `sb_secret` without touching the asymmetric key pair:

```
1sh utils/rotate-new-api-keys.sh --update-env
```

After rotating, restart services and update your client applications with the new keys:

```
1docker compose down && docker compose up -d
```

Rotating new API keys does not invalidate existing user sessions. User session JWTs issued by Auth are unaffected because they are verified using the asymmetric key pair, which remains unchanged.

## Regenerating asymmetric key pair[#](#regenerating-asymmetric-key-pair)

If the EC private key is compromised or you need to regenerate everything:

```
1sh utils/add-new-auth-keys.sh --update-env
```

This generates a new EC P-256 key pair, new JWKS, new asymmetric JWTs, and new `sb_` API keys. After updating `.env` and restarting services:

*   New user session tokens will be signed with the new EC key.
*   Existing user session tokens signed with the old EC key will fail verification. Users will need to sign in again.
*   Existing user session tokens signed with the legacy symmetric key (`JWT_SECRET`) will continue to work, since `JWT_SECRET` hasn't changed and is still included in the new JWKS.

Regenerating asymmetric keys invalidates all ES256 user sessions. Plan a maintenance window if your users have active sessions.

## How it works[#](#how-it-works)

Below are a few notes on the details of the new authentication architecture.

### What client SDK sends[#](#what-client-sdk-sends)

Every request via `supabase-js` includes two headers:

*   `apikey` - the API key (`sb_` or legacy JWT)
*   `Authorization` - when unauthenticated, the client SDK copies the API key here (`Bearer sb_publishable_xxx` or `Bearer eyJ...`). When authenticated, this contains the user session JWT minted by Auth.

For **Realtime WebSocket** connections, the API key is sent as a `?apikey=` query parameter in the upgrade URL instead of an `apikey` header.

**Storage** and **Edge Functions** accept requests without an API key. These services handle their own authentication.

### API gateway routing[#](#api-gateway-routing)

Kong is configured with two consumers that each accept both the legacy and new API keys:

```
1consumers:2  - username: anon3    keyauth_credentials:4      - key: $SUPABASE_ANON_KEY # legacy HS256 JWT (ANON_KEY)5      - key: $SUPABASE_PUBLISHABLE_KEY # new opaque key (omitted when not configured)6  - username: service_role7    keyauth_credentials:8      - key: $SUPABASE_SERVICE_KEY # legacy HS256 JWT (SERVICE_ROLE_KEY)9      - key: $SUPABASE_SECRET_KEY # new opaque key (omitted when not configured)
```

When new API keys have not been added yet, the `kong-entrypoint.sh` script removes the empty credential entries before Kong loads the config.

To assist with the authorization flows a specialized configuration in `kong.yml` substitutes internal, gateway-level-only pre-signed JWTs for `sb_publishable` and `sb_secret` API keys. These pre-signed JWTs are also auto-configured in `.env` but **should not** be used in any application code.

Route

Service

API key required

Header substitution

`/auth/v1/*`

Auth

Yes

`Authorization`

`/rest/v1/*`

PostgREST

Yes

`Authorization`

`/graphql/v1`

PostgREST

Yes

`Authorization`

`/realtime/v1/api/*`

Realtime (REST)

Yes

`Authorization`

`/realtime/v1/*`

Realtime (WebSocket)

Yes

`x-api-key`

`/storage/v1/*`

Storage

No

`Authorization`

`/functions/v1/*`

Edge Functions

No

\-

### Request flows[#](#request-flows)

The API gateway (Kong) configuration has the logic to decide what `Authorization` header the upstream service, such as Auth, receives. The logic handles two cases: requests that only carry an API key (no user session), and requests that carry a user session JWT.

#### Unauthenticated requests (API key only, no user session JWT)[#](#unauthenticated-requests-api-key-only-no-user-session-jwt)

When the client sends only an `apikey` header with the API key (no `Authorization` header), or also the API key duplicated in `Authorization` by `supabase-js`:

1.  The client sends `apikey: sb_publishable_xxx` (or legacy `apikey: eyJ...`).
2.  The API gateway checks the key and identifies the consumer (`anon` or `service_role`).
3.  The API gateway inspects the `Authorization` header. Since it is either absent or starts with `Bearer sb_` (an opaque key, not a session JWT), the plugin replaces it:
    *   **The new `sb_` key:** `Authorization` header is set to the internal pre-signed ES256 JWT that corresponds to the role.
    *   **The Legacy JWT key:** `Authorization` header is set to the legacy HS256 JWT (the `apikey` value is copied as-is).
4.  The upstream service receives a valid JWT in `Authorization` and verifies it using `JWT_JWKS` (or `JWT_SECRET`).

#### Authenticated requests (user session JWT)[#](#authenticated-requests-user-session-jwt)

When the client has previously signed in through Auth and has a valid user session JWT token:

1.  The client sends `Authorization: Bearer eyJ...` (a JWT session token from Auth) alongside `apikey: sb_publishable_xxx` (or legacy `apikey: eyJ...`).
2.  The API gateway checks the API key and identifies the consumer.
3.  The API gateway inspects the `Authorization` header. Since it exists and does **not** start with `Bearer sb_` (it's a real JWT, not an `sb_` API key), the plugin **passes it through unchanged**. This works the same way regardless of whether the `apikey` is a new `sb_` key or a legacy JWT - the gateway only looks at the `Authorization` header to decide whether a user session is present.
4.  The upstream service verifies the session JWT. If Auth signed it with ES256 (when `JWT_KEYS` is configured), verification uses the EC public key. If Auth signed it with HS256 (legacy), verification uses the symmetric key. Both keys are available in `JWT_JWKS`.

The `request-transformer` expression in `kong.yml` implements this as a single Lua conditional:

```
1-- Pseudocode for the Authorization header logic:2if authorization exists AND does not start with "Bearer sb_" then3  -- User session JWT: pass through unchanged4  keep authorization5elseif apikey matches secret key then6  -- Replace with pre-signed service_role ES256 JWT7  set authorization = "Bearer <service_role ES256 JWT>"8elseif apikey matches publishable key then9  -- Replace with pre-signed anon ES256 JWT10  set authorization = "Bearer <anon ES256 JWT>"11else12  -- Legacy JWT key: copy apikey as authorization13  set authorization = apikey14end
```

## Additional resources[#](#additional-resources)

*   [Understanding API keys](/docs/guides/api/api-keys) - How API keys work on the Supabase platform
*   [Auth architecture](/docs/guides/auth/architecture) - How the Auth service handles authentication and token signing
*   [JWT Signing Keys](/docs/guides/auth/signing-keys) - Best practices on managing keys used by Supabase Auth to create and verify JSON Web Tokens
*   [JSON Web Token (JWT)](/docs/guides/auth/jwts) - How to best use JSON Web Tokens with Supabase
*   [Self-hosting with Docker](/docs/guides/self-hosting/docker) - Initial setup guide, including legacy key generation

On GitHub:

*   [Upcoming changes to Supabase API Keys (Discussion #29260)](https://github.com/orgs/supabase/discussions/29260)
*   [Supabase Auth: Asymmetric Keys support (Discussion #29289)](https://github.com/orgs/supabase/discussions/29289)
