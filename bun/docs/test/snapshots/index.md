---
title: "Snapshots"
source: "https://bun.com/docs/test/snapshots"
canonical_url: "https://bun.com/docs/test/snapshots"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:44.726Z"
content_hash: "3093a88470ac8756efc2c3e8f3f0286246a025dc1cae2081e189305336e4b9c4"
menu_path: ["Snapshots"]
section_path: []
nav_prev: {"path": "bun/docs/test/runtime-behavior/index.md", "title": "Runtime behavior"}
nav_next: {"path": "bun/docs/test/writing-tests/index.md", "title": "Writing tests"}
---

# See what changed
git diff __snapshots__/

# Update if changes are intentional
bun test --update-snapshots

# Commit the updated snapshots
git add __snapshots__/
git commit -m "Update snapshots after UI changes"
```

### Cleaning Up Unused Snapshots

Bun will warn about unused snapshots:

warning

```
Warning: 1 unused snapshot found:
  my-test.test.ts.snap: "old test that no longer exists 1"
```

Remove unused snapshots by deleting them from the snapshot files or by running tests with cleanup flags if available.

### Organizing Large Snapshot Files

For large projects, consider organizing tests to keep snapshot files manageable:

directory structure

```
tests/
├── components/
│   ├── Button.test.tsx
│   └── __snapshots__/
│       └── Button.test.tsx.snap
├── utils/
│   ├── formatters.test.ts
│   └── __snapshots__/
│       └── formatters.test.ts.snap
```

## Troubleshooting

### Snapshot Failures

When snapshots fail, you’ll see a diff:

diff

```
- Expected
+ Received

  Object {
-   "name": "John",
+   "name": "Jane",
  }
```

Common causes:

*   Intentional changes (update with `--update-snapshots`)
*   Unintentional changes (fix the code)
*   Dynamic data (use property matchers)
*   Environment differences (normalize the data)

### Platform Differences

Be aware of platform-specific differences:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
// Paths might differ between Windows/Unix
test("file operations", () => {
  const result = processFile("./test.txt");

  expect({
    ...result,
    path: result.path.replace(/\\/g, "/"), // Normalize paths
  }).toMatchSnapshot();
});
```
