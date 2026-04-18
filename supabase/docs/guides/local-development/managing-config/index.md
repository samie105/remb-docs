---
title: "Managing config and secrets"
source: "https://supabase.com/docs/guides/local-development/managing-config"
canonical_url: "https://supabase.com/docs/guides/local-development/managing-config"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:41.406Z"
content_hash: "4cfb3324f44cb0546a62907d62ed0bc9017a64e46f0fc041b072947a4b3795bf"
menu_path: ["Local Dev / CLI","Local Dev / CLI","Local development","Local development","Managing config and secrets","Managing config and secrets"]
section_path: ["Local Dev / CLI","Local Dev / CLI","Local development","Local development","Managing config and secrets","Managing config and secrets"]
---
# 

Managing config and secrets

* * *

The Supabase CLI uses a `config.toml` file to manage local configuration. This file is located in the `supabase` directory of your project.

## Config reference[#](#config-reference)

The `config.toml` file is automatically created when you run `supabase init`.

There are a wide variety of options available, which can be found in the [CLI Config Reference](/docs/guides/cli/config).

For example, to enable the "Apple" OAuth provider for local development, you can append the following information to `config.toml`:

```
1[auth.external.apple]2enabled = false3client_id = ""4secret = ""5redirect_uri = "" # Overrides the default auth redirectUrl.
```

## Using secrets inside config.toml[#](#using-secrets-inside-configtoml)

You can reference environment variables within the `config.toml` file using the `env()` function. This will detect any values stored in an `.env` file at the root of your project directory. This is particularly useful for storing sensitive information like API keys, and any other values that you don't want to check into version control.

```
1.2├── .env3├── .env.example4└── supabase5    └── config.toml
```

Do NOT commit your `.env` into git. Be sure to configure your `.gitignore` to exclude this file.

For example, if your `.env` contained the following values:

```
1GITHUB_CLIENT_ID=""2GITHUB_SECRET=""
```

Then you would reference them inside of our `config.toml` like this:

```
1[auth.external.github]2enabled = true3client_id = "env(GITHUB_CLIENT_ID)"4secret = "env(GITHUB_SECRET)"5redirect_uri = "" # Overrides the default auth redirectUrl.
```

### Going further[#](#going-further)

For more advanced secrets management workflows, including:

*   **Using dotenvx for encrypted secrets**: Learn how to securely manage environment variables across different branches and environments
*   **Branch-specific secrets**: Understand how to manage secrets for different deployment environments
*   **Encrypted configuration values**: Use encrypted values directly in your `config.toml`

See the [Managing secrets for branches](/docs/guides/deployment/branching#managing-secrets-for-branches) section in our branching documentation, or check out the [dotenvx example repository](https://github.com/supabase/supabase/blob/master/examples/slack-clone/nextjs-slack-clone-dotenvx/README.md) for a complete implementation.
