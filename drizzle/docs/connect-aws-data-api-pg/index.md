---
title: "Drizzle <> AWS Data API Postgres"
source: "https://orm.drizzle.team/docs/connect-aws-data-api-pg"
canonical_url: "https://orm.drizzle.team/docs/connect-aws-data-api-pg"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:26:53.975Z"
content_hash: "15fc848af935bd0b269cd0bdabce2b0a6bdf59077348a2fa7b27178abea77ba5"
menu_path: ["Drizzle <> AWS Data API Postgres"]
section_path: []
content_language: "en"
---
#### Step 1 - Install packages[](#step-1---install-packages)

```
npm i drizzle-orm @aws-sdk/client-rds-data
npm i -D drizzle-kit
```

```
yarn add drizzle-orm @aws-sdk/client-rds-data
yarn add -D drizzle-kit
```

```
pnpm add drizzle-orm @aws-sdk/client-rds-data
pnpm add -D drizzle-kit
```

```
bun add drizzle-orm @aws-sdk/client-rds-data
bun add -D drizzle-kit
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

```typescript
import { drizzle } from 'drizzle-orm/aws-data-api/pg';

// These three properties are required. You can also specify
// any property from the RDSDataClient type inside the connection object.
const db = drizzle({ connection: {
  database: process.env['DATABASE']!,
  secretArn: process.env['SECRET_ARN']!,
  resourceArn: process.env['RESOURCE_ARN']!,
}});

await db.select().from(...);
```

If you need to provide your existing driver:

```typescript
import { drizzle } from 'drizzle-orm/aws-data-api/pg';
import { RDSDataClient } from '@aws-sdk/client-rds-data';

const rdsClient = new RDSDataClient({ region: 'us-east-1' });

const db = drizzle(rdsClient, {
  database: process.env['DATABASE']!,
  secretArn: process.env['SECRET_ARN']!,
  resourceArn: process.env['RESOURCE_ARN']!,
});

await db.select().from(...);
```

#### What’s next?[](#whats-next)
