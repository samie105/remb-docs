---
title: "dns - Node documentation"
source: "https://docs.deno.com/api/node/dns/"
canonical_url: "https://docs.deno.com/api/node/dns/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:05:38.408Z"
content_hash: "ce2611b8b5fefae0bb51b042a25375f4bb94157ca72f81ed3f3fe344550635be"
menu_path: ["dns - Node documentation"]
section_path: []
content_language: "en"
---
### Usage in Deno

```typescript
import * as mod from "node:dns";
```

The `node:dns` module enables name resolution. For example, use it to look up IP addresses of host names.

Although named for the [Domain Name System (DNS)](https://en.wikipedia.org/wiki/Domain_Name_System), it does not always use the DNS protocol for lookups. [lookup](.././dns/~/lookup) uses the operating system facilities to perform name resolution. It may not need to perform any network communication. To perform name resolution the way other applications on the same system do, use [lookup](.././dns/~/lookup).

```js
import dns from 'node:dns';

dns.lookup('example.org', (err, address, family) => {
  console.log('address: %j family: IPv%s', address, family);
});
// address: "93.184.216.34" family: IPv4
```

All other functions in the `node:dns` module connect to an actual DNS server to perform name resolution. They will always use the network to perform DNS queries. These functions do not use the same set of configuration files used by [lookup](.././dns/~/lookup) (e.g. `/etc/hosts`). Use these functions to always perform DNS queries, bypassing other name-resolution facilities.

```js
import dns from 'node:dns';

dns.resolve4('archive.org', (err, addresses) => {
  if (err) throw err;

  console.log(`addresses: ${JSON.stringify(addresses)}`);

  addresses.forEach((a) => {
    dns.reverse(a, (err, hostnames) => {
      if (err) {
        throw err;
      }
      console.log(`reverse for ${a}: ${JSON.stringify(hostnames)}`);
    });
  });
});
```

See the [Implementation considerations section](https://nodejs.org/docs/latest-v22.x/api/dns.html#implementation-considerations) for more information.

c

[promises.Resolver](.././dns/promises/~/promises.Resolver "promises.Resolver")

An independent resolver for DNS requests.

-   [cancel](.././dns/promises/~/promises.Resolver#method_cancel_0)
-   [getServers](.././dns/promises/~/promises.Resolver#property_getservers)
-   [resolve](.././dns/promises/~/promises.Resolver#property_resolve)
-   [resolve4](.././dns/promises/~/promises.Resolver#property_resolve4)
-   [resolve6](.././dns/promises/~/promises.Resolver#property_resolve6)
-   [resolveAny](.././dns/promises/~/promises.Resolver#property_resolveany)
-   [resolveCaa](.././dns/promises/~/promises.Resolver#property_resolvecaa)
-   [resolveCname](.././dns/promises/~/promises.Resolver#property_resolvecname)
-   [resolveMx](.././dns/promises/~/promises.Resolver#property_resolvemx)
-   [resolveNaptr](.././dns/promises/~/promises.Resolver#property_resolvenaptr)
-   [resolveNs](.././dns/promises/~/promises.Resolver#property_resolvens)
-   [resolvePtr](.././dns/promises/~/promises.Resolver#property_resolveptr)
-   [resolveSoa](.././dns/promises/~/promises.Resolver#property_resolvesoa)
-   [resolveSrv](.././dns/promises/~/promises.Resolver#property_resolvesrv)
-   [resolveTxt](.././dns/promises/~/promises.Resolver#property_resolvetxt)
-   [reverse](.././dns/promises/~/promises.Resolver#property_reverse)
-   [setLocalAddress](.././dns/promises/~/promises.Resolver#method_setlocaladdress_0)
-   [setServers](.././dns/promises/~/promises.Resolver#property_setservers)

c

[Resolver](.././dns/~/Resolver "Resolver")

An independent resolver for DNS requests.

-   [cancel](.././dns/~/Resolver#method_cancel_0)
-   [getServers](.././dns/~/Resolver#property_getservers)
-   [resolve](.././dns/~/Resolver#property_resolve)
-   [resolve4](.././dns/~/Resolver#property_resolve4)
-   [resolve6](.././dns/~/Resolver#property_resolve6)
-   [resolveAny](.././dns/~/Resolver#property_resolveany)
-   [resolveCaa](.././dns/~/Resolver#property_resolvecaa)
-   [resolveCname](.././dns/~/Resolver#property_resolvecname)
-   [resolveMx](.././dns/~/Resolver#property_resolvemx)
-   [resolveNaptr](.././dns/~/Resolver#property_resolvenaptr)
-   [resolveNs](.././dns/~/Resolver#property_resolvens)
-   [resolvePtr](.././dns/~/Resolver#property_resolveptr)
-   [resolveSoa](.././dns/~/Resolver#property_resolvesoa)
-   [resolveSrv](.././dns/~/Resolver#property_resolvesrv)
-   [resolveTxt](.././dns/~/Resolver#property_resolvetxt)
-   [reverse](.././dns/~/Resolver#property_reverse)
-   [setLocalAddress](.././dns/~/Resolver#method_setlocaladdress_0)
-   [setServers](.././dns/~/Resolver#property_setservers)

f

[getDefaultResultOrder](.././dns/~/getDefaultResultOrder "getDefaultResultOrder")

Get the default value for `order` in [lookup](.././dns/~/lookup) and [`dnsPromises.lookup()`](https://nodejs.org/docs/latest-v22.x/api/dns.html#dnspromiseslookuphostname-options). The value could be:

f

[getServers](.././dns/~/getServers "getServers")

Returns an array of IP address strings, formatted according to [RFC 5952](https://tools.ietf.org/html/rfc5952#section-6), that are currently configured for DNS resolution. A string will include a port section if a custom port is used.

f

[lookup](.././dns/~/lookup "lookup")

Resolves a host name (e.g. `'nodejs.org'`) into the first found A (IPv4) or AAAA (IPv6) record. All `option` properties are optional. If `options` is an integer, then it must be `4` or `6` – if `options` is `0` or not provided, then IPv4 and IPv6 addresses are both returned if found.

f

[lookupService](.././dns/~/lookupService "lookupService")

Resolves the given `address` and `port` into a host name and service using the operating system's underlying `getnameinfo` implementation.

f

[promises.getDefaultResultOrder](.././dns/promises/~/promises.getDefaultResultOrder "promises.getDefaultResultOrder")

Get the default value for `verbatim` in [lookup](.././dns/~/lookup) and [dnsPromises.lookup()](https://nodejs.org/docs/latest-v20.x/api/dns.html#dnspromiseslookuphostname-options). The value could be:

f

[promises.getServers](.././dns/promises/~/promises.getServers "promises.getServers")

Returns an array of IP address strings, formatted according to [RFC 5952](https://tools.ietf.org/html/rfc5952#section-6), that are currently configured for DNS resolution. A string will include a port section if a custom port is used.

f

[promises.lookup](.././dns/promises/~/promises.lookup "promises.lookup")

Resolves a host name (e.g. `'nodejs.org'`) into the first found A (IPv4) or AAAA (IPv6) record. All `option` properties are optional. If `options` is an integer, then it must be `4` or `6` – if `options` is not provided, then IPv4 and IPv6 addresses are both returned if found.

f

[promises.lookupService](.././dns/promises/~/promises.lookupService "promises.lookupService")

Resolves the given `address` and `port` into a host name and service using the operating system's underlying `getnameinfo` implementation.

f

[promises.resolve](.././dns/promises/~/promises.resolve "promises.resolve")

Uses the DNS protocol to resolve a host name (e.g. `'nodejs.org'`) into an array of the resource records. When successful, the `Promise` is resolved with an array of resource records. The type and structure of individual results vary based on `rrtype`:

f

[promises.resolve4](.././dns/promises/~/promises.resolve4 "promises.resolve4")

Uses the DNS protocol to resolve IPv4 addresses (`A` records) for the `hostname`. On success, the `Promise` is resolved with an array of IPv4 addresses (e.g. `['74.125.79.104', '74.125.79.105', '74.125.79.106']`).

f

[promises.resolve6](.././dns/promises/~/promises.resolve6 "promises.resolve6")

Uses the DNS protocol to resolve IPv6 addresses (`AAAA` records) for the `hostname`. On success, the `Promise` is resolved with an array of IPv6 addresses.

f

[promises.resolveAny](.././dns/promises/~/promises.resolveAny "promises.resolveAny")

Uses the DNS protocol to resolve all records (also known as `ANY` or `*` query). On success, the `Promise` is resolved with an array containing various types of records. Each object has a property `type` that indicates the type of the current record. And depending on the `type`, additional properties will be present on the object:

f

[promises.resolveCaa](.././dns/promises/~/promises.resolveCaa "promises.resolveCaa")

Uses the DNS protocol to resolve `CAA` records for the `hostname`. On success, the `Promise` is resolved with an array of objects containing available certification authority authorization records available for the `hostname` (e.g. `[{critical: 0, iodef: 'mailto:pki@example.com'},{critical: 128, issue: 'pki.example.com'}]`).

f

[promises.resolveCname](.././dns/promises/~/promises.resolveCname "promises.resolveCname")

Uses the DNS protocol to resolve `CNAME` records for the `hostname`. On success, the `Promise` is resolved with an array of canonical name records available for the `hostname` (e.g. `['bar.example.com']`).

f

[promises.resolveMx](.././dns/promises/~/promises.resolveMx "promises.resolveMx")

Uses the DNS protocol to resolve mail exchange records (`MX` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects containing both a `priority` and `exchange` property (e.g.`[{priority: 10, exchange: 'mx.example.com'}, ...]`).

f

[promises.resolveNaptr](.././dns/promises/~/promises.resolveNaptr "promises.resolveNaptr")

Uses the DNS protocol to resolve regular expression-based records (`NAPTR` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects with the following properties:

f

[promises.resolveNs](.././dns/promises/~/promises.resolveNs "promises.resolveNs")

Uses the DNS protocol to resolve name server records (`NS` records) for the `hostname`. On success, the `Promise` is resolved with an array of name server records available for `hostname` (e.g.`['ns1.example.com', 'ns2.example.com']`).

f

[promises.resolvePtr](.././dns/promises/~/promises.resolvePtr "promises.resolvePtr")

Uses the DNS protocol to resolve pointer records (`PTR` records) for the `hostname`. On success, the `Promise` is resolved with an array of strings containing the reply records.

f

[promises.resolveSoa](.././dns/promises/~/promises.resolveSoa "promises.resolveSoa")

Uses the DNS protocol to resolve a start of authority record (`SOA` record) for the `hostname`. On success, the `Promise` is resolved with an object with the following properties:

f

[promises.resolveSrv](.././dns/promises/~/promises.resolveSrv "promises.resolveSrv")

Uses the DNS protocol to resolve service records (`SRV` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects with the following properties:

f

[promises.resolveTxt](.././dns/promises/~/promises.resolveTxt "promises.resolveTxt")

Uses the DNS protocol to resolve text queries (`TXT` records) for the `hostname`. On success, the `Promise` is resolved with a two-dimensional array of the text records available for `hostname` (e.g.`[ ['v=spf1 ip4:0.0.0.0 ', '~all' ] ]`). Each sub-array contains TXT chunks of one record. Depending on the use case, these could be either joined together or treated separately.

f

[promises.reverse](.././dns/promises/~/promises.reverse "promises.reverse")

Performs a reverse DNS query that resolves an IPv4 or IPv6 address to an array of host names.

f

[promises.setDefaultResultOrder](.././dns/promises/~/promises.setDefaultResultOrder "promises.setDefaultResultOrder")

Set the default value of `order` in `dns.lookup()` and `[lookup](.././dns/~/lookup)`. The value could be:

f

[promises.setServers](.././dns/promises/~/promises.setServers "promises.setServers")

Sets the IP address and port of servers to be used when performing DNS resolution. The `servers` argument is an array of [RFC 5952](https://tools.ietf.org/html/rfc5952#section-6) formatted addresses. If the port is the IANA default DNS port (53) it can be omitted.

f

[resolve](.././dns/~/resolve "resolve")

No documentation available

f

[resolve4](.././dns/~/resolve4 "resolve4")

No documentation available

f

[resolve6](.././dns/~/resolve6 "resolve6")

No documentation available

f

[resolveAny](.././dns/~/resolveAny "resolveAny")

No documentation available

f

[resolveCaa](.././dns/~/resolveCaa "resolveCaa")

No documentation available

f

[resolveCname](.././dns/~/resolveCname "resolveCname")

No documentation available

f

[resolveMx](.././dns/~/resolveMx "resolveMx")

No documentation available

f

[resolveNaptr](.././dns/~/resolveNaptr "resolveNaptr")

No documentation available

f

[resolveNs](.././dns/~/resolveNs "resolveNs")

No documentation available

f

[resolvePtr](.././dns/~/resolvePtr "resolvePtr")

No documentation available

f

[resolveSoa](.././dns/~/resolveSoa "resolveSoa")

No documentation available

f

[resolveSrv](.././dns/~/resolveSrv "resolveSrv")

No documentation available

f

[resolveTxt](.././dns/~/resolveTxt "resolveTxt")

No documentation available

f

[reverse](.././dns/~/reverse "reverse")

Performs a reverse DNS query that resolves an IPv4 or IPv6 address to an array of host names.

f

[setDefaultResultOrder](.././dns/~/setDefaultResultOrder "setDefaultResultOrder")

Set the default value of `order` in [lookup](.././dns/~/lookup) and [`dnsPromises.lookup()`](https://nodejs.org/docs/latest-v22.x/api/dns.html#dnspromiseslookuphostname-options). The value could be:

f

[setServers](.././dns/~/setServers "setServers")

Sets the IP address and port of servers to be used when performing DNS resolution. The `servers` argument is an array of [RFC 5952](https://tools.ietf.org/html/rfc5952#section-6) formatted addresses. If the port is the IANA default DNS port (53) it can be omitted.

I

[AnyAaaaRecord](.././dns/~/AnyAaaaRecord "AnyAaaaRecord")

No documentation available

-   [type](.././dns/~/AnyAaaaRecord#property_type)

I

[AnyARecord](.././dns/~/AnyARecord "AnyARecord")

No documentation available

-   [type](.././dns/~/AnyARecord#property_type)

I

[AnyCnameRecord](.././dns/~/AnyCnameRecord "AnyCnameRecord")

No documentation available

-   [type](.././dns/~/AnyCnameRecord#property_type)
-   [value](.././dns/~/AnyCnameRecord#property_value)

I

[AnyMxRecord](.././dns/~/AnyMxRecord "AnyMxRecord")

No documentation available

-   [type](.././dns/~/AnyMxRecord#property_type)

I

[AnyNaptrRecord](.././dns/~/AnyNaptrRecord "AnyNaptrRecord")

No documentation available

-   [type](.././dns/~/AnyNaptrRecord#property_type)

I

[AnyNsRecord](.././dns/~/AnyNsRecord "AnyNsRecord")

No documentation available

-   [type](.././dns/~/AnyNsRecord#property_type)
-   [value](.././dns/~/AnyNsRecord#property_value)

I

[AnyPtrRecord](.././dns/~/AnyPtrRecord "AnyPtrRecord")

No documentation available

-   [type](.././dns/~/AnyPtrRecord#property_type)
-   [value](.././dns/~/AnyPtrRecord#property_value)

I

[AnySoaRecord](.././dns/~/AnySoaRecord "AnySoaRecord")

No documentation available

-   [type](.././dns/~/AnySoaRecord#property_type)

I

[AnySrvRecord](.././dns/~/AnySrvRecord "AnySrvRecord")

No documentation available

-   [type](.././dns/~/AnySrvRecord#property_type)

I

[AnyTxtRecord](.././dns/~/AnyTxtRecord "AnyTxtRecord")

No documentation available

-   [entries](.././dns/~/AnyTxtRecord#property_entries)
-   [type](.././dns/~/AnyTxtRecord#property_type)

I

[CaaRecord](.././dns/~/CaaRecord "CaaRecord")

No documentation available

-   [contactemail](.././dns/~/CaaRecord#property_contactemail)
-   [contactphone](.././dns/~/CaaRecord#property_contactphone)
-   [critical](.././dns/~/CaaRecord#property_critical)
-   [iodef](.././dns/~/CaaRecord#property_iodef)
-   [issue](.././dns/~/CaaRecord#property_issue)
-   [issuewild](.././dns/~/CaaRecord#property_issuewild)

I

[LookupAddress](.././dns/~/LookupAddress "LookupAddress")

No documentation available

-   [address](.././dns/~/LookupAddress#property_address)
-   [family](.././dns/~/LookupAddress#property_family)

I

[LookupAllOptions](.././dns/~/LookupAllOptions "LookupAllOptions")

No documentation available

-   [all](.././dns/~/LookupAllOptions#property_all)

I

[LookupOneOptions](.././dns/~/LookupOneOptions "LookupOneOptions")

No documentation available

-   [all](.././dns/~/LookupOneOptions#property_all)

I

[LookupOptions](.././dns/~/LookupOptions "LookupOptions")

No documentation available

-   [all](.././dns/~/LookupOptions#property_all)
-   [family](.././dns/~/LookupOptions#property_family)
-   [hints](.././dns/~/LookupOptions#property_hints)
-   [order](.././dns/~/LookupOptions#property_order)
-   [verbatim](.././dns/~/LookupOptions#property_verbatim)

I

[MxRecord](.././dns/~/MxRecord "MxRecord")

No documentation available

-   [exchange](.././dns/~/MxRecord#property_exchange)
-   [priority](.././dns/~/MxRecord#property_priority)

I

[NaptrRecord](.././dns/~/NaptrRecord "NaptrRecord")

No documentation available

-   [flags](.././dns/~/NaptrRecord#property_flags)
-   [order](.././dns/~/NaptrRecord#property_order)
-   [preference](.././dns/~/NaptrRecord#property_preference)
-   [regexp](.././dns/~/NaptrRecord#property_regexp)
-   [replacement](.././dns/~/NaptrRecord#property_replacement)
-   [service](.././dns/~/NaptrRecord#property_service)

I

[RecordWithTtl](.././dns/~/RecordWithTtl "RecordWithTtl")

No documentation available

-   [address](.././dns/~/RecordWithTtl#property_address)
-   [ttl](.././dns/~/RecordWithTtl#property_ttl)

I

[ResolveOptions](.././dns/~/ResolveOptions "ResolveOptions")

No documentation available

-   [ttl](.././dns/~/ResolveOptions#property_ttl)

I

[ResolverOptions](.././dns/~/ResolverOptions "ResolverOptions")

No documentation available

-   [timeout](.././dns/~/ResolverOptions#property_timeout)
-   [tries](.././dns/~/ResolverOptions#property_tries)

I

[ResolveWithTtlOptions](.././dns/~/ResolveWithTtlOptions "ResolveWithTtlOptions")

No documentation available

-   [ttl](.././dns/~/ResolveWithTtlOptions#property_ttl)

I

[SoaRecord](.././dns/~/SoaRecord "SoaRecord")

No documentation available

-   [expire](.././dns/~/SoaRecord#property_expire)
-   [hostmaster](.././dns/~/SoaRecord#property_hostmaster)
-   [minttl](.././dns/~/SoaRecord#property_minttl)
-   [nsname](.././dns/~/SoaRecord#property_nsname)
-   [refresh](.././dns/~/SoaRecord#property_refresh)
-   [retry](.././dns/~/SoaRecord#property_retry)
-   [serial](.././dns/~/SoaRecord#property_serial)

I

[SrvRecord](.././dns/~/SrvRecord "SrvRecord")

No documentation available

-   [name](.././dns/~/SrvRecord#property_name)
-   [port](.././dns/~/SrvRecord#property_port)
-   [priority](.././dns/~/SrvRecord#property_priority)
-   [weight](.././dns/~/SrvRecord#property_weight)

N

[promises](.././dns/~/promises "promises")

The `dns.promises` API provides an alternative set of asynchronous DNS methods that return `Promise` objects rather than using callbacks. The API is accessible via `import { promises as dnsPromises } from 'node:dns'` or `import dnsPromises from 'node:dns/promises'`.

T

[AnyRecord](.././dns/~/AnyRecord "AnyRecord")

No documentation available

T

[AnyRecordWithTtl](.././dns/~/AnyRecordWithTtl "AnyRecordWithTtl")

No documentation available

v

[ADDRCONFIG](.././dns/~/ADDRCONFIG "ADDRCONFIG")

Limits returned address types to the types of non-loopback addresses configured on the system. For example, IPv4 addresses are only returned if the current system has at least one IPv4 address configured.

v

[ADDRGETNETWORKPARAMS](.././dns/~/ADDRGETNETWORKPARAMS "ADDRGETNETWORKPARAMS")

No documentation available

v

[ALL](.././dns/~/ALL "ALL")

If `dns.V4MAPPED` is specified, return resolved IPv6 addresses as well as IPv4 mapped IPv6 addresses.

v

[BADFAMILY](.././dns/~/BADFAMILY "BADFAMILY")

No documentation available

v

[BADFLAGS](.././dns/~/BADFLAGS "BADFLAGS")

No documentation available

v

[BADHINTS](.././dns/~/BADHINTS "BADHINTS")

No documentation available

v

[BADNAME](.././dns/~/BADNAME "BADNAME")

No documentation available

v

[BADQUERY](.././dns/~/BADQUERY "BADQUERY")

No documentation available

v

[BADRESP](.././dns/~/BADRESP "BADRESP")

No documentation available

v

[BADSTR](.././dns/~/BADSTR "BADSTR")

No documentation available

v

[CANCELLED](.././dns/~/CANCELLED "CANCELLED")

No documentation available

v

[CONNREFUSED](.././dns/~/CONNREFUSED "CONNREFUSED")

No documentation available

v

[DESTRUCTION](.././dns/~/DESTRUCTION "DESTRUCTION")

No documentation available

v

[EOF](.././dns/~/EOF "EOF")

No documentation available

v

[FILE](.././dns/~/FILE "FILE")

No documentation available

v

[FORMERR](.././dns/~/FORMERR "FORMERR")

No documentation available

v

[LOADIPHLPAPI](.././dns/~/LOADIPHLPAPI "LOADIPHLPAPI")

No documentation available

v

[NODATA](.././dns/~/NODATA "NODATA")

No documentation available

v

[NOMEM](.././dns/~/NOMEM "NOMEM")

No documentation available

v

[NONAME](.././dns/~/NONAME "NONAME")

No documentation available

v

[NOTFOUND](.././dns/~/NOTFOUND "NOTFOUND")

No documentation available

v

[NOTIMP](.././dns/~/NOTIMP "NOTIMP")

No documentation available

v

[NOTINITIALIZED](.././dns/~/NOTINITIALIZED "NOTINITIALIZED")

No documentation available

v

[promises.ADDRGETNETWORKPARAMS](.././dns/promises/~/promises.ADDRGETNETWORKPARAMS "promises.ADDRGETNETWORKPARAMS")

No documentation available

v

[promises.BADFAMILY](.././dns/promises/~/promises.BADFAMILY "promises.BADFAMILY")

No documentation available

v

[promises.BADFLAGS](.././dns/promises/~/promises.BADFLAGS "promises.BADFLAGS")

No documentation available

v

[promises.BADHINTS](.././dns/promises/~/promises.BADHINTS "promises.BADHINTS")

No documentation available

v

[promises.BADNAME](.././dns/promises/~/promises.BADNAME "promises.BADNAME")

No documentation available

v

[promises.BADQUERY](.././dns/promises/~/promises.BADQUERY "promises.BADQUERY")

No documentation available

v

[promises.BADRESP](.././dns/promises/~/promises.BADRESP "promises.BADRESP")

No documentation available

v

[promises.BADSTR](.././dns/promises/~/promises.BADSTR "promises.BADSTR")

No documentation available

v

[promises.CANCELLED](.././dns/promises/~/promises.CANCELLED "promises.CANCELLED")

No documentation available

v

[promises.CONNREFUSED](.././dns/promises/~/promises.CONNREFUSED "promises.CONNREFUSED")

No documentation available

v

[promises.DESTRUCTION](.././dns/promises/~/promises.DESTRUCTION "promises.DESTRUCTION")

No documentation available

v

[promises.EOF](.././dns/promises/~/promises.EOF "promises.EOF")

No documentation available

v

[promises.FILE](.././dns/promises/~/promises.FILE "promises.FILE")

No documentation available

v

[promises.FORMERR](.././dns/promises/~/promises.FORMERR "promises.FORMERR")

No documentation available

v

[promises.LOADIPHLPAPI](.././dns/promises/~/promises.LOADIPHLPAPI "promises.LOADIPHLPAPI")

No documentation available

v

[promises.NODATA](.././dns/promises/~/promises.NODATA "promises.NODATA")

No documentation available

v

[promises.NOMEM](.././dns/promises/~/promises.NOMEM "promises.NOMEM")

No documentation available

v

[promises.NONAME](.././dns/promises/~/promises.NONAME "promises.NONAME")

No documentation available

v

[promises.NOTFOUND](.././dns/promises/~/promises.NOTFOUND "promises.NOTFOUND")

No documentation available

v

[promises.NOTIMP](.././dns/promises/~/promises.NOTIMP "promises.NOTIMP")

No documentation available

v

[promises.NOTINITIALIZED](.././dns/promises/~/promises.NOTINITIALIZED "promises.NOTINITIALIZED")

No documentation available

v

[promises.REFUSED](.././dns/promises/~/promises.REFUSED "promises.REFUSED")

No documentation available

v

[promises.SERVFAIL](.././dns/promises/~/promises.SERVFAIL "promises.SERVFAIL")

No documentation available

v

[promises.TIMEOUT](.././dns/promises/~/promises.TIMEOUT "promises.TIMEOUT")

No documentation available

v

[REFUSED](.././dns/~/REFUSED "REFUSED")

No documentation available

v

[SERVFAIL](.././dns/~/SERVFAIL "SERVFAIL")

No documentation available

v

[TIMEOUT](.././dns/~/TIMEOUT "TIMEOUT")

No documentation available

v

[V4MAPPED](.././dns/~/V4MAPPED "V4MAPPED")

If the IPv6 family was specified, but no IPv6 addresses were found, then return IPv4 mapped IPv6 addresses. It is not supported on some operating systems (e.g. FreeBSD 10.1).
