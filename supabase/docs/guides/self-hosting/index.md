---
title: "Self-Hosting"
source: "https://supabase.com/docs/guides/self-hosting"
canonical_url: "https://supabase.com/docs/guides/self-hosting"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:44.831Z"
content_hash: "f7bd129ce45e179bc266aa7fbac0615c4e6bc715ef8aee3d63aac8478ca57e8b"
menu_path: ["Self-Hosting","Self-Hosting","Overview","Overview"]
section_path: ["Self-Hosting","Self-Hosting","Overview","Overview"]
nav_prev: {"path": "supabase/docs/guides/security/soc-2-compliance/index.md", "title": "SOC 2 Compliance and Supabase"}
nav_next: {"path": "supabase/docs/guides/self-hosting/copy-from-platform-s3/index.md", "title": "Copy Storage Objects from Platform"}
---

# 

Self-Hosting

## 

Install and run your own Supabase on your computer, server, or cloud infrastructure.

* * *

## Get started[#](#get-started)

The fastest and recommended way to self-host Supabase is using Docker.

[

![\[object Object\]](/docs/img/icons/docker-light.svg)

Docker

Official

Deploy Supabase within your own infrastructure using Docker Compose.

](/docs/guides/self-hosting/docker)

## Community-driven projects[#](#community-driven-projects)

There are several other options to deploy Supabase. If you're interested in helping these projects, visit our [Community](/contribute) page.

[

Kubernetes

Helm charts to deploy a Supabase on Kubernetes.

](https://github.com/supabase-community/supabase-kubernetes)

[

Traefik

A self-hosted Supabase setup with Traefik as a reverse proxy.

](https://github.com/supabase-community/supabase-traefik)

## About self-hosting[#](#about-self-hosting)

Self-hosting is a good fit if you need full control over your data, have compliance requirements that prevent using managed services, or want to run Supabase in an isolated environment.

### How self-hosted Supabase differs[#](#how-self-hosted-supabase-differs)

Self-hosted Supabase is different from:

*   **Supabase CLI** (local development), which is intended for development and testing only.
*   **Managed Supabase** platform, which is fully hosted and operated by Supabase.

### Telemetry[#](#telemetry)

Self-hosted Supabase (Docker) does not phone home or collect any telemetry.

The **Supabase CLI** is a [separate tool](../local-development/cli/getting-started/index.md) from self-hosted Supabase and collects usage telemetry to help improve the developer experience. You can opt out by running `supabase telemetry disable` or setting `SUPABASE_TELEMETRY_DISABLED=1`. See [CLI telemetry](../local-development/cli/getting-started/index.md#telemetry) for other opt-out methods.

### Your responsibilities when self-hosting[#](#your-responsibilities-when-self-hosting)

When you self-host, **you are responsible for**:

*   Server provisioning and maintenance
*   Security hardening and keeping OS and services updated
*   Maintaining the Postgres database
*   Backups and disaster recovery
*   Monitoring and uptime

## Support and community[#](#support-and-community)

Self-hosted Supabase is community-supported.

For resolving common issues:

*   [GitHub Discussions](https://github.com/orgs/supabase/discussions?discussions_q=is%3Aopen+label%3Aself-hosted) - Questions, feature requests, and workarounds
*   [GitHub Issues](https://github.com/supabase/supabase/issues?q=is%3Aissue%20state%3Aopen%20label%3Aself-hosted) - Known issues

Get help and connect with other users:

*   [Discord](https://discord.supabase.com) - Real-time chat and community support
*   [Reddit](https://www.reddit.com/r/Supabase/) - Official Supabase subreddit

Share your self-hosting experience:

*   [GitHub Discussions](https://github.com/orgs/supabase/discussions/39820) - "Self-hosting: What's working (and what's not)?"

### Enterprise self-hosting[#](#enterprise-self-hosting)

If you're an enterprise using self-hosted Supabase, we'd love to hear from you. Reach out to our [Growth Team](https://forms.supabase.com/enterprise) to discuss your use case, share feedback, or explore design partnership opportunities.
