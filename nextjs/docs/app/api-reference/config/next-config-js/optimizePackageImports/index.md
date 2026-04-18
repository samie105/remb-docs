---
title: "optimizePackageImports"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:08:00.067Z"
content_hash: "76d7a9c90dcc0ba49aafc8e3e4cf82dae5fd3b7b789ef7546bf31fd9a8cf4ef9"
menu_path: ["optimizePackageImports"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/onDemandEntries/index.md", "title": "onDemandEntries"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/output/index.md", "title": "output"}
---

# optimizePackageImports

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 15, 2026

Some packages can export hundreds or thousands of modules, which can cause performance issues in development and production.

Adding a package to `experimental.optimizePackageImports` will only load the modules you are actually using, while still giving you the convenience of writing import statements with many named exports.

next.config.js

```
module.exports = {
  experimental: {
    optimizePackageImports: ['package-name'],
  },
}
```

The following libraries are optimized by default:

*   `lucide-react`
*   `date-fns`
*   `lodash-es`
*   `ramda`
*   `antd`
*   `react-bootstrap`
*   `ahooks`
*   `@ant-design/icons`
*   `@headlessui/react`
*   `@headlessui-float/react`
*   `@heroicons/react/20/solid`
*   `@heroicons/react/24/solid`
*   `@heroicons/react/24/outline`
*   `@visx/visx`
*   `@tremor/react`
*   `rxjs`
*   `@mui/material`
*   `@mui/icons-material`
*   `recharts`
*   `react-use`
*   `@material-ui/core`
*   `@material-ui/icons`
*   `@tabler/icons-react`
*   `mui-core`
*   `react-icons/*`
*   `effect`
*   `@effect/*`

[Previous

onDemandEntries

](/docs/app/api-reference/config/next-config-js/onDemandEntries)

[Next

output

](/docs/app/api-reference/config/next-config-js/output)

Was this helpful?

supported.

Send




