---
title: "process - Node documentation"
source: "https://docs.deno.com/api/node/process/"
canonical_url: "https://docs.deno.com/api/node/process/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:07.118Z"
content_hash: "6c06ade3bfcc2f55d544d4bcf5f200ff6e5ada1b475683f46b4d1273681d0dd0"
menu_path: ["process - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/perf_hooks/index.md", "title": "perf_hooks - Node documentation"}
nav_next: {"path": "deno/deno/api/node/punycode/index.md", "title": "punycode - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:process";
```

### Interfaces [#](#Interfaces)

I

[CpuUsage](.././process/~/CpuUsage "CpuUsage")

No documentation available

*   [system](.././process/~/CpuUsage#property_system)
*   [user](.././process/~/CpuUsage#property_user)

I

[EmitWarningOptions](.././process/~/EmitWarningOptions "EmitWarningOptions")

No documentation available

*   [code](.././process/~/EmitWarningOptions#property_code)
*   [ctor](.././process/~/EmitWarningOptions#property_ctor)
*   [detail](.././process/~/EmitWarningOptions#property_detail)
*   [type](.././process/~/EmitWarningOptions#property_type)

I

[HRTime](.././process/~/HRTime "HRTime")

No documentation available

*   [bigint](.././process/~/HRTime#method_bigint_0)

I

[MemoryUsage](.././process/~/MemoryUsage "MemoryUsage")

No documentation available

*   [arrayBuffers](.././process/~/MemoryUsage#property_arraybuffers)
*   [external](.././process/~/MemoryUsage#property_external)
*   [heapTotal](.././process/~/MemoryUsage#property_heaptotal)
*   [heapUsed](.././process/~/MemoryUsage#property_heapused)
*   [rss](.././process/~/MemoryUsage#property_rss)

I

[MemoryUsageFn](.././process/~/MemoryUsageFn "MemoryUsageFn")

No documentation available

*   [rss](.././process/~/MemoryUsageFn#method_rss_0)

I

[Process](.././process/~/Process "Process")

No documentation available

*   [abort](.././process/~/Process#method_abort_0)
*   [addListener](.././process/~/Process#method_addlistener_0)
*   [allowedNodeEnvironmentFlags](.././process/~/Process#property_allowednodeenvironmentflags)
*   [arch](.././process/~/Process#property_arch)
*   [argv](.././process/~/Process#property_argv)
*   [argv0](.././process/~/Process#property_argv0)
*   [availableMemory](.././process/~/Process#method_availablememory_0)
*   [channel](.././process/~/Process#property_channel)
*   [chdir](.././process/~/Process#method_chdir_0)
*   [config](.././process/~/Process#property_config)
*   [connected](.././process/~/Process#property_connected)
*   [constrainedMemory](.././process/~/Process#method_constrainedmemory_0)
*   [cpuUsage](.././process/~/Process#method_cpuusage_0)
*   [cwd](.././process/~/Process#method_cwd_0)
*   [debugPort](.././process/~/Process#property_debugport)
*   [disconnect](.././process/~/Process#method_disconnect_0)
*   [dlopen](.././process/~/Process#method_dlopen_0)
*   [emit](.././process/~/Process#method_emit_0)
*   [emitWarning](.././process/~/Process#method_emitwarning_0)
*   [env](.././process/~/Process#property_env)
*   [execArgv](.././process/~/Process#property_execargv)
*   [execPath](.././process/~/Process#property_execpath)
*   [exit](.././process/~/Process#method_exit_0)
*   [exitCode](.././process/~/Process#property_exitcode)
*   [features](.././process/~/Process#property_features)
*   [finalization](.././process/~/Process#property_finalization)
*   [getActiveResourcesInfo](.././process/~/Process#method_getactiveresourcesinfo_0)
*   [getBuiltinModule](.././process/~/Process#method_getbuiltinmodule_0)
*   [getegid](.././process/~/Process#property_getegid)
*   [geteuid](.././process/~/Process#property_geteuid)
*   [getgid](.././process/~/Process#property_getgid)
*   [getgroups](.././process/~/Process#property_getgroups)
*   [getuid](.././process/~/Process#property_getuid)
*   [hasUncaughtExceptionCaptureCallback](.././process/~/Process#method_hasuncaughtexceptioncapturecallback_0)
*   [hrtime](.././process/~/Process#property_hrtime)
*   [kill](.././process/~/Process#method_kill_0)
*   [listeners](.././process/~/Process#method_listeners_0)
*   [loadEnvFile](.././process/~/Process#method_loadenvfile_0)
*   [mainModule](.././process/~/Process#property_mainmodule)
*   [memoryUsage](.././process/~/Process#property_memoryusage)
*   [nextTick](.././process/~/Process#method_nexttick_0)
*   [on](.././process/~/Process#method_on_0)
*   [once](.././process/~/Process#method_once_0)
*   [permission](.././process/~/Process#property_permission)
*   [pid](.././process/~/Process#property_pid)
*   [platform](.././process/~/Process#property_platform)
*   [ppid](.././process/~/Process#property_ppid)
*   [prependListener](.././process/~/Process#method_prependlistener_0)
*   [prependOnceListener](.././process/~/Process#method_prependoncelistener_0)
*   [ref](.././process/~/Process#method_ref_0)
*   [release](.././process/~/Process#property_release)
*   [report](.././process/~/Process#property_report)
*   [resourceUsage](.././process/~/Process#method_resourceusage_0)
*   [send](.././process/~/Process#method_send_0)
*   [setSourceMapsEnabled](.././process/~/Process#method_setsourcemapsenabled_0)
*   [setUncaughtExceptionCaptureCallback](.././process/~/Process#method_setuncaughtexceptioncapturecallback_0)
*   [setegid](.././process/~/Process#property_setegid)
*   [seteuid](.././process/~/Process#property_seteuid)
*   [setgid](.././process/~/Process#property_setgid)
*   [setgroups](.././process/~/Process#property_setgroups)
*   [setuid](.././process/~/Process#property_setuid)
*   [sourceMapsEnabled](.././process/~/Process#property_sourcemapsenabled)
*   [stderr](.././process/~/Process#property_stderr)
*   [stdin](.././process/~/Process#property_stdin)
*   [stdout](.././process/~/Process#property_stdout)
*   [throwDeprecation](.././process/~/Process#property_throwdeprecation)
*   [title](.././process/~/Process#property_title)
*   [traceDeprecation](.././process/~/Process#property_tracedeprecation)
*   [umask](.././process/~/Process#method_umask_0)
*   [unref](.././process/~/Process#method_unref_0)
*   [uptime](.././process/~/Process#method_uptime_0)
*   [version](.././process/~/Process#property_version)
*   [versions](.././process/~/Process#property_versions)

I

[ProcessConfig](.././process/~/ProcessConfig "ProcessConfig")

No documentation available

*   [target\_defaults](.././process/~/ProcessConfig#property_target_defaults)
*   [variables](.././process/~/ProcessConfig#property_variables)

I

[ProcessEnv](.././process/~/ProcessEnv "ProcessEnv")

No documentation available

*   [TZ](.././process/~/ProcessEnv#property_tz)

I

[ProcessFeatures](.././process/~/ProcessFeatures "ProcessFeatures")

No documentation available

*   [cached\_builtins](.././process/~/ProcessFeatures#property_cached_builtins)
*   [debug](.././process/~/ProcessFeatures#property_debug)
*   [inspector](.././process/~/ProcessFeatures#property_inspector)
*   [ipv6](.././process/~/ProcessFeatures#property_ipv6)
*   [require\_module](.././process/~/ProcessFeatures#property_require_module)
*   [tls](.././process/~/ProcessFeatures#property_tls)
*   [tls\_alpn](.././process/~/ProcessFeatures#property_tls_alpn)
*   [tls\_ocsp](.././process/~/ProcessFeatures#property_tls_ocsp)
*   [tls\_sni](.././process/~/ProcessFeatures#property_tls_sni)
*   [typescript](.././process/~/ProcessFeatures#property_typescript)
*   [uv](.././process/~/ProcessFeatures#property_uv)

I

[ProcessPermission](.././process/~/ProcessPermission "ProcessPermission")

No documentation available

*   [has](.././process/~/ProcessPermission#method_has_0)

I

[ProcessRelease](.././process/~/ProcessRelease "ProcessRelease")

No documentation available

*   [headersUrl](.././process/~/ProcessRelease#property_headersurl)
*   [libUrl](.././process/~/ProcessRelease#property_liburl)
*   [lts](.././process/~/ProcessRelease#property_lts)
*   [name](.././process/~/ProcessRelease#property_name)
*   [sourceUrl](.././process/~/ProcessRelease#property_sourceurl)

I

[ProcessReport](.././process/~/ProcessReport "ProcessReport")

No documentation available

*   [compact](.././process/~/ProcessReport#property_compact)
*   [directory](.././process/~/ProcessReport#property_directory)
*   [filename](.././process/~/ProcessReport#property_filename)
*   [getReport](.././process/~/ProcessReport#method_getreport_0)
*   [reportOnFatalError](.././process/~/ProcessReport#property_reportonfatalerror)
*   [reportOnSignal](.././process/~/ProcessReport#property_reportonsignal)
*   [reportOnUncaughtException](.././process/~/ProcessReport#property_reportonuncaughtexception)
*   [signal](.././process/~/ProcessReport#property_signal)
*   [writeReport](.././process/~/ProcessReport#method_writereport_0)

I

[ProcessVersions](.././process/~/ProcessVersions "ProcessVersions")

No documentation available

*   [ares](.././process/~/ProcessVersions#property_ares)
*   [http\_parser](.././process/~/ProcessVersions#property_http_parser)
*   [modules](.././process/~/ProcessVersions#property_modules)
*   [node](.././process/~/ProcessVersions#property_node)
*   [openssl](.././process/~/ProcessVersions#property_openssl)
*   [uv](.././process/~/ProcessVersions#property_uv)
*   [v8](.././process/~/ProcessVersions#property_v8)
*   [zlib](.././process/~/ProcessVersions#property_zlib)

I

[ReadStream](.././process/~/ReadStream "ReadStream")

No documentation available

I

[ResourceUsage](.././process/~/ResourceUsage "ResourceUsage")

No documentation available

*   [fsRead](.././process/~/ResourceUsage#property_fsread)
*   [fsWrite](.././process/~/ResourceUsage#property_fswrite)
*   [involuntaryContextSwitches](.././process/~/ResourceUsage#property_involuntarycontextswitches)
*   [ipcReceived](.././process/~/ResourceUsage#property_ipcreceived)
*   [ipcSent](.././process/~/ResourceUsage#property_ipcsent)
*   [majorPageFault](.././process/~/ResourceUsage#property_majorpagefault)
*   [maxRSS](.././process/~/ResourceUsage#property_maxrss)
*   [minorPageFault](.././process/~/ResourceUsage#property_minorpagefault)
*   [sharedMemorySize](.././process/~/ResourceUsage#property_sharedmemorysize)
*   [signalsCount](.././process/~/ResourceUsage#property_signalscount)
*   [swappedOut](.././process/~/ResourceUsage#property_swappedout)
*   [systemCPUTime](.././process/~/ResourceUsage#property_systemcputime)
*   [unsharedDataSize](.././process/~/ResourceUsage#property_unshareddatasize)
*   [unsharedStackSize](.././process/~/ResourceUsage#property_unsharedstacksize)
*   [userCPUTime](.././process/~/ResourceUsage#property_usercputime)
*   [voluntaryContextSwitches](.././process/~/ResourceUsage#property_voluntarycontextswitches)

I

[Socket](.././process/~/Socket "Socket")

No documentation available

*   [isTTY](.././process/~/Socket#property_istty)

I

[WriteStream](.././process/~/WriteStream "WriteStream")

No documentation available

### Type Aliases [#](<#Type Aliases>)

T

[Architecture](.././process/~/Architecture "Architecture")

No documentation available

T

[BeforeExitListener](.././process/~/BeforeExitListener "BeforeExitListener")

No documentation available

T

[DisconnectListener](.././process/~/DisconnectListener "DisconnectListener")

No documentation available

T

[ExitListener](.././process/~/ExitListener "ExitListener")

No documentation available

T

[MessageListener](.././process/~/MessageListener "MessageListener")

No documentation available

T

[MultipleResolveListener](.././process/~/MultipleResolveListener "MultipleResolveListener")

No documentation available

T

[MultipleResolveType](.././process/~/MultipleResolveType "MultipleResolveType")

No documentation available

T

[Platform](.././process/~/Platform "Platform")

No documentation available

T

[RejectionHandledListener](.././process/~/RejectionHandledListener "RejectionHandledListener")

No documentation available

T

[Signals](.././process/~/Signals "Signals")

No documentation available

T

[SignalsListener](.././process/~/SignalsListener "SignalsListener")

No documentation available

T

[UncaughtExceptionListener](.././process/~/UncaughtExceptionListener "UncaughtExceptionListener")

No documentation available

T

[UncaughtExceptionOrigin](.././process/~/UncaughtExceptionOrigin "UncaughtExceptionOrigin")

No documentation available

T

[UnhandledRejectionListener](.././process/~/UnhandledRejectionListener "UnhandledRejectionListener")

Most of the time the unhandledRejection will be an Error, but this should not be relied upon as _anything_ can be thrown/rejected, it is therefore unsafe to assume that the value is an Error.

T

[WarningListener](.././process/~/WarningListener "WarningListener")

No documentation available

T

[WorkerListener](.././process/~/WorkerListener "WorkerListener")

No documentation available

### Variables [#](#Variables)

v

[process](.././process/~/process "process")

No documentation available
