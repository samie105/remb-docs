---
title: "Supabase CLI"
source: "https://supabase.com/docs/guides/local-development/cli/getting-started"
canonical_url: "https://supabase.com/docs/guides/local-development/cli/getting-started"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:28.369Z"
content_hash: "1350e84eff1c6bf5f0ec8359e08887df7b64f1f60502ff04ddc459748502b5cc"
menu_path: ["Local Dev / CLI","Local Dev / CLI","CLI","CLI","Getting started","Getting started"]
section_path: ["Local Dev / CLI","Local Dev / CLI","CLI","CLI","Getting started","Getting started"]
nav_prev: {"path": "../../index.md", "title": "Local Development & CLI"}
nav_next: {"path": "../testing-and-linting/index.md", "title": "Testing and linting"}
---

# 

Supabase CLI

## 

Develop locally, deploy to the Supabase Platform, and set up CI/CD workflows

* * *

The Supabase CLI enables you to run the entire Supabase stack locally, on your machine or in a CI environment. With just two commands, you can set up and start a new local project:

1.  `supabase init` to create a new local project
2.  `supabase start` to launch the Supabase services

## Installing the Supabase CLI[#](#installing-the-supabase-cli)

Run the CLI by prefixing each command with `npx` or `bunx`:

```
1npx supabase --help
```

The Supabase CLI requires **Node.js 20 or later** when run via `npx` or `npm`. Older Node.js versions, such as 16, are not supported and fail to start the CLI.

Installing the Supabase CLI globally using `npm install -g supabase` is **not supported**.

For global usage, install the CLI via Homebrew, Scoop, or the standalone binary.

Alternatively, you can run the CLI using `npx supabase` or install it locally as a dev dependency.

You can also install the CLI as dev dependency via [npm](https://www.npmjs.com/package/supabase):

```
1npm install supabase --save-dev
```

Global installation using `npm install -g supabase` is not supported. For global CLI usage, install via [Homebrew](/docs/guides/local-development/cli/getting-started?queryGroups=platform&platform=macos), [Scoop](/docs/guides/local-development/cli/getting-started?queryGroups=platform&platform=windows), or the [standalone binary](/docs/guides/local-development/cli/getting-started?queryGroups=platform&platform=linux).

## Updating the Supabase CLI[#](#updating-the-supabase-cli)

When a new [version](https://github.com/supabase/cli/releases) is released, you can update the CLI using the same methods.

If you have installed the CLI as dev dependency via [npm](https://www.npmjs.com/package/supabase), you can update it with:

```
1npm update supabase --save-dev
```

If you have any Supabase containers running locally, stop them and delete their data volumes before proceeding with the upgrade. This ensures that Supabase managed services can apply new migrations on a clean state of the local database.

##### Backup and stop running containers

Remember to save any local schema and data changes before stopping because the `--no-backup` flag will delete them.

```
1supabase db diff -f my_schema2supabase db dump --local --data-only > supabase/seed.sql3supabase stop --no-backup
```

## Running Supabase locally[#](#running-supabase-locally)

The Supabase CLI uses Docker containers to manage the local development stack. Follow the official guide to install and configure [Docker Desktop](https://docs.docker.com/desktop):

![Docker settings on Mac: Select Integrated, Virtualization Framework, and osxfs](/docs/img/guides/cli/docker-mac-light.png)

Alternately, you can use a different container tool that offers Docker compatible APIs.

*   [Rancher Desktop](https://rancherdesktop.io/) (macOS, Windows, Linux)
*   [Podman](https://podman.io/) (macOS, Windows, Linux)
*   [OrbStack](https://orbstack.dev/) (macOS)
*   [colima](https://github.com/abiosoft/colima) (macOS)

Inside the folder where you want to create your project, run:

```
1supabase init
```

This will create a new `supabase` folder. It's safe to commit this folder to your version control system.

Now, to start the Supabase stack, run:

```
1supabase start
```

This takes time on your first run because the CLI needs to download the Docker images to your local machine. The CLI includes the entire Supabase toolset, and a few additional images that are useful for local development (like a local SMTP server and a database diff tool).

## Access your project's services[#](#access-your-projects-services)

Once all of the Supabase services are running, you'll see output containing your local Supabase credentials. It should look like this, with urls and keys that you'll use in your local project:

```
1Started supabase local development setup.23         API URL: http://localhost:543214          DB URL: postgresql://postgres:postgres@localhost:54322/postgres5      Studio URL: http://localhost:543236     Mailpit URL: http://localhost:543247        anon key: eyJh......8service_role key: eyJh......
```

```
1# Default URL:2http://localhost:54323
```

The local development environment includes Supabase Studio, a graphical interface for working with your database.

![Local Studio](/docs/img/guides/cli/local-studio.png)

## Stopping local services[#](#stopping-local-services)

When you are finished working on your Supabase project, you can stop the stack (without resetting your local database):

```
1supabase stop
```

## Telemetry[#](#telemetry)

The Supabase CLI collects telemetry data about general usage. Participating in this program is optional, and you can opt out at any time.

### How to opt out[#](#how-to-opt-out)

You can disable telemetry by running:

```
1supabase telemetry disable
```

You can check the current status and re-enable with:

```
1supabase telemetry status2supabase telemetry enable
```

You can also opt out using the `SUPABASE_TELEMETRY_DISABLED=1` environment variable. The broader `DO_NOT_TRACK=1` convention is also respected.

## Learn more[#](#learn-more)

*   [CLI configuration](/docs/guides/local-development/cli/config)
*   [CLI reference](/docs/reference/cli)
