---
title: "optimizePackageImports"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:06:49.522Z"
content_hash: "b782e8f9fd6137fada26a4d1c57e2751e28ae39ffd18fca0a047dd585665fedc"
menu_path: ["optimizePackageImports"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../onDemandEntries/index.md", "title": "onDemandEntries"}
nav_next: {"path": "../output/index.md", "title": "output"}
---

# optimizePackageImports

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 23, 2026

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

-   `lucide-react`
-   `date-fns`
-   `lodash-es`
-   `ramda`
-   `antd`
-   `react-bootstrap`
-   `ahooks`
-   `@ant-design/icons`
-   `@headlessui/react`
-   `@headlessui-float/react`
-   `@heroicons/react/20/solid`
-   `@heroicons/react/24/solid`
-   `@heroicons/react/24/outline`
-   `@visx/visx`
-   `@tremor/react`
-   `rxjs`
-   `@mui/material`
-   `@mui/icons-material`
-   `recharts`
-   `react-use`
-   `@material-ui/core`
-   `@material-ui/icons`
-   `@tabler/icons-react`
-   `mui-core`
-   `react-icons/*`
-   `effect`
-   `@effect/*`

Was this helpful?
