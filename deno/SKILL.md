**Overview**

Deno is a secure-by-default JavaScript/TypeScript runtime that ships as a single executable with built-in testing, formatting, linting, and dependency management. Agents need to know Deno to write portable scripts and services that explicitly declare permissions, leverage web-standard APIs, and deploy across servers and edge environments.

**Mental Model**

Deno treats host access—file system, network, subprocesses, and environment—as privileged operations that must be granted at runtime through a granular permission system (`deno/api/deno/permissions/index.md`). The runtime exposes capabilities through a unified `Deno` namespace (`deno/api/deno/index.md`) while keeping web-compatible primitives like fetch and HTTP servers (`deno/api/deno/fetch/index.md`, `deno/api/deno/http-server/index.md`) first-class. This architecture favors explicit capability declarations over implicit global access, so an agent should always check permissions and errors before performing I/O.

**Learning Paths**

**1. Getting Started**
- `deno/api/deno/index.md` — Explore the Deno namespace and core APIs.
- `deno/api/deno/runtime/index.md` — Learn process, signal, and environment basics.
- `deno/api/deno/file-system/index.md` — Master file handles and disk operations.
- `deno/examples/reading_files/index.md` — Follow a practical file-reading tutorial.

**2. Production Networking**
- `deno/api/deno/permissions/index.md` — Understand the permission model.
- `deno/api/deno/network/index.md` — Work with TCP and QUIC endpoints.
- `deno/api/deno/fetch/index.md` — Configure HTTP clients and proxies.
- `deno/api/deno/http-server/index.md` — Build services with `Deno.serve`.
- `deno/examples/file_server_tutorial/index.md` — Complete a file-server tutorial.

**3. Advanced & Specialized**
- `deno/api/deno/errors/index.md` — Catalog runtime error classes.
- `deno/api/deno/ffi/index.md` — Interface with native libraries.
- `deno/api/deno/gpu/index.md` — Use WebGPU and window surfaces.
- `deno/api/deno/cloud/index.md` — Operate KV and cloud primitives.
- `deno/api/deno/jupyter/index.md` — Integrate with Jupyter notebooks.

**Concept Map**

- **Core Runtime**
  - Namespace APIs → `deno/api/deno/index.md`
  - Runtime → `deno/api/deno/runtime/index.md`
  - Permissions → `deno/api/deno/permissions/index.md`
  - Errors → `deno/api/deno/errors/index.md`
- **I/O & Network**
  - File System → `deno/api/deno/file-system/index.md`
  - I/O → `deno/api/deno/io/index.md`
  - Network → `deno/api/deno/network/index.md`
  - Fetch → `deno/api/deno/fetch/index.md`
- **Server & Cloud**
  - HTTP Server → `deno/api/deno/http-server/index.md`
  - Cloud / KV → `deno/api/deno/cloud/index.md`
  - GPU → `deno/api/deno/gpu/index.md`
- **Tooling & Extension**
  - Linter → `deno/api/deno/linter/index.md`
  - Jupyter → `deno/api/deno/jupyter/index.md`
  - FFI → `deno/api/deno/ffi/index.md`
- **Reference**
  - All Symbols → `deno/api/deno/all_symbols/index.md`

**If You Need To...**

| If you need to... | Read |
|---|---|
| Understand the Deno namespace and entry points | `deno/api/deno/index.md` |
| Query or request runtime permissions | `deno/api/deno/permissions/index.md` |
| Read, write, or lock files | `deno/api/deno/file-system/index.md` |
| Call remote APIs or configure proxies | `deno/api/deno/fetch/index.md` |
| Accept TCP/QUIC connections | `deno/api/deno/network/index.md` |
| Serve HTTP traffic | `deno/api/deno/http-server/index.md` |
| Handle runtime exceptions | `deno/api/deno/errors/index.md` |
| Bind native libraries | `deno/api/deno/ffi/index.md` |
| Use WebGPU or window surfaces | `deno/api/deno/gpu/index.md` |
| Run Deno in Jupyter notebooks | `deno/api/deno/jupyter/index.md` |
| Build a custom linter plugin | `deno/api/deno/linter/index.md` |

**Top Must-Know Pages**

1. `deno/api/deno/index.md` — The canonical entry point for the Deno namespace, covering built-in APIs and links to examples.
2. `deno/api/deno/permissions/index.md` — Defines how to query, request, and revoke runtime access to system resources.
3. `deno/api/deno/runtime/index.md` — Documents process control, current working directory, signal handling, and execution context.
4. `deno/api/deno/file-system/index.md` — Provides file-handle operations, locking, and terminal detection for disk I/O.
5. `deno/api/deno/network/index.md` — Describes low-level networking primitives including QUIC endpoints and TCP connections.
6. `deno/api/deno/fetch/index.md` — Covers HTTP client configuration, custom agents, proxy support, and `Deno.HttpClient`.
7. `deno/api/deno/http-server/index.md` — Reference for `Deno.serve`, server lifecycle, and the `HttpServer` API.
8. `deno/api/deno/errors/index.md` — Catalog of runtime-specific error classes such as `AddrInUse` and `BadResource`.
9. `deno/api/deno/ffi/index.md` — Explains unsafe callbacks, pointer definitions, and foreign function interface bindings.
10. `deno/api/deno/cloud/index.md` — Introduces KV atomic operations and cloud-native primitives for Deno Deploy.