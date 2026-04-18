---
title: "Configuration"
source: "https://supabase.com/docs/guides/deployment/branching/configuration"
canonical_url: "https://supabase.com/docs/guides/deployment/branching/configuration"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:03.779Z"
content_hash: "1760b8cb547225a5bd83b58085704707b8d12cdadc150befa2a76837381c1ab2"
menu_path: ["Deployment & Branching","Deployment & Branching","Branching","Branching","Configuration","Configuration"]
section_path: ["Deployment & Branching","Deployment & Branching","Branching","Branching","Configuration","Configuration"]
nav_prev: {"path": "supabase/docs/guides/database/replication/replication-monitoring/index.md", "title": "Replication Monitoring"}
nav_next: {"path": "supabase/docs/guides/database/replication/replication-setup/index.md", "title": "Replication Setup"}
---

# 

Configuration

## 

Configure your Supabase branches using configuration as code

* * *

This guide covers how to configure your Supabase branches, using the `config.toml` file. In one single file, you can configure all your branches, including branch settings and secrets.

## Branch configuration with remotes[#](#branch-configuration-with-remotes)

When Branching is enabled, your `config.toml` settings automatically sync to all ephemeral branches through a one-to-one mapping between your Git and Supabase branches.

### Basic configuration[#](#basic-configuration)

To update configuration for a Supabase branch, modify `config.toml` and push to git. The Supabase integration will detect the changes and apply them to the corresponding branch.

### Remote-specific configuration[#](#remote-specific-configuration)

For persistent branches that need specific settings, you can use the `[remotes]` block in your `config.toml`. Each remote configuration must reference an existing project ID.

Here's an example of configuring a separate seed script for a staging environment:

```
1[remotes.staging]2project_id = "your-project-ref"34[remotes.staging.db.seed]5enabled = true6sql_paths = ["./seeds/staging.sql"]
```

Since the `project_id` field must reference an existing branch, you need to create the persistent branch before adding its configuration. Use the CLI to create a persistent branch first:

```
1supabase --experimental branches create --persistent2# Do you want to create a branch named develop? [Y/n]
```

To retrieve the project ID for an existing branch, use the `branches list` command:

```
1supabase --experimental branches list
```

This will display a table showing all your branches with their corresponding project ID. Use the value from the `BRANCH PROJECT ID` column as your `project_id` in the remote configuration.

### Configuration merging[#](#configuration-merging)

When merging a PR into a persistent branch, the Supabase integration:

1.  Checks for configuration changes
2.  Logs the changes
3.  Applies them to the target remote

If no remote is declared or the project ID is incorrect, the configuration step is skipped.

### Available configuration options[#](#available-configuration-options)

All standard configuration options are available in the `[remotes]` block. This includes:

*   Database settings
*   API configurations
*   Authentication settings
*   Edge Functions configuration
*   And more

You can use this to maintain different configurations for different environments while keeping them all in version control.

## Managing secrets for branches[#](#managing-secrets-for-branches)

For sensitive configuration like SMTP credentials or API keys, you can use the Supabase CLI to manage secrets for your branches. This is especially useful for custom SMTP setup or other services that require secure credentials.

To set secrets for a persistent branch:

```
1# Set secrets from a .env file2supabase secrets set --env-file ./supabase/.env34# Or set individual secrets5supabase secrets set SMTP_HOST=smtp.example.com6supabase secrets set SMTP_USER=your-username7supabase secrets set SMTP_PASSWORD=your-password
```

These secrets will be available to your branch's services and can be used in your configuration. For example, in your `config.toml`:

```
1[auth.smtp]2host = "env(SMTP_HOST)"3user = "env(SMTP_USER)"4password = "env(SMTP_PASSWORD)"
```

##### Secrets are branch-specific

Secrets set for one branch are not automatically available in other branches. You'll need to set them separately for each branch that needs them.

### Using dotenvx for git-based workflow[#](#using-dotenvx-for-git-based-workflow)

For managing environment variables across different branches, you can use [dotenvx](https://dotenvx.com/) to securely manage your configurations. This approach is particularly useful for teams working with Git branches and preview deployments.

#### Environment file structure[#](#environment-file-structure)

Following the conventions used in the [example repository](https://github.com/supabase/supabase/blob/master/examples/slack-clone/nextjs-slack-clone-dotenvx/README.md), environments are configured using dotenv files in the `supabase` directory:

File

Environment

`.gitignore` it?

Encrypted

.env.keys

All

Yes

No

.env.local

Local

Yes

No

.env.production

Production

No

Yes

.env.preview

Branches

No

Yes

.env

Any

Maybe

Yes

#### Setting up encrypted secrets[#](#setting-up-encrypted-secrets)

1.  Generate key pair and encrypt your secrets:

```
1npx @dotenvx/dotenvx set SUPABASE_AUTH_EXTERNAL_GITHUB_SECRET "<your-secret>" -f supabase/.env.preview
```

This creates a new encryption key in `supabase/.env.preview` and a new decryption key in `supabase/.env.keys`.

2.  Update project secrets:

```
1npx supabase secrets set --env-file supabase/.env.keys
```

3.  Choose your configuration approach in `config.toml`:

Option A: Use encrypted values directly:

```
1[auth.external.github]2enabled = true3secret = "encrypted:<encrypted-value>"
```

Option B: Use environment variables:

```
1[auth.external.github]2enabled = true3client_id = "env(SUPABASE_AUTH_EXTERNAL_GITHUB_CLIENT_ID)"4secret = "env(SUPABASE_AUTH_EXTERNAL_GITHUB_SECRET)"
```

##### Secret fields

The `encrypted:` syntax only works for designated "secret" fields in the configuration. Using encrypted values in other fields will not be automatically decrypted and may cause issues. For non-secret fields, use environment variables with the `env()` syntax instead.

The following fields support the `encrypted:` syntax:

**Studio**

*   `studio.openai_api_key`

**Database**

*   `db.root_key`
*   `db.vault.*` (any key in the vault map)

**Auth - Core Keys**

*   `auth.publishable_key`
*   `auth.secret_key`
*   `auth.jwt_secret`
*   `auth.anon_key`
*   `auth.service_role_key`

**Auth - Email (SMTP)**

*   `auth.email.smtp.pass`

**Auth - Captcha**

*   `auth.captcha.secret`

**Auth - Hooks**

*   `auth.hook.mfa_verification_attempt.secrets`
*   `auth.hook.password_verification_attempt.secrets`
*   `auth.hook.custom_access_token.secrets`
*   `auth.hook.send_sms.secrets`
*   `auth.hook.send_email.secrets`
*   `auth.hook.before_user_created.secrets`

**Auth - SMS Providers**

*   `auth.sms.twilio.auth_token`
*   `auth.sms.twilio_verify.auth_token`
*   `auth.sms.messagebird.access_key`
*   `auth.sms.textlocal.api_key`
*   `auth.sms.vonage.api_secret`

**Auth - External OAuth Providers**

*   `auth.external.*.secret`

**Edge Runtime**

*   `edge_runtime.secrets.*` (any key in the secrets map)

#### Using with preview branches[#](#using-with-preview-branches)

When you commit your `.env.preview` file with encrypted values, the branching executor will automatically retrieve and use these values when deploying your branch. This allows you to maintain different configurations for different branches while keeping sensitive information secure.

## Configuration examples[#](#configuration-examples)

### Multi-environment setup[#](#multi-environment-setup)

Here's an example of a complete multi-environment configuration:

```
1# Default configuration for all branches2[api]3enabled = true4port = 543215schemas = ["public", "storage", "graphql_public"]67[db]8port = 543229pool_size = 101011# Staging-specific configuration12[remotes.staging]13project_id = "staging-project-ref"1415[remotes.staging.api]16max_rows = 10001718[remotes.staging.db.seed]19sql_paths = ["./seeds/staging.sql"]2021# Production-specific configuration22[remotes.production]23project_id = "prod-project-ref"2425[remotes.production.api]26max_rows = 5002728[remotes.production.db]29pool_size = 25
```

To retrieve the project ID for an existing branch, use the `branches list` command:

```
1supabase --experimental branches list
```

This will display a table showing all your branches with their corresponding project ID. Use the value from the `BRANCH PROJECT ID` column as your `project_id` in the remote configuration.

### Feature branch configuration[#](#feature-branch-configuration)

For feature branches that need specific settings:

```
1[remotes.feature-oauth]2project_id = "feature-branch-ref"34[remotes.feature-oauth.auth.external.google]5enabled = true6client_id = "env(GOOGLE_CLIENT_ID)"7secret = "env(GOOGLE_CLIENT_SECRET)"
```

To retrieve the project ID for an existing branch, use the `branches list` command:

```
1supabase --experimental branches list
```

This will display a table showing all your branches with their corresponding project ID. Use the value from the `BRANCH PROJECT ID` column as your `project_id` in the remote configuration.

## Next steps[#](#next-steps)

*   Explore [branching integrations](/docs/guides/deployment/branching/integrations)
*   Learn about [troubleshooting branches](/docs/guides/deployment/branching/troubleshooting)
*   Review [branching pricing](/docs/guides/platform/manage-your-usage/branching#pricing)
