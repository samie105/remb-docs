---
title: "trailingSlash"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/trailingSlash"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/trailingSlash"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:08:44.431Z"
content_hash: "16df31d186a51774ecf0657ddfc26530bbb9c801735e8dfed769347b0e73e266"
menu_path: ["trailingSlash"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/taint/index.md", "title": "taint"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/transpilePackages/index.md", "title": "transpilePackages"}
---

# trailingSlash

Last updated April 15, 2026

By default Next.js will redirect URLs with trailing slashes to their counterpart without a trailing slash. For example `/about/` will redirect to `/about`. You can configure this behavior to act the opposite way, where URLs without trailing slashes are redirected to their counterparts with trailing slashes.

Open `next.config.js` and add the `trailingSlash` config:

next.config.js

```
module.exports = {
  trailingSlash: true,
}
```

With this option set, URLs like `/about` will redirect to `/about/`.

When using `trailingSlash: true`, certain URLs are exceptions and will not have a trailing slash appended:

*   Static file URLs, such as files with extensions.
*   Any paths under `.well-known/`.

For example, the following URLs will remain unchanged: `/file.txt`, `images/photos/picture.png`, and `.well-known/subfolder/config.json`.

When used with [`output: "export"`](/docs/app/guides/static-exports) configuration, the `/about` page will output `/about/index.html` (instead of the default `/about.html`).

## Version History[](#version-history)

Version

Changes

`v9.5.0`

`trailingSlash` added.

[Previous

taint

](/docs/app/api-reference/config/next-config-js/taint)

[Next

transpilePackages

](/docs/app/api-reference/config/next-config-js/transpilePackages)

Was this helpful?

supported.

Send
