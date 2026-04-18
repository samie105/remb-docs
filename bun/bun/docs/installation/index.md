---
title: "Installation"
source: "https://www.bun.com/docs/installation"
canonical_url: "https://bun.com/docs/installation"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:53.187Z"
content_hash: "e526f403d65500393cddd6ad80c0fc95abb05c305c1429ae4448d0b88437e1fe"
menu_path: ["Installation"]
section_path: []
nav_next: {"path": "bun/bun/docs/pm/bunx/index.md", "title": "bunx"}
nav_prev: {"path": "bun/bun/docs/guides/write-file/unlink/index.md", "title": "Delete a file"}
---

# Output: 1.x.y

# See the precise commit of `oven-sh/bun` that you're using
bun --revision
# Output: 1.x.y+b7982ac13189
```

If you’ve installed Bun but are seeing a `command not found` error, you may have to manually add the installation directory (`~/.bun/bin`) to your `PATH`.

Add Bun to your PATH

*   macOS & Linux
    
*   Windows
    

1

[

](#)

Determine which shell you're using

terminal

```
echo $SHELL
# /bin/zsh  or /bin/bash or /bin/fish
```

2

[

](#)

Open your shell configuration file

*   For bash: `~/.bashrc`
*   For zsh: `~/.zshrc`
*   For fish: `~/.config/fish/config.fish`

3

[

](#)

Add the Bun directory to PATH

Add this line to your configuration file:

terminal

```
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"
```

4

[

](#)

Reload your shell configuration

terminal

```
source ~/.bashrc  # or ~/.zshrc
```

1

[

](#)

Determine if the bun binary is properly installed

terminal

```
& "$env:USERPROFILE\.bun\bin\bun" --version
```

If the command runs successfully but `bun --version` is not recognized, it means that bun is not in your system’s PATH. To fix this, open a Powershell terminal and run the following command:

terminal

```
[System.Environment]::SetEnvironmentVariable(
  "Path",
  [System.Environment]::GetEnvironmentVariable("Path", "User") + ";$env:USERPROFILE\.bun\bin",
  [System.EnvironmentVariableTarget]::User
)
```

2

[

](#)

Restart your terminal

After running the command, restart your terminal and test with `bun --version`

terminal

```
bun --version
```

* * *

## 

[​

](#upgrading)

Upgrading

Once installed, the binary can upgrade itself:

terminal

```
bun upgrade
```

**Homebrew users**  
To avoid conflicts with Homebrew, use `brew upgrade bun` instead.**Scoop users**  
To avoid conflicts with Scoop, use `scoop update bun` instead.

* * *

## 

[​

](#canary-builds)

Canary Builds

[\-> View canary build](https://github.com/oven-sh/bun/releases/tag/canary) Bun automatically releases an (untested) canary build on every commit to main. To upgrade to the latest canary build:

terminal

```
# Upgrade to latest canary
bun upgrade --canary

# Switch back to stable
bun upgrade --stable
```

The canary build is useful for testing new features and bug fixes before they’re released in a stable build. To help the Bun team fix bugs faster, canary builds automatically upload crash reports to Bun’s team.

* * *

## 

[​

](#installing-older-versions)

Installing Older Versions

Since Bun is a single binary, you can install older versions by re-running the installer script with a specific version.

*   Linux & macOS
    
*   Windows
    

To install a specific version, pass the git tag to the install script:

terminal

```
curl -fsSL https://bun.com/install | bash -s "bun-v1.3.3"
```

On Windows, pass the version number to the PowerShell install script:

PowerShell

```
iex "& {$(irm https://bun.com/install.ps1)} -Version 1.3.3"
```

* * *

## 

[​

](#direct-downloads)

Direct Downloads

To download Bun binaries directly, visit the [releases page on GitHub](https://github.com/oven-sh/bun/releases).

### 

[​

](#latest-version-downloads)

Latest Version Downloads

### 

[​

](#musl-binaries)

Musl Binaries

For distributions without `glibc` (Alpine Linux, Void Linux):

*   [Linux x64 musl](https://github.com/oven-sh/bun/releases/latest/download/bun-linux-x64-musl.zip)
*   [Linux x64 musl baseline](https://github.com/oven-sh/bun/releases/latest/download/bun-linux-x64-musl-baseline.zip)
*   [Linux ARM64 musl](https://github.com/oven-sh/bun/releases/latest/download/bun-linux-aarch64-musl.zip)

If you encounter an error like `bun: /lib/x86_64-linux-gnu/libm.so.6: version GLIBC_2.29 not found`, try using the musl binary. Bun’s install script automatically chooses the correct binary for your system.

* * *

## 

[​

](#cpu-requirements)

CPU Requirements

Bun has specific CPU requirements based on the binary you’re using:

*   Standard Builds
    
*   Baseline Builds
    

**x64 binaries** target the Haswell CPU architecture (AVX and AVX2 instructions required)

Platform

Intel Requirement

AMD Requirement

x64

Haswell (4th gen Core) or newer

Excavator or newer

**x64-baseline binaries** target the Nehalem architecture for older CPUs

Platform

Intel Requirement

AMD Requirement

x64-baseline

Nehalem (1st gen Core) or newer

Bulldozer or newer

Baseline builds are slower than regular builds. Use them only if you encounter an “Illegal Instruction” error.

Bun does not support CPUs older than the baseline target, which mandates the SSE4.2 extension. macOS requires version 13.0 or later.

* * *

## 

[​

](#uninstall)

Uninstall

To remove Bun from your system:

*   macOS & Linux
    
*   Windows
    
*   Package Managers
    

terminal

```
rm -rf ~/.bun
```

PowerShell

```
powershell -c ~\.bun\uninstall.ps1
```

```
npm uninstall -g bun
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/installation.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /installation>)

[

Welcome to Bun

Previous

](/docs)[

Quickstart

Next

](/docs/quickstart)


