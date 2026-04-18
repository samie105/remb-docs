---
title: "Scheduling Edge Functions"
source: "https://supabase.com/docs/guides/functions/schedule-functions"
canonical_url: "https://supabase.com/docs/guides/functions/schedule-functions"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:31.897Z"
content_hash: "3a74136e7dec30a0358763943a3ca7641240ecb66acff3305085d3babcb254a3"
menu_path: ["Edge Functions","Edge Functions","Examples","Examples","Scheduling Functions","Scheduling Functions"]
section_path: ["Edge Functions","Edge Functions","Examples","Examples","Scheduling Functions","Scheduling Functions"]
nav_prev: {"path": "supabase/docs/guides/functions/secrets/index.md", "title": "Environment Variables"}
nav_next: {"path": "supabase/docs/guides/functions/status-codes/index.md", "title": "Status codes"}
---

# 

Scheduling Edge Functions

* * *

The hosted Supabase Platform supports the [`pg_cron` extension](/docs/guides/database/extensions/pgcron), a recurring job scheduler in Postgres.

In combination with the [`pg_net` extension](/docs/guides/database/extensions/pgnet), this allows us to invoke Edge Functions periodically on a set schedule.

To access the auth token securely for your Edge Function call, we recommend storing them in [Supabase Vault](/docs/guides/database/vault).

## Examples[#](#examples)

### Invoke an Edge Function every minute[#](#invoke-an-edge-function-every-minute)

Store `project_url` and `anon_key` in Supabase Vault:

```
1select vault.create_secret('https://project-ref.supabase.co', 'project_url');2select vault.create_secret('YOUR_SUPABASE_ANON_KEY', 'anon_key');
```

Make a POST request to a Supabase Edge Function every minute:

```
1select2  cron.schedule(3    'invoke-function-every-minute',4    '* * * * *', -- every minute5    $$6    select7      net.http_post(8          url:= (select decrypted_secret from vault.decrypted_secrets where name = 'project_url') || '/functions/v1/function-name',9          headers:=jsonb_build_object(10            'Content-type', 'application/json',11            'Authorization', 'Bearer ' || (select decrypted_secret from vault.decrypted_secrets where name = 'anon_key')12          ),13          body:=concat('{"time": "', now(), '"}')::jsonb14      ) as request_id;15    $$16  );
```

## Resources[#](#resources)

*   [`pg_net` extension](/docs/guides/database/extensions/pgnet)
*   [`pg_cron` extension](/docs/guides/database/extensions/pgcron)
