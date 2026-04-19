---
title: "Deployment & Branching"
source: "https://supabase.com/docs/guides/deployment"
canonical_url: "https://supabase.com/docs/guides/deployment"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:06.824Z"
content_hash: "d8bd30c40928b47a4216aae6a3c6d51c44986c09c2b8284334af5fd73735f612"
menu_path: ["Deployment & Branching","Deployment & Branching","Overview","Overview"]
section_path: ["Deployment & Branching","Deployment & Branching","Overview","Overview"]
nav_prev: {"path": "supabase/docs/guides/database/webhooks/index.md", "title": "Database Webhooks"}
nav_next: {"path": "supabase/docs/guides/deployment/branching/index.md", "title": "Branching"}
---

# 

Deployment & Branching

* * *

Deploying your app makes it live and accessible to users. Usually, you deploy an app to at least two environments: a production environment for users and (one or multiple) staging or preview environments for developers.

Supabase provides several options for environment management and deployment.

## Environment management[#](#environment-management)

You can maintain separate development, staging, and production environments for Supabase:

*   **Development**: Develop with a local Supabase stack using the [Supabase CLI](/docs/guides/local-development).
*   **Staging**: Use [branching](/docs/guides/deployment/branching) to create staging or preview environments. You can use persistent branches for a long-lived staging setup, or ephemeral branches for short-lived previews (which are often tied to a pull request).
*   **Production**: If you have branching enabled, you can use the Supabase GitHub integration to automatically push your migration files when you merge a pull request. Alternatively, you can set up your own continuous deployment pipeline using the Supabase CLI.

##### Self-hosting

Read the [self-hosting guides](/docs/guides/self-hosting) for instructions on hosting your own Supabase stack.

## Deployment[#](#deployment)

You can automate deployments using:

*   The [Supabase GitHub integration](/dashboard/project/_/settings/integrations) (with branching enabled)
*   The [Supabase CLI](/docs/guides/local-development) in your own continuous deployment pipeline
*   The [Supabase Terraform provider](/docs/guides/deployment/terraform)
