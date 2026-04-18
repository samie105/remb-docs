---
title: "Building Windows"
source: "https://bun.com/docs/project/building-windows"
canonical_url: "https://bun.com/docs/project/building-windows"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:15.422Z"
content_hash: "78379d01c8ce25a7441d6cb5da1a9f84f022f9d286606bb669423092473605bd"
menu_path: ["Building Windows"]
section_path: []
nav_prev: {"path": "bun/bun/docs/project/bindgen/index.md", "title": "Bindgen"}
nav_next: {"path": "bun/bun/docs/project/license/index.md", "title": "License"}
---

# scoop seems to be buggy if you install llvm and the rest at the same time
scoop install llvm@21.1.8
```

For Windows ARM64, download LLVM 21.1.8 directly from GitHub releases (first version with ARM64 Windows builds):

ARM64

```
# Download and install LLVM for ARM64
Invoke-WebRequest -Uri "https://github.com/llvm/llvm-project/releases/download/llvmorg-21.1.8/LLVM-21.1.8-woa64.exe" -OutFile "$env:TEMP\LLVM-21.1.8-woa64.exe"
Start-Process -FilePath "$env:TEMP\LLVM-21.1.8-woa64.exe" -ArgumentList "/S" -Wait
```

If you intend on building WebKit locally (optional, x64 only), you should install these packages:

Scoop

```
scoop install make cygwin python
```

From here on out, it is **expected you use a PowerShell Terminal with `.\scripts\vs-shell.ps1` sourced**. This script is available in the Bun repository and can be loaded by executing it:

```
.\scripts\vs-shell.ps1
```

To verify, you can check for an MSVC-only command line such as `mt.exe`

```
Get-Command mt
```

```
bun run build

# after the initial `bun run build` you can use the following to build
ninja -Cbuild/debug
```

If this was successful, you should have a `bun-debug.exe` in the `build/debug` folder.

```
.\build\debug\bun-debug.exe --revision
```

You should add this to `$Env:PATH`. The simplest way to do so is to open the start menu, type “Path”, and then navigate the environment variables menu to add `C:\.....\bun\build\debug` to the user environment variable `PATH`. You should then restart your editor (if it does not update still, log out and log back in).

*   WebKit is extracted to `build/debug/cache/webkit/`
*   Zig is extracted to `build/debug/cache/zig/bin/zig.exe`

## Tests

You can run the test suite either using `bun test <path>` or by using the wrapper script `bun node:test <path>`. The `bun node:test` command runs every test file in a separate instance of bun.exe, to prevent a crash in the test runner from stopping the entire suite.

```
# Setup
bun i --cwd packages\bun-internal-test

# Run the entire test suite with reporter
# the package.json script "test" uses "build/debug/bun-debug.exe" by default
bun run test

# Run an individual test file:
bun-debug test node\fs
bun-debug test "C:\bun\test\js\bun\resolve\import-meta.test.js"
```

## Troubleshooting

### .rc file fails to build

`llvm-rc.exe` is odd. don’t use it. use `rc.exe`, to do this make sure you are in a visual studio dev terminal, check `rc /?` to ensure it is `Microsoft Resource Compiler`

### failed to write output ‘bun-debug.exe’: permission denied

you cannot overwrite `bun-debug.exe` if it is already open. you likely have a running instance, maybe in the vscode debugger?
