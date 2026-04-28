1. **Overview**
Bun is an all-in-one JavaScript toolkit that bundles, transpiles, runs, and tests code from a single binary. It replaces Node.js, esbuild, Babel, and npm with a unified, high-performance engine. Agents need to know Bun to build, bundle, and deploy modern JavaScript/TypeScript applications efficiently.

2. **Mental Model**
Bun collapses the traditional toolchain into a single layer: the runtime, package manager, bundler, and test runner all share a common core built on JavaScriptCore and Zig. This means the same loader, plugin, and module resolution logic applies whether you are running a script in dev mode or compiling a standalone executable. Start with the entry points at `bun/docs/index.md`, `bun/docs/bundler/index.md`, and `bun/docs/runtime/index.md` to understand how execution and bundling are unified.

3. **Learning Paths**
- **Getting Started** — `bun/docs/index.md` → `bun/docs/cli/index.md` → `bun/docs/runtime/index.md` → `bun/docs/bundler/index.md`
- **Production Ready** — `bun/docs/pm/cli/install.md` → `bun/docs/bundler/minifier/index.md` → `bun/docs/bundler/executables/index.md` → `bun/docs/guides/docker/index.md`
- **Reference Deep-Dive** — `bun/docs/bundler/plugins/index.md` → `bun/docs/bundler/loaders/index.md` → `bun/docs/bundler/macros/index.md` → `bun/docs/bundler/esbuild/index.md`

4. **Concept Map**
- Runtime & APIs
  - Runtime API → `bun/docs/runtime/index.md`
  - Module Import / ES Modules → `bun/docs/runtime/modules.md`
  - JSX → `bun/docs/runtime/jsx.md`
  - JSON → `bun/docs/runtime/json.md`
  - Error Handling → `bun/docs/runtime/error-handling.md`
- CLI & Package Management
  - CLI Usage → `bun/docs/cli/index.md`
  - Install Dependencies → `bun/docs/pm/cli/install.md`
- Bundler
  - Overview / Configuration / Examples → `bun/docs/bundler/index.md`
  - Usage / Basic Usage → `bun/docs/bundler/bytecode/index.md`, `bun/docs/bundler/minifier/index.md`
  - Loaders → `bun/docs/bundler/loaders/index.md`
  - Plugins
    - Lifecycle Hooks → `bun/docs/bundler/plugins/index.md`
    - onresolve / onload → `bun/docs/bundler/plugins/index.md`
    - Reference → `bun/docs/bundler/plugins/index.md`
  - Content & Styling
    - CSS → `bun/docs/bundler/css/index.md`
    - HTML & Static Sites → `bun/docs/bundler/html-static/index.md`
    - Standalone HTML → `bun/docs/bundler/standalone-html/index.md`
  - Outputs
    - Single-file Executables → `bun/docs/bundler/executables/index.md`
    - Bytecode Caching → `bun/docs/bundler/bytecode/index.md`
  - Developer Experience
    - Hot Reloading → `bun/docs/bundler/hot-reloading/index.md`
    - Fullstack Dev Server → `bun/docs/bundler/fullstack/index.md`
    - Minifier → `bun/docs/bundler/minifier/index.md`
  - Advanced
    - Macros → `bun/docs/bundler/macros/index.md`
    - esbuild Comparison → `bun/docs/bundler/esbuild/index.md`
- Testing
  - Overview → `bun/docs/test/index.md`
- Guides
  - Docker
    - Official Image / package.json & bun.lockb / Dependencies / Application Copy → `bun/docs/guides/docker/index.md`
  - Binary Data → `bun/docs/guides/binary/arraybuffer-to-array/index.md`
- Meta
  - Feedback → `bun/docs/feedback/index.md`

5. **If You Need To...**
| If you need to... | Read |
|---|---|
| Get started quickly | `bun/docs/index.md` |
| Understand the runtime API | `bun/docs/runtime/index.md` |
| Bundle an application | `bun/docs/bundler/index.md` |
| Minify for production | `bun/docs/bundler/minifier/index.md` |
| Build a standalone executable | `bun/docs/bundler/executables/index.md` |
| Add custom loaders or plugins | `bun/docs/bundler/plugins/index.md` |
| Resolve or load modules manually | `bun/docs/bundler/plugins/index.md` |
| Handle CSS, JSX, TS, or TSX | `bun/docs/bundler/loaders/index.md` |
| Set up a fullstack dev server | `bun/docs/bundler/fullstack/index.md` |
| Configure hot reloading | `bun/docs/bundler/hot-reloading/index.md` |
| Use build-time macros | `bun/docs/bundler/macros/index.md` |
| Cache bytecode | `bun/docs/bundler/bytecode/index.md` |
| Compare with esbuild | `bun/docs/bundler/esbuild/index.md` |
| Install packages | `bun/docs/pm/cli/install.md` |
| Run tests | `bun/docs/test/index.md` |
| Deploy with Docker | `bun/docs/guides/docker/index.md` |
| Convert an ArrayBuffer to an array | `bun/docs/guides/binary/arraybuffer-to-array/index.md` |

6. **Top Must-Know Pages**
1. `bun/docs/index.md` — Entry point for quickstart, overview, and basic orientation.
2. `bun/docs/runtime/index.md` — Runtime APIs, module execution, and core environment.
3. `bun/docs/bundler/index.md` — Bundler overview, configuration, and why/when to bundle.
4. `bun/docs/bundler/plugins/index.md` — Plugin lifecycle, hooks, namespaces, and reference.
5. `bun/docs/bundler/loaders/index.md` — Built-in loaders for JavaScript, TypeScript, and JSX.
6. `bun/docs/bundler/minifier/index.md` — CLI usage, production mode, and granular minification controls.
7. `bun/docs/bundler/executables/index.md` — Cross-compiling single-file executables for any platform.
8. `bun/docs/pm/cli/install.md` — Package installation and dependency management.
9. `bun/docs/test/index.md` — Test runner overview and usage.
10. `bun/docs/bundler/esbuild/index.md` — Performance characteristics and API differences from esbuild.