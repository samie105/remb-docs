---
title: "Best Practices"
source: "https://developer.flutterwave.com/docs/best-practices#"
canonical_url: "https://developer.flutterwave.com/docs/best-practices"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:32:52.522Z"
content_hash: "263150f891084a3383723488800512a321c657a04151a084c1028b32dfaa56de"
menu_path: ["Best Practices"]
section_path: []
content_language: "de"
nav_prev: {"path": "flutterwave/docs/testing/index.md", "title": "Testing"}
nav_next: {"path": "flutterwave/docs/introduction-1/index.md", "title": "Introduction"}
---

As a developer or business integrating Flutterwave to receive payments, it's important to follow best practices to maintain reliability, security, and compliance. Here are some key guidelines:

-   Always [verify the payment](https://developer.flutterwave.com/v4.0/reference/charges_get) before giving value. Confirm the `amount`, `currency`, `transaction reference` and customer details.
    
-   Implement webhooks to handle transaction updates reliably.
    
-   When checking transaction status, make sure you're not hitting rate limits.
    

  

-   For USSD and transfer payments, use [webhooks](https://developer.flutterwave.com/v4.0/docs/webhooks) to confirm payment completion.

  

-   Handle edge cases carefully by giving value or rendering service only on definite API responses.
    
-   Catch all errors and show user-friendly, general messages when necessary.
    

  

-   Set a [signature](https://developer.flutterwave.com/v4.0/docs/webhooks) from your dashboard under **Settings > Webhooks** to verify all incoming webhooks.

Verify that your app meets the following requirements for managing your API keys:

-   Never hardcode API credentials in your codebase.
-   Only initiate token-protected API calls from your backend, not from the client (browser or mobile app).
-   Store credentials in environment variables or use a secrets manager.

  

-   Enforce strong password policies (e.g., minimum 8 characters, including uppercase, lowercase, numbers, and symbols).
-   Use input validation during login.
-   Prevent brute-force attacks using rate limits, account lockouts, and two-factor authentication.
-   Store database credentials securely, preferably using a secrets manager.

  

-   Set all app session cookies with `Secure` and `HttpOnly` attributes.
-   On logout, terminate the session on the server and clear client-side session tokens to prevent caching.
-   Store session tokens in cookies and transport them only via HTTP cookie headers.

  

-   Set session timeouts on the server.
-   Limit session duration to a maximum of 10 hours, after which re-authentication is required.
-   Implement idle timeouts.
-   Prevent concurrent sessions.
-   Use a cryptographically secure random number generator for session tokens.

  

-   Provide a clearly accessible logout option to terminate user sessions.
-   Invalidate sessions on the server during logout.
-   Destroy all session tokens on logout to make them unusable.

  

-   Use secure channels (`TLS 1.2` or `TLS 1.3`) for key exchange.
-   Limit storage and transmission of sensitive data. Use abstract identifiers where possible.
-   Encrypt sensitive data at rest.

  

-   Log all privileged changes and administrative/user activities.
-   Log all access to sensitive data.
-   On unhandled exceptions, show a generic message to users. Never expose internal details like database errors or server traces.
-   Store logs securely and follow global log retention standards.

  

-   Validate all inputs on the server side, even if already validated on the client.
-   Encode all outputs.
-   Proper validation and encoding protect your application against stored and reflected cross-site scripting (XSS) in headers, cookies, form fields, query strings, and hidden fields.
-   Use character whitelists for user inputs.
-   Validate uploaded files thoroughly.
-   Use parameterized SQL queries to prevent SQL injection.

  

-   Disable caching for SSL pages and any page with sensitive data. Use `Cache-Control: no-cache` or `no-store` instead of `private`.
-   Keep OS, web server, and app server security patches up to date.
-   Only support TLS 1.2 or higher.
-   Enforce HTTPS across all pages and endpoints.
-   Disable `TRACE` and other unnecessary HTTP methods on your web server.

Your application should be protected against common security risks, including:

-   Cross-Site Request Forgery (CSRF)
-   Reflected and Stored Cross-Site Scripting (XSS)
-   SQL Injection
-   XML Injection

Updated 10 months ago

* * *
