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
nav_prev: {"path": "supabase/docs/guides/security/platform-security/index.md", "title": "Secure configuration of Supabase platform"}
nav_next: {"path": "supabase/docs/guides/security/security-testing/index.md", "title": "Security testing of your Supabase projects"}
---

# 

Secure configuration of Supabase products

* * *

The Supabase [production checklist](../../deployment/going-into-prod/index.md) provides detailed advice on preparing an app for production. While our [SOC 2](../soc-2-compliance/index.md) and [HIPAA](../hipaa-compliance/index.md) compliance documents outline the roles and responsibilities for building a secure and compliant app.

Various products at Supabase have their own hardening and configuration guides, below is a definitive list of these to help guide your way.

## Auth[#](#auth)

*   [Password security](../../auth/password-security/index.md)
*   [Rate limits](../../auth/rate-limits/index.md)
*   [Bot detection / Prevention](../../auth/auth-captcha/index.md)
*   [JWTs](../../auth/jwts/index.md)

## Database[#](#database)

*   [Row Level Security](../../database/postgres/row-level-security/index.md)
*   [Column Level Security](../../database/postgres/column-level-security/index.md)
*   [Hardening the Data API](../../api/hardening-data-api/index.md)
*   [Additional security controls for the Data API](../../api/securing-your-api/index.md)
*   [Custom claims and role based access control](../../api/custom-claims-and-role-based-access-control-rbac/index.md)
*   [Managing Postgres roles](../../database/postgres/roles/index.md)
*   [Managing secrets with Vault](../../database/vault/index.md)
*   [Superuser access and unsupported operations](docs/guides/database/postgres/roles-superuser)

## Storage[#](#storage)

*   [Object ownership](../../storage/security/ownership/index.md)
*   [Access control](../../storage/security/access-control/index.md)
    *   The Storage API docs contain hints about required [RLS policy permissions](/docs/reference/javascript/storage-createbucket)
*   [Custom roles with the storage schema](../../storage/schema/custom-roles/index.md)

## Realtime[#](#realtime)

*   [Authorization](docs/guides/realtime/authorization)
