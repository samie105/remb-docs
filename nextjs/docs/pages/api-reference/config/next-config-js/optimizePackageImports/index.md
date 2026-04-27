---
title: "optimizePackageImports"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/optimizePackageImports"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/optimizePackageImports"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:20:25.482Z"
content_hash: "4f4621d96119fb85b5013027813054c386c3c8aa3cf7969dfaa09e435cb6f6f1"
menu_path: ["optimizePackageImports"]
section_path: []
version: "latest"
content_language: "en"
---
[Configuration](/docs/pages/api-reference/config)[next.config.js Options](/docs/pages/api-reference/config/next-config-js)optimizePackageImports

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
