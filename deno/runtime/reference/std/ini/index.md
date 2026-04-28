---
title: "@std/ini"
source: "https://docs.deno.com/runtime/reference/std/ini/"
canonical_url: "https://docs.deno.com/runtime/reference/std/ini/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:43:38.514Z"
content_hash: "4a79ba1d0f066ffc32c8ffb0869c90f01ec1880c20df80fa65e8333e8f965cf1"
menu_path: ["@std/ini"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/std/http/index.md", "title": "@std/http"}
nav_next: {"path": "deno/runtime/reference/std/internal/index.md", "title": "@std/internal"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

Unstable

This @std package is experimental and its API may change without a major version bump.

## Overview

[`parse`](https://jsr.io/@std/ini@0.225.2/doc/~/parse) and [`stringify`](https://jsr.io/@std/ini@0.225.2/doc/~/stringify) for handling [INI](https://en.wikipedia.org/wiki/INI_file) encoded data, such as the [Desktop Entry specification](https://specifications.freedesktop.org/desktop-entry-spec/latest/ar01s03.html). Values are parsed as strings by default to preserve data parity from the original. Customization is possible in the form of reviver/replacer functions like those in `JSON.parse` and `JSON.stringify`. Nested sections, repeated key names within a section, and key/value arrays are not supported, but will be preserved when using [`IniMap`](https://jsr.io/@std/ini@0.225.2/doc/~/IniMap). Multi-line values are not supported and will throw a syntax error. White space padding and lines starting with '#', ';', or '//' will be treated as comments.

```js
import * as ini from "@std/ini";
import { assertEquals } from "@std/assert";

const iniFile = `# Example configuration file
Global Key=Some data here

[Section #1]
Section Value=42
Section Date=1977-05-25`;

const parsed = ini.parse(iniFile, {
  reviver(key, value, section) {
    if (section === "Section #1") {
      if (key === "Section Value") return Number(value);
      if (key === "Section Date") return new Date(value);
    }
    return value;
  },
});

assertEquals(parsed, {
  "Global Key": "Some data here",
  "Section #1": {
    "Section Value": 42,
    "Section Date": new Date("1977-05-25T00:00:00.000Z"),
  },
});

const text = ini.stringify(parsed, {
  replacer(key, value, section) {
    if (section === "Section #1" && key === "Section Date") {
      return (value as Date).toISOString().split("T")[0];
    }
    return value;
  },
});

assertEquals(text, `Global Key=Some data here
[Section #1]
Section Value=42
Section Date=1977-05-25`);
```

Optionally, [`IniMap`](https://jsr.io/@std/ini@0.225.2/doc/~/IniMap) may be used for finer INI handling. Using this class will permit preserving comments, accessing values like a map, iterating over key/value/section entries, and more.

```js
import { IniMap } from "@std/ini/ini-map";
import { assertEquals } from "@std/assert";

const ini = new IniMap();
ini.set("section1", "keyA", 100);
assertEquals(ini.toString(), `[section1]
keyA=100`);

ini.set('keyA', 25)
assertEquals(ini.toObject(), {
  keyA: 25,
  section1: {
    keyA: 100
  }
});
```

The reviver and replacer APIs can be used to extend the behavior of IniMap, such as adding support for duplicate keys as if they were arrays of values.

```js
import { IniMap } from "@std/ini/ini-map";
import { assertEquals } from "@std/assert";

const iniFile = `# Example of key/value arrays
[section1]
key1=This key
key1=is non-standard
key1=but can be captured!`;

const ini = new IniMap({ assignment: "=", deduplicate: true });
ini.parse(iniFile, (key, value, section) => {
  if (section) {
    if (ini.has(section, key)) {
      const exists = ini.get(section, key);
      if (Array.isArray(exists)) {
        exists.push(value);
        return exists;
      } else {
        return [exists, value];
      }
    }
  }
  return value;
});

assertEquals(
  ini.get("section1", "key1"),
  ["This key", "is non-standard", "but can be captured!"]
);

const result = ini.toString((key, value) => {
  if (Array.isArray(value)) {
    return value.join(
      `${ini.formatting.lineBreak}${key}${ini.formatting.assignment}`,
    );
  }
  return value;
});

assertEquals(result, iniFile);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/ini
```

[See all symbols in @std/ini on](https://jsr.io/@std/ini/doc)
