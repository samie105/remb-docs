---
title: "PostgreSQL: Documentation: 18: 9.19. Array Functions and Operators"
source: "https://www.postgresql.org/docs/current/functions-array.html"
canonical_url: "https://www.postgresql.org/docs/current/functions-array.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:32.019Z"
content_hash: "7a8b4a7f7e50f1a2515b94a1150d443984afbe8384d43164c551922746ec4cc8"
menu_path: ["PostgreSQL: Documentation: 18: 9.19. Array Functions and Operators"]
section_path: []
nav_prev: {"path": "postgres/docs/current/view-pg-locks.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.13.\u00a0pg_locks"}
nav_next: {"path": "postgres/docs/current/infoschema-routine-privileges.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.41.\u00a0routine_privileges"}
---

Function

Description

Example(s)

`array_append` ( `anycompatiblearray`, `anycompatible` ) → `anycompatiblearray`

Appends an element to the end of an array (same as the `anycompatiblearray` `||` `anycompatible` operator).

`array_append(ARRAY[1,2], 3)` → `{1,2,3}`

`array_cat` ( `anycompatiblearray`, `anycompatiblearray` ) → `anycompatiblearray`

Concatenates two arrays (same as the `anycompatiblearray` `||` `anycompatiblearray` operator).

`array_cat(ARRAY[1,2,3], ARRAY[4,5])` → `{1,2,3,4,5}`

`array_dims` ( `anyarray` ) → `text`

Returns a text representation of the array's dimensions.

`array_dims(ARRAY[[1,2,3], [4,5,6]])` → `[1:2][1:3]`

`array_fill` ( `anyelement`, `integer[]` \[, `integer[]` \] ) → `anyarray`

Returns an array filled with copies of the given value, having dimensions of the lengths specified by the second argument. The optional third argument supplies lower-bound values for each dimension (which default to all `1`).

`array_fill(11, ARRAY[2,3])` → `{{11,11,11},{11,11,11}}`

`array_fill(7, ARRAY[3], ARRAY[2])` → `[2:4]={7,7,7}`

`array_length` ( `anyarray`, `integer` ) → `integer`

Returns the length of the requested array dimension. (Produces NULL instead of 0 for empty or missing array dimensions.)

`array_length(array[1,2,3], 1)` → `3`

`array_length(array[]::int[], 1)` → `NULL`

`array_length(array['text'], 2)` → `NULL`

`array_lower` ( `anyarray`, `integer` ) → `integer`

Returns the lower bound of the requested array dimension.

`array_lower('[0:2]={1,2,3}'::integer[], 1)` → `0`

`array_ndims` ( `anyarray` ) → `integer`

Returns the number of dimensions of the array.

`array_ndims(ARRAY[[1,2,3], [4,5,6]])` → `2`

`array_position` ( `anycompatiblearray`, `anycompatible` \[, `integer` \] ) → `integer`

Returns the subscript of the first occurrence of the second argument in the array, or `NULL` if it's not present. If the third argument is given, the search begins at that subscript. The array must be one-dimensional. Comparisons are done using `IS NOT DISTINCT FROM` semantics, so it is possible to search for `NULL`.

`array_position(ARRAY['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'], 'mon')` → `2`

`array_positions` ( `anycompatiblearray`, `anycompatible` ) → `integer[]`

Returns an array of the subscripts of all occurrences of the second argument in the array given as first argument. The array must be one-dimensional. Comparisons are done using `IS NOT DISTINCT FROM` semantics, so it is possible to search for `NULL`. `NULL` is returned only if the array is `NULL`; if the value is not found in the array, an empty array is returned.

`array_positions(ARRAY['A','A','B','A'], 'A')` → `{1,2,4}`

`array_prepend` ( `anycompatible`, `anycompatiblearray` ) → `anycompatiblearray`

Prepends an element to the beginning of an array (same as the `anycompatible` `||` `anycompatiblearray` operator).

`array_prepend(1, ARRAY[2,3])` → `{1,2,3}`

`array_remove` ( `anycompatiblearray`, `anycompatible` ) → `anycompatiblearray`

Removes all elements equal to the given value from the array. The array must be one-dimensional. Comparisons are done using `IS NOT DISTINCT FROM` semantics, so it is possible to remove `NULL`s.

`array_remove(ARRAY[1,2,3,2], 2)` → `{1,3}`

`array_replace` ( `anycompatiblearray`, `anycompatible`, `anycompatible` ) → `anycompatiblearray`

Replaces each array element equal to the second argument with the third argument.

`array_replace(ARRAY[1,2,5,4], 5, 3)` → `{1,2,3,4}`

`array_reverse` ( `anyarray` ) → `anyarray`

Reverses the first dimension of the array.

`array_reverse(ARRAY[[1,2],[3,4],[5,6]])` → `{{5,6},{3,4},{1,2}}`

`array_sample` ( _`array`_ `anyarray`, _`n`_ `integer` ) → `anyarray`

Returns an array of _`n`_ items randomly selected from _`array`_. _`n`_ may not exceed the length of _`array`_'s first dimension. If _`array`_ is multi-dimensional, an “item” is a slice having a given first subscript.

`array_sample(ARRAY[1,2,3,4,5,6], 3)` → `{2,6,1}`

`array_sample(ARRAY[[1,2],[3,4],[5,6]], 2)` → `{{5,6},{1,2}}`

`array_shuffle` ( `anyarray` ) → `anyarray`

Randomly shuffles the first dimension of the array.

`array_shuffle(ARRAY[[1,2],[3,4],[5,6]])` → `{{5,6},{1,2},{3,4}}`

`array_sort` ( _`array`_ `anyarray` \[, _`descending`_ `boolean` \[, _`nulls_first`_ `boolean` \]\] ) → `anyarray`

Sorts the first dimension of the array. The sort order is determined by the default sort ordering of the array's element type; however, if the element type is collatable, the collation to use can be specified by adding a `COLLATE` clause to the _`array`_ argument.

If _`descending`_ is true then sort in descending order, otherwise ascending order. If omitted, the default is ascending order. If _`nulls_first`_ is true then nulls appear before non-null values, otherwise nulls appear after non-null values. If omitted, _`nulls_first`_ is taken to have the same value as _`descending`_.

`array_sort(ARRAY[[2,4],[2,1],[6,5]])` → `{{2,1},{2,4},{6,5}}`

`array_to_string` ( _`array`_ `anyarray`, _`delimiter`_ `text` \[, _`null_string`_ `text` \] ) → `text`

Converts each array element to its text representation, and concatenates those separated by the _`delimiter`_ string. If _`null_string`_ is given and is not `NULL`, then `NULL` array entries are represented by that string; otherwise, they are omitted. See also [`string_to_array`](postgres/docs/current/functions-string.html/index.md#FUNCTION-STRING-TO-ARRAY).

`array_to_string(ARRAY[1, 2, 3, NULL, 5], ',', '*')` → `1,2,3,*,5`

`array_upper` ( `anyarray`, `integer` ) → `integer`

Returns the upper bound of the requested array dimension.

`array_upper(ARRAY[1,8,3,7], 1)` → `4`

`cardinality` ( `anyarray` ) → `integer`

Returns the total number of elements in the array, or 0 if the array is empty.

`cardinality(ARRAY[[1,2],[3,4]])` → `4`

`trim_array` ( _`array`_ `anyarray`, _`n`_ `integer` ) → `anyarray`

Trims an array by removing the last _`n`_ elements. If the array is multidimensional, only the first dimension is trimmed.

`trim_array(ARRAY[1,2,3,4,5,6], 2)` → `{1,2,3,4}`

`unnest` ( `anyarray` ) → `setof anyelement`

Expands an array into a set of rows. The array's elements are read out in storage order.

`unnest(ARRAY[1,2])` →

 1
 2

`unnest(ARRAY[['foo','bar'],['baz','quux']])` →

 foo
 bar
 baz
 quux

`unnest` ( `anyarray`, `anyarray` \[, ... \] ) → `setof anyelement, anyelement [, ... ]`

Expands multiple arrays (possibly of different data types) into a set of rows. If the arrays are not all the same length then the shorter ones are padded with `NULL`s. This form is only allowed in a query's FROM clause; see [Section 7.2.1.4](https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-TABLEFUNCTIONS "7.2.1.4. Table Functions").

`select * from unnest(ARRAY[1,2], ARRAY['foo','bar','baz']) as x(a,b)` →

 a |  b
---+-----
 1 | foo
 2 | bar
   | baz


