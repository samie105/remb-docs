---
title: "PostgreSQL: Documentation: 18: 30.4. Extensibility"
source: "https://www.postgresql.org/docs/current/jit-extensibility.html"
canonical_url: "https://www.postgresql.org/docs/current/jit-extensibility.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:28.634Z"
content_hash: "9f7d22786b925adf7771deab210f16394cbee9f552baa438a8250f8dfb6488b1"
menu_path: ["PostgreSQL: Documentation: 18: 30.4. Extensibility"]
section_path: []
nav_prev: {"path": "postgres/docs/current/catalog-pg-policy.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.38.\u00a0pg_policy"}
nav_next: {"path": "postgres/docs/current/rangetypes.html/index.md", "title": "PostgreSQL: Documentation: 18: 8.17.\u00a0Range Types"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/jit-extensibility.html "PostgreSQL devel - 30.4. Extensibility")

Unsupported versions: [13](https://www.postgresql.org/docs/13/jit-extensibility.html "PostgreSQL 13 - 30.4. Extensibility") / [12](https://www.postgresql.org/docs/12/jit-extensibility.html "PostgreSQL 12 - 30.4. Extensibility") / [11](https://www.postgresql.org/docs/11/jit-extensibility.html "PostgreSQL 11 - 30.4. Extensibility")

### 30.4.1. Inlining Support for Extensions [#](#JIT-EXTENSIBILITY-BITCODE)

PostgreSQL's JIT implementation can inline the bodies of functions of types `C` and `internal`, as well as operators based on such functions. To do so for functions in extensions, the definitions of those functions need to be made available. When using [PGXS](https://www.postgresql.org/docs/current/extend-pgxs.html "36.18. Extension Building Infrastructure") to build an extension against a server that has been compiled with LLVM JIT support, the relevant files will be built and installed automatically.

The relevant files have to be installed into `$pkglibdir/bitcode/$extension/` and a summary of them into `$pkglibdir/bitcode/$extension.index.bc`, where `$pkglibdir` is the directory returned by `pg_config --pkglibdir` and `$extension` is the base name of the extension's shared library.

### Note

For functions built into PostgreSQL itself, the bitcode is installed into `$pkglibdir/bitcode/postgres`.

### 30.4.2. Pluggable JIT Providers [#](#JIT-PLUGGABLE)

PostgreSQL provides a JIT implementation based on LLVM. The interface to the JIT provider is pluggable and the provider can be changed without recompiling (although currently, the build process only provides inlining support data for LLVM). The active provider is chosen via the setting [jit\_provider](postgres/docs/current/runtime-config-client.html/index.md#GUC-JIT-PROVIDER).

#### 30.4.2.1. JIT Provider Interface [#](#JIT-PLUGGABLE-PROVIDER-INTERFACE)

A JIT provider is loaded by dynamically loading the named shared library. The normal library search path is used to locate the library. To provide the required JIT provider callbacks and to indicate that the library is actually a JIT provider, it needs to provide a C function named `_PG_jit_provider_init`. This function is passed a struct that needs to be filled with the callback function pointers for individual actions:

struct JitProviderCallbacks
{
    JitProviderResetAfterErrorCB reset\_after\_error;
    JitProviderReleaseContextCB release\_context;
    JitProviderCompileExprCB compile\_expr;
};

extern void \_PG\_jit\_provider\_init(JitProviderCallbacks \*cb);

