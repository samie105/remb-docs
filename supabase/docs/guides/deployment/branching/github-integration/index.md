---
title: "GitHub integration"
source: "https://supabase.com/docs/guides/deployment/branching/github-integration"
canonical_url: "https://supabase.com/docs/guides/deployment/branching/github-integration"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:10.424Z"
content_hash: "42d40640f2228f8aaea2dcd330ce7923e6dc2c2d60c77cf9aa78b746c9fd00f4"
menu_path: ["Deployment & Branching","Deployment & Branching","Branching","Branching","Branching via GitHub","Branching via GitHub"]
section_path: ["Deployment & Branching","Deployment & Branching","Branching","Branching","Branching via GitHub","Branching via GitHub"]
nav_prev: {"path": "supabase/docs/guides/deployment/branching/integrations/index.md", "title": "Integrations"}
nav_next: {"path": "supabase/docs/guides/deployment/branching/troubleshooting/index.md", "title": "Troubleshooting"}
---

# 

GitHub integration

## 

Connect with GitHub to sync branches with your repository

* * *

Supabase Branching uses the Supabase GitHub integration to read files from your GitHub repository. With this integration, Supabase watches all commits, branches, and pull requests of your GitHub repository.

## Installation[#](#installation)

In the Supabase Dashboard:

1.  Go to **Project Settings** > [**Integrations**](/dashboard/project/_/settings/integrations).
2.  Under **GitHub Integration**, click **Authorize GitHub**.
3.  You are redirected to a GitHub authorization page. Click **Authorize Supabase**.
4.  You are redirected back to the Integrations page. Choose a GitHub repository to connect your project to.
5.  Fill in the relative path to the Supabase directory from your repository root.
6.  Configure the other options as needed to automate your GitHub connection.
7.  Click **Enable integration**.

## Preparing your Git repository[#](#preparing-your-git-repository)

You will be using the [Supabase CLI](/docs/guides/cli) to initialise your local `./supabase` directory:

1

### Initialize Supabase locally

If you don't have a `./supabase` directory, you can create one:

```
1supabase init
```

2

### Pull your database migration

Pull your database changes using `supabase db pull`. To get your database connection string, go to your project dashboard, click [Connect](/dashboard/project/_?showConnect=true&method=session) and look for the Session pooler connection string.

```
1supabase db pull --db-url <db_connection_string>23# Your Database connection string will look like this:4# postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:5432/postgres
```

If you're in an [IPv6 environment](https://github.com/orgs/supabase/discussions/27034) or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.

3

### Commit the \`supabase\` directory to Git

Commit the `supabase` directory to Git, and push your changes to your remote repository.

```
1git add supabase2git commit -m "Initial migration"3git push
```

## Syncing GitHub branches[#](#syncing-github-branches)

Enable the **Automatic branching** option in your GitHub Integration configuration to automatically sync GitHub branches with Supabase branches.

When a new branch is created in GitHub, a corresponding branch is created in Supabase. (You can enable the **Supabase changes only** option to only create Supabase branches when Supabase files change.)

### Configuration[#](#configuration)

You can test configuration changes on your Preview Branch by configuring the `config.toml` file in your Supabase directory. See the [Configuration docs](/docs/guides/deployment/branching/configuration) for more information.

A comment is added to your PR with the deployment status of your preview branch.

### Migrations[#](#migrations)

The migrations in the `migrations` subdirectory of your Supabase directory are automatically run.

### Seeding[#](#seeding)

No production data is copied to your Preview branch. This is meant to protect your sensitive production data.

You can seed your Preview Branch with sample data using the `seed.sql` file in your Supabase directory. See the [Seeding docs](/docs/guides/local-development/seeding-your-database) for more information.

Data changes in your seed files are not merged to production.

## Deploying changes to production[#](#deploying-changes-to-production)

Enable the **Deploy to production** option in your GitHub Integration configuration to automatically deploy changes when you push or merge to production branch.

The following changes are deployed:

*   New migrations are applied
*   Edge Functions declared in `config.toml` are deployed
*   Storage buckets declared in `config.toml` are deployed

All other configurations, including API, Auth, and seed files, are ignored by default.

## Preventing migration failures[#](#preventing-migration-failures)

We highly recommend turning on a 'required check' for the Supabase integration. You can do this from your GitHub repository settings. This prevents PRs from being merged when migration checks fail, and stops invalid migrations from being merged into your production branch.

![Check the "Require status checks to pass before merging" option.](/docs/img/guides/platform/branching/github-required-check.jpg?v=1)

Check the "Require status checks to pass before merging" option.

### Email notifications[#](#email-notifications)

To catch failures early, we also recommend subscribing to email notifications on your branch. Common errors include migration conflict, function deployment failure, or invalid configuration file.

You can setup a custom GitHub Action to monitor the status of any Supabase Branch.

###### .github/workflows/notify-failure.yaml

```
1name: Branch Status23on:4  pull_request:5    types:6      - opened7      - reopened8      - synchronize9    branches:10      - main11      - develop12    paths:13      - 'supabase/**'1415jobs:16  failed:17    runs-on: ubuntu-latest18    steps:19      - uses: fountainhead/action-wait-for-check@v1.2.020        id: check21        with:22          checkName: Supabase Preview23          ref: ${{ github.event.pull_request.head.sha || github.sha }}24          token: ${{ secrets.GITHUB_TOKEN }}2526      - if: ${{ steps.check.outputs.conclusion == 'failure' }}27        run: exit 1
```
