---
title: "Using bun install with Artifactory"
source: "https://bun.com/docs/guides/install/jfrog-artifactory"
canonical_url: "https://bun.com/docs/guides/install/jfrog-artifactory"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:03.947Z"
content_hash: "a1ed2fecca79b5f5681fb7f80e41e75b578b26664ca31bb13457798ac5463590"
menu_path: ["Using bun install with Artifactory"]
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

[JFrog Artifactory](https://jfrog.com/artifactory/) is a package management system for npm, Docker, Maven, NuGet, Ruby, Helm, and more. It allows you to host your own private npm registry, npm packages, and other types of packages as well. To use it with `bun install`, add a `bunfig.toml` file to your project with the following contents:

* * *

### 

[​

](#configure-with-bunfig-toml)

Configure with bunfig.toml

Make sure to replace `MY_SUBDOMAIN` with your JFrog Artifactory subdomain, such as `jarred1234` and MY\_TOKEN with your JFrog Artifactory token.

bunfig.toml

```
[install.registry]
url = "https://MY_SUBDOMAIN.jfrog.io/artifactory/api/npm/npm/_auth=MY_TOKEN"
# You can use an environment variable here
# url = "$NPM_CONFIG_REGISTRY"
```

* * *

### 

[​

](#configure-with-$npm-config-registry)

Configure with `$NPM_CONFIG_REGISTRY`

Like with npm, you can use the `NPM_CONFIG_REGISTRY` environment variable to configure JFrog Artifactory with bun install.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/jfrog-artifactory.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/jfrog-artifactory>)

[

Using bun install with an Azure Artifacts npm registry

Previous

](/docs/guides/install/azure-artifacts)[

Add a trusted dependency

Next

](/docs/guides/install/trusted)
