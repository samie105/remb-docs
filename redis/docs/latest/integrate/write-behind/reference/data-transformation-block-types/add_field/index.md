---
title: "add_field"
source: "https://redis.io/docs/latest/integrate/write-behind/reference/data-transformation-block-types/add_field/"
canonical_url: "https://redis.io/docs/latest/integrate/write-behind/reference/data-transformation-block-types/add_field/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:15:41.443Z"
content_hash: "b102d9a0d6b12a18e40e4477e52541692f508e451d4fb8a60518415575ebe332"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Write-behind (preview)","→","Write-behind (preview)","→\n      \n        Write-behind reference","→","Write-behind reference","→\n      \n        Data transformation block types","→","Data transformation block types","→\n      \n        add_field","→","add_field"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Write-behind (preview)","→","Write-behind (preview)","→\n      \n        Write-behind reference","→","Write-behind reference","→\n      \n        Data transformation block types","→","Data transformation block types","→\n      \n        add_field","→","add_field"]
nav_prev: {"path": "redis/docs/latest/integrate/redis-data-integration/reference/data-transformation/add_field/index.md", "title": "add_field"}
nav_next: {"path": "redis/docs/latest/develop/ai/search-and-query/query/aggregation/index.md", "title": "Aggregation queries"}
---

# add\_field

Add fields to a record

Add fields to a record

**Option 1 (alternative):** Add multiple fields

**Properties**

Name

Type

Description

Required

[**fields**](#option1fields)

`object[]`

Fields  

yes

**Additional Properties:** not allowed

**Example**

```yaml
source:
  server_name: redislabs
  schema: dbo
  table: emp
transform:
  - uses: add_field
    with:
      fields:
        - field: name.full_name
          language: jmespath
          expression: concat([name.fname, ' ', name.lname])
        - field: name.fname_upper
          language: jmespath
          expression: upper(name.fname)
```

**Option 2 (alternative):** Add one field

**Properties**

Name

Type

Description

Required

**field**

`string`

Field  

yes

**expression**

`string`

Expression  

yes

**language**

`string`

Language  
Enum: `"jmespath"`, `"sql"`  

yes

**Additional Properties:** not allowed

**Example**

```yaml
source:
  server_name: redislabs
  schema: dbo
  table: emp
transform:
  - uses: add_field
    with:
      field: country
      language: sql
      expression: country_code || ' - ' || UPPER(country_name)
```

## Option 1: fields\[\]: array

Fields

**Items**

**Item Properties**

Name

Type

Description

Required

**field**

`string`

Field  

yes

**expression**

`string`

Expression  

yes

**language**

`string`

Language  
Enum: `"jmespath"`, `"sql"`  

yes

**Item Additional Properties:** not allowed

**Example**

```yaml
- {}
```

## On this page

