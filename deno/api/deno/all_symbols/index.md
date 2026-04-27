---
title: "All Symbols - Deno documentation"
source: "https://docs.deno.com/api/deno/all_symbols"
canonical_url: "https://docs.deno.com/api/deno/all_symbols"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:56:26.054Z"
content_hash: "efb61e1cec2f124c9a37ea526f1892895d2a1928430fe2559bdb1c8db3e61766"
menu_path: ["All Symbols - Deno documentation"]
section_path: []
content_language: "en"
---
N

[Deno](./././~/Deno "Deno")

The global namespace where Deno specific, non-standard APIs are located.

T

[Deno.Addr](./././~/Deno.Addr "Deno.Addr")

No documentation available

f

[Deno.addSignalListener](./././~/Deno.addSignalListener "Deno.addSignalListener")

Registers the given function as a listener of the given signal event.

v

[Deno.args](./././~/Deno.args "Deno.args")

Returns the script arguments to the program.

I

[Deno.AtomicCheck](./././~/Deno.AtomicCheck "Deno.AtomicCheck")

A check to perform as part of a [`Deno.AtomicOperation`](./././~/Deno.AtomicOperation). The check will fail if the versionstamp for the key-value pair in the KV store does not match the given versionstamp. A check with a `null` versionstamp checks that the key-value pair does not currently exist in the KV store.

-   [key](./././~/Deno.AtomicCheck#property_key)
-   [versionstamp](./././~/Deno.AtomicCheck#property_versionstamp)

c

[Deno.AtomicOperation](./././~/Deno.AtomicOperation "Deno.AtomicOperation")

An operation on a [`Deno.Kv`](./././~/Deno.Kv) that can be performed atomically. Atomic operations do not auto-commit, and must be committed explicitly by calling the `commit` method.

-   [check](./././~/Deno.AtomicOperation#method_check_0)
-   [commit](./././~/Deno.AtomicOperation#method_commit_0)
-   [delete](./././~/Deno.AtomicOperation#method_delete_0)
-   [enqueue](./././~/Deno.AtomicOperation#method_enqueue_0)
-   [max](./././~/Deno.AtomicOperation#method_max_0)
-   [min](./././~/Deno.AtomicOperation#method_min_0)
-   [mutate](./././~/Deno.AtomicOperation#method_mutate_0)
-   [set](./././~/Deno.AtomicOperation#method_set_0)
-   [sum](./././~/Deno.AtomicOperation#method_sum_0)

I

[Deno.BasicAuth](./././~/Deno.BasicAuth "Deno.BasicAuth")

Basic authentication credentials to be used with a [`Deno.Proxy`](./././~/Deno.Proxy) server when specifying [`Deno.CreateHttpClientOptions`](./././~/Deno.CreateHttpClientOptions).

-   [password](./././~/Deno.BasicAuth#property_password)
-   [username](./././~/Deno.BasicAuth#property_username)

f

[Deno.bench](./././~/Deno.bench "Deno.bench")

Register a benchmark test which will be run when `deno bench` is used on the command line and the containing module looks like a bench module.

I

[Deno.BenchContext](./././~/Deno.BenchContext "Deno.BenchContext")

Context that is passed to a benchmarked function. The instance is shared between iterations of the benchmark. Its methods can be used for example to override of the measured portion of the function.

-   [end](./././~/Deno.BenchContext#method_end_0)
-   [name](./././~/Deno.BenchContext#property_name)
-   [origin](./././~/Deno.BenchContext#property_origin)
-   [start](./././~/Deno.BenchContext#method_start_0)

I

[Deno.BenchDefinition](./././~/Deno.BenchDefinition "Deno.BenchDefinition")

The interface for defining a benchmark test using [`Deno.bench`](./././~/Deno.bench).

-   [baseline](./././~/Deno.BenchDefinition#property_baseline)
-   [fn](./././~/Deno.BenchDefinition#property_fn)
-   [group](./././~/Deno.BenchDefinition#property_group)
-   [ignore](./././~/Deno.BenchDefinition#property_ignore)
-   [n](./././~/Deno.BenchDefinition#property_n)
-   [name](./././~/Deno.BenchDefinition#property_name)
-   [only](./././~/Deno.BenchDefinition#property_only)
-   [permissions](./././~/Deno.BenchDefinition#property_permissions)
-   [sanitizeExit](./././~/Deno.BenchDefinition#property_sanitizeexit)
-   [warmup](./././~/Deno.BenchDefinition#property_warmup)

v

[Deno.brand](./././~/Deno.brand "Deno.brand")

No documentation available

v

[Deno.build](./././~/Deno.build "Deno.build")

Information related to the build of the current Deno runtime.

-   [arch](./././~/Deno.build#property_arch)
-   [env](./././~/Deno.build#property_env)
-   [os](./././~/Deno.build#property_os)
-   [standalone](./././~/Deno.build#property_standalone)
-   [target](./././~/Deno.build#property_target)
-   [vendor](./././~/Deno.build#property_vendor)

f

N

[Deno.bundle](./././~/Deno.bundle "Deno.bundle")

Bundle Typescript/Javascript code

T

[Deno.bundle.Format](./././~/Deno.bundle.Format "Deno.bundle.Format")

The output format of the bundle.

I

[Deno.bundle.Message](./././~/Deno.bundle.Message "Deno.bundle.Message")

A message emitted from the bundler.

-   [location](./././~/Deno.bundle.Message#property_location)
-   [notes](./././~/Deno.bundle.Message#property_notes)
-   [text](./././~/Deno.bundle.Message#property_text)

I

[Deno.bundle.MessageLocation](./././~/Deno.bundle.MessageLocation "Deno.bundle.MessageLocation")

The location of a message.

-   [column](./././~/Deno.bundle.MessageLocation#property_column)
-   [file](./././~/Deno.bundle.MessageLocation#property_file)
-   [length](./././~/Deno.bundle.MessageLocation#property_length)
-   [line](./././~/Deno.bundle.MessageLocation#property_line)
-   [namespace](./././~/Deno.bundle.MessageLocation#property_namespace)
-   [suggestion](./././~/Deno.bundle.MessageLocation#property_suggestion)

I

[Deno.bundle.MessageNote](./././~/Deno.bundle.MessageNote "Deno.bundle.MessageNote")

A note about a message.

-   [location](./././~/Deno.bundle.MessageNote#property_location)
-   [text](./././~/Deno.bundle.MessageNote#property_text)

I

[Deno.bundle.Options](./././~/Deno.bundle.Options "Deno.bundle.Options")

Options for the bundle.

-   [codeSplitting](./././~/Deno.bundle.Options#property_codesplitting)
-   [entrypoints](./././~/Deno.bundle.Options#property_entrypoints)
-   [external](./././~/Deno.bundle.Options#property_external)
-   [format](./././~/Deno.bundle.Options#property_format)
-   [inlineImports](./././~/Deno.bundle.Options#property_inlineimports)
-   [keepNames](./././~/Deno.bundle.Options#property_keepnames)
-   [minify](./././~/Deno.bundle.Options#property_minify)
-   [outputDir](./././~/Deno.bundle.Options#property_outputdir)
-   [outputPath](./././~/Deno.bundle.Options#property_outputpath)
-   [packages](./././~/Deno.bundle.Options#property_packages)
-   [platform](./././~/Deno.bundle.Options#property_platform)
-   [sourcemap](./././~/Deno.bundle.Options#property_sourcemap)
-   [write](./././~/Deno.bundle.Options#property_write)

I

[Deno.bundle.OutputFile](./././~/Deno.bundle.OutputFile "Deno.bundle.OutputFile")

An output file in the bundle.

-   [contents](./././~/Deno.bundle.OutputFile#property_contents)
-   [hash](./././~/Deno.bundle.OutputFile#property_hash)
-   [path](./././~/Deno.bundle.OutputFile#property_path)
-   [text](./././~/Deno.bundle.OutputFile#method_text_0)

T

[Deno.bundle.PackageHandling](./././~/Deno.bundle.PackageHandling "Deno.bundle.PackageHandling")

How to handle packages.

T

[Deno.bundle.Platform](./././~/Deno.bundle.Platform "Deno.bundle.Platform")

The target platform of the bundle.

I

[Deno.bundle.Result](./././~/Deno.bundle.Result "Deno.bundle.Result")

The result of bundling.

-   [errors](./././~/Deno.bundle.Result#property_errors)
-   [outputFiles](./././~/Deno.bundle.Result#property_outputfiles)
-   [success](./././~/Deno.bundle.Result#property_success)
-   [warnings](./././~/Deno.bundle.Result#property_warnings)

T

[Deno.bundle.SourceMapType](./././~/Deno.bundle.SourceMapType "Deno.bundle.SourceMapType")

The source map type of the bundle.

I

[Deno.CaaRecord](./././~/Deno.CaaRecord "Deno.CaaRecord")

If [`Deno.resolveDns`](./././~/Deno.resolveDns) is called with `"CAA"` record type specified, it will resolve with an array of objects with this interface.

-   [critical](./././~/Deno.CaaRecord#property_critical)
-   [tag](./././~/Deno.CaaRecord#property_tag)
-   [value](./././~/Deno.CaaRecord#property_value)

f

[Deno.chdir](./././~/Deno.chdir "Deno.chdir")

Change the current working directory to the specified path.

c

[Deno.ChildProcess](./././~/Deno.ChildProcess "Deno.ChildProcess")

The interface for handling a child process returned from `Deno.Command.spawn`.

-   [kill](./././~/Deno.ChildProcess#method_kill_0)
-   [output](./././~/Deno.ChildProcess#method_output_0)
-   [pid](./././~/Deno.ChildProcess#property_pid)
-   [ref](./././~/Deno.ChildProcess#method_ref_0)
-   [status](./././~/Deno.ChildProcess#property_status)
-   [stderr](./././~/Deno.ChildProcess#accessor_stderr)
-   [stdin](./././~/Deno.ChildProcess#accessor_stdin)
-   [stdout](./././~/Deno.ChildProcess#accessor_stdout)
-   [unref](./././~/Deno.ChildProcess#method_unref_0)

f

[Deno.chmod](./././~/Deno.chmod "Deno.chmod")

Changes the permission of a specific file/directory of specified path. Ignores the process's umask.

f

[Deno.chmodSync](./././~/Deno.chmodSync "Deno.chmodSync")

Synchronously changes the permission of a specific file/directory of specified path. Ignores the process's umask.

f

[Deno.chown](./././~/Deno.chown "Deno.chown")

Change owner of a regular file or directory.

f

[Deno.chownSync](./././~/Deno.chownSync "Deno.chownSync")

Synchronously change owner of a regular file or directory.

c

[Deno.Command](./././~/Deno.Command "Deno.Command")

Create a child process.

-   [output](./././~/Deno.Command#method_output_0)
-   [outputSync](./././~/Deno.Command#method_outputsync_0)
-   [spawn](./././~/Deno.Command#method_spawn_0)

I

[Deno.CommandOptions](./././~/Deno.CommandOptions "Deno.CommandOptions")

Options which can be set when calling [`Deno.Command`](./././~/Deno.Command).

-   [args](./././~/Deno.CommandOptions#property_args)
-   [clearEnv](./././~/Deno.CommandOptions#property_clearenv)
-   [cwd](./././~/Deno.CommandOptions#property_cwd)
-   [detached](./././~/Deno.CommandOptions#property_detached)
-   [env](./././~/Deno.CommandOptions#property_env)
-   [gid](./././~/Deno.CommandOptions#property_gid)
-   [signal](./././~/Deno.CommandOptions#property_signal)
-   [stderr](./././~/Deno.CommandOptions#property_stderr)
-   [stdin](./././~/Deno.CommandOptions#property_stdin)
-   [stdout](./././~/Deno.CommandOptions#property_stdout)
-   [uid](./././~/Deno.CommandOptions#property_uid)
-   [windowsRawArguments](./././~/Deno.CommandOptions#property_windowsrawarguments)

I

[Deno.CommandOutput](./././~/Deno.CommandOutput "Deno.CommandOutput")

The interface returned from calling `Deno.Command.output` or `Deno.Command.outputSync` which represents the result of spawning the child process.

-   [stderr](./././~/Deno.CommandOutput#property_stderr)
-   [stdout](./././~/Deno.CommandOutput#property_stdout)

I

[Deno.CommandStatus](./././~/Deno.CommandStatus "Deno.CommandStatus")

No documentation available

-   [code](./././~/Deno.CommandStatus#property_code)
-   [signal](./././~/Deno.CommandStatus#property_signal)
-   [success](./././~/Deno.CommandStatus#property_success)

T

[Deno.ConditionalAsync](./././~/Deno.ConditionalAsync "Deno.ConditionalAsync")

No documentation available

I

[Deno.Conn](./././~/Deno.Conn "Deno.Conn")

No documentation available

-   [close](./././~/Deno.Conn#method_close_0)
-   [closeWrite](./././~/Deno.Conn#method_closewrite_0)
-   [localAddr](./././~/Deno.Conn#property_localaddr)
-   [read](./././~/Deno.Conn#method_read_0)
-   [readable](./././~/Deno.Conn#property_readable)
-   [ref](./././~/Deno.Conn#method_ref_0)
-   [remoteAddr](./././~/Deno.Conn#property_remoteaddr)
-   [unref](./././~/Deno.Conn#method_unref_0)
-   [writable](./././~/Deno.Conn#property_writable)
-   [write](./././~/Deno.Conn#method_write_0)

f

[Deno.connect](./././~/Deno.connect "Deno.connect")

Connects to the hostname (default is "127.0.0.1") and port on the named transport (default is "tcp"), and resolves to the connection (`Conn`).

I

[Deno.ConnectOptions](./././~/Deno.ConnectOptions "Deno.ConnectOptions")

No documentation available

-   [hostname](./././~/Deno.ConnectOptions#property_hostname)
-   [port](./././~/Deno.ConnectOptions#property_port)
-   [signal](./././~/Deno.ConnectOptions#property_signal)
-   [transport](./././~/Deno.ConnectOptions#property_transport)

f

[Deno.connectQuic](./././~/Deno.connectQuic "Deno.connectQuic")

Establishes a secure connection over QUIC using a hostname and port. The cert file is optional and if not included Mozilla's root certificates will be used. See also [https://github.com/ctz/webpki-roots](https://github.com/ctz/webpki-roots) for specifics.

I

[Deno.ConnectQuicOptions](./././~/Deno.ConnectQuicOptions "Deno.ConnectQuicOptions")

No documentation available

-   [alpnProtocols](./././~/Deno.ConnectQuicOptions#property_alpnprotocols)
-   [caCerts](./././~/Deno.ConnectQuicOptions#property_cacerts)
-   [endpoint](./././~/Deno.ConnectQuicOptions#property_endpoint)
-   [hostname](./././~/Deno.ConnectQuicOptions#property_hostname)
-   [port](./././~/Deno.ConnectQuicOptions#property_port)
-   [serverName](./././~/Deno.ConnectQuicOptions#property_servername)
-   [zeroRtt](./././~/Deno.ConnectQuicOptions#property_zerortt)

f

[Deno.connectTls](./././~/Deno.connectTls "Deno.connectTls")

Establishes a secure connection over TLS (transport layer security) using an optional list of CA certs, hostname (default is "127.0.0.1") and port.

I

[Deno.ConnectTlsOptions](./././~/Deno.ConnectTlsOptions "Deno.ConnectTlsOptions")

No documentation available

-   [alpnProtocols](./././~/Deno.ConnectTlsOptions#property_alpnprotocols)
-   [caCerts](./././~/Deno.ConnectTlsOptions#property_cacerts)
-   [hostname](./././~/Deno.ConnectTlsOptions#property_hostname)
-   [port](./././~/Deno.ConnectTlsOptions#property_port)
-   [unsafelyDisableHostnameVerification](./././~/Deno.ConnectTlsOptions#property_unsafelydisablehostnameverification)

f

[Deno.consoleSize](./././~/Deno.consoleSize "Deno.consoleSize")

Gets the size of the console as columns/rows.

f

[Deno.copyFile](./././~/Deno.copyFile "Deno.copyFile")

Copies the contents and permissions of one file to another specified path, by default creating a new file if needed, else overwriting. Fails if target path is a directory or is unwritable.

f

[Deno.copyFileSync](./././~/Deno.copyFileSync "Deno.copyFileSync")

Synchronously copies the contents and permissions of one file to another specified path, by default creating a new file if needed, else overwriting. Fails if target path is a directory or is unwritable.

f

[Deno.create](./././~/Deno.create "Deno.create")

Creates a file if none exists or truncates an existing file and resolves to an instance of [`Deno.FsFile`](./././~/Deno.FsFile).

f

[Deno.createHttpClient](./././~/Deno.createHttpClient "Deno.createHttpClient")

Create a custom HttpClient to use with `fetch`. This is an extension of the web platform Fetch API which allows Deno to use custom TLS CA certificates and connect via a proxy while using `fetch()`.

I

[Deno.CreateHttpClientOptions](./././~/Deno.CreateHttpClientOptions "Deno.CreateHttpClientOptions")

The options used when creating a [`Deno.HttpClient`](./././~/Deno.HttpClient).

-   [allowHost](./././~/Deno.CreateHttpClientOptions#property_allowhost)
-   [caCerts](./././~/Deno.CreateHttpClientOptions#property_cacerts)
-   [http1](./././~/Deno.CreateHttpClientOptions#property_http1)
-   [http2](./././~/Deno.CreateHttpClientOptions#property_http2)
-   [localAddress](./././~/Deno.CreateHttpClientOptions#property_localaddress)
-   [poolIdleTimeout](./././~/Deno.CreateHttpClientOptions#property_poolidletimeout)
-   [poolMaxIdlePerHost](./././~/Deno.CreateHttpClientOptions#property_poolmaxidleperhost)
-   [proxy](./././~/Deno.CreateHttpClientOptions#property_proxy)

f

[Deno.createSync](./././~/Deno.createSync "Deno.createSync")

Creates a file if none exists or truncates an existing file and returns an instance of [`Deno.FsFile`](./././~/Deno.FsFile).

f

[Deno.cron](./././~/Deno.cron "Deno.cron")

Create a cron job that will periodically execute the provided handler callback based on the specified schedule.

I

[Deno.CronSchedule](./././~/Deno.CronSchedule "Deno.CronSchedule")

CronSchedule is the interface used for JSON format cron `schedule`.

-   [dayOfMonth](./././~/Deno.CronSchedule#property_dayofmonth)
-   [dayOfWeek](./././~/Deno.CronSchedule#property_dayofweek)
-   [hour](./././~/Deno.CronSchedule#property_hour)
-   [minute](./././~/Deno.CronSchedule#property_minute)
-   [month](./././~/Deno.CronSchedule#property_month)

T

[Deno.CronScheduleExpression](./././~/Deno.CronScheduleExpression "Deno.CronScheduleExpression")

CronScheduleExpression is used as the type of `minute`, `hour`, `dayOfMonth`, `month`, and `dayOfWeek` in `CronSchedule`.

f

[Deno.cwd](./././~/Deno.cwd "Deno.cwd")

Return a string representing the current working directory.

I

[Deno.DatagramConn](./././~/Deno.DatagramConn "Deno.DatagramConn")

A generic transport listener for message-oriented protocols.

-   [addr](./././~/Deno.DatagramConn#property_addr)
-   [close](./././~/Deno.DatagramConn#method_close_0)
-   [joinMulticastV4](./././~/Deno.DatagramConn#method_joinmulticastv4_0)
-   [joinMulticastV6](./././~/Deno.DatagramConn#method_joinmulticastv6_0)
-   [receive](./././~/Deno.DatagramConn#method_receive_0)
-   [send](./././~/Deno.DatagramConn#method_send_0)

I

[Deno.DenoTest](./././~/Deno.DenoTest "Deno.DenoTest")

No documentation available

-   [afterAll](./././~/Deno.DenoTest#method_afterall_0)
-   [afterEach](./././~/Deno.DenoTest#method_aftereach_0)
-   [beforeAll](./././~/Deno.DenoTest#method_beforeall_0)
-   [beforeEach](./././~/Deno.DenoTest#method_beforeeach_0)
-   [ignore](./././~/Deno.DenoTest#method_ignore_0)
-   [only](./././~/Deno.DenoTest#method_only_0)

I

[Deno.DirEntry](./././~/Deno.DirEntry "Deno.DirEntry")

Information about a directory entry returned from [`Deno.readDir`](./././~/Deno.readDir) and [`Deno.readDirSync`](./././~/Deno.readDirSync).

-   [isDirectory](./././~/Deno.DirEntry#property_isdirectory)
-   [isFile](./././~/Deno.DirEntry#property_isfile)
-   [isSymlink](./././~/Deno.DirEntry#property_issymlink)
-   [name](./././~/Deno.DirEntry#property_name)

f

[Deno.dlopen](./././~/Deno.dlopen "Deno.dlopen")

Opens an external dynamic library and registers symbols, making foreign functions available to be called.

I

[Deno.DynamicLibrary](./././~/Deno.DynamicLibrary "Deno.DynamicLibrary")

A dynamic library resource. Use [`Deno.dlopen`](./././~/Deno.dlopen) to load a dynamic library and return this interface.

-   [close](./././~/Deno.DynamicLibrary#method_close_0)
-   [symbols](./././~/Deno.DynamicLibrary#property_symbols)

I

[Deno.Env](./././~/Deno.Env "Deno.Env")

An interface containing methods to interact with the process environment variables.

-   [delete](./././~/Deno.Env#method_delete_0)
-   [get](./././~/Deno.Env#method_get_0)
-   [has](./././~/Deno.Env#method_has_0)
-   [set](./././~/Deno.Env#method_set_0)
-   [toObject](./././~/Deno.Env#method_toobject_0)

v

[Deno.env](./././~/Deno.env "Deno.env")

An interface containing methods to interact with the process environment variables.

I

[Deno.EnvPermissionDescriptor](./././~/Deno.EnvPermissionDescriptor "Deno.EnvPermissionDescriptor")

The permission descriptor for the `allow-env` and `deny-env` permissions, which controls access to being able to read and write to the process environment variables as well as access other information about the environment. The option `variable` allows scoping the permission to a specific environment variable.

-   [name](./././~/Deno.EnvPermissionDescriptor#property_name)
-   [variable](./././~/Deno.EnvPermissionDescriptor#property_variable)

N

[Deno.errors](./././~/Deno.errors "Deno.errors")

A set of error constructors that are raised by Deno APIs.

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

f

[Deno.execPath](./././~/Deno.execPath "Deno.execPath")

Returns the path to the current deno executable.

f

[Deno.exit](./././~/Deno.exit "Deno.exit")

Exit the Deno process with optional exit code.

v

[Deno.exitCode](./././~/Deno.exitCode "Deno.exitCode")

The exit code for the Deno process.

I

[Deno.FfiPermissionDescriptor](./././~/Deno.FfiPermissionDescriptor "Deno.FfiPermissionDescriptor")

The permission descriptor for the `allow-ffi` and `deny-ffi` permissions, which controls access to loading _foreign_ code and interfacing with it via the [Foreign Function Interface API](https://docs.deno.com/runtime/manual/runtime/ffi_api) available in Deno. The option `path` allows scoping the permission to a specific path on the host.

-   [name](./././~/Deno.FfiPermissionDescriptor#property_name)
-   [path](./././~/Deno.FfiPermissionDescriptor#property_path)

I

[Deno.FileInfo](./././~/Deno.FileInfo "Deno.FileInfo")

Provides information about a file and is returned by [`Deno.stat`](./././~/Deno.stat), [`Deno.lstat`](./././~/Deno.lstat), [`Deno.statSync`](./././~/Deno.statSync), and [`Deno.lstatSync`](./././~/Deno.lstatSync) or from calling `stat()` and `statSync()` on an [`Deno.FsFile`](./././~/Deno.FsFile) instance.

-   [atime](./././~/Deno.FileInfo#property_atime)
-   [birthtime](./././~/Deno.FileInfo#property_birthtime)
-   [blksize](./././~/Deno.FileInfo#property_blksize)
-   [blocks](./././~/Deno.FileInfo#property_blocks)
-   [ctime](./././~/Deno.FileInfo#property_ctime)
-   [dev](./././~/Deno.FileInfo#property_dev)
-   [gid](./././~/Deno.FileInfo#property_gid)
-   [ino](./././~/Deno.FileInfo#property_ino)
-   [isBlockDevice](./././~/Deno.FileInfo#property_isblockdevice)
-   [isCharDevice](./././~/Deno.FileInfo#property_ischardevice)
-   [isDirectory](./././~/Deno.FileInfo#property_isdirectory)
-   [isFifo](./././~/Deno.FileInfo#property_isfifo)
-   [isFile](./././~/Deno.FileInfo#property_isfile)
-   [isSocket](./././~/Deno.FileInfo#property_issocket)
-   [isSymlink](./././~/Deno.FileInfo#property_issymlink)
-   [mode](./././~/Deno.FileInfo#property_mode)
-   [mtime](./././~/Deno.FileInfo#property_mtime)
-   [nlink](./././~/Deno.FileInfo#property_nlink)
-   [rdev](./././~/Deno.FileInfo#property_rdev)
-   [size](./././~/Deno.FileInfo#property_size)
-   [uid](./././~/Deno.FileInfo#property_uid)

I

[Deno.ForeignFunction](./././~/Deno.ForeignFunction "Deno.ForeignFunction")

The interface for a foreign function as defined by its parameter and result types.

-   [name](./././~/Deno.ForeignFunction#property_name)
-   [nonblocking](./././~/Deno.ForeignFunction#property_nonblocking)
-   [optional](./././~/Deno.ForeignFunction#property_optional)
-   [parameters](./././~/Deno.ForeignFunction#property_parameters)
-   [result](./././~/Deno.ForeignFunction#property_result)

I

[Deno.ForeignLibraryInterface](./././~/Deno.ForeignLibraryInterface "Deno.ForeignLibraryInterface")

A foreign library interface descriptor.

I

[Deno.ForeignStatic](./././~/Deno.ForeignStatic "Deno.ForeignStatic")

No documentation available

-   [name](./././~/Deno.ForeignStatic#property_name)
-   [optional](./././~/Deno.ForeignStatic#property_optional)
-   [type](./././~/Deno.ForeignStatic#property_type)

T

[Deno.FromForeignFunction](./././~/Deno.FromForeignFunction "Deno.FromForeignFunction")

No documentation available

T

[Deno.FromNativeParameterTypes](./././~/Deno.FromNativeParameterTypes "Deno.FromNativeParameterTypes")

No documentation available

T

[Deno.FromNativeResultType](./././~/Deno.FromNativeResultType "Deno.FromNativeResultType")

Type conversion for foreign symbol return types.

T

[Deno.FromNativeType](./././~/Deno.FromNativeType "Deno.FromNativeType")

Type conversion for foreign symbol return types and unsafe callback parameters.

I

[Deno.FsEvent](./././~/Deno.FsEvent "Deno.FsEvent")

Represents a unique file system event yielded by a [`Deno.FsWatcher`](./././~/Deno.FsWatcher).

-   [flag](./././~/Deno.FsEvent#property_flag)
-   [kind](./././~/Deno.FsEvent#property_kind)
-   [paths](./././~/Deno.FsEvent#property_paths)

T

[Deno.FsEventFlag](./././~/Deno.FsEventFlag "Deno.FsEventFlag")

Additional information for FsEvent objects with the "other" kind.

c

[Deno.FsFile](./././~/Deno.FsFile "Deno.FsFile")

The Deno abstraction for reading and writing files.

-   [close](./././~/Deno.FsFile#method_close_0)
-   [isTerminal](./././~/Deno.FsFile#method_isterminal_0)
-   [lock](./././~/Deno.FsFile#method_lock_0)
-   [lockSync](./././~/Deno.FsFile#method_locksync_0)
-   [read](./././~/Deno.FsFile#method_read_0)
-   [readSync](./././~/Deno.FsFile#method_readsync_0)
-   [readable](./././~/Deno.FsFile#property_readable)
-   [seek](./././~/Deno.FsFile#method_seek_0)
-   [seekSync](./././~/Deno.FsFile#method_seeksync_0)
-   [setRaw](./././~/Deno.FsFile#method_setraw_0)
-   [stat](./././~/Deno.FsFile#method_stat_0)
-   [statSync](./././~/Deno.FsFile#method_statsync_0)
-   [sync](./././~/Deno.FsFile#method_sync_0)
-   [syncData](./././~/Deno.FsFile#method_syncdata_0)
-   [syncDataSync](./././~/Deno.FsFile#method_syncdatasync_0)
-   [syncSync](./././~/Deno.FsFile#method_syncsync_0)
-   [truncate](./././~/Deno.FsFile#method_truncate_0)
-   [truncateSync](./././~/Deno.FsFile#method_truncatesync_0)
-   [tryLock](./././~/Deno.FsFile#method_trylock_0)
-   [tryLockSync](./././~/Deno.FsFile#method_trylocksync_0)
-   [unlock](./././~/Deno.FsFile#method_unlock_0)
-   [unlockSync](./././~/Deno.FsFile#method_unlocksync_0)
-   [utime](./././~/Deno.FsFile#method_utime_0)
-   [utimeSync](./././~/Deno.FsFile#method_utimesync_0)
-   [writable](./././~/Deno.FsFile#property_writable)
-   [write](./././~/Deno.FsFile#method_write_0)
-   [writeSync](./././~/Deno.FsFile#method_writesync_0)

I

[Deno.FsWatcher](./././~/Deno.FsWatcher "Deno.FsWatcher")

Returned by [`Deno.watchFs`](./././~/Deno.watchFs). It is an async iterator yielding up system events. To stop watching the file system by calling `.close()` method.

-   [close](./././~/Deno.FsWatcher#method_close_0)
-   [return](./././~/Deno.FsWatcher#method_return_0)

f

[Deno.gid](./././~/Deno.gid "Deno.gid")

Returns the group id of the process on POSIX platforms. Returns null on windows.

f

[Deno.hostname](./././~/Deno.hostname "Deno.hostname")

Get the `hostname` of the machine the Deno process is running on.

c

[Deno.HttpClient](./././~/Deno.HttpClient "Deno.HttpClient")

A custom `HttpClient` for use with `fetch` function. This is designed to allow custom certificates or proxies to be used with `fetch()`.

-   [close](./././~/Deno.HttpClient#method_close_0)

I

[Deno.HttpServer](./././~/Deno.HttpServer "Deno.HttpServer")

An instance of the server created using `Deno.serve()` API.

-   [addr](./././~/Deno.HttpServer#property_addr)
-   [finished](./././~/Deno.HttpServer#property_finished)
-   [ref](./././~/Deno.HttpServer#method_ref_0)
-   [shutdown](./././~/Deno.HttpServer#method_shutdown_0)
-   [unref](./././~/Deno.HttpServer#method_unref_0)

I

[Deno.ImportPermissionDescriptor](./././~/Deno.ImportPermissionDescriptor "Deno.ImportPermissionDescriptor")

The permission descriptor for the `allow-import` and `deny-import` permissions, which controls access to importing from remote hosts via the network. The option `host` allows scoping the permission for outbound connection to a specific host and port.

-   [host](./././~/Deno.ImportPermissionDescriptor#property_host)
-   [name](./././~/Deno.ImportPermissionDescriptor#property_name)

f

[Deno.inspect](./././~/Deno.inspect "Deno.inspect")

Converts the input into a string that has the same format as printed by `console.log()`.

I

[Deno.InspectOptions](./././~/Deno.InspectOptions "Deno.InspectOptions")

Option which can be specified when performing [`Deno.inspect`](./././~/Deno.inspect).

-   [breakLength](./././~/Deno.InspectOptions#property_breaklength)
-   [colors](./././~/Deno.InspectOptions#property_colors)
-   [compact](./././~/Deno.InspectOptions#property_compact)
-   [depth](./././~/Deno.InspectOptions#property_depth)
-   [escapeSequences](./././~/Deno.InspectOptions#property_escapesequences)
-   [getters](./././~/Deno.InspectOptions#property_getters)
-   [iterableLimit](./././~/Deno.InspectOptions#property_iterablelimit)
-   [showHidden](./././~/Deno.InspectOptions#property_showhidden)
-   [showProxy](./././~/Deno.InspectOptions#property_showproxy)
-   [sorted](./././~/Deno.InspectOptions#property_sorted)
-   [strAbbreviateSize](./././~/Deno.InspectOptions#property_strabbreviatesize)
-   [trailingComma](./././~/Deno.InspectOptions#property_trailingcomma)

N

[Deno.jupyter](./././~/Deno.jupyter "Deno.jupyter")

A namespace containing runtime APIs available in Jupyter notebooks.

v

[Deno.jupyter.$display](./././~/Deno.jupyter.$display "Deno.jupyter.$display")

No documentation available

f

[Deno.jupyter.broadcast](./././~/Deno.jupyter.broadcast "Deno.jupyter.broadcast")

Broadcast a message on IO pub channel.

f

[Deno.jupyter.display](./././~/Deno.jupyter.display "Deno.jupyter.display")

Display function for Jupyter Deno Kernel. Mimics the behavior of IPython's `display(obj, raw=True)` function to allow asynchronous displaying of objects in Jupyter.

I

[Deno.jupyter.Displayable](./././~/Deno.jupyter.Displayable "Deno.jupyter.Displayable")

No documentation available

-   [$display](./././~/Deno.jupyter.Displayable#property_$display)

I

[Deno.jupyter.DisplayOptions](./././~/Deno.jupyter.DisplayOptions "Deno.jupyter.DisplayOptions")

No documentation available

-   [display\_id](./././~/Deno.jupyter.DisplayOptions#property_display_id)
-   [raw](./././~/Deno.jupyter.DisplayOptions#property_raw)
-   [update](./././~/Deno.jupyter.DisplayOptions#property_update)

f

[Deno.jupyter.format](./././~/Deno.jupyter.format "Deno.jupyter.format")

Format an object for displaying in Deno

f

[Deno.jupyter.html](./././~/Deno.jupyter.html "Deno.jupyter.html")

Show HTML in Jupyter frontends with a tagged template function.

f

[Deno.jupyter.image](./././~/Deno.jupyter.image "Deno.jupyter.image")

Display a JPG or PNG image.

f

[Deno.jupyter.md](./././~/Deno.jupyter.md "Deno.jupyter.md")

Show Markdown in Jupyter frontends with a tagged template function.

I

[Deno.jupyter.MediaBundle](./././~/Deno.jupyter.MediaBundle "Deno.jupyter.MediaBundle")

A collection of supported media types and data for Jupyter frontends.

-   [application/geo+json](./././~/Deno.jupyter.MediaBundle#property_application/geo+json)
-   [application/javascript](./././~/Deno.jupyter.MediaBundle#property_application/javascript)
-   [application/json](./././~/Deno.jupyter.MediaBundle#property_application/json)
-   [application/pdf](./././~/Deno.jupyter.MediaBundle#property_application/pdf)
-   [application/vdom.v1+json](./././~/Deno.jupyter.MediaBundle#property_application/vdom_v1+json)
-   [application/vnd.plotly.v1+json](./././~/Deno.jupyter.MediaBundle#property_application/vnd_plotly_v1+json)
-   [application/vnd.vega.v5+json](./././~/Deno.jupyter.MediaBundle#property_application/vnd_vega_v5+json)
-   [application/vnd.vegalite.v4+json](./././~/Deno.jupyter.MediaBundle#property_application/vnd_vegalite_v4+json)
-   [application/vnd.vegalite.v5+json](./././~/Deno.jupyter.MediaBundle#property_application/vnd_vegalite_v5+json)
-   [image/gif](./././~/Deno.jupyter.MediaBundle#property_image/gif)
-   [image/jpeg](./././~/Deno.jupyter.MediaBundle#property_image/jpeg)
-   [image/png](./././~/Deno.jupyter.MediaBundle#property_image/png)
-   [image/svg+xml](./././~/Deno.jupyter.MediaBundle#property_image/svg+xml)
-   [text/html](./././~/Deno.jupyter.MediaBundle#property_text/html)
-   [text/markdown](./././~/Deno.jupyter.MediaBundle#property_text/markdown)
-   [text/plain](./././~/Deno.jupyter.MediaBundle#property_text/plain)

f

[Deno.jupyter.svg](./././~/Deno.jupyter.svg "Deno.jupyter.svg")

SVG Tagged Template Function.

I

[Deno.jupyter.VegaObject](./././~/Deno.jupyter.VegaObject "Deno.jupyter.VegaObject")

No documentation available

-   [$schema](./././~/Deno.jupyter.VegaObject#property_$schema)

f

[Deno.kill](./././~/Deno.kill "Deno.kill")

Send a signal to process under given `pid`. The value and meaning of the `signal` to the process is operating system and process dependant. `Signal` provides the most common signals. Default signal is `"SIGTERM"`.

c

[Deno.Kv](./././~/Deno.Kv "Deno.Kv")

A key-value database that can be used to store and retrieve data.

-   [atomic](./././~/Deno.Kv#method_atomic_0)
-   [close](./././~/Deno.Kv#method_close_0)
-   [commitVersionstamp](./././~/Deno.Kv#method_commitversionstamp_0)
-   [delete](./././~/Deno.Kv#method_delete_0)
-   [enqueue](./././~/Deno.Kv#method_enqueue_0)
-   [get](./././~/Deno.Kv#method_get_0)
-   [getMany](./././~/Deno.Kv#method_getmany_0)
-   [list](./././~/Deno.Kv#method_list_0)
-   [listenQueue](./././~/Deno.Kv#method_listenqueue_0)
-   [set](./././~/Deno.Kv#method_set_0)
-   [watch](./././~/Deno.Kv#method_watch_0)

I

[Deno.KvCommitError](./././~/Deno.KvCommitError "Deno.KvCommitError")

No documentation available

-   [ok](./././~/Deno.KvCommitError#property_ok)

I

[Deno.KvCommitResult](./././~/Deno.KvCommitResult "Deno.KvCommitResult")

No documentation available

-   [ok](./././~/Deno.KvCommitResult#property_ok)
-   [versionstamp](./././~/Deno.KvCommitResult#property_versionstamp)

T

[Deno.KvConsistencyLevel](./././~/Deno.KvConsistencyLevel "Deno.KvConsistencyLevel")

Consistency level of a KV operation.

I

[Deno.KvEntry](./././~/Deno.KvEntry "Deno.KvEntry")

A versioned pair of key and value in a [`Deno.Kv`](./././~/Deno.Kv).

-   [key](./././~/Deno.KvEntry#property_key)
-   [value](./././~/Deno.KvEntry#property_value)
-   [versionstamp](./././~/Deno.KvEntry#property_versionstamp)

T

[Deno.KvEntryMaybe](./././~/Deno.KvEntryMaybe "Deno.KvEntryMaybe")

An optional versioned pair of key and value in a [`Deno.Kv`](./././~/Deno.Kv).

T

[Deno.KvKey](./././~/Deno.KvKey "Deno.KvKey")

A key to be persisted in a [`Deno.Kv`](./././~/Deno.Kv). A key is a sequence of [`Deno.KvKeyPart`](./././~/Deno.KvKeyPart)s.

T

[Deno.KvKeyPart](./././~/Deno.KvKeyPart "Deno.KvKeyPart")

A single part of a [`Deno.KvKey`](./././~/Deno.KvKey). Parts are ordered lexicographically, first by their type, and within a given type by their value.

c

[Deno.KvListIterator](./././~/Deno.KvListIterator "Deno.KvListIterator")

An iterator over a range of data entries in a [`Deno.Kv`](./././~/Deno.Kv).

-   [cursor](./././~/Deno.KvListIterator#accessor_cursor)
-   [next](./././~/Deno.KvListIterator#method_next_0)

I

[Deno.KvListOptions](./././~/Deno.KvListOptions "Deno.KvListOptions")

Options for listing key-value pairs in a [`Deno.Kv`](./././~/Deno.Kv).

-   [batchSize](./././~/Deno.KvListOptions#property_batchsize)
-   [consistency](./././~/Deno.KvListOptions#property_consistency)
-   [cursor](./././~/Deno.KvListOptions#property_cursor)
-   [limit](./././~/Deno.KvListOptions#property_limit)
-   [reverse](./././~/Deno.KvListOptions#property_reverse)

T

[Deno.KvListSelector](./././~/Deno.KvListSelector "Deno.KvListSelector")

A selector that selects the range of data returned by a list operation on a [`Deno.Kv`](./././~/Deno.Kv).

T

[Deno.KvMutation](./././~/Deno.KvMutation "Deno.KvMutation")

A mutation to a key in a [`Deno.Kv`](./././~/Deno.Kv). A mutation is a combination of a key, a value, and a type. The type determines how the mutation is applied to the key.

c

[Deno.KvU64](./././~/Deno.KvU64 "Deno.KvU64")

Wrapper type for 64-bit unsigned integers for use as values in a [`Deno.Kv`](./././~/Deno.Kv).

-   [value](./././~/Deno.KvU64#property_value)

f

[Deno.link](./././~/Deno.link "Deno.link")

Creates `newpath` as a hard link to `oldpath`.

f

[Deno.linkSync](./././~/Deno.linkSync "Deno.linkSync")

Synchronously creates `newpath` as a hard link to `oldpath`.

N

[Deno.lint](./././~/Deno.lint "Deno.lint")

No documentation available

T

[Deno.lint.Accessibility](./././~/Deno.lint.Accessibility "Deno.lint.Accessibility")

TypeScript accessibility modifiers used in classes

I

[Deno.lint.AccessorProperty](./././~/Deno.lint.AccessorProperty "Deno.lint.AccessorProperty")

No documentation available

-   [accessibility](./././~/Deno.lint.AccessorProperty#property_accessibility)
-   [computed](./././~/Deno.lint.AccessorProperty#property_computed)
-   [declare](./././~/Deno.lint.AccessorProperty#property_declare)
-   [decorators](./././~/Deno.lint.AccessorProperty#property_decorators)
-   [key](./././~/Deno.lint.AccessorProperty#property_key)
-   [optional](./././~/Deno.lint.AccessorProperty#property_optional)
-   [override](./././~/Deno.lint.AccessorProperty#property_override)
-   [parent](./././~/Deno.lint.AccessorProperty#property_parent)
-   [range](./././~/Deno.lint.AccessorProperty#property_range)
-   [readonly](./././~/Deno.lint.AccessorProperty#property_readonly)
-   [static](./././~/Deno.lint.AccessorProperty#property_static)
-   [type](./././~/Deno.lint.AccessorProperty#property_type)
-   [value](./././~/Deno.lint.AccessorProperty#property_value)

I

[Deno.lint.ArrayExpression](./././~/Deno.lint.ArrayExpression "Deno.lint.ArrayExpression")

An array literal

-   [elements](./././~/Deno.lint.ArrayExpression#property_elements)
-   [parent](./././~/Deno.lint.ArrayExpression#property_parent)
-   [range](./././~/Deno.lint.ArrayExpression#property_range)
-   [type](./././~/Deno.lint.ArrayExpression#property_type)

I

[Deno.lint.ArrayPattern](./././~/Deno.lint.ArrayPattern "Deno.lint.ArrayPattern")

Destructure an array.

-   [elements](./././~/Deno.lint.ArrayPattern#property_elements)
-   [optional](./././~/Deno.lint.ArrayPattern#property_optional)
-   [parent](./././~/Deno.lint.ArrayPattern#property_parent)
-   [range](./././~/Deno.lint.ArrayPattern#property_range)
-   [type](./././~/Deno.lint.ArrayPattern#property_type)
-   [typeAnnotation](./././~/Deno.lint.ArrayPattern#property_typeannotation)

I

[Deno.lint.ArrowFunctionExpression](./././~/Deno.lint.ArrowFunctionExpression "Deno.lint.ArrowFunctionExpression")

Arrow function expression

-   [async](./././~/Deno.lint.ArrowFunctionExpression#property_async)
-   [body](./././~/Deno.lint.ArrowFunctionExpression#property_body)
-   [generator](./././~/Deno.lint.ArrowFunctionExpression#property_generator)
-   [id](./././~/Deno.lint.ArrowFunctionExpression#property_id)
-   [params](./././~/Deno.lint.ArrowFunctionExpression#property_params)
-   [parent](./././~/Deno.lint.ArrowFunctionExpression#property_parent)
-   [range](./././~/Deno.lint.ArrowFunctionExpression#property_range)
-   [returnType](./././~/Deno.lint.ArrowFunctionExpression#property_returntype)
-   [type](./././~/Deno.lint.ArrowFunctionExpression#property_type)
-   [typeParameters](./././~/Deno.lint.ArrowFunctionExpression#property_typeparameters)

I

[Deno.lint.AssignmentExpression](./././~/Deno.lint.AssignmentExpression "Deno.lint.AssignmentExpression")

Updaate a variable or property.

-   [left](./././~/Deno.lint.AssignmentExpression#property_left)
-   [operator](./././~/Deno.lint.AssignmentExpression#property_operator)
-   [parent](./././~/Deno.lint.AssignmentExpression#property_parent)
-   [range](./././~/Deno.lint.AssignmentExpression#property_range)
-   [right](./././~/Deno.lint.AssignmentExpression#property_right)
-   [type](./././~/Deno.lint.AssignmentExpression#property_type)

I

[Deno.lint.AssignmentPattern](./././~/Deno.lint.AssignmentPattern "Deno.lint.AssignmentPattern")

Assign default values in parameters.

-   [left](./././~/Deno.lint.AssignmentPattern#property_left)
-   [parent](./././~/Deno.lint.AssignmentPattern#property_parent)
-   [range](./././~/Deno.lint.AssignmentPattern#property_range)
-   [right](./././~/Deno.lint.AssignmentPattern#property_right)
-   [type](./././~/Deno.lint.AssignmentPattern#property_type)

I

[Deno.lint.AwaitExpression](./././~/Deno.lint.AwaitExpression "Deno.lint.AwaitExpression")

Await a `Promise` and get its fulfilled value.

-   [argument](./././~/Deno.lint.AwaitExpression#property_argument)
-   [parent](./././~/Deno.lint.AwaitExpression#property_parent)
-   [range](./././~/Deno.lint.AwaitExpression#property_range)
-   [type](./././~/Deno.lint.AwaitExpression#property_type)

I

[Deno.lint.BigIntLiteral](./././~/Deno.lint.BigIntLiteral "Deno.lint.BigIntLiteral")

Represents numbers that are too high or too low to be represented by the `number` type.

-   [bigint](./././~/Deno.lint.BigIntLiteral#property_bigint)
-   [parent](./././~/Deno.lint.BigIntLiteral#property_parent)
-   [range](./././~/Deno.lint.BigIntLiteral#property_range)
-   [raw](./././~/Deno.lint.BigIntLiteral#property_raw)
-   [type](./././~/Deno.lint.BigIntLiteral#property_type)
-   [value](./././~/Deno.lint.BigIntLiteral#property_value)

I

[Deno.lint.BinaryExpression](./././~/Deno.lint.BinaryExpression "Deno.lint.BinaryExpression")

Compare left and right value with the specifier operator.

-   [left](./././~/Deno.lint.BinaryExpression#property_left)
-   [operator](./././~/Deno.lint.BinaryExpression#property_operator)
-   [parent](./././~/Deno.lint.BinaryExpression#property_parent)
-   [range](./././~/Deno.lint.BinaryExpression#property_range)
-   [right](./././~/Deno.lint.BinaryExpression#property_right)
-   [type](./././~/Deno.lint.BinaryExpression#property_type)

I

[Deno.lint.BlockComment](./././~/Deno.lint.BlockComment "Deno.lint.BlockComment")

A potentially multi-line block comment

-   [range](./././~/Deno.lint.BlockComment#property_range)
-   [type](./././~/Deno.lint.BlockComment#property_type)
-   [value](./././~/Deno.lint.BlockComment#property_value)

I

[Deno.lint.BlockStatement](./././~/Deno.lint.BlockStatement "Deno.lint.BlockStatement")

No documentation available

-   [body](./././~/Deno.lint.BlockStatement#property_body)
-   [parent](./././~/Deno.lint.BlockStatement#property_parent)
-   [range](./././~/Deno.lint.BlockStatement#property_range)
-   [type](./././~/Deno.lint.BlockStatement#property_type)

I

[Deno.lint.BooleanLiteral](./././~/Deno.lint.BooleanLiteral "Deno.lint.BooleanLiteral")

Either `true` or `false`

-   [parent](./././~/Deno.lint.BooleanLiteral#property_parent)
-   [range](./././~/Deno.lint.BooleanLiteral#property_range)
-   [raw](./././~/Deno.lint.BooleanLiteral#property_raw)
-   [type](./././~/Deno.lint.BooleanLiteral#property_type)
-   [value](./././~/Deno.lint.BooleanLiteral#property_value)

I

[Deno.lint.BreakStatement](./././~/Deno.lint.BreakStatement "Deno.lint.BreakStatement")

Break any loop or labeled statement, example:

-   [label](./././~/Deno.lint.BreakStatement#property_label)
-   [parent](./././~/Deno.lint.BreakStatement#property_parent)
-   [range](./././~/Deno.lint.BreakStatement#property_range)
-   [type](./././~/Deno.lint.BreakStatement#property_type)

I

[Deno.lint.CallExpression](./././~/Deno.lint.CallExpression "Deno.lint.CallExpression")

A function call.

-   [arguments](./././~/Deno.lint.CallExpression#property_arguments)
-   [callee](./././~/Deno.lint.CallExpression#property_callee)
-   [optional](./././~/Deno.lint.CallExpression#property_optional)
-   [parent](./././~/Deno.lint.CallExpression#property_parent)
-   [range](./././~/Deno.lint.CallExpression#property_range)
-   [type](./././~/Deno.lint.CallExpression#property_type)
-   [typeArguments](./././~/Deno.lint.CallExpression#property_typearguments)

I

[Deno.lint.CatchClause](./././~/Deno.lint.CatchClause "Deno.lint.CatchClause")

The catch clause of a try/catch statement

-   [body](./././~/Deno.lint.CatchClause#property_body)
-   [param](./././~/Deno.lint.CatchClause#property_param)
-   [parent](./././~/Deno.lint.CatchClause#property_parent)
-   [range](./././~/Deno.lint.CatchClause#property_range)
-   [type](./././~/Deno.lint.CatchClause#property_type)

I

[Deno.lint.ChainExpression](./././~/Deno.lint.ChainExpression "Deno.lint.ChainExpression")

ChainExpression

-   [expression](./././~/Deno.lint.ChainExpression#property_expression)
-   [parent](./././~/Deno.lint.ChainExpression#property_parent)
-   [range](./././~/Deno.lint.ChainExpression#property_range)
-   [type](./././~/Deno.lint.ChainExpression#property_type)

I

[Deno.lint.ClassBody](./././~/Deno.lint.ClassBody "Deno.lint.ClassBody")

Represents the body of a class and contains all members

-   [body](./././~/Deno.lint.ClassBody#property_body)
-   [parent](./././~/Deno.lint.ClassBody#property_parent)
-   [range](./././~/Deno.lint.ClassBody#property_range)
-   [type](./././~/Deno.lint.ClassBody#property_type)

I

[Deno.lint.ClassDeclaration](./././~/Deno.lint.ClassDeclaration "Deno.lint.ClassDeclaration")

Declares a class in the current scope

-   [abstract](./././~/Deno.lint.ClassDeclaration#property_abstract)
-   [body](./././~/Deno.lint.ClassDeclaration#property_body)
-   [declare](./././~/Deno.lint.ClassDeclaration#property_declare)
-   [id](./././~/Deno.lint.ClassDeclaration#property_id)
-   [implements](./././~/Deno.lint.ClassDeclaration#property_implements)
-   [parent](./././~/Deno.lint.ClassDeclaration#property_parent)
-   [range](./././~/Deno.lint.ClassDeclaration#property_range)
-   [superClass](./././~/Deno.lint.ClassDeclaration#property_superclass)
-   [type](./././~/Deno.lint.ClassDeclaration#property_type)

I

[Deno.lint.ClassExpression](./././~/Deno.lint.ClassExpression "Deno.lint.ClassExpression")

Similar to ClassDeclaration but for declaring a class as an expression. The main difference is that the class name(=id) can be omitted.

-   [abstract](./././~/Deno.lint.ClassExpression#property_abstract)
-   [body](./././~/Deno.lint.ClassExpression#property_body)
-   [declare](./././~/Deno.lint.ClassExpression#property_declare)
-   [id](./././~/Deno.lint.ClassExpression#property_id)
-   [implements](./././~/Deno.lint.ClassExpression#property_implements)
-   [parent](./././~/Deno.lint.ClassExpression#property_parent)
-   [range](./././~/Deno.lint.ClassExpression#property_range)
-   [superClass](./././~/Deno.lint.ClassExpression#property_superclass)
-   [superTypeArguments](./././~/Deno.lint.ClassExpression#property_supertypearguments)
-   [type](./././~/Deno.lint.ClassExpression#property_type)
-   [typeParameters](./././~/Deno.lint.ClassExpression#property_typeparameters)

I

[Deno.lint.ConditionalExpression](./././~/Deno.lint.ConditionalExpression "Deno.lint.ConditionalExpression")

Inline if-statement.

-   [alternate](./././~/Deno.lint.ConditionalExpression#property_alternate)
-   [consequent](./././~/Deno.lint.ConditionalExpression#property_consequent)
-   [parent](./././~/Deno.lint.ConditionalExpression#property_parent)
-   [range](./././~/Deno.lint.ConditionalExpression#property_range)
-   [test](./././~/Deno.lint.ConditionalExpression#property_test)
-   [type](./././~/Deno.lint.ConditionalExpression#property_type)

I

[Deno.lint.ContinueStatement](./././~/Deno.lint.ContinueStatement "Deno.lint.ContinueStatement")

Terminates the current loop and continues with the next iteration.

-   [label](./././~/Deno.lint.ContinueStatement#property_label)
-   [parent](./././~/Deno.lint.ContinueStatement#property_parent)
-   [range](./././~/Deno.lint.ContinueStatement#property_range)
-   [type](./././~/Deno.lint.ContinueStatement#property_type)

I

[Deno.lint.DebuggerStatement](./././~/Deno.lint.DebuggerStatement "Deno.lint.DebuggerStatement")

The `debugger;` statement.

-   [parent](./././~/Deno.lint.DebuggerStatement#property_parent)
-   [range](./././~/Deno.lint.DebuggerStatement#property_range)
-   [type](./././~/Deno.lint.DebuggerStatement#property_type)

I

[Deno.lint.Decorator](./././~/Deno.lint.Decorator "Deno.lint.Decorator")

Experimental: Decorators

-   [expression](./././~/Deno.lint.Decorator#property_expression)
-   [parent](./././~/Deno.lint.Decorator#property_parent)
-   [range](./././~/Deno.lint.Decorator#property_range)
-   [type](./././~/Deno.lint.Decorator#property_type)

I

[Deno.lint.Diagnostic](./././~/Deno.lint.Diagnostic "Deno.lint.Diagnostic")

No documentation available

-   [fix](./././~/Deno.lint.Diagnostic#property_fix)
-   [hint](./././~/Deno.lint.Diagnostic#property_hint)
-   [id](./././~/Deno.lint.Diagnostic#property_id)
-   [message](./././~/Deno.lint.Diagnostic#property_message)
-   [range](./././~/Deno.lint.Diagnostic#property_range)

I

[Deno.lint.DoWhileStatement](./././~/Deno.lint.DoWhileStatement "Deno.lint.DoWhileStatement")

Re-run loop for as long as test expression is truthy.

-   [body](./././~/Deno.lint.DoWhileStatement#property_body)
-   [parent](./././~/Deno.lint.DoWhileStatement#property_parent)
-   [range](./././~/Deno.lint.DoWhileStatement#property_range)
-   [test](./././~/Deno.lint.DoWhileStatement#property_test)
-   [type](./././~/Deno.lint.DoWhileStatement#property_type)

I

[Deno.lint.ExportAllDeclaration](./././~/Deno.lint.ExportAllDeclaration "Deno.lint.ExportAllDeclaration")

No documentation available

-   [attributes](./././~/Deno.lint.ExportAllDeclaration#property_attributes)
-   [exportKind](./././~/Deno.lint.ExportAllDeclaration#property_exportkind)
-   [exported](./././~/Deno.lint.ExportAllDeclaration#property_exported)
-   [parent](./././~/Deno.lint.ExportAllDeclaration#property_parent)
-   [range](./././~/Deno.lint.ExportAllDeclaration#property_range)
-   [source](./././~/Deno.lint.ExportAllDeclaration#property_source)
-   [type](./././~/Deno.lint.ExportAllDeclaration#property_type)

I

[Deno.lint.ExportDefaultDeclaration](./././~/Deno.lint.ExportDefaultDeclaration "Deno.lint.ExportDefaultDeclaration")

No documentation available

-   [declaration](./././~/Deno.lint.ExportDefaultDeclaration#property_declaration)
-   [exportKind](./././~/Deno.lint.ExportDefaultDeclaration#property_exportkind)
-   [parent](./././~/Deno.lint.ExportDefaultDeclaration#property_parent)
-   [range](./././~/Deno.lint.ExportDefaultDeclaration#property_range)
-   [type](./././~/Deno.lint.ExportDefaultDeclaration#property_type)

I

[Deno.lint.ExportNamedDeclaration](./././~/Deno.lint.ExportNamedDeclaration "Deno.lint.ExportNamedDeclaration")

No documentation available

-   [attributes](./././~/Deno.lint.ExportNamedDeclaration#property_attributes)
-   [declaration](./././~/Deno.lint.ExportNamedDeclaration#property_declaration)
-   [exportKind](./././~/Deno.lint.ExportNamedDeclaration#property_exportkind)
-   [parent](./././~/Deno.lint.ExportNamedDeclaration#property_parent)
-   [range](./././~/Deno.lint.ExportNamedDeclaration#property_range)
-   [source](./././~/Deno.lint.ExportNamedDeclaration#property_source)
-   [specifiers](./././~/Deno.lint.ExportNamedDeclaration#property_specifiers)
-   [type](./././~/Deno.lint.ExportNamedDeclaration#property_type)

I

[Deno.lint.ExportSpecifier](./././~/Deno.lint.ExportSpecifier "Deno.lint.ExportSpecifier")

No documentation available

-   [exportKind](./././~/Deno.lint.ExportSpecifier#property_exportkind)
-   [exported](./././~/Deno.lint.ExportSpecifier#property_exported)
-   [local](./././~/Deno.lint.ExportSpecifier#property_local)
-   [parent](./././~/Deno.lint.ExportSpecifier#property_parent)
-   [range](./././~/Deno.lint.ExportSpecifier#property_range)
-   [type](./././~/Deno.lint.ExportSpecifier#property_type)

T

[Deno.lint.Expression](./././~/Deno.lint.Expression "Deno.lint.Expression")

Union type of all possible expression nodes

I

[Deno.lint.ExpressionStatement](./././~/Deno.lint.ExpressionStatement "Deno.lint.ExpressionStatement")

Statement that holds an expression.

-   [expression](./././~/Deno.lint.ExpressionStatement#property_expression)
-   [parent](./././~/Deno.lint.ExpressionStatement#property_parent)
-   [range](./././~/Deno.lint.ExpressionStatement#property_range)
-   [type](./././~/Deno.lint.ExpressionStatement#property_type)

I

[Deno.lint.Fix](./././~/Deno.lint.Fix "Deno.lint.Fix")

No documentation available

-   [range](./././~/Deno.lint.Fix#property_range)
-   [text](./././~/Deno.lint.Fix#property_text)

I

[Deno.lint.Fixer](./././~/Deno.lint.Fixer "Deno.lint.Fixer")

No documentation available

-   [insertTextAfter](./././~/Deno.lint.Fixer#method_inserttextafter_0)
-   [insertTextAfterRange](./././~/Deno.lint.Fixer#method_inserttextafterrange_0)
-   [insertTextBefore](./././~/Deno.lint.Fixer#method_inserttextbefore_0)
-   [insertTextBeforeRange](./././~/Deno.lint.Fixer#method_inserttextbeforerange_0)
-   [remove](./././~/Deno.lint.Fixer#method_remove_0)
-   [removeRange](./././~/Deno.lint.Fixer#method_removerange_0)
-   [replaceText](./././~/Deno.lint.Fixer#method_replacetext_0)
-   [replaceTextRange](./././~/Deno.lint.Fixer#method_replacetextrange_0)

I

[Deno.lint.ForInStatement](./././~/Deno.lint.ForInStatement "Deno.lint.ForInStatement")

Enumerate over all enumerable string properties of an object.

-   [body](./././~/Deno.lint.ForInStatement#property_body)
-   [left](./././~/Deno.lint.ForInStatement#property_left)
-   [parent](./././~/Deno.lint.ForInStatement#property_parent)
-   [range](./././~/Deno.lint.ForInStatement#property_range)
-   [right](./././~/Deno.lint.ForInStatement#property_right)
-   [type](./././~/Deno.lint.ForInStatement#property_type)

I

[Deno.lint.ForOfStatement](./././~/Deno.lint.ForOfStatement "Deno.lint.ForOfStatement")

Iterate over sequence of values from an iterator.

-   [await](./././~/Deno.lint.ForOfStatement#property_await)
-   [body](./././~/Deno.lint.ForOfStatement#property_body)
-   [left](./././~/Deno.lint.ForOfStatement#property_left)
-   [parent](./././~/Deno.lint.ForOfStatement#property_parent)
-   [range](./././~/Deno.lint.ForOfStatement#property_range)
-   [right](./././~/Deno.lint.ForOfStatement#property_right)
-   [type](./././~/Deno.lint.ForOfStatement#property_type)

I

[Deno.lint.ForStatement](./././~/Deno.lint.ForStatement "Deno.lint.ForStatement")

Classic for-loop.

-   [body](./././~/Deno.lint.ForStatement#property_body)
-   [init](./././~/Deno.lint.ForStatement#property_init)
-   [parent](./././~/Deno.lint.ForStatement#property_parent)
-   [range](./././~/Deno.lint.ForStatement#property_range)
-   [test](./././~/Deno.lint.ForStatement#property_test)
-   [type](./././~/Deno.lint.ForStatement#property_type)
-   [update](./././~/Deno.lint.ForStatement#property_update)

I

[Deno.lint.FunctionDeclaration](./././~/Deno.lint.FunctionDeclaration "Deno.lint.FunctionDeclaration")

Declares a function in the current scope

-   [async](./././~/Deno.lint.FunctionDeclaration#property_async)
-   [body](./././~/Deno.lint.FunctionDeclaration#property_body)
-   [declare](./././~/Deno.lint.FunctionDeclaration#property_declare)
-   [generator](./././~/Deno.lint.FunctionDeclaration#property_generator)
-   [id](./././~/Deno.lint.FunctionDeclaration#property_id)
-   [params](./././~/Deno.lint.FunctionDeclaration#property_params)
-   [parent](./././~/Deno.lint.FunctionDeclaration#property_parent)
-   [range](./././~/Deno.lint.FunctionDeclaration#property_range)
-   [returnType](./././~/Deno.lint.FunctionDeclaration#property_returntype)
-   [type](./././~/Deno.lint.FunctionDeclaration#property_type)
-   [typeParameters](./././~/Deno.lint.FunctionDeclaration#property_typeparameters)

I

[Deno.lint.FunctionExpression](./././~/Deno.lint.FunctionExpression "Deno.lint.FunctionExpression")

Declare a function as an expression. Similar to `FunctionDeclaration`, with an optional name (=id).

-   [async](./././~/Deno.lint.FunctionExpression#property_async)
-   [body](./././~/Deno.lint.FunctionExpression#property_body)
-   [generator](./././~/Deno.lint.FunctionExpression#property_generator)
-   [id](./././~/Deno.lint.FunctionExpression#property_id)
-   [params](./././~/Deno.lint.FunctionExpression#property_params)
-   [parent](./././~/Deno.lint.FunctionExpression#property_parent)
-   [range](./././~/Deno.lint.FunctionExpression#property_range)
-   [returnType](./././~/Deno.lint.FunctionExpression#property_returntype)
-   [type](./././~/Deno.lint.FunctionExpression#property_type)
-   [typeParameters](./././~/Deno.lint.FunctionExpression#property_typeparameters)

I

[Deno.lint.Identifier](./././~/Deno.lint.Identifier "Deno.lint.Identifier")

Custom named node by the developer. Can be a variable name, a function name, parameter, etc.

-   [name](./././~/Deno.lint.Identifier#property_name)
-   [optional](./././~/Deno.lint.Identifier#property_optional)
-   [parent](./././~/Deno.lint.Identifier#property_parent)
-   [range](./././~/Deno.lint.Identifier#property_range)
-   [type](./././~/Deno.lint.Identifier#property_type)
-   [typeAnnotation](./././~/Deno.lint.Identifier#property_typeannotation)

I

[Deno.lint.IfStatement](./././~/Deno.lint.IfStatement "Deno.lint.IfStatement")

Execute a statement the test passes, otherwise the alternate statement, if it was defined.

-   [alternate](./././~/Deno.lint.IfStatement#property_alternate)
-   [consequent](./././~/Deno.lint.IfStatement#property_consequent)
-   [parent](./././~/Deno.lint.IfStatement#property_parent)
-   [range](./././~/Deno.lint.IfStatement#property_range)
-   [test](./././~/Deno.lint.IfStatement#property_test)
-   [type](./././~/Deno.lint.IfStatement#property_type)

I

[Deno.lint.ImportAttribute](./././~/Deno.lint.ImportAttribute "Deno.lint.ImportAttribute")

No documentation available

-   [key](./././~/Deno.lint.ImportAttribute#property_key)
-   [parent](./././~/Deno.lint.ImportAttribute#property_parent)
-   [range](./././~/Deno.lint.ImportAttribute#property_range)
-   [type](./././~/Deno.lint.ImportAttribute#property_type)
-   [value](./././~/Deno.lint.ImportAttribute#property_value)

I

[Deno.lint.ImportDeclaration](./././~/Deno.lint.ImportDeclaration "Deno.lint.ImportDeclaration")

An import declaration, examples:

-   [attributes](./././~/Deno.lint.ImportDeclaration#property_attributes)
-   [importKind](./././~/Deno.lint.ImportDeclaration#property_importkind)
-   [parent](./././~/Deno.lint.ImportDeclaration#property_parent)
-   [range](./././~/Deno.lint.ImportDeclaration#property_range)
-   [source](./././~/Deno.lint.ImportDeclaration#property_source)
-   [specifiers](./././~/Deno.lint.ImportDeclaration#property_specifiers)
-   [type](./././~/Deno.lint.ImportDeclaration#property_type)

I

[Deno.lint.ImportDefaultSpecifier](./././~/Deno.lint.ImportDefaultSpecifier "Deno.lint.ImportDefaultSpecifier")

No documentation available

-   [local](./././~/Deno.lint.ImportDefaultSpecifier#property_local)
-   [parent](./././~/Deno.lint.ImportDefaultSpecifier#property_parent)
-   [range](./././~/Deno.lint.ImportDefaultSpecifier#property_range)
-   [type](./././~/Deno.lint.ImportDefaultSpecifier#property_type)

I

[Deno.lint.ImportExpression](./././~/Deno.lint.ImportExpression "Deno.lint.ImportExpression")

Dynamically import a module.

-   [options](./././~/Deno.lint.ImportExpression#property_options)
-   [parent](./././~/Deno.lint.ImportExpression#property_parent)
-   [range](./././~/Deno.lint.ImportExpression#property_range)
-   [source](./././~/Deno.lint.ImportExpression#property_source)
-   [type](./././~/Deno.lint.ImportExpression#property_type)

I

[Deno.lint.ImportNamespaceSpecifier](./././~/Deno.lint.ImportNamespaceSpecifier "Deno.lint.ImportNamespaceSpecifier")

No documentation available

-   [local](./././~/Deno.lint.ImportNamespaceSpecifier#property_local)
-   [parent](./././~/Deno.lint.ImportNamespaceSpecifier#property_parent)
-   [range](./././~/Deno.lint.ImportNamespaceSpecifier#property_range)
-   [type](./././~/Deno.lint.ImportNamespaceSpecifier#property_type)

I

[Deno.lint.ImportSpecifier](./././~/Deno.lint.ImportSpecifier "Deno.lint.ImportSpecifier")

No documentation available

-   [importKind](./././~/Deno.lint.ImportSpecifier#property_importkind)
-   [imported](./././~/Deno.lint.ImportSpecifier#property_imported)
-   [local](./././~/Deno.lint.ImportSpecifier#property_local)
-   [parent](./././~/Deno.lint.ImportSpecifier#property_parent)
-   [range](./././~/Deno.lint.ImportSpecifier#property_range)
-   [type](./././~/Deno.lint.ImportSpecifier#property_type)

I

[Deno.lint.JSXAttribute](./././~/Deno.lint.JSXAttribute "Deno.lint.JSXAttribute")

A JSX attribute

-   [name](./././~/Deno.lint.JSXAttribute#property_name)
-   [parent](./././~/Deno.lint.JSXAttribute#property_parent)
-   [range](./././~/Deno.lint.JSXAttribute#property_range)
-   [type](./././~/Deno.lint.JSXAttribute#property_type)
-   [value](./././~/Deno.lint.JSXAttribute#property_value)

T

[Deno.lint.JSXChild](./././~/Deno.lint.JSXChild "Deno.lint.JSXChild")

Union type of all possible child nodes in JSX

I

[Deno.lint.JSXClosingElement](./././~/Deno.lint.JSXClosingElement "Deno.lint.JSXClosingElement")

The closing tag of a JSXElement. Only used when the element is not self-closing.

-   [name](./././~/Deno.lint.JSXClosingElement#property_name)
-   [parent](./././~/Deno.lint.JSXClosingElement#property_parent)
-   [range](./././~/Deno.lint.JSXClosingElement#property_range)
-   [type](./././~/Deno.lint.JSXClosingElement#property_type)

I

[Deno.lint.JSXClosingFragment](./././~/Deno.lint.JSXClosingFragment "Deno.lint.JSXClosingFragment")

The closing tag of a JSXFragment.

-   [parent](./././~/Deno.lint.JSXClosingFragment#property_parent)
-   [range](./././~/Deno.lint.JSXClosingFragment#property_range)
-   [type](./././~/Deno.lint.JSXClosingFragment#property_type)

I

[Deno.lint.JSXElement](./././~/Deno.lint.JSXElement "Deno.lint.JSXElement")

A JSX element.

-   [children](./././~/Deno.lint.JSXElement#property_children)
-   [closingElement](./././~/Deno.lint.JSXElement#property_closingelement)
-   [openingElement](./././~/Deno.lint.JSXElement#property_openingelement)
-   [parent](./././~/Deno.lint.JSXElement#property_parent)
-   [range](./././~/Deno.lint.JSXElement#property_range)
-   [type](./././~/Deno.lint.JSXElement#property_type)

I

[Deno.lint.JSXEmptyExpression](./././~/Deno.lint.JSXEmptyExpression "Deno.lint.JSXEmptyExpression")

Empty JSX expression.

-   [parent](./././~/Deno.lint.JSXEmptyExpression#property_parent)
-   [range](./././~/Deno.lint.JSXEmptyExpression#property_range)
-   [type](./././~/Deno.lint.JSXEmptyExpression#property_type)

I

[Deno.lint.JSXExpressionContainer](./././~/Deno.lint.JSXExpressionContainer "Deno.lint.JSXExpressionContainer")

Inserts a normal JS expression into JSX.

-   [expression](./././~/Deno.lint.JSXExpressionContainer#property_expression)
-   [parent](./././~/Deno.lint.JSXExpressionContainer#property_parent)
-   [range](./././~/Deno.lint.JSXExpressionContainer#property_range)
-   [type](./././~/Deno.lint.JSXExpressionContainer#property_type)

I

[Deno.lint.JSXFragment](./././~/Deno.lint.JSXFragment "Deno.lint.JSXFragment")

Usually a passthrough node to pass multiple sibling elements as the JSX syntax requires one root element.

-   [children](./././~/Deno.lint.JSXFragment#property_children)
-   [closingFragment](./././~/Deno.lint.JSXFragment#property_closingfragment)
-   [openingFragment](./././~/Deno.lint.JSXFragment#property_openingfragment)
-   [parent](./././~/Deno.lint.JSXFragment#property_parent)
-   [range](./././~/Deno.lint.JSXFragment#property_range)
-   [type](./././~/Deno.lint.JSXFragment#property_type)

I

[Deno.lint.JSXIdentifier](./././~/Deno.lint.JSXIdentifier "Deno.lint.JSXIdentifier")

User named identifier inside JSX.

-   [name](./././~/Deno.lint.JSXIdentifier#property_name)
-   [parent](./././~/Deno.lint.JSXIdentifier#property_parent)
-   [range](./././~/Deno.lint.JSXIdentifier#property_range)
-   [type](./././~/Deno.lint.JSXIdentifier#property_type)

I

[Deno.lint.JSXMemberExpression](./././~/Deno.lint.JSXMemberExpression "Deno.lint.JSXMemberExpression")

JSX member expression.

-   [object](./././~/Deno.lint.JSXMemberExpression#property_object)
-   [parent](./././~/Deno.lint.JSXMemberExpression#property_parent)
-   [property](./././~/Deno.lint.JSXMemberExpression#property_property)
-   [range](./././~/Deno.lint.JSXMemberExpression#property_range)
-   [type](./././~/Deno.lint.JSXMemberExpression#property_type)

I

[Deno.lint.JSXNamespacedName](./././~/Deno.lint.JSXNamespacedName "Deno.lint.JSXNamespacedName")

Namespaced name in JSX

-   [name](./././~/Deno.lint.JSXNamespacedName#property_name)
-   [namespace](./././~/Deno.lint.JSXNamespacedName#property_namespace)
-   [parent](./././~/Deno.lint.JSXNamespacedName#property_parent)
-   [range](./././~/Deno.lint.JSXNamespacedName#property_range)
-   [type](./././~/Deno.lint.JSXNamespacedName#property_type)

I

[Deno.lint.JSXOpeningElement](./././~/Deno.lint.JSXOpeningElement "Deno.lint.JSXOpeningElement")

The opening tag of a JSXElement

-   [attributes](./././~/Deno.lint.JSXOpeningElement#property_attributes)
-   [name](./././~/Deno.lint.JSXOpeningElement#property_name)
-   [parent](./././~/Deno.lint.JSXOpeningElement#property_parent)
-   [range](./././~/Deno.lint.JSXOpeningElement#property_range)
-   [selfClosing](./././~/Deno.lint.JSXOpeningElement#property_selfclosing)
-   [type](./././~/Deno.lint.JSXOpeningElement#property_type)
-   [typeArguments](./././~/Deno.lint.JSXOpeningElement#property_typearguments)

I

[Deno.lint.JSXOpeningFragment](./././~/Deno.lint.JSXOpeningFragment "Deno.lint.JSXOpeningFragment")

The opening tag of a JSXFragment.

-   [parent](./././~/Deno.lint.JSXOpeningFragment#property_parent)
-   [range](./././~/Deno.lint.JSXOpeningFragment#property_range)
-   [type](./././~/Deno.lint.JSXOpeningFragment#property_type)

I

[Deno.lint.JSXSpreadAttribute](./././~/Deno.lint.JSXSpreadAttribute "Deno.lint.JSXSpreadAttribute")

Spreads an object as JSX attributes.

-   [argument](./././~/Deno.lint.JSXSpreadAttribute#property_argument)
-   [parent](./././~/Deno.lint.JSXSpreadAttribute#property_parent)
-   [range](./././~/Deno.lint.JSXSpreadAttribute#property_range)
-   [type](./././~/Deno.lint.JSXSpreadAttribute#property_type)

I

[Deno.lint.JSXText](./././~/Deno.lint.JSXText "Deno.lint.JSXText")

Plain text in JSX.

-   [parent](./././~/Deno.lint.JSXText#property_parent)
-   [range](./././~/Deno.lint.JSXText#property_range)
-   [raw](./././~/Deno.lint.JSXText#property_raw)
-   [type](./././~/Deno.lint.JSXText#property_type)
-   [value](./././~/Deno.lint.JSXText#property_value)

I

[Deno.lint.LabeledStatement](./././~/Deno.lint.LabeledStatement "Deno.lint.LabeledStatement")

Custom control flow based on labels.

-   [body](./././~/Deno.lint.LabeledStatement#property_body)
-   [label](./././~/Deno.lint.LabeledStatement#property_label)
-   [parent](./././~/Deno.lint.LabeledStatement#property_parent)
-   [range](./././~/Deno.lint.LabeledStatement#property_range)
-   [type](./././~/Deno.lint.LabeledStatement#property_type)

I

[Deno.lint.LineComment](./././~/Deno.lint.LineComment "Deno.lint.LineComment")

A single line comment

-   [range](./././~/Deno.lint.LineComment#property_range)
-   [type](./././~/Deno.lint.LineComment#property_type)
-   [value](./././~/Deno.lint.LineComment#property_value)

T

[Deno.lint.LintVisitor](./././~/Deno.lint.LintVisitor "Deno.lint.LintVisitor")

No documentation available

T

[Deno.lint.Literal](./././~/Deno.lint.Literal "Deno.lint.Literal")

Union type of all Literals

I

[Deno.lint.LogicalExpression](./././~/Deno.lint.LogicalExpression "Deno.lint.LogicalExpression")

Chain expressions based on the operator specified

-   [left](./././~/Deno.lint.LogicalExpression#property_left)
-   [operator](./././~/Deno.lint.LogicalExpression#property_operator)
-   [parent](./././~/Deno.lint.LogicalExpression#property_parent)
-   [range](./././~/Deno.lint.LogicalExpression#property_range)
-   [right](./././~/Deno.lint.LogicalExpression#property_right)
-   [type](./././~/Deno.lint.LogicalExpression#property_type)

I

[Deno.lint.MemberExpression](./././~/Deno.lint.MemberExpression "Deno.lint.MemberExpression")

MemberExpression

-   [computed](./././~/Deno.lint.MemberExpression#property_computed)
-   [object](./././~/Deno.lint.MemberExpression#property_object)
-   [optional](./././~/Deno.lint.MemberExpression#property_optional)
-   [parent](./././~/Deno.lint.MemberExpression#property_parent)
-   [property](./././~/Deno.lint.MemberExpression#property_property)
-   [range](./././~/Deno.lint.MemberExpression#property_range)
-   [type](./././~/Deno.lint.MemberExpression#property_type)

I

[Deno.lint.MetaProperty](./././~/Deno.lint.MetaProperty "Deno.lint.MetaProperty")

Can either be `import.meta` or `new.target`.

-   [meta](./././~/Deno.lint.MetaProperty#property_meta)
-   [parent](./././~/Deno.lint.MetaProperty#property_parent)
-   [property](./././~/Deno.lint.MetaProperty#property_property)
-   [range](./././~/Deno.lint.MetaProperty#property_range)
-   [type](./././~/Deno.lint.MetaProperty#property_type)

I

[Deno.lint.MethodDefinition](./././~/Deno.lint.MethodDefinition "Deno.lint.MethodDefinition")

No documentation available

-   [accessibility](./././~/Deno.lint.MethodDefinition#property_accessibility)
-   [computed](./././~/Deno.lint.MethodDefinition#property_computed)
-   [declare](./././~/Deno.lint.MethodDefinition#property_declare)
-   [decorators](./././~/Deno.lint.MethodDefinition#property_decorators)
-   [key](./././~/Deno.lint.MethodDefinition#property_key)
-   [kind](./././~/Deno.lint.MethodDefinition#property_kind)
-   [optional](./././~/Deno.lint.MethodDefinition#property_optional)
-   [override](./././~/Deno.lint.MethodDefinition#property_override)
-   [parent](./././~/Deno.lint.MethodDefinition#property_parent)
-   [range](./././~/Deno.lint.MethodDefinition#property_range)
-   [readonly](./././~/Deno.lint.MethodDefinition#property_readonly)
-   [static](./././~/Deno.lint.MethodDefinition#property_static)
-   [type](./././~/Deno.lint.MethodDefinition#property_type)
-   [value](./././~/Deno.lint.MethodDefinition#property_value)

I

[Deno.lint.NewExpression](./././~/Deno.lint.NewExpression "Deno.lint.NewExpression")

Create a new instance of a class.

-   [arguments](./././~/Deno.lint.NewExpression#property_arguments)
-   [callee](./././~/Deno.lint.NewExpression#property_callee)
-   [parent](./././~/Deno.lint.NewExpression#property_parent)
-   [range](./././~/Deno.lint.NewExpression#property_range)
-   [type](./././~/Deno.lint.NewExpression#property_type)
-   [typeArguments](./././~/Deno.lint.NewExpression#property_typearguments)

T

[Deno.lint.Node](./././~/Deno.lint.Node "Deno.lint.Node")

Union type of all possible AST nodes

I

[Deno.lint.NullLiteral](./././~/Deno.lint.NullLiteral "Deno.lint.NullLiteral")

The `null` literal

-   [parent](./././~/Deno.lint.NullLiteral#property_parent)
-   [range](./././~/Deno.lint.NullLiteral#property_range)
-   [raw](./././~/Deno.lint.NullLiteral#property_raw)
-   [type](./././~/Deno.lint.NullLiteral#property_type)
-   [value](./././~/Deno.lint.NullLiteral#property_value)

I

[Deno.lint.NumberLiteral](./././~/Deno.lint.NumberLiteral "Deno.lint.NumberLiteral")

A number literal

-   [parent](./././~/Deno.lint.NumberLiteral#property_parent)
-   [range](./././~/Deno.lint.NumberLiteral#property_range)
-   [raw](./././~/Deno.lint.NumberLiteral#property_raw)
-   [type](./././~/Deno.lint.NumberLiteral#property_type)
-   [value](./././~/Deno.lint.NumberLiteral#property_value)

I

[Deno.lint.ObjectExpression](./././~/Deno.lint.ObjectExpression "Deno.lint.ObjectExpression")

An object literal.

-   [parent](./././~/Deno.lint.ObjectExpression#property_parent)
-   [properties](./././~/Deno.lint.ObjectExpression#property_properties)
-   [range](./././~/Deno.lint.ObjectExpression#property_range)
-   [type](./././~/Deno.lint.ObjectExpression#property_type)

I

[Deno.lint.ObjectPattern](./././~/Deno.lint.ObjectPattern "Deno.lint.ObjectPattern")

Destructure an object.

-   [optional](./././~/Deno.lint.ObjectPattern#property_optional)
-   [parent](./././~/Deno.lint.ObjectPattern#property_parent)
-   [properties](./././~/Deno.lint.ObjectPattern#property_properties)
-   [range](./././~/Deno.lint.ObjectPattern#property_range)
-   [type](./././~/Deno.lint.ObjectPattern#property_type)
-   [typeAnnotation](./././~/Deno.lint.ObjectPattern#property_typeannotation)

T

[Deno.lint.Parameter](./././~/Deno.lint.Parameter "Deno.lint.Parameter")

Function/Method parameter

I

[Deno.lint.Plugin](./././~/Deno.lint.Plugin "Deno.lint.Plugin")

In your plugins file do something like

-   [name](./././~/Deno.lint.Plugin#property_name)
-   [rules](./././~/Deno.lint.Plugin#property_rules)

I

[Deno.lint.PrivateIdentifier](./././~/Deno.lint.PrivateIdentifier "Deno.lint.PrivateIdentifier")

Private members inside of classes, must start with `#`.

-   [name](./././~/Deno.lint.PrivateIdentifier#property_name)
-   [parent](./././~/Deno.lint.PrivateIdentifier#property_parent)
-   [range](./././~/Deno.lint.PrivateIdentifier#property_range)
-   [type](./././~/Deno.lint.PrivateIdentifier#property_type)

I

[Deno.lint.Program](./././~/Deno.lint.Program "Deno.lint.Program")

No documentation available

-   [body](./././~/Deno.lint.Program#property_body)
-   [comments](./././~/Deno.lint.Program#property_comments)
-   [range](./././~/Deno.lint.Program#property_range)
-   [sourceType](./././~/Deno.lint.Program#property_sourcetype)
-   [type](./././~/Deno.lint.Program#property_type)

I

[Deno.lint.Property](./././~/Deno.lint.Property "Deno.lint.Property")

No documentation available

-   [computed](./././~/Deno.lint.Property#property_computed)
-   [key](./././~/Deno.lint.Property#property_key)
-   [kind](./././~/Deno.lint.Property#property_kind)
-   [method](./././~/Deno.lint.Property#property_method)
-   [parent](./././~/Deno.lint.Property#property_parent)
-   [range](./././~/Deno.lint.Property#property_range)
-   [shorthand](./././~/Deno.lint.Property#property_shorthand)
-   [type](./././~/Deno.lint.Property#property_type)
-   [value](./././~/Deno.lint.Property#property_value)

I

[Deno.lint.PropertyDefinition](./././~/Deno.lint.PropertyDefinition "Deno.lint.PropertyDefinition")

No documentation available

-   [accessibility](./././~/Deno.lint.PropertyDefinition#property_accessibility)
-   [computed](./././~/Deno.lint.PropertyDefinition#property_computed)
-   [declare](./././~/Deno.lint.PropertyDefinition#property_declare)
-   [decorators](./././~/Deno.lint.PropertyDefinition#property_decorators)
-   [key](./././~/Deno.lint.PropertyDefinition#property_key)
-   [optional](./././~/Deno.lint.PropertyDefinition#property_optional)
-   [override](./././~/Deno.lint.PropertyDefinition#property_override)
-   [parent](./././~/Deno.lint.PropertyDefinition#property_parent)
-   [range](./././~/Deno.lint.PropertyDefinition#property_range)
-   [readonly](./././~/Deno.lint.PropertyDefinition#property_readonly)
-   [static](./././~/Deno.lint.PropertyDefinition#property_static)
-   [type](./././~/Deno.lint.PropertyDefinition#property_type)
-   [typeAnnotation](./././~/Deno.lint.PropertyDefinition#property_typeannotation)
-   [value](./././~/Deno.lint.PropertyDefinition#property_value)

T

[Deno.lint.Range](./././~/Deno.lint.Range "Deno.lint.Range")

No documentation available

I

[Deno.lint.RegExpLiteral](./././~/Deno.lint.RegExpLiteral "Deno.lint.RegExpLiteral")

A regex literal:

-   [parent](./././~/Deno.lint.RegExpLiteral#property_parent)
-   [range](./././~/Deno.lint.RegExpLiteral#property_range)
-   [raw](./././~/Deno.lint.RegExpLiteral#property_raw)
-   [regex](./././~/Deno.lint.RegExpLiteral#property_regex)
-   [type](./././~/Deno.lint.RegExpLiteral#property_type)
-   [value](./././~/Deno.lint.RegExpLiteral#property_value)

I

[Deno.lint.ReportData](./././~/Deno.lint.ReportData "Deno.lint.ReportData")

No documentation available

-   [fix](./././~/Deno.lint.ReportData#method_fix_0)
-   [hint](./././~/Deno.lint.ReportData#property_hint)
-   [message](./././~/Deno.lint.ReportData#property_message)
-   [node](./././~/Deno.lint.ReportData#property_node)
-   [range](./././~/Deno.lint.ReportData#property_range)

I

[Deno.lint.RestElement](./././~/Deno.lint.RestElement "Deno.lint.RestElement")

The rest of function parameters.

-   [argument](./././~/Deno.lint.RestElement#property_argument)
-   [parent](./././~/Deno.lint.RestElement#property_parent)
-   [range](./././~/Deno.lint.RestElement#property_range)
-   [type](./././~/Deno.lint.RestElement#property_type)
-   [typeAnnotation](./././~/Deno.lint.RestElement#property_typeannotation)

I

[Deno.lint.ReturnStatement](./././~/Deno.lint.ReturnStatement "Deno.lint.ReturnStatement")

Returns a value from a function.

-   [argument](./././~/Deno.lint.ReturnStatement#property_argument)
-   [parent](./././~/Deno.lint.ReturnStatement#property_parent)
-   [range](./././~/Deno.lint.ReturnStatement#property_range)
-   [type](./././~/Deno.lint.ReturnStatement#property_type)

I

[Deno.lint.Rule](./././~/Deno.lint.Rule "Deno.lint.Rule")

No documentation available

-   [create](./././~/Deno.lint.Rule#method_create_0)
-   [destroy](./././~/Deno.lint.Rule#method_destroy_0)

I

[Deno.lint.RuleContext](./././~/Deno.lint.RuleContext "Deno.lint.RuleContext")

No documentation available

-   [filename](./././~/Deno.lint.RuleContext#property_filename)
-   [getFilename](./././~/Deno.lint.RuleContext#method_getfilename_0)
-   [getSourceCode](./././~/Deno.lint.RuleContext#method_getsourcecode_0)
-   [id](./././~/Deno.lint.RuleContext#property_id)
-   [report](./././~/Deno.lint.RuleContext#method_report_0)
-   [sourceCode](./././~/Deno.lint.RuleContext#property_sourcecode)

f

[Deno.lint.runPlugin](./././~/Deno.lint.runPlugin "Deno.lint.runPlugin")

This API is useful for testing lint plugins.

I

[Deno.lint.SequenceExpression](./././~/Deno.lint.SequenceExpression "Deno.lint.SequenceExpression")

Execute multiple expressions in sequence.

-   [expressions](./././~/Deno.lint.SequenceExpression#property_expressions)
-   [parent](./././~/Deno.lint.SequenceExpression#property_parent)
-   [range](./././~/Deno.lint.SequenceExpression#property_range)
-   [type](./././~/Deno.lint.SequenceExpression#property_type)

I

[Deno.lint.SourceCode](./././~/Deno.lint.SourceCode "Deno.lint.SourceCode")

No documentation available

-   [ast](./././~/Deno.lint.SourceCode#property_ast)
-   [getAllComments](./././~/Deno.lint.SourceCode#method_getallcomments_0)
-   [getAncestors](./././~/Deno.lint.SourceCode#method_getancestors_0)
-   [getCommentsAfter](./././~/Deno.lint.SourceCode#method_getcommentsafter_0)
-   [getCommentsBefore](./././~/Deno.lint.SourceCode#method_getcommentsbefore_0)
-   [getCommentsInside](./././~/Deno.lint.SourceCode#method_getcommentsinside_0)
-   [getText](./././~/Deno.lint.SourceCode#method_gettext_0)
-   [text](./././~/Deno.lint.SourceCode#property_text)

I

[Deno.lint.SpreadElement](./././~/Deno.lint.SpreadElement "Deno.lint.SpreadElement")

No documentation available

-   [argument](./././~/Deno.lint.SpreadElement#property_argument)
-   [parent](./././~/Deno.lint.SpreadElement#property_parent)
-   [range](./././~/Deno.lint.SpreadElement#property_range)
-   [type](./././~/Deno.lint.SpreadElement#property_type)

T

[Deno.lint.Statement](./././~/Deno.lint.Statement "Deno.lint.Statement")

Union type of all possible statement nodes

I

[Deno.lint.StaticBlock](./././~/Deno.lint.StaticBlock "Deno.lint.StaticBlock")

Static class initializiation block.

-   [body](./././~/Deno.lint.StaticBlock#property_body)
-   [parent](./././~/Deno.lint.StaticBlock#property_parent)
-   [range](./././~/Deno.lint.StaticBlock#property_range)
-   [type](./././~/Deno.lint.StaticBlock#property_type)

I

[Deno.lint.StringLiteral](./././~/Deno.lint.StringLiteral "Deno.lint.StringLiteral")

A string literal

-   [parent](./././~/Deno.lint.StringLiteral#property_parent)
-   [range](./././~/Deno.lint.StringLiteral#property_range)
-   [raw](./././~/Deno.lint.StringLiteral#property_raw)
-   [type](./././~/Deno.lint.StringLiteral#property_type)
-   [value](./././~/Deno.lint.StringLiteral#property_value)

I

[Deno.lint.Super](./././~/Deno.lint.Super "Deno.lint.Super")

The `super` keyword used in classes.

-   [parent](./././~/Deno.lint.Super#property_parent)
-   [range](./././~/Deno.lint.Super#property_range)
-   [type](./././~/Deno.lint.Super#property_type)

I

[Deno.lint.SwitchCase](./././~/Deno.lint.SwitchCase "Deno.lint.SwitchCase")

A single case of a SwitchStatement.

-   [consequent](./././~/Deno.lint.SwitchCase#property_consequent)
-   [parent](./././~/Deno.lint.SwitchCase#property_parent)
-   [range](./././~/Deno.lint.SwitchCase#property_range)
-   [test](./././~/Deno.lint.SwitchCase#property_test)
-   [type](./././~/Deno.lint.SwitchCase#property_type)

I

[Deno.lint.SwitchStatement](./././~/Deno.lint.SwitchStatement "Deno.lint.SwitchStatement")

Match an expression against a series of cases.

-   [cases](./././~/Deno.lint.SwitchStatement#property_cases)
-   [discriminant](./././~/Deno.lint.SwitchStatement#property_discriminant)
-   [parent](./././~/Deno.lint.SwitchStatement#property_parent)
-   [range](./././~/Deno.lint.SwitchStatement#property_range)
-   [type](./././~/Deno.lint.SwitchStatement#property_type)

I

[Deno.lint.TaggedTemplateExpression](./././~/Deno.lint.TaggedTemplateExpression "Deno.lint.TaggedTemplateExpression")

Tagged template expression.

-   [parent](./././~/Deno.lint.TaggedTemplateExpression#property_parent)
-   [quasi](./././~/Deno.lint.TaggedTemplateExpression#property_quasi)
-   [range](./././~/Deno.lint.TaggedTemplateExpression#property_range)
-   [tag](./././~/Deno.lint.TaggedTemplateExpression#property_tag)
-   [type](./././~/Deno.lint.TaggedTemplateExpression#property_type)
-   [typeArguments](./././~/Deno.lint.TaggedTemplateExpression#property_typearguments)

I

[Deno.lint.TemplateElement](./././~/Deno.lint.TemplateElement "Deno.lint.TemplateElement")

The static portion of a template literal.

-   [cooked](./././~/Deno.lint.TemplateElement#property_cooked)
-   [parent](./././~/Deno.lint.TemplateElement#property_parent)
-   [range](./././~/Deno.lint.TemplateElement#property_range)
-   [raw](./././~/Deno.lint.TemplateElement#property_raw)
-   [tail](./././~/Deno.lint.TemplateElement#property_tail)
-   [type](./././~/Deno.lint.TemplateElement#property_type)

I

[Deno.lint.TemplateLiteral](./././~/Deno.lint.TemplateLiteral "Deno.lint.TemplateLiteral")

A template literal string.

-   [expressions](./././~/Deno.lint.TemplateLiteral#property_expressions)
-   [parent](./././~/Deno.lint.TemplateLiteral#property_parent)
-   [quasis](./././~/Deno.lint.TemplateLiteral#property_quasis)
-   [range](./././~/Deno.lint.TemplateLiteral#property_range)
-   [type](./././~/Deno.lint.TemplateLiteral#property_type)

I

[Deno.lint.ThisExpression](./././~/Deno.lint.ThisExpression "Deno.lint.ThisExpression")

The `this` keyword used in classes.

-   [parent](./././~/Deno.lint.ThisExpression#property_parent)
-   [range](./././~/Deno.lint.ThisExpression#property_range)
-   [type](./././~/Deno.lint.ThisExpression#property_type)

I

[Deno.lint.ThrowStatement](./././~/Deno.lint.ThrowStatement "Deno.lint.ThrowStatement")

Throw a user defined exception. Stops execution of the current function.

-   [argument](./././~/Deno.lint.ThrowStatement#property_argument)
-   [parent](./././~/Deno.lint.ThrowStatement#property_parent)
-   [range](./././~/Deno.lint.ThrowStatement#property_range)
-   [type](./././~/Deno.lint.ThrowStatement#property_type)

I

[Deno.lint.TryStatement](./././~/Deno.lint.TryStatement "Deno.lint.TryStatement")

Try/catch statement

-   [block](./././~/Deno.lint.TryStatement#property_block)
-   [finalizer](./././~/Deno.lint.TryStatement#property_finalizer)
-   [handler](./././~/Deno.lint.TryStatement#property_handler)
-   [parent](./././~/Deno.lint.TryStatement#property_parent)
-   [range](./././~/Deno.lint.TryStatement#property_range)
-   [type](./././~/Deno.lint.TryStatement#property_type)

I

[Deno.lint.TSAbstractMethodDefinition](./././~/Deno.lint.TSAbstractMethodDefinition "Deno.lint.TSAbstractMethodDefinition")

No documentation available

-   [accessibility](./././~/Deno.lint.TSAbstractMethodDefinition#property_accessibility)
-   [computed](./././~/Deno.lint.TSAbstractMethodDefinition#property_computed)
-   [key](./././~/Deno.lint.TSAbstractMethodDefinition#property_key)
-   [kind](./././~/Deno.lint.TSAbstractMethodDefinition#property_kind)
-   [optional](./././~/Deno.lint.TSAbstractMethodDefinition#property_optional)
-   [override](./././~/Deno.lint.TSAbstractMethodDefinition#property_override)
-   [parent](./././~/Deno.lint.TSAbstractMethodDefinition#property_parent)
-   [range](./././~/Deno.lint.TSAbstractMethodDefinition#property_range)
-   [static](./././~/Deno.lint.TSAbstractMethodDefinition#property_static)
-   [type](./././~/Deno.lint.TSAbstractMethodDefinition#property_type)
-   [value](./././~/Deno.lint.TSAbstractMethodDefinition#property_value)

I

[Deno.lint.TSAbstractPropertyDefinition](./././~/Deno.lint.TSAbstractPropertyDefinition "Deno.lint.TSAbstractPropertyDefinition")

No documentation available

-   [accessibility](./././~/Deno.lint.TSAbstractPropertyDefinition#property_accessibility)
-   [computed](./././~/Deno.lint.TSAbstractPropertyDefinition#property_computed)
-   [declare](./././~/Deno.lint.TSAbstractPropertyDefinition#property_declare)
-   [decorators](./././~/Deno.lint.TSAbstractPropertyDefinition#property_decorators)
-   [definite](./././~/Deno.lint.TSAbstractPropertyDefinition#property_definite)
-   [key](./././~/Deno.lint.TSAbstractPropertyDefinition#property_key)
-   [optional](./././~/Deno.lint.TSAbstractPropertyDefinition#property_optional)
-   [override](./././~/Deno.lint.TSAbstractPropertyDefinition#property_override)
-   [parent](./././~/Deno.lint.TSAbstractPropertyDefinition#property_parent)
-   [range](./././~/Deno.lint.TSAbstractPropertyDefinition#property_range)
-   [readonly](./././~/Deno.lint.TSAbstractPropertyDefinition#property_readonly)
-   [static](./././~/Deno.lint.TSAbstractPropertyDefinition#property_static)
-   [type](./././~/Deno.lint.TSAbstractPropertyDefinition#property_type)
-   [typeAnnotation](./././~/Deno.lint.TSAbstractPropertyDefinition#property_typeannotation)
-   [value](./././~/Deno.lint.TSAbstractPropertyDefinition#property_value)

I

[Deno.lint.TSAnyKeyword](./././~/Deno.lint.TSAnyKeyword "Deno.lint.TSAnyKeyword")

No documentation available

-   [parent](./././~/Deno.lint.TSAnyKeyword#property_parent)
-   [range](./././~/Deno.lint.TSAnyKeyword#property_range)
-   [type](./././~/Deno.lint.TSAnyKeyword#property_type)

I

[Deno.lint.TSArrayType](./././~/Deno.lint.TSArrayType "Deno.lint.TSArrayType")

No documentation available

-   [elementType](./././~/Deno.lint.TSArrayType#property_elementtype)
-   [parent](./././~/Deno.lint.TSArrayType#property_parent)
-   [range](./././~/Deno.lint.TSArrayType#property_range)
-   [type](./././~/Deno.lint.TSArrayType#property_type)

I

[Deno.lint.TSAsExpression](./././~/Deno.lint.TSAsExpression "Deno.lint.TSAsExpression")

No documentation available

-   [expression](./././~/Deno.lint.TSAsExpression#property_expression)
-   [parent](./././~/Deno.lint.TSAsExpression#property_parent)
-   [range](./././~/Deno.lint.TSAsExpression#property_range)
-   [type](./././~/Deno.lint.TSAsExpression#property_type)
-   [typeAnnotation](./././~/Deno.lint.TSAsExpression#property_typeannotation)

I

[Deno.lint.TSBigIntKeyword](./././~/Deno.lint.TSBigIntKeyword "Deno.lint.TSBigIntKeyword")

No documentation available

-   [parent](./././~/Deno.lint.TSBigIntKeyword#property_parent)
-   [range](./././~/Deno.lint.TSBigIntKeyword#property_range)
-   [type](./././~/Deno.lint.TSBigIntKeyword#property_type)

I

[Deno.lint.TSBooleanKeyword](./././~/Deno.lint.TSBooleanKeyword "Deno.lint.TSBooleanKeyword")

No documentation available

-   [parent](./././~/Deno.lint.TSBooleanKeyword#property_parent)
-   [range](./././~/Deno.lint.TSBooleanKeyword#property_range)
-   [type](./././~/Deno.lint.TSBooleanKeyword#property_type)

I

[Deno.lint.TSCallSignatureDeclaration](./././~/Deno.lint.TSCallSignatureDeclaration "Deno.lint.TSCallSignatureDeclaration")

No documentation available

-   [params](./././~/Deno.lint.TSCallSignatureDeclaration#property_params)
-   [parent](./././~/Deno.lint.TSCallSignatureDeclaration#property_parent)
-   [range](./././~/Deno.lint.TSCallSignatureDeclaration#property_range)
-   [returnType](./././~/Deno.lint.TSCallSignatureDeclaration#property_returntype)
-   [type](./././~/Deno.lint.TSCallSignatureDeclaration#property_type)
-   [typeParameters](./././~/Deno.lint.TSCallSignatureDeclaration#property_typeparameters)

I

[Deno.lint.TSClassImplements](./././~/Deno.lint.TSClassImplements "Deno.lint.TSClassImplements")

No documentation available

-   [expression](./././~/Deno.lint.TSClassImplements#property_expression)
-   [parent](./././~/Deno.lint.TSClassImplements#property_parent)
-   [range](./././~/Deno.lint.TSClassImplements#property_range)
-   [type](./././~/Deno.lint.TSClassImplements#property_type)
-   [typeArguments](./././~/Deno.lint.TSClassImplements#property_typearguments)

I

[Deno.lint.TSConditionalType](./././~/Deno.lint.TSConditionalType "Deno.lint.TSConditionalType")

No documentation available

-   [checkType](./././~/Deno.lint.TSConditionalType#property_checktype)
-   [extendsType](./././~/Deno.lint.TSConditionalType#property_extendstype)
-   [falseType](./././~/Deno.lint.TSConditionalType#property_falsetype)
-   [parent](./././~/Deno.lint.TSConditionalType#property_parent)
-   [range](./././~/Deno.lint.TSConditionalType#property_range)
-   [trueType](./././~/Deno.lint.TSConditionalType#property_truetype)
-   [type](./././~/Deno.lint.TSConditionalType#property_type)

I

[Deno.lint.TSConstructSignatureDeclaration](./././~/Deno.lint.TSConstructSignatureDeclaration "Deno.lint.TSConstructSignatureDeclaration")

No documentation available

-   [params](./././~/Deno.lint.TSConstructSignatureDeclaration#property_params)
-   [parent](./././~/Deno.lint.TSConstructSignatureDeclaration#property_parent)
-   [range](./././~/Deno.lint.TSConstructSignatureDeclaration#property_range)
-   [returnType](./././~/Deno.lint.TSConstructSignatureDeclaration#property_returntype)
-   [type](./././~/Deno.lint.TSConstructSignatureDeclaration#property_type)
-   [typeParameters](./././~/Deno.lint.TSConstructSignatureDeclaration#property_typeparameters)

I

[Deno.lint.TSDeclareFunction](./././~/Deno.lint.TSDeclareFunction "Deno.lint.TSDeclareFunction")

No documentation available

-   [async](./././~/Deno.lint.TSDeclareFunction#property_async)
-   [body](./././~/Deno.lint.TSDeclareFunction#property_body)
-   [declare](./././~/Deno.lint.TSDeclareFunction#property_declare)
-   [generator](./././~/Deno.lint.TSDeclareFunction#property_generator)
-   [id](./././~/Deno.lint.TSDeclareFunction#property_id)
-   [params](./././~/Deno.lint.TSDeclareFunction#property_params)
-   [parent](./././~/Deno.lint.TSDeclareFunction#property_parent)
-   [range](./././~/Deno.lint.TSDeclareFunction#property_range)
-   [returnType](./././~/Deno.lint.TSDeclareFunction#property_returntype)
-   [type](./././~/Deno.lint.TSDeclareFunction#property_type)
-   [typeParameters](./././~/Deno.lint.TSDeclareFunction#property_typeparameters)

I

[Deno.lint.TSEmptyBodyFunctionExpression](./././~/Deno.lint.TSEmptyBodyFunctionExpression "Deno.lint.TSEmptyBodyFunctionExpression")

No documentation available

-   [async](./././~/Deno.lint.TSEmptyBodyFunctionExpression#property_async)
-   [body](./././~/Deno.lint.TSEmptyBodyFunctionExpression#property_body)
-   [declare](./././~/Deno.lint.TSEmptyBodyFunctionExpression#property_declare)
-   [expression](./././~/Deno.lint.TSEmptyBodyFunctionExpression#property_expression)
-   [generator](./././~/Deno.lint.TSEmptyBodyFunctionExpression#property_generator)
-   [id](./././~/Deno.lint.TSEmptyBodyFunctionExpression#property_id)
-   [params](./././~/Deno.lint.TSEmptyBodyFunctionExpression#property_params)
-   [parent](./././~/Deno.lint.TSEmptyBodyFunctionExpression#property_parent)
-   [range](./././~/Deno.lint.TSEmptyBodyFunctionExpression#property_range)
-   [returnType](./././~/Deno.lint.TSEmptyBodyFunctionExpression#property_returntype)
-   [type](./././~/Deno.lint.TSEmptyBodyFunctionExpression#property_type)
-   [typeParameters](./././~/Deno.lint.TSEmptyBodyFunctionExpression#property_typeparameters)

I

[Deno.lint.TSEnumBody](./././~/Deno.lint.TSEnumBody "Deno.lint.TSEnumBody")

The body of a `TSEnumDeclaration`

-   [members](./././~/Deno.lint.TSEnumBody#property_members)
-   [parent](./././~/Deno.lint.TSEnumBody#property_parent)
-   [range](./././~/Deno.lint.TSEnumBody#property_range)
-   [type](./././~/Deno.lint.TSEnumBody#property_type)

I

[Deno.lint.TSEnumDeclaration](./././~/Deno.lint.TSEnumDeclaration "Deno.lint.TSEnumDeclaration")

No documentation available

-   [body](./././~/Deno.lint.TSEnumDeclaration#property_body)
-   [const](./././~/Deno.lint.TSEnumDeclaration#property_const)
-   [declare](./././~/Deno.lint.TSEnumDeclaration#property_declare)
-   [id](./././~/Deno.lint.TSEnumDeclaration#property_id)
-   [parent](./././~/Deno.lint.TSEnumDeclaration#property_parent)
-   [range](./././~/Deno.lint.TSEnumDeclaration#property_range)
-   [type](./././~/Deno.lint.TSEnumDeclaration#property_type)

I

[Deno.lint.TSEnumMember](./././~/Deno.lint.TSEnumMember "Deno.lint.TSEnumMember")

A member of a `TSEnumDeclaration`

-   [id](./././~/Deno.lint.TSEnumMember#property_id)
-   [initializer](./././~/Deno.lint.TSEnumMember#property_initializer)
-   [parent](./././~/Deno.lint.TSEnumMember#property_parent)
-   [range](./././~/Deno.lint.TSEnumMember#property_range)
-   [type](./././~/Deno.lint.TSEnumMember#property_type)

I

[Deno.lint.TSExportAssignment](./././~/Deno.lint.TSExportAssignment "Deno.lint.TSExportAssignment")

No documentation available

-   [expression](./././~/Deno.lint.TSExportAssignment#property_expression)
-   [parent](./././~/Deno.lint.TSExportAssignment#property_parent)
-   [range](./././~/Deno.lint.TSExportAssignment#property_range)
-   [type](./././~/Deno.lint.TSExportAssignment#property_type)

I

[Deno.lint.TSExternalModuleReference](./././~/Deno.lint.TSExternalModuleReference "Deno.lint.TSExternalModuleReference")

No documentation available

-   [expression](./././~/Deno.lint.TSExternalModuleReference#property_expression)
-   [parent](./././~/Deno.lint.TSExternalModuleReference#property_parent)
-   [range](./././~/Deno.lint.TSExternalModuleReference#property_range)
-   [type](./././~/Deno.lint.TSExternalModuleReference#property_type)

I

[Deno.lint.TSFunctionType](./././~/Deno.lint.TSFunctionType "Deno.lint.TSFunctionType")

No documentation available

-   [params](./././~/Deno.lint.TSFunctionType#property_params)
-   [parent](./././~/Deno.lint.TSFunctionType#property_parent)
-   [range](./././~/Deno.lint.TSFunctionType#property_range)
-   [returnType](./././~/Deno.lint.TSFunctionType#property_returntype)
-   [type](./././~/Deno.lint.TSFunctionType#property_type)
-   [typeParameters](./././~/Deno.lint.TSFunctionType#property_typeparameters)

I

[Deno.lint.TSImportEqualsDeclaration](./././~/Deno.lint.TSImportEqualsDeclaration "Deno.lint.TSImportEqualsDeclaration")

No documentation available

-   [id](./././~/Deno.lint.TSImportEqualsDeclaration#property_id)
-   [importKind](./././~/Deno.lint.TSImportEqualsDeclaration#property_importkind)
-   [moduleReference](./././~/Deno.lint.TSImportEqualsDeclaration#property_modulereference)
-   [parent](./././~/Deno.lint.TSImportEqualsDeclaration#property_parent)
-   [range](./././~/Deno.lint.TSImportEqualsDeclaration#property_range)
-   [type](./././~/Deno.lint.TSImportEqualsDeclaration#property_type)

I

[Deno.lint.TSImportType](./././~/Deno.lint.TSImportType "Deno.lint.TSImportType")

No documentation available

-   [argument](./././~/Deno.lint.TSImportType#property_argument)
-   [parent](./././~/Deno.lint.TSImportType#property_parent)
-   [qualifier](./././~/Deno.lint.TSImportType#property_qualifier)
-   [range](./././~/Deno.lint.TSImportType#property_range)
-   [type](./././~/Deno.lint.TSImportType#property_type)
-   [typeArguments](./././~/Deno.lint.TSImportType#property_typearguments)

I

[Deno.lint.TSIndexedAccessType](./././~/Deno.lint.TSIndexedAccessType "Deno.lint.TSIndexedAccessType")

No documentation available

-   [indexType](./././~/Deno.lint.TSIndexedAccessType#property_indextype)
-   [objectType](./././~/Deno.lint.TSIndexedAccessType#property_objecttype)
-   [parent](./././~/Deno.lint.TSIndexedAccessType#property_parent)
-   [range](./././~/Deno.lint.TSIndexedAccessType#property_range)
-   [type](./././~/Deno.lint.TSIndexedAccessType#property_type)

I

[Deno.lint.TSIndexSignature](./././~/Deno.lint.TSIndexSignature "Deno.lint.TSIndexSignature")

No documentation available

-   [parameters](./././~/Deno.lint.TSIndexSignature#property_parameters)
-   [parent](./././~/Deno.lint.TSIndexSignature#property_parent)
-   [range](./././~/Deno.lint.TSIndexSignature#property_range)
-   [readonly](./././~/Deno.lint.TSIndexSignature#property_readonly)
-   [static](./././~/Deno.lint.TSIndexSignature#property_static)
-   [type](./././~/Deno.lint.TSIndexSignature#property_type)
-   [typeAnnotation](./././~/Deno.lint.TSIndexSignature#property_typeannotation)

I

[Deno.lint.TSInferType](./././~/Deno.lint.TSInferType "Deno.lint.TSInferType")

No documentation available

-   [parent](./././~/Deno.lint.TSInferType#property_parent)
-   [range](./././~/Deno.lint.TSInferType#property_range)
-   [type](./././~/Deno.lint.TSInferType#property_type)
-   [typeParameter](./././~/Deno.lint.TSInferType#property_typeparameter)

I

[Deno.lint.TSInstantiationExpression](./././~/Deno.lint.TSInstantiationExpression "Deno.lint.TSInstantiationExpression")

No documentation available

-   [expression](./././~/Deno.lint.TSInstantiationExpression#property_expression)
-   [parent](./././~/Deno.lint.TSInstantiationExpression#property_parent)
-   [range](./././~/Deno.lint.TSInstantiationExpression#property_range)
-   [type](./././~/Deno.lint.TSInstantiationExpression#property_type)
-   [typeArguments](./././~/Deno.lint.TSInstantiationExpression#property_typearguments)

I

[Deno.lint.TSInterfaceBody](./././~/Deno.lint.TSInterfaceBody "Deno.lint.TSInterfaceBody")

No documentation available

-   [body](./././~/Deno.lint.TSInterfaceBody#property_body)
-   [parent](./././~/Deno.lint.TSInterfaceBody#property_parent)
-   [range](./././~/Deno.lint.TSInterfaceBody#property_range)
-   [type](./././~/Deno.lint.TSInterfaceBody#property_type)

I

[Deno.lint.TSInterfaceDeclaration](./././~/Deno.lint.TSInterfaceDeclaration "Deno.lint.TSInterfaceDeclaration")

No documentation available

-   [body](./././~/Deno.lint.TSInterfaceDeclaration#property_body)
-   [declare](./././~/Deno.lint.TSInterfaceDeclaration#property_declare)
-   [extends](./././~/Deno.lint.TSInterfaceDeclaration#property_extends)
-   [id](./././~/Deno.lint.TSInterfaceDeclaration#property_id)
-   [parent](./././~/Deno.lint.TSInterfaceDeclaration#property_parent)
-   [range](./././~/Deno.lint.TSInterfaceDeclaration#property_range)
-   [type](./././~/Deno.lint.TSInterfaceDeclaration#property_type)
-   [typeParameters](./././~/Deno.lint.TSInterfaceDeclaration#property_typeparameters)

I

[Deno.lint.TSInterfaceHeritage](./././~/Deno.lint.TSInterfaceHeritage "Deno.lint.TSInterfaceHeritage")

No documentation available

-   [expression](./././~/Deno.lint.TSInterfaceHeritage#property_expression)
-   [parent](./././~/Deno.lint.TSInterfaceHeritage#property_parent)
-   [range](./././~/Deno.lint.TSInterfaceHeritage#property_range)
-   [type](./././~/Deno.lint.TSInterfaceHeritage#property_type)
-   [typeArguments](./././~/Deno.lint.TSInterfaceHeritage#property_typearguments)

I

[Deno.lint.TSIntersectionType](./././~/Deno.lint.TSIntersectionType "Deno.lint.TSIntersectionType")

No documentation available

-   [parent](./././~/Deno.lint.TSIntersectionType#property_parent)
-   [range](./././~/Deno.lint.TSIntersectionType#property_range)
-   [type](./././~/Deno.lint.TSIntersectionType#property_type)
-   [types](./././~/Deno.lint.TSIntersectionType#property_types)

I

[Deno.lint.TSIntrinsicKeyword](./././~/Deno.lint.TSIntrinsicKeyword "Deno.lint.TSIntrinsicKeyword")

No documentation available

-   [parent](./././~/Deno.lint.TSIntrinsicKeyword#property_parent)
-   [range](./././~/Deno.lint.TSIntrinsicKeyword#property_range)
-   [type](./././~/Deno.lint.TSIntrinsicKeyword#property_type)

I

[Deno.lint.TSLiteralType](./././~/Deno.lint.TSLiteralType "Deno.lint.TSLiteralType")

No documentation available

-   [literal](./././~/Deno.lint.TSLiteralType#property_literal)
-   [parent](./././~/Deno.lint.TSLiteralType#property_parent)
-   [range](./././~/Deno.lint.TSLiteralType#property_range)
-   [type](./././~/Deno.lint.TSLiteralType#property_type)

I

[Deno.lint.TSMappedType](./././~/Deno.lint.TSMappedType "Deno.lint.TSMappedType")

No documentation available

-   [constraint](./././~/Deno.lint.TSMappedType#property_constraint)
-   [key](./././~/Deno.lint.TSMappedType#property_key)
-   [nameType](./././~/Deno.lint.TSMappedType#property_nametype)
-   [optional](./././~/Deno.lint.TSMappedType#property_optional)
-   [parent](./././~/Deno.lint.TSMappedType#property_parent)
-   [range](./././~/Deno.lint.TSMappedType#property_range)
-   [readonly](./././~/Deno.lint.TSMappedType#property_readonly)
-   [type](./././~/Deno.lint.TSMappedType#property_type)
-   [typeAnnotation](./././~/Deno.lint.TSMappedType#property_typeannotation)

I

[Deno.lint.TSMethodSignature](./././~/Deno.lint.TSMethodSignature "Deno.lint.TSMethodSignature")

No documentation available

-   [computed](./././~/Deno.lint.TSMethodSignature#property_computed)
-   [key](./././~/Deno.lint.TSMethodSignature#property_key)
-   [kind](./././~/Deno.lint.TSMethodSignature#property_kind)
-   [optional](./././~/Deno.lint.TSMethodSignature#property_optional)
-   [params](./././~/Deno.lint.TSMethodSignature#property_params)
-   [parent](./././~/Deno.lint.TSMethodSignature#property_parent)
-   [range](./././~/Deno.lint.TSMethodSignature#property_range)
-   [readonly](./././~/Deno.lint.TSMethodSignature#property_readonly)
-   [returnType](./././~/Deno.lint.TSMethodSignature#property_returntype)
-   [static](./././~/Deno.lint.TSMethodSignature#property_static)
-   [type](./././~/Deno.lint.TSMethodSignature#property_type)
-   [typeParameters](./././~/Deno.lint.TSMethodSignature#property_typeparameters)

I

[Deno.lint.TSModuleBlock](./././~/Deno.lint.TSModuleBlock "Deno.lint.TSModuleBlock")

Body of a `TSModuleDeclaration`

-   [body](./././~/Deno.lint.TSModuleBlock#property_body)
-   [parent](./././~/Deno.lint.TSModuleBlock#property_parent)
-   [range](./././~/Deno.lint.TSModuleBlock#property_range)
-   [type](./././~/Deno.lint.TSModuleBlock#property_type)

I

[Deno.lint.TSModuleDeclaration](./././~/Deno.lint.TSModuleDeclaration "Deno.lint.TSModuleDeclaration")

No documentation available

-   [body](./././~/Deno.lint.TSModuleDeclaration#property_body)
-   [declare](./././~/Deno.lint.TSModuleDeclaration#property_declare)
-   [id](./././~/Deno.lint.TSModuleDeclaration#property_id)
-   [kind](./././~/Deno.lint.TSModuleDeclaration#property_kind)
-   [parent](./././~/Deno.lint.TSModuleDeclaration#property_parent)
-   [range](./././~/Deno.lint.TSModuleDeclaration#property_range)
-   [type](./././~/Deno.lint.TSModuleDeclaration#property_type)

I

[Deno.lint.TSNamedTupleMember](./././~/Deno.lint.TSNamedTupleMember "Deno.lint.TSNamedTupleMember")

No documentation available

-   [elementType](./././~/Deno.lint.TSNamedTupleMember#property_elementtype)
-   [label](./././~/Deno.lint.TSNamedTupleMember#property_label)
-   [optional](./././~/Deno.lint.TSNamedTupleMember#property_optional)
-   [parent](./././~/Deno.lint.TSNamedTupleMember#property_parent)
-   [range](./././~/Deno.lint.TSNamedTupleMember#property_range)
-   [type](./././~/Deno.lint.TSNamedTupleMember#property_type)

I

[Deno.lint.TSNamespaceExportDeclaration](./././~/Deno.lint.TSNamespaceExportDeclaration "Deno.lint.TSNamespaceExportDeclaration")

No documentation available

-   [id](./././~/Deno.lint.TSNamespaceExportDeclaration#property_id)
-   [parent](./././~/Deno.lint.TSNamespaceExportDeclaration#property_parent)
-   [range](./././~/Deno.lint.TSNamespaceExportDeclaration#property_range)
-   [type](./././~/Deno.lint.TSNamespaceExportDeclaration#property_type)

I

[Deno.lint.TSNeverKeyword](./././~/Deno.lint.TSNeverKeyword "Deno.lint.TSNeverKeyword")

No documentation available

-   [parent](./././~/Deno.lint.TSNeverKeyword#property_parent)
-   [range](./././~/Deno.lint.TSNeverKeyword#property_range)
-   [type](./././~/Deno.lint.TSNeverKeyword#property_type)

I

[Deno.lint.TSNonNullExpression](./././~/Deno.lint.TSNonNullExpression "Deno.lint.TSNonNullExpression")

No documentation available

-   [expression](./././~/Deno.lint.TSNonNullExpression#property_expression)
-   [parent](./././~/Deno.lint.TSNonNullExpression#property_parent)
-   [range](./././~/Deno.lint.TSNonNullExpression#property_range)
-   [type](./././~/Deno.lint.TSNonNullExpression#property_type)

I

[Deno.lint.TSNullKeyword](./././~/Deno.lint.TSNullKeyword "Deno.lint.TSNullKeyword")

No documentation available

-   [parent](./././~/Deno.lint.TSNullKeyword#property_parent)
-   [range](./././~/Deno.lint.TSNullKeyword#property_range)
-   [type](./././~/Deno.lint.TSNullKeyword#property_type)

I

[Deno.lint.TSNumberKeyword](./././~/Deno.lint.TSNumberKeyword "Deno.lint.TSNumberKeyword")

No documentation available

-   [parent](./././~/Deno.lint.TSNumberKeyword#property_parent)
-   [range](./././~/Deno.lint.TSNumberKeyword#property_range)
-   [type](./././~/Deno.lint.TSNumberKeyword#property_type)

I

[Deno.lint.TSObjectKeyword](./././~/Deno.lint.TSObjectKeyword "Deno.lint.TSObjectKeyword")

No documentation available

-   [parent](./././~/Deno.lint.TSObjectKeyword#property_parent)
-   [range](./././~/Deno.lint.TSObjectKeyword#property_range)
-   [type](./././~/Deno.lint.TSObjectKeyword#property_type)

I

[Deno.lint.TSOptionalType](./././~/Deno.lint.TSOptionalType "Deno.lint.TSOptionalType")

No documentation available

-   [parent](./././~/Deno.lint.TSOptionalType#property_parent)
-   [range](./././~/Deno.lint.TSOptionalType#property_range)
-   [type](./././~/Deno.lint.TSOptionalType#property_type)
-   [typeAnnotation](./././~/Deno.lint.TSOptionalType#property_typeannotation)

I

[Deno.lint.TSParameterProperty](./././~/Deno.lint.TSParameterProperty "Deno.lint.TSParameterProperty")

No documentation available

-   [accessibility](./././~/Deno.lint.TSParameterProperty#property_accessibility)
-   [decorators](./././~/Deno.lint.TSParameterProperty#property_decorators)
-   [override](./././~/Deno.lint.TSParameterProperty#property_override)
-   [parameter](./././~/Deno.lint.TSParameterProperty#property_parameter)
-   [parent](./././~/Deno.lint.TSParameterProperty#property_parent)
-   [range](./././~/Deno.lint.TSParameterProperty#property_range)
-   [readonly](./././~/Deno.lint.TSParameterProperty#property_readonly)
-   [static](./././~/Deno.lint.TSParameterProperty#property_static)
-   [type](./././~/Deno.lint.TSParameterProperty#property_type)

I

[Deno.lint.TSPropertySignature](./././~/Deno.lint.TSPropertySignature "Deno.lint.TSPropertySignature")

No documentation available

-   [computed](./././~/Deno.lint.TSPropertySignature#property_computed)
-   [key](./././~/Deno.lint.TSPropertySignature#property_key)
-   [optional](./././~/Deno.lint.TSPropertySignature#property_optional)
-   [parent](./././~/Deno.lint.TSPropertySignature#property_parent)
-   [range](./././~/Deno.lint.TSPropertySignature#property_range)
-   [readonly](./././~/Deno.lint.TSPropertySignature#property_readonly)
-   [static](./././~/Deno.lint.TSPropertySignature#property_static)
-   [type](./././~/Deno.lint.TSPropertySignature#property_type)
-   [typeAnnotation](./././~/Deno.lint.TSPropertySignature#property_typeannotation)

I

[Deno.lint.TSQualifiedName](./././~/Deno.lint.TSQualifiedName "Deno.lint.TSQualifiedName")

No documentation available

-   [left](./././~/Deno.lint.TSQualifiedName#property_left)
-   [parent](./././~/Deno.lint.TSQualifiedName#property_parent)
-   [range](./././~/Deno.lint.TSQualifiedName#property_range)
-   [right](./././~/Deno.lint.TSQualifiedName#property_right)
-   [type](./././~/Deno.lint.TSQualifiedName#property_type)

I

[Deno.lint.TSRestType](./././~/Deno.lint.TSRestType "Deno.lint.TSRestType")

No documentation available

-   [parent](./././~/Deno.lint.TSRestType#property_parent)
-   [range](./././~/Deno.lint.TSRestType#property_range)
-   [type](./././~/Deno.lint.TSRestType#property_type)
-   [typeAnnotation](./././~/Deno.lint.TSRestType#property_typeannotation)

I

[Deno.lint.TSSatisfiesExpression](./././~/Deno.lint.TSSatisfiesExpression "Deno.lint.TSSatisfiesExpression")

No documentation available

-   [expression](./././~/Deno.lint.TSSatisfiesExpression#property_expression)
-   [parent](./././~/Deno.lint.TSSatisfiesExpression#property_parent)
-   [range](./././~/Deno.lint.TSSatisfiesExpression#property_range)
-   [type](./././~/Deno.lint.TSSatisfiesExpression#property_type)
-   [typeAnnotation](./././~/Deno.lint.TSSatisfiesExpression#property_typeannotation)

I

[Deno.lint.TSStringKeyword](./././~/Deno.lint.TSStringKeyword "Deno.lint.TSStringKeyword")

No documentation available

-   [parent](./././~/Deno.lint.TSStringKeyword#property_parent)
-   [range](./././~/Deno.lint.TSStringKeyword#property_range)
-   [type](./././~/Deno.lint.TSStringKeyword#property_type)

I

[Deno.lint.TSSymbolKeyword](./././~/Deno.lint.TSSymbolKeyword "Deno.lint.TSSymbolKeyword")

No documentation available

-   [parent](./././~/Deno.lint.TSSymbolKeyword#property_parent)
-   [range](./././~/Deno.lint.TSSymbolKeyword#property_range)
-   [type](./././~/Deno.lint.TSSymbolKeyword#property_type)

I

[Deno.lint.TSTemplateLiteralType](./././~/Deno.lint.TSTemplateLiteralType "Deno.lint.TSTemplateLiteralType")

No documentation available

-   [parent](./././~/Deno.lint.TSTemplateLiteralType#property_parent)
-   [quasis](./././~/Deno.lint.TSTemplateLiteralType#property_quasis)
-   [range](./././~/Deno.lint.TSTemplateLiteralType#property_range)
-   [type](./././~/Deno.lint.TSTemplateLiteralType#property_type)
-   [types](./././~/Deno.lint.TSTemplateLiteralType#property_types)

I

[Deno.lint.TSThisType](./././~/Deno.lint.TSThisType "Deno.lint.TSThisType")

No documentation available

-   [parent](./././~/Deno.lint.TSThisType#property_parent)
-   [range](./././~/Deno.lint.TSThisType#property_range)
-   [type](./././~/Deno.lint.TSThisType#property_type)

I

[Deno.lint.TSTupleType](./././~/Deno.lint.TSTupleType "Deno.lint.TSTupleType")

No documentation available

-   [elementTypes](./././~/Deno.lint.TSTupleType#property_elementtypes)
-   [parent](./././~/Deno.lint.TSTupleType#property_parent)
-   [range](./././~/Deno.lint.TSTupleType#property_range)
-   [type](./././~/Deno.lint.TSTupleType#property_type)

I

[Deno.lint.TSTypeAliasDeclaration](./././~/Deno.lint.TSTypeAliasDeclaration "Deno.lint.TSTypeAliasDeclaration")

No documentation available

-   [declare](./././~/Deno.lint.TSTypeAliasDeclaration#property_declare)
-   [id](./././~/Deno.lint.TSTypeAliasDeclaration#property_id)
-   [parent](./././~/Deno.lint.TSTypeAliasDeclaration#property_parent)
-   [range](./././~/Deno.lint.TSTypeAliasDeclaration#property_range)
-   [type](./././~/Deno.lint.TSTypeAliasDeclaration#property_type)
-   [typeAnnotation](./././~/Deno.lint.TSTypeAliasDeclaration#property_typeannotation)
-   [typeParameters](./././~/Deno.lint.TSTypeAliasDeclaration#property_typeparameters)

I

[Deno.lint.TSTypeAnnotation](./././~/Deno.lint.TSTypeAnnotation "Deno.lint.TSTypeAnnotation")

No documentation available

-   [parent](./././~/Deno.lint.TSTypeAnnotation#property_parent)
-   [range](./././~/Deno.lint.TSTypeAnnotation#property_range)
-   [type](./././~/Deno.lint.TSTypeAnnotation#property_type)
-   [typeAnnotation](./././~/Deno.lint.TSTypeAnnotation#property_typeannotation)

I

[Deno.lint.TSTypeAssertion](./././~/Deno.lint.TSTypeAssertion "Deno.lint.TSTypeAssertion")

No documentation available

-   [expression](./././~/Deno.lint.TSTypeAssertion#property_expression)
-   [parent](./././~/Deno.lint.TSTypeAssertion#property_parent)
-   [range](./././~/Deno.lint.TSTypeAssertion#property_range)
-   [type](./././~/Deno.lint.TSTypeAssertion#property_type)
-   [typeAnnotation](./././~/Deno.lint.TSTypeAssertion#property_typeannotation)

I

[Deno.lint.TSTypeLiteral](./././~/Deno.lint.TSTypeLiteral "Deno.lint.TSTypeLiteral")

No documentation available

-   [members](./././~/Deno.lint.TSTypeLiteral#property_members)
-   [parent](./././~/Deno.lint.TSTypeLiteral#property_parent)
-   [range](./././~/Deno.lint.TSTypeLiteral#property_range)
-   [type](./././~/Deno.lint.TSTypeLiteral#property_type)

I

[Deno.lint.TSTypeOperator](./././~/Deno.lint.TSTypeOperator "Deno.lint.TSTypeOperator")

No documentation available

-   [operator](./././~/Deno.lint.TSTypeOperator#property_operator)
-   [parent](./././~/Deno.lint.TSTypeOperator#property_parent)
-   [range](./././~/Deno.lint.TSTypeOperator#property_range)
-   [type](./././~/Deno.lint.TSTypeOperator#property_type)
-   [typeAnnotation](./././~/Deno.lint.TSTypeOperator#property_typeannotation)

I

[Deno.lint.TSTypeParameter](./././~/Deno.lint.TSTypeParameter "Deno.lint.TSTypeParameter")

No documentation available

-   [const](./././~/Deno.lint.TSTypeParameter#property_const)
-   [constraint](./././~/Deno.lint.TSTypeParameter#property_constraint)
-   [default](./././~/Deno.lint.TSTypeParameter#property_default)
-   [in](./././~/Deno.lint.TSTypeParameter#property_in)
-   [name](./././~/Deno.lint.TSTypeParameter#property_name)
-   [out](./././~/Deno.lint.TSTypeParameter#property_out)
-   [parent](./././~/Deno.lint.TSTypeParameter#property_parent)
-   [range](./././~/Deno.lint.TSTypeParameter#property_range)
-   [type](./././~/Deno.lint.TSTypeParameter#property_type)

I

[Deno.lint.TSTypeParameterDeclaration](./././~/Deno.lint.TSTypeParameterDeclaration "Deno.lint.TSTypeParameterDeclaration")

No documentation available

-   [params](./././~/Deno.lint.TSTypeParameterDeclaration#property_params)
-   [parent](./././~/Deno.lint.TSTypeParameterDeclaration#property_parent)
-   [range](./././~/Deno.lint.TSTypeParameterDeclaration#property_range)
-   [type](./././~/Deno.lint.TSTypeParameterDeclaration#property_type)

I

[Deno.lint.TSTypeParameterInstantiation](./././~/Deno.lint.TSTypeParameterInstantiation "Deno.lint.TSTypeParameterInstantiation")

No documentation available

-   [params](./././~/Deno.lint.TSTypeParameterInstantiation#property_params)
-   [parent](./././~/Deno.lint.TSTypeParameterInstantiation#property_parent)
-   [range](./././~/Deno.lint.TSTypeParameterInstantiation#property_range)
-   [type](./././~/Deno.lint.TSTypeParameterInstantiation#property_type)

I

[Deno.lint.TSTypePredicate](./././~/Deno.lint.TSTypePredicate "Deno.lint.TSTypePredicate")

No documentation available

-   [asserts](./././~/Deno.lint.TSTypePredicate#property_asserts)
-   [parameterName](./././~/Deno.lint.TSTypePredicate#property_parametername)
-   [parent](./././~/Deno.lint.TSTypePredicate#property_parent)
-   [range](./././~/Deno.lint.TSTypePredicate#property_range)
-   [type](./././~/Deno.lint.TSTypePredicate#property_type)
-   [typeAnnotation](./././~/Deno.lint.TSTypePredicate#property_typeannotation)

I

[Deno.lint.TSTypeQuery](./././~/Deno.lint.TSTypeQuery "Deno.lint.TSTypeQuery")

No documentation available

-   [exprName](./././~/Deno.lint.TSTypeQuery#property_exprname)
-   [parent](./././~/Deno.lint.TSTypeQuery#property_parent)
-   [range](./././~/Deno.lint.TSTypeQuery#property_range)
-   [type](./././~/Deno.lint.TSTypeQuery#property_type)
-   [typeArguments](./././~/Deno.lint.TSTypeQuery#property_typearguments)

I

[Deno.lint.TSTypeReference](./././~/Deno.lint.TSTypeReference "Deno.lint.TSTypeReference")

No documentation available

-   [parent](./././~/Deno.lint.TSTypeReference#property_parent)
-   [range](./././~/Deno.lint.TSTypeReference#property_range)
-   [type](./././~/Deno.lint.TSTypeReference#property_type)
-   [typeArguments](./././~/Deno.lint.TSTypeReference#property_typearguments)
-   [typeName](./././~/Deno.lint.TSTypeReference#property_typename)

I

[Deno.lint.TSUndefinedKeyword](./././~/Deno.lint.TSUndefinedKeyword "Deno.lint.TSUndefinedKeyword")

No documentation available

-   [parent](./././~/Deno.lint.TSUndefinedKeyword#property_parent)
-   [range](./././~/Deno.lint.TSUndefinedKeyword#property_range)
-   [type](./././~/Deno.lint.TSUndefinedKeyword#property_type)

I

[Deno.lint.TSUnionType](./././~/Deno.lint.TSUnionType "Deno.lint.TSUnionType")

No documentation available

-   [parent](./././~/Deno.lint.TSUnionType#property_parent)
-   [range](./././~/Deno.lint.TSUnionType#property_range)
-   [type](./././~/Deno.lint.TSUnionType#property_type)
-   [types](./././~/Deno.lint.TSUnionType#property_types)

I

[Deno.lint.TSUnknownKeyword](./././~/Deno.lint.TSUnknownKeyword "Deno.lint.TSUnknownKeyword")

No documentation available

-   [parent](./././~/Deno.lint.TSUnknownKeyword#property_parent)
-   [range](./././~/Deno.lint.TSUnknownKeyword#property_range)
-   [type](./././~/Deno.lint.TSUnknownKeyword#property_type)

I

[Deno.lint.TSVoidKeyword](./././~/Deno.lint.TSVoidKeyword "Deno.lint.TSVoidKeyword")

No documentation available

-   [parent](./././~/Deno.lint.TSVoidKeyword#property_parent)
-   [range](./././~/Deno.lint.TSVoidKeyword#property_range)
-   [type](./././~/Deno.lint.TSVoidKeyword#property_type)

T

[Deno.lint.TypeNode](./././~/Deno.lint.TypeNode "Deno.lint.TypeNode")

Union type of all possible type nodes in TypeScript

I

[Deno.lint.UnaryExpression](./././~/Deno.lint.UnaryExpression "Deno.lint.UnaryExpression")

Apply operand on value based on the specified operator.

-   [argument](./././~/Deno.lint.UnaryExpression#property_argument)
-   [operator](./././~/Deno.lint.UnaryExpression#property_operator)
-   [parent](./././~/Deno.lint.UnaryExpression#property_parent)
-   [range](./././~/Deno.lint.UnaryExpression#property_range)
-   [type](./././~/Deno.lint.UnaryExpression#property_type)

I

[Deno.lint.UpdateExpression](./././~/Deno.lint.UpdateExpression "Deno.lint.UpdateExpression")

Syntactic sugar to increment or decrement a value.

-   [argument](./././~/Deno.lint.UpdateExpression#property_argument)
-   [operator](./././~/Deno.lint.UpdateExpression#property_operator)
-   [parent](./././~/Deno.lint.UpdateExpression#property_parent)
-   [prefix](./././~/Deno.lint.UpdateExpression#property_prefix)
-   [range](./././~/Deno.lint.UpdateExpression#property_range)
-   [type](./././~/Deno.lint.UpdateExpression#property_type)

I

[Deno.lint.VariableDeclaration](./././~/Deno.lint.VariableDeclaration "Deno.lint.VariableDeclaration")

Variable declaration.

-   [declarations](./././~/Deno.lint.VariableDeclaration#property_declarations)
-   [declare](./././~/Deno.lint.VariableDeclaration#property_declare)
-   [kind](./././~/Deno.lint.VariableDeclaration#property_kind)
-   [parent](./././~/Deno.lint.VariableDeclaration#property_parent)
-   [range](./././~/Deno.lint.VariableDeclaration#property_range)
-   [type](./././~/Deno.lint.VariableDeclaration#property_type)

I

[Deno.lint.VariableDeclarator](./././~/Deno.lint.VariableDeclarator "Deno.lint.VariableDeclarator")

A VariableDeclaration can declare multiple variables. This node represents a single declaration out of that.

-   [definite](./././~/Deno.lint.VariableDeclarator#property_definite)
-   [id](./././~/Deno.lint.VariableDeclarator#property_id)
-   [init](./././~/Deno.lint.VariableDeclarator#property_init)
-   [parent](./././~/Deno.lint.VariableDeclarator#property_parent)
-   [range](./././~/Deno.lint.VariableDeclarator#property_range)
-   [type](./././~/Deno.lint.VariableDeclarator#property_type)

I

[Deno.lint.WhileStatement](./././~/Deno.lint.WhileStatement "Deno.lint.WhileStatement")

Run a loop while the test expression is truthy.

-   [body](./././~/Deno.lint.WhileStatement#property_body)
-   [parent](./././~/Deno.lint.WhileStatement#property_parent)
-   [range](./././~/Deno.lint.WhileStatement#property_range)
-   [test](./././~/Deno.lint.WhileStatement#property_test)
-   [type](./././~/Deno.lint.WhileStatement#property_type)

I

[Deno.lint.YieldExpression](./././~/Deno.lint.YieldExpression "Deno.lint.YieldExpression")

Pause or resume a generator function.

-   [argument](./././~/Deno.lint.YieldExpression#property_argument)
-   [delegate](./././~/Deno.lint.YieldExpression#property_delegate)
-   [parent](./././~/Deno.lint.YieldExpression#property_parent)
-   [range](./././~/Deno.lint.YieldExpression#property_range)
-   [type](./././~/Deno.lint.YieldExpression#property_type)

f

[Deno.listen](./././~/Deno.listen "Deno.listen")

Listen announces on the local transport address.

f

[Deno.listenDatagram](./././~/Deno.listenDatagram "Deno.listenDatagram")

Listen announces on the local transport address.

I

[Deno.Listener](./././~/Deno.Listener "Deno.Listener")

A generic network listener for stream-oriented protocols.

-   [accept](./././~/Deno.Listener#method_accept_0)
-   [addr](./././~/Deno.Listener#property_addr)
-   [close](./././~/Deno.Listener#method_close_0)
-   [ref](./././~/Deno.Listener#method_ref_0)
-   [unref](./././~/Deno.Listener#method_unref_0)

I

[Deno.ListenOptions](./././~/Deno.ListenOptions "Deno.ListenOptions")

No documentation available

-   [hostname](./././~/Deno.ListenOptions#property_hostname)
-   [port](./././~/Deno.ListenOptions#property_port)
-   [tcpBacklog](./././~/Deno.ListenOptions#property_tcpbacklog)

f

[Deno.listenTls](./././~/Deno.listenTls "Deno.listenTls")

Listen announces on the local transport address over TLS (transport layer security).

I

[Deno.ListenTlsOptions](./././~/Deno.ListenTlsOptions "Deno.ListenTlsOptions")

No documentation available

-   [alpnProtocols](./././~/Deno.ListenTlsOptions#property_alpnprotocols)
-   [transport](./././~/Deno.ListenTlsOptions#property_transport)

f

[Deno.loadavg](./././~/Deno.loadavg "Deno.loadavg")

Returns an array containing the 1, 5, and 15 minute load averages. The load average is a measure of CPU and IO utilization of the last one, five, and 15 minute periods expressed as a fractional number. Zero means there is no load. On Windows, the three values are always the same and represent the current load, not the 1, 5 and 15 minute load averages.

f

[Deno.lstat](./././~/Deno.lstat "Deno.lstat")

Resolves to a [`Deno.FileInfo`](./././~/Deno.FileInfo) for the specified `path`. If `path` is a symlink, information for the symlink will be returned instead of what it points to.

f

[Deno.lstatSync](./././~/Deno.lstatSync "Deno.lstatSync")

Synchronously returns a [`Deno.FileInfo`](./././~/Deno.FileInfo) for the specified `path`. If `path` is a symlink, information for the symlink will be returned instead of what it points to.

v

[Deno.mainModule](./././~/Deno.mainModule "Deno.mainModule")

The URL of the entrypoint module entered from the command-line. It requires read permission to the CWD.

f

[Deno.makeTempDir](./././~/Deno.makeTempDir "Deno.makeTempDir")

Creates a new temporary directory in the default directory for temporary files, unless `dir` is specified. Other optional options include prefixing and suffixing the directory name with `prefix` and `suffix` respectively.

f

[Deno.makeTempDirSync](./././~/Deno.makeTempDirSync "Deno.makeTempDirSync")

Synchronously creates a new temporary directory in the default directory for temporary files, unless `dir` is specified. Other optional options include prefixing and suffixing the directory name with `prefix` and `suffix` respectively.

f

[Deno.makeTempFile](./././~/Deno.makeTempFile "Deno.makeTempFile")

Creates a new temporary file in the default directory for temporary files, unless `dir` is specified.

f

[Deno.makeTempFileSync](./././~/Deno.makeTempFileSync "Deno.makeTempFileSync")

Synchronously creates a new temporary file in the default directory for temporary files, unless `dir` is specified.

I

[Deno.MakeTempOptions](./././~/Deno.MakeTempOptions "Deno.MakeTempOptions")

Options which can be set when using [`Deno.makeTempDir`](./././~/Deno.makeTempDir), [`Deno.makeTempDirSync`](./././~/Deno.makeTempDirSync), [`Deno.makeTempFile`](./././~/Deno.makeTempFile), and [`Deno.makeTempFileSync`](./././~/Deno.makeTempFileSync).

-   [dir](./././~/Deno.MakeTempOptions#property_dir)
-   [prefix](./././~/Deno.MakeTempOptions#property_prefix)
-   [suffix](./././~/Deno.MakeTempOptions#property_suffix)

I

[Deno.MemoryUsage](./././~/Deno.MemoryUsage "Deno.MemoryUsage")

No documentation available

-   [external](./././~/Deno.MemoryUsage#property_external)
-   [heapTotal](./././~/Deno.MemoryUsage#property_heaptotal)
-   [heapUsed](./././~/Deno.MemoryUsage#property_heapused)
-   [rss](./././~/Deno.MemoryUsage#property_rss)

f

[Deno.memoryUsage](./././~/Deno.memoryUsage "Deno.memoryUsage")

Returns an object describing the memory usage of the Deno process and the V8 subsystem measured in bytes.

f

[Deno.mkdir](./././~/Deno.mkdir "Deno.mkdir")

Creates a new directory with the specified path.

I

[Deno.MkdirOptions](./././~/Deno.MkdirOptions "Deno.MkdirOptions")

Options which can be set when using [`Deno.mkdir`](./././~/Deno.mkdir) and [`Deno.mkdirSync`](./././~/Deno.mkdirSync).

-   [mode](./././~/Deno.MkdirOptions#property_mode)
-   [recursive](./././~/Deno.MkdirOptions#property_recursive)

f

[Deno.mkdirSync](./././~/Deno.mkdirSync "Deno.mkdirSync")

Synchronously creates a new directory with the specified path.

I

[Deno.MulticastV4Membership](./././~/Deno.MulticastV4Membership "Deno.MulticastV4Membership")

Represents membership of a IPv4 multicast group.

-   [leave](./././~/Deno.MulticastV4Membership#property_leave)
-   [setLoopback](./././~/Deno.MulticastV4Membership#property_setloopback)
-   [setTTL](./././~/Deno.MulticastV4Membership#property_setttl)

I

[Deno.MulticastV6Membership](./././~/Deno.MulticastV6Membership "Deno.MulticastV6Membership")

Represents membership of a IPv6 multicast group.

-   [leave](./././~/Deno.MulticastV6Membership#property_leave)
-   [setLoopback](./././~/Deno.MulticastV6Membership#property_setloopback)

I

[Deno.MxRecord](./././~/Deno.MxRecord "Deno.MxRecord")

If [`Deno.resolveDns`](./././~/Deno.resolveDns) is called with `"MX"` record type specified, it will return an array of objects with this interface.

-   [exchange](./././~/Deno.MxRecord#property_exchange)
-   [preference](./././~/Deno.MxRecord#property_preference)

I

[Deno.NaptrRecord](./././~/Deno.NaptrRecord "Deno.NaptrRecord")

If [`Deno.resolveDns`](./././~/Deno.resolveDns) is called with `"NAPTR"` record type specified, it will return an array of objects with this interface.

-   [flags](./././~/Deno.NaptrRecord#property_flags)
-   [order](./././~/Deno.NaptrRecord#property_order)
-   [preference](./././~/Deno.NaptrRecord#property_preference)
-   [regexp](./././~/Deno.NaptrRecord#property_regexp)
-   [replacement](./././~/Deno.NaptrRecord#property_replacement)
-   [services](./././~/Deno.NaptrRecord#property_services)

T

[Deno.NativeBigIntType](./././~/Deno.NativeBigIntType "Deno.NativeBigIntType")

All BigInt number types for interfacing with foreign functions.

T

[Deno.NativeBooleanType](./././~/Deno.NativeBooleanType "Deno.NativeBooleanType")

The native boolean type for interfacing to foreign functions.

T

[Deno.NativeBufferType](./././~/Deno.NativeBufferType "Deno.NativeBufferType")

The native buffer type for interfacing to foreign functions.

T

[Deno.NativeFunctionType](./././~/Deno.NativeFunctionType "Deno.NativeFunctionType")

The native function type for interfacing with foreign functions.

T

[Deno.NativeI16Enum](./././~/Deno.NativeI16Enum "Deno.NativeI16Enum")

No documentation available

T

[Deno.NativeI32Enum](./././~/Deno.NativeI32Enum "Deno.NativeI32Enum")

No documentation available

T

[Deno.NativeI8Enum](./././~/Deno.NativeI8Enum "Deno.NativeI8Enum")

No documentation available

T

[Deno.NativeNumberType](./././~/Deno.NativeNumberType "Deno.NativeNumberType")

All plain number types for interfacing with foreign functions.

T

[Deno.NativePointerType](./././~/Deno.NativePointerType "Deno.NativePointerType")

The native pointer type for interfacing to foreign functions.

T

[Deno.NativeResultType](./././~/Deno.NativeResultType "Deno.NativeResultType")

No documentation available

I

[Deno.NativeStructType](./././~/Deno.NativeStructType "Deno.NativeStructType")

The native struct type for interfacing with foreign functions.

-   [struct](./././~/Deno.NativeStructType#property_struct)

T

[Deno.NativeType](./././~/Deno.NativeType "Deno.NativeType")

All supported types for interfacing with foreign functions.

T

[Deno.NativeTypedFunction](./././~/Deno.NativeTypedFunction "Deno.NativeTypedFunction")

No documentation available

T

[Deno.NativeTypedPointer](./././~/Deno.NativeTypedPointer "Deno.NativeTypedPointer")

No documentation available

T

[Deno.NativeU16Enum](./././~/Deno.NativeU16Enum "Deno.NativeU16Enum")

No documentation available

T

[Deno.NativeU32Enum](./././~/Deno.NativeU32Enum "Deno.NativeU32Enum")

No documentation available

T

[Deno.NativeU8Enum](./././~/Deno.NativeU8Enum "Deno.NativeU8Enum")

No documentation available

T

[Deno.NativeVoidType](./././~/Deno.NativeVoidType "Deno.NativeVoidType")

The native void type for interfacing with foreign functions.

I

[Deno.NetAddr](./././~/Deno.NetAddr "Deno.NetAddr")

No documentation available

-   [hostname](./././~/Deno.NetAddr#property_hostname)
-   [port](./././~/Deno.NetAddr#property_port)
-   [transport](./././~/Deno.NetAddr#property_transport)

I

[Deno.NetPermissionDescriptor](./././~/Deno.NetPermissionDescriptor "Deno.NetPermissionDescriptor")

The permission descriptor for the `allow-net` and `deny-net` permissions, which controls access to opening network ports and connecting to remote hosts via the network. The option `host` allows scoping the permission for outbound connection to a specific host and port.

-   [host](./././~/Deno.NetPermissionDescriptor#property_host)
-   [name](./././~/Deno.NetPermissionDescriptor#property_name)

I

[Deno.NetworkInterfaceInfo](./././~/Deno.NetworkInterfaceInfo "Deno.NetworkInterfaceInfo")

The information for a network interface returned from a call to [`Deno.networkInterfaces`](./././~/Deno.networkInterfaces).

-   [address](./././~/Deno.NetworkInterfaceInfo#property_address)
-   [cidr](./././~/Deno.NetworkInterfaceInfo#property_cidr)
-   [family](./././~/Deno.NetworkInterfaceInfo#property_family)
-   [mac](./././~/Deno.NetworkInterfaceInfo#property_mac)
-   [name](./././~/Deno.NetworkInterfaceInfo#property_name)
-   [netmask](./././~/Deno.NetworkInterfaceInfo#property_netmask)
-   [scopeid](./././~/Deno.NetworkInterfaceInfo#property_scopeid)

f

[Deno.networkInterfaces](./././~/Deno.networkInterfaces "Deno.networkInterfaces")

Returns an array of the network interface information.

v

[Deno.noColor](./././~/Deno.noColor "Deno.noColor")

Reflects the `NO_COLOR` environment variable at program start.

f

[Deno.open](./././~/Deno.open "Deno.open")

Open a file and resolve to an instance of [`Deno.FsFile`](./././~/Deno.FsFile). The file does not need to previously exist if using the `create` or `createNew` open options. The caller may have the resulting file automatically closed by the runtime once it's out of scope by declaring the file variable with the `using` keyword.

f

[Deno.openKv](./././~/Deno.openKv "Deno.openKv")

Open a new [`Deno.Kv`](./././~/Deno.Kv) connection to persist data.

I

[Deno.OpenOptions](./././~/Deno.OpenOptions "Deno.OpenOptions")

Options which can be set when doing [`Deno.open`](./././~/Deno.open) and [`Deno.openSync`](./././~/Deno.openSync).

-   [append](./././~/Deno.OpenOptions#property_append)
-   [create](./././~/Deno.OpenOptions#property_create)
-   [createNew](./././~/Deno.OpenOptions#property_createnew)
-   [mode](./././~/Deno.OpenOptions#property_mode)
-   [read](./././~/Deno.OpenOptions#property_read)
-   [truncate](./././~/Deno.OpenOptions#property_truncate)
-   [write](./././~/Deno.OpenOptions#property_write)

f

[Deno.openSync](./././~/Deno.openSync "Deno.openSync")

Synchronously open a file and return an instance of [`Deno.FsFile`](./././~/Deno.FsFile). The file does not need to previously exist if using the `create` or `createNew` open options. The caller may have the resulting file automatically closed by the runtime once it's out of scope by declaring the file variable with the `using` keyword.

f

[Deno.osRelease](./././~/Deno.osRelease "Deno.osRelease")

Returns the release version of the Operating System.

f

[Deno.osUptime](./././~/Deno.osUptime "Deno.osUptime")

Returns the Operating System uptime in number of seconds.

T

[Deno.PermissionDescriptor](./././~/Deno.PermissionDescriptor "Deno.PermissionDescriptor")

Permission descriptors which define a permission and can be queried, requested, or revoked.

T

[Deno.PermissionName](./././~/Deno.PermissionName "Deno.PermissionName")

The name of a privileged feature which needs permission.

T

[Deno.PermissionOptions](./././~/Deno.PermissionOptions "Deno.PermissionOptions")

Options which define the permissions within a test or worker context.

I

[Deno.PermissionOptionsObject](./././~/Deno.PermissionOptionsObject "Deno.PermissionOptionsObject")

A set of options which can define the permissions within a test or worker context at a highly specific level.

-   [env](./././~/Deno.PermissionOptionsObject#property_env)
-   [ffi](./././~/Deno.PermissionOptionsObject#property_ffi)
-   [import](./././~/Deno.PermissionOptionsObject#property_import)
-   [net](./././~/Deno.PermissionOptionsObject#property_net)
-   [read](./././~/Deno.PermissionOptionsObject#property_read)
-   [run](./././~/Deno.PermissionOptionsObject#property_run)
-   [sys](./././~/Deno.PermissionOptionsObject#property_sys)
-   [write](./././~/Deno.PermissionOptionsObject#property_write)

c

[Deno.Permissions](./././~/Deno.Permissions "Deno.Permissions")

Deno's permission management API.

-   [query](./././~/Deno.Permissions#method_query_0)
-   [querySync](./././~/Deno.Permissions#method_querysync_0)
-   [request](./././~/Deno.Permissions#method_request_0)
-   [requestSync](./././~/Deno.Permissions#method_requestsync_0)
-   [revoke](./././~/Deno.Permissions#method_revoke_0)
-   [revokeSync](./././~/Deno.Permissions#method_revokesync_0)

v

[Deno.permissions](./././~/Deno.permissions "Deno.permissions")

Deno's permission management API.

T

[Deno.PermissionState](./././~/Deno.PermissionState "Deno.PermissionState")

The current status of the permission:

c

[Deno.PermissionStatus](./././~/Deno.PermissionStatus "Deno.PermissionStatus")

An `EventTarget` returned from the [`Deno.permissions`](./././~/Deno.permissions) API which can provide updates to any state changes of the permission.

-   [addEventListener](./././~/Deno.PermissionStatus#method_addeventlistener_0)
-   [onchange](./././~/Deno.PermissionStatus#property_onchange)
-   [partial](./././~/Deno.PermissionStatus#property_partial)
-   [removeEventListener](./././~/Deno.PermissionStatus#method_removeeventlistener_0)
-   [state](./././~/Deno.PermissionStatus#property_state)

I

[Deno.PermissionStatusEventMap](./././~/Deno.PermissionStatusEventMap "Deno.PermissionStatusEventMap")

The interface which defines what event types are supported by `PermissionStatus` instances.

-   [change](./././~/Deno.PermissionStatusEventMap#property_change)

v

[Deno.pid](./././~/Deno.pid "Deno.pid")

The current process ID of this instance of the Deno CLI.

I

[Deno.PointerObject](./././~/Deno.PointerObject "Deno.PointerObject")

A non-null pointer, represented as an object at runtime. The object's prototype is `null` and cannot be changed. The object cannot be assigned to either and is thus entirely read-only.

-   [brand](./././~/Deno.PointerObject#property_brand)

T

[Deno.PointerValue](./././~/Deno.PointerValue "Deno.PointerValue")

Pointers are represented either with a `PointerObject` object or a `null` if the pointer is null.

v

[Deno.ppid](./././~/Deno.ppid "Deno.ppid")

The process ID of parent process of this instance of the Deno CLI.

T

[Deno.Proxy](./././~/Deno.Proxy "Deno.Proxy")

The definition for alternative transports (or proxies) in [`Deno.CreateHttpClientOptions`](./././~/Deno.CreateHttpClientOptions).

I

[Deno.QuicAcceptOptions](./././~/Deno.QuicAcceptOptions "Deno.QuicAcceptOptions")

No documentation available

-   [alpnProtocols](./././~/Deno.QuicAcceptOptions#property_alpnprotocols)
-   [zeroRtt](./././~/Deno.QuicAcceptOptions#property_zerortt)

I

[Deno.QuicBidirectionalStream](./././~/Deno.QuicBidirectionalStream "Deno.QuicBidirectionalStream")

No documentation available

-   [readable](./././~/Deno.QuicBidirectionalStream#property_readable)
-   [writable](./././~/Deno.QuicBidirectionalStream#property_writable)

I

[Deno.QuicCloseInfo](./././~/Deno.QuicCloseInfo "Deno.QuicCloseInfo")

No documentation available

-   [closeCode](./././~/Deno.QuicCloseInfo#property_closecode)
-   [reason](./././~/Deno.QuicCloseInfo#property_reason)

I

[Deno.QuicConn](./././~/Deno.QuicConn "Deno.QuicConn")

No documentation available

-   [close](./././~/Deno.QuicConn#method_close_0)
-   [closed](./././~/Deno.QuicConn#property_closed)
-   [createBidirectionalStream](./././~/Deno.QuicConn#method_createbidirectionalstream_0)
-   [createUnidirectionalStream](./././~/Deno.QuicConn#method_createunidirectionalstream_0)
-   [endpoint](./././~/Deno.QuicConn#property_endpoint)
-   [handshake](./././~/Deno.QuicConn#property_handshake)
-   [incomingBidirectionalStreams](./././~/Deno.QuicConn#property_incomingbidirectionalstreams)
-   [incomingUnidirectionalStreams](./././~/Deno.QuicConn#property_incomingunidirectionalstreams)
-   [maxDatagramSize](./././~/Deno.QuicConn#property_maxdatagramsize)
-   [protocol](./././~/Deno.QuicConn#property_protocol)
-   [readDatagram](./././~/Deno.QuicConn#method_readdatagram_0)
-   [remoteAddr](./././~/Deno.QuicConn#property_remoteaddr)
-   [sendDatagram](./././~/Deno.QuicConn#method_senddatagram_0)
-   [serverName](./././~/Deno.QuicConn#property_servername)

c

[Deno.QuicEndpoint](./././~/Deno.QuicEndpoint "Deno.QuicEndpoint")

No documentation available

-   [addr](./././~/Deno.QuicEndpoint#property_addr)
-   [close](./././~/Deno.QuicEndpoint#method_close_0)
-   [listen](./././~/Deno.QuicEndpoint#method_listen_0)

I

[Deno.QuicEndpointOptions](./././~/Deno.QuicEndpointOptions "Deno.QuicEndpointOptions")

No documentation available

-   [hostname](./././~/Deno.QuicEndpointOptions#property_hostname)
-   [port](./././~/Deno.QuicEndpointOptions#property_port)

I

[Deno.QuicIncoming](./././~/Deno.QuicIncoming "Deno.QuicIncoming")

An incoming connection for which the server has not yet begun its part of the handshake.

-   [accept](./././~/Deno.QuicIncoming#method_accept_0)
-   [ignore](./././~/Deno.QuicIncoming#method_ignore_0)
-   [localIp](./././~/Deno.QuicIncoming#property_localip)
-   [refuse](./././~/Deno.QuicIncoming#method_refuse_0)
-   [remoteAddr](./././~/Deno.QuicIncoming#property_remoteaddr)
-   [remoteAddressValidated](./././~/Deno.QuicIncoming#property_remoteaddressvalidated)

I

[Deno.QuicListener](./././~/Deno.QuicListener "Deno.QuicListener")

Specialized listener that accepts QUIC connections.

-   [accept](./././~/Deno.QuicListener#method_accept_0)
-   [endpoint](./././~/Deno.QuicListener#property_endpoint)
-   [incoming](./././~/Deno.QuicListener#method_incoming_0)
-   [stop](./././~/Deno.QuicListener#method_stop_0)

I

[Deno.QuicListenOptions](./././~/Deno.QuicListenOptions "Deno.QuicListenOptions")

No documentation available

-   [alpnProtocols](./././~/Deno.QuicListenOptions#property_alpnprotocols)
-   [cert](./././~/Deno.QuicListenOptions#property_cert)
-   [key](./././~/Deno.QuicListenOptions#property_key)

I

[Deno.QuicReceiveStream](./././~/Deno.QuicReceiveStream "Deno.QuicReceiveStream")

No documentation available

-   [id](./././~/Deno.QuicReceiveStream#property_id)

I

[Deno.QuicSendStream](./././~/Deno.QuicSendStream "Deno.QuicSendStream")

No documentation available

-   [id](./././~/Deno.QuicSendStream#property_id)
-   [sendOrder](./././~/Deno.QuicSendStream#property_sendorder)

I

[Deno.QuicSendStreamOptions](./././~/Deno.QuicSendStreamOptions "Deno.QuicSendStreamOptions")

No documentation available

-   [sendOrder](./././~/Deno.QuicSendStreamOptions#property_sendorder)
-   [waitUntilAvailable](./././~/Deno.QuicSendStreamOptions#property_waituntilavailable)

I

[Deno.QuicServerTransportOptions](./././~/Deno.QuicServerTransportOptions "Deno.QuicServerTransportOptions")

No documentation available

-   [preferredAddressV4](./././~/Deno.QuicServerTransportOptions#property_preferredaddressv4)
-   [preferredAddressV6](./././~/Deno.QuicServerTransportOptions#property_preferredaddressv6)

I

[Deno.QuicTransportOptions](./././~/Deno.QuicTransportOptions "Deno.QuicTransportOptions")

No documentation available

-   [congestionControl](./././~/Deno.QuicTransportOptions#property_congestioncontrol)
-   [keepAliveInterval](./././~/Deno.QuicTransportOptions#property_keepaliveinterval)
-   [maxConcurrentBidirectionalStreams](./././~/Deno.QuicTransportOptions#property_maxconcurrentbidirectionalstreams)
-   [maxConcurrentUnidirectionalStreams](./././~/Deno.QuicTransportOptions#property_maxconcurrentunidirectionalstreams)
-   [maxIdleTimeout](./././~/Deno.QuicTransportOptions#property_maxidletimeout)

f

[Deno.readDir](./././~/Deno.readDir "Deno.readDir")

Reads the directory given by `path` and returns an async iterable of [`Deno.DirEntry`](./././~/Deno.DirEntry). The order of entries is not guaranteed.

f

[Deno.readDirSync](./././~/Deno.readDirSync "Deno.readDirSync")

Synchronously reads the directory given by `path` and returns an iterable of [`Deno.DirEntry`](./././~/Deno.DirEntry). The order of entries is not guaranteed.

f

[Deno.readFile](./././~/Deno.readFile "Deno.readFile")

Reads and resolves to the entire contents of a file as an array of bytes. `TextDecoder` can be used to transform the bytes to string if required. Rejects with an error when reading a directory.

I

[Deno.ReadFileOptions](./././~/Deno.ReadFileOptions "Deno.ReadFileOptions")

Options which can be set when using [`Deno.readFile`](./././~/Deno.readFile) or [`Deno.readFileSync`](./././~/Deno.readFileSync).

-   [signal](./././~/Deno.ReadFileOptions#property_signal)

f

[Deno.readFileSync](./././~/Deno.readFileSync "Deno.readFileSync")

Synchronously reads and returns the entire contents of a file as an array of bytes. `TextDecoder` can be used to transform the bytes to string if required. Throws an error when reading a directory.

f

[Deno.readLink](./././~/Deno.readLink "Deno.readLink")

Resolves to the full path destination of the named symbolic link.

f

[Deno.readLinkSync](./././~/Deno.readLinkSync "Deno.readLinkSync")

Synchronously returns the full path destination of the named symbolic link.

I

[Deno.ReadPermissionDescriptor](./././~/Deno.ReadPermissionDescriptor "Deno.ReadPermissionDescriptor")

The permission descriptor for the `allow-read` and `deny-read` permissions, which controls access to reading resources from the local host. The option `path` allows scoping the permission to a specific path (and if the path is a directory any sub paths).

-   [name](./././~/Deno.ReadPermissionDescriptor#property_name)
-   [path](./././~/Deno.ReadPermissionDescriptor#property_path)

f

[Deno.readTextFile](./././~/Deno.readTextFile "Deno.readTextFile")

Asynchronously reads and returns the entire contents of a file as an UTF-8 decoded string. Reading a directory throws an error.

f

[Deno.readTextFileSync](./././~/Deno.readTextFileSync "Deno.readTextFileSync")

Synchronously reads and returns the entire contents of a file as an UTF-8 decoded string. Reading a directory throws an error.

f

[Deno.realPath](./././~/Deno.realPath "Deno.realPath")

Resolves to the absolute normalized path, with symbolic links resolved.

f

[Deno.realPathSync](./././~/Deno.realPathSync "Deno.realPathSync")

Synchronously returns absolute normalized path, with symbolic links resolved.

T

[Deno.RecordType](./././~/Deno.RecordType "Deno.RecordType")

The type of the resource record to resolve via DNS using [`Deno.resolveDns`](./././~/Deno.resolveDns).

f

[Deno.refTimer](./././~/Deno.refTimer "Deno.refTimer")

Make the timer of the given `id` block the event loop from finishing.

f

[Deno.remove](./././~/Deno.remove "Deno.remove")

Removes the named file or directory.

I

[Deno.RemoveOptions](./././~/Deno.RemoveOptions "Deno.RemoveOptions")

Options which can be set when using [`Deno.remove`](./././~/Deno.remove) and [`Deno.removeSync`](./././~/Deno.removeSync).

-   [recursive](./././~/Deno.RemoveOptions#property_recursive)

f

[Deno.removeSignalListener](./././~/Deno.removeSignalListener "Deno.removeSignalListener")

Removes the given signal listener that has been registered with [`Deno.addSignalListener`](./././~/Deno.addSignalListener).

f

[Deno.removeSync](./././~/Deno.removeSync "Deno.removeSync")

Synchronously removes the named file or directory.

f

[Deno.rename](./././~/Deno.rename "Deno.rename")

Renames (moves) `oldpath` to `newpath`. Paths may be files or directories. If `newpath` already exists and is not a directory, `rename()` replaces it. OS-specific restrictions may apply when `oldpath` and `newpath` are in different directories.

f

[Deno.renameSync](./././~/Deno.renameSync "Deno.renameSync")

Synchronously renames (moves) `oldpath` to `newpath`. Paths may be files or directories. If `newpath` already exists and is not a directory, `renameSync()` replaces it. OS-specific restrictions may apply when `oldpath` and `newpath` are in different directories.

f

[Deno.resolveDns](./././~/Deno.resolveDns "Deno.resolveDns")

Performs DNS resolution against the given query, returning resolved records.

I

[Deno.ResolveDnsOptions](./././~/Deno.ResolveDnsOptions "Deno.ResolveDnsOptions")

Options which can be set when using [`Deno.resolveDns`](./././~/Deno.resolveDns).

-   [nameServer](./././~/Deno.ResolveDnsOptions#property_nameserver)
-   [signal](./././~/Deno.ResolveDnsOptions#property_signal)

I

[Deno.RunPermissionDescriptor](./././~/Deno.RunPermissionDescriptor "Deno.RunPermissionDescriptor")

The permission descriptor for the `allow-run` and `deny-run` permissions, which controls access to what sub-processes can be executed by Deno. The option `command` allows scoping the permission to a specific executable.

-   [command](./././~/Deno.RunPermissionDescriptor#property_command)
-   [name](./././~/Deno.RunPermissionDescriptor#property_name)

E

[Deno.SeekMode](./././~/Deno.SeekMode "Deno.SeekMode")

A enum which defines the seek mode for IO related APIs that support seeking.

f

[Deno.serve](./././~/Deno.serve "Deno.serve")

Serves HTTP requests with the given handler.

I

[Deno.ServeDefaultExport](./././~/Deno.ServeDefaultExport "Deno.ServeDefaultExport")

Interface that module run with `deno serve` subcommand must conform to.

-   [fetch](./././~/Deno.ServeDefaultExport#property_fetch)
-   [onListen](./././~/Deno.ServeDefaultExport#property_onlisten)

T

[Deno.ServeHandler](./././~/Deno.ServeHandler "Deno.ServeHandler")

A handler for HTTP requests. Consumes a request and returns a response.

I

[Deno.ServeHandlerInfo](./././~/Deno.ServeHandlerInfo "Deno.ServeHandlerInfo")

Additional information for an HTTP request and its connection.

-   [completed](./././~/Deno.ServeHandlerInfo#property_completed)
-   [remoteAddr](./././~/Deno.ServeHandlerInfo#property_remoteaddr)

I

[Deno.ServeInit](./././~/Deno.ServeInit "Deno.ServeInit")

No documentation available

-   [handler](./././~/Deno.ServeInit#property_handler)

I

[Deno.ServeOptions](./././~/Deno.ServeOptions "Deno.ServeOptions")

Options which can be set when calling [`Deno.serve`](./././~/Deno.serve).

-   [onError](./././~/Deno.ServeOptions#property_onerror)
-   [onListen](./././~/Deno.ServeOptions#property_onlisten)
-   [signal](./././~/Deno.ServeOptions#property_signal)

I

[Deno.ServeTcpOptions](./././~/Deno.ServeTcpOptions "Deno.ServeTcpOptions")

Options that can be passed to `Deno.serve` to create a server listening on a TCP port.

-   [hostname](./././~/Deno.ServeTcpOptions#property_hostname)
-   [port](./././~/Deno.ServeTcpOptions#property_port)
-   [reusePort](./././~/Deno.ServeTcpOptions#property_reuseport)
-   [tcpBacklog](./././~/Deno.ServeTcpOptions#property_tcpbacklog)
-   [transport](./././~/Deno.ServeTcpOptions#property_transport)

I

[Deno.ServeUnixOptions](./././~/Deno.ServeUnixOptions "Deno.ServeUnixOptions")

Options that can be passed to `Deno.serve` to create a server listening on a Unix domain socket.

-   [path](./././~/Deno.ServeUnixOptions#property_path)
-   [transport](./././~/Deno.ServeUnixOptions#property_transport)

I

[Deno.ServeVsockOptions](./././~/Deno.ServeVsockOptions "Deno.ServeVsockOptions")

Options that can be passed to `Deno.serve` to create a server listening on a VSOCK socket.

-   [cid](./././~/Deno.ServeVsockOptions#property_cid)
-   [port](./././~/Deno.ServeVsockOptions#property_port)
-   [transport](./././~/Deno.ServeVsockOptions#property_transport)

I

[Deno.SetRawOptions](./././~/Deno.SetRawOptions "Deno.SetRawOptions")

No documentation available

-   [cbreak](./././~/Deno.SetRawOptions#property_cbreak)

T

[Deno.Signal](./././~/Deno.Signal "Deno.Signal")

Operating signals which can be listened for or sent to sub-processes. What signals and what their standard behaviors are OS dependent.

I

[Deno.SoaRecord](./././~/Deno.SoaRecord "Deno.SoaRecord")

If [`Deno.resolveDns`](./././~/Deno.resolveDns) is called with `"SOA"` record type specified, it will return an array of objects with this interface.

-   [expire](./././~/Deno.SoaRecord#property_expire)
-   [minimum](./././~/Deno.SoaRecord#property_minimum)
-   [mname](./././~/Deno.SoaRecord#property_mname)
-   [refresh](./././~/Deno.SoaRecord#property_refresh)
-   [retry](./././~/Deno.SoaRecord#property_retry)
-   [rname](./././~/Deno.SoaRecord#property_rname)
-   [serial](./././~/Deno.SoaRecord#property_serial)

f

[Deno.spawn](./././~/Deno.spawn "Deno.spawn")

Spawns a new subprocess, returning a [`Deno.ChildProcess`](./././~/Deno.ChildProcess) handle.

f

[Deno.spawnAndWait](./././~/Deno.spawnAndWait "Deno.spawnAndWait")

Spawns a subprocess, waits for it to finish, and returns the output.

f

[Deno.spawnAndWaitSync](./././~/Deno.spawnAndWaitSync "Deno.spawnAndWaitSync")

Synchronously spawns a subprocess, waits for it to finish, and returns the output.

I

[Deno.SrvRecord](./././~/Deno.SrvRecord "Deno.SrvRecord")

If [`Deno.resolveDns`](./././~/Deno.resolveDns) is called with `"SRV"` record type specified, it will return an array of objects with this interface.

-   [port](./././~/Deno.SrvRecord#property_port)
-   [priority](./././~/Deno.SrvRecord#property_priority)
-   [target](./././~/Deno.SrvRecord#property_target)
-   [weight](./././~/Deno.SrvRecord#property_weight)

f

[Deno.startTls](./././~/Deno.startTls "Deno.startTls")

Start TLS handshake from an existing connection using an optional list of CA certificates, and hostname (default is "127.0.0.1"). Specifying CA certs is optional. By default the configured root certificates are used. Using this function requires that the other end of the connection is prepared for a TLS handshake.

I

[Deno.StartTlsOptions](./././~/Deno.StartTlsOptions "Deno.StartTlsOptions")

No documentation available

-   [alpnProtocols](./././~/Deno.StartTlsOptions#property_alpnprotocols)
-   [caCerts](./././~/Deno.StartTlsOptions#property_cacerts)
-   [hostname](./././~/Deno.StartTlsOptions#property_hostname)
-   [unsafelyDisableHostnameVerification](./././~/Deno.StartTlsOptions#property_unsafelydisablehostnameverification)

f

[Deno.stat](./././~/Deno.stat "Deno.stat")

Resolves to a [`Deno.FileInfo`](./././~/Deno.FileInfo) for the specified `path`. Will always follow symlinks.

T

[Deno.StaticForeignLibraryInterface](./././~/Deno.StaticForeignLibraryInterface "Deno.StaticForeignLibraryInterface")

A utility type that infers a foreign library interface.

T

[Deno.StaticForeignSymbol](./././~/Deno.StaticForeignSymbol "Deno.StaticForeignSymbol")

A utility type that infers a foreign symbol.

T

[Deno.StaticForeignSymbolReturnType](./././~/Deno.StaticForeignSymbolReturnType "Deno.StaticForeignSymbolReturnType")

No documentation available

f

[Deno.statSync](./././~/Deno.statSync "Deno.statSync")

Synchronously returns a [`Deno.FileInfo`](./././~/Deno.FileInfo) for the specified `path`. Will always follow symlinks.

v

[Deno.stderr](./././~/Deno.stderr "Deno.stderr")

A reference to `stderr` which can be used to write directly to `stderr`. It implements the Deno specific [`Writer`](https://jsr.io/@std/io/doc/types/~/Writer), [`WriterSync`](https://jsr.io/@std/io/doc/types/~/WriterSync), and [`Closer`](https://jsr.io/@std/io/doc/types/~/Closer) interfaces as well as provides a `WritableStream` interface.

-   [close](./././~/Deno.stderr#method_close_0)
-   [isTerminal](./././~/Deno.stderr#method_isterminal_0)
-   [writable](./././~/Deno.stderr#property_writable)
-   [write](./././~/Deno.stderr#method_write_0)
-   [writeSync](./././~/Deno.stderr#method_writesync_0)

v

[Deno.stdin](./././~/Deno.stdin "Deno.stdin")

A reference to `stdin` which can be used to read directly from `stdin`.

-   [close](./././~/Deno.stdin#method_close_0)
-   [isTerminal](./././~/Deno.stdin#method_isterminal_0)
-   [read](./././~/Deno.stdin#method_read_0)
-   [readSync](./././~/Deno.stdin#method_readsync_0)
-   [readable](./././~/Deno.stdin#property_readable)
-   [setRaw](./././~/Deno.stdin#method_setraw_0)

v

[Deno.stdout](./././~/Deno.stdout "Deno.stdout")

A reference to `stdout` which can be used to write directly to `stdout`. It implements the Deno specific [`Writer`](https://jsr.io/@std/io/doc/types/~/Writer), [`WriterSync`](https://jsr.io/@std/io/doc/types/~/WriterSync), and [`Closer`](https://jsr.io/@std/io/doc/types/~/Closer) interfaces as well as provides a `WritableStream` interface.

-   [close](./././~/Deno.stdout#method_close_0)
-   [isTerminal](./././~/Deno.stdout#method_isterminal_0)
-   [writable](./././~/Deno.stdout#property_writable)
-   [write](./././~/Deno.stdout#method_write_0)
-   [writeSync](./././~/Deno.stdout#method_writesync_0)

I

[Deno.SubprocessReadableStream](./././~/Deno.SubprocessReadableStream "Deno.SubprocessReadableStream")

The interface for stdout and stderr streams for child process returned from `Deno.Command.spawn`.

-   [arrayBuffer](./././~/Deno.SubprocessReadableStream#method_arraybuffer_0)
-   [bytes](./././~/Deno.SubprocessReadableStream#method_bytes_0)
-   [json](./././~/Deno.SubprocessReadableStream#method_json_0)
-   [text](./././~/Deno.SubprocessReadableStream#method_text_0)

f

[Deno.symlink](./././~/Deno.symlink "Deno.symlink")

Creates `newpath` as a symbolic link to `oldpath`.

I

[Deno.SymlinkOptions](./././~/Deno.SymlinkOptions "Deno.SymlinkOptions")

Options that can be used with `symlink` and `symlinkSync`.

-   [type](./././~/Deno.SymlinkOptions#property_type)

f

[Deno.symlinkSync](./././~/Deno.symlinkSync "Deno.symlinkSync")

Creates `newpath` as a symbolic link to `oldpath`.

I

[Deno.SysPermissionDescriptor](./././~/Deno.SysPermissionDescriptor "Deno.SysPermissionDescriptor")

The permission descriptor for the `allow-sys` and `deny-sys` permissions, which controls access to sensitive host system information, which malicious code might attempt to exploit. The option `kind` allows scoping the permission to a specific piece of information.

-   [kind](./././~/Deno.SysPermissionDescriptor#property_kind)
-   [name](./././~/Deno.SysPermissionDescriptor#property_name)

I

[Deno.SystemMemoryInfo](./././~/Deno.SystemMemoryInfo "Deno.SystemMemoryInfo")

Information returned from a call to [`Deno.systemMemoryInfo`](./././~/Deno.systemMemoryInfo).

-   [available](./././~/Deno.SystemMemoryInfo#property_available)
-   [buffers](./././~/Deno.SystemMemoryInfo#property_buffers)
-   [cached](./././~/Deno.SystemMemoryInfo#property_cached)
-   [free](./././~/Deno.SystemMemoryInfo#property_free)
-   [swapFree](./././~/Deno.SystemMemoryInfo#property_swapfree)
-   [swapTotal](./././~/Deno.SystemMemoryInfo#property_swaptotal)
-   [total](./././~/Deno.SystemMemoryInfo#property_total)

f

[Deno.systemMemoryInfo](./././~/Deno.systemMemoryInfo "Deno.systemMemoryInfo")

Displays the total amount of free and used physical and swap memory in the system, as well as the buffers and caches used by the kernel.

I

[Deno.TcpConn](./././~/Deno.TcpConn "Deno.TcpConn")

No documentation available

-   [setKeepAlive](./././~/Deno.TcpConn#method_setkeepalive_0)
-   [setNoDelay](./././~/Deno.TcpConn#method_setnodelay_0)

T

[Deno.TcpListener](./././~/Deno.TcpListener "Deno.TcpListener")

Specialized listener that accepts TCP connections.

I

[Deno.TcpListenOptions](./././~/Deno.TcpListenOptions "Deno.TcpListenOptions")

No documentation available

-   [reusePort](./././~/Deno.TcpListenOptions#property_reuseport)

N

[Deno.telemetry](./././~/Deno.telemetry "Deno.telemetry")

APIs for working with the OpenTelemetry observability framework. Deno can export traces, metrics, and logs to OpenTelemetry compatible backends via the OTLP protocol.

v

[Deno.telemetry.contextManager](./././~/Deno.telemetry.contextManager "Deno.telemetry.contextManager")

A ContextManager compatible with OpenTelemetry.js [https://open-telemetry.github.io/opentelemetry-js/interfaces/\_opentelemetry\_api.ContextManager.html](https://open-telemetry.github.io/opentelemetry-js/interfaces/_opentelemetry_api.ContextManager.html)

v

[Deno.telemetry.meterProvider](./././~/Deno.telemetry.meterProvider "Deno.telemetry.meterProvider")

A MeterProvider compatible with OpenTelemetry.js [https://open-telemetry.github.io/opentelemetry-js/interfaces/\_opentelemetry\_api.MeterProvider.html](https://open-telemetry.github.io/opentelemetry-js/interfaces/_opentelemetry_api.MeterProvider.html)

v

[Deno.telemetry.tracerProvider](./././~/Deno.telemetry.tracerProvider "Deno.telemetry.tracerProvider")

A TracerProvider compatible with OpenTelemetry.js [https://open-telemetry.github.io/opentelemetry-js/interfaces/\_opentelemetry\_api.TracerProvider.html](https://open-telemetry.github.io/opentelemetry-js/interfaces/_opentelemetry_api.TracerProvider.html)

v

[Deno.test](./././~/Deno.test "Deno.test")

Register a test which will be run when `deno test` is used on the command line and the containing module looks like a test module.

I

[Deno.TestContext](./././~/Deno.TestContext "Deno.TestContext")

Context that is passed to a testing function, which can be used to either gain information about the current test, or register additional test steps within the current test.

-   [name](./././~/Deno.TestContext#property_name)
-   [origin](./././~/Deno.TestContext#property_origin)
-   [parent](./././~/Deno.TestContext#property_parent)
-   [step](./././~/Deno.TestContext#method_step_0)

I

[Deno.TestDefinition](./././~/Deno.TestDefinition "Deno.TestDefinition")

No documentation available

-   [fn](./././~/Deno.TestDefinition#property_fn)
-   [ignore](./././~/Deno.TestDefinition#property_ignore)
-   [name](./././~/Deno.TestDefinition#property_name)
-   [only](./././~/Deno.TestDefinition#property_only)
-   [permissions](./././~/Deno.TestDefinition#property_permissions)
-   [sanitizeExit](./././~/Deno.TestDefinition#property_sanitizeexit)
-   [sanitizeOps](./././~/Deno.TestDefinition#property_sanitizeops)
-   [sanitizeResources](./././~/Deno.TestDefinition#property_sanitizeresources)

I

[Deno.TestStepDefinition](./././~/Deno.TestStepDefinition "Deno.TestStepDefinition")

No documentation available

-   [fn](./././~/Deno.TestStepDefinition#property_fn)
-   [ignore](./././~/Deno.TestStepDefinition#property_ignore)
-   [name](./././~/Deno.TestStepDefinition#property_name)
-   [sanitizeExit](./././~/Deno.TestStepDefinition#property_sanitizeexit)
-   [sanitizeOps](./././~/Deno.TestStepDefinition#property_sanitizeops)
-   [sanitizeResources](./././~/Deno.TestStepDefinition#property_sanitizeresources)

I

[Deno.TlsCertifiedKeyPem](./././~/Deno.TlsCertifiedKeyPem "Deno.TlsCertifiedKeyPem")

Provides certified key material from strings. The key material is provided in `PEM`\-format (Privacy Enhanced Mail, [https://www.rfc-editor.org/rfc/rfc1422](https://www.rfc-editor.org/rfc/rfc1422)) which can be identified by having `-----BEGIN-----` and `-----END-----` markers at the beginning and end of the strings. This type of key is not compatible with `DER`\-format keys which are binary.

-   [cert](./././~/Deno.TlsCertifiedKeyPem#property_cert)
-   [key](./././~/Deno.TlsCertifiedKeyPem#property_key)
-   [keyFormat](./././~/Deno.TlsCertifiedKeyPem#property_keyformat)

I

[Deno.TlsConn](./././~/Deno.TlsConn "Deno.TlsConn")

No documentation available

-   [handshake](./././~/Deno.TlsConn#method_handshake_0)

I

[Deno.TlsHandshakeInfo](./././~/Deno.TlsHandshakeInfo "Deno.TlsHandshakeInfo")

No documentation available

-   [alpnProtocol](./././~/Deno.TlsHandshakeInfo#property_alpnprotocol)

T

[Deno.TlsListener](./././~/Deno.TlsListener "Deno.TlsListener")

Specialized listener that accepts TLS connections.

T

[Deno.ToNativeParameterTypes](./././~/Deno.ToNativeParameterTypes "Deno.ToNativeParameterTypes")

A utility type for conversion of parameter types of foreign functions.

T

[Deno.ToNativeResultType](./././~/Deno.ToNativeResultType "Deno.ToNativeResultType")

Type conversion for unsafe callback return types.

T

[Deno.ToNativeType](./././~/Deno.ToNativeType "Deno.ToNativeType")

Type conversion for foreign symbol parameters and unsafe callback return types.

f

[Deno.truncate](./././~/Deno.truncate "Deno.truncate")

Truncates (or extends) the specified file, to reach the specified `len`. If `len` is not specified then the entire file contents are truncated.

f

[Deno.truncateSync](./././~/Deno.truncateSync "Deno.truncateSync")

Synchronously truncates (or extends) the specified file, to reach the specified `len`. If `len` is not specified then the entire file contents are truncated.

I

[Deno.UdpListenOptions](./././~/Deno.UdpListenOptions "Deno.UdpListenOptions")

Unstable options which can be set when opening a datagram listener via [`Deno.listenDatagram`](./././~/Deno.listenDatagram).

-   [loopback](./././~/Deno.UdpListenOptions#property_loopback)
-   [reuseAddress](./././~/Deno.UdpListenOptions#property_reuseaddress)

f

[Deno.uid](./././~/Deno.uid "Deno.uid")

Returns the user id of the process on POSIX platforms. Returns null on Windows.

f

[Deno.umask](./././~/Deno.umask "Deno.umask")

Retrieve the process umask. If `mask` is provided, sets the process umask. This call always returns what the umask was before the call.

I

[Deno.UnixAddr](./././~/Deno.UnixAddr "Deno.UnixAddr")

No documentation available

-   [path](./././~/Deno.UnixAddr#property_path)
-   [transport](./././~/Deno.UnixAddr#property_transport)

I

[Deno.UnixConn](./././~/Deno.UnixConn "Deno.UnixConn")

No documentation available

I

[Deno.UnixConnectOptions](./././~/Deno.UnixConnectOptions "Deno.UnixConnectOptions")

No documentation available

-   [path](./././~/Deno.UnixConnectOptions#property_path)
-   [transport](./././~/Deno.UnixConnectOptions#property_transport)

T

[Deno.UnixListener](./././~/Deno.UnixListener "Deno.UnixListener")

Specialized listener that accepts Unix connections.

I

[Deno.UnixListenOptions](./././~/Deno.UnixListenOptions "Deno.UnixListenOptions")

Options which can be set when opening a Unix listener via [`Deno.listen`](./././~/Deno.listen) or [`Deno.listenDatagram`](./././~/Deno.listenDatagram).

-   [path](./././~/Deno.UnixListenOptions#property_path)

f

[Deno.unrefTimer](./././~/Deno.unrefTimer "Deno.unrefTimer")

Make the timer of the given `id` not block the event loop from finishing.

c

[Deno.UnsafeCallback](./././~/Deno.UnsafeCallback "Deno.UnsafeCallback")

An unsafe function pointer for passing JavaScript functions as C function pointers to foreign function calls.

-   [callback](./././~/Deno.UnsafeCallback#property_callback)
-   [close](./././~/Deno.UnsafeCallback#method_close_0)
-   [definition](./././~/Deno.UnsafeCallback#property_definition)
-   [pointer](./././~/Deno.UnsafeCallback#property_pointer)
-   [ref](./././~/Deno.UnsafeCallback#method_ref_0)
-   [threadSafe](./././~/Deno.UnsafeCallback#method_threadsafe_0)
-   [unref](./././~/Deno.UnsafeCallback#method_unref_0)

I

[Deno.UnsafeCallbackDefinition](./././~/Deno.UnsafeCallbackDefinition "Deno.UnsafeCallbackDefinition")

Definition of a unsafe callback function.

-   [parameters](./././~/Deno.UnsafeCallbackDefinition#property_parameters)
-   [result](./././~/Deno.UnsafeCallbackDefinition#property_result)

T

[Deno.UnsafeCallbackFunction](./././~/Deno.UnsafeCallbackFunction "Deno.UnsafeCallbackFunction")

An unsafe callback function.

c

[Deno.UnsafeFnPointer](./././~/Deno.UnsafeFnPointer "Deno.UnsafeFnPointer")

An unsafe pointer to a function, for calling functions that are not present as symbols.

-   [call](./././~/Deno.UnsafeFnPointer#property_call)
-   [definition](./././~/Deno.UnsafeFnPointer#property_definition)
-   [pointer](./././~/Deno.UnsafeFnPointer#property_pointer)

c

[Deno.UnsafePointer](./././~/Deno.UnsafePointer "Deno.UnsafePointer")

A collection of static functions for interacting with pointer objects.

-   [create](./././~/Deno.UnsafePointer#method_create_0)
-   [equals](./././~/Deno.UnsafePointer#method_equals_0)
-   [of](./././~/Deno.UnsafePointer#method_of_0)
-   [offset](./././~/Deno.UnsafePointer#method_offset_0)
-   [value](./././~/Deno.UnsafePointer#method_value_0)

c

[Deno.UnsafePointerView](./././~/Deno.UnsafePointerView "Deno.UnsafePointerView")

An unsafe pointer view to a memory location as specified by the `pointer` value. The `UnsafePointerView` API follows the standard built in interface `DataView` for accessing the underlying types at an memory location (numbers, strings and raw bytes).

-   [copyInto](./././~/Deno.UnsafePointerView#method_copyinto_0)
-   [getArrayBuffer](./././~/Deno.UnsafePointerView#method_getarraybuffer_0)
-   [getBigInt64](./././~/Deno.UnsafePointerView#method_getbigint64_0)
-   [getBigUint64](./././~/Deno.UnsafePointerView#method_getbiguint64_0)
-   [getBool](./././~/Deno.UnsafePointerView#method_getbool_0)
-   [getCString](./././~/Deno.UnsafePointerView#method_getcstring_0)
-   [getFloat32](./././~/Deno.UnsafePointerView#method_getfloat32_0)
-   [getFloat64](./././~/Deno.UnsafePointerView#method_getfloat64_0)
-   [getInt16](./././~/Deno.UnsafePointerView#method_getint16_0)
-   [getInt32](./././~/Deno.UnsafePointerView#method_getint32_0)
-   [getInt8](./././~/Deno.UnsafePointerView#method_getint8_0)
-   [getPointer](./././~/Deno.UnsafePointerView#method_getpointer_0)
-   [getUint16](./././~/Deno.UnsafePointerView#method_getuint16_0)
-   [getUint32](./././~/Deno.UnsafePointerView#method_getuint32_0)
-   [getUint8](./././~/Deno.UnsafePointerView#method_getuint8_0)
-   [pointer](./././~/Deno.UnsafePointerView#property_pointer)

c

[Deno.UnsafeWindowSurface](./././~/Deno.UnsafeWindowSurface "Deno.UnsafeWindowSurface")

Creates a presentable WebGPU surface from given window and display handles.

-   [getContext](./././~/Deno.UnsafeWindowSurface#method_getcontext_0)
-   [present](./././~/Deno.UnsafeWindowSurface#method_present_0)
-   [resize](./././~/Deno.UnsafeWindowSurface#method_resize_0)

f

[Deno.upgradeWebSocket](./././~/Deno.upgradeWebSocket "Deno.upgradeWebSocket")

Upgrade an incoming HTTP request to a WebSocket.

I

[Deno.UpgradeWebSocketOptions](./././~/Deno.UpgradeWebSocketOptions "Deno.UpgradeWebSocketOptions")

Options which can be set when performing a [`Deno.upgradeWebSocket`](./././~/Deno.upgradeWebSocket) upgrade of a `Request`

-   [idleTimeout](./././~/Deno.UpgradeWebSocketOptions#property_idletimeout)
-   [protocol](./././~/Deno.UpgradeWebSocketOptions#property_protocol)

f

[Deno.upgradeWebTransport](./././~/Deno.upgradeWebTransport "Deno.upgradeWebTransport")

Upgrade a QUIC connection into a WebTransport instance.

f

[Deno.utime](./././~/Deno.utime "Deno.utime")

Changes the access (`atime`) and modification (`mtime`) times of a file system object referenced by `path`. Given times are either in seconds (UNIX epoch time) or as `Date` objects.

f

[Deno.utimeSync](./././~/Deno.utimeSync "Deno.utimeSync")

Synchronously changes the access (`atime`) and modification (`mtime`) times of a file system object referenced by `path`. Given times are either in seconds (UNIX epoch time) or as `Date` objects.

v

[Deno.version](./././~/Deno.version "Deno.version")

Version information related to the current Deno CLI runtime environment.

-   [deno](./././~/Deno.version#property_deno)
-   [typescript](./././~/Deno.version#property_typescript)
-   [v8](./././~/Deno.version#property_v8)

I

[Deno.VsockAddr](./././~/Deno.VsockAddr "Deno.VsockAddr")

No documentation available

-   [cid](./././~/Deno.VsockAddr#property_cid)
-   [port](./././~/Deno.VsockAddr#property_port)
-   [transport](./././~/Deno.VsockAddr#property_transport)

I

[Deno.VsockConn](./././~/Deno.VsockConn "Deno.VsockConn")

No documentation available

I

[Deno.VsockConnectOptions](./././~/Deno.VsockConnectOptions "Deno.VsockConnectOptions")

No documentation available

-   [cid](./././~/Deno.VsockConnectOptions#property_cid)
-   [port](./././~/Deno.VsockConnectOptions#property_port)
-   [transport](./././~/Deno.VsockConnectOptions#property_transport)

T

[Deno.VsockListener](./././~/Deno.VsockListener "Deno.VsockListener")

Specialized listener that accepts VSOCK connections.

I

[Deno.VsockListenOptions](./././~/Deno.VsockListenOptions "Deno.VsockListenOptions")

Options which can be set when opening a VSOCK listener via [`Deno.listen`](./././~/Deno.listen).

-   [cid](./././~/Deno.VsockListenOptions#property_cid)
-   [port](./././~/Deno.VsockListenOptions#property_port)

f

[Deno.watchFs](./././~/Deno.watchFs "Deno.watchFs")

Watch for file system events against one or more `paths`, which can be files or directories. These paths must exist already. One user action (e.g. `touch test.file`) can generate multiple file system events. Likewise, one user action can result in multiple file paths in one event (e.g. `mv old_name.txt new_name.txt`).

N

[Deno.webgpu](./././~/Deno.webgpu "Deno.webgpu")

The webgpu namespace provides additional APIs that the WebGPU specification does not specify.

f

[Deno.webgpu.deviceStartCapture](./././~/Deno.webgpu.deviceStartCapture "Deno.webgpu.deviceStartCapture")

Starts a frame capture.

f

[Deno.webgpu.deviceStopCapture](./././~/Deno.webgpu.deviceStopCapture "Deno.webgpu.deviceStopCapture")

Stops a frame capture.

I

[Deno.WebSocketUpgrade](./././~/Deno.WebSocketUpgrade "Deno.WebSocketUpgrade")

The object that is returned from a [`Deno.upgradeWebSocket`](./././~/Deno.upgradeWebSocket) request.

-   [response](./././~/Deno.WebSocketUpgrade#property_response)
-   [socket](./././~/Deno.WebSocketUpgrade#property_socket)

f

[Deno.writeFile](./././~/Deno.writeFile "Deno.writeFile")

Write `data` to the given `path`, by default creating a new file if needed, else overwriting.

I

[Deno.WriteFileOptions](./././~/Deno.WriteFileOptions "Deno.WriteFileOptions")

Options for writing to a file.

-   [append](./././~/Deno.WriteFileOptions#property_append)
-   [create](./././~/Deno.WriteFileOptions#property_create)
-   [createNew](./././~/Deno.WriteFileOptions#property_createnew)
-   [mode](./././~/Deno.WriteFileOptions#property_mode)
-   [signal](./././~/Deno.WriteFileOptions#property_signal)

f

[Deno.writeFileSync](./././~/Deno.writeFileSync "Deno.writeFileSync")

Synchronously write `data` to the given `path`, by default creating a new file if needed, else overwriting.

I

[Deno.WritePermissionDescriptor](./././~/Deno.WritePermissionDescriptor "Deno.WritePermissionDescriptor")

The permission descriptor for the `allow-write` and `deny-write` permissions, which controls access to writing to resources from the local host. The option `path` allow scoping the permission to a specific path (and if the path is a directory any sub paths).

-   [name](./././~/Deno.WritePermissionDescriptor#property_name)
-   [path](./././~/Deno.WritePermissionDescriptor#property_path)

f

[Deno.writeTextFile](./././~/Deno.writeTextFile "Deno.writeTextFile")

Write string `data` to the given `path`, by default creating a new file if needed, else overwriting.

f

[Deno.writeTextFileSync](./././~/Deno.writeTextFileSync "Deno.writeTextFileSync")

Synchronously write string `data` to the given `path`, by default creating a new file if needed, else overwriting.

I

[Deno.lint.WithStatement](./././~/Deno.lint.WithStatement "Deno.lint.WithStatement")

Legacy JavaScript feature, that's discouraged from being used today.

-   [body](./././~/Deno.lint.WithStatement#property_body)
-   [object](./././~/Deno.lint.WithStatement#property_object)
-   [parent](./././~/Deno.lint.WithStatement#property_parent)
-   [range](./././~/Deno.lint.WithStatement#property_range)
-   [type](./././~/Deno.lint.WithStatement#property_type)
