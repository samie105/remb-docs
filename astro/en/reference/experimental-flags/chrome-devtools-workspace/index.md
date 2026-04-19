---
title: "Experimental Chrome DevTools workspace"
source: "https://docs.astro.build/en/reference/experimental-flags/chrome-devtools-workspace/"
canonical_url: "https://docs.astro.build/en/reference/experimental-flags/chrome-devtools-workspace/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:00.361Z"
content_hash: "7eae4b92a371388209fe178623b832ec10da93e8b71587e6b10450480037a8a8"
menu_path: ["Experimental Chrome DevTools workspace"]
section_path: []
nav_prev: {"path": "astro/en/reference/experimental-flags/content-intellisense/index.md", "title": "Experimental Intellisense for content collections"}
nav_next: {"path": "astro/en/reference/experimental-flags/svg-optimization/index.md", "title": "Experimental SVG optimization"}
---

# Experimental Chrome DevTools workspace

**Type:** `boolean`  
**Default:** `false`  

**Added in:** `astro@5.13.0`

Enables experimental [Chrome DevTools workspace integration](https://developer.chrome.com/docs/devtools/workspaces) for the Astro dev server.

This feature allows you to edit files directly in Chrome DevTools and have those changes reflected in your local file system via a connected workspace folder. This is useful for applying edits such as adjusting CSS values without leaving your browser tab.

With this feature enabled, running `astro dev` will automatically configure a Chrome DevTools workspace for your project. Your project will then appear as an available [workspace source that you can connect](#connecting-your-project). Then, changes that you make in the “Sources” panel are automatically saved to your project source code.

To enable this feature, add the experimental flag `chromeDevtoolsWorkspace` to your Astro config:

```
import { defineConfig } from 'astro/config';
export default defineConfig({  experimental: {    chromeDevtoolsWorkspace: true,  },});
```

## Connecting your project

[Section titled “Connecting your project”](#connecting-your-project)

Astro will create the necessary configuration file to support Chrome DevTools workspaces. However, your project must also be [connected as a source](https://developer.chrome.com/docs/devtools/workspaces#manual-connection) to enable file saving.

1.  [Start the Astro dev server](/en/develop-and-build/#start-the-astro-dev-server) with the appropriate CLI command for your package manager.
    
2.  Navigate to your site preview (e.g. `http://localhost:4321/`) in Chrome and open DevTools.
    
3.  Under the **Sources** > **Workspaces** tab, you will find your Astro project folder. Click **Connect** to add your directory as a workspace.
    

See the [Chrome DevTools workspace documentation](https://developer.chrome.com/docs/devtools/workspaces#connect) for more information.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
