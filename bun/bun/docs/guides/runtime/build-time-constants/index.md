---
title: "Build-time constants with --define"
source: "https://bun.com/docs/guides/runtime/build-time-constants"
canonical_url: "https://bun.com/docs/guides/runtime/build-time-constants"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:10.423Z"
content_hash: "0235f6d3221460b0b58ff15f7096c1dfd5c7526d88a72ffaee7a9e877b5c3ee8"
menu_path: ["Build-time constants with --define"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/read-file/watch/index.md", "title": "Watch a directory for changes"}
nav_next: {"path": "bun/bun/docs/guides/runtime/cicd/index.md", "title": "Install and run Bun in GitHub Actions"}
---

# Bundle with build-time constants
bun build --define BUILD_VERSION='"1.0.0"' --define NODE_ENV='"production"' src/index.ts --outdir ./dist
```

### With `bun build --compile`

terminal

```
# Compile to executable with build-time constants
bun build --compile --define BUILD_VERSION='"1.0.0"' --define BUILD_TIME='"2024-01-15T10:30:00Z"' src/cli.ts --outfile mycli
```

### JavaScript API

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)build.ts

```
await Bun.build({
  entrypoints: ["./src/index.ts"],
  outdir: "./dist",
  define: {
    BUILD_VERSION: '"1.0.0"',
    BUILD_TIME: '"2024-01-15T10:30:00Z"',
    DEBUG: "false",
  },
});
```

* * *

## Common use cases

### Version information

Embed version and build metadata directly into your executable:

### Feature flags

Use build-time constants to enable/disable features:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)src/version.ts

```
// Replaced at build time
declare const ENABLE_ANALYTICS: boolean;
declare const ENABLE_DEBUG: boolean;

function trackEvent(event: string) {
  if (ENABLE_ANALYTICS) {
    // This entire block is removed if ENABLE_ANALYTICS is false
    console.log("Tracking:", event);
  }
}

if (ENABLE_DEBUG) {
  console.log("Debug mode enabled");
}
```

```
# Production build - analytics enabled, debug disabled
bun build --compile --define ENABLE_ANALYTICS=true --define ENABLE_DEBUG=false src/app.ts --outfile app-prod

# Development build - both enabled
bun build --compile --define ENABLE_ANALYTICS=false --define ENABLE_DEBUG=true src/app.ts --outfile app-dev
```

### Configuration

Replace configuration objects at build time:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)src/version.ts

```
declare const CONFIG: {
  apiUrl: string;
  timeout: number;
  retries: number;
};

// CONFIG is replaced with the actual object at build time
const response = await fetch(CONFIG.apiUrl, {
  timeout: CONFIG.timeout,
});
```

```
bun build --compile --define 'CONFIG={"apiUrl":"https://api.example.com","timeout":5000,"retries":3}' src/app.ts --outfile app
```

* * *

## Advanced patterns

### Environment-specific builds

Create different executables for different environments:

```
{
  "scripts": {
    "build:dev": "bun build --compile --define NODE_ENV='\"development\"' --define API_URL='\"http://localhost:3000\"' src/app.ts --outfile app-dev",
    "build:staging": "bun build --compile --define NODE_ENV='\"staging\"' --define API_URL='\"https://staging.example.com\"' src/app.ts --outfile app-staging",
    "build:prod": "bun build --compile --define NODE_ENV='\"production\"' --define API_URL='\"https://api.example.com\"' src/app.ts --outfile app-prod"
  }
}
```

### Using shell commands for dynamic values

Generate build-time constants from shell commands:

```
# Use git to get current commit and timestamp
bun build --compile \
  --define BUILD_VERSION="\"$(git describe --tags --always)\"" \
  --define BUILD_TIME="\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"" \
  --define GIT_COMMIT="\"$(git rev-parse HEAD)\"" \
  src/cli.ts --outfile mycli
```

### Build automation script

Create a build script that automatically injects build metadata:

```
// build.ts
import { $ } from "bun";

const version = await $`git describe --tags --always`.text();
const buildTime = new Date().toISOString();
const gitCommit = await $`git rev-parse HEAD`.text();

await Bun.build({
  entrypoints: ["./src/cli.ts"],
  outdir: "./dist",
  define: {
    BUILD_VERSION: JSON.stringify(version.trim()),
    BUILD_TIME: JSON.stringify(buildTime),
    GIT_COMMIT: JSON.stringify(gitCommit.trim()),
  },
});

console.log(`Built with version ${version.trim()}`);
```

* * *

## Important considerations

### Value format

Values must be valid JSON that will be parsed and inlined as JavaScript expressions:

```
# ✅ Strings must be JSON-quoted
--define VERSION='"1.0.0"'

# ✅ Numbers are JSON literals
--define PORT=3000

# ✅ Booleans are JSON literals
--define DEBUG=true

# ✅ Objects and arrays (use single quotes to wrap the JSON)
--define 'CONFIG={"host":"localhost","port":3000}'

# ✅ Arrays work too
--define 'FEATURES=["auth","billing","analytics"]'

# ❌ This won't work - missing quotes around string
--define VERSION=1.0.0
```

### Property keys

You can use property access patterns as keys, not just simple identifiers:

```
# ✅ Replace process.env.NODE_ENV with "production"
--define 'process.env.NODE_ENV="production"'

# ✅ Replace process.env.API_KEY with the actual key
--define 'process.env.API_KEY="abc123"'

# ✅ Replace nested properties
--define 'window.myApp.version="1.0.0"'

# ✅ Replace array access
--define 'process.argv[2]="--production"'
```

This is particularly useful for environment variables:

```
// Before compilation
if (process.env.NODE_ENV === "production") {
  console.log("Production mode");
}

// After compilation with --define 'process.env.NODE_ENV="production"'
if ("production" === "production") {
  console.log("Production mode");
}

// After optimization
console.log("Production mode");
```

### TypeScript declarations

For TypeScript projects, declare your constants to avoid type errors:

```
// types/build-constants.d.ts
declare const BUILD_VERSION: string;
declare const BUILD_TIME: string;
declare const NODE_ENV: "development" | "staging" | "production";
declare const DEBUG: boolean;
```

### Cross-platform compatibility

When building for multiple platforms, constants work the same way:

```
# Linux
bun build --compile --target=bun-linux-x64 --define PLATFORM='"linux"' src/app.ts --outfile app-linux

# macOS
bun build --compile --target=bun-darwin-x64 --define PLATFORM='"darwin"' src/app.ts --outfile app-macos

# Windows
bun build --compile --target=bun-windows-x64 --define PLATFORM='"windows"' src/app.ts --outfile app-windows.exe
```

* * *

*   [Define constants at runtime](bun/bun/docs/guides/runtime/define-constant/index.md) - Using `--define` with `bun run`
*   [Building executables](bun/bun/docs/bundler/executables/index.md) - Complete guide to `bun build --compile`
*   [Bundler API](bun/bun/docs/bundler/index.md) - Full bundler documentation including `define` option
