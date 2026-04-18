---
title: "React Developer Tools"
source: "https://react.dev/learn/react-developer-tools"
canonical_url: "https://react.dev/learn/react-developer-tools"
docset: "react"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:40.272Z"
content_hash: "54bc954b44714db78639dfcb008b4f4e31356fd140a69fb201043bc6aec2ce4d"
menu_path: ["React Developer Tools"]
section_path: []
nav_prev: {"path": "react/learn/typescript/index.md", "title": "Using TypeScript"}
nav_next: {"path": "react/learn/react-compiler/index.md", "title": "React Compiler"}
---

# Yarnyarn global add react-devtools# Npmnpm install -g react-devtools
```

Next open the developer tools from the terminal:

```
react-devtools
```

Then connect your website by adding the following `<script>` tag to the beginning of your website’s `<head>`:

```
<html><head><script src="http://localhost:8097"></script>
```

Reload your website in the browser now to view it in developer tools.

![React Developer Tools standalone](https://react.dev/images/docs/react-devtools-standalone.png)

## Mobile (React Native)[](#mobile-react-native "Link for Mobile (React Native) ")

To inspect apps built with [React Native](https://reactnative.dev/), you can use [React Native DevTools](https://reactnative.dev/docs/react-native-devtools), the built-in debugger that deeply integrates React Developer Tools. All features work identically to the browser extension, including native element highlighting and selection.

[Learn more about debugging in React Native.](https://reactnative.dev/docs/debugging)

> For versions of React Native earlier than 0.76, please use the standalone build of React DevTools by following the [Safari and other browsers](#safari-and-other-browsers) guide above.

