---
title: "SQL to REST API Translator"
source: "https://supabase.com/docs/guides/api/sql-to-rest"
canonical_url: "https://supabase.com/docs/guides/api/sql-to-rest"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:00.974Z"
content_hash: "2eedf98f1fa6d78cb05eeb2a6681c77133a4c39cf151ec9ee18ae0f4a3c5255d"
menu_path: ["Data REST API","Data REST API","Tools","Tools","SQL to REST API Translator","SQL to REST API Translator"]
section_path: ["Data REST API","Data REST API","Tools","Tools","SQL to REST API Translator","SQL to REST API Translator"]
---
# 

SQL to REST API Translator

## 

Translate SQL queries to HTTP requests and Supabase client code

* * *

Sometimes it's challenging to translate SQL queries to the equivalent [PostgREST](https://postgrest.org/) request or Supabase client code. Use this tool to help with this translation.

PostgREST supports a subset of SQL, so not all SQL queries will translate.

Enter SQL to translate

Choose language to translate to

```curl
curl -G http://localhost:54321/rest/v1/books \
  -d "select=title,description" \
  -d "description=ilike.*cheese*" \
  -d "order=title.desc" \
  -d "limit=5" \
  -d "offset=10"
```

### FAQs
