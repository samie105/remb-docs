---
title: "bun why"
source: "https://bun.com/docs/pm/cli/why"
canonical_url: "https://bun.com/docs/pm/cli/why"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:46.313Z"
content_hash: "fec11b2778fb9b3be5b20f2ac26dfdf1a1bbf134dee1fff7830a00904ed8a510"
menu_path: ["bun why"]
section_path: []
nav_prev: {"path": "bun/bun/docs/pm/cli/update/index.md", "title": "bun update"}
nav_next: {"path": "bun/bun/docs/pm/filter/index.md", "title": "bun --filter"}
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

The `bun why` command explains why a package is installed in your project by showing the dependency chain that led to its installation.

## 

[​

](#usage)

Usage

terminal

```
bun why <package>
```

## 

[​

](#arguments)

Arguments

*   `<package>`: The name of the package to explain. Supports glob patterns like `@org/*` or `*-lodash`.

## 

[​

](#options)

Options

*   `--top`: Show only the top-level dependencies instead of the complete dependency tree.
*   `--depth <number>`: Maximum depth of the dependency tree to display.

## 

[​

](#examples)

Examples

Check why a specific package is installed:

terminal

```
bun why react
```

```
react@18.2.0
  └─ my-app@1.0.0 (requires ^18.0.0)
```

Check why all packages with a specific pattern are installed:

terminal

```
bun why "@types/*"
```

```
@types/react@18.2.15
  └─ dev my-app@1.0.0 (requires ^18.0.0)

@types/react-dom@18.2.7
  └─ dev my-app@1.0.0 (requires ^18.0.0)
```

Show only top-level dependencies:

terminal

```
bun why express --top
```

```
express@4.18.2
  └─ my-app@1.0.0 (requires ^4.18.2)
```

Limit the dependency tree depth:

terminal

```
bun why express --depth 2
```

```
express@4.18.2
  └─ express-pollyfill@1.20.1 (requires ^4.18.2)
     └─ body-parser@1.20.1 (requires ^1.20.1)
     └─ accepts@1.3.8 (requires ^1.3.8)
        └─ (deeper dependencies hidden)
```

## 

[​

](#understanding-the-output)

Understanding the Output

The output shows:

*   The package name and version being queried
*   The dependency chain that led to its installation
*   The type of dependency (dev, peer, optional, or production)
*   The version requirement specified in each package’s dependencies

For nested dependencies, the command shows the complete dependency tree by default, with indentation indicating the relationship hierarchy.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/pm/cli/why.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /pm/cli/why>)

[

bun outdated

Previous

](/docs/pm/cli/outdated)[

bun audit

Next

](/docs/pm/cli/audit)


