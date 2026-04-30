---
title: "Authentication"
source: "https://developer.flutterwave.com/docs/authentication#"
canonical_url: "https://developer.flutterwave.com/docs/authentication"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:32:34.924Z"
content_hash: "589df348356c109fca9696f2166d8e0e8209b2646fe83d2941f8ef8d771ec024"
menu_path: ["Authentication"]
section_path: []
tab_variants: ["JavaScript","Python","PHP"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/environments/index.md", "title": "Environments"}
nav_next: {"path": "flutterwave/docs/api-headers/index.md", "title": "Supported Request Headers"}
---

# Sample cURL request to the payment gateway's API endpoint
curl -X GET https://{{ENVIRONMENT}}.flutterwave.com/endpoint \
     -H "Authorization: Bearer {{ACCESS_TOKEN}}" \
     -H "Content-Type: application/json"
```

> ## 🚧
> 
> Managing your Access Token
> 
> Your access token grants access to your Flutterwave account. Keep it confidential and store it securely on your server, ideally as an environment variable. Do not commit it to your Git repository or expose it in frontend code.

Tokens expire periodically to help reduce security risks. Each token is valid for **10 minutes** (as indicated by the `expires_in` field), so you should refresh it before it expires to maintain uninterrupted access.

We recommend refreshing the token at least one minute before it expires. Below are example implementations:

#### JavaScript

```javascript
const axios = require('axios');

let accessToken = null;
let expiresIn = 0; // token expiry time in seconds
let lastTokenRefreshTime = 0;

async function refreshToken() {
  try {
    const response = await axios.post(
      'https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token',
      new URLSearchParams({
        client_id: '<CLIENT_ID>',
        client_secret: '<CLIENT_SECRET>',
        grant_type: 'client_credentials'
      }),
      {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      }
    );

    accessToken = response.data.access_token;
    expiresIn = response.data.expires_in;
    lastTokenRefreshTime = Date.now();

    console.log('New Token:', accessToken);
    console.log('Expires in:', expiresIn, 'seconds');
  } catch (error) {
    console.error('Error refreshing token:', error.response ? error.response.data : error.message);
  }
}

async function ensureTokenIsValid() {
  const currentTime = Date.now();
  const timeSinceLastRefresh = (currentTime - lastTokenRefreshTime) / 1000; // convert to seconds
  const timeLeft = expiresIn - timeSinceLastRefresh;

  if (!accessToken || timeLeft < 60) { // refresh if less than 1 minute remains
    console.log('Refreshing token...');
    await refreshToken();
  } else {
    console.log(`Token is still valid for ${Math.floor(timeLeft)} seconds.`);
  }
}

// Example usage: Call `ensureTokenIsValid` before making API requests
setInterval(ensureTokenIsValid, 5000); // check every 5 seconds
```

```python
#using .env variables for client and secret.

class AuthManager:
    def __init__(self):
        self.credentials = []
        self.load_credentials()

    def load_credentials(self):
        while True:
            client_id = os.getenv(f"FLW_CLIENT_ID")
            client_secret = os.getenv(f"FLW_CLIENT_SECRET")
            
            if not client_id or not client_secret:
                break

            self.credentials.append({
                "client_id": client_id,
                "client_key": client_secret,
                "access_token": None,
                "expiry": None
            })

            indx += 1
    
    def get_credentials(self):
        return self.credentials
    
    def generate_access_token(self):
        idx = 0

        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "client_id": self.credentials["client_id"],
            "client_key": self.credentials["client_key"],
            "grant_type": "client_credentials"
        }

        response = requests.post(url='https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token', headers=header, data=data)

        response_json = response.json()
        return response_json
    
    def get_access_token(self):
        idx = 0

        if self.credentials['access_token'] and self.credentials['expiry'] is None:
            self.generate_access_token(self.credentials)
        
        expiry_delta = self.credentials['expiry'] - datetime.now()
        if expiry_delta < timedelta(minutes=1):
            self.generate_access_token(self.credentials)

        return self.credentials['access_token']
```

```php
<?php

declare(strict_types=1);

namespace Flutterwave;

use Exception;
use Flutterwave\Concerns\Configuration\OAuthConfigurationResolver;
use Flutterwave\Exception\FlutterwaveException;
use Flutterwave\ValueObjects\AccessToken;

use function curl_close;

final class ProfileManager
{
    public const TOKEN_EXPIRY_THRESHOLD = 59; //about a minute

    public const TOKEN_URL = 'https://keycloak.dev-flutterwave.com/realms/flutterwave/protocol/openid-connect/token';

    public static int $requestCount = 0;

    private static array $tokens = [];

    private OAuthConfigurationResolver $resolver;

    public function __construct(OAuthConfigurationResolver $resolver)
    {
        $this->resolver = $resolver;
    }

    /**
     * @throws Exception
     */
    public function addAccount($profile): self
    {
        if (empty($profile)) {
            throw new FlutterwaveException('Profile name cannot be empty');
        }

        if (isset(self::$tokens[$profile])) {
            throw new FlutterwaveException('Profile already exists');
        }

        $config = $this->resolver->resolveOAuthConfig(['profile' => $profile]);
        self::$tokens[$profile] = [
            'token' => $this->getToken($config['client_id'], $config['client_secret']),
            'client_id' => $config['client_id'],
        ];

        return $this;
    }

    public function getAccounts(): array
    {
        return array_keys(self::$tokens);
    }

    /**
     * @throws Exception
     */
    public function getAccount($profile): array
    {
        //        $config = $this->resolver->resolveOAuthConfig(['profile' => $profile]);
        return self::$tokens[$profile] ?? [];
    }

    /**
     * @throws Exception
     */
    public function getAccessToken($profile): AccessToken
    {
        if (! isset(self::$tokens[$profile])) {
            if ($profile !== 'default') {
                throw new FlutterwaveException('Credentials related to the '.$profile.' profile not found.');
            }

            throw new FlutterwaveException('Default Credential are not set. set the environment variables `FLW_CLIENT_ID` and `FLW_CLIENT_SECRET` to use the default credentials or pass a profile name to in the sdk constructor to use a different profile.');
        }

        $token = self::$tokens[$profile]['token'];

        if ($token->isAboutToExpire(self::TOKEN_EXPIRY_THRESHOLD)) {
            $config = $this->resolver->resolveOAuthConfig(['profile' => $profile]);
            self::$tokens[$profile]['token'] = $this->getToken($config['client_id'], $config['client_secret']);
        }

        return self::$tokens[$profile]['token'];
    }

    /**
     * @throws Exception
     */
    private function getToken($clientId, $clientSecret): AccessToken
    {
        self::$requestCount++;

        $postFields = http_build_query([
            'grant_type' => 'client_credentials',
            'client_id' => $clientId,
            'client_secret' => $clientSecret,
        ]);

        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, self::TOKEN_URL);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $postFields);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Content-Type: application/x-www-form-urlencoded',
        ]);

        $response = curl_exec($ch);

        if (curl_errno($ch)) {
            throw new FlutterwaveException('Error during OAuth token request: '.curl_error($ch));
        }

        $responseBody = json_decode($response, true);
        curl_close($ch);

        if (isset($responseBody['access_token'])) {
            return new AccessToken($responseBody['access_token'], $responseBody['expires_in']);
        }

        throw new FlutterwaveException('Failed to retrieve access token. Response: '.$response);
    }
}
```

#### Python

```javascript
const axios = require('axios');

let accessToken = null;
let expiresIn = 0; // token expiry time in seconds
let lastTokenRefreshTime = 0;

async function refreshToken() {
  try {
    const response = await axios.post(
      'https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token',
      new URLSearchParams({
        client_id: '<CLIENT_ID>',
        client_secret: '<CLIENT_SECRET>',
        grant_type: 'client_credentials'
      }),
      {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      }
    );

    accessToken = response.data.access_token;
    expiresIn = response.data.expires_in;
    lastTokenRefreshTime = Date.now();

    console.log('New Token:', accessToken);
    console.log('Expires in:', expiresIn, 'seconds');
  } catch (error) {
    console.error('Error refreshing token:', error.response ? error.response.data : error.message);
  }
}

async function ensureTokenIsValid() {
  const currentTime = Date.now();
  const timeSinceLastRefresh = (currentTime - lastTokenRefreshTime) / 1000; // convert to seconds
  const timeLeft = expiresIn - timeSinceLastRefresh;

  if (!accessToken || timeLeft < 60) { // refresh if less than 1 minute remains
    console.log('Refreshing token...');
    await refreshToken();
  } else {
    console.log(`Token is still valid for ${Math.floor(timeLeft)} seconds.`);
  }
}

// Example usage: Call `ensureTokenIsValid` before making API requests
setInterval(ensureTokenIsValid, 5000); // check every 5 seconds
```

```python
#using .env variables for client and secret.

class AuthManager:
    def __init__(self):
        self.credentials = []
        self.load_credentials()

    def load_credentials(self):
        while True:
            client_id = os.getenv(f"FLW_CLIENT_ID")
            client_secret = os.getenv(f"FLW_CLIENT_SECRET")
            
            if not client_id or not client_secret:
                break

            self.credentials.append({
                "client_id": client_id,
                "client_key": client_secret,
                "access_token": None,
                "expiry": None
            })

            indx += 1
    
    def get_credentials(self):
        return self.credentials
    
    def generate_access_token(self):
        idx = 0

        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "client_id": self.credentials["client_id"],
            "client_key": self.credentials["client_key"],
            "grant_type": "client_credentials"
        }

        response = requests.post(url='https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token', headers=header, data=data)

        response_json = response.json()
        return response_json
    
    def get_access_token(self):
        idx = 0

        if self.credentials['access_token'] and self.credentials['expiry'] is None:
            self.generate_access_token(self.credentials)
        
        expiry_delta = self.credentials['expiry'] - datetime.now()
        if expiry_delta < timedelta(minutes=1):
            self.generate_access_token(self.credentials)

        return self.credentials['access_token']
```

```php
<?php

declare(strict_types=1);

namespace Flutterwave;

use Exception;
use Flutterwave\Concerns\Configuration\OAuthConfigurationResolver;
use Flutterwave\Exception\FlutterwaveException;
use Flutterwave\ValueObjects\AccessToken;

use function curl_close;

final class ProfileManager
{
    public const TOKEN_EXPIRY_THRESHOLD = 59; //about a minute

    public const TOKEN_URL = 'https://keycloak.dev-flutterwave.com/realms/flutterwave/protocol/openid-connect/token';

    public static int $requestCount = 0;

    private static array $tokens = [];

    private OAuthConfigurationResolver $resolver;

    public function __construct(OAuthConfigurationResolver $resolver)
    {
        $this->resolver = $resolver;
    }

    /**
     * @throws Exception
     */
    public function addAccount($profile): self
    {
        if (empty($profile)) {
            throw new FlutterwaveException('Profile name cannot be empty');
        }

        if (isset(self::$tokens[$profile])) {
            throw new FlutterwaveException('Profile already exists');
        }

        $config = $this->resolver->resolveOAuthConfig(['profile' => $profile]);
        self::$tokens[$profile] = [
            'token' => $this->getToken($config['client_id'], $config['client_secret']),
            'client_id' => $config['client_id'],
        ];

        return $this;
    }

    public function getAccounts(): array
    {
        return array_keys(self::$tokens);
    }

    /**
     * @throws Exception
     */
    public function getAccount($profile): array
    {
        //        $config = $this->resolver->resolveOAuthConfig(['profile' => $profile]);
        return self::$tokens[$profile] ?? [];
    }

    /**
     * @throws Exception
     */
    public function getAccessToken($profile): AccessToken
    {
        if (! isset(self::$tokens[$profile])) {
            if ($profile !== 'default') {
                throw new FlutterwaveException('Credentials related to the '.$profile.' profile not found.');
            }

            throw new FlutterwaveException('Default Credential are not set. set the environment variables `FLW_CLIENT_ID` and `FLW_CLIENT_SECRET` to use the default credentials or pass a profile name to in the sdk constructor to use a different profile.');
        }

        $token = self::$tokens[$profile]['token'];

        if ($token->isAboutToExpire(self::TOKEN_EXPIRY_THRESHOLD)) {
            $config = $this->resolver->resolveOAuthConfig(['profile' => $profile]);
            self::$tokens[$profile]['token'] = $this->getToken($config['client_id'], $config['client_secret']);
        }

        return self::$tokens[$profile]['token'];
    }

    /**
     * @throws Exception
     */
    private function getToken($clientId, $clientSecret): AccessToken
    {
        self::$requestCount++;

        $postFields = http_build_query([
            'grant_type' => 'client_credentials',
            'client_id' => $clientId,
            'client_secret' => $clientSecret,
        ]);

        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, self::TOKEN_URL);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $postFields);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Content-Type: application/x-www-form-urlencoded',
        ]);

        $response = curl_exec($ch);

        if (curl_errno($ch)) {
            throw new FlutterwaveException('Error during OAuth token request: '.curl_error($ch));
        }

        $responseBody = json_decode($response, true);
        curl_close($ch);

        if (isset($responseBody['access_token'])) {
            return new AccessToken($responseBody['access_token'], $responseBody['expires_in']);
        }

        throw new FlutterwaveException('Failed to retrieve access token. Response: '.$response);
    }
}
```

#### PHP

```javascript
const axios = require('axios');

let accessToken = null;
let expiresIn = 0; // token expiry time in seconds
let lastTokenRefreshTime = 0;

async function refreshToken() {
  try {
    const response = await axios.post(
      'https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token',
      new URLSearchParams({
        client_id: '<CLIENT_ID>',
        client_secret: '<CLIENT_SECRET>',
        grant_type: 'client_credentials'
      }),
      {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      }
    );

    accessToken = response.data.access_token;
    expiresIn = response.data.expires_in;
    lastTokenRefreshTime = Date.now();

    console.log('New Token:', accessToken);
    console.log('Expires in:', expiresIn, 'seconds');
  } catch (error) {
    console.error('Error refreshing token:', error.response ? error.response.data : error.message);
  }
}

async function ensureTokenIsValid() {
  const currentTime = Date.now();
  const timeSinceLastRefresh = (currentTime - lastTokenRefreshTime) / 1000; // convert to seconds
  const timeLeft = expiresIn - timeSinceLastRefresh;

  if (!accessToken || timeLeft < 60) { // refresh if less than 1 minute remains
    console.log('Refreshing token...');
    await refreshToken();
  } else {
    console.log(`Token is still valid for ${Math.floor(timeLeft)} seconds.`);
  }
}

// Example usage: Call `ensureTokenIsValid` before making API requests
setInterval(ensureTokenIsValid, 5000); // check every 5 seconds
```

```python
#using .env variables for client and secret.

class AuthManager:
    def __init__(self):
        self.credentials = []
        self.load_credentials()

    def load_credentials(self):
        while True:
            client_id = os.getenv(f"FLW_CLIENT_ID")
            client_secret = os.getenv(f"FLW_CLIENT_SECRET")
            
            if not client_id or not client_secret:
                break

            self.credentials.append({
                "client_id": client_id,
                "client_key": client_secret,
                "access_token": None,
                "expiry": None
            })

            indx += 1
    
    def get_credentials(self):
        return self.credentials
    
    def generate_access_token(self):
        idx = 0

        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "client_id": self.credentials["client_id"],
            "client_key": self.credentials["client_key"],
            "grant_type": "client_credentials"
        }

        response = requests.post(url='https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token', headers=header, data=data)

        response_json = response.json()
        return response_json
    
    def get_access_token(self):
        idx = 0

        if self.credentials['access_token'] and self.credentials['expiry'] is None:
            self.generate_access_token(self.credentials)
        
        expiry_delta = self.credentials['expiry'] - datetime.now()
        if expiry_delta < timedelta(minutes=1):
            self.generate_access_token(self.credentials)

        return self.credentials['access_token']
```

```php
<?php

declare(strict_types=1);

namespace Flutterwave;

use Exception;
use Flutterwave\Concerns\Configuration\OAuthConfigurationResolver;
use Flutterwave\Exception\FlutterwaveException;
use Flutterwave\ValueObjects\AccessToken;

use function curl_close;

final class ProfileManager
{
    public const TOKEN_EXPIRY_THRESHOLD = 59; //about a minute

    public const TOKEN_URL = 'https://keycloak.dev-flutterwave.com/realms/flutterwave/protocol/openid-connect/token';

    public static int $requestCount = 0;

    private static array $tokens = [];

    private OAuthConfigurationResolver $resolver;

    public function __construct(OAuthConfigurationResolver $resolver)
    {
        $this->resolver = $resolver;
    }

    /**
     * @throws Exception
     */
    public function addAccount($profile): self
    {
        if (empty($profile)) {
            throw new FlutterwaveException('Profile name cannot be empty');
        }

        if (isset(self::$tokens[$profile])) {
            throw new FlutterwaveException('Profile already exists');
        }

        $config = $this->resolver->resolveOAuthConfig(['profile' => $profile]);
        self::$tokens[$profile] = [
            'token' => $this->getToken($config['client_id'], $config['client_secret']),
            'client_id' => $config['client_id'],
        ];

        return $this;
    }

    public function getAccounts(): array
    {
        return array_keys(self::$tokens);
    }

    /**
     * @throws Exception
     */
    public function getAccount($profile): array
    {
        //        $config = $this->resolver->resolveOAuthConfig(['profile' => $profile]);
        return self::$tokens[$profile] ?? [];
    }

    /**
     * @throws Exception
     */
    public function getAccessToken($profile): AccessToken
    {
        if (! isset(self::$tokens[$profile])) {
            if ($profile !== 'default') {
                throw new FlutterwaveException('Credentials related to the '.$profile.' profile not found.');
            }

            throw new FlutterwaveException('Default Credential are not set. set the environment variables `FLW_CLIENT_ID` and `FLW_CLIENT_SECRET` to use the default credentials or pass a profile name to in the sdk constructor to use a different profile.');
        }

        $token = self::$tokens[$profile]['token'];

        if ($token->isAboutToExpire(self::TOKEN_EXPIRY_THRESHOLD)) {
            $config = $this->resolver->resolveOAuthConfig(['profile' => $profile]);
            self::$tokens[$profile]['token'] = $this->getToken($config['client_id'], $config['client_secret']);
        }

        return self::$tokens[$profile]['token'];
    }

    /**
     * @throws Exception
     */
    private function getToken($clientId, $clientSecret): AccessToken
    {
        self::$requestCount++;

        $postFields = http_build_query([
            'grant_type' => 'client_credentials',
            'client_id' => $clientId,
            'client_secret' => $clientSecret,
        ]);

        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, self::TOKEN_URL);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $postFields);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Content-Type: application/x-www-form-urlencoded',
        ]);

        $response = curl_exec($ch);

        if (curl_errno($ch)) {
            throw new FlutterwaveException('Error during OAuth token request: '.curl_error($ch));
        }

        $responseBody = json_decode($response, true);
        curl_close($ch);

        if (isset($responseBody['access_token'])) {
            return new AccessToken($responseBody['access_token'], $responseBody['expires_in']);
        }

        throw new FlutterwaveException('Failed to retrieve access token. Response: '.$response);
    }
}
```

Updated 5 months ago

* * *
