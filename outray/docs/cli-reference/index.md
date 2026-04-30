---
title: "CLI Reference"
source: "https://outray.dev/docs/cli-reference"
canonical_url: "https://outray.dev/docs/cli-reference"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:27:50.236Z"
content_hash: "e321740412d79c59d5559e09e9844c1a8ccd79d6ef9e7f2ccf9575eed4757d2d"
menu_path: ["CLI Reference"]
section_path: []
nav_prev: {"path": "outray/docs/protocols/index.md", "title": "TCP & UDP Tunnels"}
nav_next: {"path": "outray/docs/architecture/index.md", "title": "Architecture"}
---

# Use default outray/config.toml
outray start

# Use a custom config file
outray start --config /path/to/config.toml
```

**Options:**

-   `--config <path>`: Path to the TOML configuration file (default: `outray/config.toml`).

See the [Configuration Files](index.md) section below for details on the config file format.

### [`outray validate-config`](#outray-validate-config)

Validates a TOML configuration file without starting any tunnels. Useful for checking your config file syntax and structure.

```
# Validate default outray/config.toml
outray validate-config

# Validate a custom config file
outray validate-config --config /path/to/config.toml
```

**Options:**

-   `--config <path>`: Path to the TOML configuration file (default: `outray/config.toml`).

### [`outray <port>`](#outray-port)

Starts a tunnel for the specified local port. This is the most common command you will use.

```
outray 3000
```

**Arguments:**

-   `port`: The local port number you want to expose (e.g., `3000`, `8080`).

**Options:**

-   `--subdomain <name>`: Request a specific subdomain.
-   `--domain <domain>`: Use a custom domain.
-   `--org <slug>`: Run the tunnel under a specific organization.
-   `--key <token>`: Use a specific API key instead of the logged-in user.
-   `--no-logs`: Disable tunnel request logs.

### [`outray switch`](#outray-switch)

Switch between organizations. If you belong to multiple organizations, you can use this command to change your active context.

```
# Interactive selection
outray switch

# Direct switch
outray switch my-org-slug
```

### [`outray whoami`](#outray-whoami)

Displays information about the currently authenticated user and the active organization.

```
outray whoami
```

### [`outray logout`](#outray-logout)

Clears the local authentication credentials.

```
outray logout
```

You can define multiple tunnels in a TOML configuration file and start them all at once using the `outray start` command.

### [Config File Format](#config-file-format)

Create an `outray/config.toml` file in your project directory:

```
[global]
org = "my-team"
server_url = "wss://api.outray.dev/"

[tunnel.web]
protocol = "http"
local_port = 3000
local_host = "localhost"
subdomain = "my-app"
custom_domain = "app.example.com"

[tunnel.api]
protocol = "http"
local_port = 8000
subdomain = "api"

[tunnel.postgres]
protocol = "tcp"
local_port = 5432
local_host = "localhost"
remote_port = 20000

[tunnel.game-server]
protocol = "udp"
local_port = 5000
remote_port = 30000
```

### [Configuration Options](#configuration-options)

**Global Settings:**

-   `org`: Default organization slug for all tunnels (can be overridden per tunnel)
-   `server_url`: Tunnel server URL (optional, defaults to production server)

**Tunnel Settings:**

-   `protocol`: Tunnel protocol - `"http"`, `"tcp"`, or `"udp"` (required)
-   `local_port`: Local port number to expose (required, 1-65535)
-   `local_host`: Local hostname (optional, defaults to `"localhost"`)
-   `subdomain`: Custom subdomain for HTTP tunnels (optional, HTTP only)
-   `custom_domain`: Custom domain for HTTP tunnels (optional, HTTP only)
-   `remote_port`: Remote port for TCP/UDP tunnels (optional, TCP/UDP only)
-   `org`: Organization slug for this tunnel (optional, overrides global setting)

### [Example Usage](#example-usage)

```
# Validate your config file first
outray validate-config

# Start all tunnels from outray/config.toml
outray start

# Start tunnels from a custom config file
outray start --config production.toml
```

These flags can be used with most commands:

-   `--version`, `-v`: Display the current CLI version.
-   `--help`, `-h`: Display help information.
-   `--config <path>`: Path to config file (for `start` and `validate-config` commands).
-   `--no-logs`: Disable tunnel request logs (for tunnel commands).
