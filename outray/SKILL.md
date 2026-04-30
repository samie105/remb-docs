## Overview

Outray is a tunneling platform that exposes local services to the internet via public URLs, supporting HTTP, TCP, and UDP traffic, custom domains, and framework-specific plugins. Agents need to know it to spin up secure tunnels, embed tunneling into Node.js applications, and manage production deployments from local or CI/CD environments.

## Mental Model

Outray bridges local or private services to the public internet through a hosted edge network, combining a CLI for manual control, framework plugins for zero-config integration, and production features like authentication and observability. The system treats tunneling as infrastructure—configure once via `outray/docs/cli-reference/index.md`, expose services through `outray/docs/opening-a-tunnel/index.md`, and scale using patterns described in `outray/docs/architecture/index.md`.

## Learning Paths

- **Getting Started** — `outray/docs/index.md` → `outray/docs/installation/index.md` → `outray/docs/opening-a-tunnel/index.md`
- **Production Ready** — `outray/docs/architecture/index.md` → `outray/docs/authentication/index.md` → `outray/docs/password-protection/index.md` → `outray/docs/custom-domains/index.md` → `outray/docs/reserved-subdomains/index.md` → `outray/docs/observability/index.md` → `outray/docs/ci-cd/index.md`
- **Reference Deep-Dive** — `outray/docs/cli-reference/index.md` → `outray/docs/protocols/index.md` → `outray/docs/express-plugin/index.md` → `outray/docs/nestjs-plugin/index.md` → `outray/docs/nextjs-plugin/index.md`

## Concept Map

- **Core Platform**
  - Architecture → `outray/docs/architecture/index.md`
  - Introduction → `outray/docs/index.md`
  - Installation → `outray/docs/installation/index.md`
- **Tunneling**
  - Opening a Tunnel → `outray/docs/opening-a-tunnel/index.md`
  - TCP & UDP Tunnels → `outray/docs/protocols/index.md`
- **Security & Access**
  - Authentication → `outray/docs/authentication/index.md`
  - Password Protection → `outray/docs/password-protection/index.md`
  - Custom Domains → `outray/docs/custom-domains/index.md`
  - Reserved Subdomains → `outray/docs/reserved-subdomains/index.md`
- **Framework Plugins**
  - Options
    - Express Plugin → `outray/docs/express-plugin/index.md`
    - NestJS Plugin → `outray/docs/nestjs-plugin/index.md`
    - Next.js Plugin → `outray/docs/nextjs-plugin/index.md`
  - Custom Subdomain
    - Express Plugin → `outray/docs/express-plugin/index.md`
    - NestJS Plugin → `outray/docs/nestjs-plugin/index.md`
    - Next.js Plugin → `outray/docs/nextjs-plugin/index.md`
  - Custom Domain
    - Express Plugin → `outray/docs/express-plugin/index.md`
    - NestJS Plugin → `outray/docs/nestjs-plugin/index.md`
    - Next.js Plugin → `outray/docs/nextjs-plugin/index.md`
  - Conditional Enabling
    - Express Plugin → `outray/docs/express-plugin/index.md`
    - NestJS Plugin → `outray/docs/nestjs-plugin/index.md`
    - Next.js Plugin → `outray/docs/nextjs-plugin/index.md`
- **Operations**
  - CLI Reference → `outray/docs/cli-reference/index.md`
  - Observability → `outray/docs/observability/index.md`
  - CI/CD Integration → `outray/docs/ci-cd/index.md`

## If You Need To...

| If you need to... | Read |
|---|---|
| Install the CLI | `outray/docs/installation/index.md` |
| Open a tunnel | `outray/docs/opening-a-tunnel/index.md` |
| Understand system design | `outray/docs/architecture/index.md` |
| Add login requirements | `outray/docs/authentication/index.md` |
| Use your own domain | `outray/docs/custom-domains/index.md` |
| Reserve a fixed subdomain | `outray/docs/reserved-subdomains/index.md` |
| Integrate with a framework | `outray/docs/express-plugin/index.md`, `outray/docs/nestjs-plugin/index.md`, `outray/docs/nextjs-plugin/index.md` |
| Validate configuration | `outray/docs/cli-reference/index.md` |
| Monitor or debug | `outray/docs/observability/index.md` |
| Automate in CI/CD | `outray/docs/ci-cd/index.md` |

## Top Must-Know Pages

1. `outray/docs/index.md` — Introduction to outray concepts and value proposition.
2. `outray/docs/installation/index.md` — How to install the outray CLI and required dependencies.
3. `outray/docs/opening-a-tunnel/index.md` — Step-by-step guide to start and manage your first tunnel.
4. `outray/docs/architecture/index.md` — Explains how outray routes public traffic to local services.
5. `outray/docs/authentication/index.md` — Identity and access control for securing tunnel endpoints.
6. `outray/docs/custom-domains/index.md` — Configure branded domains instead of auto-generated URLs.
7. `outray/docs/cli-reference/index.md` — Complete command reference including config validation and flags.
8. `outray/docs/protocols/index.md` — Using TCP and UDP tunnels for non-HTTP traffic.
9. `outray/docs/express-plugin/index.md` — Zero-config Express integration with options, subdomains, and conditional enabling.
10. `outray/docs/ci-cd/index.md` — Patterns for automating outray in continuous deployment pipelines.