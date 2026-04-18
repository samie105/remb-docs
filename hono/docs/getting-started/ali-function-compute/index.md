---
title: "Alibaba Cloud Function Compute ​"
source: "https://hono.dev/docs/getting-started/ali-function-compute"
canonical_url: "https://hono.dev/docs/getting-started/ali-function-compute"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:52.252Z"
content_hash: "e027e40aa022d3e8f6ea14bef7fdbd53b1e29d55279e2895a3a8c3ecb4c7a17d"
menu_path: ["Alibaba Cloud Function Compute ​"]
section_path: []
nav_prev: {"path": "hono/docs/getting-started/supabase-functions/index.md", "title": "Supabase Edge Functions \u200b"}
nav_next: {"path": "hono/docs/getting-started/webassembly-wasi/index.md", "title": "WebAssembly (w/ WASI) \u200b"}
---

# Please select a provider: Alibaba Cloud (alibaba)
# Input your AccessKeyID & AccessKeySecret
```

Edit `s.yaml`

yaml

```
edition: 3.0.0
name: my-app
access: 'default'

vars:
  region: 'us-west-1'

resources:
  my-app:
    component: fc3
    props:
      region: ${vars.region}
      functionName: 'my-app'
      description: 'Hello World by Hono'
      runtime: 'nodejs20'
      code: ./dist
      handler: index.handler
      memorySize: 1024
      timeout: 300
```

Edit `scripts` section in `package.json`:

json

```
{
  "scripts": {
    "build": "esbuild --bundle --outfile=./dist/index.js --platform=node --target=node20 ./src/index.ts",
    "deploy": "s deploy -y"
  }
}
```

## 4\. Deploy [​](#_4-deploy)

Finally, run the command to deploy:

sh

```
npm run build # Compile the TypeScript code to JavaScript
npm run deploy # Deploy the function to Alibaba Cloud Function Compute
```

