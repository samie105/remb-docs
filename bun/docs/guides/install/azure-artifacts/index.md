---
title: "Using bun install with an Azure Artifacts npm registry"
source: "https://bun.com/docs/guides/install/azure-artifacts"
canonical_url: "https://bun.com/docs/guides/install/azure-artifacts"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:37.360Z"
content_hash: "1e62adb5a5a8c72c2c2f839569a306323f62349c60c9720b21167101962dcf09"
menu_path: ["Using bun install with an Azure Artifacts npm registry"]
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

In [Azure Artifact’s](https://learn.microsoft.com/en-us/azure/devops/artifacts/npm/npmrc?view=azure-devops&tabs=windows%2Cclassic) instructions for `.npmrc`, they say to base64 encode the password. Do not do this for `bun install`. Bun will automatically base64 encode the password for you if needed.

[Azure Artifacts](https://azure.microsoft.com/en-us/products/devops/artifacts) is a package management system for Azure DevOps. It allows you to host your own private npm registry, npm packages, and other types of packages as well.

* * *

### 

[​

](#configure-with-bunfig-toml)

Configure with bunfig.toml

* * *

To use it with `bun install`, add a `bunfig.toml` file to your project with the following contents. Make sure to replace `my-azure-artifacts-user` with your Azure Artifacts username, such as `jarred1234`.

bunfig.toml

```
[install.registry]
url = "https://pkgs.dev.azure.com/my-azure-artifacts-user/_packaging/my-azure-artifacts-user/npm/registry"
username = "my-azure-artifacts-user"
# You can use an environment variable here
password = "$NPM_PASSWORD"
```

* * *

Then assign your Azure Personal Access Token to the `NPM_PASSWORD` environment variable. Bun [automatically reads](/docs/runtime/environment-variables) `.env` files, so create a file called `.env` in your project root. There is no need to base-64 encode this token! Bun will do this for you.

.env

```
NPM_PASSWORD=<paste token here>
```

* * *

### 

[​

](#configure-with-environment-variables)

Configure with environment variables

* * *

To configure Azure Artifacts without `bunfig.toml`, you can set the `NPM_CONFIG_REGISTRY` environment variable. The URL should include `:username` and `:_password` as query parameters. Replace `<USERNAME>` and `<PASSWORD>` with the appropriate values.

terminal

```
NPM_CONFIG_REGISTRY=https://pkgs.dev.azure.com/my-azure-artifacts-user/_packaging/my-azure-artifacts-user/npm/registry/:username=<USERNAME>:_password=<PASSWORD>
```

* * *

### 

[​

](#don’t-base64-encode-the-password)

Don’t base64 encode the password

* * *

In [Azure Artifact’s](https://learn.microsoft.com/en-us/azure/devops/artifacts/npm/npmrc?view=azure-devops&tabs=windows%2Cclassic) instructions for `.npmrc`, they say to base64 encode the password. Do not do this for `bun install`. Bun will automatically base64 encode the password for you if needed.

**Tip** — If it ends with `==`, it probably is base64 encoded.

* * *

To decode a base64-encoded password, open your browser console and run:

browser

```
atob("<base64-encoded password>");
```

* * *

Alternatively, use the `base64` command line tool, but doing so means it may be saved in your terminal history which is not recommended:

terminal

```
echo "base64-encoded-password" | base64 --decode
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/azure-artifacts.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/azure-artifacts>)

[

Configure a private registry for an organization scope with bun install

Previous

](/docs/guides/install/registry-scope)[

Using bun install with Artifactory

Next

](/docs/guides/install/jfrog-artifactory)
