---
title: "Hash a password"
source: "https://bun.com/docs/guides/util/hash-a-password"
canonical_url: "https://bun.com/docs/guides/util/hash-a-password"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:57.904Z"
content_hash: "c4d21605c7ec05a627c2a0def15b49bcab332a1781f1bab748cc24a15bb80233"
menu_path: ["Hash a password"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/util/gzip/index.md", "title": "Compress and decompress data with gzip"}
nav_next: {"path": "bun/bun/docs/guides/util/import-meta-dir/index.md", "title": "Get the directory of the current file"}
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

The `Bun.password.hash()` function provides a fast, built-in mechanism for securely hashing passwords in Bun. No third-party dependencies are required.

```
const password = "super-secure-pa$$word";

const hash = await Bun.password.hash(password);
// => $argon2id$v=19$m=65536,t=2,p=1$tFq+9AVr1bfPxQdh6E8DQRhEXg/M/...
```

* * *

By default, this uses the [Argon2id](https://en.wikipedia.org/wiki/Argon2) algorithm. Pass a second argument to `Bun.password.hash()` to use a different algorithm or configure the hashing parameters.

```
const password = "super-secure-pa$$word";

// use argon2 (default)
const argonHash = await Bun.password.hash(password, {
  memoryCost: 4, // memory usage in kibibytes
  timeCost: 3, // the number of iterations
});
```

* * *

Bun also implements the [bcrypt](https://en.wikipedia.org/wiki/Bcrypt) algorithm. Specify `algorithm: "bcrypt"` to use it.

```
// use bcrypt
const bcryptHash = await Bun.password.hash(password, {
  algorithm: "bcrypt",
  cost: 4, // number between 4-31
});
```

* * *

Use `Bun.password.verify()` to verify a password. The algorithm and its parameters are stored in the hash itself, so re-specifying configuration is unnecessary.

```
const password = "super-secure-pa$$word";
const hash = await Bun.password.hash(password);

const isMatch = await Bun.password.verify(password, hash);
// => true
```

* * *

See [Docs > API > Hashing](/docs/runtime/hashing#bun-password) for complete documentation.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/hash-a-password.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/hash-a-password>)

[

Get the current Bun version

Previous

](/docs/guides/util/version)[

Generate a UUID

Next

](/docs/guides/util/javascript-uuid)

