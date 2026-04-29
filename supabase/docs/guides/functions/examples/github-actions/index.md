---
title: "GitHub Actions"
source: "https://supabase.com/docs/guides/functions/examples/github-actions"
canonical_url: "https://supabase.com/docs/guides/functions/examples/github-actions"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:31.183Z"
content_hash: "c12128e3158e8c4f59022fcf2f41bc4ebd05dcb7d3aee9e55cb295ff9d2229f8"
menu_path: ["GitHub Actions"]
section_path: []
nav_prev: {"path": "supabase/docs/guides/functions/examples/elevenlabs-transcribe-speech/index.md", "title": "Transcription Telegram Bot"}
nav_next: {"path": "supabase/docs/guides/functions/examples/image-manipulation/index.md", "title": "Image Manipulation"}
---

# 

GitHub Actions

* * *

Use the Supabase CLI together with GitHub Actions to automatically deploy our Supabase Edge Functions. [View on GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/github-action-deploy).

```
1name: Deploy Function23on:4  push:5    branches:6      - main7  workflow_dispatch:89jobs:10  deploy:11    runs-on: ubuntu-latest1213    env:14      SUPABASE_ACCESS_TOKEN: YOUR_SUPABASE_ACCESS_TOKEN15      PROJECT_ID: YOUR_SUPABASE_PROJECT_ID1617    steps:18      - uses: actions/checkout@v41920      - uses: supabase/setup-cli@v121        with:22          version: latest2324      - run: supabase functions deploy --project-ref $PROJECT_ID
```

Since Supabase CLI [v1.62.0](https://github.com/supabase/cli/releases/tag/v1.62.0) you can deploy all functions with a single command.

Individual function configuration like [JWT verification](/docs/guides/cli/config#functions.function_name.verify_jwt) and [import map location](/docs/guides/cli/config#functions.function_name.import_map) can be set via the `config.toml` file.

```
1[functions.hello-world]2verify_jwt = false
```
