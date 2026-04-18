---
title: "Add a trusted dependency"
source: "https://bun.com/docs/guides/install/trusted"
canonical_url: "https://bun.com/docs/guides/install/trusted"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:17.914Z"
content_hash: "afbb9af7f99ad2be16107ab3201f138c298bb31fd660f850f149425609abb815"
menu_path: ["Add a trusted dependency"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/install/registry-scope/index.md", "title": "Configure a private registry for an organization scope with bun install"}
nav_next: {"path": "bun/bun/docs/guides/install/workspaces/index.md", "title": "Configuring a monorepo using workspaces"}
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

Unlike other npm clients, Bun does not execute arbitrary lifecycle scripts for installed dependencies, such as `postinstall` and `node-gyp` builds. These scripts represent a potential security risk, as they can execute arbitrary code on your machine.

Bun includes a default allowlist of popular packages containing `postinstall` scripts that are known to be safe. You can see this list [here](https://github.com/oven-sh/bun/blob/main/src/install/default-trusted-dependencies.txt). This default list only applies to packages installed from npm. For packages from other sources (such as `file:`, `link:`, `git:`, or `github:` dependencies), you must explicitly add them to `trustedDependencies`.

* * *

If you are seeing one of the following errors, you are probably trying to use a package that uses `postinstall` to work properly:

*   `error: could not determine executable to run for package`
*   `InvalidExe`

* * *

To allow Bun to execute lifecycle scripts for a specific package, add the package to `trustedDependencies` in your package.json file. You can do this automatically by running the command `bun pm trust <pkg>`.

Note that this only allows lifecycle scripts for the specific package listed in `trustedDependencies`, _not_ the dependencies of that dependency!

package.json

```
{
  "name": "my-app",
  "version": "1.0.0",
  "trustedDependencies": ["my-trusted-package"] 
}
```

* * *

Once this is added, run a fresh install. Bun will re-install your dependencies and properly install

terminal

```
rm -rf node_modules
rm bun.lock
bun install
```

* * *

See [Docs > Package manager > Trusted dependencies](/docs/pm/lifecycle) for complete documentation of trusted dependencies.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/trusted.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/trusted>)

[

Using bun install with Artifactory

Previous

](/docs/guides/install/jfrog-artifactory)[

Generate a yarn-compatible lockfile

Next

](/docs/guides/install/yarnlock)

