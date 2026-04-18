---
title: "Enabling MCP Server Access"
source: "https://supabase.com/docs/guides/self-hosting/enable-mcp"
canonical_url: "https://supabase.com/docs/guides/self-hosting/enable-mcp"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:22.605Z"
content_hash: "cb2146d12538a465abf3ac4de8ac2c59b5e431d21c8ad6f20251bcc7a26f9ac6"
menu_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Enable MCP server","Enable MCP server"]
section_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Enable MCP server","Enable MCP server"]
nav_prev: {"path": "supabase/docs/guides/self-hosting/docker/index.md", "title": "Self-Hosting with Docker"}
nav_next: {"path": "supabase/docs/guides/self-hosting/postgres-upgrade-17/index.md", "title": "Upgrade to Postgres 17"}
---

# 

Enabling MCP Server Access

## 

Configure secure access to the MCP server in your self-hosted Supabase instance.

* * *

The MCP (Model Context Protocol) server in [self-hosted Supabase](/docs/guides/self-hosting/docker) runs behind the internal API. Currently, it does not offer OAuth 2.1 authentication, and is not intended to be exposed to the Internet. The corresponding API route has to be protected by restricting network connections from the outside. By default, all connections to the MCP server are denied.

This guide explains how to securely enable access to your self-hosted MCP server.

## Security considerations[#](#security-considerations)

Do not allow connections to the self-hosted MCP server from the Internet. Only access it via:

*   A VPN connection to the server running the Studio container
*   An SSH tunnel from your local machine

## Accessing via SSH tunnel[#](#accessing-via-ssh-tunnel)

### Step 1: Determine the local IP address that will be used to access the MCP server[#](#step-1-determine-the-local-ip-address-that-will-be-used-to-access-the-mcp-server)

When connecting via an SSH tunnel to the Studio Docker container, the source IP will be that of the Docker bridge gateway. You need to allow connections from this IP address.

Determine the Docker bridge gateway IP on the host running your Supabase containers:

```
1docker inspect supabase-kong \2  --format '{{range .NetworkSettings.Networks}}{{println .Gateway}}{{end}}'
```

This command will output an IP address, e.g., `172.18.0.1`.

### Step 2: Allow connections from the gateway IP[#](#step-2-allow-connections-from-the-gateway-ip)

Add the IP address you discovered to the Kong configuration by editing the following section in `./volumes/api/kong.yml`:

1.  Comment out the request-termination section
2.  Remove the # symbols from the entire section starting with `- name: cors`, including `deny: []`
3.  Add your local IP to the 'allow' list.
4.  Your edited configuration should look like the example below.

```
1## MCP endpoint - local access2- name: mcp3  _comment: 'MCP: /mcp -> http://studio:3000/api/mcp (local access)'4  url: http://studio:3000/api/mcp5  routes:6    - name: mcp7      strip_path: true8      paths:9        - /mcp10  plugins:11    # Block access to /mcp by default12    #- name: request-termination13    #  config:14    #    status_code: 40315    #    message: "Access is forbidden."16    # Enable local access (danger zone!)17    # 1. Comment out the 'request-termination' section above18    # 2. Uncomment the entire section below, including 'deny'19    # 3. Add your local IPs to the 'allow' list20    - name: cors21    - name: ip-restriction22      config:23        allow:24          - 127.0.0.125          - ::126          # Add your Docker bridge gateway IP below27          - 172.18.0.128        # Do not remove deny!29        deny: []
```

### Step 3: Restart API gateway[#](#step-3-restart-api-gateway)

After you've added the local IP address as above, restart the Kong container:

```
1docker compose restart kong
```

### Step 4: Create the SSH tunnel[#](#step-4-create-the-ssh-tunnel)

From your local machine, create an SSH tunnel to your Supabase host:

```
1ssh -L localhost:8080:localhost:8000 you@your-supabase-host
```

This command forwards local port `8080` to port `8000` on your Supabase host.

### Step 5: Configure your MCP client[#](#step-5-configure-your-mcp-client)

Edit the settings for your MCP client and add the following to `"mcpServers": {}` or `"servers": {}`:

```
1{2  "mcpServers": {3    "supabase-self-hosted": {4      "url": "http://localhost:8080/mcp"5    }6  }7}
```

### Step 6: Start using the self-hosted MCP server[#](#step-6-start-using-the-self-hosted-mcp-server)

From your local machine, check that the MCP server is reachable:

```
1curl http://localhost:8080/mcp \2  -X POST \3  -H "Content-Type: application/json" \4  -H "Accept: application/json, text/event-stream" \5  -H "MCP-Protocol-Version: 2025-06-18" \6  -d '{7    "jsonrpc": "2.0",8    "id": 1,9    "method": "initialize",10    "params": {11      "protocolVersion": "2025-06-18",12      "capabilities": {13        "elicitation": {}14      },15      "clientInfo": {16        "name": "test-client",17        "title": "Test Client",18        "version": "1.0.0"19      }20    }21  }'
```

Start your MCP client (Claude Code, Cursor, etc.) and verify access to the MCP tools. For example, you can ask: "What is Supabase anon key? Use the Supabase MCP server tools."

## Troubleshooting[#](#troubleshooting)

If you are unable to connect to the MCP server:

1.  Update Kong configuration file to the [latest version](https://github.com/supabase/supabase/blob/master/docker/volumes/api/kong.yml) and edit carefully
2.  Confirm the Docker bridge gateway IP is correctly added in `./volumes/api/kong.yml`
3.  Check Kong's logs for errors: `docker compose logs kong`
4.  Make sure your SSH tunnel is active
