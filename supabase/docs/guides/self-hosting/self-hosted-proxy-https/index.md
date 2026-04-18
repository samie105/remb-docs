---
title: "Configure Reverse Proxy and HTTPS"
source: "https://supabase.com/docs/guides/self-hosting/self-hosted-proxy-https"
canonical_url: "https://supabase.com/docs/guides/self-hosting/self-hosted-proxy-https"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:51.613Z"
content_hash: "b0830e7c07176c70394d0ae6c36dedee02a06f1da5c350e24f4738c80c398c03"
menu_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Add Reverse Proxy with HTTPS","Add Reverse Proxy with HTTPS"]
section_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Add Reverse Proxy with HTTPS","Add Reverse Proxy with HTTPS"]
nav_prev: {"path": "supabase/docs/guides/self-hosting/self-hosted-phone-mfa/index.md", "title": "Configure Phone Login & MFA"}
nav_next: {"path": "supabase/docs/guides/self-hosting/self-hosted-s3/index.md", "title": "Configure S3 Storage"}
---

# 

Configure Reverse Proxy and HTTPS

## 

Set up a reverse proxy with HTTPS for self-hosted Supabase.

* * *

HTTPS is required for production self-hosted Supabase deployments. This guide covers two production approaches using a reverse proxy in front of self-hosted Supabase API gateway, plus a self-signed certificate option for development environment.

## Before you begin[#](#before-you-begin)

You need:

*   A working self-hosted Supabase installation. See [Self-Hosting with Docker](/docs/guides/self-hosting/docker).
*   A domain name with DNS pointing to your server's public IP address (to obtain Let's Encrypt certificate).
*   Ports 80 and 443 open.

## Set up HTTPS[#](#set-up-https)

Below are two options for adding a reverse proxy with automatic HTTPS in front of your self-hosted Supabase: **Caddy** (simpler, zero-config TLS) and **Nginx + Let's Encrypt** (more control over proxy settings). Both sit in front of Kong and terminate TLS, so internal traffic stays on HTTP.

##### Using a different reverse proxy?

If you already run [HAProxy](https://www.haproxy.com/), [Traefik](https://traefik.io/), [Nginx Proxy Manager](https://nginxproxymanager.com/), or another reverse proxy for your infrastructure, you can use it instead of Caddy or Nginx above. The key requirements are:

*   Proxy to Kong on port `8000` (or `<your-ip>:8000` if the proxy runs outside the Docker network)
*   Enable WebSocket support (required for Realtime)
*   Proxy traffic to Storage directly to the container, bypassing Kong
*   Add `X-Forwarded` headers to all requests
*   Comment out Kong's host port bindings in `docker-compose.yml` if the proxy runs in the same Docker network
*   Update `SUPABASE_PUBLIC_URL`, `API_EXTERNAL_URL`, and `SITE_URL` in `.env` to your HTTPS URL

### Step 1: Update environment variables[#](#step-1-update-environment-variables)

Update the URL configuration in your `.env` file to use your HTTPS domain:

```
1SUPABASE_PUBLIC_URL=https://<your-domain>2API_EXTERNAL_URL=https://<your-domain>3SITE_URL=https://<your-domain>
```

Change the following to your domain name and a **valid** email address:

```
1PROXY_DOMAIN=your-domain.example.com2CERTBOT_EMAIL=admin@your-domain.example.com
```

### Step 2: Start the reverse proxy[#](#step-2-start-the-reverse-proxy)

Pick one of the options below and use the corresponding Docker Compose overlay.

[Caddy](https://caddyserver.com/) automatically provisions and renews Let's Encrypt TLS certificates with zero configuration. It also handles HTTP-to-HTTPS redirects, WebSocket upgrades, and HTTP/2 and HTTP/3 out of the box.

Start Caddy by using the pre-configured `docker-compose.caddy.yml` overlay:

```
1docker compose -f docker-compose.yml -f docker-compose.caddy.yml up -d
```

Caddy configuration is in `volumes/proxy/caddy/Caddyfile`.

### Step 3: Verify HTTPS connection[#](#step-3-verify-https-connection)

```
1curl -I https://<your-domain>/auth/v1/
```

You should receive a `401` response confirming you could connect to Auth.

## Self-signed certificates (development only)[#](#self-signed-certificates-development-only)

Self-signed certificates trigger browser warnings and are rejected by most OAuth providers. Use this approach only in development environment or internal networks.

For development or internal networks where you cannot use Let's Encrypt, you can configure Kong to serve HTTPS directly using self-signed certificates.

### Step 1: Generate a self-signed certificate[#](#step-1-generate-a-self-signed-certificate)

Change `<your-domain>` in the example below, and create certificates with `openssl`:

```
1openssl req -x509 -nodes -days 365 -newkey rsa:2048 \2  -keyout volumes/api/server.key \3  -out volumes/api/server.crt \4  -subj "/CN=<your-domain>" && \5  chmod 640 volumes/api/server.key && \6  chgrp 65533 volumes/api/server.key
```

### Step 2: Configure Kong for SSL[#](#step-2-configure-kong-for-ssl)

Comment out Kong's **HTTP** port mapping in `docker-compose.yml`:

```
1kong:2  # ...3  ports:4    #- ${KONG_HTTP_PORT}:8000/tcp
```

Uncomment the certificate volume mounts and SSL environment variables in `docker-compose.yml`:

```
1kong:2  # ... existing configuration ...3  volumes:4    - ./volumes/api/kong.yml:/home/kong/temp.yml:ro,z5    - ./volumes/api/server.crt:/home/kong/server.crt:ro6    - ./volumes/api/server.key:/home/kong/server.key:ro7  environment:8    # ... existing environment variables ...9    KONG_SSL_CERT: /home/kong/server.crt10    KONG_SSL_CERT_KEY: /home/kong/server.key
```

### Step 3: Update configuration variables[#](#step-3-update-configuration-variables)

Edit your `.env` file to use HTTPS with the Kong HTTPS port:

```
1SUPABASE_PUBLIC_URL=https://<your-domain>:84432API_EXTERNAL_URL=https://<your-domain>:84433SITE_URL=https://<your-domain>:8443
```

### Step 4: Restart and verify[#](#step-4-restart-and-verify)

```
1docker compose down && docker compose up -d
```

```
1curl -I -k https://<your-domain>:8443/auth/v1/
```

The `-k` flag tells curl to accept the self-signed certificate.

## Troubleshooting[#](#troubleshooting)

### Certificate not issued[#](#certificate-not-issued)

If Caddy or Certbot fails to obtain a certificate:

*   Verify that ports 80 and 443 are open on your firewall
*   Verify that your domain's DNS A record points to your server's public IP
*   Check proxy logs via `docker logs supabase-caddy` or `docker logs supabase-nginx`
*   Let's Encrypt has [rate limits](https://letsencrypt.org/docs/rate-limits/) - if you hit them, wait before retrying

### WebSocket connection failed[#](#websocket-connection-failed)

If Realtime subscriptions fail to connect:

*   **Caddy** handles WebSocket upgrades automatically - check that Kong is healthy
*   **Nginx** requires explicit `Upgrade` and `Connection` headers on the `/realtime/v1/` location. Verify your `nginx.conf` includes these headers as shown above

### OAuth callback URL mismatch[#](#oauth-callback-url-mismatch)

If OAuth redirects fail with a callback URL error:

*   Verify `API_EXTERNAL_URL` in `.env` is set to your HTTPS URL
*   Verify the callback URL registered with your OAuth provider matches `API_EXTERNAL_URL` followed by `/auth/v1/callback`
*   After changing `API_EXTERNAL_URL`, restart all services with `docker compose down && docker compose up -d`

### Mixed content warnings[#](#mixed-content-warnings)

If the browser console shows mixed content errors:

*   Verify `SUPABASE_PUBLIC_URL` is set to your HTTPS URL
*   Verify `SITE_URL` is also set to HTTPS
*   Clear your browser cache after making changes

### ERR\_CERT\_AUTHORITY\_INVALID[#](#errcertauthorityinvalid)

This is expected when using self-signed certificates. For production, use Caddy or Nginx with Let's Encrypt. If you need to use self-signed certificates, add the certificate to your system's trust store or use a browser flag to bypass the warning.

## Additional resources[#](#additional-resources)

*   [Caddy documentation](https://caddyserver.com/docs/)
*   [Nginx documentation](https://nginx.org/en/docs/) (on nginx.org)
*   [docker-nginx-certbot on GitHub](https://github.com/JonasAlfredsson/docker-nginx-certbot)


