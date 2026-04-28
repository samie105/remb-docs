---
title: "Lifecycle scripts"
source: "https://bun.com/docs/pm/lifecycle"
canonical_url: "https://bun.com/docs/pm/lifecycle"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:56.219Z"
content_hash: "a00253a74bb22d5b80d97dd3231f91fbfe44b51255d5e93669421131f232e9f1"
menu_path: ["Lifecycle scripts"]
section_path: []
nav_prev: {"path": "bun/docs/pm/isolated-installs/index.md", "title": "Isolated installs"}
nav_next: {"path": "bun/docs/pm/lockfile/index.md", "title": "Lockfile"}
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

Packages on `npm` can define _lifecycle scripts_ in their `package.json`. Some of the most common are below, but there are [many others](https://docs.npmjs.com/cli/v10/using-npm/scripts).

*   `preinstall`: Runs before the package is installed
*   `postinstall`: Runs after the package is installed
*   `preuninstall`: Runs before the package is uninstalled
*   `prepublishOnly`: Runs before the package is published

These scripts are arbitrary shell commands that the package manager is expected to read and execute at the appropriate time. But executing arbitrary scripts represents a potential security risk, so—unlike other `npm` clients—Bun does not execute arbitrary lifecycle scripts by default.

* * *

## 

[​

](#postinstall)

`postinstall`

The `postinstall` script is particularly important. It’s widely used to build or install platform-specific binaries for packages that are implemented as [native Node.js add-ons](https://nodejs.org/api/addons.html). For example, `node-sass` is a popular package that uses `postinstall` to build a native binary for Sass.

package.json

```
{
  "name": "my-app",
  "version": "1.0.0",
  "dependencies": {
    "node-sass": "^6.0.1"
  }
}
```

* * *

## 

[​

](#trusteddependencies)

`trustedDependencies`

Instead of executing arbitrary scripts, Bun uses a “default-secure” approach. You can add certain packages to an allow list, and Bun will execute lifecycle scripts for those packages. To tell Bun to allow lifecycle scripts for a particular package, add the package name to `trustedDependencies` array in your `package.json`.

package.json

```
{
  "name": "my-app",
  "version": "1.0.0",
  "trustedDependencies": ["node-sass"] 
}
```

Once added to `trustedDependencies`, install/re-install the package. Bun will read this field and run lifecycle scripts for `my-trusted-package`. The top 500 npm packages with lifecycle scripts are allowed by default. You can see the full list [here](https://github.com/oven-sh/bun/blob/main/src/install/default-trusted-dependencies.txt).

The default trusted dependencies list only applies to packages installed from npm. For packages from other sources (such as `file:`, `link:`, `git:`, or `github:` dependencies), you must explicitly add them to `trustedDependencies` to run their lifecycle scripts, even if the package name matches an entry in the default list. This prevents malicious packages from spoofing trusted package names through local file paths or git repositories.

* * *

## 

[​

](#ignore-scripts)

`--ignore-scripts`

To disable lifecycle scripts for all packages, use the `--ignore-scripts` flag.

terminal

```
bun install --ignore-scripts
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/pm/lifecycle.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /pm/lifecycle>)

[

Lockfile

Previous

](/docs/pm/lockfile)[

Scopes and registries

Next

](/docs/pm/scopes-registries)
