---
title: "OAuth 2.1 Server"
source: "https://supabase.com/docs/guides/auth/oauth-server"
canonical_url: "https://supabase.com/docs/guides/auth/oauth-server"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:11.111Z"
content_hash: "180aa62f16d5d87e31c96e5d19fa2a9fb0d2bfc25dcf7b5ac287a0ac3b888b13"
menu_path: ["Auth","Auth","OAuth 2.1 Server","OAuth 2.1 Server","Overview","Overview"]
section_path: ["Auth","Auth","OAuth 2.1 Server","OAuth 2.1 Server","Overview","Overview"]
nav_prev: {"path": "supabase/docs/guides/auth/managing-user-data/index.md", "title": "User Management"}
nav_next: {"path": "supabase/docs/guides/auth/password-security/index.md", "title": "Password security"}
---

# 

OAuth 2.1 Server

* * *

Supabase Auth can act as an OAuth 2.1 and OpenID Connect (OIDC) identity provider. This allows other applications and services to use your Supabase project as their authentication provider, just like "Sign in with Google" or "Sign in with GitHub".

You can use this to build "Sign in with \[Your App\]" experiences, authenticate AI agents through the Model Context Protocol (MCP), power developer platforms with third-party integrations, or implement standards-compliant enterprise SSO.

## Use cases[#](#use-cases)

There are several reasons why you might want to enable OAuth 2.1 Server in your Supabase project:

*   **Developer platforms and marketplaces**: Allow third-party developers to build integrations and apps for your platform. Partners can offer "Sign in with \[Your App\]" to their users, with your control over data access through Row Level Security policies.
    
*   **AI agents and automation**: Authenticate AI agents, LLM tools, and MCP servers that need to access user data. The Model Context Protocol provides automatic OAuth discovery and client registration for AI applications.
    
*   **Mobile and desktop apps**: Issue OAuth tokens to your own mobile apps, desktop applications, or other first-party clients. All tokens respect your existing Row Level Security policies and work with Custom Access Token Hooks.
    
*   **Enterprise SSO**: Provide OpenID Connect (OIDC) authentication for enterprise customers who need standards-compliant identity federation across multiple services.
    

## Overview[#](#overview)

Supabase Auth implements the OAuth 2.1 authorization code flow with PKCE (Proof Key for Code Exchange). When a third-party application wants to access user data:

1.  The application redirects the user to your authorization endpoint
2.  Supabase Auth validates the request and redirects to your custom authorization UI
3.  The user authenticates (using any of your enabled auth methods) and approves access
4.  Supabase Auth issues an authorization code
5.  The application exchanges the code for access and refresh tokens
6.  The application uses the access token to make authenticated API requests

Access tokens are standard Supabase JWTs that include `user_id`, `role`, and `client_id` claims. Your existing Row Level Security policies automatically apply to OAuth tokens, giving you fine-grained control over what each client can access.

### Supported standards[#](#supported-standards)

*   **OAuth 2.1**: Latest OAuth specification with mandatory PKCE
*   **OpenID Connect**: ID tokens (with `openid` scope), UserInfo endpoint, and OIDC discovery
*   **Standard scopes**: `openid`, `email`, `profile`, and `phone` scopes for controlling data access
*   **Dynamic client registration**: Automatic registration for MCP-compatible clients
*   **JWKS endpoint**: Public keys for third parties to validate tokens

### Integration with existing auth[#](#integration-with-existing-auth)

OAuth 2.1 Server works seamlessly with your existing Supabase Auth configuration:

*   Users can authenticate using any enabled method (password, magic link, social providers, MFA, phone)
*   [Custom Access Token Hooks](/guides/auth/auth-hooks/access-token-hook) apply to OAuth tokens, allowing you to customize claims like `audience` or add client-specific permissions
*   Row Level Security policies control data access using the `client_id` claim in tokens
*   All standard Supabase features (email templates, hooks, rate limiting) continue to work

## Set up OAuth 2.1 server[#](#set-up-oauth-21-server)

To enable OAuth 2.1 Server in your project, follow these guides:

[

Getting Started

Enable OAuth 2.1, configure your authorization endpoint, and register your first client.

](/docs/guides/auth/oauth-server/getting-started)

[

OAuth Flows

Detailed walkthrough of authorization code and refresh token flows.

](/docs/guides/auth/oauth-server/oauth-flows)

[

MCP Authentication

Authenticate AI agents and LLM tools using Model Context Protocol.

](/docs/guides/auth/oauth-server/mcp-authentication)

[

Token Security & RLS

Control data access with Row Level Security policies for OAuth clients.

](/docs/guides/auth/oauth-server/token-security)

## Resources[#](#resources)

*   [GitHub Discussion](https://github.com/orgs/supabase/discussions/38022) - Share your use cases and help shape the roadmap
*   [Discord Community](https://discord.supabase.com/) - Get help and share what you're building
