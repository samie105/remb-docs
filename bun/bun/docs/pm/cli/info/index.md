---
title: "bun info"
source: "https://bun.com/docs/pm/cli/info"
canonical_url: "https://bun.com/docs/pm/cli/info"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:15.598Z"
content_hash: "23935cd7c0accd4005c501573c7bcf9370bfedb167befe9f06accb1c35b2fe08"
menu_path: ["bun info"]
section_path: []
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

`bun info` displays package metadata from the npm registry.

## 

[​

](#usage)

Usage

terminal

```
bun info react
```

This will display information about the `react` package, including its latest version, description, homepage, dependencies, and more.

## 

[​

](#viewing-specific-versions)

Viewing specific versions

To view information about a specific version:

terminal

```
bun info react@18.0.0
```

## 

[​

](#viewing-specific-properties)

Viewing specific properties

You can also query specific properties from the package metadata:

terminal

```
bun info react version
bun info react dependencies
bun info react repository.url
```

## 

[​

](#json-output)

JSON output

To get the output in JSON format, use the `--json` flag:

terminal

```
bun info react --json
```

## 

[​

](#alias)

Alias

`bun pm view` is an alias for `bun info`:

terminal

```
bun pm view react  # equivalent to: bun info react
```

## 

[​

](#examples)

Examples

terminal

```
# View basic package information
bun info is-number

# View a specific version
bun info is-number@7.0.0

# View all available versions
bun info is-number versions

# View package dependencies
bun info express dependencies

# View package homepage
bun info lodash homepage

# Get JSON output
bun info react --json
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/pm/cli/info.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /pm/cli/info>)

[

bun audit

Previous

](/docs/pm/cli/audit)[

Workspaces

Next

](/docs/pm/workspaces)
