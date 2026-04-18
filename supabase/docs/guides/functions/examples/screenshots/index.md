---
title: "Taking Screenshots with Puppeteer"
source: "https://supabase.com/docs/guides/functions/examples/screenshots"
canonical_url: "https://supabase.com/docs/guides/functions/examples/screenshots"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:43.971Z"
content_hash: "3d1fe34562cce65010910ea0d3d7b71fb021d5efc79dbbc8b5c5caf215f45db1"
menu_path: ["Edge Functions","Edge Functions","Examples","Examples","Taking Screenshots with Puppeteer","Taking Screenshots with Puppeteer"]
section_path: ["Edge Functions","Edge Functions","Examples","Examples","Taking Screenshots with Puppeteer","Taking Screenshots with Puppeteer"]
---
# 

Taking Screenshots with Puppeteer

* * *

[Puppeteer](https://pptr.dev/) is a handy tool to programmatically take screenshots and generate PDFs. However, trying to do so in Edge Functions can be challenging due to the size restrictions. Luckily there is a [serverless browser offering available](https://www.browserless.io/) that we can connect to via WebSockets.

Find the code on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/puppeteer).
