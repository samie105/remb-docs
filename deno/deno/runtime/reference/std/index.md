---
title: "Deno Standard Library (@std)"
source: "https://docs.deno.com/runtime/reference/std/"
canonical_url: "https://docs.deno.com/runtime/reference/std/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:34.325Z"
content_hash: "95b9fd3744b7d739bfc407940edfb053d687ff5ef114408e02de9faff24e995c"
menu_path: ["Deno Standard Library (@std)"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/cli/x/index.md", "title": "deno x"}
nav_next: {"path": "deno/deno/runtime/reference/std/assert/index.md", "title": "Standard Assertions (@std/assert)"}
---

On this page

*   [Packages](#packages)

The Deno standard library is published as a set of modular JSR packages under the `@std` scope.

## Packages

*   [@std/assert](/runtime/reference/std/assert/) – Common assertion functions, especially useful for testing
*   [@std/async](/runtime/reference/std/async/) – Utilities for asynchronous operations, like delays, debouncing, or pooling
*   [@std/bytes](/runtime/reference/std/bytes/) – Utilities to manipulate Uint8Arrays that are not built-in to JavaScript
*   [@std/cache](/runtime/reference/std/cache/) – UNSTABLE: Cache utilities
*   [@std/cbor](/runtime/reference/std/cbor/) – UNSTABLE: Utilities for parsing and serializing Concise Binary Object Representation (CBOR)
*   [@std/cli](/runtime/reference/std/cli/) – Tools for creating interactive command line tools
*   [@std/collections](/runtime/reference/std/collections/) – Pure functions for common tasks related to collection types like arrays and objects
*   [@std/crypto](/runtime/reference/std/crypto/) – Extensions to the Web Crypto API
*   [@std/csv](/runtime/reference/std/csv/) – Reading and writing of comma-separated values (CSV) files
*   [@std/data-structures](/runtime/reference/std/data-structures/) – Common data structures like red-black trees and binary heaps
*   [@std/datetime](/runtime/reference/std/datetime/) – UNSTABLE: Utilities for dealing with Date objects
*   [@std/dotenv](/runtime/reference/std/dotenv/) – UNSTABLE: Parsing and loading environment variables from a `.env` file
*   [@std/encoding](/runtime/reference/std/encoding/) – Utilities for encoding and decoding common formats like hex, base64, and varint
*   [@std/expect](/runtime/reference/std/expect/) – Jest compatible `expect` assertion functions
*   [@std/fmt](/runtime/reference/std/fmt/) – Utilities for formatting values, such as adding colors to text, formatting durations, printf utils, formatting byte numbers.
*   [@std/front-matter](/runtime/reference/std/front-matter/) – Extract front matter from strings
*   [@std/fs](/runtime/reference/std/fs/) – Helpers for working with the file system
*   [@std/html](/runtime/reference/std/html/) – Functions for HTML, such as escaping or unescaping HTML entities
*   [@std/http](/runtime/reference/std/http/) – Utilities for building HTTP servers
*   [@std/ini](/runtime/reference/std/ini/) – UNSTABLE: Parsing and serializing of INI files
*   [@std/internal](/runtime/reference/std/internal/) – INTERNAL: The internal package for @std. Do not use this directly.
*   [@std/io](/runtime/reference/std/io/) – UNSTABLE: The utilities for advanced I/O operations using Reader and Writer interfaces.
*   [@std/json](/runtime/reference/std/json/) – (Streaming) parsing and serializing of JSON files
*   [@std/jsonc](/runtime/reference/std/jsonc/) – Parsing and serializing of JSONC files
*   [@std/log](/runtime/reference/std/log/) – UNSTABLE: A customizable logger framework
*   [@std/math](/runtime/reference/std/math/) – Basic math utilities
*   [@std/media-types](/runtime/reference/std/media-types/) – Utility functions for media types (MIME types)
*   [@std/msgpack](/runtime/reference/std/msgpack/) – Encoding and decoding for the msgpack format
*   [@std/net](/runtime/reference/std/net/) – Utilities for working with the network
*   [@std/path](/runtime/reference/std/path/) – Utilities for working with file system paths
*   [@std/random](/runtime/reference/std/random/) – UNSTABLE: Various utilities using random number generators. The package also provides seeded pseudo-random number generator.
*   [@std/regexp](/runtime/reference/std/regexp/) – Utilities for working with RegExp
*   [@std/semver](/runtime/reference/std/semver/) – Parsing and comparing of semantic versions (SemVer)
*   [@std/streams](/runtime/reference/std/streams/) – Utilities for working with the Web Streams API
*   [@std/tar](/runtime/reference/std/tar/) – UNSTABLE: Streaming utilities for working with tar archives.
*   [@std/testing](/runtime/reference/std/testing/) – Tools for testing Deno code like snapshot testing, bdd testing, and time mocking
*   [@std/text](/runtime/reference/std/text/) – Utilities for working with text
*   [@std/toml](/runtime/reference/std/toml/) – Parsing and serializing of TOML files
*   [@std/ulid](/runtime/reference/std/ulid/) – Generation of Universally Unique Lexicographically Sortable Identifiers (ULIDs)
*   [@std/uuid](/runtime/reference/std/uuid/) – Generators and validators for UUIDs
*   [@std/webgpu](/runtime/reference/std/webgpu/) – UNSTABLE: Utilities for working with the Web GPU API
*   [@std/xml](/runtime/reference/std/xml/) – XML parsing and serialization for Deno.
*   [@std/yaml](/runtime/reference/std/yaml/) – Parsing and serializing of YAML files

> This index and the individual package overview sections are generated. Add extra examples by creating files in `_overrides/<package>.md`.
