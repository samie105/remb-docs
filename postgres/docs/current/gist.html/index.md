---
title: "PostgreSQL: Documentation: 18: 65.2. GiST Indexes"
source: "https://www.postgresql.org/docs/current/gist.html"
canonical_url: "https://www.postgresql.org/docs/current/gist.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:25.772Z"
content_hash: "186f97f5acb2f002b31b63425b987948df86e36e2b60ff9a545db97101196854"
menu_path: ["PostgreSQL: Documentation: 18: 65.2. GiST Indexes"]
section_path: []
nav_prev: {"path": "postgres/docs/current/gin.html/index.md", "title": "PostgreSQL: Documentation: 18: 65.4.\u00a0GIN Indexes"}
nav_next: {"path": "postgres/docs/current/git.html/index.md", "title": "PostgreSQL: Documentation: 18: I.1.\u00a0Getting the Source via Git"}
---

### 65.2.1. Introduction [#](#GIST-INTRO)

GiST stands for Generalized Search Tree. It is a balanced, tree-structured access method, that acts as a base template in which to implement arbitrary indexing schemes. B-trees, R-trees and many other indexing schemes can be implemented in GiST.

One advantage of GiST is that it allows the development of custom data types with the appropriate access methods, by an expert in the domain of the data type, rather than a database expert.

Some of the information here is derived from the University of California at Berkeley's GiST Indexing Project [web site](http://gist.cs.berkeley.edu/) and Marcel Kornacker's thesis, [Access Methods for Next-Generation Database Systems](http://www.sai.msu.su/~megera/postgres/gist/papers/concurrency/access-methods-for-next-generation.pdf.gz). The GiST implementation in PostgreSQL is primarily maintained by Teodor Sigaev and Oleg Bartunov, and there is more information on their [web site](http://www.sai.msu.su/~megera/postgres/gist/).

### 65.2.2. Built-in Operator Classes [#](#GIST-BUILTIN-OPCLASSES)

The core PostgreSQL distribution includes the GiST operator classes shown in [Table 65.1](https://www.postgresql.org/docs/current/gist.html#GIST-BUILTIN-OPCLASSES-TABLE "Table 65.1. Built-in GiST Operator Classes"). (Some of the optional modules described in [Appendix F](https://www.postgresql.org/docs/current/contrib.html "Appendix F. Additional Supplied Modules and Extensions") provide additional GiST operator classes.)

**Table 65.1. Built-in GiST Operator Classes**

  

Name

Indexable Operators

Ordering Operators

`box_ops`

`<< (box, box)`

`<-> (box, point)`

`&< (box, box)`

`&& (box, box)`

`&> (box, box)`

`>> (box, box)`

`~= (box, box)`

`@> (box, box)`

`<@ (box, box)`

`&<| (box, box)`

`<<| (box, box)`

`|>> (box, box)`

`|&> (box, box)`

`circle_ops`

`<< (circle, circle)`

`<-> (circle, point)`

`&< (circle, circle)`

`&> (circle, circle)`

`>> (circle, circle)`

`<@ (circle, circle)`

`@> (circle, circle)`

`~= (circle, circle)`

`&& (circle, circle)`

`|>> (circle, circle)`

`<<| (circle, circle)`

`&<| (circle, circle)`

`|&> (circle, circle)`

`inet_ops`

`<< (inet, inet)`

 

`<<= (inet, inet)`

`>> (inet, inet)`

`>>= (inet, inet)`

`= (inet, inet)`

`<> (inet, inet)`

`< (inet, inet)`

`<= (inet, inet)`

`> (inet, inet)`

`>= (inet, inet)`

`&& (inet, inet)`

`multirange_ops`

`= (anymultirange, anymultirange)`

 

`&& (anymultirange, anymultirange)`

`&& (anymultirange, anyrange)`

`@> (anymultirange, anyelement)`

`@> (anymultirange, anymultirange)`

`@> (anymultirange, anyrange)`

`<@ (anymultirange, anymultirange)`

`<@ (anymultirange, anyrange)`

`<< (anymultirange, anymultirange)`

`<< (anymultirange, anyrange)`

`>> (anymultirange, anymultirange)`

`>> (anymultirange, anyrange)`

`&< (anymultirange, anymultirange)`

`&< (anymultirange, anyrange)`

`&> (anymultirange, anymultirange)`

`&> (anymultirange, anyrange)`

`-|- (anymultirange, anymultirange)`

`-|- (anymultirange, anyrange)`

`point_ops`

`|>> (point, point)`

`<-> (point, point)`

`<< (point, point)`

`>> (point, point)`

`<<| (point, point)`

`~= (point, point)`

`<@ (point, box)`

`<@ (point, polygon)`

`<@ (point, circle)`

`poly_ops`

`<< (polygon, polygon)`

`<-> (polygon, point)`

`&< (polygon, polygon)`

`&> (polygon, polygon)`

`>> (polygon, polygon)`

`<@ (polygon, polygon)`

`@> (polygon, polygon)`

`~= (polygon, polygon)`

`&& (polygon, polygon)`

`<<| (polygon, polygon)`

`&<| (polygon, polygon)`

`|&> (polygon, polygon)`

`|>> (polygon, polygon)`

`range_ops`

`= (anyrange, anyrange)`

 

`&& (anyrange, anyrange)`

`&& (anyrange, anymultirange)`

`@> (anyrange, anyelement)`

`@> (anyrange, anyrange)`

`@> (anyrange, anymultirange)`

`<@ (anyrange, anyrange)`

`<@ (anyrange, anymultirange)`

`<< (anyrange, anyrange)`

`<< (anyrange, anymultirange)`

`>> (anyrange, anyrange)`

`>> (anyrange, anymultirange)`

`&< (anyrange, anyrange)`

`&< (anyrange, anymultirange)`

`&> (anyrange, anyrange)`

`&> (anyrange, anymultirange)`

`-|- (anyrange, anyrange)`

`-|- (anyrange, anymultirange)`

`tsquery_ops`

`<@ (tsquery, tsquery)`

 

`@> (tsquery, tsquery)`

`tsvector_ops`

`@@ (tsvector, tsquery)`

 

For historical reasons, the `inet_ops` operator class is not the default class for types `inet` and `cidr`. To use it, mention the class name in `CREATE INDEX`, for example

CREATE INDEX ON my\_table USING GIST (my\_inet\_column inet\_ops);

### 65.2.3. Extensibility [#](#GIST-EXTENSIBILITY)

Traditionally, implementing a new index access method meant a lot of difficult work. It was necessary to understand the inner workings of the database, such as the lock manager and Write-Ahead Log. The GiST interface has a high level of abstraction, requiring the access method implementer only to implement the semantics of the data type being accessed. The GiST layer itself takes care of concurrency, logging and searching the tree structure.

This extensibility should not be confused with the extensibility of the other standard search trees in terms of the data they can handle. For example, PostgreSQL supports extensible B-trees and hash indexes. That means that you can use PostgreSQL to build a B-tree or hash over any data type you want. But B-trees only support range predicates (`<`, `=`, `>`), and hash indexes only support equality queries.

So if you index, say, an image collection with a PostgreSQL B-tree, you can only issue queries such as “is imagex equal to imagey”, “is imagex less than imagey” and “is imagex greater than imagey”. Depending on how you define “equals”, “less than” and “greater than” in this context, this could be useful. However, by using a GiST based index, you could create ways to ask domain-specific questions, perhaps “find all images of horses” or “find all over-exposed images”.

All it takes to get a GiST access method up and running is to implement several user-defined methods, which define the behavior of keys in the tree. Of course these methods have to be pretty fancy to support fancy queries, but for all the standard queries (B-trees, R-trees, etc.) they're relatively straightforward. In short, GiST combines extensibility along with generality, code reuse, and a clean interface.

There are five methods that an index operator class for GiST must provide, and seven that are optional. Correctness of the index is ensured by proper implementation of the `same`, `consistent` and `union` methods, while efficiency (size and speed) of the index will depend on the `penalty` and `picksplit` methods. Two optional methods are `compress` and `decompress`, which allow an index to have internal tree data of a different type than the data it indexes. The leaves are to be of the indexed data type, while the other tree nodes can be of any C struct (but you still have to follow PostgreSQL data type rules here, see about `varlena` for variable sized data). If the tree's internal data type exists at the SQL level, the `STORAGE` option of the `CREATE OPERATOR CLASS` command can be used. The optional eighth method is `distance`, which is needed if the operator class wishes to support ordered scans (nearest-neighbor searches). The optional ninth method `fetch` is needed if the operator class wishes to support index-only scans, except when the `compress` method is omitted. The optional tenth method `options` is needed if the operator class has user-specified parameters. The optional eleventh method `sortsupport` is used to speed up building a GiST index. The optional twelfth method `stratnum` is used to translate compare types (from `src/include/access/cmptype.h`) into strategy numbers used by the operator class. This lets the core code look up operators for temporal constraint indexes.

`consistent`

Given an index entry `p` and a query value `q`, this function determines whether the index entry is “consistent” with the query; that is, could the predicate “_`indexed_column`_ _`indexable_operator`_ `q`” be true for any row represented by the index entry? For a leaf index entry this is equivalent to testing the indexable condition, while for an internal tree node this determines whether it is necessary to scan the subtree of the index represented by the tree node. When the result is `true`, a `recheck` flag must also be returned. This indicates whether the predicate is certainly true or only possibly true. If `recheck` = `false` then the index has tested the predicate condition exactly, whereas if `recheck` = `true` the row is only a candidate match. In that case the system will automatically evaluate the _`indexable_operator`_ against the actual row value to see if it is really a match. This convention allows GiST to support both lossless and lossy index structures.

The SQL declaration of the function must look like this:

CREATE OR REPLACE FUNCTION my\_consistent(internal, data\_type, smallint, oid, internal)
RETURNS bool
AS 'MODULE\_PATHNAME'
LANGUAGE C STRICT;

And the matching code in the C module could then follow this skeleton:

PG\_FUNCTION\_INFO\_V1(my\_consistent);

Datum
my\_consistent(PG\_FUNCTION\_ARGS)
{
    GISTENTRY  \*entry = (GISTENTRY \*) PG\_GETARG\_POINTER(0);
    data\_type  \*query = PG\_GETARG\_DATA\_TYPE\_P(1);
    StrategyNumber strategy = (StrategyNumber) PG\_GETARG\_UINT16(2);
    /\* Oid subtype = PG\_GETARG\_OID(3); \*/
    bool       \*recheck = (bool \*) PG\_GETARG\_POINTER(4);
    data\_type  \*key = DatumGetDataType(entry->key);
    bool        retval;

    /\*
     \* determine return value as a function of strategy, key and query.
     \*
     \* Use GIST\_LEAF(entry) to know where you're called in the index tree,
     \* which comes handy when supporting the = operator for example (you could
     \* check for non empty union() in non-leaf nodes and equality in leaf
     \* nodes).
     \*/

    \*recheck = true;        /\* or false if check is exact \*/

    PG\_RETURN\_BOOL(retval);
}

Here, `key` is an element in the index and `query` the value being looked up in the index. The `StrategyNumber` parameter indicates which operator of your operator class is being applied — it matches one of the operator numbers in the `CREATE OPERATOR CLASS` command.

Depending on which operators you have included in the class, the data type of `query` could vary with the operator, since it will be whatever type is on the right-hand side of the operator, which might be different from the indexed data type appearing on the left-hand side. (The above code skeleton assumes that only one type is possible; if not, fetching the `query` argument value would have to depend on the operator.) It is recommended that the SQL declaration of the `consistent` function use the opclass's indexed data type for the `query` argument, even though the actual type might be something else depending on the operator.

`union`

This method consolidates information in the tree. Given a set of entries, this function generates a new index entry that represents all the given entries.

The SQL declaration of the function must look like this:

CREATE OR REPLACE FUNCTION my\_union(internal, internal)
RETURNS storage\_type
AS 'MODULE\_PATHNAME'
LANGUAGE C STRICT;

And the matching code in the C module could then follow this skeleton:

PG\_FUNCTION\_INFO\_V1(my\_union);

Datum
my\_union(PG\_FUNCTION\_ARGS)
{
    GistEntryVector \*entryvec = (GistEntryVector \*) PG\_GETARG\_POINTER(0);
    GISTENTRY  \*ent = entryvec->vector;
    data\_type  \*out,
               \*tmp,
               \*old;
    int         numranges,
                i = 0;

    numranges = entryvec->n;
    tmp = DatumGetDataType(ent\[0\].key);
    out = tmp;

    if (numranges == 1)
    {
        out = data\_type\_deep\_copy(tmp);

        PG\_RETURN\_DATA\_TYPE\_P(out);
    }

    for (i = 1; i < numranges; i++)
    {
        old = out;
        tmp = DatumGetDataType(ent\[i\].key);
        out = my\_union\_implementation(out, tmp);
    }

    PG\_RETURN\_DATA\_TYPE\_P(out);
}

As you can see, in this skeleton we're dealing with a data type where `union(X, Y, Z) = union(union(X, Y), Z)`. It's easy enough to support data types where this is not the case, by implementing the proper union algorithm in this GiST support method.

The result of the `union` function must be a value of the index's storage type, whatever that is (it might or might not be different from the indexed column's type). The `union` function should return a pointer to newly `palloc()`ed memory. You can't just return the input value as-is, even if there is no type change.

As shown above, the `union` function's first `internal` argument is actually a `GistEntryVector` pointer. The second argument is a pointer to an integer variable, which can be ignored. (It used to be required that the `union` function store the size of its result value into that variable, but this is no longer necessary.)

`compress`

Converts a data item into a format suitable for physical storage in an index page. If the `compress` method is omitted, data items are stored in the index without modification.

The SQL declaration of the function must look like this:

CREATE OR REPLACE FUNCTION my\_compress(internal)
RETURNS internal
AS 'MODULE\_PATHNAME'
LANGUAGE C STRICT;

And the matching code in the C module could then follow this skeleton:

PG\_FUNCTION\_INFO\_V1(my\_compress);

Datum
my\_compress(PG\_FUNCTION\_ARGS)
{
    GISTENTRY  \*entry = (GISTENTRY \*) PG\_GETARG\_POINTER(0);
    GISTENTRY  \*retval;

    if (entry->leafkey)
    {
        /\* replace entry->key with a compressed version \*/
        compressed\_data\_type \*compressed\_data = palloc(sizeof(compressed\_data\_type));

        /\* fill \*compressed\_data from entry->key ... \*/

        retval = palloc(sizeof(GISTENTRY));
        gistentryinit(\*retval, PointerGetDatum(compressed\_data),
                      entry->rel, entry->page, entry->offset, FALSE);
    }
    else
    {
        /\* typically we needn't do anything with non-leaf entries \*/
        retval = entry;
    }

    PG\_RETURN\_POINTER(retval);
}

You have to adapt _`compressed_data_type`_ to the specific type you're converting to in order to compress your leaf nodes, of course.

`decompress`

Converts the stored representation of a data item into a format that can be manipulated by the other GiST methods in the operator class. If the `decompress` method is omitted, it is assumed that the other GiST methods can work directly on the stored data format. (`decompress` is not necessarily the reverse of the `compress` method; in particular, if `compress` is lossy then it's impossible for `decompress` to exactly reconstruct the original data. `decompress` is not necessarily equivalent to `fetch`, either, since the other GiST methods might not require full reconstruction of the data.)

The SQL declaration of the function must look like this:

CREATE OR REPLACE FUNCTION my\_decompress(internal)
RETURNS internal
AS 'MODULE\_PATHNAME'
LANGUAGE C STRICT;

And the matching code in the C module could then follow this skeleton:

PG\_FUNCTION\_INFO\_V1(my\_decompress);

Datum
my\_decompress(PG\_FUNCTION\_ARGS)
{
    PG\_RETURN\_POINTER(PG\_GETARG\_POINTER(0));
}

The above skeleton is suitable for the case where no decompression is needed. (But, of course, omitting the method altogether is even easier, and is recommended in such cases.)

`penalty`

Returns a value indicating the “cost” of inserting the new entry into a particular branch of the tree. Items will be inserted down the path of least `penalty` in the tree. Values returned by `penalty` should be non-negative. If a negative value is returned, it will be treated as zero.

The SQL declaration of the function must look like this:

CREATE OR REPLACE FUNCTION my\_penalty(internal, internal, internal)
RETURNS internal
AS 'MODULE\_PATHNAME'
LANGUAGE C STRICT;  -- in some cases penalty functions need not be strict

And the matching code in the C module could then follow this skeleton:

PG\_FUNCTION\_INFO\_V1(my\_penalty);

Datum
my\_penalty(PG\_FUNCTION\_ARGS)
{
    GISTENTRY  \*origentry = (GISTENTRY \*) PG\_GETARG\_POINTER(0);
    GISTENTRY  \*newentry = (GISTENTRY \*) PG\_GETARG\_POINTER(1);
    float      \*penalty = (float \*) PG\_GETARG\_POINTER(2);
    data\_type  \*orig = DatumGetDataType(origentry->key);
    data\_type  \*new = DatumGetDataType(newentry->key);

    \*penalty = my\_penalty\_implementation(orig, new);
    PG\_RETURN\_POINTER(penalty);
}

For historical reasons, the `penalty` function doesn't just return a `float` result; instead it has to store the value at the location indicated by the third argument. The return value per se is ignored, though it's conventional to pass back the address of that argument.

The `penalty` function is crucial to good performance of the index. It'll get used at insertion time to determine which branch to follow when choosing where to add the new entry in the tree. At query time, the more balanced the index, the quicker the lookup.

`picksplit`

When an index page split is necessary, this function decides which entries on the page are to stay on the old page, and which are to move to the new page.

The SQL declaration of the function must look like this:

CREATE OR REPLACE FUNCTION my\_picksplit(internal, internal)
RETURNS internal
AS 'MODULE\_PATHNAME'
LANGUAGE C STRICT;

And the matching code in the C module could then follow this skeleton:

PG\_FUNCTION\_INFO\_V1(my\_picksplit);

Datum
my\_picksplit(PG\_FUNCTION\_ARGS)
{
    GistEntryVector \*entryvec = (GistEntryVector \*) PG\_GETARG\_POINTER(0);
    GIST\_SPLITVEC \*v = (GIST\_SPLITVEC \*) PG\_GETARG\_POINTER(1);
    OffsetNumber maxoff = entryvec->n - 1;
    GISTENTRY  \*ent = entryvec->vector;
    int         i,
                nbytes;
    OffsetNumber \*left,
               \*right;
    data\_type  \*tmp\_union;
    data\_type  \*unionL;
    data\_type  \*unionR;
    GISTENTRY \*\*raw\_entryvec;

    maxoff = entryvec->n - 1;
    nbytes = (maxoff + 1) \* sizeof(OffsetNumber);

    v->spl\_left = (OffsetNumber \*) palloc(nbytes);
    left = v->spl\_left;
    v->spl\_nleft = 0;

    v->spl\_right = (OffsetNumber \*) palloc(nbytes);
    right = v->spl\_right;
    v->spl\_nright = 0;

    unionL = NULL;
    unionR = NULL;

    /\* Initialize the raw entry vector. \*/
    raw\_entryvec = (GISTENTRY \*\*) malloc(entryvec->n \* sizeof(void \*));
    for (i = FirstOffsetNumber; i <= maxoff; i = OffsetNumberNext(i))
        raw\_entryvec\[i\] = &(entryvec->vector\[i\]);

    for (i = FirstOffsetNumber; i <= maxoff; i = OffsetNumberNext(i))
    {
        int         real\_index = raw\_entryvec\[i\] - entryvec->vector;

        tmp\_union = DatumGetDataType(entryvec->vector\[real\_index\].key);
        Assert(tmp\_union != NULL);

        /\*
         \* Choose where to put the index entries and update unionL and unionR
         \* accordingly. Append the entries to either v->spl\_left or
         \* v->spl\_right, and care about the counters.
         \*/

        if (my\_choice\_is\_left(unionL, curl, unionR, curr))
        {
            if (unionL == NULL)
                unionL = tmp\_union;
            else
                unionL = my\_union\_implementation(unionL, tmp\_union);

            \*left = real\_index;
            ++left;
            ++(v->spl\_nleft);
        }
        else
        {
            /\*
             \* Same on the right
             \*/
        }
    }

    v->spl\_ldatum = DataTypeGetDatum(unionL);
    v->spl\_rdatum = DataTypeGetDatum(unionR);
    PG\_RETURN\_POINTER(v);
}

Notice that the `picksplit` function's result is delivered by modifying the passed-in `v` structure. The return value per se is ignored, though it's conventional to pass back the address of `v`.

Like `penalty`, the `picksplit` function is crucial to good performance of the index. Designing suitable `penalty` and `picksplit` implementations is where the challenge of implementing well-performing GiST indexes lies.

`same`

Returns true if two index entries are identical, false otherwise. (An “index entry” is a value of the index's storage type, not necessarily the original indexed column's type.)

The SQL declaration of the function must look like this:

CREATE OR REPLACE FUNCTION my\_same(storage\_type, storage\_type, internal)
RETURNS internal
AS 'MODULE\_PATHNAME'
LANGUAGE C STRICT;

And the matching code in the C module could then follow this skeleton:

PG\_FUNCTION\_INFO\_V1(my\_same);

Datum
my\_same(PG\_FUNCTION\_ARGS)
{
    prefix\_range \*v1 = PG\_GETARG\_PREFIX\_RANGE\_P(0);
    prefix\_range \*v2 = PG\_GETARG\_PREFIX\_RANGE\_P(1);
    bool       \*result = (bool \*) PG\_GETARG\_POINTER(2);

    \*result = my\_eq(v1, v2);
    PG\_RETURN\_POINTER(result);
}

For historical reasons, the `same` function doesn't just return a Boolean result; instead it has to store the flag at the location indicated by the third argument. The return value per se is ignored, though it's conventional to pass back the address of that argument.

`distance`

Given an index entry `p` and a query value `q`, this function determines the index entry's “distance” from the query value. This function must be supplied if the operator class contains any ordering operators. A query using the ordering operator will be implemented by returning index entries with the smallest “distance” values first, so the results must be consistent with the operator's semantics. For a leaf index entry the result just represents the distance to the index entry; for an internal tree node, the result must be the smallest distance that any child entry could have.

The SQL declaration of the function must look like this:

CREATE OR REPLACE FUNCTION my\_distance(internal, data\_type, smallint, oid, internal)
RETURNS float8
AS 'MODULE\_PATHNAME'
LANGUAGE C STRICT;

And the matching code in the C module could then follow this skeleton:

PG\_FUNCTION\_INFO\_V1(my\_distance);

Datum
my\_distance(PG\_FUNCTION\_ARGS)
{
    GISTENTRY  \*entry = (GISTENTRY \*) PG\_GETARG\_POINTER(0);
    data\_type  \*query = PG\_GETARG\_DATA\_TYPE\_P(1);
    StrategyNumber strategy = (StrategyNumber) PG\_GETARG\_UINT16(2);
    /\* Oid subtype = PG\_GETARG\_OID(3); \*/
    /\* bool \*recheck = (bool \*) PG\_GETARG\_POINTER(4); \*/
    data\_type  \*key = DatumGetDataType(entry->key);
    double      retval;

    /\*
     \* determine return value as a function of strategy, key and query.
     \*/

    PG\_RETURN\_FLOAT8(retval);
}

The arguments to the `distance` function are identical to the arguments of the `consistent` function.

Some approximation is allowed when determining the distance, so long as the result is never greater than the entry's actual distance. Thus, for example, distance to a bounding box is usually sufficient in geometric applications. For an internal tree node, the distance returned must not be greater than the distance to any of the child nodes. If the returned distance is not exact, the function must set `*recheck` to true. (This is not necessary for internal tree nodes; for them, the calculation is always assumed to be inexact.) In this case the executor will calculate the accurate distance after fetching the tuple from the heap, and reorder the tuples if necessary.

If the distance function returns `*recheck = true` for any leaf node, the original ordering operator's return type must be `float8` or `float4`, and the distance function's result values must be comparable to those of the original ordering operator, since the executor will sort using both distance function results and recalculated ordering-operator results. Otherwise, the distance function's result values can be any finite `float8` values, so long as the relative order of the result values matches the order returned by the ordering operator. (Infinity and minus infinity are used internally to handle cases such as nulls, so it is not recommended that `distance` functions return these values.)

`fetch`

Converts the compressed index representation of a data item into the original data type, for index-only scans. The returned data must be an exact, non-lossy copy of the originally indexed value.

The SQL declaration of the function must look like this:

CREATE OR REPLACE FUNCTION my\_fetch(internal)
RETURNS internal
AS 'MODULE\_PATHNAME'
LANGUAGE C STRICT;

The argument is a pointer to a `GISTENTRY` struct. On entry, its `key` field contains a non-NULL leaf datum in compressed form. The return value is another `GISTENTRY` struct, whose `key` field contains the same datum in its original, uncompressed form. If the opclass's compress function does nothing for leaf entries, the `fetch` method can return the argument as-is. Or, if the opclass does not have a compress function, the `fetch` method can be omitted as well, since it would necessarily be a no-op.

The matching code in the C module could then follow this skeleton:

PG\_FUNCTION\_INFO\_V1(my\_fetch);

Datum
my\_fetch(PG\_FUNCTION\_ARGS)
{
    GISTENTRY  \*entry = (GISTENTRY \*) PG\_GETARG\_POINTER(0);
    input\_data\_type \*in = DatumGetPointer(entry->key);
    fetched\_data\_type \*fetched\_data;
    GISTENTRY  \*retval;

    retval = palloc(sizeof(GISTENTRY));
    fetched\_data = palloc(sizeof(fetched\_data\_type));

    /\*
     \* Convert 'fetched\_data' into the a Datum of the original datatype.
     \*/

    /\* fill \*retval from fetched\_data. \*/
    gistentryinit(\*retval, PointerGetDatum(converted\_datum),
                  entry->rel, entry->page, entry->offset, FALSE);

    PG\_RETURN\_POINTER(retval);
}

If the compress method is lossy for leaf entries, the operator class cannot support index-only scans, and must not define a `fetch` function.

`options`

Allows definition of user-visible parameters that control operator class behavior.

The SQL declaration of the function must look like this:

CREATE OR REPLACE FUNCTION my\_options(internal)
RETURNS void
AS 'MODULE\_PATHNAME'
LANGUAGE C STRICT;

The function is passed a pointer to a `local_relopts` struct, which needs to be filled with a set of operator class specific options. The options can be accessed from other support functions using the `PG_HAS_OPCLASS_OPTIONS()` and `PG_GET_OPCLASS_OPTIONS()` macros.

An example implementation of my\_options() and parameters use from other support functions are given below:

typedef enum MyEnumType
{
    MY\_ENUM\_ON,
    MY\_ENUM\_OFF,
    MY\_ENUM\_AUTO
} MyEnumType;

typedef struct
{
    int32   vl\_len\_;    /\* varlena header (do not touch directly!) \*/
    int     int\_param;  /\* integer parameter \*/
    double  real\_param; /\* real parameter \*/
    MyEnumType enum\_param; /\* enum parameter \*/
    int     str\_param;  /\* string parameter \*/
} MyOptionsStruct;

/\* String representation of enum values \*/
static relopt\_enum\_elt\_def myEnumValues\[\] =
{
    {"on", MY\_ENUM\_ON},
    {"off", MY\_ENUM\_OFF},
    {"auto", MY\_ENUM\_AUTO},
    {(const char \*) NULL}   /\* list terminator \*/
};

static char \*str\_param\_default = "default";

/\*
 \* Sample validator: checks that string is not longer than 8 bytes.
 \*/
static void
validate\_my\_string\_relopt(const char \*value)
{
    if (strlen(value) > 8)
        ereport(ERROR,
                (errcode(ERRCODE\_INVALID\_PARAMETER\_VALUE),
                 errmsg("str\_param must be at most 8 bytes")));
}

/\*
 \* Sample filler: switches characters to lower case.
 \*/
static Size
fill\_my\_string\_relopt(const char \*value, void \*ptr)
{
    char   \*tmp = str\_tolower(value, strlen(value), DEFAULT\_COLLATION\_OID);
    int     len = strlen(tmp);

    if (ptr)
        strcpy(ptr, tmp);

    pfree(tmp);
    return len + 1;
}

PG\_FUNCTION\_INFO\_V1(my\_options);

Datum
my\_options(PG\_FUNCTION\_ARGS)
{
    local\_relopts \*relopts = (local\_relopts \*) PG\_GETARG\_POINTER(0);

    init\_local\_reloptions(relopts, sizeof(MyOptionsStruct));
    add\_local\_int\_reloption(relopts, "int\_param", "integer parameter",
                            100, 0, 1000000,
                            offsetof(MyOptionsStruct, int\_param));
    add\_local\_real\_reloption(relopts, "real\_param", "real parameter",
                             1.0, 0.0, 1000000.0,
                             offsetof(MyOptionsStruct, real\_param));
    add\_local\_enum\_reloption(relopts, "enum\_param", "enum parameter",
                             myEnumValues, MY\_ENUM\_ON,
                             "Valid values are: \\"on\\", \\"off\\" and \\"auto\\".",
                             offsetof(MyOptionsStruct, enum\_param));
    add\_local\_string\_reloption(relopts, "str\_param", "string parameter",
                               str\_param\_default,
                               &validate\_my\_string\_relopt,
                               &fill\_my\_string\_relopt,
                               offsetof(MyOptionsStruct, str\_param));

    PG\_RETURN\_VOID();
}

PG\_FUNCTION\_INFO\_V1(my\_compress);

Datum
my\_compress(PG\_FUNCTION\_ARGS)
{
    int     int\_param = 100;
    double  real\_param = 1.0;
    MyEnumType enum\_param = MY\_ENUM\_ON;
    char   \*str\_param = str\_param\_default;

    /\*
     \* Normally, when opclass contains 'options' method, then options are always
     \* passed to support functions.  However, if you add 'options' method to
     \* existing opclass, previously defined indexes have no options, so the
     \* check is required.
     \*/
    if (PG\_HAS\_OPCLASS\_OPTIONS())
    {
        MyOptionsStruct \*options = (MyOptionsStruct \*) PG\_GET\_OPCLASS\_OPTIONS();

        int\_param = options->int\_param;
        real\_param = options->real\_param;
        enum\_param = options->enum\_param;
        str\_param = GET\_STRING\_RELOPTION(options, str\_param);
    }

    /\* the rest implementation of support function \*/
}

Since the representation of the key in GiST is flexible, it may depend on user-specified parameters. For instance, the length of key signature may be specified. See `gtsvector_options()` for example.

`sortsupport`

Returns a comparator function to sort data in a way that preserves locality. It is used by `CREATE INDEX` and `REINDEX` commands. The quality of the created index depends on how well the sort order determined by the comparator function preserves locality of the inputs.

The `sortsupport` method is optional. If it is not provided, `CREATE INDEX` builds the index by inserting each tuple to the tree using the `penalty` and `picksplit` functions, which is much slower.

The SQL declaration of the function must look like this:

CREATE OR REPLACE FUNCTION my\_sortsupport(internal)
RETURNS void
AS 'MODULE\_PATHNAME'
LANGUAGE C STRICT;

The argument is a pointer to a `SortSupport` struct. At a minimum, the function must fill in its comparator field. The comparator takes three arguments: two Datums to compare, and a pointer to the `SortSupport` struct. The Datums are the two indexed values in the format that they are stored in the index; that is, in the format returned by the `compress` method. The full API is defined in `src/include/utils/sortsupport.h`.

The matching code in the C module could then follow this skeleton:

PG\_FUNCTION\_INFO\_V1(my\_sortsupport);

static int
my\_fastcmp(Datum x, Datum y, SortSupport ssup)
{
  /\* establish order between x and y by computing some sorting value z \*/

  int z1 = ComputeSpatialCode(x);
  int z2 = ComputeSpatialCode(y);

  return z1 == z2 ? 0 : z1 > z2 ? 1 : -1;
}

Datum
my\_sortsupport(PG\_FUNCTION\_ARGS)
{
  SortSupport ssup = (SortSupport) PG\_GETARG\_POINTER(0);

  ssup->comparator = my\_fastcmp;
  PG\_RETURN\_VOID();
}

`translate_cmptype`

Given a `CompareType` value from `src/include/access/cmptype.h`, returns a strategy number used by this operator class for matching functionality. The function should return `InvalidStrategy` if the operator class has no matching strategy.

This is used for temporal index constraints (i.e., `PRIMARY KEY` and `UNIQUE`). If the operator class provides this function and it returns results for `COMPARE_EQ`, it can be used in the non-`WITHOUT OVERLAPS` part(s) of an index constraint.

This support function corresponds to the index access method callback function `amtranslatecmptype` (see [Section 63.2](https://www.postgresql.org/docs/current/index-functions.html "63.2. Index Access Method Functions")). The `amtranslatecmptype` callback function for GiST indexes merely calls down to the `translate_cmptype` support function of the respective operator family, since the GiST index access method has no fixed strategy numbers itself.

The SQL declaration of the function must look like this:

CREATE OR REPLACE FUNCTION my\_translate\_cmptype(integer)
RETURNS smallint
AS 'MODULE\_PATHNAME'
LANGUAGE C STRICT;

And the operator family registration must look like this:

ALTER OPERATOR FAMILY my\_opfamily USING gist ADD
    FUNCTION 12 ("any", "any") my\_translate\_cmptype(int);

The matching code in the C module could then follow this skeleton:

PG\_FUNCTION\_INFO\_V1(my\_translate\_cmptype);

Datum
my\_translate\_cmptype(PG\_FUNCTION\_ARGS)
{
    CompareType cmptype = PG\_GETARG\_INT32(0);
    StrategyNumber ret = InvalidStrategy;

    switch (cmptype)
    {
        case COMPARE\_EQ:
            ret = BTEqualStrategyNumber;
    }

    PG\_RETURN\_UINT16(ret);
}

One translation function is provided by PostgreSQL: `gist_translate_cmptype_common` is for operator classes that use the `RT*StrategyNumber` constants. The `btree_gist` extension defines a second translation function, `gist_translate_cmptype_btree`, for operator classes that use the `BT*StrategyNumber` constants.

All the GiST support methods are normally called in short-lived memory contexts; that is, `CurrentMemoryContext` will get reset after each tuple is processed. It is therefore not very important to worry about pfree'ing everything you palloc. However, in some cases it's useful for a support method to cache data across repeated calls. To do that, allocate the longer-lived data in `fcinfo->flinfo->fn_mcxt`, and keep a pointer to it in `fcinfo->flinfo->fn_extra`. Such data will survive for the life of the index operation (e.g., a single GiST index scan, index build, or index tuple insertion). Be careful to pfree the previous value when replacing a `fn_extra` value, or the leak will accumulate for the duration of the operation.

### 65.2.4. Implementation [#](#GIST-IMPLEMENTATION)

#### 65.2.4.1. GiST Index Build Methods [#](#GIST-BUFFERING-BUILD)

The simplest way to build a GiST index is just to insert all the entries, one by one. This tends to be slow for large indexes, because if the index tuples are scattered across the index and the index is large enough to not fit in cache, a lot of random I/O will be needed. PostgreSQL supports two alternative methods for initial build of a GiST index: _sorted_ and _buffered_ modes.

The sorted method is only available if each of the opclasses used by the index provides a `sortsupport` function, as described in [Section 65.2.3](https://www.postgresql.org/docs/current/gist.html#GIST-EXTENSIBILITY "65.2.3. Extensibility"). If they do, this method is usually the best, so it is used by default.

The buffered method works by not inserting tuples directly into the index right away. It can dramatically reduce the amount of random I/O needed for non-ordered data sets. For well-ordered data sets the benefit is smaller or non-existent, because only a small number of pages receive new tuples at a time, and those pages fit in cache even if the index as a whole does not.

The buffered method needs to call the `penalty` function more often than the simple method does, which consumes some extra CPU resources. Also, the buffers need temporary disk space, up to the size of the resulting index. Buffering can also influence the quality of the resulting index, in both positive and negative directions. That influence depends on various factors, like the distribution of the input data and the operator class implementation.

If sorting is not possible, then by default a GiST index build switches to the buffering method when the index size reaches [effective\_cache\_size](postgres/docs/current/runtime-config-query.html/index.md#GUC-EFFECTIVE-CACHE-SIZE). Buffering can be manually forced or prevented by the `buffering` parameter to the CREATE INDEX command. The default behavior is good for most cases, but turning buffering off might speed up the build somewhat if the input data is ordered.

### 65.2.5. Examples [#](#GIST-EXAMPLES)

The PostgreSQL source distribution includes several examples of index methods implemented using GiST. The core system currently provides text search support (indexing for `tsvector` and `tsquery`) as well as R-Tree equivalent functionality for some of the built-in geometric data types (see `src/backend/access/gist/gistproc.c`). The following `contrib` modules also contain GiST operator classes:

`btree_gist`

B-tree equivalent functionality for several data types

`cube`

Indexing for multidimensional cubes

`hstore`

Module for storing (key, value) pairs

`intarray`

RD-Tree for one-dimensional array of int4 values

`ltree`

Indexing for tree-like structures

`pg_trgm`

Text similarity using trigram matching

`seg`

Indexing for “float ranges”
