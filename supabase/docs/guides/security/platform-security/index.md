---
title: "Secure configuration of Supabase platform"
source: "https://supabase.com/docs/guides/security/platform-security"
canonical_url: "https://supabase.com/docs/guides/security/platform-security"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:04.290Z"
content_hash: "67a086994fb11bf805b7ea3ab9239c157c063a705b66e6f4ebfd3eb4dc595b86"
menu_path: ["Security","Security","Product security","Product security","Platform configuration","Platform configuration"]
section_path: ["Security","Security","Product security","Product security","Platform configuration","Platform configuration"]
---
# 

Secure configuration of Supabase platform

* * *

The Supabase hosted platform provides a secure by default configuration. Some organizations may however require further security controls to meet their own security policies or compliance requirements.

Access to additional security controls can be found under the [security tab](/dashboard/org/_/security) for organizations.

## Available controls[#](#available-controls)

Additional security controls are under active development. Any changes will be published here and in our [changelog](/changelog).

### Enforce multi-factor authentication (MFA)[#](#enforce-multi-factor-authentication-mfa)

Organization owners can choose to enforce MFA for all team members.

For configuration information, see [Enforce MFA on Organization](/docs/guides/platform/mfa/org-mfa-enforcement)

### SSO for organizations[#](#sso-for-organizations)

Supabase offers single sign-on (SSO) as a login option to provide additional account security for your team. This allows company administrators to enforce the use of an identity provider when logging into Supabase.

For configuration information, see [Enable SSO for Your Organization](/docs/guides/platform/sso).

### Postgres SSL enforcement[#](#postgres-ssl-enforcement)

Supabase projects support connecting to the Postgres DB without SSL enforced to maximize client compatibility. For increased security, you can prevent clients from connecting if they're not using SSL.

For configuration information, see [Postgres SSL Enforcement](/docs/guides/platform/ssl-enforcement)

Controlling this at the organization level is on our roadmap.

### Network restrictions[#](#network-restrictions)

Each Supabase project comes with configurable restrictions on the IP ranges that are allowed to connect to Postgres and its pooler ("your database"). These restrictions are enforced before traffic reaches the database. If a connection is not restricted by IP, it still needs to authenticate successfully with valid database credentials.

For configuration information, see [Network Restrictions](/docs/guides/platform/network-restrictions)

Controlling this at the organization level is on our roadmap.

### PrivateLink[#](#privatelink)

PrivateLink provides enterprise-grade private network connectivity between your AWS VPC and your Supabase database using AWS VPC Lattice. This eliminates exposure to the public internet by creating a secure, private connection that keeps your database traffic within the AWS network backbone.

For configuration information, see [PrivateLink](/docs/guides/platform/privatelink)

PrivateLink is currently in beta. To establish PrivateLink with a Read Replica, reach out to your account rep.
