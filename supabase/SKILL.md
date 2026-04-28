## 1. Overview

Supabase is an open-source Firebase alternative built around PostgreSQL, offering integrated authentication, real-time subscriptions, storage, and edge functions. An agent needs to know it because application development on Supabase requires understanding its database-centric architecture, where extensions like `pgvector` and services like Auth and Realtime extend a unified Postgres core.

## 2. Mental Model

Treat Supabase as PostgreSQL with integrated superpowers: all persistent state—user identities, vector embeddings, and relational data—lives in the database, while Auth, Realtime, and Storage are tightly coupled services that leverage it. Edge Functions provide serverless compute for external APIs and heavy processing, and database extensions such as `pgvector`, `pgmq`, and `pg_net` enable AI, queuing, and networking without external infrastructure. Canonical pages include the AI concepts overview (`supabase/docs/guides/ai/concepts/index.md`), session architecture (`supabase/docs/guides/auth/sessions/index.md`), and connection pooling (`supabase/docs/guides/database/connection-management/index.md`).

## 3. Learning Paths

**Getting Started**
1. `supabase/docs/guides/getting-started/create-a-project/index.md`
2. `supabase/docs/guides/auth/sessions/index.md`
3. `supabase/docs/guides/database/connection-management/index.md`

**Production Ready**
1. `supabase/docs/guides/auth/auth-mfa/index.md`
2. `supabase/docs/guides/auth/auth-smtp/index.md`
3. `supabase/docs/guides/ai/engineering-for-scale/index.md`
4. `supabase/docs/guides/realtime/error_codes/index.md`

**AI & Vector Deep-Dive**
1. `supabase/docs/guides/ai/concepts/index.md`
2. `supabase/docs/guides/ai/automatic-embeddings/index.md`
3. `supabase/docs/guides/ai/examples/headless-vector-search/index.md`
4. `supabase/docs/guides/ai/choosing-compute-addon/index.md`

## 4. Concept Map

- **AI & Vector Search**
  - Core Concepts
    - `supabase/docs/guides/ai/concepts/index.md`
    - `supabase/docs/guides/ai/automatic-embeddings/index.md`
  - Scaling & Performance
    - `supabase/docs/guides/ai/choosing-compute-addon/index.md`
    - `supabase/docs/guides/ai/engineering-for-scale/index.md`
  - Examples & Integrations
    - `supabase/docs/guides/ai/examples/building-chatgpt-plugins/index.md`
    - `supabase/docs/guides/ai/examples/headless-vector-search/index.md`
    - `supabase/docs/guides/ai/examples/huggingface-image-captioning/index.md`
    - `supabase/docs/guides/ai/examples/image-search-openai-clip/index.md`
- **Authentication & Security**
  - Sessions & Flows
    - `supabase/docs/guides/auth/sessions/index.md`
  - Multi-Factor Authentication
    - `supabase/docs/guides/auth/auth-mfa/index.md`
  - Enterprise SSO
    - `supabase/docs/guides/auth/enterprise-sso/auth-sso-saml/index.md`
  - Email & Reputation
    - `supabase/docs/guides/auth/auth-smtp/index.md`
  - Debugging
    - `supabase/docs/guides/auth/debugging/error-codes/index.md`
- **Database & Realtime Operations**
  - Connection Management
    - `supabase/docs/guides/database/connection-management/index.md`
  - Operational Errors
    - `supabase/docs/guides/realtime/error_codes/index.md`
- **Project Lifecycle & Billing**
  - Setup
    - `supabase/docs/guides/getting-started/create-a-project/index.md`
    - `supabase/docs/guides/getting-started/project-setup/index.md`
  - Pricing & Usage
    - `supabase/docs/guides/platform/pricing/index.md`
    - `supabase/docs/guides/platform/what-you-are-charged-for/index.md`
    - `supabase/docs/guides/platform/how-charges-are-calculated/index.md`
    - `supabase/docs/guides/platform/usage-on-your-invoice/index.md`

## 5. If You Need To...

| If you need to... | Read this page |
|---|---|
| Create a new Supabase project | `supabase/docs/guides/getting-started/create-a-project/index.md` |
| Understand vector embeddings and similarity | `supabase/docs/guides/ai/concepts/index.md` |
| Build automatic embeddings with queues | `supabase/docs/guides/ai/automatic-embeddings/index.md` |
| Add MFA to your application | `supabase/docs/guides/auth/auth-mfa/index.md` |
| Set up enterprise SAML 2.0 sign-on | `supabase/docs/guides/auth/enterprise-sso/auth-sso-saml/index.md` |
| Configure a custom SMTP server for auth emails | `supabase/docs/guides/auth/auth-smtp/index.md` |
| Debug authentication errors and codes | `supabase/docs/guides/auth/debugging/error-codes/index.md` |
| Manage database connections and Supavisor pooling | `supabase/docs/guides/database/connection-management/index.md` |
| Diagnose realtime operational issues | `supabase/docs/guides/realtime/error_codes/index.md` |
| Scale vector workloads for production | `supabase/docs/guides/ai/engineering-for-scale/index.md` |
| Choose the right compute add-on for AI | `supabase/docs/guides/ai/choosing-compute-addon/index.md` |
| Understand billing and invoice charges | `supabase/docs/guides/platform/pricing/index.md` |

## 6. Top Must-Know Pages

1. `supabase/docs/guides/ai/concepts/index.md` — Learn what embeddings are and how vector similarity works inside Postgres.
2. `supabase/docs/guides/ai/automatic-embeddings/index.md` — Understand the architecture for generating embeddings using background workers and queues.
3. `supabase/docs/guides/ai/engineering-for-scale/index.md` — Explore patterns for enterprise-grade vector architectures and read replicas.
4. `supabase/docs/guides/auth/sessions/index.md` — Master session lifecycles, JWT claims, and the difference between PKCE and implicit flows.
5. `supabase/docs/guides/auth/auth-mfa/index.md` — Implement multi-factor authentication using TOTP or phone verification.
6. `supabase/docs/guides/auth/enterprise-sso/auth-sso-saml/index.md` — Configure SAML 2.0 single sign-on for project-level identity provider integration.
7. `supabase/docs/guides/auth/debugging/error-codes/index.md` — Resolve auth issues quickly using the error code reference and HTTP status mappings.
8. `supabase/docs/guides/database/connection-management/index.md` — Configure pool sizes, monitor Supavisor, and manage your connection resources.
9. `supabase/docs/guides/ai/examples/headless-vector-search/index.md` — Build a ChatGPT-style documentation search using the headless vector search toolkit.
10. `supabase/docs/guides/realtime/error_codes/index.md` — Interpret operational error codes to understand deployment and usage health.