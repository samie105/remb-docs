---
title: "Environments"
source: "https://developer.flutterwave.com/docs/environments#"
canonical_url: "https://developer.flutterwave.com/docs/environments"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:32:30.551Z"
content_hash: "dcef13a497157d2585f6af2d0d1f1c39877b47828dd4b1c53db856838c225387"
menu_path: ["Environments"]
section_path: []
content_language: "de"
nav_prev: {"path": "flutterwave/docs/integration-journey/index.md", "title": "Integration Journey"}
nav_next: {"path": "flutterwave/docs/authentication/index.md", "title": "Authentication"}
---

> ## 📘
> 
> v4 APIs support two environments: Test mode (sandbox) and Production (live).

In our test environment, all data is mocked, and transactions are stored separately from those in production. No transaction processing actually occurs, so that you can test with real user data during your integration.

> ## 🚧
> 
> Data Retention Limit
> 
> We archive your test data after 30 days. Once test data is archived, it can't be accessed again.

To make requests in the test environment, set.`https://developersandbox-api.flutterwave.com` as your base URL for your requests.

```curl
curl --location 'https://developersandbox-api.flutterwave.com/customers?page=1' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--header 'Content-Type: application/json'
```

  

1.  Log in to your [developer account](https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/auth?client_id=2e5450b8-ee6a-4e5d-b6db-cd9240b5bba3&redirect_uri=https%3A%2F%2Fdevelopersandbox.flutterwave.com%2Fexchange&response_type=code&scope=openid) to access your test credentials.
2.  Copy your API credentials from the main dashboard.

![](https://files.readme.io/47db2b3e9378a4d28aa2ffb04fa83ccb48e6aac4258745c0ec0dad41dcc1df27-test-mode-auth.png)

To connect to our production environment, use `https://f4bexperience.flutterwave.com/` as the base URL.

```curl
curl --location 'https://f4bexperience.flutterwave.com/customers?page=1' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--header 'Content-Type: application/json'
```

  

1.  Log in to your Flutterwave account and navigate to `settings`.
2.  Select the `API Keys` option from your settings.
3.  Depending on whether you are on v3 or v4, perform one of the following
    1.  If you are on v3, i.e. the visible fields are `Public Key`, `Private Key` and `Encryption Key`, click the `Switch to v4 live API keys` to see v4 API credentials.
    2.  If you are on v4, no action is required at this stage.
4.  Copy your API credentials.

Switching between environments is an efficient way to handle your integration. There are several ways to manage your API requests in different environments, but you can use this example as a guide to handle your multi-environment setup:

```javascript
// config.js:
const isProd = process.env.NODE_ENV === 'production';

export const FLW_BASE_URL = isProd
  ? 'https://developersandbox-api.flutterwave.com'
  : 'https://f4bexperience.flutterwave.com'; 

export const FLW_CLIENT_ID = isProd
  ? process.env.FLW_PROD_CLIENT_ID
  : process.env.FLW_SANDBOX_CLIENT_ID;

export const FLW_CLIENT_SECRET = isProd
  ? process.env.FLW_PROD_SECRET_KEY
  : process.env.FLW_SANDBOX_SECRET_KEY;
 
// tokenManager.ts:
import { 
  FLW_CLIENT_ID, 
  FLW_CLIENT_SECRET } from './config';

// (TokenManager class definition...)
class TokenManager {
  ...
  async refreshToken() {
    const response = await fetch('https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: new URLSearchParams({
        'client_id': FLW_CLIENT_ID,
        'client_secret': FLW_CLIENT_SECRET,
        'grant_type': 'client_credentials'
      })
    });
    
    const data = await response.json();
    
    if (data.access_token) {
      this.token = data.access_token;
      // Set expiration time
      this.expiresAt = Date.now() + (data.expires_in * 1000); 
  }
}

// Example usage:
import { FLW_BASE_URL } from './config';
import { tokenManager } from './tokenManager'; 

async function getCustomers() {
  const accessToken = await tokenManager.getToken(); 

  const response = await fetch(`${FLW_BASE_URL}/customers`, {
    headers: {
      'Authorization': `Bearer ${accessToken}`
    }
  });
  
  return response.json();
}
```

Updated 5 months ago

* * *
