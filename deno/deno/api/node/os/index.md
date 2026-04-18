---
title: "os - Node documentation"
source: "https://docs.deno.com/api/node/os/"
canonical_url: "https://docs.deno.com/api/node/os/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:26.285Z"
content_hash: "888e62675179f8570701959d05885baee2f826838a7ed58ce8d79e2a302758af"
menu_path: ["os - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/path/index.md", "title": "path - Node documentation"}
nav_next: {"path": "deno/deno/api/node/perf_hooks/index.md", "title": "perf_hooks - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:os";
```

The `node:os` module provides operating system-related utility methods and properties. It can be accessed using:

```js
import os from 'node:os';
```

### Functions [#](#Functions)

f

[arch](.././os/~/arch "arch")

Returns the operating system CPU architecture for which the Node.js binary was compiled. Possible values are `'arm'`, `'arm64'`, `'ia32'`, `'loong64'`, `'mips'`, `'mipsel'`, `'ppc'`, `'ppc64'`, `'riscv64'`, `'s390'`, `'s390x'`, and `'x64'`.

f

[availableParallelism](.././os/~/availableParallelism "availableParallelism")

Returns an estimate of the default amount of parallelism a program should use. Always returns a value greater than zero.

f

[cpus](.././os/~/cpus "cpus")

Returns an array of objects containing information about each logical CPU core. The array will be empty if no CPU information is available, such as if the `/proc` file system is unavailable.

f

[endianness](.././os/~/endianness "endianness")

Returns a string identifying the endianness of the CPU for which the Node.js binary was compiled.

f

[freemem](.././os/~/freemem "freemem")

Returns the amount of free system memory in bytes as an integer.

f

[getPriority](.././os/~/getPriority "getPriority")

Returns the scheduling priority for the process specified by `pid`. If `pid` is not provided or is `0`, the priority of the current process is returned.

f

[homedir](.././os/~/homedir "homedir")

Returns the string path of the current user's home directory.

f

[hostname](.././os/~/hostname "hostname")

Returns the host name of the operating system as a string.

f

[loadavg](.././os/~/loadavg "loadavg")

Returns an array containing the 1, 5, and 15 minute load averages.

f

[machine](.././os/~/machine "machine")

Returns the machine type as a string, such as `arm`, `arm64`, `aarch64`, `mips`, `mips64`, `ppc64`, `ppc64le`, `s390`, `s390x`, `i386`, `i686`, `x86_64`.

f

[networkInterfaces](.././os/~/networkInterfaces "networkInterfaces")

Returns an object containing network interfaces that have been assigned a network address.

f

[platform](.././os/~/platform "platform")

Returns a string identifying the operating system platform for which the Node.js binary was compiled. The value is set at compile time. Possible values are `'aix'`, `'darwin'`, `'freebsd'`, `'linux'`, `'openbsd'`, `'sunos'`, and `'win32'`.

f

[release](.././os/~/release "release")

Returns the operating system as a string.

f

[setPriority](.././os/~/setPriority "setPriority")

Attempts to set the scheduling priority for the process specified by `pid`. If `pid` is not provided or is `0`, the process ID of the current process is used.

f

[tmpdir](.././os/~/tmpdir "tmpdir")

Returns the operating system's default directory for temporary files as a string.

f

[totalmem](.././os/~/totalmem "totalmem")

Returns the total amount of system memory in bytes as an integer.

f

[type](.././os/~/type "type")

Returns the operating system name as returned by [`uname(3)`](https://linux.die.net/man/3/uname). For example, it returns `'Linux'` on Linux, `'Darwin'` on macOS, and `'Windows_NT'` on Windows.

f

[uptime](.././os/~/uptime "uptime")

Returns the system uptime in number of seconds.

f

[userInfo](.././os/~/userInfo "userInfo")

Returns information about the currently effective user. On POSIX platforms, this is typically a subset of the password file. The returned object includes the `username`, `uid`, `gid`, `shell`, and `homedir`. On Windows, the `uid` and `gid` fields are `-1`, and `shell` is `null`.

f

[version](.././os/~/version "version")

Returns a string identifying the kernel version.

### Interfaces [#](#Interfaces)

I

[CpuInfo](.././os/~/CpuInfo "CpuInfo")

The `node:os` module provides operating system-related utility methods and properties. It can be accessed using:

*   [model](.././os/~/CpuInfo#property_model)
*   [speed](.././os/~/CpuInfo#property_speed)
*   [times](.././os/~/CpuInfo#property_times)

I

[NetworkInterfaceBase](.././os/~/NetworkInterfaceBase "NetworkInterfaceBase")

No documentation available

*   [address](.././os/~/NetworkInterfaceBase#property_address)
*   [cidr](.././os/~/NetworkInterfaceBase#property_cidr)
*   [internal](.././os/~/NetworkInterfaceBase#property_internal)
*   [mac](.././os/~/NetworkInterfaceBase#property_mac)
*   [netmask](.././os/~/NetworkInterfaceBase#property_netmask)

I

[NetworkInterfaceInfoIPv4](.././os/~/NetworkInterfaceInfoIPv4 "NetworkInterfaceInfoIPv4")

No documentation available

*   [family](.././os/~/NetworkInterfaceInfoIPv4#property_family)
*   [scopeid](.././os/~/NetworkInterfaceInfoIPv4#property_scopeid)

I

[NetworkInterfaceInfoIPv6](.././os/~/NetworkInterfaceInfoIPv6 "NetworkInterfaceInfoIPv6")

No documentation available

*   [family](.././os/~/NetworkInterfaceInfoIPv6#property_family)
*   [scopeid](.././os/~/NetworkInterfaceInfoIPv6#property_scopeid)

I

[UserInfo](.././os/~/UserInfo "UserInfo")

No documentation available

*   [gid](.././os/~/UserInfo#property_gid)
*   [homedir](.././os/~/UserInfo#property_homedir)
*   [shell](.././os/~/UserInfo#property_shell)
*   [uid](.././os/~/UserInfo#property_uid)
*   [username](.././os/~/UserInfo#property_username)

### Namespaces [#](#Namespaces)

N

[constants](.././os/~/constants "constants")

No documentation available

N

[constants.dlopen](.././os/~/constants.dlopen "constants.dlopen")

No documentation available

N

[constants.errno](.././os/~/constants.errno "constants.errno")

No documentation available

N

[constants.priority](.././os/~/constants.priority "constants.priority")

No documentation available

N

v

[constants.signals](.././os/~/constants.signals "constants.signals")

No documentation available

### Type Aliases [#](<#Type Aliases>)

T

[NetworkInterfaceInfo](.././os/~/NetworkInterfaceInfo "NetworkInterfaceInfo")

No documentation available

T

[SignalConstants](.././os/~/SignalConstants "SignalConstants")

No documentation available

### Variables [#](#Variables)

v

[constants.dlopen.RTLD\_DEEPBIND](.././os/~/constants.dlopen.RTLD_DEEPBIND "constants.dlopen.RTLD_DEEPBIND")

No documentation available

v

[constants.dlopen.RTLD\_GLOBAL](.././os/~/constants.dlopen.RTLD_GLOBAL "constants.dlopen.RTLD_GLOBAL")

No documentation available

v

[constants.dlopen.RTLD\_LAZY](.././os/~/constants.dlopen.RTLD_LAZY "constants.dlopen.RTLD_LAZY")

No documentation available

v

[constants.dlopen.RTLD\_LOCAL](.././os/~/constants.dlopen.RTLD_LOCAL "constants.dlopen.RTLD_LOCAL")

No documentation available

v

[constants.dlopen.RTLD\_NOW](.././os/~/constants.dlopen.RTLD_NOW "constants.dlopen.RTLD_NOW")

No documentation available

v

[constants.errno.E2BIG](.././os/~/constants.errno.E2BIG "constants.errno.E2BIG")

No documentation available

v

[constants.errno.EACCES](.././os/~/constants.errno.EACCES "constants.errno.EACCES")

No documentation available

v

[constants.errno.EADDRINUSE](.././os/~/constants.errno.EADDRINUSE "constants.errno.EADDRINUSE")

No documentation available

v

[constants.errno.EADDRNOTAVAIL](.././os/~/constants.errno.EADDRNOTAVAIL "constants.errno.EADDRNOTAVAIL")

No documentation available

v

[constants.errno.EAFNOSUPPORT](.././os/~/constants.errno.EAFNOSUPPORT "constants.errno.EAFNOSUPPORT")

No documentation available

v

[constants.errno.EAGAIN](.././os/~/constants.errno.EAGAIN "constants.errno.EAGAIN")

No documentation available

v

[constants.errno.EALREADY](.././os/~/constants.errno.EALREADY "constants.errno.EALREADY")

No documentation available

v

[constants.errno.EBADF](.././os/~/constants.errno.EBADF "constants.errno.EBADF")

No documentation available

v

[constants.errno.EBADMSG](.././os/~/constants.errno.EBADMSG "constants.errno.EBADMSG")

No documentation available

v

[constants.errno.EBUSY](.././os/~/constants.errno.EBUSY "constants.errno.EBUSY")

No documentation available

v

[constants.errno.ECANCELED](.././os/~/constants.errno.ECANCELED "constants.errno.ECANCELED")

No documentation available

v

[constants.errno.ECHILD](.././os/~/constants.errno.ECHILD "constants.errno.ECHILD")

No documentation available

v

[constants.errno.ECONNABORTED](.././os/~/constants.errno.ECONNABORTED "constants.errno.ECONNABORTED")

No documentation available

v

[constants.errno.ECONNREFUSED](.././os/~/constants.errno.ECONNREFUSED "constants.errno.ECONNREFUSED")

No documentation available

v

[constants.errno.ECONNRESET](.././os/~/constants.errno.ECONNRESET "constants.errno.ECONNRESET")

No documentation available

v

[constants.errno.EDEADLK](.././os/~/constants.errno.EDEADLK "constants.errno.EDEADLK")

No documentation available

v

[constants.errno.EDESTADDRREQ](.././os/~/constants.errno.EDESTADDRREQ "constants.errno.EDESTADDRREQ")

No documentation available

v

[constants.errno.EDOM](.././os/~/constants.errno.EDOM "constants.errno.EDOM")

No documentation available

v

[constants.errno.EDQUOT](.././os/~/constants.errno.EDQUOT "constants.errno.EDQUOT")

No documentation available

v

[constants.errno.EEXIST](.././os/~/constants.errno.EEXIST "constants.errno.EEXIST")

No documentation available

v

[constants.errno.EFAULT](.././os/~/constants.errno.EFAULT "constants.errno.EFAULT")

No documentation available

v

[constants.errno.EFBIG](.././os/~/constants.errno.EFBIG "constants.errno.EFBIG")

No documentation available

v

[constants.errno.EHOSTUNREACH](.././os/~/constants.errno.EHOSTUNREACH "constants.errno.EHOSTUNREACH")

No documentation available

v

[constants.errno.EIDRM](.././os/~/constants.errno.EIDRM "constants.errno.EIDRM")

No documentation available

v

[constants.errno.EILSEQ](.././os/~/constants.errno.EILSEQ "constants.errno.EILSEQ")

No documentation available

v

[constants.errno.EINPROGRESS](.././os/~/constants.errno.EINPROGRESS "constants.errno.EINPROGRESS")

No documentation available

v

[constants.errno.EINTR](.././os/~/constants.errno.EINTR "constants.errno.EINTR")

No documentation available

v

[constants.errno.EINVAL](.././os/~/constants.errno.EINVAL "constants.errno.EINVAL")

No documentation available

v

[constants.errno.EIO](.././os/~/constants.errno.EIO "constants.errno.EIO")

No documentation available

v

[constants.errno.EISCONN](.././os/~/constants.errno.EISCONN "constants.errno.EISCONN")

No documentation available

v

[constants.errno.EISDIR](.././os/~/constants.errno.EISDIR "constants.errno.EISDIR")

No documentation available

v

[constants.errno.ELOOP](.././os/~/constants.errno.ELOOP "constants.errno.ELOOP")

No documentation available

v

[constants.errno.EMFILE](.././os/~/constants.errno.EMFILE "constants.errno.EMFILE")

No documentation available

v

[constants.errno.EMLINK](.././os/~/constants.errno.EMLINK "constants.errno.EMLINK")

No documentation available

v

[constants.errno.EMSGSIZE](.././os/~/constants.errno.EMSGSIZE "constants.errno.EMSGSIZE")

No documentation available

v

[constants.errno.EMULTIHOP](.././os/~/constants.errno.EMULTIHOP "constants.errno.EMULTIHOP")

No documentation available

v

[constants.errno.ENAMETOOLONG](.././os/~/constants.errno.ENAMETOOLONG "constants.errno.ENAMETOOLONG")

No documentation available

v

[constants.errno.ENETDOWN](.././os/~/constants.errno.ENETDOWN "constants.errno.ENETDOWN")

No documentation available

v

[constants.errno.ENETRESET](.././os/~/constants.errno.ENETRESET "constants.errno.ENETRESET")

No documentation available

v

[constants.errno.ENETUNREACH](.././os/~/constants.errno.ENETUNREACH "constants.errno.ENETUNREACH")

No documentation available

v

[constants.errno.ENFILE](.././os/~/constants.errno.ENFILE "constants.errno.ENFILE")

No documentation available

v

[constants.errno.ENOBUFS](.././os/~/constants.errno.ENOBUFS "constants.errno.ENOBUFS")

No documentation available

v

[constants.errno.ENODATA](.././os/~/constants.errno.ENODATA "constants.errno.ENODATA")

No documentation available

v

[constants.errno.ENODEV](.././os/~/constants.errno.ENODEV "constants.errno.ENODEV")

No documentation available

v

[constants.errno.ENOENT](.././os/~/constants.errno.ENOENT "constants.errno.ENOENT")

No documentation available

v

[constants.errno.ENOEXEC](.././os/~/constants.errno.ENOEXEC "constants.errno.ENOEXEC")

No documentation available

v

[constants.errno.ENOLCK](.././os/~/constants.errno.ENOLCK "constants.errno.ENOLCK")

No documentation available

v

[constants.errno.ENOLINK](.././os/~/constants.errno.ENOLINK "constants.errno.ENOLINK")

No documentation available

v

[constants.errno.ENOMEM](.././os/~/constants.errno.ENOMEM "constants.errno.ENOMEM")

No documentation available

v

[constants.errno.ENOMSG](.././os/~/constants.errno.ENOMSG "constants.errno.ENOMSG")

No documentation available

v

[constants.errno.ENOPROTOOPT](.././os/~/constants.errno.ENOPROTOOPT "constants.errno.ENOPROTOOPT")

No documentation available

v

[constants.errno.ENOSPC](.././os/~/constants.errno.ENOSPC "constants.errno.ENOSPC")

No documentation available

v

[constants.errno.ENOSR](.././os/~/constants.errno.ENOSR "constants.errno.ENOSR")

No documentation available

v

[constants.errno.ENOSTR](.././os/~/constants.errno.ENOSTR "constants.errno.ENOSTR")

No documentation available

v

[constants.errno.ENOSYS](.././os/~/constants.errno.ENOSYS "constants.errno.ENOSYS")

No documentation available

v

[constants.errno.ENOTCONN](.././os/~/constants.errno.ENOTCONN "constants.errno.ENOTCONN")

No documentation available

v

[constants.errno.ENOTDIR](.././os/~/constants.errno.ENOTDIR "constants.errno.ENOTDIR")

No documentation available

v

[constants.errno.ENOTEMPTY](.././os/~/constants.errno.ENOTEMPTY "constants.errno.ENOTEMPTY")

No documentation available

v

[constants.errno.ENOTSOCK](.././os/~/constants.errno.ENOTSOCK "constants.errno.ENOTSOCK")

No documentation available

v

[constants.errno.ENOTSUP](.././os/~/constants.errno.ENOTSUP "constants.errno.ENOTSUP")

No documentation available

v

[constants.errno.ENOTTY](.././os/~/constants.errno.ENOTTY "constants.errno.ENOTTY")

No documentation available

v

[constants.errno.ENXIO](.././os/~/constants.errno.ENXIO "constants.errno.ENXIO")

No documentation available

v

[constants.errno.EOPNOTSUPP](.././os/~/constants.errno.EOPNOTSUPP "constants.errno.EOPNOTSUPP")

No documentation available

v

[constants.errno.EOVERFLOW](.././os/~/constants.errno.EOVERFLOW "constants.errno.EOVERFLOW")

No documentation available

v

[constants.errno.EPERM](.././os/~/constants.errno.EPERM "constants.errno.EPERM")

No documentation available

v

[constants.errno.EPIPE](.././os/~/constants.errno.EPIPE "constants.errno.EPIPE")

No documentation available

v

[constants.errno.EPROTO](.././os/~/constants.errno.EPROTO "constants.errno.EPROTO")

No documentation available

v

[constants.errno.EPROTONOSUPPORT](.././os/~/constants.errno.EPROTONOSUPPORT "constants.errno.EPROTONOSUPPORT")

No documentation available

v

[constants.errno.EPROTOTYPE](.././os/~/constants.errno.EPROTOTYPE "constants.errno.EPROTOTYPE")

No documentation available

v

[constants.errno.ERANGE](.././os/~/constants.errno.ERANGE "constants.errno.ERANGE")

No documentation available

v

[constants.errno.EROFS](.././os/~/constants.errno.EROFS "constants.errno.EROFS")

No documentation available

v

[constants.errno.ESPIPE](.././os/~/constants.errno.ESPIPE "constants.errno.ESPIPE")

No documentation available

v

[constants.errno.ESRCH](.././os/~/constants.errno.ESRCH "constants.errno.ESRCH")

No documentation available

v

[constants.errno.ESTALE](.././os/~/constants.errno.ESTALE "constants.errno.ESTALE")

No documentation available

v

[constants.errno.ETIME](.././os/~/constants.errno.ETIME "constants.errno.ETIME")

No documentation available

v

[constants.errno.ETIMEDOUT](.././os/~/constants.errno.ETIMEDOUT "constants.errno.ETIMEDOUT")

No documentation available

v

[constants.errno.ETXTBSY](.././os/~/constants.errno.ETXTBSY "constants.errno.ETXTBSY")

No documentation available

v

[constants.errno.EWOULDBLOCK](.././os/~/constants.errno.EWOULDBLOCK "constants.errno.EWOULDBLOCK")

No documentation available

v

[constants.errno.EXDEV](.././os/~/constants.errno.EXDEV "constants.errno.EXDEV")

No documentation available

v

[constants.errno.WSA\_E\_CANCELLED](.././os/~/constants.errno.WSA_E_CANCELLED "constants.errno.WSA_E_CANCELLED")

No documentation available

v

[constants.errno.WSA\_E\_NO\_MORE](.././os/~/constants.errno.WSA_E_NO_MORE "constants.errno.WSA_E_NO_MORE")

No documentation available

v

[constants.errno.WSAEACCES](.././os/~/constants.errno.WSAEACCES "constants.errno.WSAEACCES")

No documentation available

v

[constants.errno.WSAEADDRINUSE](.././os/~/constants.errno.WSAEADDRINUSE "constants.errno.WSAEADDRINUSE")

No documentation available

v

[constants.errno.WSAEADDRNOTAVAIL](.././os/~/constants.errno.WSAEADDRNOTAVAIL "constants.errno.WSAEADDRNOTAVAIL")

No documentation available

v

[constants.errno.WSAEAFNOSUPPORT](.././os/~/constants.errno.WSAEAFNOSUPPORT "constants.errno.WSAEAFNOSUPPORT")

No documentation available

v

[constants.errno.WSAEALREADY](.././os/~/constants.errno.WSAEALREADY "constants.errno.WSAEALREADY")

No documentation available

v

[constants.errno.WSAEBADF](.././os/~/constants.errno.WSAEBADF "constants.errno.WSAEBADF")

No documentation available

v

[constants.errno.WSAECANCELLED](.././os/~/constants.errno.WSAECANCELLED "constants.errno.WSAECANCELLED")

No documentation available

v

[constants.errno.WSAECONNABORTED](.././os/~/constants.errno.WSAECONNABORTED "constants.errno.WSAECONNABORTED")

No documentation available

v

[constants.errno.WSAECONNREFUSED](.././os/~/constants.errno.WSAECONNREFUSED "constants.errno.WSAECONNREFUSED")

No documentation available

v

[constants.errno.WSAECONNRESET](.././os/~/constants.errno.WSAECONNRESET "constants.errno.WSAECONNRESET")

No documentation available

v

[constants.errno.WSAEDESTADDRREQ](.././os/~/constants.errno.WSAEDESTADDRREQ "constants.errno.WSAEDESTADDRREQ")

No documentation available

v

[constants.errno.WSAEDISCON](.././os/~/constants.errno.WSAEDISCON "constants.errno.WSAEDISCON")

No documentation available

v

[constants.errno.WSAEDQUOT](.././os/~/constants.errno.WSAEDQUOT "constants.errno.WSAEDQUOT")

No documentation available

v

[constants.errno.WSAEFAULT](.././os/~/constants.errno.WSAEFAULT "constants.errno.WSAEFAULT")

No documentation available

v

[constants.errno.WSAEHOSTDOWN](.././os/~/constants.errno.WSAEHOSTDOWN "constants.errno.WSAEHOSTDOWN")

No documentation available

v

[constants.errno.WSAEHOSTUNREACH](.././os/~/constants.errno.WSAEHOSTUNREACH "constants.errno.WSAEHOSTUNREACH")

No documentation available

v

[constants.errno.WSAEINPROGRESS](.././os/~/constants.errno.WSAEINPROGRESS "constants.errno.WSAEINPROGRESS")

No documentation available

v

[constants.errno.WSAEINTR](.././os/~/constants.errno.WSAEINTR "constants.errno.WSAEINTR")

No documentation available

v

[constants.errno.WSAEINVAL](.././os/~/constants.errno.WSAEINVAL "constants.errno.WSAEINVAL")

No documentation available

v

[constants.errno.WSAEINVALIDPROCTABLE](.././os/~/constants.errno.WSAEINVALIDPROCTABLE "constants.errno.WSAEINVALIDPROCTABLE")

No documentation available

v

[constants.errno.WSAEINVALIDPROVIDER](.././os/~/constants.errno.WSAEINVALIDPROVIDER "constants.errno.WSAEINVALIDPROVIDER")

No documentation available

v

[constants.errno.WSAEISCONN](.././os/~/constants.errno.WSAEISCONN "constants.errno.WSAEISCONN")

No documentation available

v

[constants.errno.WSAELOOP](.././os/~/constants.errno.WSAELOOP "constants.errno.WSAELOOP")

No documentation available

v

[constants.errno.WSAEMFILE](.././os/~/constants.errno.WSAEMFILE "constants.errno.WSAEMFILE")

No documentation available

v

[constants.errno.WSAEMSGSIZE](.././os/~/constants.errno.WSAEMSGSIZE "constants.errno.WSAEMSGSIZE")

No documentation available

v

[constants.errno.WSAENAMETOOLONG](.././os/~/constants.errno.WSAENAMETOOLONG "constants.errno.WSAENAMETOOLONG")

No documentation available

v

[constants.errno.WSAENETDOWN](.././os/~/constants.errno.WSAENETDOWN "constants.errno.WSAENETDOWN")

No documentation available

v

[constants.errno.WSAENETRESET](.././os/~/constants.errno.WSAENETRESET "constants.errno.WSAENETRESET")

No documentation available

v

[constants.errno.WSAENETUNREACH](.././os/~/constants.errno.WSAENETUNREACH "constants.errno.WSAENETUNREACH")

No documentation available

v

[constants.errno.WSAENOBUFS](.././os/~/constants.errno.WSAENOBUFS "constants.errno.WSAENOBUFS")

No documentation available

v

[constants.errno.WSAENOMORE](.././os/~/constants.errno.WSAENOMORE "constants.errno.WSAENOMORE")

No documentation available

v

[constants.errno.WSAENOPROTOOPT](.././os/~/constants.errno.WSAENOPROTOOPT "constants.errno.WSAENOPROTOOPT")

No documentation available

v

[constants.errno.WSAENOTCONN](.././os/~/constants.errno.WSAENOTCONN "constants.errno.WSAENOTCONN")

No documentation available

v

[constants.errno.WSAENOTEMPTY](.././os/~/constants.errno.WSAENOTEMPTY "constants.errno.WSAENOTEMPTY")

No documentation available

v

[constants.errno.WSAENOTSOCK](.././os/~/constants.errno.WSAENOTSOCK "constants.errno.WSAENOTSOCK")

No documentation available

v

[constants.errno.WSAEOPNOTSUPP](.././os/~/constants.errno.WSAEOPNOTSUPP "constants.errno.WSAEOPNOTSUPP")

No documentation available

v

[constants.errno.WSAEPFNOSUPPORT](.././os/~/constants.errno.WSAEPFNOSUPPORT "constants.errno.WSAEPFNOSUPPORT")

No documentation available

v

[constants.errno.WSAEPROCLIM](.././os/~/constants.errno.WSAEPROCLIM "constants.errno.WSAEPROCLIM")

No documentation available

v

[constants.errno.WSAEPROTONOSUPPORT](.././os/~/constants.errno.WSAEPROTONOSUPPORT "constants.errno.WSAEPROTONOSUPPORT")

No documentation available

v

[constants.errno.WSAEPROTOTYPE](.././os/~/constants.errno.WSAEPROTOTYPE "constants.errno.WSAEPROTOTYPE")

No documentation available

v

[constants.errno.WSAEPROVIDERFAILEDINIT](.././os/~/constants.errno.WSAEPROVIDERFAILEDINIT "constants.errno.WSAEPROVIDERFAILEDINIT")

No documentation available

v

[constants.errno.WSAEREFUSED](.././os/~/constants.errno.WSAEREFUSED "constants.errno.WSAEREFUSED")

No documentation available

v

[constants.errno.WSAEREMOTE](.././os/~/constants.errno.WSAEREMOTE "constants.errno.WSAEREMOTE")

No documentation available

v

[constants.errno.WSAESHUTDOWN](.././os/~/constants.errno.WSAESHUTDOWN "constants.errno.WSAESHUTDOWN")

No documentation available

v

[constants.errno.WSAESOCKTNOSUPPORT](.././os/~/constants.errno.WSAESOCKTNOSUPPORT "constants.errno.WSAESOCKTNOSUPPORT")

No documentation available

v

[constants.errno.WSAESTALE](.././os/~/constants.errno.WSAESTALE "constants.errno.WSAESTALE")

No documentation available

v

[constants.errno.WSAETIMEDOUT](.././os/~/constants.errno.WSAETIMEDOUT "constants.errno.WSAETIMEDOUT")

No documentation available

v

[constants.errno.WSAETOOMANYREFS](.././os/~/constants.errno.WSAETOOMANYREFS "constants.errno.WSAETOOMANYREFS")

No documentation available

v

[constants.errno.WSAEUSERS](.././os/~/constants.errno.WSAEUSERS "constants.errno.WSAEUSERS")

No documentation available

v

[constants.errno.WSAEWOULDBLOCK](.././os/~/constants.errno.WSAEWOULDBLOCK "constants.errno.WSAEWOULDBLOCK")

No documentation available

v

[constants.errno.WSANOTINITIALISED](.././os/~/constants.errno.WSANOTINITIALISED "constants.errno.WSANOTINITIALISED")

No documentation available

v

[constants.errno.WSASERVICE\_NOT\_FOUND](.././os/~/constants.errno.WSASERVICE_NOT_FOUND "constants.errno.WSASERVICE_NOT_FOUND")

No documentation available

v

[constants.errno.WSASYSCALLFAILURE](.././os/~/constants.errno.WSASYSCALLFAILURE "constants.errno.WSASYSCALLFAILURE")

No documentation available

v

[constants.errno.WSASYSNOTREADY](.././os/~/constants.errno.WSASYSNOTREADY "constants.errno.WSASYSNOTREADY")

No documentation available

v

[constants.errno.WSATYPE\_NOT\_FOUND](.././os/~/constants.errno.WSATYPE_NOT_FOUND "constants.errno.WSATYPE_NOT_FOUND")

No documentation available

v

[constants.errno.WSAVERNOTSUPPORTED](.././os/~/constants.errno.WSAVERNOTSUPPORTED "constants.errno.WSAVERNOTSUPPORTED")

No documentation available

v

[constants.priority.PRIORITY\_ABOVE\_NORMAL](.././os/~/constants.priority.PRIORITY_ABOVE_NORMAL "constants.priority.PRIORITY_ABOVE_NORMAL")

No documentation available

v

[constants.priority.PRIORITY\_BELOW\_NORMAL](.././os/~/constants.priority.PRIORITY_BELOW_NORMAL "constants.priority.PRIORITY_BELOW_NORMAL")

No documentation available

v

[constants.priority.PRIORITY\_HIGH](.././os/~/constants.priority.PRIORITY_HIGH "constants.priority.PRIORITY_HIGH")

No documentation available

v

[constants.priority.PRIORITY\_HIGHEST](.././os/~/constants.priority.PRIORITY_HIGHEST "constants.priority.PRIORITY_HIGHEST")

No documentation available

v

[constants.priority.PRIORITY\_LOW](.././os/~/constants.priority.PRIORITY_LOW "constants.priority.PRIORITY_LOW")

No documentation available

v

[constants.priority.PRIORITY\_NORMAL](.././os/~/constants.priority.PRIORITY_NORMAL "constants.priority.PRIORITY_NORMAL")

No documentation available

v

[constants.UV\_UDP\_REUSEADDR](.././os/~/constants.UV_UDP_REUSEADDR "constants.UV_UDP_REUSEADDR")

No documentation available

v

[devNull](.././os/~/devNull "devNull")

No documentation available

v

[EOL](.././os/~/EOL "EOL")

The operating system-specific end-of-line marker.
