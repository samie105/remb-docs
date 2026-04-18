---
title: "@std/data-structures"
source: "https://docs.deno.com/runtime/reference/std/data-structures/"
canonical_url: "https://docs.deno.com/runtime/reference/std/data-structures/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:17.683Z"
content_hash: "64e0ffa01824f7b78ddaf57be7f3c11325ae6e616e4bcf687875325e9d116d68"
menu_path: ["@std/data-structures"]
section_path: []
---
On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

Data structures for use in algorithms and other data manipulation.

```js
import { BinarySearchTree } from "@std/data-structures";
import { assertEquals } from "@std/assert";

const values = [3, 10, 13, 4, 6, 7, 1, 14];
const tree = new BinarySearchTree<number>();
values.forEach((value) => tree.insert(value));

assertEquals([...tree], [1, 3, 4, 6, 7, 10, 13, 14]);
assertEquals(tree.min(), 1);
assertEquals(tree.max(), 14);
assertEquals(tree.find(42), null);
assertEquals(tree.find(7), 7);
assertEquals(tree.remove(42), false);
assertEquals(tree.remove(7), true);
assertEquals([...tree], [1, 3, 4, 6, 10, 13, 14]);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/data-structures
```

[See all symbols in @std/data-structures on](https://jsr.io/@std/data-structures/doc)
