---
title: "Postgres SSL Enforcement"
source: "https://supabase.com/docs/guides/platform/ssl-enforcement"
canonical_url: "https://supabase.com/docs/guides/platform/ssl-enforcement"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:14.825Z"
content_hash: "262d75a6cca8650668264d05eb629995aa8423dc18524abc302fdf3d786a4a59"
menu_path: ["Platform","Platform","Platform Configuration","Platform Configuration","SSL Enforcement","SSL Enforcement"]
section_path: ["Platform","Platform","Platform Configuration","Platform Configuration","SSL Enforcement","SSL Enforcement"]
nav_prev: {"path": "../regions/index.md", "title": "Available regions"}
nav_next: {"path": "../sso/index.md", "title": "Enable SSO for Your Organization"}
---

# 

Postgres SSL Enforcement

* * *

Your Supabase project supports connecting to the Postgres DB without SSL enabled to maximize client compatibility. For increased security, you can prevent clients from connecting if they're not using SSL.

Disabling SSL enforcement only applies to connections to Postgres and Supavisor ("Connection Pooler"); all HTTP APIs offered by Supabase (e.g., PostgREST, Storage, Auth) automatically enforce SSL on all incoming connections.

Applying or updating SSL enforcement triggers a fast database reboot. On small projects this usually completes in a few seconds, but larger databases may see a longer interruption.

## Manage SSL enforcement via the dashboard[#](#manage-ssl-enforcement-via-the-dashboard)

SSL enforcement can be configured via the "Enforce SSL on incoming connections" setting under the SSL Configuration section in [Database Settings page](/dashboard/project/_/database/settings) of the dashboard.

Updating SSL enforcement requires a brief database reboot. This restarts only the database and involves a few minutes of downtime.

## Manage SSL enforcement via the Management API[#](#manage-ssl-enforcement-via-the-management-api)

You can also manage SSL enforcement using the Management API:

```
1# Get your access token from https://supabase.com/dashboard/account/tokens2export SUPABASE_ACCESS_TOKEN="your-access-token"3export PROJECT_REF="your-project-ref"45# Get current SSL enforcement status6curl -X GET "https://api.supabase.com/v1/projects/$PROJECT_REF/ssl-enforcement" \7  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN"89# Enable SSL enforcement10curl -X PUT "https://api.supabase.com/v1/projects/$PROJECT_REF/ssl-enforcement" \11  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \12  -H "Content-Type: application/json" \13  -d '{14    "requestedConfig": {15      "database": true16    }17  }'1819# Disable SSL enforcement20curl -X PUT "https://api.supabase.com/v1/projects/$PROJECT_REF/ssl-enforcement" \21  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \22  -H "Content-Type: application/json" \23  -d '{24    "requestedConfig": {25      "database": false26    }27  }'
```

## Manage SSL enforcement via the CLI[#](#manage-ssl-enforcement-via-the-cli)

To get started:

1.  [Install](/docs/guides/cli) the Supabase CLI 1.37.0+.
2.  [Log in](/docs/guides/getting-started/local-development#log-in-to-the-supabase-cli) to your Supabase account using the CLI.
3.  Ensure that you have [Owner or Admin permissions](/docs/guides/platform/access-control#manage-team-members) for the project that you are enabling SSL enforcement.

### Check enforcement status[#](#check-enforcement-status)

You can use the `get` subcommand of the CLI to check whether SSL is currently being enforced:

```
1supabase ssl-enforcement --project-ref {ref} get --experimental
```

Response if SSL is being enforced:

```
1SSL is being enforced.
```

Response if SSL is not being enforced:

```
1SSL is *NOT* being enforced.
```

### Update enforcement[#](#update-enforcement)

The `update` subcommand is used to change the SSL enforcement status for your project:

```
1supabase ssl-enforcement --project-ref {ref} update --enable-db-ssl-enforcement --experimental
```

Similarly, to disable SSL enforcement:

```
1supabase ssl-enforcement --project-ref {ref} update --disable-db-ssl-enforcement --experimental
```

### A note about Postgres SSL modes[#](#a-note-about-postgres-ssl-modes)

Postgres supports [multiple SSL modes](https://www.postgresql.org/docs/current/libpq-ssl.html#LIBPQ-SSL-PROTECTION) on the client side. These modes provide different levels of protection. Depending on your needs, it is important to verify that the SSL mode in use is performing the required level of enforcement and verification of SSL connections.

SSL Mode

Encryption

Verifies CA

Verifies Hostname

Description

`disable`

No

No

No

SSL is not used. All data is transmitted in plaintext.

`allow`

Optional

No

No

Tries a non-SSL connection first; falls back to SSL if the server requires it.

`prefer`

Optional

No

No

Tries an SSL connection first; falls back to non-SSL if the server doesn't support it. This is the default.

`require`

Yes

No

No

Always uses SSL, but does not verify the server certificate or hostname.

`verify-ca`

Yes

Yes

No

Uses SSL and verifies that the server certificate is signed by a trusted CA.

`verify-full`

Yes

Yes

Yes

Uses SSL, verifies the CA certificate, and confirms the hostname matches the certificate. Recommended when SSL enforcement is enabled.

The strongest mode offered by Postgres is `verify-full` and this is the mode you most likely want to use when SSL enforcement is enabled. To use `verify-full` you will need to download the Supabase CA certificate for your database. The certificate is available through the dashboard under the SSL Configuration section in the [Database Settings page](/dashboard/project/_/database/settings).

Once the CA certificate has been downloaded, add it to the certificate authority list used by Postgres.

```
1cat {location of downloaded prod-ca-2021.crt} >> ~/.postgres/root.crt
```

With the CA certificate added to the trusted certificate authorities list, use `psql` or your client library to connect to Supabase:

```
1psql "postgresql://aws-0-eu-central-1.pooler.supabase.com:6543/postgres?sslmode=verify-full" -U postgres.<user>
```
