---
title: "Azure Functions ​"
source: "https://hono.dev/docs/getting-started/azure-functions"
canonical_url: "https://hono.dev/docs/getting-started/azure-functions"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:57.000Z"
content_hash: "90508d324eedbf4446c0c0ec95c8d261809f845141b51b399a83c0ea84913cd8"
menu_path: ["Azure Functions ​"]
section_path: []
nav_prev: {"path": "hono/docs/getting-started/lambda-edge/index.md", "title": "Lambda@Edge \u200b"}
nav_next: {"path": "hono/docs/getting-started/google-cloud-run/index.md", "title": "Google Cloud Run \u200b"}
---

[Azure Functions](https://azure.microsoft.com/en-us/products/functions) is a serverless platform from Microsoft Azure. You can run your code in response to events, and it automatically manages the underlying compute resources for you.

Hono was not designed for Azure Functions at first, but with [Azure Functions Adapter](https://github.com/Marplex/hono-azurefunc-adapter), it can run on it as well.

It works with Azure Functions **V4** running on Node.js 18 or above.

## 1\. Install CLI [​](#_1-install-cli)

To create an Azure Function, you must first install [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-typescript?pivots=nodejs-model-v4#install-the-azure-functions-core-tools).

On macOS

sh

```
brew tap azure/functions
brew install azure-functions-core-tools@4
```

Follow this link for other OS:

*   [Install the Azure Functions Core Tools | Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-typescript?pivots=nodejs-model-v4#install-the-azure-functions-core-tools)

## 2\. Setup [​](#_2-setup)

Create a TypeScript Node.js V4 project in the current folder.

sh

```
func init --typescript
```

Change the default route prefix of the host. Add this property to the root json object of `host.json`:

json

```
"extensions": {
    "http": {
        "routePrefix": ""
    }
}
```

INFO

The default Azure Functions route prefix is `/api`. If you don't change it as shown above, be sure to start all your Hono routes with `/api`

Now you are ready to install Hono and the Azure Functions Adapter with:

npmyarnpnpmbun

sh

```
npm i @marplex/hono-azurefunc-adapter hono
```

sh

```
yarn add @marplex/hono-azurefunc-adapter hono
```

sh

```
pnpm add @marplex/hono-azurefunc-adapter hono
```

sh

```
bun add @marplex/hono-azurefunc-adapter hono
```

## 3\. Hello World [​](#_3-hello-world)

Create `src/app.ts`:

ts

```
// src/app.ts
import { Hono } from 'hono'
const app = new Hono()

app.get('/', (c) => c.text('Hello Azure Functions!'))

export default app
```

Create `src/functions/httpTrigger.ts`:

ts

```
// src/functions/httpTrigger.ts
import { app } from '@azure/functions'
import { azureHonoHandler } from '@marplex/hono-azurefunc-adapter'
import honoApp from '../app'

app.http('httpTrigger', {
  methods: [
    //Add all your supported HTTP methods here
    'GET',
    'POST',
    'DELETE',
    'PUT',
  ],
  authLevel: 'anonymous',
  route: '{*proxy}',
  handler: azureHonoHandler(honoApp.fetch),
})
```

## 4\. Run [​](#_4-run)

Run the development server locally. Then, access `http://localhost:7071` in your Web browser.

npmyarnpnpmbun

sh

```
npm run start
```

sh

```
yarn start
```

sh

```
pnpm start
```

sh

```
bun run start
```

## 5\. Deploy [​](#_5-deploy)

Build the project for deployment:

npmyarnpnpmbun

sh

```
npm run build
```

sh

```
yarn build
```

sh

```
pnpm build
```

sh

```
bun run build
```

Deploy your project to the function app in Azure Cloud. Replace `<YourFunctionAppName>` with the name of your app.

sh

```
func azure functionapp publish <YourFunctionAppName>
```

