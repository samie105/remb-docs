---
title: "Loaders"
source: "https://bun.com/docs/bundler/loaders"
canonical_url: "https://bun.com/docs/bundler/loaders"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:48.946Z"
content_hash: "a353d9306d953609c0f40a19d751b12318ea89a8f3b39936f28d357245209e9a"
menu_path: ["Loaders"]
section_path: []
nav_prev: {"path": "../html-static/index.md", "title": "HTML & static sites"}
nav_next: {"path": "../minifier/index.md", "title": "Minifier"}
---

# Output: /path/to/project/logo.svg
```

In the bundler, things are slightly different. The file is copied into `outdir` as-is, and the import is resolved as a relative path pointing to the copied file.

```
// Output
var logo = "./logo.svg";
console.log(logo);
```

If a value is specified for `publicPath`, the import will use value as a prefix to construct an absolute path/URL.

Public path

Resolved import

`""` (default)

`/logo.svg`

`"/assets"`

`/assets/logo.svg`

`"https://cdn.example.com/"`

`https://cdn.example.com/logo.svg`
