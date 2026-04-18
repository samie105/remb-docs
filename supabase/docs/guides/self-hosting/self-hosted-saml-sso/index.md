---
title: "Configure SAML SSO"
source: "https://supabase.com/docs/guides/self-hosting/self-hosted-saml-sso"
canonical_url: "https://supabase.com/docs/guides/self-hosting/self-hosted-saml-sso"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:56.293Z"
content_hash: "6ad76bbde2b9a7913eead211f04f426392c40390d6a7c29fc384932688d54cb2"
menu_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Configure SAML 2.0 SSO","Configure SAML 2.0 SSO"]
section_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Configure SAML 2.0 SSO","Configure SAML 2.0 SSO"]
---
# 

Configure SAML SSO

## 

Set up SAML 2.0 Single Sign-On for self-hosted Supabase with Docker.

* * *

SAML 2.0 SSO lets your users authenticate through an enterprise Identity Provider (IdP) such as Okta, Azure AD (Entra ID), Google Workspace, or any SAML 2.0-compliant provider. Unlike OAuth providers, SAML IdPs are not configured through environment variables - they are managed dynamically at runtime through the Auth admin API.

This guide covers the full setup: generating a signing key, enabling SAML in your Supabase instance, registering an IdP, and integrating SSO into your application.

Client-side integration uses the same `supabase.auth.signInWithSSO()` method documented in the [SSO with SAML 2.0](/docs/guides/auth/enterprise-sso/auth-sso-saml) guide. This guide focuses on the self-hosted server configuration.

## Before you begin[#](#before-you-begin)

You need:

*   A running self-hosted Supabase instance (see the [setup guide](/docs/guides/self-hosting/docker))
*   Open SSL installed (for key generation)
*   Your IdP's SAML metadata URL or metadata XML
*   The `SERVICE_ROLE_KEY` from your `.env` file (needed for admin API calls)
*   `API_EXTERNAL_URL` set to the publicly-accessible URL of your Supabase Auth service (e.g., `https://<your-domain>`). This URL is used as the SAML Service Provider entity ID and for constructing the ACS endpoint URL

## How SAML SSO works in Supabase[#](#how-saml-sso-works-in-supabase)

SAML SSO is configured in two layers:

1.  **Global SAML enable (environment variables)** - a small set of env vars that enable the SAML engine and provide a signing key. These go in `.env` and `docker-compose.yml`.
2.  **Per-IdP configuration (admin API)** - individual Identity Providers are registered, updated, and deleted at runtime via the Auth admin API. No restart is needed when adding or removing providers.

The login flow works as follows:

1.  Your app calls `POST /auth/v1/sso` with a domain or provider\_id
2.  Auth generates a SAML `AuthnRequest` and returns a redirect URL to the IdP
3.  The user authenticates at the IdP
4.  The IdP POSTs a SAML Response to `POST /sso/saml/acs`
5.  Auth validates the assertion, creates or links the user, and issues a session
6.  The user is redirected back to your app with session tokens

## Step 1: Generate an RSA private key[#](#step-1-generate-an-rsa-private-key)

SAML requests must be signed. The value expected by `GOTRUE_SAML_PRIVATE_KEY` is a Base64-encoded PKCS#1 DER RSA private key (with a 2048-bit key as the minimum requirement). Generate it with:

```
1openssl genpkey -algorithm RSA -out pk_pkcs8.pem -quiet && \2openssl pkey -in pk_pkcs8.pem -out pk_rsa1.der -outform DER -traditional && \3base64 -w 0 -i pk_rsa1.der
```

The commands above:

1.  Generate an RSA private key in PKCS#8 PEM format
2.  Convert the key to PKCS#1 DER format
3.  Base64-encode the key for use as the value of `GOTRUE_SAML_PRIVATE_KEY`

Save the Base64 output - make sure to copy it as single line, ignoring the trailing newline. Remove the temporary files.

Keep this key secret. Anyone with the private key can forge SAML requests on behalf of your Service Provider. Do not commit it to the version control system.

For a production deployment, consider using a 4096-bit key by adding `-pkeyopt rsa_keygen_bits:4096` to the `openssl genpkey` command above.

## Step 2: Add environment variables[#](#step-2-add-environment-variables)

Add the following to your `.env` file:

```
1############2# SAML SSO3############45SAML_ENABLED=true6SAML_PRIVATE_KEY=<your-base64-encoded-private-key>78# Optional: accept encrypted SAML assertions from IdPs (default: false)9# SAML_ALLOW_ENCRYPTED_ASSERTIONS=false1011# Optional: how long relay state tokens remain valid (default: 2m0s)12# SAML_RELAY_STATE_VALIDITY_PERIOD=2m0s1314# Optional: override the SAML entity ID / ACS base URL15# Defaults to API_EXTERNAL_URL if not set16# SAML_EXTERNAL_URL=https://supabase.example.com:80001718# Optional: rate limit on the ACS endpoint (requests per second, default: 15)19# SAML_RATE_LIMIT_ASSERTION=15
```

## Step 3: Pass SAML variables to the Auth container[#](#step-3-pass-saml-variables-to-the-auth-container)

In `docker-compose.yml`, add the SAML environment variables to the `auth` service. Auth expects the `GOTRUE_` prefix for all of its configuration variables:

```
1auth:2  environment:3    # ... existing variables ...45    # SAML SSO6    GOTRUE_SAML_ENABLED: ${SAML_ENABLED}7    GOTRUE_SAML_PRIVATE_KEY: ${SAML_PRIVATE_KEY}8    # GOTRUE_SAML_ALLOW_ENCRYPTED_ASSERTIONS: ${SAML_ALLOW_ENCRYPTED_ASSERTIONS}9    # GOTRUE_SAML_RELAY_STATE_VALIDITY_PERIOD: ${SAML_RELAY_STATE_VALIDITY_PERIOD}10    # GOTRUE_SAML_EXTERNAL_URL: ${SAML_EXTERNAL_URL}11    # GOTRUE_SAML_RATE_LIMIT_ASSERTION: ${SAML_RATE_LIMIT_ASSERTION}
```

## Step 4: Restart the containers[#](#step-4-restart-the-containers)

Apply the configuration changes:

```
1docker compose down && \2docker compose up -d
```

Verify the Auth service is healthy:

```
1docker compose ps auth
```

## Step 5: Retrieve your service provider metadata[#](#step-5-retrieve-your-service-provider-metadata)

Once SAML is enabled, your Supabase instance exposes service provider (SP) metadata at `{API_EXTERNAL_URL}/sso/saml/metadata`.

Verify it using `curl`:

```
1curl http://<your-domain>/sso/saml/metadata
```

This returns an XML document containing your SP entity ID, ACS endpoint URL, and signing certificate. You will need to provide this to your IdP.

Add `?download=true` to the request URL to get the metadata as a downloadable XML file with a 5-year validity period - this is useful for IdPs that require a file upload instead of a URL.

Key values in the metadata:

Field

Value

Entity ID

`{API_EXTERNAL_URL}/sso/saml/metadata`

ACS URL

`{API_EXTERNAL_URL}/sso/saml/acs`

NameID formats

`persistent`, `emailAddress`

Signing certificate

Derived from your `SAML_PRIVATE_KEY`

## Step 6: Register an identity provider[#](#step-6-register-an-identity-provider)

Use the Auth admin API to register your IdP. You need the `SERVICE_ROLE_KEY` for authentication.

### Option A: Register with a metadata URL (recommended)[#](#option-a-register-with-a-metadata-url-recommended)

If your IdP provides a metadata URL, Auth will fetch and cache the metadata automatically and refresh it when it becomes stale:

```
1curl -X POST 'http://<your-domain>/auth/v1/admin/sso/providers' \2  -H 'Authorization: Bearer your-service-role-key' \3  -H 'Content-Type: application/json' \4  -H 'apikey: your-service-role-key' \5  -d '{6    "type": "saml",7    "metadata_url": "https://idp.example.com/saml/metadata",8    "domains": ["example.com"],9    "attribute_mapping": {10      "keys": {11        "email": {12          "name": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"13        },14        "name": {15          "name": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name"16        }17      }18    }19  }'
```

### Option B: Register with inline metadata XML[#](#option-b-register-with-inline-metadata-xml)

If you have the IdP metadata as an XML string:

```
1curl -X POST 'http://<your-domain>/auth/v1/admin/sso/providers' \2  -H 'Authorization: Bearer your-service-role-key' \3  -H 'Content-Type: application/json' \4  -H 'apikey: your-service-role-key' \5  -d '{6    "type": "saml",7    "metadata_xml": "<EntityDescriptor ...>...</EntityDescriptor>",8    "domains": ["example.com"]9  }'
```

When using `metadata_url`, the URL must use HTTPS. Auth validates the metadata XML format and checks that the EntityID is unique across all registered providers.

The response includes the provider `id` (UUID) - save this for use in your application or for later management:

```
1{2  "id": "d3f5a1b2-...",3  "resource_id": null,4  "disabled": false,5  "saml": {6    "entity_id": "https://idp.example.com/saml",7    "metadata_url": "https://idp.example.com/saml/metadata"8  },9  "domains": [{ "domain": "example.com" }],10  "created_at": "...",11  "updated_at": "..."12}
```

### Registration parameters reference[#](#registration-parameters-reference)

Parameter

Required

Description

`type`

Yes

Must be `"saml"`

`metadata_url`

One of these

HTTPS URL to the IdP's SAML metadata (auto-refreshed)

`metadata_xml`

One of these

Raw IdP metadata XML string

`domains`

No

Array of email domains to associate (e.g., `["acme.com"]`). Used for domain-based SSO lookup.

`attribute_mapping`

No

Map SAML attributes to user claims (see [Attribute mapping](#attribute-mapping))

`name_id_format`

No

Request a specific NameID format: `persistent`, `emailAddress`, `transient`, or `unspecified`

`resource_id`

No

A custom external identifier for the provider

`disabled`

No

Set to `true` to register but disable the provider

## Step 8: Configure your identity provider[#](#step-8-configure-your-identity-provider)

On the IdP side, create a new SAML application and configure it with your SP details:

IdP setting

Value

SP Entity ID / Audience

`{API_EXTERNAL_URL}/sso/saml/metadata`

ACS URL / Reply URL

`{API_EXTERNAL_URL}/sso/saml/acs`

NameID format

`persistent` (recommended) or `emailAddress`

Signing certificate

Upload from the SP metadata XML or provide the metadata URL

### IdP-specific configuration[#](#idp-specific-configuration)

**Okta setup:**

*   Create a "SAML 2.0" application
*   Single Sign-On URL: `{API_EXTERNAL_URL}/sso/saml/acs`
*   Audience URI (SP Entity ID): `{API_EXTERNAL_URL}/sso/saml/metadata`
*   Default RelayState: leave blank
*   Name ID format: `Persistent`

## Attribute mapping[#](#attribute-mapping)

Attribute mapping lets you control how SAML assertion attributes are translated into Supabase user claims. If no mapping is provided, Auth uses sensible defaults:

**Default email detection order:**

1.  `urn:oid:0.9.2342.19200300.100.1.3` (LDAP mail OID)
2.  `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`
3.  `http://schemas.xmlsoap.org/claims/EmailAddress`
4.  Attributes named `mail`, `Mail`, or `email`
5.  Subject NameID (if it looks like an email address)

**Default user ID detection:**

1.  `urn:oasis:names:tc:SAML:attribute:subject-id` attribute
2.  Subject NameID (if format is `persistent`)

### Custom attribute mapping example[#](#custom-attribute-mapping-example)

Map IdP-specific attributes to user metadata:

```
1{2  "attribute_mapping": {3    "keys": {4      "email": {5        "name": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"6      },7      "name": {8        "name": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name"9      },10      "department": {11        "name": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/department",12        "default": "unknown"13      },14      "groups": {15        "name": "http://schemas.microsoft.com/ws/2008/06/identity/claims/groups",16        "array": true17      },18      "role": {19        "names": ["http://schemas.microsoft.com/ws/2008/06/identity/claims/role", "role", "Role"],20        "default": "member"21      }22    }23  }24}
```

Each mapping key supports:

Field

Description

`name`

Primary SAML attribute name to look for (matched against both `Name` and `FriendlyName`, case-insensitive)

`names`

Array of fallback attribute names to try in order

`default`

Default value if the attribute is not present in the assertion

`array`

Set to `true` to collect all values (for multi-valued attributes like groups)

Mapped attributes are stored in the user's `raw_user_meta_data` and are available via `user.user_metadata` in your application.

## Managing providers[#](#managing-providers)

### List all providers[#](#list-all-providers)

```
1curl 'http://<your-domain>/auth/v1/admin/sso/providers' \2  -H 'Authorization: Bearer your-service-role-key' \3  -H 'apikey: your-service-role-key'
```

Filter by resource ID using exact match:

```
1curl 'http://<your-domain>/auth/v1/admin/sso/providers?resource_id=my-idp' \2  -H 'Authorization: Bearer your-service-role-key' \3  -H 'apikey: your-service-role-key'
```

or prefix match:

```
1curl 'http://<your-domain>/auth/v1/admin/sso/providers?resource_id_prefix=prod-' \2  -H 'Authorization: Bearer your-service-role-key' \3  -H 'apikey: your-service-role-key'
```

### Get a specific provider[#](#get-a-specific-provider)

```
1curl 'http://<your-domain>/auth/v1/admin/sso/providers/{provider_id}' \2  -H 'Authorization: Bearer your-service-role-key' \3  -H 'apikey: your-service-role-key'
```

### Update a provider[#](#update-a-provider)

```
1curl -X PUT 'http://<your-domain>/auth/v1/admin/sso/providers/{provider_id}' \2  -H 'Authorization: Bearer your-service-role-key' \3  -H 'Content-Type: application/json' \4  -H 'apikey: your-service-role-key' \5  -d '{6    "domains": ["example.com", "subsidiary.com"],7    "attribute_mapping": {8      "keys": {9        "email": {10          "name": "mail"11        }12      }13    }14  }'
```

### Disable a provider (without deleting)[#](#disable-a-provider-without-deleting)

```
1curl -X PUT 'http://<your-domain>/auth/v1/admin/sso/providers/{provider_id}' \2  -H 'Authorization: Bearer your-service-role-key' \3  -H 'Content-Type: application/json' \4  -H 'apikey: your-service-role-key' \5  -d '{ "disabled": true }'
```

### Delete a provider[#](#delete-a-provider)

```
1curl -X DELETE 'http://<your-domain>/auth/v1/admin/sso/providers/{provider_id}' \2  -H 'Authorization: Bearer your-service-role-key' \3  -H 'apikey: your-service-role-key'
```

## Client-side integration[#](#client-side-integration)

### Using supabase-js[#](#using-supabase-js)

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('http://<your-domain>', 'your-anon-key')45// Option 1: SSO by email domain6const { data, error } = await supabase.auth.signInWithSSO({7  domain: 'example.com',8})910// Option 2: SSO by provider ID11const { data, error } = await supabase.auth.signInWithSSO({12  providerId: 'd3f5a1b2-...',13})1415// Redirect the user to the IdP16if (data?.url) {17  window.location.href = data.url18}
```

Both methods return an object with a `url` property - redirect the user to this URL to begin authentication at the IdP.

### Using the REST API directly[#](#using-the-rest-api-directly)

By domain:

```
1curl -X POST 'http://<your-domain>/auth/v1/sso' \2  -H 'Content-Type: application/json' \3  -H 'apikey: your-anon-key' \4  -d '{5    "domain": "example.com",6    "skip_http_redirect": true7  }'
```

By provider ID:

```
1curl -X POST 'http://<your-domain>/auth/v1/sso' \2  -H 'Content-Type: application/json' \3  -H 'apikey: your-anon-key' \4  -d '{5    "provider_id": "d3f5a1b2-...",6    "skip_http_redirect": true7  }'
```

Both return `{ "url": "https://idp.example.com/sso?SAMLRequest=..." }`.

### Domain-based vs provider-based lookup[#](#domain-based-vs-provider-based-lookup)

Method

Use case

`domain`

Extract the domain from the user's email and let Auth find the right IdP. Best for login forms where the user enters their email first.

`providerId`

Use when you know the exact provider - for example, a dedicated "Sign in with Okta" button.

## Test the login flow[#](#test-the-login-flow)

1.  Open your application and trigger SSO login (or use the curl command above)
2.  You should be redirected to your IdP's login page
3.  After authenticating, the IdP posts back to the ACS endpoint
4.  Auth processes the assertion and redirects you back to your `SITE_URL` (or `redirect_to` URL) with session tokens

To verify the session was created:

```
1curl 'http://<your-domain>/auth/v1/user' \2  -H 'Authorization: Bearer user-session-token' \3  -H 'apikey: your-anon-key'
```

The response should include `app_metadata.provider: "sso:saml"` and any mapped attributes in `user_metadata`.

## Environment variable reference[#](#environment-variable-reference)

Variable

Default

Description

`SAML_ENABLED`

`false`

Enable the SAML SSO engine

`SAML_PRIVATE_KEY`

\-

Base64-encoded PKCS#1 RSA private key (min 2048-bit). Used to sign SAML requests and optionally decrypt assertions.

`SAML_ALLOW_ENCRYPTED_ASSERTIONS`

`false`

Accept encrypted SAML assertions from IdPs

`SAML_RELAY_STATE_VALIDITY_PERIOD`

`2m0s`

How long relay state tokens remain valid. Increase if users on slow networks time out during the IdP redirect.

`SAML_EXTERNAL_URL`

`API_EXTERNAL_URL`

Override the base URL used for the SAML entity ID and ACS endpoint. Only needed if the SAML endpoints are served on a different URL than the rest of the Auth API.

`SAML_RATE_LIMIT_ASSERTION`

`15`

Maximum ACS requests per second. Protects against assertion replay floods.

## Troubleshooting[#](#troubleshooting)

### "SAML is not enabled on this server"[#](#saml-is-not-enabled-on-this-server)

The `GOTRUE_SAML_ENABLED` variable is not set to `true`, or the Auth container did not pick up the change. Verify the env var is passed through `docker-compose.yml` and restart:

```
1docker compose down && docker compose up -d
```

### "Invalid private key" on startup[#](#invalid-private-key-on-startup)

The `GOTRUE_SAML_PRIVATE_KEY` value is malformed. Ensure it is:

*   Base64-encoded (single line, no line breaks)
*   In PKCS#1 format (`openssl pkey ... -traditional` output)
*   At least 2048-bit RSA

Regenerate if needed:

```
1openssl genpkey -algorithm RSA -out pk_pkcs8.pem -quiet && \2openssl pkey -in pk_pkcs8.pem -out pk_rsa1.der -outform DER -traditional && \3base64 -w 0 -i pk_rsa1.der
```

### IdP cannot reach the ACS endpoint[#](#idp-cannot-reach-the-acs-endpoint)

*   Verify `API_EXTERNAL_URL` is set to a URL the IdP can reach (not `localhost` unless testing locally)
*   Check that the Kong routes for `/sso/saml/acs` and `/sso/saml/metadata` are configured as open (no `key-auth` plugin).
*   Check the Auth container logs: `docker compose logs auth`

### "No SSO provider found for this domain"[#](#no-sso-provider-found-for-this-domain)

*   Verify the domain is registered: list providers and check the `domains` array
*   Domain matching is exact and case-insensitive - `Example.com` matches `example.com`

### Assertion validation fails[#](#assertion-validation-fails)

*   Ensure the IdP's signing certificate matches what is in the metadata registered with Auth
*   If using `metadata_url`, Auth automatically refreshes stale metadata (after `ValidUntil`, `CacheDuration`, or 24 hours). Force a refresh by updating the provider.
*   Check clock sync between your server and the IdP - SAML assertions have time-based validity windows (`NotBefore` / `NotOnOrAfter`)

### User is created but attributes are missing[#](#user-is-created-but-attributes-are-missing)

*   Check your `attribute_mapping` configuration. Use the IdP's SAML assertion viewer (most IdPs have one) to see the exact attribute names being sent.
*   Attribute names are matched case-insensitively against both the `Name` and `FriendlyName` fields in the assertion.
*   Mapped attributes appear in `user.user_metadata`.

### Relay state expired[#](#relay-state-expired)

The user took too long between initiating SSO and completing authentication at the IdP. Increase `GOTRUE_SAML_RELAY_STATE_VALIDITY_PERIOD` (default is 2 minutes).

## Additional resources[#](#additional-resources)

*   [SSO with SAML 2.0](/docs/guides/auth/enterprise-sso/auth-sso-saml) - Client-side SAML integration guide
*   [Auth server configuration reference](/docs/guides/self-hosting/auth/config) - Full list of Auth environment variables
*   [SAML 2.0 specification](http://docs.oasis-open.org/security/saml/v2.0/) - The underlying standard
