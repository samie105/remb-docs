---
title: "namespace Deno"
source: "https://docs.deno.com/api/deno/~/Deno"
canonical_url: "https://docs.deno.com/api/deno/~/Deno"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T18:04:09.083Z"
content_hash: "91f5014a979e0115dbc5bb19bb43f1230bbad95ede5a4a046e51b94d762c79f5"
menu_path: ["namespace Deno"]
section_path: []
content_language: "en"
---
# namespace Deno

The global namespace where Deno specific, non-standard APIs are located.

c

[Deno.AtomicOperation](../././~/Deno.AtomicOperation "Deno.AtomicOperation")

An operation on a [`Deno.Kv`](../././~/Deno.Kv) that can be performed atomically. Atomic operations do not auto-commit, and must be committed explicitly by calling the `commit` method.

-   [check](../././~/Deno.AtomicOperation#method_check_0)
-   [commit](../././~/Deno.AtomicOperation#method_commit_0)
-   [delete](../././~/Deno.AtomicOperation#method_delete_0)
-   [enqueue](../././~/Deno.AtomicOperation#method_enqueue_0)
-   [max](../././~/Deno.AtomicOperation#method_max_0)
-   [min](../././~/Deno.AtomicOperation#method_min_0)
-   [mutate](../././~/Deno.AtomicOperation#method_mutate_0)
-   [set](../././~/Deno.AtomicOperation#method_set_0)
-   [sum](../././~/Deno.AtomicOperation#method_sum_0)

c

[Deno.ChildProcess](../././~/Deno.ChildProcess "Deno.ChildProcess")

The interface for handling a child process returned from `Deno.Command.spawn`.

-   [kill](../././~/Deno.ChildProcess#method_kill_0)
-   [output](../././~/Deno.ChildProcess#method_output_0)
-   [pid](../././~/Deno.ChildProcess#property_pid)
-   [ref](../././~/Deno.ChildProcess#method_ref_0)
-   [status](../././~/Deno.ChildProcess#property_status)
-   [stderr](../././~/Deno.ChildProcess#accessor_stderr)
-   [stdin](../././~/Deno.ChildProcess#accessor_stdin)
-   [stdout](../././~/Deno.ChildProcess#accessor_stdout)
-   [unref](../././~/Deno.ChildProcess#method_unref_0)

c

[Deno.Command](../././~/Deno.Command "Deno.Command")

Create a child process.

-   [output](../././~/Deno.Command#method_output_0)
-   [outputSync](../././~/Deno.Command#method_outputsync_0)
-   [spawn](../././~/Deno.Command#method_spawn_0)

c

[Deno.FsFile](../././~/Deno.FsFile "Deno.FsFile")

The Deno abstraction for reading and writing files.

-   [close](../././~/Deno.FsFile#method_close_0)
-   [isTerminal](../././~/Deno.FsFile#method_isterminal_0)
-   [lock](../././~/Deno.FsFile#method_lock_0)
-   [lockSync](../././~/Deno.FsFile#method_locksync_0)
-   [read](../././~/Deno.FsFile#method_read_0)
-   [readSync](../././~/Deno.FsFile#method_readsync_0)
-   [readable](../././~/Deno.FsFile#property_readable)
-   [seek](../././~/Deno.FsFile#method_seek_0)
-   [seekSync](../././~/Deno.FsFile#method_seeksync_0)
-   [setRaw](../././~/Deno.FsFile#method_setraw_0)
-   [stat](../././~/Deno.FsFile#method_stat_0)
-   [statSync](../././~/Deno.FsFile#method_statsync_0)
-   [sync](../././~/Deno.FsFile#method_sync_0)
-   [syncData](../././~/Deno.FsFile#method_syncdata_0)
-   [syncDataSync](../././~/Deno.FsFile#method_syncdatasync_0)
-   [syncSync](../././~/Deno.FsFile#method_syncsync_0)
-   [truncate](../././~/Deno.FsFile#method_truncate_0)
-   [truncateSync](../././~/Deno.FsFile#method_truncatesync_0)
-   [tryLock](../././~/Deno.FsFile#method_trylock_0)
-   [tryLockSync](../././~/Deno.FsFile#method_trylocksync_0)
-   [unlock](../././~/Deno.FsFile#method_unlock_0)
-   [unlockSync](../././~/Deno.FsFile#method_unlocksync_0)
-   [utime](../././~/Deno.FsFile#method_utime_0)
-   [utimeSync](../././~/Deno.FsFile#method_utimesync_0)
-   [writable](../././~/Deno.FsFile#property_writable)
-   [write](../././~/Deno.FsFile#method_write_0)
-   [writeSync](../././~/Deno.FsFile#method_writesync_0)

c

[Deno.HttpClient](../././~/Deno.HttpClient "Deno.HttpClient")

A custom `HttpClient` for use with `fetch` function. This is designed to allow custom certificates or proxies to be used with `fetch()`.

-   [close](../././~/Deno.HttpClient#method_close_0)

c

[Deno.Kv](../././~/Deno.Kv "Deno.Kv")

A key-value database that can be used to store and retrieve data.

-   [atomic](../././~/Deno.Kv#method_atomic_0)
-   [close](../././~/Deno.Kv#method_close_0)
-   [commitVersionstamp](../././~/Deno.Kv#method_commitversionstamp_0)
-   [delete](../././~/Deno.Kv#method_delete_0)
-   [enqueue](../././~/Deno.Kv#method_enqueue_0)
-   [get](../././~/Deno.Kv#method_get_0)
-   [getMany](../././~/Deno.Kv#method_getmany_0)
-   [list](../././~/Deno.Kv#method_list_0)
-   [listenQueue](../././~/Deno.Kv#method_listenqueue_0)
-   [set](../././~/Deno.Kv#method_set_0)
-   [watch](../././~/Deno.Kv#method_watch_0)

c

[Deno.KvListIterator](../././~/Deno.KvListIterator "Deno.KvListIterator")

An iterator over a range of data entries in a [`Deno.Kv`](../././~/Deno.Kv).

-   [cursor](../././~/Deno.KvListIterator#accessor_cursor)
-   [next](../././~/Deno.KvListIterator#method_next_0)

c

[Deno.KvU64](../././~/Deno.KvU64 "Deno.KvU64")

Wrapper type for 64-bit unsigned integers for use as values in a [`Deno.Kv`](../././~/Deno.Kv).

-   [value](../././~/Deno.KvU64#property_value)

c

[Deno.Permissions](../././~/Deno.Permissions "Deno.Permissions")

Deno's permission management API.

-   [query](../././~/Deno.Permissions#method_query_0)
-   [querySync](../././~/Deno.Permissions#method_querysync_0)
-   [request](../././~/Deno.Permissions#method_request_0)
-   [requestSync](../././~/Deno.Permissions#method_requestsync_0)
-   [revoke](../././~/Deno.Permissions#method_revoke_0)
-   [revokeSync](../././~/Deno.Permissions#method_revokesync_0)

c

[Deno.PermissionStatus](../././~/Deno.PermissionStatus "Deno.PermissionStatus")

An `EventTarget` returned from the [`Deno.permissions`](../././~/Deno.permissions) API which can provide updates to any state changes of the permission.

-   [addEventListener](../././~/Deno.PermissionStatus#method_addeventlistener_0)
-   [onchange](../././~/Deno.PermissionStatus#property_onchange)
-   [partial](../././~/Deno.PermissionStatus#property_partial)
-   [removeEventListener](../././~/Deno.PermissionStatus#method_removeeventlistener_0)
-   [state](../././~/Deno.PermissionStatus#property_state)

c

[Deno.QuicEndpoint](../././~/Deno.QuicEndpoint "Deno.QuicEndpoint")

No documentation available

-   [addr](../././~/Deno.QuicEndpoint#property_addr)
-   [close](../././~/Deno.QuicEndpoint#method_close_0)
-   [listen](../././~/Deno.QuicEndpoint#method_listen_0)

c

[Deno.UnsafeCallback](../././~/Deno.UnsafeCallback "Deno.UnsafeCallback")

An unsafe function pointer for passing JavaScript functions as C function pointers to foreign function calls.

-   [callback](../././~/Deno.UnsafeCallback#property_callback)
-   [close](../././~/Deno.UnsafeCallback#method_close_0)
-   [definition](../././~/Deno.UnsafeCallback#property_definition)
-   [pointer](../././~/Deno.UnsafeCallback#property_pointer)
-   [ref](../././~/Deno.UnsafeCallback#method_ref_0)
-   [threadSafe](../././~/Deno.UnsafeCallback#method_threadsafe_0)
-   [unref](../././~/Deno.UnsafeCallback#method_unref_0)

c

[Deno.UnsafeFnPointer](../././~/Deno.UnsafeFnPointer "Deno.UnsafeFnPointer")

An unsafe pointer to a function, for calling functions that are not present as symbols.

-   [call](../././~/Deno.UnsafeFnPointer#property_call)
-   [definition](../././~/Deno.UnsafeFnPointer#property_definition)
-   [pointer](../././~/Deno.UnsafeFnPointer#property_pointer)

c

[Deno.UnsafePointer](../././~/Deno.UnsafePointer "Deno.UnsafePointer")

A collection of static functions for interacting with pointer objects.

-   [create](../././~/Deno.UnsafePointer#method_create_0)
-   [equals](../././~/Deno.UnsafePointer#method_equals_0)
-   [of](../././~/Deno.UnsafePointer#method_of_0)
-   [offset](../././~/Deno.UnsafePointer#method_offset_0)
-   [value](../././~/Deno.UnsafePointer#method_value_0)

c

[Deno.UnsafePointerView](../././~/Deno.UnsafePointerView "Deno.UnsafePointerView")

An unsafe pointer view to a memory location as specified by the `pointer` value. The `UnsafePointerView` API follows the standard built in interface `DataView` for accessing the underlying types at an memory location (numbers, strings and raw bytes).

-   [copyInto](../././~/Deno.UnsafePointerView#method_copyinto_0)
-   [getArrayBuffer](../././~/Deno.UnsafePointerView#method_getarraybuffer_0)
-   [getBigInt64](../././~/Deno.UnsafePointerView#method_getbigint64_0)
-   [getBigUint64](../././~/Deno.UnsafePointerView#method_getbiguint64_0)
-   [getBool](../././~/Deno.UnsafePointerView#method_getbool_0)
-   [getCString](../././~/Deno.UnsafePointerView#method_getcstring_0)
-   [getFloat32](../././~/Deno.UnsafePointerView#method_getfloat32_0)
-   [getFloat64](../././~/Deno.UnsafePointerView#method_getfloat64_0)
-   [getInt16](../././~/Deno.UnsafePointerView#method_getint16_0)
-   [getInt32](../././~/Deno.UnsafePointerView#method_getint32_0)
-   [getInt8](../././~/Deno.UnsafePointerView#method_getint8_0)
-   [getPointer](../././~/Deno.UnsafePointerView#method_getpointer_0)
-   [getUint16](../././~/Deno.UnsafePointerView#method_getuint16_0)
-   [getUint32](../././~/Deno.UnsafePointerView#method_getuint32_0)
-   [getUint8](../././~/Deno.UnsafePointerView#method_getuint8_0)
-   [pointer](../././~/Deno.UnsafePointerView#property_pointer)

c

[Deno.UnsafeWindowSurface](../././~/Deno.UnsafeWindowSurface "Deno.UnsafeWindowSurface")

Creates a presentable WebGPU surface from given window and display handles.

-   [getContext](../././~/Deno.UnsafeWindowSurface#method_getcontext_0)
-   [present](../././~/Deno.UnsafeWindowSurface#method_present_0)
-   [resize](../././~/Deno.UnsafeWindowSurface#method_resize_0)

E

[Deno.SeekMode](../././~/Deno.SeekMode "Deno.SeekMode")

A enum which defines the seek mode for IO related APIs that support seeking.

f

[Deno.addSignalListener](../././~/Deno.addSignalListener "Deno.addSignalListener")

Registers the given function as a listener of the given signal event.

f

[Deno.bench](../././~/Deno.bench "Deno.bench")

Register a benchmark test which will be run when `deno bench` is used on the command line and the containing module looks like a bench module.

f

[Deno.chdir](../././~/Deno.chdir "Deno.chdir")

Change the current working directory to the specified path.

f

[Deno.chmod](../././~/Deno.chmod "Deno.chmod")

Changes the permission of a specific file/directory of specified path. Ignores the process's umask.

f

[Deno.chmodSync](../././~/Deno.chmodSync "Deno.chmodSync")

Synchronously changes the permission of a specific file/directory of specified path. Ignores the process's umask.

f

[Deno.chown](../././~/Deno.chown "Deno.chown")

Change owner of a regular file or directory.

f

[Deno.chownSync](../././~/Deno.chownSync "Deno.chownSync")

Synchronously change owner of a regular file or directory.

f

[Deno.connect](../././~/Deno.connect "Deno.connect")

Connects to the hostname (default is "127.0.0.1") and port on the named transport (default is "tcp"), and resolves to the connection (`Conn`).

f

[Deno.connectQuic](../././~/Deno.connectQuic "Deno.connectQuic")

Establishes a secure connection over QUIC using a hostname and port. The cert file is optional and if not included Mozilla's root certificates will be used. See also [https://github.com/ctz/webpki-roots](https://github.com/ctz/webpki-roots) for specifics.

f

[Deno.connectTls](../././~/Deno.connectTls "Deno.connectTls")

Establishes a secure connection over TLS (transport layer security) using an optional list of CA certs, hostname (default is "127.0.0.1") and port.

f

[Deno.consoleSize](../././~/Deno.consoleSize "Deno.consoleSize")

Gets the size of the console as columns/rows.

f

[Deno.copyFile](../././~/Deno.copyFile "Deno.copyFile")

Copies the contents and permissions of one file to another specified path, by default creating a new file if needed, else overwriting. Fails if target path is a directory or is unwritable.

f

[Deno.copyFileSync](../././~/Deno.copyFileSync "Deno.copyFileSync")

Synchronously copies the contents and permissions of one file to another specified path, by default creating a new file if needed, else overwriting. Fails if target path is a directory or is unwritable.

f

[Deno.create](../././~/Deno.create "Deno.create")

Creates a file if none exists or truncates an existing file and resolves to an instance of [`Deno.FsFile`](../././~/Deno.FsFile).

f

[Deno.createHttpClient](../././~/Deno.createHttpClient "Deno.createHttpClient")

Create a custom HttpClient to use with `fetch`. This is an extension of the web platform Fetch API which allows Deno to use custom TLS CA certificates and connect via a proxy while using `fetch()`.

f

[Deno.createSync](../././~/Deno.createSync "Deno.createSync")

Creates a file if none exists or truncates an existing file and returns an instance of [`Deno.FsFile`](../././~/Deno.FsFile).

f

[Deno.cron](../././~/Deno.cron "Deno.cron")

Create a cron job that will periodically execute the provided handler callback based on the specified schedule.

f

[Deno.cwd](../././~/Deno.cwd "Deno.cwd")

Return a string representing the current working directory.

f

[Deno.dlopen](../././~/Deno.dlopen "Deno.dlopen")

Opens an external dynamic library and registers symbols, making foreign functions available to be called.

f

[Deno.execPath](../././~/Deno.execPath "Deno.execPath")

Returns the path to the current deno executable.

f

[Deno.exit](../././~/Deno.exit "Deno.exit")

Exit the Deno process with optional exit code.

f

[Deno.gid](../././~/Deno.gid "Deno.gid")

Returns the group id of the process on POSIX platforms. Returns null on windows.

f

[Deno.hostname](../././~/Deno.hostname "Deno.hostname")

Get the `hostname` of the machine the Deno process is running on.

f

[Deno.inspect](../././~/Deno.inspect "Deno.inspect")

Converts the input into a string that has the same format as printed by `console.log()`.

f

[Deno.kill](../././~/Deno.kill "Deno.kill")

Send a signal to process under given `pid`. The value and meaning of the `signal` to the process is operating system and process dependant. [`Signal`](../././~/Deno.Signal) provides the most common signals. Default signal is `"SIGTERM"`.

f

[Deno.link](../././~/Deno.link "Deno.link")

Creates `newpath` as a hard link to `oldpath`.

f

[Deno.linkSync](../././~/Deno.linkSync "Deno.linkSync")

Synchronously creates `newpath` as a hard link to `oldpath`.

f

[Deno.listen](../././~/Deno.listen "Deno.listen")

Listen announces on the local transport address.

f

[Deno.listenDatagram](../././~/Deno.listenDatagram "Deno.listenDatagram")

Listen announces on the local transport address.

f

[Deno.listenTls](../././~/Deno.listenTls "Deno.listenTls")

Listen announces on the local transport address over TLS (transport layer security).

f

[Deno.loadavg](../././~/Deno.loadavg "Deno.loadavg")

Returns an array containing the 1, 5, and 15 minute load averages. The load average is a measure of CPU and IO utilization of the last one, five, and 15 minute periods expressed as a fractional number. Zero means there is no load. On Windows, the three values are always the same and represent the current load, not the 1, 5 and 15 minute load averages.

f

[Deno.lstat](../././~/Deno.lstat "Deno.lstat")

Resolves to a [`Deno.FileInfo`](../././~/Deno.FileInfo) for the specified `path`. If `path` is a symlink, information for the symlink will be returned instead of what it points to.

f

[Deno.lstatSync](../././~/Deno.lstatSync "Deno.lstatSync")

Synchronously returns a [`Deno.FileInfo`](../././~/Deno.FileInfo) for the specified `path`. If `path` is a symlink, information for the symlink will be returned instead of what it points to.

f

[Deno.makeTempDir](../././~/Deno.makeTempDir "Deno.makeTempDir")

Creates a new temporary directory in the default directory for temporary files, unless `dir` is specified. Other optional options include prefixing and suffixing the directory name with `prefix` and `suffix` respectively.

f

[Deno.makeTempDirSync](../././~/Deno.makeTempDirSync "Deno.makeTempDirSync")

Synchronously creates a new temporary directory in the default directory for temporary files, unless `dir` is specified. Other optional options include prefixing and suffixing the directory name with `prefix` and `suffix` respectively.

f

[Deno.makeTempFile](../././~/Deno.makeTempFile "Deno.makeTempFile")

Creates a new temporary file in the default directory for temporary files, unless `dir` is specified.

f

[Deno.makeTempFileSync](../././~/Deno.makeTempFileSync "Deno.makeTempFileSync")

Synchronously creates a new temporary file in the default directory for temporary files, unless `dir` is specified.

f

[Deno.memoryUsage](../././~/Deno.memoryUsage "Deno.memoryUsage")

Returns an object describing the memory usage of the Deno process and the V8 subsystem measured in bytes.

f

[Deno.mkdir](../././~/Deno.mkdir "Deno.mkdir")

Creates a new directory with the specified path.

f

[Deno.mkdirSync](../././~/Deno.mkdirSync "Deno.mkdirSync")

Synchronously creates a new directory with the specified path.

f

[Deno.networkInterfaces](../././~/Deno.networkInterfaces "Deno.networkInterfaces")

Returns an array of the network interface information.

f

[Deno.open](../././~/Deno.open "Deno.open")

Open a file and resolve to an instance of [`Deno.FsFile`](../././~/Deno.FsFile). The file does not need to previously exist if using the `create` or `createNew` open options. The caller may have the resulting file automatically closed by the runtime once it's out of scope by declaring the file variable with the `using` keyword.

f

[Deno.openKv](../././~/Deno.openKv "Deno.openKv")

Open a new [`Deno.Kv`](../././~/Deno.Kv) connection to persist data.

f

[Deno.openSync](../././~/Deno.openSync "Deno.openSync")

Synchronously open a file and return an instance of [`Deno.FsFile`](../././~/Deno.FsFile). The file does not need to previously exist if using the `create` or `createNew` open options. The caller may have the resulting file automatically closed by the runtime once it's out of scope by declaring the file variable with the `using` keyword.

f

[Deno.osRelease](../././~/Deno.osRelease "Deno.osRelease")

Returns the release version of the Operating System.

f

[Deno.osUptime](../././~/Deno.osUptime "Deno.osUptime")

Returns the Operating System uptime in number of seconds.

f

[Deno.readDir](../././~/Deno.readDir "Deno.readDir")

Reads the directory given by `path` and returns an async iterable of [`Deno.DirEntry`](../././~/Deno.DirEntry). The order of entries is not guaranteed.

f

[Deno.readDirSync](../././~/Deno.readDirSync "Deno.readDirSync")

Synchronously reads the directory given by `path` and returns an iterable of [`Deno.DirEntry`](../././~/Deno.DirEntry). The order of entries is not guaranteed.

f

[Deno.readFile](../././~/Deno.readFile "Deno.readFile")

Reads and resolves to the entire contents of a file as an array of bytes. `TextDecoder` can be used to transform the bytes to string if required. Rejects with an error when reading a directory.

f

[Deno.readFileSync](../././~/Deno.readFileSync "Deno.readFileSync")

Synchronously reads and returns the entire contents of a file as an array of bytes. `TextDecoder` can be used to transform the bytes to string if required. Throws an error when reading a directory.

f

[Deno.readLink](../././~/Deno.readLink "Deno.readLink")

Resolves to the full path destination of the named symbolic link.

f

[Deno.readLinkSync](../././~/Deno.readLinkSync "Deno.readLinkSync")

Synchronously returns the full path destination of the named symbolic link.

f

[Deno.readTextFile](../././~/Deno.readTextFile "Deno.readTextFile")

Asynchronously reads and returns the entire contents of a file as an UTF-8 decoded string. Reading a directory throws an error.

f

[Deno.readTextFileSync](../././~/Deno.readTextFileSync "Deno.readTextFileSync")

Synchronously reads and returns the entire contents of a file as an UTF-8 decoded string. Reading a directory throws an error.

f

[Deno.realPath](../././~/Deno.realPath "Deno.realPath")

Resolves to the absolute normalized path, with symbolic links resolved.

f

[Deno.realPathSync](../././~/Deno.realPathSync "Deno.realPathSync")

Synchronously returns absolute normalized path, with symbolic links resolved.

f

[Deno.refTimer](../././~/Deno.refTimer "Deno.refTimer")

Make the timer of the given `id` block the event loop from finishing.

f

[Deno.remove](../././~/Deno.remove "Deno.remove")

Removes the named file or directory.

f

[Deno.removeSignalListener](../././~/Deno.removeSignalListener "Deno.removeSignalListener")

Removes the given signal listener that has been registered with [`Deno.addSignalListener`](../././~/Deno.addSignalListener).

f

[Deno.removeSync](../././~/Deno.removeSync "Deno.removeSync")

Synchronously removes the named file or directory.

f

[Deno.rename](../././~/Deno.rename "Deno.rename")

Renames (moves) `oldpath` to `newpath`. Paths may be files or directories. If `newpath` already exists and is not a directory, `rename()` replaces it. OS-specific restrictions may apply when `oldpath` and `newpath` are in different directories.

f

[Deno.renameSync](../././~/Deno.renameSync "Deno.renameSync")

Synchronously renames (moves) `oldpath` to `newpath`. Paths may be files or directories. If `newpath` already exists and is not a directory, `renameSync()` replaces it. OS-specific restrictions may apply when `oldpath` and `newpath` are in different directories.

f

[Deno.resolveDns](../././~/Deno.resolveDns "Deno.resolveDns")

Performs DNS resolution against the given query, returning resolved records.

f

[Deno.serve](../././~/Deno.serve "Deno.serve")

Serves HTTP requests with the given handler.

f

[Deno.spawn](../././~/Deno.spawn "Deno.spawn")

Spawns a new subprocess, returning a [`Deno.ChildProcess`](../././~/Deno.ChildProcess) handle.

f

[Deno.spawnAndWait](../././~/Deno.spawnAndWait "Deno.spawnAndWait")

Spawns a subprocess, waits for it to finish, and returns the output.

f

[Deno.spawnAndWaitSync](../././~/Deno.spawnAndWaitSync "Deno.spawnAndWaitSync")

Synchronously spawns a subprocess, waits for it to finish, and returns the output.

f

[Deno.startTls](../././~/Deno.startTls "Deno.startTls")

Start TLS handshake from an existing connection using an optional list of CA certificates, and hostname (default is "127.0.0.1"). Specifying CA certs is optional. By default the configured root certificates are used. Using this function requires that the other end of the connection is prepared for a TLS handshake.

f

[Deno.stat](../././~/Deno.stat "Deno.stat")

Resolves to a [`Deno.FileInfo`](../././~/Deno.FileInfo) for the specified `path`. Will always follow symlinks.

f

[Deno.statSync](../././~/Deno.statSync "Deno.statSync")

Synchronously returns a [`Deno.FileInfo`](../././~/Deno.FileInfo) for the specified `path`. Will always follow symlinks.

f

[Deno.symlink](../././~/Deno.symlink "Deno.symlink")

Creates `newpath` as a symbolic link to `oldpath`.

f

[Deno.symlinkSync](../././~/Deno.symlinkSync "Deno.symlinkSync")

Creates `newpath` as a symbolic link to `oldpath`.

f

[Deno.systemMemoryInfo](../././~/Deno.systemMemoryInfo "Deno.systemMemoryInfo")

Displays the total amount of free and used physical and swap memory in the system, as well as the buffers and caches used by the kernel.

f

[Deno.truncate](../././~/Deno.truncate "Deno.truncate")

Truncates (or extends) the specified file, to reach the specified `len`. If `len` is not specified then the entire file contents are truncated.

f

[Deno.truncateSync](../././~/Deno.truncateSync "Deno.truncateSync")

Synchronously truncates (or extends) the specified file, to reach the specified `len`. If `len` is not specified then the entire file contents are truncated.

f

[Deno.uid](../././~/Deno.uid "Deno.uid")

Returns the user id of the process on POSIX platforms. Returns null on Windows.

f

[Deno.umask](../././~/Deno.umask "Deno.umask")

Retrieve the process umask. If `mask` is provided, sets the process umask. This call always returns what the umask was before the call.

f

[Deno.unrefTimer](../././~/Deno.unrefTimer "Deno.unrefTimer")

Make the timer of the given `id` not block the event loop from finishing.

f

[Deno.upgradeWebSocket](../././~/Deno.upgradeWebSocket "Deno.upgradeWebSocket")

Upgrade an incoming HTTP request to a WebSocket.

f

[Deno.upgradeWebTransport](../././~/Deno.upgradeWebTransport "Deno.upgradeWebTransport")

Upgrade a QUIC connection into a WebTransport instance.

f

[Deno.utime](../././~/Deno.utime "Deno.utime")

Changes the access (`atime`) and modification (`mtime`) times of a file system object referenced by `path`. Given times are either in seconds (UNIX epoch time) or as `Date` objects.

f

[Deno.utimeSync](../././~/Deno.utimeSync "Deno.utimeSync")

Synchronously changes the access (`atime`) and modification (`mtime`) times of a file system object referenced by `path`. Given times are either in seconds (UNIX epoch time) or as `Date` objects.

f

[Deno.watchFs](../././~/Deno.watchFs "Deno.watchFs")

Watch for file system events against one or more `paths`, which can be files or directories. These paths must exist already. One user action (e.g. `touch test.file`) can generate multiple file system events. Likewise, one user action can result in multiple file paths in one event (e.g. `mv old_name.txt new_name.txt`).

f

[Deno.writeFile](../././~/Deno.writeFile "Deno.writeFile")

Write `data` to the given `path`, by default creating a new file if needed, else overwriting.

f

[Deno.writeFileSync](../././~/Deno.writeFileSync "Deno.writeFileSync")

Synchronously write `data` to the given `path`, by default creating a new file if needed, else overwriting.

f

[Deno.writeTextFile](../././~/Deno.writeTextFile "Deno.writeTextFile")

Write string `data` to the given `path`, by default creating a new file if needed, else overwriting.

f

[Deno.writeTextFileSync](../././~/Deno.writeTextFileSync "Deno.writeTextFileSync")

Synchronously write string `data` to the given `path`, by default creating a new file if needed, else overwriting.

I

[Deno.AtomicCheck](../././~/Deno.AtomicCheck "Deno.AtomicCheck")

A check to perform as part of a [`Deno.AtomicOperation`](../././~/Deno.AtomicOperation). The check will fail if the versionstamp for the key-value pair in the KV store does not match the given versionstamp. A check with a `null` versionstamp checks that the key-value pair does not currently exist in the KV store.

-   [key](../././~/Deno.AtomicCheck#property_key)
-   [versionstamp](../././~/Deno.AtomicCheck#property_versionstamp)

I

[Deno.BasicAuth](../././~/Deno.BasicAuth "Deno.BasicAuth")

Basic authentication credentials to be used with a [`Deno.Proxy`](../././~/Deno.Proxy) server when specifying [`Deno.CreateHttpClientOptions`](../././~/Deno.CreateHttpClientOptions).

-   [password](../././~/Deno.BasicAuth#property_password)
-   [username](../././~/Deno.BasicAuth#property_username)

I

[Deno.BenchContext](../././~/Deno.BenchContext "Deno.BenchContext")

Context that is passed to a benchmarked function. The instance is shared between iterations of the benchmark. Its methods can be used for example to override of the measured portion of the function.

-   [end](../././~/Deno.BenchContext#method_end_0)
-   [name](../././~/Deno.BenchContext#property_name)
-   [origin](../././~/Deno.BenchContext#property_origin)
-   [start](../././~/Deno.BenchContext#method_start_0)

I

[Deno.BenchDefinition](../././~/Deno.BenchDefinition "Deno.BenchDefinition")

The interface for defining a benchmark test using [`Deno.bench`](../././~/Deno.bench).

-   [baseline](../././~/Deno.BenchDefinition#property_baseline)
-   [fn](../././~/Deno.BenchDefinition#property_fn)
-   [group](../././~/Deno.BenchDefinition#property_group)
-   [ignore](../././~/Deno.BenchDefinition#property_ignore)
-   [n](../././~/Deno.BenchDefinition#property_n)
-   [name](../././~/Deno.BenchDefinition#property_name)
-   [only](../././~/Deno.BenchDefinition#property_only)
-   [permissions](../././~/Deno.BenchDefinition#property_permissions)
-   [sanitizeExit](../././~/Deno.BenchDefinition#property_sanitizeexit)
-   [warmup](../././~/Deno.BenchDefinition#property_warmup)

I

[Deno.CaaRecord](../././~/Deno.CaaRecord "Deno.CaaRecord")

If [`Deno.resolveDns`](../././~/Deno.resolveDns) is called with `"CAA"` record type specified, it will resolve with an array of objects with this interface.

-   [critical](../././~/Deno.CaaRecord#property_critical)
-   [tag](../././~/Deno.CaaRecord#property_tag)
-   [value](../././~/Deno.CaaRecord#property_value)

I

[Deno.CommandOptions](../././~/Deno.CommandOptions "Deno.CommandOptions")

Options which can be set when calling [`Deno.Command`](../././~/Deno.Command).

-   [args](../././~/Deno.CommandOptions#property_args)
-   [clearEnv](../././~/Deno.CommandOptions#property_clearenv)
-   [cwd](../././~/Deno.CommandOptions#property_cwd)
-   [detached](../././~/Deno.CommandOptions#property_detached)
-   [env](../././~/Deno.CommandOptions#property_env)
-   [gid](../././~/Deno.CommandOptions#property_gid)
-   [signal](../././~/Deno.CommandOptions#property_signal)
-   [stderr](../././~/Deno.CommandOptions#property_stderr)
-   [stdin](../././~/Deno.CommandOptions#property_stdin)
-   [stdout](../././~/Deno.CommandOptions#property_stdout)
-   [uid](../././~/Deno.CommandOptions#property_uid)
-   [windowsRawArguments](../././~/Deno.CommandOptions#property_windowsrawarguments)

I

[Deno.CommandOutput](../././~/Deno.CommandOutput "Deno.CommandOutput")

The interface returned from calling `Deno.Command.output` or `Deno.Command.outputSync` which represents the result of spawning the child process.

-   [stderr](../././~/Deno.CommandOutput#property_stderr)
-   [stdout](../././~/Deno.CommandOutput#property_stdout)

I

[Deno.CommandStatus](../././~/Deno.CommandStatus "Deno.CommandStatus")

No documentation available

-   [code](../././~/Deno.CommandStatus#property_code)
-   [signal](../././~/Deno.CommandStatus#property_signal)
-   [success](../././~/Deno.CommandStatus#property_success)

I

[Deno.Conn](../././~/Deno.Conn "Deno.Conn")

No documentation available

-   [close](../././~/Deno.Conn#method_close_0)
-   [closeWrite](../././~/Deno.Conn#method_closewrite_0)
-   [localAddr](../././~/Deno.Conn#property_localaddr)
-   [read](../././~/Deno.Conn#method_read_0)
-   [readable](../././~/Deno.Conn#property_readable)
-   [ref](../././~/Deno.Conn#method_ref_0)
-   [remoteAddr](../././~/Deno.Conn#property_remoteaddr)
-   [unref](../././~/Deno.Conn#method_unref_0)
-   [writable](../././~/Deno.Conn#property_writable)
-   [write](../././~/Deno.Conn#method_write_0)

I

[Deno.ConnectOptions](../././~/Deno.ConnectOptions "Deno.ConnectOptions")

No documentation available

-   [hostname](../././~/Deno.ConnectOptions#property_hostname)
-   [port](../././~/Deno.ConnectOptions#property_port)
-   [signal](../././~/Deno.ConnectOptions#property_signal)
-   [transport](../././~/Deno.ConnectOptions#property_transport)

I

[Deno.ConnectQuicOptions](../././~/Deno.ConnectQuicOptions "Deno.ConnectQuicOptions")

No documentation available

-   [alpnProtocols](../././~/Deno.ConnectQuicOptions#property_alpnprotocols)
-   [caCerts](../././~/Deno.ConnectQuicOptions#property_cacerts)
-   [endpoint](../././~/Deno.ConnectQuicOptions#property_endpoint)
-   [hostname](../././~/Deno.ConnectQuicOptions#property_hostname)
-   [port](../././~/Deno.ConnectQuicOptions#property_port)
-   [serverName](../././~/Deno.ConnectQuicOptions#property_servername)
-   [zeroRtt](../././~/Deno.ConnectQuicOptions#property_zerortt)

I

[Deno.ConnectTlsOptions](../././~/Deno.ConnectTlsOptions "Deno.ConnectTlsOptions")

No documentation available

-   [alpnProtocols](../././~/Deno.ConnectTlsOptions#property_alpnprotocols)
-   [caCerts](../././~/Deno.ConnectTlsOptions#property_cacerts)
-   [hostname](../././~/Deno.ConnectTlsOptions#property_hostname)
-   [port](../././~/Deno.ConnectTlsOptions#property_port)
-   [unsafelyDisableHostnameVerification](../././~/Deno.ConnectTlsOptions#property_unsafelydisablehostnameverification)

I

[Deno.CreateHttpClientOptions](../././~/Deno.CreateHttpClientOptions "Deno.CreateHttpClientOptions")

The options used when creating a [`Deno.HttpClient`](../././~/Deno.HttpClient).

-   [allowHost](../././~/Deno.CreateHttpClientOptions#property_allowhost)
-   [caCerts](../././~/Deno.CreateHttpClientOptions#property_cacerts)
-   [http1](../././~/Deno.CreateHttpClientOptions#property_http1)
-   [http2](../././~/Deno.CreateHttpClientOptions#property_http2)
-   [localAddress](../././~/Deno.CreateHttpClientOptions#property_localaddress)
-   [poolIdleTimeout](../././~/Deno.CreateHttpClientOptions#property_poolidletimeout)
-   [poolMaxIdlePerHost](../././~/Deno.CreateHttpClientOptions#property_poolmaxidleperhost)
-   [proxy](../././~/Deno.CreateHttpClientOptions#property_proxy)

I

[Deno.CronSchedule](../././~/Deno.CronSchedule "Deno.CronSchedule")

CronSchedule is the interface used for JSON format cron `schedule`.

-   [dayOfMonth](../././~/Deno.CronSchedule#property_dayofmonth)
-   [dayOfWeek](../././~/Deno.CronSchedule#property_dayofweek)
-   [hour](../././~/Deno.CronSchedule#property_hour)
-   [minute](../././~/Deno.CronSchedule#property_minute)
-   [month](../././~/Deno.CronSchedule#property_month)

I

[Deno.DatagramConn](../././~/Deno.DatagramConn "Deno.DatagramConn")

A generic transport listener for message-oriented protocols.

-   [addr](../././~/Deno.DatagramConn#property_addr)
-   [close](../././~/Deno.DatagramConn#method_close_0)
-   [joinMulticastV4](../././~/Deno.DatagramConn#method_joinmulticastv4_0)
-   [joinMulticastV6](../././~/Deno.DatagramConn#method_joinmulticastv6_0)
-   [receive](../././~/Deno.DatagramConn#method_receive_0)
-   [send](../././~/Deno.DatagramConn#method_send_0)

I

[Deno.DenoTest](../././~/Deno.DenoTest "Deno.DenoTest")

No documentation available

-   [afterAll](../././~/Deno.DenoTest#method_afterall_0)
-   [afterEach](../././~/Deno.DenoTest#method_aftereach_0)
-   [beforeAll](../././~/Deno.DenoTest#method_beforeall_0)
-   [beforeEach](../././~/Deno.DenoTest#method_beforeeach_0)
-   [ignore](../././~/Deno.DenoTest#method_ignore_0)
-   [only](../././~/Deno.DenoTest#method_only_0)

I

[Deno.DirEntry](../././~/Deno.DirEntry "Deno.DirEntry")

Information about a directory entry returned from [`Deno.readDir`](../././~/Deno.readDir) and [`Deno.readDirSync`](../././~/Deno.readDirSync).

-   [isDirectory](../././~/Deno.DirEntry#property_isdirectory)
-   [isFile](../././~/Deno.DirEntry#property_isfile)
-   [isSymlink](../././~/Deno.DirEntry#property_issymlink)
-   [name](../././~/Deno.DirEntry#property_name)

I

[Deno.DynamicLibrary](../././~/Deno.DynamicLibrary "Deno.DynamicLibrary")

A dynamic library resource. Use [`Deno.dlopen`](../././~/Deno.dlopen) to load a dynamic library and return this interface.

-   [close](../././~/Deno.DynamicLibrary#method_close_0)
-   [symbols](../././~/Deno.DynamicLibrary#property_symbols)

I

[Deno.Env](../././~/Deno.Env "Deno.Env")

An interface containing methods to interact with the process environment variables.

-   [delete](../././~/Deno.Env#method_delete_0)
-   [get](../././~/Deno.Env#method_get_0)
-   [has](../././~/Deno.Env#method_has_0)
-   [set](../././~/Deno.Env#method_set_0)
-   [toObject](../././~/Deno.Env#method_toobject_0)

I

[Deno.EnvPermissionDescriptor](../././~/Deno.EnvPermissionDescriptor "Deno.EnvPermissionDescriptor")

The permission descriptor for the `allow-env` and `deny-env` permissions, which controls access to being able to read and write to the process environment variables as well as access other information about the environment. The option `variable` allows scoping the permission to a specific environment variable.

-   [name](../././~/Deno.EnvPermissionDescriptor#property_name)
-   [variable](../././~/Deno.EnvPermissionDescriptor#property_variable)

I

[Deno.FfiPermissionDescriptor](../././~/Deno.FfiPermissionDescriptor "Deno.FfiPermissionDescriptor")

The permission descriptor for the `allow-ffi` and `deny-ffi` permissions, which controls access to loading _foreign_ code and interfacing with it via the [Foreign Function Interface API](https://docs.deno.com/runtime/manual/runtime/ffi_api) available in Deno. The option `path` allows scoping the permission to a specific path on the host.

-   [name](../././~/Deno.FfiPermissionDescriptor#property_name)
-   [path](../././~/Deno.FfiPermissionDescriptor#property_path)

I

[Deno.FileInfo](../././~/Deno.FileInfo "Deno.FileInfo")

Provides information about a file and is returned by [`Deno.stat`](../././~/Deno.stat), [`Deno.lstat`](../././~/Deno.lstat), [`Deno.statSync`](../././~/Deno.statSync), and [`Deno.lstatSync`](../././~/Deno.lstatSync) or from calling `stat()` and `statSync()` on an [`Deno.FsFile`](../././~/Deno.FsFile) instance.

-   [atime](../././~/Deno.FileInfo#property_atime)
-   [birthtime](../././~/Deno.FileInfo#property_birthtime)
-   [blksize](../././~/Deno.FileInfo#property_blksize)
-   [blocks](../././~/Deno.FileInfo#property_blocks)
-   [ctime](../././~/Deno.FileInfo#property_ctime)
-   [dev](../././~/Deno.FileInfo#property_dev)
-   [gid](../././~/Deno.FileInfo#property_gid)
-   [ino](../././~/Deno.FileInfo#property_ino)
-   [isBlockDevice](../././~/Deno.FileInfo#property_isblockdevice)
-   [isCharDevice](../././~/Deno.FileInfo#property_ischardevice)
-   [isDirectory](../././~/Deno.FileInfo#property_isdirectory)
-   [isFifo](../././~/Deno.FileInfo#property_isfifo)
-   [isFile](../././~/Deno.FileInfo#property_isfile)
-   [isSocket](../././~/Deno.FileInfo#property_issocket)
-   [isSymlink](../././~/Deno.FileInfo#property_issymlink)
-   [mode](../././~/Deno.FileInfo#property_mode)
-   [mtime](../././~/Deno.FileInfo#property_mtime)
-   [nlink](../././~/Deno.FileInfo#property_nlink)
-   [rdev](../././~/Deno.FileInfo#property_rdev)
-   [size](../././~/Deno.FileInfo#property_size)
-   [uid](../././~/Deno.FileInfo#property_uid)

I

[Deno.ForeignFunction](../././~/Deno.ForeignFunction "Deno.ForeignFunction")

The interface for a foreign function as defined by its parameter and result types.

-   [name](../././~/Deno.ForeignFunction#property_name)
-   [nonblocking](../././~/Deno.ForeignFunction#property_nonblocking)
-   [optional](../././~/Deno.ForeignFunction#property_optional)
-   [parameters](../././~/Deno.ForeignFunction#property_parameters)
-   [result](../././~/Deno.ForeignFunction#property_result)

I

[Deno.ForeignLibraryInterface](../././~/Deno.ForeignLibraryInterface "Deno.ForeignLibraryInterface")

A foreign library interface descriptor.

I

[Deno.ForeignStatic](../././~/Deno.ForeignStatic "Deno.ForeignStatic")

No documentation available

-   [name](../././~/Deno.ForeignStatic#property_name)
-   [optional](../././~/Deno.ForeignStatic#property_optional)
-   [type](../././~/Deno.ForeignStatic#property_type)

I

[Deno.FsEvent](../././~/Deno.FsEvent "Deno.FsEvent")

Represents a unique file system event yielded by a [`Deno.FsWatcher`](../././~/Deno.FsWatcher).

-   [flag](../././~/Deno.FsEvent#property_flag)
-   [kind](../././~/Deno.FsEvent#property_kind)
-   [paths](../././~/Deno.FsEvent#property_paths)

I

[Deno.FsWatcher](../././~/Deno.FsWatcher "Deno.FsWatcher")

Returned by [`Deno.watchFs`](../././~/Deno.watchFs). It is an async iterator yielding up system events. To stop watching the file system by calling `.close()` method.

-   [close](../././~/Deno.FsWatcher#method_close_0)
-   [return](../././~/Deno.FsWatcher#method_return_0)

I

[Deno.HttpServer](../././~/Deno.HttpServer "Deno.HttpServer")

An instance of the server created using `Deno.serve()` API.

-   [addr](../././~/Deno.HttpServer#property_addr)
-   [finished](../././~/Deno.HttpServer#property_finished)
-   [ref](../././~/Deno.HttpServer#method_ref_0)
-   [shutdown](../././~/Deno.HttpServer#method_shutdown_0)
-   [unref](../././~/Deno.HttpServer#method_unref_0)

I

[Deno.ImportPermissionDescriptor](../././~/Deno.ImportPermissionDescriptor "Deno.ImportPermissionDescriptor")

The permission descriptor for the `allow-import` and `deny-import` permissions, which controls access to importing from remote hosts via the network. The option `host` allows scoping the permission for outbound connection to a specific host and port.

-   [host](../././~/Deno.ImportPermissionDescriptor#property_host)
-   [name](../././~/Deno.ImportPermissionDescriptor#property_name)

I

[Deno.InspectOptions](../././~/Deno.InspectOptions "Deno.InspectOptions")

Option which can be specified when performing [`Deno.inspect`](../././~/Deno.inspect).

-   [breakLength](../././~/Deno.InspectOptions#property_breaklength)
-   [colors](../././~/Deno.InspectOptions#property_colors)
-   [compact](../././~/Deno.InspectOptions#property_compact)
-   [depth](../././~/Deno.InspectOptions#property_depth)
-   [escapeSequences](../././~/Deno.InspectOptions#property_escapesequences)
-   [getters](../././~/Deno.InspectOptions#property_getters)
-   [iterableLimit](../././~/Deno.InspectOptions#property_iterablelimit)
-   [showHidden](../././~/Deno.InspectOptions#property_showhidden)
-   [showProxy](../././~/Deno.InspectOptions#property_showproxy)
-   [sorted](../././~/Deno.InspectOptions#property_sorted)
-   [strAbbreviateSize](../././~/Deno.InspectOptions#property_strabbreviatesize)
-   [trailingComma](../././~/Deno.InspectOptions#property_trailingcomma)

I

[Deno.KvCommitError](../././~/Deno.KvCommitError "Deno.KvCommitError")

No documentation available

-   [ok](../././~/Deno.KvCommitError#property_ok)

I

[Deno.KvCommitResult](../././~/Deno.KvCommitResult "Deno.KvCommitResult")

No documentation available

-   [ok](../././~/Deno.KvCommitResult#property_ok)
-   [versionstamp](../././~/Deno.KvCommitResult#property_versionstamp)

I

[Deno.KvEntry](../././~/Deno.KvEntry "Deno.KvEntry")

A versioned pair of key and value in a [`Deno.Kv`](../././~/Deno.Kv).

-   [key](../././~/Deno.KvEntry#property_key)
-   [value](../././~/Deno.KvEntry#property_value)
-   [versionstamp](../././~/Deno.KvEntry#property_versionstamp)

I

[Deno.KvListOptions](../././~/Deno.KvListOptions "Deno.KvListOptions")

Options for listing key-value pairs in a [`Deno.Kv`](../././~/Deno.Kv).

-   [batchSize](../././~/Deno.KvListOptions#property_batchsize)
-   [consistency](../././~/Deno.KvListOptions#property_consistency)
-   [cursor](../././~/Deno.KvListOptions#property_cursor)
-   [limit](../././~/Deno.KvListOptions#property_limit)
-   [reverse](../././~/Deno.KvListOptions#property_reverse)

I

[Deno.Listener](../././~/Deno.Listener "Deno.Listener")

A generic network listener for stream-oriented protocols.

-   [accept](../././~/Deno.Listener#method_accept_0)
-   [addr](../././~/Deno.Listener#property_addr)
-   [close](../././~/Deno.Listener#method_close_0)
-   [ref](../././~/Deno.Listener#method_ref_0)
-   [unref](../././~/Deno.Listener#method_unref_0)

I

[Deno.ListenOptions](../././~/Deno.ListenOptions "Deno.ListenOptions")

No documentation available

-   [hostname](../././~/Deno.ListenOptions#property_hostname)
-   [port](../././~/Deno.ListenOptions#property_port)
-   [tcpBacklog](../././~/Deno.ListenOptions#property_tcpbacklog)

I

[Deno.ListenTlsOptions](../././~/Deno.ListenTlsOptions "Deno.ListenTlsOptions")

No documentation available

-   [alpnProtocols](../././~/Deno.ListenTlsOptions#property_alpnprotocols)
-   [transport](../././~/Deno.ListenTlsOptions#property_transport)

I

[Deno.MakeTempOptions](../././~/Deno.MakeTempOptions "Deno.MakeTempOptions")

Options which can be set when using [`Deno.makeTempDir`](../././~/Deno.makeTempDir), [`Deno.makeTempDirSync`](../././~/Deno.makeTempDirSync), [`Deno.makeTempFile`](../././~/Deno.makeTempFile), and [`Deno.makeTempFileSync`](../././~/Deno.makeTempFileSync).

-   [dir](../././~/Deno.MakeTempOptions#property_dir)
-   [prefix](../././~/Deno.MakeTempOptions#property_prefix)
-   [suffix](../././~/Deno.MakeTempOptions#property_suffix)

I

[Deno.MemoryUsage](../././~/Deno.MemoryUsage "Deno.MemoryUsage")

No documentation available

-   [external](../././~/Deno.MemoryUsage#property_external)
-   [heapTotal](../././~/Deno.MemoryUsage#property_heaptotal)
-   [heapUsed](../././~/Deno.MemoryUsage#property_heapused)
-   [rss](../././~/Deno.MemoryUsage#property_rss)

I

[Deno.MkdirOptions](../././~/Deno.MkdirOptions "Deno.MkdirOptions")

Options which can be set when using [`Deno.mkdir`](../././~/Deno.mkdir) and [`Deno.mkdirSync`](../././~/Deno.mkdirSync).

-   [mode](../././~/Deno.MkdirOptions#property_mode)
-   [recursive](../././~/Deno.MkdirOptions#property_recursive)

I

[Deno.MulticastV4Membership](../././~/Deno.MulticastV4Membership "Deno.MulticastV4Membership")

Represents membership of a IPv4 multicast group.

-   [leave](../././~/Deno.MulticastV4Membership#property_leave)
-   [setLoopback](../././~/Deno.MulticastV4Membership#property_setloopback)
-   [setTTL](../././~/Deno.MulticastV4Membership#property_setttl)

I

[Deno.MulticastV6Membership](../././~/Deno.MulticastV6Membership "Deno.MulticastV6Membership")

Represents membership of a IPv6 multicast group.

-   [leave](../././~/Deno.MulticastV6Membership#property_leave)
-   [setLoopback](../././~/Deno.MulticastV6Membership#property_setloopback)

I

[Deno.MxRecord](../././~/Deno.MxRecord "Deno.MxRecord")

If [`Deno.resolveDns`](../././~/Deno.resolveDns) is called with `"MX"` record type specified, it will return an array of objects with this interface.

-   [exchange](../././~/Deno.MxRecord#property_exchange)
-   [preference](../././~/Deno.MxRecord#property_preference)

I

[Deno.NaptrRecord](../././~/Deno.NaptrRecord "Deno.NaptrRecord")

If [`Deno.resolveDns`](../././~/Deno.resolveDns) is called with `"NAPTR"` record type specified, it will return an array of objects with this interface.

-   [flags](../././~/Deno.NaptrRecord#property_flags)
-   [order](../././~/Deno.NaptrRecord#property_order)
-   [preference](../././~/Deno.NaptrRecord#property_preference)
-   [regexp](../././~/Deno.NaptrRecord#property_regexp)
-   [replacement](../././~/Deno.NaptrRecord#property_replacement)
-   [services](../././~/Deno.NaptrRecord#property_services)

I

[Deno.NativeStructType](../././~/Deno.NativeStructType "Deno.NativeStructType")

The native struct type for interfacing with foreign functions.

-   [struct](../././~/Deno.NativeStructType#property_struct)

I

[Deno.NetAddr](../././~/Deno.NetAddr "Deno.NetAddr")

No documentation available

-   [hostname](../././~/Deno.NetAddr#property_hostname)
-   [port](../././~/Deno.NetAddr#property_port)
-   [transport](../././~/Deno.NetAddr#property_transport)

I

[Deno.NetPermissionDescriptor](../././~/Deno.NetPermissionDescriptor "Deno.NetPermissionDescriptor")

The permission descriptor for the `allow-net` and `deny-net` permissions, which controls access to opening network ports and connecting to remote hosts via the network. The option `host` allows scoping the permission for outbound connection to a specific host and port.

-   [host](../././~/Deno.NetPermissionDescriptor#property_host)
-   [name](../././~/Deno.NetPermissionDescriptor#property_name)

I

[Deno.NetworkInterfaceInfo](../././~/Deno.NetworkInterfaceInfo "Deno.NetworkInterfaceInfo")

The information for a network interface returned from a call to [`Deno.networkInterfaces`](../././~/Deno.networkInterfaces).

-   [address](../././~/Deno.NetworkInterfaceInfo#property_address)
-   [cidr](../././~/Deno.NetworkInterfaceInfo#property_cidr)
-   [family](../././~/Deno.NetworkInterfaceInfo#property_family)
-   [mac](../././~/Deno.NetworkInterfaceInfo#property_mac)
-   [name](../././~/Deno.NetworkInterfaceInfo#property_name)
-   [netmask](../././~/Deno.NetworkInterfaceInfo#property_netmask)
-   [scopeid](../././~/Deno.NetworkInterfaceInfo#property_scopeid)

I

[Deno.OpenOptions](../././~/Deno.OpenOptions "Deno.OpenOptions")

Options which can be set when doing [`Deno.open`](../././~/Deno.open) and [`Deno.openSync`](../././~/Deno.openSync).

-   [append](../././~/Deno.OpenOptions#property_append)
-   [create](../././~/Deno.OpenOptions#property_create)
-   [createNew](../././~/Deno.OpenOptions#property_createnew)
-   [mode](../././~/Deno.OpenOptions#property_mode)
-   [read](../././~/Deno.OpenOptions#property_read)
-   [truncate](../././~/Deno.OpenOptions#property_truncate)
-   [write](../././~/Deno.OpenOptions#property_write)

I

[Deno.PermissionOptionsObject](../././~/Deno.PermissionOptionsObject "Deno.PermissionOptionsObject")

A set of options which can define the permissions within a test or worker context at a highly specific level.

-   [env](../././~/Deno.PermissionOptionsObject#property_env)
-   [ffi](../././~/Deno.PermissionOptionsObject#property_ffi)
-   [import](../././~/Deno.PermissionOptionsObject#property_import)
-   [net](../././~/Deno.PermissionOptionsObject#property_net)
-   [read](../././~/Deno.PermissionOptionsObject#property_read)
-   [run](../././~/Deno.PermissionOptionsObject#property_run)
-   [sys](../././~/Deno.PermissionOptionsObject#property_sys)
-   [write](../././~/Deno.PermissionOptionsObject#property_write)

I

[Deno.PermissionStatusEventMap](../././~/Deno.PermissionStatusEventMap "Deno.PermissionStatusEventMap")

The interface which defines what event types are supported by [`PermissionStatus`](../././~/Deno.PermissionStatus) instances.

-   [change](../././~/Deno.PermissionStatusEventMap#property_change)

I

[Deno.PointerObject](../././~/Deno.PointerObject "Deno.PointerObject")

A non-null pointer, represented as an object at runtime. The object's prototype is `null` and cannot be changed. The object cannot be assigned to either and is thus entirely read-only.

-   [brand](../././~/Deno.PointerObject#property_brand)

I

[Deno.QuicAcceptOptions](../././~/Deno.QuicAcceptOptions "Deno.QuicAcceptOptions")

No documentation available

-   [alpnProtocols](../././~/Deno.QuicAcceptOptions#property_alpnprotocols)
-   [zeroRtt](../././~/Deno.QuicAcceptOptions#property_zerortt)

I

[Deno.QuicBidirectionalStream](../././~/Deno.QuicBidirectionalStream "Deno.QuicBidirectionalStream")

No documentation available

-   [readable](../././~/Deno.QuicBidirectionalStream#property_readable)
-   [writable](../././~/Deno.QuicBidirectionalStream#property_writable)

I

[Deno.QuicCloseInfo](../././~/Deno.QuicCloseInfo "Deno.QuicCloseInfo")

No documentation available

-   [closeCode](../././~/Deno.QuicCloseInfo#property_closecode)
-   [reason](../././~/Deno.QuicCloseInfo#property_reason)

I

[Deno.QuicConn](../././~/Deno.QuicConn "Deno.QuicConn")

No documentation available

-   [close](../././~/Deno.QuicConn#method_close_0)
-   [closed](../././~/Deno.QuicConn#property_closed)
-   [createBidirectionalStream](../././~/Deno.QuicConn#method_createbidirectionalstream_0)
-   [createUnidirectionalStream](../././~/Deno.QuicConn#method_createunidirectionalstream_0)
-   [endpoint](../././~/Deno.QuicConn#property_endpoint)
-   [handshake](../././~/Deno.QuicConn#property_handshake)
-   [incomingBidirectionalStreams](../././~/Deno.QuicConn#property_incomingbidirectionalstreams)
-   [incomingUnidirectionalStreams](../././~/Deno.QuicConn#property_incomingunidirectionalstreams)
-   [maxDatagramSize](../././~/Deno.QuicConn#property_maxdatagramsize)
-   [protocol](../././~/Deno.QuicConn#property_protocol)
-   [readDatagram](../././~/Deno.QuicConn#method_readdatagram_0)
-   [remoteAddr](../././~/Deno.QuicConn#property_remoteaddr)
-   [sendDatagram](../././~/Deno.QuicConn#method_senddatagram_0)
-   [serverName](../././~/Deno.QuicConn#property_servername)

I

[Deno.QuicEndpointOptions](../././~/Deno.QuicEndpointOptions "Deno.QuicEndpointOptions")

No documentation available

-   [hostname](../././~/Deno.QuicEndpointOptions#property_hostname)
-   [port](../././~/Deno.QuicEndpointOptions#property_port)

I

[Deno.QuicIncoming](../././~/Deno.QuicIncoming "Deno.QuicIncoming")

An incoming connection for which the server has not yet begun its part of the handshake.

-   [accept](../././~/Deno.QuicIncoming#method_accept_0)
-   [ignore](../././~/Deno.QuicIncoming#method_ignore_0)
-   [localIp](../././~/Deno.QuicIncoming#property_localip)
-   [refuse](../././~/Deno.QuicIncoming#method_refuse_0)
-   [remoteAddr](../././~/Deno.QuicIncoming#property_remoteaddr)
-   [remoteAddressValidated](../././~/Deno.QuicIncoming#property_remoteaddressvalidated)

I

[Deno.QuicListener](../././~/Deno.QuicListener "Deno.QuicListener")

Specialized listener that accepts QUIC connections.

-   [accept](../././~/Deno.QuicListener#method_accept_0)
-   [endpoint](../././~/Deno.QuicListener#property_endpoint)
-   [incoming](../././~/Deno.QuicListener#method_incoming_0)
-   [stop](../././~/Deno.QuicListener#method_stop_0)

I

[Deno.QuicListenOptions](../././~/Deno.QuicListenOptions "Deno.QuicListenOptions")

No documentation available

-   [alpnProtocols](../././~/Deno.QuicListenOptions#property_alpnprotocols)
-   [cert](../././~/Deno.QuicListenOptions#property_cert)
-   [key](../././~/Deno.QuicListenOptions#property_key)

I

[Deno.QuicReceiveStream](../././~/Deno.QuicReceiveStream "Deno.QuicReceiveStream")

No documentation available

-   [id](../././~/Deno.QuicReceiveStream#property_id)

I

[Deno.QuicSendStream](../././~/Deno.QuicSendStream "Deno.QuicSendStream")

No documentation available

-   [id](../././~/Deno.QuicSendStream#property_id)
-   [sendOrder](../././~/Deno.QuicSendStream#property_sendorder)

I

[Deno.QuicSendStreamOptions](../././~/Deno.QuicSendStreamOptions "Deno.QuicSendStreamOptions")

No documentation available

-   [sendOrder](../././~/Deno.QuicSendStreamOptions#property_sendorder)
-   [waitUntilAvailable](../././~/Deno.QuicSendStreamOptions#property_waituntilavailable)

I

[Deno.QuicServerTransportOptions](../././~/Deno.QuicServerTransportOptions "Deno.QuicServerTransportOptions")

No documentation available

-   [preferredAddressV4](../././~/Deno.QuicServerTransportOptions#property_preferredaddressv4)
-   [preferredAddressV6](../././~/Deno.QuicServerTransportOptions#property_preferredaddressv6)

I

[Deno.QuicTransportOptions](../././~/Deno.QuicTransportOptions "Deno.QuicTransportOptions")

No documentation available

-   [congestionControl](../././~/Deno.QuicTransportOptions#property_congestioncontrol)
-   [keepAliveInterval](../././~/Deno.QuicTransportOptions#property_keepaliveinterval)
-   [maxConcurrentBidirectionalStreams](../././~/Deno.QuicTransportOptions#property_maxconcurrentbidirectionalstreams)
-   [maxConcurrentUnidirectionalStreams](../././~/Deno.QuicTransportOptions#property_maxconcurrentunidirectionalstreams)
-   [maxIdleTimeout](../././~/Deno.QuicTransportOptions#property_maxidletimeout)

I

[Deno.ReadFileOptions](../././~/Deno.ReadFileOptions "Deno.ReadFileOptions")

Options which can be set when using [`Deno.readFile`](../././~/Deno.readFile) or [`Deno.readFileSync`](../././~/Deno.readFileSync).

-   [signal](../././~/Deno.ReadFileOptions#property_signal)

I

[Deno.ReadPermissionDescriptor](../././~/Deno.ReadPermissionDescriptor "Deno.ReadPermissionDescriptor")

The permission descriptor for the `allow-read` and `deny-read` permissions, which controls access to reading resources from the local host. The option `path` allows scoping the permission to a specific path (and if the path is a directory any sub paths).

-   [name](../././~/Deno.ReadPermissionDescriptor#property_name)
-   [path](../././~/Deno.ReadPermissionDescriptor#property_path)

I

[Deno.RemoveOptions](../././~/Deno.RemoveOptions "Deno.RemoveOptions")

Options which can be set when using [`Deno.remove`](../././~/Deno.remove) and [`Deno.removeSync`](../././~/Deno.removeSync).

-   [recursive](../././~/Deno.RemoveOptions#property_recursive)

I

[Deno.ResolveDnsOptions](../././~/Deno.ResolveDnsOptions "Deno.ResolveDnsOptions")

Options which can be set when using [`Deno.resolveDns`](../././~/Deno.resolveDns).

-   [nameServer](../././~/Deno.ResolveDnsOptions#property_nameserver)
-   [signal](../././~/Deno.ResolveDnsOptions#property_signal)

I

[Deno.RunPermissionDescriptor](../././~/Deno.RunPermissionDescriptor "Deno.RunPermissionDescriptor")

The permission descriptor for the `allow-run` and `deny-run` permissions, which controls access to what sub-processes can be executed by Deno. The option `command` allows scoping the permission to a specific executable.

-   [command](../././~/Deno.RunPermissionDescriptor#property_command)
-   [name](../././~/Deno.RunPermissionDescriptor#property_name)

I

[Deno.ServeDefaultExport](../././~/Deno.ServeDefaultExport "Deno.ServeDefaultExport")

Interface that module run with `deno serve` subcommand must conform to.

-   [fetch](../././~/Deno.ServeDefaultExport#property_fetch)
-   [onListen](../././~/Deno.ServeDefaultExport#property_onlisten)

I

[Deno.ServeHandlerInfo](../././~/Deno.ServeHandlerInfo "Deno.ServeHandlerInfo")

Additional information for an HTTP request and its connection.

-   [completed](../././~/Deno.ServeHandlerInfo#property_completed)
-   [remoteAddr](../././~/Deno.ServeHandlerInfo#property_remoteaddr)

I

[Deno.ServeInit](../././~/Deno.ServeInit "Deno.ServeInit")

No documentation available

-   [handler](../././~/Deno.ServeInit#property_handler)

I

[Deno.ServeOptions](../././~/Deno.ServeOptions "Deno.ServeOptions")

Options which can be set when calling [`Deno.serve`](../././~/Deno.serve).

-   [onError](../././~/Deno.ServeOptions#property_onerror)
-   [onListen](../././~/Deno.ServeOptions#property_onlisten)
-   [signal](../././~/Deno.ServeOptions#property_signal)

I

[Deno.ServeTcpOptions](../././~/Deno.ServeTcpOptions "Deno.ServeTcpOptions")

Options that can be passed to `Deno.serve` to create a server listening on a TCP port.

-   [hostname](../././~/Deno.ServeTcpOptions#property_hostname)
-   [port](../././~/Deno.ServeTcpOptions#property_port)
-   [reusePort](../././~/Deno.ServeTcpOptions#property_reuseport)
-   [tcpBacklog](../././~/Deno.ServeTcpOptions#property_tcpbacklog)
-   [transport](../././~/Deno.ServeTcpOptions#property_transport)

I

[Deno.ServeUnixOptions](../././~/Deno.ServeUnixOptions "Deno.ServeUnixOptions")

Options that can be passed to `Deno.serve` to create a server listening on a Unix domain socket.

-   [path](../././~/Deno.ServeUnixOptions#property_path)
-   [transport](../././~/Deno.ServeUnixOptions#property_transport)

I

[Deno.ServeVsockOptions](../././~/Deno.ServeVsockOptions "Deno.ServeVsockOptions")

Options that can be passed to `Deno.serve` to create a server listening on a VSOCK socket.

-   [cid](../././~/Deno.ServeVsockOptions#property_cid)
-   [port](../././~/Deno.ServeVsockOptions#property_port)
-   [transport](../././~/Deno.ServeVsockOptions#property_transport)

I

[Deno.SetRawOptions](../././~/Deno.SetRawOptions "Deno.SetRawOptions")

No documentation available

-   [cbreak](../././~/Deno.SetRawOptions#property_cbreak)

I

[Deno.SoaRecord](../././~/Deno.SoaRecord "Deno.SoaRecord")

If [`Deno.resolveDns`](../././~/Deno.resolveDns) is called with `"SOA"` record type specified, it will return an array of objects with this interface.

-   [expire](../././~/Deno.SoaRecord#property_expire)
-   [minimum](../././~/Deno.SoaRecord#property_minimum)
-   [mname](../././~/Deno.SoaRecord#property_mname)
-   [refresh](../././~/Deno.SoaRecord#property_refresh)
-   [retry](../././~/Deno.SoaRecord#property_retry)
-   [rname](../././~/Deno.SoaRecord#property_rname)
-   [serial](../././~/Deno.SoaRecord#property_serial)

I

[Deno.SrvRecord](../././~/Deno.SrvRecord "Deno.SrvRecord")

If [`Deno.resolveDns`](../././~/Deno.resolveDns) is called with `"SRV"` record type specified, it will return an array of objects with this interface.

-   [port](../././~/Deno.SrvRecord#property_port)
-   [priority](../././~/Deno.SrvRecord#property_priority)
-   [target](../././~/Deno.SrvRecord#property_target)
-   [weight](../././~/Deno.SrvRecord#property_weight)

I

[Deno.StartTlsOptions](../././~/Deno.StartTlsOptions "Deno.StartTlsOptions")

No documentation available

-   [alpnProtocols](../././~/Deno.StartTlsOptions#property_alpnprotocols)
-   [caCerts](../././~/Deno.StartTlsOptions#property_cacerts)
-   [hostname](../././~/Deno.StartTlsOptions#property_hostname)
-   [unsafelyDisableHostnameVerification](../././~/Deno.StartTlsOptions#property_unsafelydisablehostnameverification)

I

[Deno.SubprocessReadableStream](../././~/Deno.SubprocessReadableStream "Deno.SubprocessReadableStream")

The interface for stdout and stderr streams for child process returned from `Deno.Command.spawn`.

-   [arrayBuffer](../././~/Deno.SubprocessReadableStream#method_arraybuffer_0)
-   [bytes](../././~/Deno.SubprocessReadableStream#method_bytes_0)
-   [json](../././~/Deno.SubprocessReadableStream#method_json_0)
-   [text](../././~/Deno.SubprocessReadableStream#method_text_0)

I

[Deno.SymlinkOptions](../././~/Deno.SymlinkOptions "Deno.SymlinkOptions")

Options that can be used with [`symlink`](../././~/Deno.symlink) and [`symlinkSync`](../././~/Deno.symlinkSync).

-   [type](../././~/Deno.SymlinkOptions#property_type)

I

[Deno.SysPermissionDescriptor](../././~/Deno.SysPermissionDescriptor "Deno.SysPermissionDescriptor")

The permission descriptor for the `allow-sys` and `deny-sys` permissions, which controls access to sensitive host system information, which malicious code might attempt to exploit. The option `kind` allows scoping the permission to a specific piece of information.

-   [kind](../././~/Deno.SysPermissionDescriptor#property_kind)
-   [name](../././~/Deno.SysPermissionDescriptor#property_name)

I

[Deno.SystemMemoryInfo](../././~/Deno.SystemMemoryInfo "Deno.SystemMemoryInfo")

Information returned from a call to [`Deno.systemMemoryInfo`](../././~/Deno.systemMemoryInfo).

-   [available](../././~/Deno.SystemMemoryInfo#property_available)
-   [buffers](../././~/Deno.SystemMemoryInfo#property_buffers)
-   [cached](../././~/Deno.SystemMemoryInfo#property_cached)
-   [free](../././~/Deno.SystemMemoryInfo#property_free)
-   [swapFree](../././~/Deno.SystemMemoryInfo#property_swapfree)
-   [swapTotal](../././~/Deno.SystemMemoryInfo#property_swaptotal)
-   [total](../././~/Deno.SystemMemoryInfo#property_total)

I

[Deno.TcpConn](../././~/Deno.TcpConn "Deno.TcpConn")

No documentation available

-   [setKeepAlive](../././~/Deno.TcpConn#method_setkeepalive_0)
-   [setNoDelay](../././~/Deno.TcpConn#method_setnodelay_0)

I

[Deno.TcpListenOptions](../././~/Deno.TcpListenOptions "Deno.TcpListenOptions")

No documentation available

-   [reusePort](../././~/Deno.TcpListenOptions#property_reuseport)

I

[Deno.TestContext](../././~/Deno.TestContext "Deno.TestContext")

Context that is passed to a testing function, which can be used to either gain information about the current test, or register additional test steps within the current test.

-   [name](../././~/Deno.TestContext#property_name)
-   [origin](../././~/Deno.TestContext#property_origin)
-   [parent](../././~/Deno.TestContext#property_parent)
-   [step](../././~/Deno.TestContext#method_step_0)

I

[Deno.TestDefinition](../././~/Deno.TestDefinition "Deno.TestDefinition")

No documentation available

-   [fn](../././~/Deno.TestDefinition#property_fn)
-   [ignore](../././~/Deno.TestDefinition#property_ignore)
-   [name](../././~/Deno.TestDefinition#property_name)
-   [only](../././~/Deno.TestDefinition#property_only)
-   [permissions](../././~/Deno.TestDefinition#property_permissions)
-   [sanitizeExit](../././~/Deno.TestDefinition#property_sanitizeexit)
-   [sanitizeOps](../././~/Deno.TestDefinition#property_sanitizeops)
-   [sanitizeResources](../././~/Deno.TestDefinition#property_sanitizeresources)

I

[Deno.TestStepDefinition](../././~/Deno.TestStepDefinition "Deno.TestStepDefinition")

No documentation available

-   [fn](../././~/Deno.TestStepDefinition#property_fn)
-   [ignore](../././~/Deno.TestStepDefinition#property_ignore)
-   [name](../././~/Deno.TestStepDefinition#property_name)
-   [sanitizeExit](../././~/Deno.TestStepDefinition#property_sanitizeexit)
-   [sanitizeOps](../././~/Deno.TestStepDefinition#property_sanitizeops)
-   [sanitizeResources](../././~/Deno.TestStepDefinition#property_sanitizeresources)

I

[Deno.TlsCertifiedKeyPem](../././~/Deno.TlsCertifiedKeyPem "Deno.TlsCertifiedKeyPem")

Provides certified key material from strings. The key material is provided in `PEM`\-format (Privacy Enhanced Mail, [https://www.rfc-editor.org/rfc/rfc1422](https://www.rfc-editor.org/rfc/rfc1422)) which can be identified by having `-----BEGIN-----` and `-----END-----` markers at the beginning and end of the strings. This type of key is not compatible with `DER`\-format keys which are binary.

-   [cert](../././~/Deno.TlsCertifiedKeyPem#property_cert)
-   [key](../././~/Deno.TlsCertifiedKeyPem#property_key)
-   [keyFormat](../././~/Deno.TlsCertifiedKeyPem#property_keyformat)

I

[Deno.TlsConn](../././~/Deno.TlsConn "Deno.TlsConn")

No documentation available

-   [handshake](../././~/Deno.TlsConn#method_handshake_0)

I

[Deno.TlsHandshakeInfo](../././~/Deno.TlsHandshakeInfo "Deno.TlsHandshakeInfo")

No documentation available

-   [alpnProtocol](../././~/Deno.TlsHandshakeInfo#property_alpnprotocol)

I

[Deno.UdpListenOptions](../././~/Deno.UdpListenOptions "Deno.UdpListenOptions")

Unstable options which can be set when opening a datagram listener via [`Deno.listenDatagram`](../././~/Deno.listenDatagram).

-   [loopback](../././~/Deno.UdpListenOptions#property_loopback)
-   [reuseAddress](../././~/Deno.UdpListenOptions#property_reuseaddress)

I

[Deno.UnixAddr](../././~/Deno.UnixAddr "Deno.UnixAddr")

No documentation available

-   [path](../././~/Deno.UnixAddr#property_path)
-   [transport](../././~/Deno.UnixAddr#property_transport)

I

[Deno.UnixConn](../././~/Deno.UnixConn "Deno.UnixConn")

No documentation available

I

[Deno.UnixConnectOptions](../././~/Deno.UnixConnectOptions "Deno.UnixConnectOptions")

No documentation available

-   [path](../././~/Deno.UnixConnectOptions#property_path)
-   [transport](../././~/Deno.UnixConnectOptions#property_transport)

I

[Deno.UnixListenOptions](../././~/Deno.UnixListenOptions "Deno.UnixListenOptions")

Options which can be set when opening a Unix listener via [`Deno.listen`](../././~/Deno.listen) or [`Deno.listenDatagram`](../././~/Deno.listenDatagram).

-   [path](../././~/Deno.UnixListenOptions#property_path)

I

[Deno.UnsafeCallbackDefinition](../././~/Deno.UnsafeCallbackDefinition "Deno.UnsafeCallbackDefinition")

Definition of a unsafe callback function.

-   [parameters](../././~/Deno.UnsafeCallbackDefinition#property_parameters)
-   [result](../././~/Deno.UnsafeCallbackDefinition#property_result)

I

[Deno.UpgradeWebSocketOptions](../././~/Deno.UpgradeWebSocketOptions "Deno.UpgradeWebSocketOptions")

Options which can be set when performing a [`Deno.upgradeWebSocket`](../././~/Deno.upgradeWebSocket) upgrade of a `Request`

-   [idleTimeout](../././~/Deno.UpgradeWebSocketOptions#property_idletimeout)
-   [protocol](../././~/Deno.UpgradeWebSocketOptions#property_protocol)

I

[Deno.VsockAddr](../././~/Deno.VsockAddr "Deno.VsockAddr")

No documentation available

-   [cid](../././~/Deno.VsockAddr#property_cid)
-   [port](../././~/Deno.VsockAddr#property_port)
-   [transport](../././~/Deno.VsockAddr#property_transport)

I

[Deno.VsockConn](../././~/Deno.VsockConn "Deno.VsockConn")

No documentation available

I

[Deno.VsockConnectOptions](../././~/Deno.VsockConnectOptions "Deno.VsockConnectOptions")

No documentation available

-   [cid](../././~/Deno.VsockConnectOptions#property_cid)
-   [port](../././~/Deno.VsockConnectOptions#property_port)
-   [transport](../././~/Deno.VsockConnectOptions#property_transport)

I

[Deno.VsockListenOptions](../././~/Deno.VsockListenOptions "Deno.VsockListenOptions")

Options which can be set when opening a VSOCK listener via [`Deno.listen`](../././~/Deno.listen).

-   [cid](../././~/Deno.VsockListenOptions#property_cid)
-   [port](../././~/Deno.VsockListenOptions#property_port)

I

[Deno.WebSocketUpgrade](../././~/Deno.WebSocketUpgrade "Deno.WebSocketUpgrade")

The object that is returned from a [`Deno.upgradeWebSocket`](../././~/Deno.upgradeWebSocket) request.

-   [response](../././~/Deno.WebSocketUpgrade#property_response)
-   [socket](../././~/Deno.WebSocketUpgrade#property_socket)

I

[Deno.WriteFileOptions](../././~/Deno.WriteFileOptions "Deno.WriteFileOptions")

Options for writing to a file.

-   [append](../././~/Deno.WriteFileOptions#property_append)
-   [create](../././~/Deno.WriteFileOptions#property_create)
-   [createNew](../././~/Deno.WriteFileOptions#property_createnew)
-   [mode](../././~/Deno.WriteFileOptions#property_mode)
-   [signal](../././~/Deno.WriteFileOptions#property_signal)

I

[Deno.WritePermissionDescriptor](../././~/Deno.WritePermissionDescriptor "Deno.WritePermissionDescriptor")

The permission descriptor for the `allow-write` and `deny-write` permissions, which controls access to writing to resources from the local host. The option `path` allow scoping the permission to a specific path (and if the path is a directory any sub paths).

-   [name](../././~/Deno.WritePermissionDescriptor#property_name)
-   [path](../././~/Deno.WritePermissionDescriptor#property_path)

f

N

[Deno.bundle](../././~/Deno.bundle "Deno.bundle")

Bundle Typescript/Javascript code

N

[Deno.errors](../././~/Deno.errors "Deno.errors")

A set of error constructors that are raised by Deno APIs.

N

[Deno.jupyter](../././~/Deno.jupyter "Deno.jupyter")

A namespace containing runtime APIs available in Jupyter notebooks.

N

[Deno.lint](../././~/Deno.lint "Deno.lint")

No documentation available

N

[Deno.telemetry](../././~/Deno.telemetry "Deno.telemetry")

APIs for working with the OpenTelemetry observability framework. Deno can export traces, metrics, and logs to OpenTelemetry compatible backends via the OTLP protocol.

N

[Deno.webgpu](../././~/Deno.webgpu "Deno.webgpu")

The webgpu namespace provides additional APIs that the WebGPU specification does not specify.

T

[Deno.Addr](../././~/Deno.Addr "Deno.Addr")

No documentation available

T

[Deno.ConditionalAsync](../././~/Deno.ConditionalAsync "Deno.ConditionalAsync")

No documentation available

T

[Deno.CronScheduleExpression](../././~/Deno.CronScheduleExpression "Deno.CronScheduleExpression")

CronScheduleExpression is used as the type of `minute`, `hour`, `dayOfMonth`, `month`, and `dayOfWeek` in [`CronSchedule`](../././~/Deno.CronSchedule).

T

[Deno.FromForeignFunction](../././~/Deno.FromForeignFunction "Deno.FromForeignFunction")

No documentation available

T

[Deno.FromNativeParameterTypes](../././~/Deno.FromNativeParameterTypes "Deno.FromNativeParameterTypes")

No documentation available

T

[Deno.FromNativeResultType](../././~/Deno.FromNativeResultType "Deno.FromNativeResultType")

Type conversion for foreign symbol return types.

T

[Deno.FromNativeType](../././~/Deno.FromNativeType "Deno.FromNativeType")

Type conversion for foreign symbol return types and unsafe callback parameters.

T

[Deno.FsEventFlag](../././~/Deno.FsEventFlag "Deno.FsEventFlag")

Additional information for FsEvent objects with the "other" kind.

T

[Deno.KvConsistencyLevel](../././~/Deno.KvConsistencyLevel "Deno.KvConsistencyLevel")

Consistency level of a KV operation.

T

[Deno.KvEntryMaybe](../././~/Deno.KvEntryMaybe "Deno.KvEntryMaybe")

An optional versioned pair of key and value in a [`Deno.Kv`](../././~/Deno.Kv).

T

[Deno.KvKey](../././~/Deno.KvKey "Deno.KvKey")

A key to be persisted in a [`Deno.Kv`](../././~/Deno.Kv). A key is a sequence of [`Deno.KvKeyPart`](../././~/Deno.KvKeyPart)s.

T

[Deno.KvKeyPart](../././~/Deno.KvKeyPart "Deno.KvKeyPart")

A single part of a [`Deno.KvKey`](../././~/Deno.KvKey). Parts are ordered lexicographically, first by their type, and within a given type by their value.

T

[Deno.KvListSelector](../././~/Deno.KvListSelector "Deno.KvListSelector")

A selector that selects the range of data returned by a list operation on a [`Deno.Kv`](../././~/Deno.Kv).

T

[Deno.KvMutation](../././~/Deno.KvMutation "Deno.KvMutation")

A mutation to a key in a [`Deno.Kv`](../././~/Deno.Kv). A mutation is a combination of a key, a value, and a type. The type determines how the mutation is applied to the key.

T

[Deno.NativeBigIntType](../././~/Deno.NativeBigIntType "Deno.NativeBigIntType")

All BigInt number types for interfacing with foreign functions.

T

[Deno.NativeBooleanType](../././~/Deno.NativeBooleanType "Deno.NativeBooleanType")

The native boolean type for interfacing to foreign functions.

T

[Deno.NativeBufferType](../././~/Deno.NativeBufferType "Deno.NativeBufferType")

The native buffer type for interfacing to foreign functions.

T

[Deno.NativeFunctionType](../././~/Deno.NativeFunctionType "Deno.NativeFunctionType")

The native function type for interfacing with foreign functions.

T

[Deno.NativeI16Enum](../././~/Deno.NativeI16Enum "Deno.NativeI16Enum")

No documentation available

T

[Deno.NativeI32Enum](../././~/Deno.NativeI32Enum "Deno.NativeI32Enum")

No documentation available

T

[Deno.NativeI8Enum](../././~/Deno.NativeI8Enum "Deno.NativeI8Enum")

No documentation available

T

[Deno.NativeNumberType](../././~/Deno.NativeNumberType "Deno.NativeNumberType")

All plain number types for interfacing with foreign functions.

T

[Deno.NativePointerType](../././~/Deno.NativePointerType "Deno.NativePointerType")

The native pointer type for interfacing to foreign functions.

T

[Deno.NativeResultType](../././~/Deno.NativeResultType "Deno.NativeResultType")

No documentation available

T

[Deno.NativeType](../././~/Deno.NativeType "Deno.NativeType")

All supported types for interfacing with foreign functions.

T

[Deno.NativeTypedFunction](../././~/Deno.NativeTypedFunction "Deno.NativeTypedFunction")

No documentation available

T

[Deno.NativeTypedPointer](../././~/Deno.NativeTypedPointer "Deno.NativeTypedPointer")

No documentation available

T

[Deno.NativeU16Enum](../././~/Deno.NativeU16Enum "Deno.NativeU16Enum")

No documentation available

T

[Deno.NativeU32Enum](../././~/Deno.NativeU32Enum "Deno.NativeU32Enum")

No documentation available

T

[Deno.NativeU8Enum](../././~/Deno.NativeU8Enum "Deno.NativeU8Enum")

No documentation available

T

[Deno.NativeVoidType](../././~/Deno.NativeVoidType "Deno.NativeVoidType")

The native void type for interfacing with foreign functions.

T

[Deno.PermissionDescriptor](../././~/Deno.PermissionDescriptor "Deno.PermissionDescriptor")

Permission descriptors which define a permission and can be queried, requested, or revoked.

T

[Deno.PermissionName](../././~/Deno.PermissionName "Deno.PermissionName")

The name of a privileged feature which needs permission.

T

[Deno.PermissionOptions](../././~/Deno.PermissionOptions "Deno.PermissionOptions")

Options which define the permissions within a test or worker context.

T

[Deno.PermissionState](../././~/Deno.PermissionState "Deno.PermissionState")

The current status of the permission:

T

[Deno.PointerValue](../././~/Deno.PointerValue "Deno.PointerValue")

Pointers are represented either with a [`PointerObject`](../././~/Deno.PointerObject) object or a `null` if the pointer is null.

T

[Deno.Proxy](../././~/Deno.Proxy "Deno.Proxy")

The definition for alternative transports (or proxies) in [`Deno.CreateHttpClientOptions`](../././~/Deno.CreateHttpClientOptions).

T

[Deno.RecordType](../././~/Deno.RecordType "Deno.RecordType")

The type of the resource record to resolve via DNS using [`Deno.resolveDns`](../././~/Deno.resolveDns).

T

[Deno.ServeHandler](../././~/Deno.ServeHandler "Deno.ServeHandler")

A handler for HTTP requests. Consumes a request and returns a response.

T

[Deno.Signal](../././~/Deno.Signal "Deno.Signal")

Operating signals which can be listened for or sent to sub-processes. What signals and what their standard behaviors are OS dependent.

T

[Deno.StaticForeignLibraryInterface](../././~/Deno.StaticForeignLibraryInterface "Deno.StaticForeignLibraryInterface")

A utility type that infers a foreign library interface.

T

[Deno.StaticForeignSymbol](../././~/Deno.StaticForeignSymbol "Deno.StaticForeignSymbol")

A utility type that infers a foreign symbol.

T

[Deno.StaticForeignSymbolReturnType](../././~/Deno.StaticForeignSymbolReturnType "Deno.StaticForeignSymbolReturnType")

No documentation available

T

[Deno.TcpListener](../././~/Deno.TcpListener "Deno.TcpListener")

Specialized listener that accepts TCP connections.

T

[Deno.TlsListener](../././~/Deno.TlsListener "Deno.TlsListener")

Specialized listener that accepts TLS connections.

T

[Deno.ToNativeParameterTypes](../././~/Deno.ToNativeParameterTypes "Deno.ToNativeParameterTypes")

A utility type for conversion of parameter types of foreign functions.

T

[Deno.ToNativeResultType](../././~/Deno.ToNativeResultType "Deno.ToNativeResultType")

Type conversion for unsafe callback return types.

T

[Deno.ToNativeType](../././~/Deno.ToNativeType "Deno.ToNativeType")

Type conversion for foreign symbol parameters and unsafe callback return types.

T

[Deno.UnixListener](../././~/Deno.UnixListener "Deno.UnixListener")

Specialized listener that accepts Unix connections.

T

[Deno.UnsafeCallbackFunction](../././~/Deno.UnsafeCallbackFunction "Deno.UnsafeCallbackFunction")

An unsafe callback function.

T

[Deno.VsockListener](../././~/Deno.VsockListener "Deno.VsockListener")

Specialized listener that accepts VSOCK connections.

v

[Deno.args](../././~/Deno.args "Deno.args")

Returns the script arguments to the program.

v

[Deno.brand](../././~/Deno.brand "Deno.brand")

No documentation available

v

[Deno.build](../././~/Deno.build "Deno.build")

Information related to the build of the current Deno runtime.

-   [arch](../././~/Deno.build#property_arch)
-   [env](../././~/Deno.build#property_env)
-   [os](../././~/Deno.build#property_os)
-   [standalone](../././~/Deno.build#property_standalone)
-   [target](../././~/Deno.build#property_target)
-   [vendor](../././~/Deno.build#property_vendor)

v

[Deno.env](../././~/Deno.env "Deno.env")

An interface containing methods to interact with the process environment variables.

v

[Deno.exitCode](../././~/Deno.exitCode "Deno.exitCode")

The exit code for the Deno process.

v

[Deno.mainModule](../././~/Deno.mainModule "Deno.mainModule")

The URL of the entrypoint module entered from the command-line. It requires read permission to the CWD.

v

[Deno.noColor](../././~/Deno.noColor "Deno.noColor")

Reflects the `NO_COLOR` environment variable at program start.

v

[Deno.permissions](../././~/Deno.permissions "Deno.permissions")

Deno's permission management API.

v

[Deno.pid](../././~/Deno.pid "Deno.pid")

The current process ID of this instance of the Deno CLI.

v

[Deno.ppid](../././~/Deno.ppid "Deno.ppid")

The process ID of parent process of this instance of the Deno CLI.

v

[Deno.stderr](../././~/Deno.stderr "Deno.stderr")

A reference to `stderr` which can be used to write directly to `stderr`. It implements the Deno specific [`Writer`](https://jsr.io/@std/io/doc/types/~/Writer), [`WriterSync`](https://jsr.io/@std/io/doc/types/~/WriterSync), and [`Closer`](https://jsr.io/@std/io/doc/types/~/Closer) interfaces as well as provides a `WritableStream` interface.

-   [close](../././~/Deno.stderr#method_close_0)
-   [isTerminal](../././~/Deno.stderr#method_isterminal_0)
-   [writable](../././~/Deno.stderr#property_writable)
-   [write](../././~/Deno.stderr#method_write_0)
-   [writeSync](../././~/Deno.stderr#method_writesync_0)

v

[Deno.stdin](../././~/Deno.stdin "Deno.stdin")

A reference to `stdin` which can be used to read directly from `stdin`.

-   [close](../././~/Deno.stdin#method_close_0)
-   [isTerminal](../././~/Deno.stdin#method_isterminal_0)
-   [read](../././~/Deno.stdin#method_read_0)
-   [readSync](../././~/Deno.stdin#method_readsync_0)
-   [readable](../././~/Deno.stdin#property_readable)
-   [setRaw](../././~/Deno.stdin#method_setraw_0)

v

[Deno.stdout](../././~/Deno.stdout "Deno.stdout")

A reference to `stdout` which can be used to write directly to `stdout`. It implements the Deno specific [`Writer`](https://jsr.io/@std/io/doc/types/~/Writer), [`WriterSync`](https://jsr.io/@std/io/doc/types/~/WriterSync), and [`Closer`](https://jsr.io/@std/io/doc/types/~/Closer) interfaces as well as provides a `WritableStream` interface.

-   [close](../././~/Deno.stdout#method_close_0)
-   [isTerminal](../././~/Deno.stdout#method_isterminal_0)
-   [writable](../././~/Deno.stdout#property_writable)
-   [write](../././~/Deno.stdout#method_write_0)
-   [writeSync](../././~/Deno.stdout#method_writesync_0)

v

[Deno.test](../././~/Deno.test "Deno.test")

Register a test which will be run when `deno test` is used on the command line and the containing module looks like a test module.

v

[Deno.version](../././~/Deno.version "Deno.version")

Version information related to the current Deno CLI runtime environment.

-   [deno](../././~/Deno.version#property_deno)
-   [typescript](../././~/Deno.version#property_typescript)
-   [v8](../././~/Deno.version#property_v8)
