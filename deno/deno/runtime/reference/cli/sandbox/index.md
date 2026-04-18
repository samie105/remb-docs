---
title: "deno sandbox"
source: "https://docs.deno.com/runtime/reference/cli/sandbox/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/sandbox/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:30.200Z"
content_hash: "be3bfbade6d4b6dbfbdb2a96f7d41cf0c7af7eb825882cdcce2c80f70830f345"
menu_path: ["deno sandbox"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/cli/run/index.md", "title": "deno run"}
nav_next: {"path": "deno/deno/runtime/reference/cli/serve/index.md", "title": "deno serve"}
---

On this page

*   [Authentication](#authentication)
*   [Global options](#global-options)
*   [Subcommands](#subcommands)
    *   [Create a new sandbox](#create-a-new-sandbox)
    *   [List your sandboxes](#list-your-sandboxes)
    *   [Kill a sandbox](#kill-a-sandbox)
    *   [Copy files](#copy-files)
    *   [Execute a command](#execute-a-command)
    *   [Extend timeout](#extend-timeout)
    *   [SSH into a sandbox](#ssh-into-a-sandbox)
    *   [Deploy a sandbox](#deploy-a-sandbox)
    *   [Manage volumes](#manage-volumes)
        *   [Create a volume](#create-a-volume)
        *   [List volumes](#list-volumes)
        *   [Delete a volume](#delete-a-volume)
        *   [Snapshot a volume](#snapshot-a-volume)
    *   [Manage snapshots](#manage-snapshots)
        *   [Create a snapshot](#create-a-snapshot)
        *   [List snapshots](#list-snapshots)
        *   [Delete a snapshot](#delete-a-snapshot)
    *   [Switch organizations or apps](#switch-organizations-or-apps)

The `deno sandbox` command allows you to spin up a secure Linux microVM, designed for running untrusted code in a sandboxed environment. See the [Sandbox documentation](/sandbox/cli/) for more detailed examples of usage.

## Authentication

In order to use the `deno sandbox` command, you need to have a Deno Deploy account and a valid authentication token. Follow the instructions in the [Getting started with Deno Sandbox](/sandbox/getting_started/) documentation.

## Global options

*   `-h`, `--help` - Show this help.
*   `--token` \- Auth token to use
*   `--config` \- Path for the config file
*   `--org` \- The name of the organization

## Subcommands

### Create a new sandbox

Creates a new sandbox in an organization. Accepts the aliases `create` and `new`.

\>\_

```sh
deno sandbox create
```

### List your sandboxes

Lists all sandboxes in an organization. Accepts the aliases `list` and `ls`.

\>\_

```sh
deno sandbox list
```

### Kill a sandbox

Terminates a running sandbox immediately. Accepts the aliases `kill`, `remove`, and `rm`.

\>\_

```sh
deno sandbox kill <sandbox-id>
```

### Copy files

Copies files between your local machine and a running sandbox. Use `copy` or its shorter alias `cp`.

\>\_

```sh
deno sandbox copy <paths...>
```

### Execute a command

Runs an arbitrary command inside an existing sandbox.

\>\_

```sh
deno sandbox exec <sandbox-id> <command...>
```

Example:

\>\_

```sh
deno sandbox exec sbx-1234 uptime
```

### Extend timeout

Extends how long a sandbox stays active before timing out.

\>\_

```sh
deno sandbox extend <sandbox-id> <timeout>
```

Accepts time durations in the format of a number followed by a unit, where the unit can be `s` for seconds, `m` for minutes, or `h` for hours.

Example:

\>\_

```sh
deno sandbox extend <sandbox-id> 30m
```

### SSH into a sandbox

Opens an interactive SSH session to the sandbox.

\>\_

```sh
deno sandbox ssh <sandbox-id>
```

### Deploy a sandbox

Turns the state of a running sandbox into a Deno Deploy application.

\>\_

```sh
deno sandbox deploy <sandbox-id> <app>
```

### Manage volumes

Creates, lists, and attaches persistent block volumes.

\>\_

```sh
deno sandbox volumes --help
```

#### Create a volume

Creates a new volume. Accepts the alias `volumes create` or `volumes new`.

\>\_

```sh
deno sandbox volumes create <name>
```

#### List volumes

Lists all volumes in an organization. Accepts the alias `volumes list` or `volumes ls`.

\>\_

```sh
deno sandbox volumes list
```

#### Delete a volume

Deletes a volume. Accepts the alias `volumes delete`, `volumes rm` or `volumes remove`.

\>\_

```sh
deno sandbox volumes delete <volume-id-or-slug>
```

or

\>\_

```sh
deno sandbox volumes delete <volume-slug>
```

#### Snapshot a volume

Creates a snapshot of a volume. Accepts a volume ID or slug and a snapshot slug

\>\_

```sh
deno sandbox volumes snapshot <volume-id-or-slug> <snapshot-slug>
```

or

\>\_

```sh
deno sandbox volumes snapshot <volume-slug> <snapshot-slug>
```

### Manage snapshots

Creates and restores filesystem snapshots for sandboxes.

\>\_

```sh
deno sandbox snapshots --help
```

#### Create a snapshot

Creates a new snapshot of a sandbox. Accepts the alias `snapshots create` or `snapshots new`. It requires a volume ID or volume slug and a snapshot slug.

\>\_

```sh
deno sandbox snapshots create <volume-id-or-slug> <snapshot-slug>
```

#### List snapshots

Lists all snapshots in an organization. Accepts the alias `snapshots list` or `snapshots ls`.

\>\_

```sh
deno sandbox snapshots list
```

#### Delete a snapshot

Deletes a snapshot. Accepts the alias `snapshots delete`, `snapshots rm` or `snapshots remove`. It requires a snapshot ID or snapshot slug.

\>\_

```sh
deno sandbox snapshots delete <id-or-slug>
```

### Switch organizations or apps

Switches your current Deploy organization or application context, which the sandbox command uses for authentication.

\>\_

```sh
deno sandbox switch
```

Command line usage:

```
deno sandbox [OPTIONS] [args]...
```
