---
title: "bun install"
source: "https://bun.com/docs/pm/cli/install"
canonical_url: "https://bun.com/docs/pm/cli/install"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:27.135Z"
content_hash: "dc68141421e14db55c3cd93918f3eeabda57b75ae578f75e414d6ddf61cf0387"
menu_path: ["bun install"]
section_path: []
nav_prev: {"path": "bun/bun/docs/pm/cli/link/index.md", "title": "bun link"}
nav_next: {"path": "bun/bun/docs/pm/cli/outdated/index.md", "title": "bun outdated"}
---

# Install dependencies for all workspaces except `pkg-c`
bun install --filter '!pkg-c'

# Install dependencies for only `pkg-a` in `./packages/pkg-a`
bun install --filter './packages/pkg-a'
```

For more information on filtering with `bun install`, refer to [Package Manager > Filtering](bun/bun/docs/pm/filter/index.md#bun-install-and-bun-outdated)

* * *

## Overrides and resolutions

Bun supports npm’s `"overrides"` and Yarn’s `"resolutions"` in `package.json`. These are mechanisms for specifying a version range for _metadependencies_—the dependencies of your dependencies. Refer to [Package manager > Overrides and resolutions](bun/bun/docs/pm/overrides/index.md) for complete documentation.

package.json

```
{
  "name": "my-app",
  "dependencies": {
    "foo": "^2.0.0"
  },
  "overrides": { 
    "bar": "~4.4.0"
  } 
}
```

* * *

## Global packages

To install a package globally, use the `-g`/`--global` flag. Typically this is used for installing command-line tools.

terminal

```
bun install --global cowsay # or `bun install -g cowsay`
cowsay "Bun!"
```

```
 ______
< Bun! >
 ------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

* * *

## Production mode

To install in production mode (i.e. without `devDependencies` or `optionalDependencies`):

terminal

```
bun install --production
```

For reproducible installs, use `--frozen-lockfile`. This will install the exact versions of each package specified in the lockfile. If your `package.json` disagrees with `bun.lock`, Bun will exit with an error. The lockfile will not be updated.

terminal

```
bun install --frozen-lockfile
```

For more information on Bun’s lockfile `bun.lock`, refer to [Package manager > Lockfile](bun/bun/docs/pm/lockfile/index.md).

* * *

## Omitting dependencies

To omit dev, peer, or optional dependencies use the `--omit` flag.

terminal

```
# Exclude "devDependencies" from the installation. This will apply to the
# root package and workspaces if they exist. Transitive dependencies will
# not have "devDependencies".
bun install --omit dev

# Install only dependencies from "dependencies"
bun install --omit=dev --omit=peer --omit=optional
```

* * *

## Dry run

To perform a dry run (i.e. don’t actually install anything):

terminal

```
bun install --dry-run
```

* * *

## Non-npm dependencies

Bun supports installing dependencies from Git, GitHub, and local or remotely-hosted tarballs. For complete documentation refer to [Package manager > Git, GitHub, and tarball dependencies](bun/bun/docs/pm/cli/add/index.md).

package.json

```
{
  "dependencies": {
    "dayjs": "git+https://github.com/iamkun/dayjs.git",
    "lodash": "git+ssh://github.com/lodash/lodash.git#4.17.21",
    "moment": "git@github.com:moment/moment.git",
    "zod": "github:colinhacks/zod",
    "react": "https://registry.npmjs.org/react/-/react-18.2.0.tgz",
    "bun-types": "npm:@types/bun"
  }
}
```

* * *

## Installation strategies

Bun supports two package installation strategies that determine how dependencies are organized in `node_modules`:

### Hoisted installs

The traditional npm/Yarn approach that flattens dependencies into a shared `node_modules` directory:

terminal

```
bun install --linker hoisted
```

### Isolated installs

A pnpm-like approach that creates strict dependency isolation to prevent phantom dependencies:

terminal

```
bun install --linker isolated
```

Isolated installs create a central package store in `node_modules/.bun/` with symlinks in the top-level `node_modules`. This ensures packages can only access their declared dependencies.

### Default strategy

The default linker strategy depends on whether you’re starting fresh or have an existing project:

*   **New workspaces/monorepos**: `isolated` (prevents phantom dependencies)
*   **New single-package projects**: `hoisted` (traditional npm behavior)
*   **Existing projects (made pre-v1.3.2)**: `hoisted` (preserves backward compatibility)

The default is controlled by a `configVersion` field in your lockfile. For a detailed explanation, see [Package manager > Isolated installs](bun/bun/docs/pm/isolated-installs/index.md).

* * *

## Minimum release age

To protect against supply chain attacks where malicious packages are quickly published, you can configure a minimum age requirement for npm packages. Package versions published more recently than the specified threshold (in seconds) will be filtered out during installation.

terminal

```
# Only install package versions published at least 3 days ago
bun add @types/bun --minimum-release-age 259200 # seconds
```

You can also configure this in `bunfig.toml`:

bunfig.toml

```
[install]
# Only install package versions published at least 3 days ago
minimumReleaseAge = 259200 # seconds

# Exclude trusted packages from the age gate
minimumReleaseAgeExcludes = ["@types/node", "typescript"]
```

When the minimum age filter is active:

*   Only affects new package resolution - existing packages in `bun.lock` remain unchanged
*   All dependencies (direct and transitive) are filtered to meet the age requirement when being resolved
*   When versions are blocked by the age gate, a stability check detects rapid bugfix patterns
    *   If multiple versions were published close together just outside your age gate, it extends the filter to skip those potentially unstable versions and selects an older, more mature version
    *   Searches up to 7 days after the age gate, however if still finding rapid releases it ignores stability check
    *   Exact version requests (like `package@1.1.1`) still respect the age gate but bypass the stability check
*   Versions without a `time` field are treated as passing the age check (npm registry should always provide timestamps)

For more advanced security scanning, including integration with services & custom filtering, see [Package manager > Security Scanner API](bun/bun/docs/pm/security-scanner-api/index.md).

* * *

## Configuration

### Configuring `bun install` with `bunfig.toml`

`bunfig.toml` is searched for in the following paths on `bun install`, `bun remove`, and `bun add`:

1.  `$XDG_CONFIG_HOME/.bunfig.toml` or `$HOME/.bunfig.toml`
2.  `./bunfig.toml`

If both are found, the results are merged together. Configuring with `bunfig.toml` is optional. Bun tries to be zero configuration in general, but that’s not always possible. The default behavior of `bun install` can be configured in `bunfig.toml`. The default values are shown below.

bunfig.toml

```
[install]

# whether to install optionalDependencies
optional = true

# whether to install devDependencies
dev = true

# whether to install peerDependencies
peer = true

# equivalent to `--production` flag
production = false

# equivalent to `--save-text-lockfile` flag
saveTextLockfile = false

# equivalent to `--frozen-lockfile` flag
frozenLockfile = false

# equivalent to `--dry-run` flag
dryRun = false

# equivalent to `--concurrent-scripts` flag
concurrentScripts = 16 # (cpu count or GOMAXPROCS) x2

# installation strategy: "hoisted" or "isolated"
# default depends on lockfile configVersion and workspaces:
# - configVersion = 1: "isolated" if using workspaces, otherwise "hoisted"
# - configVersion = 0: "hoisted"
linker = "hoisted"

# minimum age config
minimumReleaseAge = 259200 # seconds
minimumReleaseAgeExcludes = ["@types/node", "typescript"]
```

### Configuring with environment variables

Environment variables have a higher priority than `bunfig.toml`.

Name

Description

`BUN_CONFIG_REGISTRY`

Set an npm registry (default: [https://registry.npmjs.org](https://registry.npmjs.org/))

`BUN_CONFIG_TOKEN`

Set an auth token (currently does nothing)

`BUN_CONFIG_YARN_LOCKFILE`

Save a Yarn v1-style yarn.lock

`BUN_CONFIG_LINK_NATIVE_BINS`

Point `bin` in package.json to a platform-specific dependency

`BUN_CONFIG_SKIP_SAVE_LOCKFILE`

Don’t save a lockfile

`BUN_CONFIG_SKIP_LOAD_LOCKFILE`

Don’t load a lockfile

`BUN_CONFIG_SKIP_INSTALL_PACKAGES`

Don’t install any packages

Bun always tries to use the fastest available installation method for the target platform. On macOS, that’s `clonefile` and on Linux, that’s `hardlink`. You can change which installation method is used with the `--backend` flag. When unavailable or on error, `clonefile` and `hardlink` fallsback to a platform-specific implementation of copying files. Bun stores installed packages from npm in `~/.bun/install/cache/${name}@${version}`. Note that if the semver version has a `build` or a `pre` tag, it is replaced with a hash of that value instead. This is to reduce the chances of errors from long file paths, but unfortunately complicates figuring out where a package was installed on disk. When the `node_modules` folder exists, before installing, Bun checks if the `"name"` and `"version"` in `package/package.json` in the expected node\_modules folder matches the expected `name` and `version`. This is how it determines whether it should install. It uses a custom JSON parser which stops parsing as soon as it finds `"name"` and `"version"`. When a `bun.lock` doesn’t exist or `package.json` has changed dependencies, tarballs are downloaded & extracted eagerly while resolving. When a `bun.lock` exists and `package.json` hasn’t changed, Bun downloads missing dependencies lazily. If the package with a matching `name` & `version` already exists in the expected location within `node_modules`, Bun won’t attempt to download the tarball.

## CI/CD

Use the official [`oven-sh/setup-bun`](https://github.com/oven-sh/setup-bun) action to install `bun` in a GitHub Actions pipeline:

.github/workflows/release.yml

```
name: bun-types
jobs:
  build:
    name: build-app
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4
      - name: Install bun
        uses: oven-sh/setup-bun@v2
      - name: Install dependencies
        run: bun install
      - name: Build app
        run: bun run build
```

For CI/CD environments that want to enforce reproducible builds, use `bun ci` to fail the build if the package.json is out of sync with the lockfile:

terminal

```
bun ci
```

This is equivalent to `bun install --frozen-lockfile`. It installs exact versions from `bun.lock` and fails if `package.json` doesn’t match the lockfile. To use `bun ci` or `bun install --frozen-lockfile`, you must commit `bun.lock` to version control. And instead of running `bun install`, run `bun ci`.

.github/workflows/release.yml

```
name: bun-types
jobs:
  build:
    name: build-app
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4
      - name: Install bun
        uses: oven-sh/setup-bun@v2
      - name: Install dependencies
        run: bun ci
      - name: Build app
        run: bun run build
```

## Platform-specific dependencies?

bun stores normalized `cpu` and `os` values from npm in the lockfile, along with the resolved packages. It skips downloading, extracting, and installing packages disabled for the current target at runtime. This means the lockfile won’t change between platforms/architectures even if the packages ultimately installed do change.

### `--cpu` and `--os` flags

You can override the target platform for package selection:

```
bun install --cpu=x64 --os=linux
```

This installs packages for the specified platform instead of the current system. Useful for cross-platform builds or when preparing deployments for different environments. **Accepted values for `--cpu`**: `arm64`, `x64`, `ia32`, `ppc64`, `s390x` **Accepted values for `--os`**: `linux`, `darwin`, `win32`, `freebsd`, `openbsd`, `sunos`, `aix`

## Peer dependencies?

Peer dependencies are handled similarly to yarn. `bun install` will automatically install peer dependencies. If the dependency is marked optional in `peerDependenciesMeta`, an existing dependency will be chosen if possible.

## Lockfile

`bun.lock` is Bun’s lockfile format. See [our blogpost about the text lockfile](https://bun.com/blog/bun-lock-text-lockfile). Prior to Bun 1.2, the lockfile was binary and called `bun.lockb`. Old lockfiles can be upgraded to the new format by running `bun install --save-text-lockfile --frozen-lockfile --lockfile-only`, and then deleting `bun.lockb`.

## Cache

To delete the cache:

```
bun pm cache rm
# or
rm -rf ~/.bun/install/cache
```

## Platform-specific backends

`bun install` uses different system calls to install dependencies depending on the platform. This is a performance optimization. You can force a specific backend with the `--backend` flag. **`hardlink`** is the default backend on Linux. Benchmarking showed it to be the fastest on Linux.

```
rm -rf node_modules
bun install --backend hardlink
```

**`clonefile`** is the default backend on macOS. Benchmarking showed it to be the fastest on macOS. It is only available on macOS.

```
rm -rf node_modules
bun install --backend clonefile
```

**`clonefile_each_dir`** is similar to `clonefile`, except it clones each file individually per directory. It is only available on macOS and tends to perform slower than `clonefile`. Unlike `clonefile`, this does not recursively clone subdirectories in one system call.

```
rm -rf node_modules
bun install --backend clonefile_each_dir
```

**`copyfile`** is the fallback used when any of the above fail, and is the slowest. on macOS, it uses `fcopyfile()` and on linux it uses `copy_file_range()`.

```
rm -rf node_modules
bun install --backend copyfile
```

**`symlink`** is typically only used for `file:` dependencies (and eventually `link:`) internally. To prevent infinite loops, it skips symlinking the `node_modules` folder. If you install with `--backend=symlink`, Node.js won’t resolve node\_modules of dependencies unless each dependency has its own node\_modules folder or you pass `--preserve-symlinks` to `node` or `bun`. See [Node.js documentation on `--preserve-symlinks`](https://nodejs.org/api/cli.html#--preserve-symlinks).

```
rm -rf node_modules
bun install --backend symlink
bun --preserve-symlinks ./my-file.js
node --preserve-symlinks ./my-file.js # https://nodejs.org/api/cli.html#--preserve-symlinks
```

Bun uses a binary format for caching NPM registry responses. This loads much faster than JSON and tends to be smaller on disk. You will see these files in `~/.bun/install/cache/*.npm`. The filename pattern is `${hash(packageName)}.npm`. It’s a hash so that extra directories don’t need to be created for scoped packages. Bun’s usage of `Cache-Control` ignores `Age`. This improves performance, but means bun may be about 5 minutes out of date to receive the latest package version metadata from npm.

## pnpm migration

Bun automatically migrates projects from pnpm to bun. When a `pnpm-lock.yaml` file is detected and no `bun.lock` file exists, Bun will automatically migrate the lockfile to `bun.lock` during installation. The original `pnpm-lock.yaml` file remains unmodified.

terminal

```
bun install
```

**Note**: Migration only runs when `bun.lock` is absent. There is currently no opt-out flag for pnpm migration. The migration process handles:

### Lockfile Migration

*   Converts `pnpm-lock.yaml` to `bun.lock` format
*   Preserves package versions and resolution information
*   Maintains dependency relationships and peer dependencies
*   Handles patched dependencies with integrity hashes

### Workspace Configuration

When a `pnpm-workspace.yaml` file exists, Bun migrates workspace settings to your root `package.json`:

pnpm-workspace.yaml

```
packages:
  - "apps/*"
  - "packages/*"

catalog:
  react: ^18.0.0
  typescript: ^5.0.0

catalogs:
  build:
    webpack: ^5.0.0
    babel: ^7.0.0
```

The workspace packages list and catalogs are moved to the `workspaces` field in `package.json`:

package.json

```
{
  "workspaces": {
    "packages": ["apps/*", "packages/*"],
    "catalog": {
      "react": "^18.0.0",
      "typescript": "^5.0.0"
    },
    "catalogs": {
      "build": {
        "webpack": "^5.0.0",
        "babel": "^7.0.0"
      }
    }
  }
}
```

### Catalog Dependencies

Dependencies using pnpm’s `catalog:` protocol are preserved:

package.json

```
{
  "dependencies": {
    "react": "catalog:",
    "webpack": "catalog:build"
  }
}
```

### Configuration Migration

The following pnpm configuration is migrated from both `pnpm-lock.yaml` and `pnpm-workspace.yaml`:

*   **Overrides**: Moved from `pnpm.overrides` to root-level `overrides` in `package.json`
*   **Patched Dependencies**: Moved from `pnpm.patchedDependencies` to root-level `patchedDependencies` in `package.json`
*   **Workspace Overrides**: Applied from `pnpm-workspace.yaml` to root `package.json`

### Requirements

*   Requires pnpm lockfile version 7 or higher
*   Workspace packages must have a `name` field in their `package.json`
*   All catalog entries referenced by dependencies must exist in the catalogs definition

After migration, you can safely remove `pnpm-lock.yaml` and `pnpm-workspace.yaml` files.

* * *

## CLI Usage

terminal

```
bun install <name>@<version>
```

### General Configuration

\--config

string

Specify path to config file (bunfig.toml)

\--cwd

string

Set a specific cwd

### Dependency Scope & Management

\--production

boolean

Don’t install devDependencies

\--no-save

boolean

Don’t update package.json or save a lockfile

\--save

boolean

default:"true"

Save to package.json

\--omit

string

Exclude ‘dev’, ‘optional’, or ‘peer’ dependencies from install

\--only-missing

boolean

Only add dependencies to package.json if they are not already present

### Dependency Type & Versioning

\--dev

boolean

Add dependency to “devDependencies”

\--optional

boolean

Add dependency to “optionalDependencies”

\--peer

boolean

Add dependency to “peerDependencies”

\--exact

boolean

Add the exact version instead of the ^range

### Lockfile Control

\--yarn

boolean

Write a yarn.lock file (yarn v1)

\--frozen-lockfile

boolean

Disallow changes to lockfile

\--save-text-lockfile

boolean

Save a text-based lockfile

\--lockfile-only

boolean

Generate a lockfile without installing dependencies

### Network & Registry Settings

\--ca

string

Provide a Certificate Authority signing certificate

\--cafile

string

File path to Certificate Authority signing certificate

\--registry

string

Use a specific registry by default, overriding .npmrc, bunfig.toml and environment variables

### Installation Process Control

\--dry-run

boolean

Don’t install anything

\--force

boolean

Always request the latest versions from the registry & reinstall all dependencies

\--global

boolean

Install globally

\--backend

string

default:"clonefile"

Platform-specific optimizations: “clonefile”, “hardlink”, “symlink”, “copyfile”

\--filter

string

Install packages for the matching workspaces

\--analyze

boolean

Analyze & install all dependencies of files passed as arguments recursively

### Caching Options

\--cache-dir

string

Store & load cached data from a specific directory path

\--no-cache

boolean

Ignore manifest cache entirely

### Output & Logging

\--silent

boolean

Don’t log anything

\--verbose

boolean

Excessively verbose logging

\--no-progress

boolean

Disable the progress bar

\--no-summary

boolean

Don’t print a summary

### Security & Integrity

\--no-verify

boolean

Skip verifying integrity of newly downloaded packages

\--trust

boolean

Add to trustedDependencies in the project’s package.json and install the package(s)

### Concurrency & Performance

\--concurrent-scripts

number

default:"5"

Maximum number of concurrent jobs for lifecycle scripts

\--network-concurrency

number

default:"48"

Maximum number of concurrent network requests

### Lifecycle Script Management

\--ignore-scripts

boolean

Skip lifecycle scripts in the project’s package.json (dependency scripts are never run)

### Help Information

\--help

boolean

Print this help menu
