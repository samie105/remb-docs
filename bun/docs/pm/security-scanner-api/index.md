---
title: "Security Scanner API"
source: "https://bun.com/docs/pm/security-scanner-api"
canonical_url: "https://bun.com/docs/pm/security-scanner-api"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:07.172Z"
content_hash: "0d107bff7d7178c3afee261aed8ce1fcc74898c7e61b529b90c9da0b8d83b7aa"
menu_path: ["Security Scanner API"]
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

Bun’s package manager can scan packages for security vulnerabilities before installation, helping protect your applications from supply chain attacks and known vulnerabilities.

* * *

## 

[​

](#quick-start)

Quick Start

Configure a security scanner in your `bunfig.toml`:

bunfig.toml

```
[install.security]
scanner = "@acme/bun-security-scanner"
```

When configured, Bun will:

*   Scan all packages before installation
*   Display security warnings and advisories
*   Cancel installation if critical vulnerabilities are found
*   Automatically disable auto-install for security

* * *

## 

[​

](#how-it-works)

How It Works

Security scanners analyze packages during `bun install`, `bun add`, and other package operations. They can detect:

*   Known security vulnerabilities (CVEs)
*   Malicious packages
*   License compliance issues
*   …and more!

### 

[​

](#security-levels)

Security Levels

Scanners report issues at two severity levels:

*   **`fatal`** - Installation stops immediately, exits with non-zero code
*   **`warn`** - In interactive terminals, prompts to continue; in CI, exits immediately

* * *

## 

[​

](#using-pre-built-scanners)

Using Pre-built Scanners

Many security companies publish Bun security scanners as npm packages that you can install and use immediately.

### 

[​

](#installing-a-scanner)

Installing a Scanner

Install a security scanner from npm:

terminal

```
bun add -d @acme/bun-security-scanner
```

Consult your security scanner’s documentation for their specific package name and installation instructions. Most scanners will be installed with `bun add`.

### 

[​

](#configuring-the-scanner)

Configuring the Scanner

After installation, configure it in your `bunfig.toml`:

bunfig.toml

```
[install.security]
scanner = "@acme/bun-security-scanner"
```

### 

[​

](#enterprise-configuration)

Enterprise Configuration

Some enterprise scanners might support authentication and/or configuration through environment variables:

terminal

```
# This might go in ~/.bashrc, for example
export SECURITY_API_KEY="your-api-key"

# The scanner will now use these credentials automatically
bun install
```

Consult your security scanner’s documentation to learn which environment variables to set and if any additional configuration is required.

### 

[​

](#authoring-your-own-scanner)

Authoring your own scanner

For a complete example with tests and CI setup, see the official template: [github.com/oven-sh/security-scanner-template](https://github.com/oven-sh/security-scanner-template)

## 

[​

](#related)

Related

*   [Configuration (bunfig.toml)](/docs/runtime/bunfig#install-security-scanner)
*   [Package Manager](/docs/installation)
*   [Security Scanner Template](https://github.com/oven-sh/security-scanner-template)

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/pm/security-scanner-api.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /pm/security-scanner-api>)

[

Overrides and resolutions

Previous

](/docs/pm/overrides)[

.npmrc support

Next

](/docs/pm/npmrc)
