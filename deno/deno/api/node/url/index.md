---
title: "url - Node documentation"
source: "https://docs.deno.com/api/node/url/"
canonical_url: "https://docs.deno.com/api/node/url/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:50.054Z"
content_hash: "a0e0ded3aa20b796498a150531b36646bbafbfdd3317b198a17861b36aea434b"
menu_path: ["url - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/tty/index.md", "title": "tty - Node documentation"}
nav_next: {"path": "deno/deno/api/node/util/index.md", "title": "util - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:url";
```

The `node:url` module provides utilities for URL resolution and parsing. It can be accessed using:

```js
import url from 'node:url';
```

### Classes [#](#Classes)

c

I

v

[URL](.././url/~/URL "URL")

Browser-compatible `URL` class, implemented by following the WHATWG URL Standard. [Examples of parsed URLs](https://url.spec.whatwg.org/#example-url-parsing) may be found in the Standard itself. The `URL` class is also available on the global object.

*   [canParse](.././url/~/URL#method_canparse_0)
*   [createObjectURL](.././url/~/URL#method_createobjecturl_0)
*   [hash](.././url/~/URL#property_hash)
*   [host](.././url/~/URL#property_host)
*   [hostname](.././url/~/URL#property_hostname)
*   [href](.././url/~/URL#property_href)
*   [origin](.././url/~/URL#property_origin)
*   [parse](.././url/~/URL#method_parse_0)
*   [password](.././url/~/URL#property_password)
*   [pathname](.././url/~/URL#property_pathname)
*   [port](.././url/~/URL#property_port)
*   [protocol](.././url/~/URL#property_protocol)
*   [revokeObjectURL](.././url/~/URL#method_revokeobjecturl_0)
*   [search](.././url/~/URL#property_search)
*   [searchParams](.././url/~/URL#property_searchparams)
*   [toJSON](.././url/~/URL#method_tojson_0)
*   [toString](.././url/~/URL#method_tostring_0)
*   [username](.././url/~/URL#property_username)

c

I

v

[URLSearchParams](.././url/~/URLSearchParams "URLSearchParams")

The `URLSearchParams` API provides read and write access to the query of a `URL`. The `URLSearchParams` class can also be used standalone with one of the four following constructors. The `URLSearchParams` class is also available on the global object.

*   [append](.././url/~/URLSearchParams#method_append_0)
*   [delete](.././url/~/URLSearchParams#method_delete_0)
*   [entries](.././url/~/URLSearchParams#method_entries_0)
*   [forEach](.././url/~/URLSearchParams#method_foreach_0)
*   [get](.././url/~/URLSearchParams#method_get_0)
*   [getAll](.././url/~/URLSearchParams#method_getall_0)
*   [has](.././url/~/URLSearchParams#method_has_0)
*   [keys](.././url/~/URLSearchParams#method_keys_0)
*   [set](.././url/~/URLSearchParams#method_set_0)
*   [size](.././url/~/URLSearchParams#property_size)
*   [sort](.././url/~/URLSearchParams#method_sort_0)
*   [toString](.././url/~/URLSearchParams#method_tostring_0)
*   [values](.././url/~/URLSearchParams#method_values_0)

### Functions [#](#Functions)

f

[domainToASCII](.././url/~/domainToASCII "domainToASCII")

Returns the [Punycode](https://tools.ietf.org/html/rfc5891#section-4.4) ASCII serialization of the `domain`. If `domain` is an invalid domain, the empty string is returned.

f

[domainToUnicode](.././url/~/domainToUnicode "domainToUnicode")

Returns the Unicode serialization of the `domain`. If `domain` is an invalid domain, the empty string is returned.

f

[fileURLToPath](.././url/~/fileURLToPath "fileURLToPath")

This function ensures the correct decodings of percent-encoded characters as well as ensuring a cross-platform valid absolute path string.

f

[format](.././url/~/format "format")

The `url.format()` method returns a formatted URL string derived from `urlObject`.

f

[parse](.././url/~/parse "parse")

No documentation available

f

[pathToFileURL](.././url/~/pathToFileURL "pathToFileURL")

This function ensures that `path` is resolved absolutely, and that the URL control characters are correctly encoded when converting into a File URL.

f

[resolve](.././url/~/resolve "resolve")

The `url.resolve()` method resolves a target URL relative to a base URL in a manner similar to that of a web browser resolving an anchor tag.

f

[urlToHttpOptions](.././url/~/urlToHttpOptions "urlToHttpOptions")

This utility function converts a URL object into an ordinary options object as expected by the `http.request()` and `https.request()` APIs.

### Interfaces [#](#Interfaces)

I

[FileUrlToPathOptions](.././url/~/FileUrlToPathOptions "FileUrlToPathOptions")

No documentation available

*   [windows](.././url/~/FileUrlToPathOptions#property_windows)

I

[Global](.././url/~/Global "Global")

No documentation available

*   [URL](.././url/~/Global#property_url)
*   [URLSearchParams](.././url/~/Global#property_urlsearchparams)

I

[PathToFileUrlOptions](.././url/~/PathToFileUrlOptions "PathToFileUrlOptions")

No documentation available

*   [windows](.././url/~/PathToFileUrlOptions#property_windows)

I

[Url](.././url/~/Url "Url")

No documentation available

*   [auth](.././url/~/Url#property_auth)
*   [hash](.././url/~/Url#property_hash)
*   [host](.././url/~/Url#property_host)
*   [hostname](.././url/~/Url#property_hostname)
*   [href](.././url/~/Url#property_href)
*   [path](.././url/~/Url#property_path)
*   [pathname](.././url/~/Url#property_pathname)
*   [port](.././url/~/Url#property_port)
*   [protocol](.././url/~/Url#property_protocol)
*   [query](.././url/~/Url#property_query)
*   [search](.././url/~/Url#property_search)
*   [slashes](.././url/~/Url#property_slashes)

I

[URLFormatOptions](.././url/~/URLFormatOptions "URLFormatOptions")

No documentation available

*   [auth](.././url/~/URLFormatOptions#property_auth)
*   [fragment](.././url/~/URLFormatOptions#property_fragment)
*   [search](.././url/~/URLFormatOptions#property_search)
*   [unicode](.././url/~/URLFormatOptions#property_unicode)

I

[UrlObject](.././url/~/UrlObject "UrlObject")

No documentation available

*   [auth](.././url/~/UrlObject#property_auth)
*   [hash](.././url/~/UrlObject#property_hash)
*   [host](.././url/~/UrlObject#property_host)
*   [hostname](.././url/~/UrlObject#property_hostname)
*   [href](.././url/~/UrlObject#property_href)
*   [pathname](.././url/~/UrlObject#property_pathname)
*   [port](.././url/~/UrlObject#property_port)
*   [protocol](.././url/~/UrlObject#property_protocol)
*   [query](.././url/~/UrlObject#property_query)
*   [search](.././url/~/UrlObject#property_search)
*   [slashes](.././url/~/UrlObject#property_slashes)

I

[URLSearchParamsIterator](.././url/~/URLSearchParamsIterator "URLSearchParamsIterator")

No documentation available

I

[UrlWithParsedQuery](.././url/~/UrlWithParsedQuery "UrlWithParsedQuery")

No documentation available

*   [query](.././url/~/UrlWithParsedQuery#property_query)

I

[UrlWithStringQuery](.././url/~/UrlWithStringQuery "UrlWithStringQuery")

No documentation available

*   [query](.././url/~/UrlWithStringQuery#property_query)

