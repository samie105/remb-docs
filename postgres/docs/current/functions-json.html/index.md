---
title: "PostgreSQL: Documentation: 18: 9.16. JSON Functions and Operators"
source: "https://www.postgresql.org/docs/current/functions-json.html"
canonical_url: "https://www.postgresql.org/docs/current/functions-json.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:19.789Z"
content_hash: "b7d09a46d33581f6f91b47274a71493f9d747bc02ec87dfcf25b7c6c04cf7f72"
menu_path: ["PostgreSQL: Documentation: 18: 9.16. JSON Functions and Operators"]
section_path: []
nav_prev: {"path": "postgres/docs/current/xindex.html/index.md", "title": "PostgreSQL: Documentation: 18: 36.16.\u00a0Interfacing Extensions to Indexes"}
nav_next: {"path": "postgres/docs/current/pltcl-global.html/index.md", "title": "PostgreSQL: Documentation: 18: 42.4.\u00a0Global Data in PL/Tcl"}
---

`json_array_elements` ( `json` ) → `setof json`

`jsonb_array_elements` ( `jsonb` ) → `setof jsonb`

Expands the top-level JSON array into a set of JSON values.

`select * from json_array_elements('[1,true, [2,false]]')` →

   value
-----------
 1
 true
 \[2,false\]

`json_array_elements_text` ( `json` ) → `setof text`

`jsonb_array_elements_text` ( `jsonb` ) → `setof text`

Expands the top-level JSON array into a set of `text` values.

`select * from json_array_elements_text('["foo", "bar"]')` →

   value
-----------
 foo
 bar

`json_array_length` ( `json` ) → `integer`

`jsonb_array_length` ( `jsonb` ) → `integer`

Returns the number of elements in the top-level JSON array.

`json_array_length('[1,2,3,{"f1":1,"f2":[5,6]},4]')` → `5`

`jsonb_array_length('[]')` → `0`

`json_each` ( `json` ) → `setof record` ( _`key`_ `text`, _`value`_ `json` )

`jsonb_each` ( `jsonb` ) → `setof record` ( _`key`_ `text`, _`value`_ `jsonb` )

Expands the top-level JSON object into a set of key/value pairs.

`select * from json_each('{"a":"foo", "b":"bar"}')` →

 key | value
-----+-------
 a   | "foo"
 b   | "bar"

`json_each_text` ( `json` ) → `setof record` ( _`key`_ `text`, _`value`_ `text` )

`jsonb_each_text` ( `jsonb` ) → `setof record` ( _`key`_ `text`, _`value`_ `text` )

Expands the top-level JSON object into a set of key/value pairs. The returned _`value`_s will be of type `text`.

`select * from json_each_text('{"a":"foo", "b":"bar"}')` →

 key | value
-----+-------
 a   | foo
 b   | bar

`json_extract_path` ( _`from_json`_ `json`, `VARIADIC` _`path_elems`_ `text[]` ) → `json`

`jsonb_extract_path` ( _`from_json`_ `jsonb`, `VARIADIC` _`path_elems`_ `text[]` ) → `jsonb`

Extracts JSON sub-object at the specified path. (This is functionally equivalent to the `#>` operator, but writing the path out as a variadic list can be more convenient in some cases.)

`json_extract_path('{"f2":{"f3":1},"f4":{"f5":99,"f6":"foo"}}', 'f4', 'f6')` → `"foo"`

`json_extract_path_text` ( _`from_json`_ `json`, `VARIADIC` _`path_elems`_ `text[]` ) → `text`

`jsonb_extract_path_text` ( _`from_json`_ `jsonb`, `VARIADIC` _`path_elems`_ `text[]` ) → `text`

Extracts JSON sub-object at the specified path as `text`. (This is functionally equivalent to the `#>>` operator.)

`json_extract_path_text('{"f2":{"f3":1},"f4":{"f5":99,"f6":"foo"}}', 'f4', 'f6')` → `foo`

`json_object_keys` ( `json` ) → `setof text`

`jsonb_object_keys` ( `jsonb` ) → `setof text`

Returns the set of keys in the top-level JSON object.

`select * from json_object_keys('{"f1":"abc","f2":{"f3":"a", "f4":"b"}}')` →

 json\_object\_keys
------------------
 f1
 f2

`json_populate_record` ( _`base`_ `anyelement`, _`from_json`_ `json` ) → `anyelement`

`jsonb_populate_record` ( _`base`_ `anyelement`, _`from_json`_ `jsonb` ) → `anyelement`

Expands the top-level JSON object to a row having the composite type of the _`base`_ argument. The JSON object is scanned for fields whose names match column names of the output row type, and their values are inserted into those columns of the output. (Fields that do not correspond to any output column name are ignored.) In typical use, the value of _`base`_ is just `NULL`, which means that any output columns that do not match any object field will be filled with nulls. However, if _`base`_ isn't `NULL` then the values it contains will be used for unmatched columns.

To convert a JSON value to the SQL type of an output column, the following rules are applied in sequence:

*   A JSON null value is converted to an SQL null in all cases.
    
*   If the output column is of type `json` or `jsonb`, the JSON value is just reproduced exactly.
    
*   If the output column is a composite (row) type, and the JSON value is a JSON object, the fields of the object are converted to columns of the output row type by recursive application of these rules.
    
*   Likewise, if the output column is an array type and the JSON value is a JSON array, the elements of the JSON array are converted to elements of the output array by recursive application of these rules.
    
*   Otherwise, if the JSON value is a string, the contents of the string are fed to the input conversion function for the column's data type.
    
*   Otherwise, the ordinary text representation of the JSON value is fed to the input conversion function for the column's data type.
    

While the example below uses a constant JSON value, typical use would be to reference a `json` or `jsonb` column laterally from another table in the query's `FROM` clause. Writing `json_populate_record` in the `FROM` clause is good practice, since all of the extracted columns are available for use without duplicate function calls.

`create type subrowtype as (d int, e text);` `create type myrowtype as (a int, b text[], c subrowtype);`

`select * from json_populate_record(null::myrowtype, '{"a": 1, "b": ["2", "a b"], "c": {"d": 4, "e": "a b c"}, "x": "foo"}')` →

 a |   b       |      c
---+-----------+-------------
 1 | {2,"a b"} | (4,"a b c")

`jsonb_populate_record_valid` ( _`base`_ `anyelement`, _`from_json`_ `json` ) → `boolean`

Function for testing `jsonb_populate_record`. Returns `true` if the input `jsonb_populate_record` would finish without an error for the given input JSON object; that is, it's valid input, `false` otherwise.

`create type jsb_char2 as (a char(2));`

`select jsonb_populate_record_valid(NULL::jsb_char2, '{"a": "aaa"}');` →

 jsonb\_populate\_record\_valid
-----------------------------
 f
(1 row)

`select * from jsonb_populate_record(NULL::jsb_char2, '{"a": "aaa"}') q;` →

ERROR:  value too long for type character(2)

`select jsonb_populate_record_valid(NULL::jsb_char2, '{"a": "aa"}');` →

 jsonb\_populate\_record\_valid
-----------------------------
 t
(1 row)

`select * from jsonb_populate_record(NULL::jsb_char2, '{"a": "aa"}') q;` →

 a
----
 aa
(1 row)

`json_populate_recordset` ( _`base`_ `anyelement`, _`from_json`_ `json` ) → `setof anyelement`

`jsonb_populate_recordset` ( _`base`_ `anyelement`, _`from_json`_ `jsonb` ) → `setof anyelement`

Expands the top-level JSON array of objects to a set of rows having the composite type of the _`base`_ argument. Each element of the JSON array is processed as described above for `json[b]_populate_record`.

`create type twoints as (a int, b int);`

`select * from json_populate_recordset(null::twoints, '[{"a":1,"b":2}, {"a":3,"b":4}]')` →

 a | b
---+---
 1 | 2
 3 | 4

`json_to_record` ( `json` ) → `record`

`jsonb_to_record` ( `jsonb` ) → `record`

Expands the top-level JSON object to a row having the composite type defined by an `AS` clause. (As with all functions returning `record`, the calling query must explicitly define the structure of the record with an `AS` clause.) The output record is filled from fields of the JSON object, in the same way as described above for `json[b]_populate_record`. Since there is no input record value, unmatched columns are always filled with nulls.

`create type myrowtype as (a int, b text);`

`select * from json_to_record('{"a":1,"b":[1,2,3],"c":[1,2,3],"e":"bar","r": {"a": 123, "b": "a b c"}}') as x(a int, b text, c int[], d text, r myrowtype)` →

 a |    b    |    c    | d |       r
---+---------+---------+---+---------------
 1 | \[1,2,3\] | {1,2,3} |   | (123,"a b c")

`json_to_recordset` ( `json` ) → `setof record`

`jsonb_to_recordset` ( `jsonb` ) → `setof record`

Expands the top-level JSON array of objects to a set of rows having the composite type defined by an `AS` clause. (As with all functions returning `record`, the calling query must explicitly define the structure of the record with an `AS` clause.) Each element of the JSON array is processed as described above for `json[b]_populate_record`.

`select * from json_to_recordset('[{"a":1,"b":"foo"}, {"a":"2","c":"bar"}]') as x(a int, b text)` →

 a |  b
---+-----
 1 | foo
 2 |

`jsonb_set` ( _`target`_ `jsonb`, _`path`_ `text[]`, _`new_value`_ `jsonb` \[, _`create_if_missing`_ `boolean` \] ) → `jsonb`

Returns _`target`_ with the item designated by _`path`_ replaced by _`new_value`_, or with _`new_value`_ added if _`create_if_missing`_ is true (which is the default) and the item designated by _`path`_ does not exist. All earlier steps in the path must exist, or the _`target`_ is returned unchanged. As with the path oriented operators, negative integers that appear in the _`path`_ count from the end of JSON arrays. If the last path step is an array index that is out of range, and _`create_if_missing`_ is true, the new value is added at the beginning of the array if the index is negative, or at the end of the array if it is positive.

`jsonb_set('[{"f1":1,"f2":null},2,null,3]', '{0,f1}', '[2,3,4]', false)` → `[{"f1": [2, 3, 4], "f2": null}, 2, null, 3]`

`jsonb_set('[{"f1":1,"f2":null},2]', '{0,f3}', '[2,3,4]')` → `[{"f1": 1, "f2": null, "f3": [2, 3, 4]}, 2]`

`jsonb_set_lax` ( _`target`_ `jsonb`, _`path`_ `text[]`, _`new_value`_ `jsonb` \[, _`create_if_missing`_ `boolean` \[, _`null_value_treatment`_ `text` \]\] ) → `jsonb`

If _`new_value`_ is not `NULL`, behaves identically to `jsonb_set`. Otherwise behaves according to the value of _`null_value_treatment`_ which must be one of `'raise_exception'`, `'use_json_null'`, `'delete_key'`, or `'return_target'`. The default is `'use_json_null'`.

`jsonb_set_lax('[{"f1":1,"f2":null},2,null,3]', '{0,f1}', null)` → `[{"f1": null, "f2": null}, 2, null, 3]`

`jsonb_set_lax('[{"f1":99,"f2":null},2]', '{0,f3}', null, true, 'return_target')` → `[{"f1": 99, "f2": null}, 2]`

`jsonb_insert` ( _`target`_ `jsonb`, _`path`_ `text[]`, _`new_value`_ `jsonb` \[, _`insert_after`_ `boolean` \] ) → `jsonb`

Returns _`target`_ with _`new_value`_ inserted. If the item designated by the _`path`_ is an array element, _`new_value`_ will be inserted before that item if _`insert_after`_ is false (which is the default), or after it if _`insert_after`_ is true. If the item designated by the _`path`_ is an object field, _`new_value`_ will be inserted only if the object does not already contain that key. All earlier steps in the path must exist, or the _`target`_ is returned unchanged. As with the path oriented operators, negative integers that appear in the _`path`_ count from the end of JSON arrays. If the last path step is an array index that is out of range, the new value is added at the beginning of the array if the index is negative, or at the end of the array if it is positive.

`jsonb_insert('{"a": [0,1,2]}', '{a, 1}', '"new_value"')` → `{"a": [0, "new_value", 1, 2]}`

`jsonb_insert('{"a": [0,1,2]}', '{a, 1}', '"new_value"', true)` → `{"a": [0, 1, "new_value", 2]}`

`json_strip_nulls` ( _`target`_ `json` \[,_`strip_in_arrays`_ `boolean` \] ) → `json`

`jsonb_strip_nulls` ( _`target`_ `jsonb` \[,_`strip_in_arrays`_ `boolean` \] ) → `jsonb`

Deletes all object fields that have null values from the given JSON value, recursively. If _`strip_in_arrays`_ is true (the default is false), null array elements are also stripped. Otherwise they are not stripped. Bare null values are never stripped.

`json_strip_nulls('[{"f1":1, "f2":null}, 2, null, 3]')` → `[{"f1":1},2,null,3]`

`jsonb_strip_nulls('[1,2,null,3,4]', true)` → `[1,2,3,4]`

`jsonb_path_exists` ( _`target`_ `jsonb`, _`path`_ `jsonpath` \[, _`vars`_ `jsonb` \[, _`silent`_ `boolean` \]\] ) → `boolean`

Checks whether the JSON path returns any item for the specified JSON value. (This is useful only with SQL-standard JSON path expressions, not [predicate check expressions](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-SQLJSON-CHECK-EXPRESSIONS "9.16.2.1.1. Boolean Predicate Check Expressions"), since those always return a value.) If the _`vars`_ argument is specified, it must be a JSON object, and its fields provide named values to be substituted into the `jsonpath` expression. If the _`silent`_ argument is specified and is `true`, the function suppresses the same errors as the `@?` and `@@` operators do.

`jsonb_path_exists('{"a":[1,2,3,4,5]}', '$.a[*] ? (@ >= $min && @ <= $max)', '{"min":2, "max":4}')` → `t`

`jsonb_path_match` ( _`target`_ `jsonb`, _`path`_ `jsonpath` \[, _`vars`_ `jsonb` \[, _`silent`_ `boolean` \]\] ) → `boolean`

Returns the SQL boolean result of a JSON path predicate check for the specified JSON value. (This is useful only with [predicate check expressions](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-SQLJSON-CHECK-EXPRESSIONS "9.16.2.1.1. Boolean Predicate Check Expressions"), not SQL-standard JSON path expressions, since it will either fail or return `NULL` if the path result is not a single boolean value.) The optional _`vars`_ and _`silent`_ arguments act the same as for `jsonb_path_exists`.

`jsonb_path_match('{"a":[1,2,3,4,5]}', 'exists($.a[*] ? (@ >= $min && @ <= $max))', '{"min":2, "max":4}')` → `t`

`jsonb_path_query` ( _`target`_ `jsonb`, _`path`_ `jsonpath` \[, _`vars`_ `jsonb` \[, _`silent`_ `boolean` \]\] ) → `setof jsonb`

Returns all JSON items returned by the JSON path for the specified JSON value. For SQL-standard JSON path expressions it returns the JSON values selected from _`target`_. For [predicate check expressions](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-SQLJSON-CHECK-EXPRESSIONS "9.16.2.1.1. Boolean Predicate Check Expressions") it returns the result of the predicate check: `true`, `false`, or `null`. The optional _`vars`_ and _`silent`_ arguments act the same as for `jsonb_path_exists`.

`select * from jsonb_path_query('{"a":[1,2,3,4,5]}', '$.a[*] ? (@ >= $min && @ <= $max)', '{"min":2, "max":4}')` →

 jsonb\_path\_query
------------------
 2
 3
 4

`jsonb_path_query_array` ( _`target`_ `jsonb`, _`path`_ `jsonpath` \[, _`vars`_ `jsonb` \[, _`silent`_ `boolean` \]\] ) → `jsonb`

Returns all JSON items returned by the JSON path for the specified JSON value, as a JSON array. The parameters are the same as for `jsonb_path_query`.

`jsonb_path_query_array('{"a":[1,2,3,4,5]}', '$.a[*] ? (@ >= $min && @ <= $max)', '{"min":2, "max":4}')` → `[2, 3, 4]`

`jsonb_path_query_first` ( _`target`_ `jsonb`, _`path`_ `jsonpath` \[, _`vars`_ `jsonb` \[, _`silent`_ `boolean` \]\] ) → `jsonb`

Returns the first JSON item returned by the JSON path for the specified JSON value, or `NULL` if there are no results. The parameters are the same as for `jsonb_path_query`.

`jsonb_path_query_first('{"a":[1,2,3,4,5]}', '$.a[*] ? (@ >= $min && @ <= $max)', '{"min":2, "max":4}')` → `2`

`jsonb_path_exists_tz` ( _`target`_ `jsonb`, _`path`_ `jsonpath` \[, _`vars`_ `jsonb` \[, _`silent`_ `boolean` \]\] ) → `boolean`

`jsonb_path_match_tz` ( _`target`_ `jsonb`, _`path`_ `jsonpath` \[, _`vars`_ `jsonb` \[, _`silent`_ `boolean` \]\] ) → `boolean`

`jsonb_path_query_tz` ( _`target`_ `jsonb`, _`path`_ `jsonpath` \[, _`vars`_ `jsonb` \[, _`silent`_ `boolean` \]\] ) → `setof jsonb`

`jsonb_path_query_array_tz` ( _`target`_ `jsonb`, _`path`_ `jsonpath` \[, _`vars`_ `jsonb` \[, _`silent`_ `boolean` \]\] ) → `jsonb`

`jsonb_path_query_first_tz` ( _`target`_ `jsonb`, _`path`_ `jsonpath` \[, _`vars`_ `jsonb` \[, _`silent`_ `boolean` \]\] ) → `jsonb`

These functions act like their counterparts described above without the `_tz` suffix, except that these functions support comparisons of date/time values that require timezone-aware conversions. The example below requires interpretation of the date-only value `2015-08-02` as a timestamp with time zone, so the result depends on the current [TimeZone](postgres/docs/current/runtime-config-client.html/index.md#GUC-TIMEZONE) setting. Due to this dependency, these functions are marked as stable, which means these functions cannot be used in indexes. Their counterparts are immutable, and so can be used in indexes; but they will throw errors if asked to make such comparisons.

`jsonb_path_exists_tz('["2015-08-01 12:00:00-05"]', '$[*] ? (@.datetime() < "2015-08-02".datetime())')` → `t`

`jsonb_pretty` ( `jsonb` ) → `text`

Converts the given JSON value to pretty-printed, indented text.

`jsonb_pretty('[{"f1":1,"f2":null}, 2]')` →

\[
    {
        "f1": 1,
        "f2": null
    },
    2
\]

`json_typeof` ( `json` ) → `text`

`jsonb_typeof` ( `jsonb` ) → `text`

Returns the type of the top-level JSON value as a text string. Possible types are `object`, `array`, `string`, `number`, `boolean`, and `null`. (The `null` result should not be confused with an SQL NULL; see the examples.)

`json_typeof('-123.4')` → `number`

`json_typeof('null'::json)` → `null`

`json_typeof(NULL::json) IS NULL` → `t`


