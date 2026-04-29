---
title: "Deno Standard Library (@std)"
source: "https://docs.deno.com/runtime/reference/std/"
canonical_url: "https://docs.deno.com/runtime/reference/std/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:38:19.549Z"
content_hash: "a93ede8b1c2f566e2e5aed577b338c83a10cf769de5dc35c07dd338ff3a62ddf"
menu_path: ["Deno Standard Library (@std)"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/cli/x/index.md", "title": "deno x"}
nav_next: {"path": "deno/runtime/reference/std/assert/index.md", "title": "Standard Assertions (@std/assert)"}
---

**On this page**

-   [Packages](#packages)

The Deno standard library is published as a set of modular JSR packages under the `@std` scope.

## Packages

-   [@std/assert](assert/index.md) – Common assertion functions, especially useful for testing
-   [@std/async](async/index.md) – Utilities for asynchronous operations, like delays, debouncing, or pooling
-   [@std/bytes](bytes/index.md) – Utilities to manipulate Uint8Arrays that are not built-in to JavaScript
-   [@std/cache](cache/index.md) – UNSTABLE: Cache utilities
-   [@std/cbor](cbor/index.md) – UNSTABLE: Utilities for parsing and serializing Concise Binary Object Representation (CBOR)
-   [@std/cli](cli/index.md) – Tools for creating interactive command line tools
-   [@std/collections](collections/index.md) – Pure functions for common tasks related to collection types like arrays and objects
-   [@std/crypto](crypto/index.md) – Extensions to the Web Crypto API
-   [@std/csv](csv/index.md) – Reading and writing of comma-separated values (CSV) files
-   [@std/data-structures](data-structures/index.md) – Common data structures like red-black trees and binary heaps
-   [@std/datetime](datetime/index.md) – UNSTABLE: Utilities for dealing with Date objects
-   [@std/dotenv](dotenv/index.md) – UNSTABLE: Parsing and loading environment variables from a `.env` file
-   [@std/encoding](encoding/index.md) – Utilities for encoding and decoding common formats like hex, base64, and varint
-   [@std/expect](expect/index.md) – Jest compatible `expect` assertion functions
-   [@std/fmt](fmt/index.md) – Utilities for formatting values, such as adding colors to text, formatting durations, printf utils, formatting byte numbers.
-   [@std/front-matter](front-matter/index.md) – Extract front matter from strings
-   [@std/fs](fs/index.md) – Helpers for working with the file system
-   [@std/html](html/index.md) – Functions for HTML, such as escaping or unescaping HTML entities
-   [@std/http](http/index.md) – Utilities for building HTTP servers
-   [@std/ini](ini/index.md) – UNSTABLE: Parsing and serializing of INI files
-   [@std/internal](internal/index.md) – INTERNAL: The internal package for @std. Do not use this directly.
-   [@std/io](io/index.md) – UNSTABLE: The utilities for advanced I/O operations using Reader and Writer interfaces.
-   [@std/json](json/index.md) – (Streaming) parsing and serializing of JSON files
-   [@std/jsonc](jsonc/index.md) – Parsing and serializing of JSONC files
-   [@std/log](log/index.md) – UNSTABLE: A customizable logger framework
-   [@std/math](math/index.md) – Basic math utilities
-   [@std/media-types](media-types/index.md) – Utility functions for media types (MIME types)
-   [@std/msgpack](msgpack/index.md) – Encoding and decoding for the msgpack format
-   [@std/net](net/index.md) – Utilities for working with the network
-   [@std/path](path/index.md) – Utilities for working with file system paths
-   [@std/random](random/index.md) – UNSTABLE: Various utilities using random number generators. The package also provides seeded pseudo-random number generator.
-   [@std/regexp](regexp/index.md) – Utilities for working with RegExp
-   [@std/semver](semver/index.md) – Parsing and comparing of semantic versions (SemVer)
-   [@std/streams](streams/index.md) – Utilities for working with the Web Streams API
-   [@std/tar](tar/index.md) – UNSTABLE: Streaming utilities for working with tar archives.
-   [@std/testing](testing/index.md) – Tools for testing Deno code like snapshot testing, bdd testing, and time mocking
-   [@std/text](text/index.md) – Utilities for working with text
-   [@std/toml](toml/index.md) – Parsing and serializing of TOML files
-   [@std/ulid](ulid/index.md) – Generation of Universally Unique Lexicographically Sortable Identifiers (ULIDs)
-   [@std/uuid](uuid/index.md) – Generators and validators for UUIDs
-   [@std/webgpu](webgpu/index.md) – UNSTABLE: Utilities for working with the Web GPU API
-   [@std/xml](xml/index.md) – XML parsing and serialization for Deno.
-   [@std/yaml](yaml/index.md) – Parsing and serializing of YAML files

> This index and the individual package overview sections are generated. Add extra examples by creating files in `_overrides/<package>.md`.
