---
title: "punycode - Node documentation"
source: "https://docs.deno.com/api/node/punycode/"
canonical_url: "https://docs.deno.com/api/node/punycode/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:02.008Z"
content_hash: "24cbc4d5e906238c83ea84d87cef4afb345bb04d4787193244e811904b9a0d51"
menu_path: ["punycode - Node documentation"]
section_path: []
---
### Usage in Deno

```typescript
import * as mod from "node:punycode";
```

Deprecated

\*\*The version of the punycode module bundled in Node.js is being deprecated. \*\*In a future major version of Node.js this module will be removed. Users currently depending on the `punycode` module should switch to using the userland-provided [Punycode.js](https://github.com/bestiejs/punycode.js) module instead. For punycode-based URL encoding, see `url.domainToASCII` or, more generally, the `WHATWG URL API`.

The `punycode` module is a bundled version of the [Punycode.js](https://github.com/bestiejs/punycode.js) module. It can be accessed using:

```js
import punycode from 'node:punycode';
```

[Punycode](https://tools.ietf.org/html/rfc3492) is a character encoding scheme defined by RFC 3492 that is primarily intended for use in Internationalized Domain Names. Because host names in URLs are limited to ASCII characters only, Domain Names that contain non-ASCII characters must be converted into ASCII using the Punycode scheme. For instance, the Japanese character that translates into the English word, `'example'` is `'例'`. The Internationalized Domain Name, `'例.com'` (equivalent to `'example.com'`) is represented by Punycode as the ASCII string `'xn--fsq.com'`.

The `punycode` module provides a simple implementation of the Punycode standard.

The `punycode` module is a third-party dependency used by Node.js and made available to developers as a convenience. Fixes or other modifications to the module must be directed to the [Punycode.js](https://github.com/bestiejs/punycode.js) project.

### Functions [#](#Functions)

f

[decode](.././punycode/~/decode "decode")

The `punycode.decode()` method converts a [Punycode](https://tools.ietf.org/html/rfc3492) string of ASCII-only characters to the equivalent string of Unicode codepoints.

f

[encode](.././punycode/~/encode "encode")

The `punycode.encode()` method converts a string of Unicode codepoints to a [Punycode](https://tools.ietf.org/html/rfc3492) string of ASCII-only characters.

f

[toASCII](.././punycode/~/toASCII "toASCII")

The `punycode.toASCII()` method converts a Unicode string representing an Internationalized Domain Name to [Punycode](https://tools.ietf.org/html/rfc3492). Only the non-ASCII parts of the domain name will be converted. Calling `punycode.toASCII()` on a string that already only contains ASCII characters will have no effect.

f

[toUnicode](.././punycode/~/toUnicode "toUnicode")

The `punycode.toUnicode()` method converts a string representing a domain name containing [Punycode](https://tools.ietf.org/html/rfc3492) encoded characters into Unicode. Only the [Punycode](https://tools.ietf.org/html/rfc3492) encoded parts of the domain name are be converted.

### Variables [#](#Variables)

I

v

[ucs2](.././punycode/~/ucs2 "ucs2")

No documentation available

*   [decode](.././punycode/~/ucs2#method_decode_0)
*   [encode](.././punycode/~/ucs2#method_encode_0)

v

[version](.././punycode/~/version "version")

No documentation available
