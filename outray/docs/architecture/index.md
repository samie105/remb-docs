---
title: "Architecture"
source: "https://outray.dev/docs/architecture"
canonical_url: "https://outray.dev/docs/architecture"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:27:50.674Z"
content_hash: "cc060eb27e0884f6acc9cd8e45c9ec91fec8b61c525abd9367a7cd4450979565"
menu_path: ["Architecture"]
section_path: []
nav_prev: {"path": "outray/docs/cli-reference/index.md", "title": "CLI Reference"}
---

## Architecture

Understanding how OutRay works under the hood

OutRay is designed to be simple yet robust.

The OutRay system consists of three main components:

1.  **The Client (CLI)**: Runs on your local machine.
2.  **The Tunnel Server**: Runs in the cloud (or your server) and acts as the bridge.
3.  **The Web Dashboard**: Manages users, organizations, and configurations.

1.  **Initialization**: When you run `outray 3000`, the CLI initiates a WebSocket connection to the Tunnel Server.
2.  **Authentication**: The server verifies your identity using the token provided during login or via the `--key` flag.
3.  **Tunnel Establishment**: Once authenticated, the server assigns a public URL (e.g., `https://random.tunnel.outray.app`) to your connection.
4.  **Request Handling**:
    -   A visitor accesses the public URL.
    -   The Tunnel Server receives the request.
    -   The server forwards the request payload over the WebSocket connection to the CLI.
    -   The CLI proxies the request to your local server (e.g., `localhost:3000`).
    -   Your local server responds.
    -   The CLI sends the response back through the WebSocket to the Tunnel Server.
    -   The Tunnel Server sends the response to the visitor.

-   **Encryption**: All traffic between the CLI and the Tunnel Server is encrypted using TLS (WSS).
-   **Isolation**: Each tunnel is isolated. Traffic meant for one tunnel cannot be routed to another.
-   **Authentication**: Tunnels are tied to user accounts or API keys, preventing unauthorized usage of your resources.
