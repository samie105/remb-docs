---
title: "Permissions - Deno documentation"
source: "https://docs.deno.com/api/deno/permissions"
canonical_url: "https://docs.deno.com/api/deno/permissions"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:10:32.667Z"
content_hash: "bcbbf9e60d7e1f8d6c442766e31ba19e69ccfae3796162d7c88e26d76b620960"
menu_path: ["Permissions - Deno documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/deno/network/index.md", "title": "Network - Deno documentation"}
nav_next: {"path": "deno/deno/api/deno/runtime/index.md", "title": "Runtime - Deno documentation"}
---

### Classes [#](#Classes)

c

[Deno.Permissions](./././~/Deno.Permissions "Deno.Permissions")

Deno's permission management API.

*   [query](./././~/Deno.Permissions#method_query_0)
*   [querySync](./././~/Deno.Permissions#method_querysync_0)
*   [request](./././~/Deno.Permissions#method_request_0)
*   [requestSync](./././~/Deno.Permissions#method_requestsync_0)
*   [revoke](./././~/Deno.Permissions#method_revoke_0)
*   [revokeSync](./././~/Deno.Permissions#method_revokesync_0)

c

[Deno.PermissionStatus](./././~/Deno.PermissionStatus "Deno.PermissionStatus")

An `EventTarget` returned from the [`Deno.permissions`](./././~/Deno.permissions) API which can provide updates to any state changes of the permission.

*   [addEventListener](./././~/Deno.PermissionStatus#method_addeventlistener_0)
*   [onchange](./././~/Deno.PermissionStatus#property_onchange)
*   [partial](./././~/Deno.PermissionStatus#property_partial)
*   [removeEventListener](./././~/Deno.PermissionStatus#method_removeeventlistener_0)
*   [state](./././~/Deno.PermissionStatus#property_state)

### Interfaces [#](#Interfaces)

I

[Deno.EnvPermissionDescriptor](./././~/Deno.EnvPermissionDescriptor "Deno.EnvPermissionDescriptor")

The permission descriptor for the `allow-env` and `deny-env` permissions, which controls access to being able to read and write to the process environment variables as well as access other information about the environment. The option `variable` allows scoping the permission to a specific environment variable.

*   [name](./././~/Deno.EnvPermissionDescriptor#property_name)
*   [variable](./././~/Deno.EnvPermissionDescriptor#property_variable)

I

[Deno.FfiPermissionDescriptor](./././~/Deno.FfiPermissionDescriptor "Deno.FfiPermissionDescriptor")

The permission descriptor for the `allow-ffi` and `deny-ffi` permissions, which controls access to loading _foreign_ code and interfacing with it via the [Foreign Function Interface API](https://docs.deno.com/runtime/manual/runtime/ffi_api) available in Deno. The option `path` allows scoping the permission to a specific path on the host.

*   [name](./././~/Deno.FfiPermissionDescriptor#property_name)
*   [path](./././~/Deno.FfiPermissionDescriptor#property_path)

I

[Deno.ImportPermissionDescriptor](./././~/Deno.ImportPermissionDescriptor "Deno.ImportPermissionDescriptor")

The permission descriptor for the `allow-import` and `deny-import` permissions, which controls access to importing from remote hosts via the network. The option `host` allows scoping the permission for outbound connection to a specific host and port.

*   [host](./././~/Deno.ImportPermissionDescriptor#property_host)
*   [name](./././~/Deno.ImportPermissionDescriptor#property_name)

I

[Deno.NetPermissionDescriptor](./././~/Deno.NetPermissionDescriptor "Deno.NetPermissionDescriptor")

The permission descriptor for the `allow-net` and `deny-net` permissions, which controls access to opening network ports and connecting to remote hosts via the network. The option `host` allows scoping the permission for outbound connection to a specific host and port.

*   [host](./././~/Deno.NetPermissionDescriptor#property_host)
*   [name](./././~/Deno.NetPermissionDescriptor#property_name)

I

[Deno.PermissionOptionsObject](./././~/Deno.PermissionOptionsObject "Deno.PermissionOptionsObject")

A set of options which can define the permissions within a test or worker context at a highly specific level.

*   [env](./././~/Deno.PermissionOptionsObject#property_env)
*   [ffi](./././~/Deno.PermissionOptionsObject#property_ffi)
*   [import](./././~/Deno.PermissionOptionsObject#property_import)
*   [net](./././~/Deno.PermissionOptionsObject#property_net)
*   [read](./././~/Deno.PermissionOptionsObject#property_read)
*   [run](./././~/Deno.PermissionOptionsObject#property_run)
*   [sys](./././~/Deno.PermissionOptionsObject#property_sys)
*   [write](./././~/Deno.PermissionOptionsObject#property_write)

I

[Deno.PermissionStatusEventMap](./././~/Deno.PermissionStatusEventMap "Deno.PermissionStatusEventMap")

The interface which defines what event types are supported by `PermissionStatus` instances.

*   [change](./././~/Deno.PermissionStatusEventMap#property_change)

I

[Deno.ReadPermissionDescriptor](./././~/Deno.ReadPermissionDescriptor "Deno.ReadPermissionDescriptor")

The permission descriptor for the `allow-read` and `deny-read` permissions, which controls access to reading resources from the local host. The option `path` allows scoping the permission to a specific path (and if the path is a directory any sub paths).

*   [name](./././~/Deno.ReadPermissionDescriptor#property_name)
*   [path](./././~/Deno.ReadPermissionDescriptor#property_path)

I

[Deno.RunPermissionDescriptor](./././~/Deno.RunPermissionDescriptor "Deno.RunPermissionDescriptor")

The permission descriptor for the `allow-run` and `deny-run` permissions, which controls access to what sub-processes can be executed by Deno. The option `command` allows scoping the permission to a specific executable.

*   [command](./././~/Deno.RunPermissionDescriptor#property_command)
*   [name](./././~/Deno.RunPermissionDescriptor#property_name)

I

[Deno.SysPermissionDescriptor](./././~/Deno.SysPermissionDescriptor "Deno.SysPermissionDescriptor")

The permission descriptor for the `allow-sys` and `deny-sys` permissions, which controls access to sensitive host system information, which malicious code might attempt to exploit. The option `kind` allows scoping the permission to a specific piece of information.

*   [kind](./././~/Deno.SysPermissionDescriptor#property_kind)
*   [name](./././~/Deno.SysPermissionDescriptor#property_name)

I

[Deno.WritePermissionDescriptor](./././~/Deno.WritePermissionDescriptor "Deno.WritePermissionDescriptor")

The permission descriptor for the `allow-write` and `deny-write` permissions, which controls access to writing to resources from the local host. The option `path` allow scoping the permission to a specific path (and if the path is a directory any sub paths).

*   [name](./././~/Deno.WritePermissionDescriptor#property_name)
*   [path](./././~/Deno.WritePermissionDescriptor#property_path)

### Type Aliases [#](<#Type Aliases>)

T

[Deno.PermissionDescriptor](./././~/Deno.PermissionDescriptor "Deno.PermissionDescriptor")

Permission descriptors which define a permission and can be queried, requested, or revoked.

T

[Deno.PermissionName](./././~/Deno.PermissionName "Deno.PermissionName")

The name of a privileged feature which needs permission.

T

[Deno.PermissionOptions](./././~/Deno.PermissionOptions "Deno.PermissionOptions")

Options which define the permissions within a test or worker context.

T

[Deno.PermissionState](./././~/Deno.PermissionState "Deno.PermissionState")

The current status of the permission:

### Variables [#](#Variables)

v

[Deno.permissions](./././~/Deno.permissions "Deno.permissions")

Deno's permission management API.


