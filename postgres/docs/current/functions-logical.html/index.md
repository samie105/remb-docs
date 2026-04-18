---
title: "PostgreSQL: Documentation: 18: 9.1. Logical Operators"
source: "https://www.postgresql.org/docs/current/functions-logical.html"
canonical_url: "https://www.postgresql.org/docs/current/functions-logical.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:50.318Z"
content_hash: "03cb86b41d8c8d85ca40f125110a4a34289986a8baabf9bd475f568f27989f83"
menu_path: ["PostgreSQL: Documentation: 18: 9.1. Logical Operators"]
section_path: []
---
The usual logical operators are available:

```
boolean
```

SQL uses a three-valued logic system with true, false, and `null`, which represents “unknown”. Observe the following truth tables:

   

_`a`_

_`b`_

_`a`_ AND _`b`_

_`a`_ OR _`b`_

TRUE

TRUE

TRUE

TRUE

TRUE

FALSE

FALSE

TRUE

TRUE

NULL

NULL

TRUE

FALSE

FALSE

FALSE

FALSE

FALSE

NULL

FALSE

NULL

NULL

NULL

NULL

NULL

 

_`a`_

NOT _`a`_

TRUE

FALSE

FALSE

TRUE

NULL

NULL

The operators `AND` and `OR` are commutative, that is, you can switch the left and right operands without affecting the result. (However, it is not guaranteed that the left operand is evaluated before the right operand. See [Section 4.2.14](https://www.postgresql.org/docs/current/sql-expressions.html#SYNTAX-EXPRESS-EVAL "4.2.14. Expression Evaluation Rules") for more information about the order of evaluation of subexpressions.)
