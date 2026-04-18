---
title: "Errors - Deno documentation"
source: "https://docs.deno.com/api/deno/errors"
canonical_url: "https://docs.deno.com/api/deno/errors"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:08:47.355Z"
content_hash: "b922f15f7c405a94e82a102f9bd611248b2d4ea27f3448014e83530a591191db"
menu_path: ["Errors - Deno documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/deno/cloud/index.md", "title": "Cloud - Deno documentation"}
nav_next: {"path": "deno/deno/api/deno/fetch/index.md", "title": "Fetch - Deno documentation"}
---

### Classes [#](#Classes)

c

[Deno.errors.AddrInUse](./././~/Deno.errors.AddrInUse "Deno.errors.AddrInUse")

Raised when attempting to open a server listener on an address and port that already has a listener.

c

[Deno.errors.AddrNotAvailable](./././~/Deno.errors.AddrNotAvailable "Deno.errors.AddrNotAvailable")

Raised when the underlying operating system reports an `EADDRNOTAVAIL` error.

c

[Deno.errors.AlreadyExists](./././~/Deno.errors.AlreadyExists "Deno.errors.AlreadyExists")

Raised when trying to create a resource, like a file, that already exits.

c

[Deno.errors.BadResource](./././~/Deno.errors.BadResource "Deno.errors.BadResource")

The underlying IO resource is invalid or closed, and so the operation could not be performed.

c

[Deno.errors.BrokenPipe](./././~/Deno.errors.BrokenPipe "Deno.errors.BrokenPipe")

Raised when trying to write to a resource and a broken pipe error occurs. This can happen when trying to write directly to `stdout` or `stderr` and the operating system is unable to pipe the output for a reason external to the Deno runtime.

c

[Deno.errors.Busy](./././~/Deno.errors.Busy "Deno.errors.Busy")

Raised when the underlying IO resource is not available because it is being awaited on in another block of code.

c

[Deno.errors.ConnectionAborted](./././~/Deno.errors.ConnectionAborted "Deno.errors.ConnectionAborted")

Raised when the underlying operating system reports an `ECONNABORTED` error.

c

[Deno.errors.ConnectionRefused](./././~/Deno.errors.ConnectionRefused "Deno.errors.ConnectionRefused")

Raised when the underlying operating system reports that a connection to a resource is refused.

c

[Deno.errors.ConnectionReset](./././~/Deno.errors.ConnectionReset "Deno.errors.ConnectionReset")

Raised when the underlying operating system reports that a connection has been reset. With network servers, it can be a _normal_ occurrence where a client will abort a connection instead of properly shutting it down.

c

[Deno.errors.FilesystemLoop](./././~/Deno.errors.FilesystemLoop "Deno.errors.FilesystemLoop")

Raised when too many symbolic links were encountered when resolving the filename.

c

[Deno.errors.Http](./././~/Deno.errors.Http "Deno.errors.Http")

Raised in situations where when attempting to load a dynamic import, too many redirects were encountered.

c

[Deno.errors.Interrupted](./././~/Deno.errors.Interrupted "Deno.errors.Interrupted")

Raised when the underlying operating system reports an `EINTR` error. In many cases, this underlying IO error will be handled internally within Deno, or result in an BadResource error instead.

c

[Deno.errors.InvalidData](./././~/Deno.errors.InvalidData "Deno.errors.InvalidData")

Raised when an operation returns data that is invalid for the operation being performed.

c

[Deno.errors.IsADirectory](./././~/Deno.errors.IsADirectory "Deno.errors.IsADirectory")

Raised when trying to open, create or write to a directory.

c

[Deno.errors.NetworkUnreachable](./././~/Deno.errors.NetworkUnreachable "Deno.errors.NetworkUnreachable")

Raised when performing a socket operation but the remote host is not reachable.

c

[Deno.errors.NotADirectory](./././~/Deno.errors.NotADirectory "Deno.errors.NotADirectory")

Raised when trying to perform an operation on a path that is not a directory, when directory is required.

c

[Deno.errors.NotCapable](./././~/Deno.errors.NotCapable "Deno.errors.NotCapable")

Raised when trying to perform an operation while the relevant Deno permission (like `--allow-read`) has not been granted.

c

[Deno.errors.NotConnected](./././~/Deno.errors.NotConnected "Deno.errors.NotConnected")

Raised when the underlying operating system reports an `ENOTCONN` error.

c

[Deno.errors.NotFound](./././~/Deno.errors.NotFound "Deno.errors.NotFound")

Raised when the underlying operating system indicates that the file was not found.

c

[Deno.errors.NotSupported](./././~/Deno.errors.NotSupported "Deno.errors.NotSupported")

Raised when the underlying Deno API is asked to perform a function that is not currently supported.

c

[Deno.errors.PermissionDenied](./././~/Deno.errors.PermissionDenied "Deno.errors.PermissionDenied")

Raised when the underlying operating system indicates the current user which the Deno process is running under does not have the appropriate permissions to a file or resource.

c

[Deno.errors.TimedOut](./././~/Deno.errors.TimedOut "Deno.errors.TimedOut")

Raised when the underlying operating system reports that an I/O operation has timed out (`ETIMEDOUT`).

c

[Deno.errors.UnexpectedEof](./././~/Deno.errors.UnexpectedEof "Deno.errors.UnexpectedEof")

Raised when attempting to read bytes from a resource, but the EOF was unexpectedly encountered.

c

[Deno.errors.WouldBlock](./././~/Deno.errors.WouldBlock "Deno.errors.WouldBlock")

Raised when the underlying operating system would need to block to complete but an asynchronous (non-blocking) API is used.

c

[Deno.errors.WriteZero](./././~/Deno.errors.WriteZero "Deno.errors.WriteZero")

Raised when expecting to write to a IO buffer resulted in zero bytes being written.

### Namespaces [#](#Namespaces)

N

[Deno.errors](./././~/Deno.errors "Deno.errors")

A set of error constructors that are raised by Deno APIs.

