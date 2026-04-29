---
title: "bun audit"
source: "https://bun.com/docs/pm/cli/audit"
canonical_url: "https://bun.com/docs/pm/cli/audit"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:09.657Z"
content_hash: "64190d66a765f255b8d3aebd4e8d48801f52e6aada88af054d13ed4398157fdf"
menu_path: ["bun audit"]
section_path: []
nav_prev: {"path": "../add/index.md", "title": "bun add"}
nav_next: {"path": "../info/index.md", "title": "bun info"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](/docs)[Package Manager

](/docs/pm/cli/install)[Bundler

](/docs/bundler)[Test Runner

](/docs/test)[Guides

](/docs/guides)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](/docs/feedback)

Run the command in a project with a `bun.lock` file:

terminal

```
bun audit
```

Bun sends the list of installed packages and versions to NPM, and prints a report of any vulnerabilities that were found. Packages installed from registries other than the default registry are skipped. If no vulnerabilities are found, the command prints:

```
No vulnerabilities found
```

When vulnerabilities are detected, each affected package is listed along with the severity, a short description and a link to the advisory. At the end of the report Bun prints a summary and hints for updating:

```
3 vulnerabilities (1 high, 2 moderate)
To update all dependencies to the latest compatible versions:
  bun update
To update all dependencies to the latest versions (including breaking changes):
  bun update --latest
```

### 

[​

](#filtering-options)

Filtering options

**`--audit-level=<low|moderate|high|critical>`** - Only show vulnerabilities at this severity level or higher:

terminal

```
bun audit --audit-level=high
```

**`--prod`** - Audit only production dependencies (excludes devDependencies):

terminal

```
bun audit --prod
```

**`--ignore <CVE>`** - Ignore specific CVEs (can be used multiple times):

terminal

```
bun audit --ignore CVE-2022-25883 --ignore CVE-2023-26136
```

### 

[​

](#json)

`--json`

Use the `--json` flag to print the raw JSON response from the registry instead of the formatted report:

terminal

```
bun audit --json
```

### 

[​

](#exit-code)

Exit code

`bun audit` will exit with code `0` if no vulnerabilities are found and `1` if the report lists any vulnerabilities. This will still happen even if `--json` is passed.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/pm/cli/audit.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /pm/cli/audit>)

[

bun why

Previous

](/docs/pm/cli/why)[

bun info

Next

](/docs/pm/cli/info)
