---
title: "Local Development & CLI"
source: "https://supabase.com/docs/guides/cli"
canonical_url: "https://supabase.com/docs/guides/local-development"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:03.210Z"
content_hash: "a75999db42d4b02f2c1c8433363768e011da9f5048dc5fe9f13e527c5c547845"
menu_path: ["Local Dev / CLI","Local Dev / CLI","Overview","Overview"]
section_path: ["Local Dev / CLI","Local Dev / CLI","Overview","Overview"]
nav_prev: {"path": "supabase/docs/guides/cron/index.md", "title": "Cron"}
nav_next: {"path": "supabase/docs/guides/deployment/index.md", "title": "Deployment & Branching"}
---

# 

Local Development & CLI

## 

Learn how to develop locally and use the Supabase CLI

* * *

Develop locally while running the Supabase stack on your machine.

As a prerequisite, you must install a container runtime compatible with Docker APIs.

*   [Docker Desktop](https://docs.docker.com/desktop/) (macOS, Windows, Linux)
*   [Rancher Desktop](https://rancherdesktop.io/) (macOS, Windows, Linux)
*   [Podman](https://podman.io/) (macOS, Windows, Linux)
*   [OrbStack](https://orbstack.dev/) (macOS)

## Quickstart[#](#quickstart)

1.  Install the Supabase CLI:
    
    ```
    1npm install supabase --save-dev
    ```
    
2.  In your repo, initialize the Supabase project:
    
    ```
    1npx supabase init
    ```
    
3.  Start the Supabase stack:
    
    ```
    1npx supabase start
    ```
    
4.  View your local Supabase instance at [http://localhost:54323](http://localhost:54323).
    

If your local development machine is connected to an untrusted public network, you should create a separate docker network and bind to 127.0.0.1 before starting the local development stack. This restricts network access to only your localhost machine.

```
1docker network create -o 'com.docker.network.bridge.host_binding_ipv4=127.0.0.1' local-network2npx supabase start --network-id local-network
```

You should never expose your local development stack publicly.

## Local development[#](#local-development)

Local development with Supabase allows you to work on your projects in a self-contained environment on your local machine. Working locally has several advantages:

1.  Faster development: You can make changes and see results instantly without waiting for remote deployments.
2.  Offline work: You can continue development even without an internet connection.
3.  Cost-effective: Local development is free and doesn't consume your project's quota.
4.  Enhanced privacy: Sensitive data remains on your local machine during development.
5.  Easy testing: You can experiment with different configurations and features without affecting your production environment.

To get started with local development, you'll need to install the [Supabase CLI](#cli) and Docker. The Supabase CLI allows you to start and manage your local Supabase stack, while Docker is used to run the necessary services.

Once set up, you can initialize a new Supabase project, start the local stack, and begin developing your application using local Supabase services. This includes access to a local Postgres database, Auth, Storage, and other Supabase features.

## CLI[#](#cli)

The Supabase CLI is a powerful tool that enables developers to manage their Supabase projects directly from the terminal. It provides a suite of commands for various tasks, including:

*   Setting up and managing local development environments
*   Generating TypeScript types for your database schema
*   Handling database migrations
*   Managing environment variables and secrets
*   Deploying your project to the Supabase platform

With the CLI, you can streamline your development workflow, automate repetitive tasks, and maintain consistency across different environments. It's an essential tool for both local development and CI/CD pipelines.

See the [CLI Getting Started guide](/docs/guides/local-development/cli/getting-started) for more information.


