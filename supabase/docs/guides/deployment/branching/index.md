---
title: "Branching"
source: "https://supabase.com/docs/guides/deployment/branching"
canonical_url: "https://supabase.com/docs/guides/deployment/branching"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:47.376Z"
content_hash: "aa282f85b7715d02b4dc05690851ad63f101b1a0bf0a8d66b6f01448538e8707"
menu_path: ["Deployment & Branching","Deployment & Branching","Branching","Branching","Overview","Overview"]
section_path: ["Deployment & Branching","Deployment & Branching","Branching","Branching","Overview","Overview"]
nav_prev: {"path": "supabase/docs/guides/deployment/index.md", "title": "Deployment & Branching"}
nav_next: {"path": "supabase/docs/guides/deployment/branching/configuration/index.md", "title": "Configuration"}
---

# 

Branching

## 

Use Supabase Branches to test and preview changes

* * *

Use branching to safely experiment with changes to your Supabase project.

Supabase branches create separate environments that spin off from your main project. You can use these branching environments to create and test changes like new configurations, database schemas, or features without affecting your production setup. When you're ready to ship your changes, merge your branch to update your production instance with the new changes.

## How branching works[#](#how-branching-works)

*   **Separate Environments**: Each branch is a separate environment with its own Supabase instance and API credentials.
*   **Preview Branches**: Preview branches are ephemeral and best suited for focused testing. They are automatically paused after inactivity or deleted when a PR is merged or closed.
*   **Persistent Branches**: Persistent branches are long-lived and recommended for environments like staging, QA, or development. Unlike preview branches, they aren't automatically paused or deleted due to inactivity or when a PR is merged or closed.
*   **Managing Branches**: You can create, review, and merge branches either automatically via our [GitHub integration](github-integration/index.md) or directly [through the dashboard](dashboard/index.md) (currently in beta). All branches show up in the branches page in the dashboard, regardless of how they were created.
*   **Data-less**: New branches do not start with any data from your main project. This is meant to better protect your sensitive production data. To start your branches with data, you can use a [seed file](github-integration/index.md#seeding) if using the GitHub integration.

## Deploying to production[#](#deploying-to-production)

When you merge any branch into your main project, Supabase automatically runs a deployment workflow to deploy your changes to production. The deployment workflow is expressed as a Directed Acyclic Graph where each node represents one of the following deployment steps.

1.  **Clone** - Checks out your repository at the specified git branch (optional for [Branching via Dashboard](dashboard/index.md))
2.  **Pull** - Retrieves database migrations from your main project (also initialises the migration history table when Branching via Dashboard)
3.  **Health** - Waits up to 2 minutes for all Supabase services on your branch to be running and healthy, including Auth, API, Database, Storage, and Realtime
4.  **Configure** - Updates service configurations based on your config.toml file (only available for [Branching via GitHub](github-integration/index.md))
5.  **Migrate** - Applies pending database migrations and vault secrets to your branch
6.  **Seed** - Runs seed files to populate your branch with initial data (must be [enabled in config.toml](configuration/index.md#branch-configuration-with-remotes) for persistent branches)
7.  **Deploy** - Deploys any changed Edge Functions and updates function secrets

If a parent deployment step fails, all dependent child steps will be skipped. For instance, if your database migrations failed at step 5, our runner will not seed your branch because step 6 is skipped. If you are using GitHub integration, the same deployment workflow will be run on every commit pushed to your git branch.
