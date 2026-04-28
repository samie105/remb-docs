---
title: "Prisma Client & Prisma schema"
source: "https://www.prisma.io/docs/orm/reference/preview-features/client-preview-features"
canonical_url: "https://www.prisma.io/docs/orm/reference/preview-features/client-preview-features"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:43:01.121Z"
content_hash: "ed44971ecb32b9f9a30865d68005a1e8021fdb1190bd86d33c79960e4bd0188f"
menu_path: ["Prisma Client & Prisma schema"]
section_path: []
tab_variants: ["npm","pnpm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/reference/errors/index.md", "title": "Prisma Error Reference"}
nav_next: {"path": "prisma/docs/orm/reference/preview-features/cli-preview-features/index.md", "title": "Prisma CLI Preview features"}
---

Prisma Client and Prisma schema features that are currently in Preview

When we release a new Prisma Client or Prisma schema feature, it often starts in Preview so that you can test it and submit your feedback. After we improve the feature with your feedback and are satisfied with the internal test results, we promote the feature to general availability.

For more information, see [ORM releases and maturity levels](prisma/docs/orm/more/releases/index.md).

The following [Preview](prisma/docs/orm/more/releases/index.md#preview) feature flags are available for Prisma Client and Prisma schema:

To enable a Preview feature, [add the feature flag to the `generator` block](#enabling-a-prisma-client-preview-feature) in your `schema.prisma` file. [Share your feedback on all Preview features on GitHub](https://github.com/prisma/prisma/issues/3108).

To enable a Prisma Client Preview feature:

1.  Add the Preview feature flag to the `generator` block:
    
    ```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
      previewFeatures = ["relationJoins"]
    }
    ```
    
2.  Re-generate Prisma Client:
    
3.  If you are using Visual Studio Code and the Preview feature is not available in your `.ts` file after generating Prisma Client, run the **TypeScript: Restart TS server** command.
    

In the list below, you can find a history of Prisma Client and Prisma schema features that were in Preview and are now in general availability. The features are sorted by the most recent version in which they were promoted to general availability.
