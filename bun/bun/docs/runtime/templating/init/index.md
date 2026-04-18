---
title: "bun init"
source: "https://bun.com/docs/runtime/templating/init"
canonical_url: "https://bun.com/docs/runtime/templating/init"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:55.959Z"
content_hash: "35a544ac8dddb708fc53a7c2d45028f9bb0baee2283bc7a0fb4f11dbaac9ecd8"
menu_path: ["bun init"]
section_path: []
nav_prev: {"path": "bun/bun/docs/runtime/toml/index.md", "title": "TOML"}
nav_next: {"path": "bun/bun/docs/runtime/transpiler/index.md", "title": "Transpiler"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](/docs)[Package Manager

](/docs/pm/cli/install)[Bundler

](/docs/bundler)[Test Runner

](/docs/test)[Guides

](/docs/guides)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](/docs/feedback)

Get started with Bun by scaffolding a new project with `bun init`.

terminal

```
bun init my-app
```

```
? Select a project template - Press return to submit.
❯ Blank
  React
  Library

✓ Select a project template: Blank

 + .gitignore
 + CLAUDE.md
 + .cursor/rules/use-bun-instead-of-node-vite-npm-pnpm.mdc -> CLAUDE.md
 + index.ts
 + tsconfig.json (for editor autocomplete)
 + README.md
```

Press `enter` to accept the default answer for each prompt, or pass the `-y` flag to auto-accept the defaults.

* * *

`bun init` scaffolds a new project with Bun. It infers settings with sane defaults and is non-destructive when run multiple times.

![Demo](https://user-images.githubusercontent.com/709451/183006613-271960a3-ff22-4f7c-83f5-5e18f684c836.gif)

It creates:

*   a `package.json` file with a name that defaults to the current directory name
*   a `tsconfig.json` file or a `jsconfig.json` file, depending if the entry point is a TypeScript file or not
*   an entry point which defaults to `index.ts` unless any of `index.{tsx, jsx, js, mts, mjs}` exist or the `package.json` specifies a `module` or `main` field
*   a `README.md` file

AI Agent rules (disable with `$BUN_AGENT_RULE_DISABLED=1`):

*   a `CLAUDE.md` file when Claude CLI is detected (disable with `CLAUDE_CODE_AGENT_RULE_DISABLED` env var)
*   a `.cursor/rules/*.mdc` file to guide [Cursor AI](https://cursor.sh) to use Bun instead of Node.js and npm when Cursor is detected

If you pass `-y` or `--yes`, it will assume you want to continue without asking questions. At the end, it runs `bun install` to install `@types/bun`.

* * *

## 

[​

](#cli-usage)

CLI Usage

terminal

```
bun init <folder?>
```

### 

[​

](#initialization-options)

Initialization Options

[​

](#param-yes)

\--yes

boolean

Accept all default prompts without asking questions. Alias: `-y`

[​

](#param-minimal)

\--minimal

boolean

Only initialize type definitions (skip app scaffolding). Alias: `-m`

### 

[​

](#project-templates)

Project Templates

[​

](#param-react)

\--react

string|boolean

Scaffold a React project. When used without a value, creates a baseline React app.  
Accepts values for presets:

*   `tailwind` – React app preconfigured with Tailwind CSS
*   `shadcn` – React app with `@shadcn/ui` and Tailwind CSS

Examples:

```
bun init —react bun init —react=tailwind bun init —react=shadcn
```

### 

[​

](#output-&-files)

Output & Files

[​

](#param-result)

(result)

info

Initializes project files and configuration for the chosen options (e.g., creating essential config files and a starter directory structure). Exact files vary by template.

### 

[​

](#global-configuration-&-context)

Global Configuration & Context

[​

](#param-cwd)

\--cwd

string

Run `bun init` as if started in a different working directory (useful in scripts).

### 

[​

](#help)

Help

[​

](#param-help)

\--help

boolean

Print this help menu. Alias: `-h`

### 

[​

](#examples)

Examples

*   Accept all defaults
    
    terminal
    
    ```
    bun init -y
    ```
    
*   React
    
    terminal
    
    ```
    bun init --react
    ```
    
*   React + Tailwind CSS
    
    terminal
    
    ```
    bun init --react=tailwind
    ```
    
*   React + @shadcn/ui
    
    terminal
    
    ```
    bun init --react=shadcn
    ```
    

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/runtime/templating/init.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /runtime/templating/init>)

[

TypeScript 6 and 7

Previous

](/docs/typescript-6)[

bun create

Next

](/docs/runtime/templating/create)

![Demo](https://user-images.githubusercontent.com/709451/183006613-271960a3-ff22-4f7c-83f5-5e18f684c836.gif)
