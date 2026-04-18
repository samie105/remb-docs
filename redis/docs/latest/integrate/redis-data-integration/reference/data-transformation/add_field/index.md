---
title: "add_field"
source: "https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/add_field/"
canonical_url: "https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/add_field/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:15:32.204Z"
content_hash: "957157d3db6a238a09604637b661fbca318c146150bdcc5f13d0903708641486"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        Reference","→","Reference","→\n      \n        Data transformation reference","→","Data transformation reference","→\n      \n        add_field","→","add_field"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        Reference","→","Reference","→\n      \n        Data transformation reference","→","Data transformation reference","→\n      \n        add_field","→","add_field"]
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
