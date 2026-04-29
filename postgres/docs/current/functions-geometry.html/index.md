---
title: "PostgreSQL: Documentation: 18: 9.11. Geometric Functions and Operators"
source: "https://www.postgresql.org/docs/current/functions-geometry.html"
canonical_url: "https://www.postgresql.org/docs/current/functions-geometry.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:42.089Z"
content_hash: "4740944457f2b650aa78cde192d3115e5e89243ebec90435cded6cd85a65c592"
menu_path: ["PostgreSQL: Documentation: 18: 9.11. Geometric Functions and Operators"]
section_path: []
nav_prev: {"path": "../functions-bitstring.html/index.md", "title": "PostgreSQL: Documentation: 18: 9.6.\u00a0Bit String Functions and Operators"}
nav_next: {"path": "../functions-info.html/index.md", "title": "PostgreSQL: Documentation: 18: 9.27.\u00a0System Information Functions and Operators"}
---

_`geometric_type`_ `+` `point` → ``_`geometric_type`_``

Adds the coordinates of the second `point` to those of each point of the first argument, thus performing translation. Available for `point`, `box`, `path`, `circle`.

`box '(1,1),(0,0)' + point '(2,0)'` → `(3,1),(2,0)`

`path` `+` `path` → `path`

Concatenates two open paths (returns NULL if either path is closed).

`path '[(0,0),(1,1)]' + path '[(2,2),(3,3),(4,4)]'` → `[(0,0),(1,1),(2,2),(3,3),(4,4)]`

_`geometric_type`_ `-` `point` → ``_`geometric_type`_``

Subtracts the coordinates of the second `point` from those of each point of the first argument, thus performing translation. Available for `point`, `box`, `path`, `circle`.

`box '(1,1),(0,0)' - point '(2,0)'` → `(-1,1),(-2,0)`

_`geometric_type`_ `*` `point` → ``_`geometric_type`_``

Multiplies each point of the first argument by the second `point` (treating a point as being a complex number represented by real and imaginary parts, and performing standard complex multiplication). If one interprets the second `point` as a vector, this is equivalent to scaling the object's size and distance from the origin by the length of the vector, and rotating it counterclockwise around the origin by the vector's angle from the _`x`_ axis. Available for `point`, `box`,[\[a\]](#ftn.FUNCTIONS-GEOMETRY-ROTATION-FN) `path`, `circle`.

`path '((0,0),(1,0),(1,1))' * point '(3.0,0)'` → `((0,0),(3,0),(3,3))`

`path '((0,0),(1,0),(1,1))' * point(cosd(45), sind(45))` → `((0,0),​(0.7071067811865475,0.7071067811865475),​(0,1.414213562373095))`

_`geometric_type`_ `/` `point` → ``_`geometric_type`_``

Divides each point of the first argument by the second `point` (treating a point as being a complex number represented by real and imaginary parts, and performing standard complex division). If one interprets the second `point` as a vector, this is equivalent to scaling the object's size and distance from the origin down by the length of the vector, and rotating it clockwise around the origin by the vector's angle from the _`x`_ axis. Available for `point`, `box`,[\[a\]](https://www.postgresql.org/docs/current/functions-geometry.html#ftn.FUNCTIONS-GEOMETRY-ROTATION-FN) `path`, `circle`.

`path '((0,0),(1,0),(1,1))' / point '(2.0,0)'` → `((0,0),(0.5,0),(0.5,0.5))`

`path '((0,0),(1,0),(1,1))' / point(cosd(45), sind(45))` → `((0,0),​(0.7071067811865476,-0.7071067811865476),​(1.4142135623730951,0))`

`@-@` _`geometric_type`_ → `double precision`

Computes the total length. Available for `lseg`, `path`.

`@-@ path '[(0,0),(1,0),(1,1)]'` → `2`

`@@` _`geometric_type`_ → `point`

Computes the center point. Available for `box`, `lseg`, `polygon`, `circle`.

`@@ box '(2,2),(0,0)'` → `(1,1)`

`#` _`geometric_type`_ → `integer`

Returns the number of points. Available for `path`, `polygon`.

`# path '((1,0),(0,1),(-1,0))'` → `3`

_`geometric_type`_ `#` _`geometric_type`_ → `point`

Computes the point of intersection, or NULL if there is none. Available for `lseg`, `line`.

`lseg '[(0,0),(1,1)]' # lseg '[(1,0),(0,1)]'` → `(0.5,0.5)`

`box` `#` `box` → `box`

Computes the intersection of two boxes, or NULL if there is none.

`box '(2,2),(-1,-1)' # box '(1,1),(-2,-2)'` → `(1,1),(-1,-1)`

_`geometric_type`_ `##` _`geometric_type`_ → `point`

Computes the closest point to the first object on the second object. Available for these pairs of types: (`point`, `box`), (`point`, `lseg`), (`point`, `line`), (`lseg`, `box`), (`lseg`, `lseg`), (`line`, `lseg`).

`point '(0,0)' ## lseg '[(2,0),(0,2)]'` → `(1,1)`

_`geometric_type`_ `<->` _`geometric_type`_ → `double precision`

Computes the distance between the objects. Available for all seven geometric types, for all combinations of `point` with another geometric type, and for these additional pairs of types: (`box`, `lseg`), (`lseg`, `line`), (`polygon`, `circle`) (and the commutator cases).

`circle '<(0,0),1>' <-> circle '<(5,0),1>'` → `3`

_`geometric_type`_ `@>` _`geometric_type`_ → `boolean`

Does first object contain second? Available for these pairs of types: (`box`, `point`), (`box`, `box`), (`path`, `point`), (`polygon`, `point`), (`polygon`, `polygon`), (`circle`, `point`), (`circle`, `circle`).

`circle '<(0,0),2>' @> point '(1,1)'` → `t`

_`geometric_type`_ `<@` _`geometric_type`_ → `boolean`

Is first object contained in or on second? Available for these pairs of types: (`point`, `box`), (`point`, `lseg`), (`point`, `line`), (`point`, `path`), (`point`, `polygon`), (`point`, `circle`), (`box`, `box`), (`lseg`, `box`), (`lseg`, `line`), (`polygon`, `polygon`), (`circle`, `circle`).

`point '(1,1)' <@ circle '<(0,0),2>'` → `t`

_`geometric_type`_ `&&` _`geometric_type`_ → `boolean`

Do these objects overlap? (One point in common makes this true.) Available for `box`, `polygon`, `circle`.

`box '(1,1),(0,0)' && box '(2,2),(0,0)'` → `t`

_`geometric_type`_ `<<` _`geometric_type`_ → `boolean`

Is first object strictly left of second? Available for `point`, `box`, `polygon`, `circle`.

`circle '<(0,0),1>' << circle '<(5,0),1>'` → `t`

_`geometric_type`_ `>>` _`geometric_type`_ → `boolean`

Is first object strictly right of second? Available for `point`, `box`, `polygon`, `circle`.

`circle '<(5,0),1>' >> circle '<(0,0),1>'` → `t`

_`geometric_type`_ `&<` _`geometric_type`_ → `boolean`

Does first object not extend to the right of second? Available for `box`, `polygon`, `circle`.

`box '(1,1),(0,0)' &< box '(2,2),(0,0)'` → `t`

_`geometric_type`_ `&>` _`geometric_type`_ → `boolean`

Does first object not extend to the left of second? Available for `box`, `polygon`, `circle`.

`box '(3,3),(0,0)' &> box '(2,2),(0,0)'` → `t`

_`geometric_type`_ `<<|` _`geometric_type`_ → `boolean`

Is first object strictly below second? Available for `point`, `box`, `polygon`, `circle`.

`box '(3,3),(0,0)' <<| box '(5,5),(3,4)'` → `t`

_`geometric_type`_ `|>>` _`geometric_type`_ → `boolean`

Is first object strictly above second? Available for `point`, `box`, `polygon`, `circle`.

`box '(5,5),(3,4)' |>> box '(3,3),(0,0)'` → `t`

_`geometric_type`_ `&<|` _`geometric_type`_ → `boolean`

Does first object not extend above second? Available for `box`, `polygon`, `circle`.

`box '(1,1),(0,0)' &<| box '(2,2),(0,0)'` → `t`

_`geometric_type`_ `|&>` _`geometric_type`_ → `boolean`

Does first object not extend below second? Available for `box`, `polygon`, `circle`.

`box '(3,3),(0,0)' |&> box '(2,2),(0,0)'` → `t`

`box` `<^` `box` → `boolean`

Is first object below second (allows edges to touch)?

`box '((1,1),(0,0))' <^ box '((2,2),(1,1))'` → `t`

`box` `>^` `box` → `boolean`

Is first object above second (allows edges to touch)?

`box '((2,2),(1,1))' >^ box '((1,1),(0,0))'` → `t`

_`geometric_type`_ `?#` _`geometric_type`_ → `boolean`

Do these objects intersect? Available for these pairs of types: (`box`, `box`), (`lseg`, `box`), (`lseg`, `lseg`), (`lseg`, `line`), (`line`, `box`), (`line`, `line`), (`path`, `path`).

`lseg '[(-1,0),(1,0)]' ?# box '(2,2),(-2,-2)'` → `t`

`?-` `line` → `boolean`

`?-` `lseg` → `boolean`

Is line horizontal?

`?- lseg '[(-1,0),(1,0)]'` → `t`

`point` `?-` `point` → `boolean`

Are points horizontally aligned (that is, have same y coordinate)?

`point '(1,0)' ?- point '(0,0)'` → `t`

`?|` `line` → `boolean`

`?|` `lseg` → `boolean`

Is line vertical?

`?| lseg '[(-1,0),(1,0)]'` → `f`

`point` `?|` `point` → `boolean`

Are points vertically aligned (that is, have same x coordinate)?

`point '(0,1)' ?| point '(0,0)'` → `t`

`line` `?-|` `line` → `boolean`

`lseg` `?-|` `lseg` → `boolean`

Are lines perpendicular?

`lseg '[(0,0),(0,1)]' ?-| lseg '[(0,0),(1,0)]'` → `t`

`line` `?||` `line` → `boolean`

`lseg` `?||` `lseg` → `boolean`

Are lines parallel?

`lseg '[(-1,0),(1,0)]' ?|| lseg '[(-1,2),(1,2)]'` → `t`

_`geometric_type`_ `~=` _`geometric_type`_ → `boolean`

Are these objects the same? Available for `point`, `box`, `polygon`, `circle`.

`polygon '((0,0),(1,1))' ~= polygon '((1,1),(0,0))'` → `t`
