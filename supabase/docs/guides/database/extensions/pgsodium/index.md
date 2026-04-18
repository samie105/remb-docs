---
title: "pgsodium (pending deprecation): Encryption Features"
source: "https://supabase.com/docs/guides/database/extensions/pgsodium"
canonical_url: "https://supabase.com/docs/guides/database/extensions/pgsodium"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:05.062Z"
content_hash: "60132c6530001c720490dd8f6b38f7e199d462d19fe57172e956279e25d5bb86"
menu_path: ["Database","Database","Extensions","Extensions","pgsodium (pending deprecation): Encryption Features","pgsodium (pending deprecation): Encryption Features"]
section_path: ["Database","Database","Extensions","Extensions","pgsodium (pending deprecation): Encryption Features","pgsodium (pending deprecation): Encryption Features"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/pgvector/index.md", "title": "pgvector: Embeddings and vector similarity"}
nav_next: {"path": "supabase/docs/guides/database/extensions/pgtap/index.md", "title": "pgTAP: Unit Testing"}
---

# 

pgsodium (pending deprecation): Encryption Features

* * *

Supabase DOES NOT RECOMMEND any new usage of [`pgsodium`](https://github.com/michelp/pgsodium).

The [`pgsodium`](https://github.com/michelp/pgsodium) extension is expected to go through a deprecation cycle in the near future. We will reach out to owners of impacted projects to assist with migrations away from [`pgsodium`](https://github.com/michelp/pgsodium) once the deprecation process begins.

The [Vault extension](/docs/guides/database/vault) won’t be impacted. Its internal implementation will shift away from pgsodium, but the interface and API will remain unchanged.

[`pgsodium`](https://github.com/michelp/pgsodium) is a Postgres extension which provides SQL access to [`libsodium`'s](https://doc.libsodium.org/) high-level cryptographic algorithms.

Supabase previously documented two features derived from pgsodium. Namely [Server Key Management](https://github.com/michelp/pgsodium#server-key-management) and [Transparent Column Encryption](https://github.com/michelp/pgsodium#transparent-column-encryption). At this time, we do not recommend using either on the Supabase platform due to their high level of operational complexity and misconfiguration risk.

Note that Supabase projects are encrypted at rest by default which likely is sufficient for your compliance needs e.g. SOC2 & HIPAA.

## Get the root encryption key for your Supabase project[#](#get-the-root-encryption-key-for-your-supabase-project)

Encryption requires keys. Keeping the keys in the same database as the encrypted data would be unsafe. For more information about managing the `pgsodium` root encryption key on your Supabase project see **[encryption key location](/docs/guides/database/vault#encryption-key-location)**. This key is required to decrypt values stored in [Supabase Vault](/docs/guides/database/vault) and data encrypted with Transparent Column Encryption.

## Resources[#](#resources)

*   [Supabase Vault](/docs/guides/database/vault)
*   Read more about Supabase Vault in the [blog post](/blog/vault-now-in-beta)
*   [Supabase Vault on GitHub](https://github.com/supabase/vault)

## Resources[#](#resources)

*   Official [`pgsodium` documentation](https://github.com/michelp/pgsodium)


