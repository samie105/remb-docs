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
nav_prev: {"path": "bun/bun/docs/guides/util/sleep/index.md", "title": "Sleep for a fixed number of milliseconds"}
nav_next: {"path": "bun/bun/docs/guides/util/which-path-to-executable-bin/index.md", "title": "Get the path to an executable bin file"}
---

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

