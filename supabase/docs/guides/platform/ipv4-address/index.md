---
title: "Dedicated IPv4 Address for Ingress"
source: "https://supabase.com/docs/guides/platform/ipv4-address"
canonical_url: "https://supabase.com/docs/guides/platform/ipv4-address"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:36.911Z"
content_hash: "1cdeaf3e5e9d12d980cd431340970e031266a1e1ecaf0a7fcbd23739d6806091"
menu_path: ["Platform","Platform","Add-ons","Add-ons","IPv4 Address","IPv4 Address"]
section_path: ["Platform","Platform","Add-ons","Add-ons","IPv4 Address","IPv4 Address"]
---
# 

Dedicated IPv4 Address for Ingress

## 

Attach an IPv4 address to your database

* * *

The Supabase IPv4 add-on provides a dedicated IPv4 address for your Postgres database connection. It can be configured in the [Add-ons Settings](/dashboard/project/_/settings/addons).

## Understanding IP addresses[#](#understanding-ip-addresses)

The Internet Protocol (IP) addresses devices on the internet. There are two main versions:

*   **IPv4**: The older version, with a limited address space.
*   **IPv6**: The newer version, offering a much larger address space and the future-proof option.

## When you need the IPv4 add-on:[#](#when-you-need-the-ipv4-add-on)

IPv4 addresses are guaranteed to be static for ingress traffic. If your database is making outbound connections, the outbound IP address is not static and cannot be guaranteed.

*   When using the direct connection string in an IPv6-incompatible network instead of Supavisor or client libraries.
*   When you need a dedicated IP address for your direct connection string

## Enabling the IPv4 add-on[#](#enabling-the-ipv4-add-on)

You can enable the IPv4 add-on in your project's [add-ons settings](/dashboard/project/_/settings/addons).

You can also manage the IPv4 add-on using the Management API:

```
1# Get your access token from https://supabase.com/dashboard/account/tokens2export SUPABASE_ACCESS_TOKEN="your-access-token"3export PROJECT_REF="your-project-ref"45# Get current IPv4 add-on status6curl -X GET "https://api.supabase.com/v1/projects/$PROJECT_REF/billing/addons" \7  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN"89# Enable IPv4 add-on10curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/billing/addons" \11  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \12  -H "Content-Type: application/json" \13  -d '{14    "addon_variant": "ipv4_default",15    "addon_type": "ipv4"16  }'1718# Disable IPv4 add-on19curl -X DELETE "https://api.supabase.com/v1/projects/$PROJECT_REF/billing/addons/ipv4_default" \20  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN"
```

Note that direct database connections can experience a short amount of downtime when toggling the add-on due to DNS reconfiguration and propagation. Generally, this should be less than a minute.

## Read replicas and IPv4 add-on[#](#read-replicas-and-ipv4-add-on)

When using the add-on, each database (including read replicas) receives an IPv4 address. Each replica adds to the total IPv4 cost.

## Changes and updates[#](#changes-and-updates)

*   While the IPv4 address generally remains the same, actions like pausing/unpausing the project or enabling/disabling the add-on can lead to a new IPv4 address.

## Supabase and IPv6 compatibility[#](#supabase-and-ipv6-compatibility)

By default, Supabase Postgres use IPv6 addresses. If your system doesn't support IPv6, you have the following options:

1.  **Supavisor Connection Strings**: The Supavisor connection strings are IPv4-compatible alternatives to direct connections
2.  **Supabase Client Libraries**: These libraries are compatible with IPv4
3.  **Dedicated IPv4 Add-On (Pro Plans+)**: For a guaranteed IPv4 and static database address for the direct connection, enable this paid add-on.

### Checking your network IPv6 support[#](#checking-your-network-ipv6-support)

You can check if your personal network is IPv6 compatible at [https://test-ipv6.com](https://test-ipv6.com).

### Checking platforms for IPv6 support:[#](#checking-platforms-for-ipv6-support)

The majority of services are IPv6 compatible. However, there are a few prominent ones that only accept IPv4 connections:

*   [Retool](https://retool.com/)
*   [Vercel](https://vercel.com/)
*   [GitHub Actions](https://docs.github.com/en/actions)
*   [Render](https://render.com/)

## Finding your database's IP address[#](#finding-your-databases-ip-address)

Use an IP lookup website or this command (replace `<PROJECT_REF>`):

```
1nslookup db.<PROJECT_REF>.supabase.co
```

## Identifying your connections[#](#identifying-your-connections)

The pooler and direct connection strings can be found in the [project connect page](/dashboard/project/_?showConnect=true):

#### Direct connection[#](#direct-connection)

IPv6 unless IPv4 Add-On is enabled

```
1# Example direct connection string2postgresql://postgres:[YOUR-PASSWORD]@db.ajrbwkcuthywfihaarmflo.supabase.co:5432/postgres
```

#### Supavisor in transaction mode (port 6543)[#](#supavisor-in-transaction-mode-port-6543)

Always uses an IPv4 address

```
1# Example transaction string2postgresql://postgres.ajrbwkcuthywddfihrmflo:[YOUR-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:6543/postgres
```

#### Supavisor in session mode (port 5432)[#](#supavisor-in-session-mode-port-5432)

Always uses an IPv4 address

```
1# Example session string2postgresql://postgres.ajrbwkcuthywfddihrmflo:[YOUR-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:5432/postgres
```

## Pricing[#](#pricing)

For a detailed breakdown of how charges are calculated, refer to [Manage IPv4 usage](/docs/guides/platform/manage-your-usage/ipv4).
