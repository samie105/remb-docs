---
title: "Guide for migrating from RESP2 to RESP3 replies"
source: "https://redis.io/docs/latest/develop/data-types/json/resp3/"
canonical_url: "https://redis.io/docs/latest/develop/data-types/json/resp3/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:08:45.134Z"
content_hash: "19853cc9315428887a8b598ff0c6535c6355a79e7969f7d4b4e53c94c264018f"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis data types","→","Redis data types","→\n      \n        JSON","→","JSON","→\n      \n        Guide for migrating from RESP2 to RESP3 replies","→","Guide for migrating from RESP2 to RESP3 replies"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis data types","→","Redis data types","→\n      \n        JSON","→","JSON","→\n      \n        Guide for migrating from RESP2 to RESP3 replies","→","Guide for migrating from RESP2 to RESP3 replies"]
nav_prev: {"path": "redis/docs/latest/develop/data-types/json/ram/index.md", "title": "Redis JSON RAM Usage"}
nav_next: {"path": "redis/docs/latest/develop/data-types/json/use_cases/index.md", "title": "Use cases"}
---

# Guide for migrating from RESP2 to RESP3 replies

JSON RESP2 to RESP3 replies reference for client developers

In RESP3, the default value of the optional path argument was changed from `.` to `$`. Due to this change, the replies of some commands have slightly changed. This page provides a brief comparison between RESP2 and RESP3 responses for JSON commands to help developers in migrating their clients from RESP2 to RESP3.

### JSON command replies comparison

The types are described using a ["TypeScript-like" syntax](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html). `Array<a>` denotes an [array](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#arrays) where the type of elements is known, but the number of elements is not.

Command

RESP2

RESP3

All JSON commands

**Default value of optional `path` argument**: `.`

**Default value of optional `path` argument:** `$`

JSON.ARRAPPEND  
JSON.ARRINDEX  
JSON.ARRINSERT  
JSON.ARRLEN  
JSON.ARRTRIM  
JSON.OBJLEN  
JSON.STRAPPEND  
JSON.STRLEN  
JSON.TOGGLE

_`$`\-based path argument:_  
Reply: Array<BulkString | null>  
  
_`.`\-based path argument :_   
Reply: BulkString

_`$`\-based path argument:_   
Reply: Array<number | null>  
  
_`.`\-based path argument :_  
Reply: number

JSON.GET

Reply: JSON encoded string  
Example:  
`> JSON.SET k $ "[1,2,3]"`  
`> JSON.GET k`  
`"[1,2,3]"`

Reply: JSON encoded string with a top-level array  
Example:  
`> JSON.SET k $ "[1,2,3]"`  
`> JSON.GET k`  
`"[[1,2,3]]"`

JSON.NUMINCRBY  
JSON.NUMMULTBY

_`$`\-based path argument:_  
Reply: JSON-encoded BulkString | null  
  
_`.`\-based path argument :_   
Reply: BulkString | null | error

_`$`\-based path argument:_  
Reply: Array<number | null> | error  
  
_`.`\-based path argument :_   
Reply: number | null | error

JSON.OBJKEYS

_`$`\-based path argument:_  
Reply: Array<Array<BulkString>>  
  
_`.`\-based path argument :_   
Reply: Array<BulkString>

_`$`\-based path argument:_  
Reply: Array<Array<BulkString>>  
  
_`.`\-based path argument :_   
Reply: Array<BulkString>

JSON.TYPE

_`$`\-based path argument:_  
Reply: Array<BulkString>  
Example:  
`> JSON.TYPE k $`  
`1) "array"`  
  
_`.`\-based path argument :_   
Reply: BulkString

_`$`\-based path argument:_  
Reply: Array<Array<BulkString>>  
Example:  
`> JSON.TYPE k $`  
`1) 1) "array"`  
  
_`.`\-based path argument :_   
Reply: Array<BulkString>

## On this page
