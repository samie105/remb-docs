---
title: "Authentication"
source: "https://outray.dev/docs/authentication"
canonical_url: "https://outray.dev/docs/authentication"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:23:59.611Z"
content_hash: "fcbb9e9404020a458e4399b4016534dd2af7ce4e1153430c0bfff0d9345dab7a"
menu_path: ["Authentication"]
section_path: []
nav_prev: {"path": "outray/docs/installation/index.md", "title": "Installation"}
nav_next: {"path": "outray/docs/opening-a-tunnel/index.md", "title": "Opening a Tunnel"}
---

## Authentication

How to authenticate with the OutRay CLI

Before you can start a tunnel, you need to authenticate with your OutRay account. This ensures that your tunnels are secure and associated with your user profile.

The easiest way to authenticate is using the interactive login command. Run the following command in your terminal:

```
outray login
```

This command will:

1.  Open your default web browser to the OutRay dashboard.
2.  Ask you to authorize the CLI.
3.  Once authorized, the CLI will automatically receive an authentication token and save it locally.

For environments where you cannot use a browser (like a remote server or CI/CD pipeline), you can authenticate using an API key.

1.  Go to your [Organization Settings](https://outray.dev/settings) in the dashboard.
2.  Generate a new API Key.
3.  Use the `--key` flag when running commands:

```
outray 3000 --key outray_sk_...
```

To verify that you are logged in and see which user/organization is active, run:

```
outray whoami
```
