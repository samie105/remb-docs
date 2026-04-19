# SKILL.md — Supabase Documentation Navigation & Key Concepts

## Overview

Supabase is an open-source backend-as-a-service platform built on PostgreSQL, providing developers with instant APIs, authentication, real-time subscriptions, storage, serverless functions, and built-in support for AI vector search. The documentation is structured by feature area and guides developers from getting started to advanced integrations, examples, and operational considerations.

---

## Key Concepts

- **PostgreSQL Foundation**: Supabase projects are standardized PostgreSQL databases, extended with tools for modern app development.
- **Authentication**: Supports email/password, OAuth, social logins, and custom token hooks for flexible auth flows.
- **Realtime & Subscriptions**: Enables listening to database changes for live, interactive app experiences.
- **Edge Functions**: Serverless function support for custom backend logic, including integrations with external APIs.
- **Storage**: File/object storage with access control and seamless integration into app workflows.
- **AI & Vector Search**: Embedding storage and search, generative Q&A, multimodal examples, and compute add-ons for AI use cases.
- **Observability**: Built-in logging, metrics, and support for monitoring (e.g., Sentry).
- **Migration & Platform**: Guides for migrating from other Postgres platforms and working with cloud marketplaces.

---

## Navigation Guide

- **Getting Started & Quickstarts**: For setup across frameworks and platforms ([supabase/docs/guides/getting-started/index.md]).
- **Feature Guides**: Each main area—Auth, Database, Edge Functions, Storage, AI & Vectors—has a section with core concepts and practical guides.
- **Examples**: Code samples per language/framework for rapid ramp-up; AI, Edge Functions, Auth, and Database examples are in respective sections.
- **Platform & Migration**: For deployment, marketplace integration, and migration support.
- **Resources**: Central entry point for examples and glossary ([supabase/docs/guides/resources/index.md]).
- **Telemetry**: Logging, metrics, reports, and monitoring ([supabase/docs/guides/telemetry/logs/index.md], etc.).

**Common Task Finding**
- Want an overview/concepts? Look for "Concepts" pages inside each feature guide (e.g., [supabase/docs/guides/ai/concepts/index.md]).
- Need auth flows or OAuth? Start in Auth guides.
- Looking for cloud functions or integrations? See Edge Functions.
- Searching for AI/vector functionality or examples? Use AI & Vectors guides and examples.
- Want to check observability or logging? See Telemetry guides.

---

## Top Pages & Local Links

1. [supabase/docs/index.md] — Main documentation entry point.
2. [supabase/docs/guides/getting-started/index.md] — General getting started guide.
3. [supabase/docs/guides/getting-started/quickstarts/kotlin/index.md] — Example quickstart: Android/Kotlin integration.
4. [supabase/docs/guides/ai/concepts/index.md] — Concepts for AI and vector search functionalities.
5. [supabase/docs/guides/ai/automatic-embeddings/index.md] — Guide to automatic embeddings (core for vector search).
6. [supabase/docs/guides/ai/choosing-compute-addon/index.md] — How to select the right compute add-on for AI workloads.
7. [supabase/docs/guides/ai/engineering-for-scale/index.md] — Best practices for scaling AI/vector workloads.
8. [supabase/docs/guides/ai/examples/building-chatgpt-plugins/index.md] — Example: Building ChatGPT plugins (Python).
9. [supabase/docs/guides/ai/examples/headless-vector-search/index.md] — Example: Adding generative Q&A to docs (JavaScript).
10. [supabase/docs/guides/ai/examples/huggingface-image-captioning/index.md] — Example: Image captioning via Hugging Face (JavaScript).
11. [supabase/docs/guides/ai/examples/image-search-openai-clip/index.md] — Example: Image search using OpenAI CLIP (Python).
12. [supabase/docs/guides/ai/examples/mixpeek-video-search/index.md] — Example: Video search with multimodal embeddings.
13. [supabase/docs/guides/ai/examples/nextjs-vector-search/index.md] — Example: Generative Q&A on Next.js sites.
14. [supabase/docs/guides/ai/examples/openai/index.md] — Example: Edge Functions generating OpenAI completions.
15. [supabase/docs/guides/auth/auth-hooks/custom-access-token-hook/index.md] — Custom access token hook for authentication.
16. [supabase/docs/guides/auth/social-login/auth-azure/index.md] — Social login setup: Azure/Microsoft.
17. [supabase/docs/guides/database/extensions/pg_partman/index.md] — Overview of PostgreSQL extensions.
18. [supabase/docs/guides/database/prisma/index.md] — Connecting with Prisma ORM.
19. [supabase/docs/guides/functions/examples/discord-bot/index.md] — Building a Discord bot using Edge Functions.
20. [supabase/docs/guides/platform/migrating-to-supabase/postgres/index.md] — Migration from Postgres to Supabase.
21. [supabase/docs/guides/resources/index.md] — Resources page (examples, glossary, etc.).
22. [supabase/docs/guides/telemetry/logs/index.md] — Logging and observability overview.
23. [supabase/docs/guides/telemetry/metrics/index.md] — Metrics API guide.
24. [supabase/docs/guides/telemetry/reports/index.md] — Observability: Reports.
25. [supabase/docs/guides/platform/aws-marketplace/getting-started/index.md] — Getting started with Supabase via AWS Marketplace.

---

## Notable Gotchas & Structural Quirks

- **Feature Naming**: Major features sometimes appear under multiple headings (e.g., "Auth" in "More > Auth Hooks" and "Social Login"). Some advanced options may be deep in nested "More" menus.
- **Examples**: Language/framework/examples are scattered under their respective feature guides rather than in a single central "Examples" folder. Use "Resources" for aggregates.
- **AI, Vectors**: Many AI and vector search guides and examples live under "AI & Vectors", split between "Concepts", "Learn", and multiple "Examples" (Python, JS, third-party).
- **Observability**: "Telemetry" covers logs, metrics, reports, and third-party monitoring (like Sentry); don't miss "Logging & observability" for operational features.
- **Platform/Migration**: Migration guides may appear under "More > Migrating to Supabase" in "Platform".

---

Use this SKILL.md to rapidly map Supabase docs and answer developer questions by locating the right guides, concept pages, or practical examples via their local repo paths.