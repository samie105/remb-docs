---
title: "dns/promises - Node documentation"
source: "https://docs.deno.com/api/node/dns/promises/"
canonical_url: "https://docs.deno.com/api/node/dns/promises/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:05:45.969Z"
content_hash: "fb1d608e67f69944050f9cc19ae41967c4ea9b9e7518860498faa88fdea3ad60"
menu_path: ["dns/promises - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/api/node/dns/index.md", "title": "dns - Node documentation"}
nav_next: {"path": "deno/api/node/domain/index.md", "title": "domain - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:dns/promises";
```

The `dns.promises` API provides an alternative set of asynchronous DNS methods that return `Promise` objects rather than using callbacks. The API is accessible via `import { promises as dnsPromises } from 'node:dns'` or `import dnsPromises from 'node:dns/promises'`.

c

[Resolver](../.././dns/promises/~/Resolver "Resolver")

An independent resolver for DNS requests.

-   [cancel](../.././dns/promises/~/Resolver#method_cancel_0)
-   [getServers](../.././dns/promises/~/Resolver#property_getservers)
-   [resolve](../.././dns/promises/~/Resolver#property_resolve)
-   [resolve4](../.././dns/promises/~/Resolver#property_resolve4)
-   [resolve6](../.././dns/promises/~/Resolver#property_resolve6)
-   [resolveAny](../.././dns/promises/~/Resolver#property_resolveany)
-   [resolveCaa](../.././dns/promises/~/Resolver#property_resolvecaa)
-   [resolveCname](../.././dns/promises/~/Resolver#property_resolvecname)
-   [resolveMx](../.././dns/promises/~/Resolver#property_resolvemx)
-   [resolveNaptr](../.././dns/promises/~/Resolver#property_resolvenaptr)
-   [resolveNs](../.././dns/promises/~/Resolver#property_resolvens)
-   [resolvePtr](../.././dns/promises/~/Resolver#property_resolveptr)
-   [resolveSoa](../.././dns/promises/~/Resolver#property_resolvesoa)
-   [resolveSrv](../.././dns/promises/~/Resolver#property_resolvesrv)
-   [resolveTxt](../.././dns/promises/~/Resolver#property_resolvetxt)
-   [reverse](../.././dns/promises/~/Resolver#property_reverse)
-   [setLocalAddress](../.././dns/promises/~/Resolver#method_setlocaladdress_0)
-   [setServers](../.././dns/promises/~/Resolver#property_setservers)

f

[getDefaultResultOrder](../.././dns/promises/~/getDefaultResultOrder "getDefaultResultOrder")

Get the default value for `verbatim` in [lookup](../.././dns/promises/~/lookup) and [dnsPromises.lookup()](https://nodejs.org/docs/latest-v20.x/api/dns.html#dnspromiseslookuphostname-options). The value could be:

f

[getServers](../.././dns/promises/~/getServers "getServers")

Returns an array of IP address strings, formatted according to [RFC 5952](https://tools.ietf.org/html/rfc5952#section-6), that are currently configured for DNS resolution. A string will include a port section if a custom port is used.

f

[lookup](../.././dns/promises/~/lookup "lookup")

Resolves a host name (e.g. `'nodejs.org'`) into the first found A (IPv4) or AAAA (IPv6) record. All `option` properties are optional. If `options` is an integer, then it must be `4` or `6` – if `options` is not provided, then IPv4 and IPv6 addresses are both returned if found.

f

[lookupService](../.././dns/promises/~/lookupService "lookupService")

Resolves the given `address` and `port` into a host name and service using the operating system's underlying `getnameinfo` implementation.

f

[resolve](../.././dns/promises/~/resolve "resolve")

Uses the DNS protocol to resolve a host name (e.g. `'nodejs.org'`) into an array of the resource records. When successful, the `Promise` is resolved with an array of resource records. The type and structure of individual results vary based on `rrtype`:

f

[resolve4](../.././dns/promises/~/resolve4 "resolve4")

Uses the DNS protocol to resolve IPv4 addresses (`A` records) for the `hostname`. On success, the `Promise` is resolved with an array of IPv4 addresses (e.g. `['74.125.79.104', '74.125.79.105', '74.125.79.106']`).

f

[resolve6](../.././dns/promises/~/resolve6 "resolve6")

Uses the DNS protocol to resolve IPv6 addresses (`AAAA` records) for the `hostname`. On success, the `Promise` is resolved with an array of IPv6 addresses.

f

[resolveAny](../.././dns/promises/~/resolveAny "resolveAny")

Uses the DNS protocol to resolve all records (also known as `ANY` or `*` query). On success, the `Promise` is resolved with an array containing various types of records. Each object has a property `type` that indicates the type of the current record. And depending on the `type`, additional properties will be present on the object:

f

[resolveCaa](../.././dns/promises/~/resolveCaa "resolveCaa")

Uses the DNS protocol to resolve `CAA` records for the `hostname`. On success, the `Promise` is resolved with an array of objects containing available certification authority authorization records available for the `hostname` (e.g. `[{critical: 0, iodef: 'mailto:pki@example.com'},{critical: 128, issue: 'pki.example.com'}]`).

f

[resolveCname](../.././dns/promises/~/resolveCname "resolveCname")

Uses the DNS protocol to resolve `CNAME` records for the `hostname`. On success, the `Promise` is resolved with an array of canonical name records available for the `hostname` (e.g. `['bar.example.com']`).

f

[resolveMx](../.././dns/promises/~/resolveMx "resolveMx")

Uses the DNS protocol to resolve mail exchange records (`MX` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects containing both a `priority` and `exchange` property (e.g.`[{priority: 10, exchange: 'mx.example.com'}, ...]`).

f

[resolveNaptr](../.././dns/promises/~/resolveNaptr "resolveNaptr")

Uses the DNS protocol to resolve regular expression-based records (`NAPTR` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects with the following properties:

f

[resolveNs](../.././dns/promises/~/resolveNs "resolveNs")

Uses the DNS protocol to resolve name server records (`NS` records) for the `hostname`. On success, the `Promise` is resolved with an array of name server records available for `hostname` (e.g.`['ns1.example.com', 'ns2.example.com']`).

f

[resolvePtr](../.././dns/promises/~/resolvePtr "resolvePtr")

Uses the DNS protocol to resolve pointer records (`PTR` records) for the `hostname`. On success, the `Promise` is resolved with an array of strings containing the reply records.

f

[resolveSoa](../.././dns/promises/~/resolveSoa "resolveSoa")

Uses the DNS protocol to resolve a start of authority record (`SOA` record) for the `hostname`. On success, the `Promise` is resolved with an object with the following properties:

f

[resolveSrv](../.././dns/promises/~/resolveSrv "resolveSrv")

Uses the DNS protocol to resolve service records (`SRV` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects with the following properties:

f

[resolveTxt](../.././dns/promises/~/resolveTxt "resolveTxt")

Uses the DNS protocol to resolve text queries (`TXT` records) for the `hostname`. On success, the `Promise` is resolved with a two-dimensional array of the text records available for `hostname` (e.g.`[ ['v=spf1 ip4:0.0.0.0 ', '~all' ] ]`). Each sub-array contains TXT chunks of one record. Depending on the use case, these could be either joined together or treated separately.

f

[reverse](../.././dns/promises/~/reverse "reverse")

Performs a reverse DNS query that resolves an IPv4 or IPv6 address to an array of host names.

f

[setDefaultResultOrder](../.././dns/promises/~/setDefaultResultOrder "setDefaultResultOrder")

Set the default value of `order` in `dns.lookup()` and `[lookup](../.././dns/promises/~/lookup)`. The value could be:

f

[setServers](../.././dns/promises/~/setServers "setServers")

Sets the IP address and port of servers to be used when performing DNS resolution. The `servers` argument is an array of [RFC 5952](https://tools.ietf.org/html/rfc5952#section-6) formatted addresses. If the port is the IANA default DNS port (53) it can be omitted.

v

[ADDRGETNETWORKPARAMS](../.././dns/promises/~/ADDRGETNETWORKPARAMS "ADDRGETNETWORKPARAMS")

No documentation available

v

[BADFAMILY](../.././dns/promises/~/BADFAMILY "BADFAMILY")

No documentation available

v

[BADFLAGS](../.././dns/promises/~/BADFLAGS "BADFLAGS")

No documentation available

v

[BADHINTS](../.././dns/promises/~/BADHINTS "BADHINTS")

No documentation available

v

[BADNAME](../.././dns/promises/~/BADNAME "BADNAME")

No documentation available

v

[BADQUERY](../.././dns/promises/~/BADQUERY "BADQUERY")

No documentation available

v

[BADRESP](../.././dns/promises/~/BADRESP "BADRESP")

No documentation available

v

[BADSTR](../.././dns/promises/~/BADSTR "BADSTR")

No documentation available

v

[CANCELLED](../.././dns/promises/~/CANCELLED "CANCELLED")

No documentation available

v

[CONNREFUSED](../.././dns/promises/~/CONNREFUSED "CONNREFUSED")

No documentation available

v

[DESTRUCTION](../.././dns/promises/~/DESTRUCTION "DESTRUCTION")

No documentation available

v

[EOF](../.././dns/promises/~/EOF "EOF")

No documentation available

v

[FILE](../.././dns/promises/~/FILE "FILE")

No documentation available

v

[FORMERR](../.././dns/promises/~/FORMERR "FORMERR")

No documentation available

v

[LOADIPHLPAPI](../.././dns/promises/~/LOADIPHLPAPI "LOADIPHLPAPI")

No documentation available

v

[NODATA](../.././dns/promises/~/NODATA "NODATA")

No documentation available

v

[NOMEM](../.././dns/promises/~/NOMEM "NOMEM")

No documentation available

v

[NONAME](../.././dns/promises/~/NONAME "NONAME")

No documentation available

v

[NOTFOUND](../.././dns/promises/~/NOTFOUND "NOTFOUND")

No documentation available

v

[NOTIMP](../.././dns/promises/~/NOTIMP "NOTIMP")

No documentation available

v

[NOTINITIALIZED](../.././dns/promises/~/NOTINITIALIZED "NOTINITIALIZED")

No documentation available

v

[REFUSED](../.././dns/promises/~/REFUSED "REFUSED")

No documentation available

v

[SERVFAIL](../.././dns/promises/~/SERVFAIL "SERVFAIL")

No documentation available

v

[TIMEOUT](../.././dns/promises/~/TIMEOUT "TIMEOUT")

No documentation available
