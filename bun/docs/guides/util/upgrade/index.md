---
title: "Upgrade Bun to the latest version"
source: "https://bun.com/docs/guides/util/upgrade"
canonical_url: "https://bun.com/docs/guides/util/upgrade"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:18.420Z"
content_hash: "23708b2600862785b3e9295983644687904d600796703f165514e256b160287e"
menu_path: ["Upgrade Bun to the latest version"]
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

Bun can upgrade itself using the built-in `bun upgrade` command. This is the fastest way to get the latest features and bug fixes.

terminal

```
bun upgrade
```

This downloads and installs the latest stable version of Bun, replacing the currently installed version.

To see the current version of Bun, run `bun --version`.

* * *

## 

[​

](#verify-the-upgrade)

Verify the upgrade

After upgrading, verify the new version:

terminal

```
bun --version
# Output: 1.x.y

# See the exact commit of the Bun binary
bun --revision
# Output: 1.x.y+abc123def
```

* * *

## 

[​

](#upgrade-to-canary-builds)

Upgrade to canary builds

Canary builds are automatically released on every commit to the `main` branch. These are untested but useful for trying new features or verifying bug fixes before they’re released.

terminal

```
bun upgrade --canary
```

Canary builds are not recommended for production use. They may contain bugs or breaking changes.

* * *

## 

[​

](#switch-back-to-stable)

Switch back to stable

If you’re on a canary build and want to return to the latest stable release:

terminal

```
bun upgrade --stable
```

* * *

## 

[​

](#install-a-specific-version)

Install a specific version

To install a specific version of Bun, use the install script with a version tag:

*   macOS & Linux
    
*   Windows
    

terminal

```
curl -fsSL https://bun.sh/install | bash -s "bun-v1.3.3"
```

PowerShell

```
iex "& {$(irm https://bun.sh/install.ps1)} -Version 1.3.3"
```

* * *

## 

[​

](#package-manager-users)

Package manager users

If you installed Bun via a package manager, use that package manager to upgrade instead of `bun upgrade` to avoid conflicts.

**Homebrew users**  
To avoid conflicts with Homebrew, use `brew upgrade bun` instead.**Scoop users**  
To avoid conflicts with Scoop, use `scoop update bun` instead.

* * *

## 

[​

](#see-also)

See also

*   [Installation](/docs/installation) — Install Bun for the first time
*   [Update packages](/docs/pm/cli/update) — Update dependencies to latest versions

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/upgrade.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/upgrade>)

[

Codesign a single-file JavaScript executable on macOS

Previous

](/docs/guides/runtime/codesign-macos-executable)[

Detect when code is executed with Bun

Next

](/docs/guides/util/detect-bun)
