---
title: "Secure configuration of Supabase products"
source: "https://supabase.com/docs/guides/security/product-security"
canonical_url: "https://supabase.com/docs/guides/security/product-security"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:05.880Z"
content_hash: "b07d34eba33bc3c31c6c4bf67e620d0c3ea677b2bef2afdf6d3bd20e92bc6e5a"
menu_path: ["Security","Security","Product security","Product security","Product configuration","Product configuration"]
section_path: ["Security","Security","Product security","Product security","Product configuration","Product configuration"]
---
# 

Secure configuration of Supabase products

* * *

The Supabase [production checklist](/docs/guides/deployment/going-into-prod) provides detailed advice on preparing an app for production. While our [SOC 2](/docs/guides/security/soc-2-compliance) and [HIPAA](/docs/guides/security/hipaa-compliance) compliance documents outline the roles and responsibilities for building a secure and compliant app.

Various products at Supabase have their own hardening and configuration guides, below is a definitive list of these to help guide your way.

## Auth[#](#auth)

*   [Password security](/docs/guides/auth/password-security)
*   [Rate limits](/docs/guides/auth/rate-limits)
*   [Bot detection / Prevention](/docs/guides/auth/auth-captcha)
*   [JWTs](/docs/guides/auth/jwts)

## Database[#](#database)

*   [Row Level Security](/docs/guides/database/postgres/row-level-security)
*   [Column Level Security](/docs/guides/database/postgres/column-level-security)
*   [Hardening the Data API](/docs/guides/api/hardening-data-api)
*   [Additional security controls for the Data API](/docs/guides/api/securing-your-api)
*   [Custom claims and role based access control](/docs/guides/api/custom-claims-and-role-based-access-control-rbac)
*   [Managing Postgres roles](/docs/guides/database/postgres/roles)
*   [Managing secrets with Vault](/docs/guides/database/vault)
*   [Superuser access and unsupported operations](docs/guides/database/postgres/roles-superuser)

## Storage[#](#storage)

*   [Object ownership](/docs/guides/storage/security/ownership)
*   [Access control](/docs/guides/storage/security/access-control)
    *   The Storage API docs contain hints about required [RLS policy permissions](/docs/reference/javascript/storage-createbucket)
*   [Custom roles with the storage schema](/docs/guides/storage/schema/custom-roles)

## Realtime[#](#realtime)

*   [Authorization](docs/guides/realtime/authorization)
