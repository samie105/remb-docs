---
title: "deno approve-scripts"
source: "https://docs.deno.com/runtime/reference/cli/approve_scripts/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/approve_scripts/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:25:36.033Z"
content_hash: "796331243a7acf801b9db0e7812e51777d0d8b3ca3ee3f78cce2006a5f1e9b27"
menu_path: ["deno approve-scripts"]
section_path: []
content_language: "en"
nav_prev: {"path": "../add/index.md", "title": "deno add"}
nav_next: {"path": "../audit/index.md", "title": "deno audit"}
---

**On this page**

-   [Basic usage](#basic-usage)
-   [Why lifecycle scripts are blocked by default](#why-lifecycle-scripts-are-blocked-by-default)
-   [Options](#options)

`deno approve-scripts` lets you review and approve pending npm lifecycle scripts (such as `postinstall`) in your dependency tree. Unlike npm, Deno does not run these scripts by default for security reasons.

## Basic usage

Review and approve pending scripts interactively:

\>\_

```sh
deno approve-scripts
```

This will show you which packages have lifecycle scripts that haven't been approved yet.

## Why lifecycle scripts are blocked by default

npm lifecycle scripts (such as `preinstall` and `postinstall`) run arbitrary code during the install process. This is a known supply chain attack vector — malicious packages can execute code on your machine just by being installed.

Deno takes a safer approach: lifecycle scripts must be explicitly approved before they run.

Command line usage:

```
deno approve-scripts [OPTIONS] [packages]...
```

Approve npm lifecycle scripts for installed dependencies.

## Options

`--lockfile-only`

Install only updating the lockfile.
