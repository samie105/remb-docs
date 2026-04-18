---
title: "Network Restrictions"
source: "https://supabase.com/docs/guides/platform/network-restrictions"
canonical_url: "https://supabase.com/docs/guides/platform/network-restrictions"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:55.966Z"
content_hash: "e0ead273204831b1a51272bf70f71d21aa1385f6c24b2fe337d225dca45afa1a"
menu_path: ["Platform","Platform","Platform Configuration","Platform Configuration","Network Restrictions","Network Restrictions"]
section_path: ["Platform","Platform","Platform Configuration","Platform Configuration","Network Restrictions","Network Restrictions"]
---
# 

Network Restrictions

* * *

If you can't find the Network Restrictions section at the bottom of your [Database Settings](/dashboard/project/_/database/settings), update your version of Postgres in the [Infrastructure Settings](/dashboard/project/_/settings/infrastructure).

Each Supabase project comes with configurable restrictions on the IP ranges that are allowed to connect to Postgres and its pooler ("your database"). These restrictions are enforced before traffic reaches your database. If a connection is not restricted by IP, it still needs to authenticate successfully with valid database credentials.

If direct connections to your database [resolve to a IPv6 address](/dashboard/project/_/database/settings), you need to add both IPv4 and IPv6 CIDRs to the list of allowed CIDRs. Network Restrictions will be applied to all database connection routes, whether pooled or direct. You will need to add both the IPv4 and IPv6 networks you want to allow. There are two exceptions: If you have been granted an extension on the IPv6 migration OR if you have purchased the [IPv4 add-on](/dashboard/project/_/settings/addons), you need only add IPv4 CIDRs.

## To get started via the Dashboard:[#](#to-get-started-via-the-dashboard)

Network restrictions can be configured in the [Database Settings](/dashboard/project/_/database/settings) page. Ensure that you have [Owner or Admin permissions](/docs/guides/platform/access-control#manage-team-members) for the project that you are enabling network restrictions.

## To get started via the Management API:[#](#to-get-started-via-the-management-api)

You can also manage network restrictions using the Management API:

```
1# Get your access token from https://supabase.com/dashboard/account/tokens2export SUPABASE_ACCESS_TOKEN="your-access-token"3export PROJECT_REF="your-project-ref"45# Get current network restrictions6curl -X GET "https://api.supabase.com/v1/projects/$PROJECT_REF/network-restrictions" \7  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN"89# Update network restrictions10curl -X POST "https://api.supabase.com/v1/projects/$PROJECT_REF/network-restrictions/apply" \11  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \12  -H "Content-Type: application/json" \13  -d '{14    "db_allowed_cidrs": [15      "192.168.0.1/24",16    ]17  }'
```

## To get started via the CLI:[#](#to-get-started-via-the-cli)

1.  [Install](/docs/guides/cli) the Supabase CLI 1.22.0+.
2.  [Log in](/docs/guides/cli/local-development#log-in-to-the-supabase-cli) to your Supabase account using the CLI.
3.  If your project was created before 23rd December 2022, it will need to be [upgraded to the latest Supabase version](/docs/guides/platform/migrating-and-upgrading-projects) before Network Restrictions can be used.
4.  Ensure that you have [Owner or Admin permissions](/docs/guides/platform/access-control#manage-team-members) for the project that you are enabling network restrictions.

### Check restrictions[#](#check-restrictions)

You can use the `get` subcommand of the CLI to retrieve the restrictions currently in effect.

If restrictions have been applied, the output of the `get` command will reflect the IP ranges allowed to connect:

```
1> supabase network-restrictions --project-ref {ref} get --experimental2DB Allowed IPv4 CIDRs: &[183.12.1.1/24]3DB Allowed IPv6 CIDRs: &[2001:db8:3333:4444:5555:6666:7777:8888/64]4Restrictions applied successfully: true
```

If restrictions have never been applied to your project, the list of allowed CIDRs will be empty, but they will also not have been applied ("Restrictions applied successfully: false"). As a result, all IPs are allowed to connect to your database:

```
1> supabase network-restrictions --project-ref {ref} get --experimental2DB Allowed IPv4 CIDRs: []3DB Allowed IPv6 CIDRs: []4Restrictions applied successfully: false
```

### Update restrictions[#](#update-restrictions)

The `update` subcommand is used to apply network restrictions to your project:

```
1> supabase network-restrictions --project-ref {ref} update --db-allow-cidr 183.12.1.1/24 --db-allow-cidr 2001:db8:3333:4444:5555:6666:7777:8888/64 --experimental2DB Allowed IPv4 CIDRs: &[183.12.1.1/24]3DB Allowed IPv6 CIDRs: &[2001:db8:3333:4444:5555:6666:7777:8888/64]4Restrictions applied successfully: true
```

The restrictions specified (in the form of CIDRs) replaces any restrictions that might have been applied in the past. To add to the existing restrictions, you must include the existing restrictions within the list of CIDRs provided to the `update` command.

### Remove restrictions[#](#remove-restrictions)

To remove all restrictions on your project, you can use the `update` subcommand with the CIDR `0.0.0.0/0`:

```
1> supabase network-restrictions --project-ref {ref} update --db-allow-cidr 0.0.0.0/0 --db-allow-cidr ::/0 --experimental2DB Allowed IPv4 CIDRs: &[0.0.0.0/0]3DB Allowed IPv6 CIDRs: &[::/0]4Restrictions applied successfully: true
```

## Limitations[#](#limitations)

*   The current iteration of Network Restrictions applies to connections to Postgres and the database pooler; it doesn't currently apply to APIs offered over HTTPS (e.g., PostgREST, Storage, and Auth). This includes using Supabase client libraries like [supabase-js](/docs/reference/javascript).
*   If network restrictions are enabled, direct access to your database from Edge Functions will always be blocked. Using the Supabase client library [supabase-js](/docs/reference/javascript) is recommended to connect to a database with network restrictions from Edge Functions.
