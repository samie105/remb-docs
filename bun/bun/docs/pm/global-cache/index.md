---
title: "Global cache"
source: "https://bun.com/docs/pm/global-cache"
canonical_url: "https://bun.com/docs/pm/global-cache"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:51.009Z"
content_hash: "c858d5f4adc165f07f599241c5b0b3cfb58e5253e6b8de9a2a6366aadb071c9e"
menu_path: ["Global cache"]
section_path: []
nav_prev: {"path": "bun/bun/docs/pm/filter/index.md", "title": "bun --filter"}
nav_next: {"path": "bun/bun/docs/pm/isolated-installs/index.md", "title": "Isolated installs"}
---

# the directory to use for the cache
dir = "~/.bun/install/cache"

# when true, don't load from the global cache.
# Bun may still write to node_modules/.cache
disable = false

# when true, always resolve the latest versions from the registry
disableManifest = false
```

* * *

## 

[​

](#minimizing-re-downloads)

Minimizing re-downloads

Bun strives to avoid re-downloading packages multiple times. When installing a package, if the cache already contains a version in the range specified by `package.json`, Bun will use the cached package instead of downloading it again.

Installation details

If the semver version has pre-release suffix (`1.0.0-beta.0`) or a build suffix (`1.0.0+20220101`), it is replaced with a hash of that value instead, to reduce the chances of errors associated with long file paths.When the `node_modules` folder exists, before installing, Bun checks that `node_modules` contains all expected packages with appropriate versions. If so `bun install` completes. Bun uses a custom JSON parser which stops parsing as soon as it finds `"name"` and `"version"`.If a package is missing or has a version incompatible with the `package.json`, Bun checks for a compatible module in the cache. If found, it is installed into `node_modules`. Otherwise, the package will be downloaded from the registry then installed.

* * *

## 

[​

](#fast-copying)

Fast copying

Once a package is downloaded into the cache, Bun still needs to copy those files into `node_modules`. Bun uses the fastest syscalls available to perform this task. On Linux, it uses hardlinks; on macOS, it uses `clonefile`.

* * *

## 

[​

](#saving-disk-space)

Saving disk space

Since Bun uses hardlinks to “copy” a module into a project’s `node_modules` directory on Linux and Windows, the contents of the package only exist in a single location on disk, greatly reducing the amount of disk space dedicated to `node_modules`. This benefit also applies to macOS, but there are exceptions. It uses `clonefile` which is copy-on-write, meaning it will not occupy disk space, but it will count towards drive’s limit. This behavior is useful if something attempts to patch `node_modules/*`, so it’s impossible to affect other installations.

Installation strategies

This behavior is configurable with the `--backend` flag, which is respected by all of Bun’s package management commands.

*   **`hardlink`**: Default on Linux and Windows.
*   **`clonefile`** Default on macOS.
*   **`clonefile_each_dir`**: Similar to `clonefile`, except it clones each file individually per directory. It is only available on macOS and tends to perform slower than `clonefile`.
*   **`copyfile`**: The fallback used when any of the above fail. It is the slowest option. On macOS, it uses `fcopyfile()`; on Linux it uses `copy_file_range()`.
*   **`symlink`**: Currently used only `file:` (and eventually `link:`) dependencies. To prevent infinite loops, it skips symlinking the `node_modules` folder.

If you install with `--backend=symlink`, Node.js won’t resolve node\_modules of dependencies unless each dependency has its own `node_modules` folder or you pass `--preserve-symlinks` to `node`. See [Node.js documentation on `--preserve-symlinks`](https://nodejs.org/api/cli.html#--preserve-symlinks).

terminal

```
bun install --backend symlink
node --preserve-symlinks ./foo.js
```

Bun’s runtime does not currently expose an equivalent of `--preserve-symlinks`.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/pm/global-cache.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /pm/global-cache>)

[

bun --filter

Previous

](/docs/pm/filter)[

Isolated installs

Next

](/docs/pm/isolated-installs)
