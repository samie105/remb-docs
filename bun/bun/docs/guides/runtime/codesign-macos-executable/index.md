---
title: "Codesign a single-file JavaScript executable on macOS"
source: "https://bun.com/docs/guides/runtime/codesign-macos-executable"
canonical_url: "https://bun.com/docs/guides/runtime/codesign-macos-executable"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:19.746Z"
content_hash: "b49cee8f4c36c5e91469733e8c1804f0e11b280a16ad3f483fcccee6a09cc853"
menu_path: ["Codesign a single-file JavaScript executable on macOS"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/runtime/cicd/index.md", "title": "Install and run Bun in GitHub Actions"}
nav_next: {"path": "bun/bun/docs/guides/runtime/define-constant/index.md", "title": "Define and replace static globals & constants"}
---

Compile your executable using the `--compile` flag.

```
bun build --compile ./path/to/entry.ts --outfile myapp
```

* * *

List your available signing identities. One of these will be your signing identity that you pass to the `codesign` command. This command requires macOS.

terminal

```
security find-identity -v -p codesigning
```

```
1. XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX "Developer ID Application: Your Name (ZZZZZZZZZZ)"
   1 valid identities found
```

* * *

Optional, but recommended: create an `entitlements.plist` file with the necessary permissions for the JavaScript engine to work correctly.

entitlements.plist

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>com.apple.security.cs.allow-jit</key>
    <true/>
    <key>com.apple.security.cs.allow-unsigned-executable-memory</key>
    <true/>
    <key>com.apple.security.cs.disable-executable-page-protection</key>
    <true/>
    <key>com.apple.security.cs.allow-dyld-environment-variables</key>
    <true/>
    <key>com.apple.security.cs.disable-library-validation</key>
    <true/>
</dict>
</plist>
```

* * *

Sign your executable using the `codesign` command and verify it works.

terminal

```
codesign --entitlements entitlements.plist -vvvv --deep --sign "XXXXXXXXXX" ./myapp --force
codesign -vvv --verify ./myapp
```

* * *

For more information on macOS codesigning, refer to [Apple’s Code Signing documentation](https://developer.apple.com/documentation/security/code_signing_services). For details about creating single-file executables with Bun, see [Standalone Executables](bun/bun/docs/bundler/executables/index.md). This guide requires Bun v1.2.4 or newer.


