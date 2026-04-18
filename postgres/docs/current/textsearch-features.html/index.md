---
title: "PostgreSQL: Documentation: 18: 12.4. Additional Features"
source: "https://www.postgresql.org/docs/current/textsearch-features.html"
canonical_url: "https://www.postgresql.org/docs/current/textsearch-features.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:45.948Z"
content_hash: "4f33367f188670336be987505a93401ce80cf50c183e6a028207ded679140e8e"
menu_path: ["PostgreSQL: Documentation: 18: 12.4. Additional Features"]
section_path: []
nav_prev: {"path": "postgres/docs/current/pltcl-config.html/index.md", "title": "PostgreSQL: Documentation: 18: 42.11.\u00a0PL/Tcl Configuration"}
nav_next: {"path": "postgres/docs/current/sql-createdatabase.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE DATABASE"}
---

This section describes additional functions and operators that are useful in connection with text search.

### 12.4.1. Manipulating Documents [#](#TEXTSEARCH-MANIPULATE-TSVECTOR)

[Section 12.3.1](https://www.postgresql.org/docs/current/textsearch-controls.html#TEXTSEARCH-PARSING-DOCUMENTS "12.3.1. Parsing Documents") showed how raw textual documents can be converted into `tsvector` values. PostgreSQL also provides functions and operators that can be used to manipulate documents that are already in `tsvector` form.

`` `tsvector` || `tsvector` ``

The `tsvector` concatenation operator returns a vector which combines the lexemes and positional information of the two vectors given as arguments. Positions and weight labels are retained during the concatenation. Positions appearing in the right-hand vector are offset by the largest position mentioned in the left-hand vector, so that the result is nearly equivalent to the result of performing `to_tsvector` on the concatenation of the two original document strings. (The equivalence is not exact, because any stop-words removed from the end of the left-hand argument will not affect the result, whereas they would have affected the positions of the lexemes in the right-hand argument if textual concatenation were used.)

One advantage of using concatenation in the vector form, rather than concatenating text before applying `to_tsvector`, is that you can use different configurations to parse different sections of the document. Also, because the `setweight` function marks all lexemes of the given vector the same way, it is necessary to parse the text and do `setweight` before concatenating if you want to label different parts of the document with different weights.

`` setweight(_`vector`_ `tsvector`, _`weight`_ `"char"`) returns `tsvector` ``

`setweight` returns a copy of the input vector in which every position has been labeled with the given _`weight`_, either `A`, `B`, `C`, or `D`. (`D` is the default for new vectors and as such is not displayed on output.) These labels are retained when vectors are concatenated, allowing words from different parts of a document to be weighted differently by ranking functions.

Note that weight labels apply to _positions_, not _lexemes_. If the input vector has been stripped of positions then `setweight` does nothing.

`` length(_`vector`_ `tsvector`) returns `integer` ``

Returns the number of lexemes stored in the vector.

`` strip(_`vector`_ `tsvector`) returns `tsvector` ``

Returns a vector that lists the same lexemes as the given vector, but lacks any position or weight information. The result is usually much smaller than an unstripped vector, but it is also less useful. Relevance ranking does not work as well on stripped vectors as unstripped ones. Also, the `<->` (FOLLOWED BY) `tsquery` operator will never match stripped input, since it cannot determine the distance between lexeme occurrences.

A full list of `tsvector`\-related functions is available in [Table 9.43](https://www.postgresql.org/docs/current/functions-textsearch.html#TEXTSEARCH-FUNCTIONS-TABLE "Table 9.43. Text Search Functions").

### 12.4.2. Manipulating Queries [#](#TEXTSEARCH-MANIPULATE-TSQUERY)

[Section 12.3.2](https://www.postgresql.org/docs/current/textsearch-controls.html#TEXTSEARCH-PARSING-QUERIES "12.3.2. Parsing Queries") showed how raw textual queries can be converted into `tsquery` values. PostgreSQL also provides functions and operators that can be used to manipulate queries that are already in `tsquery` form.

`` `tsquery` && `tsquery` ``

Returns the AND-combination of the two given queries.

`` `tsquery` || `tsquery` ``

Returns the OR-combination of the two given queries.

`` !! `tsquery` ``

Returns the negation (NOT) of the given query.

`` `tsquery` <-> `tsquery` ``

Returns a query that searches for a match to the first given query immediately followed by a match to the second given query, using the `<->` (FOLLOWED BY) `tsquery` operator. For example:

SELECT to\_tsquery('fat') <-> to\_tsquery('cat | rat');
          ?column?
----------------------------
 'fat' <-> ( 'cat' | 'rat' )

`` tsquery_phrase(_`query1`_ `tsquery`, _`query2`_ `tsquery` [, _`distance`_ `integer` ]) returns `tsquery` ``

Returns a query that searches for a match to the first given query followed by a match to the second given query at a distance of exactly _`distance`_ lexemes, using the ``<_`N`_>`` `tsquery` operator. For example:

SELECT tsquery\_phrase(to\_tsquery('fat'), to\_tsquery('cat'), 10);
  tsquery\_phrase
------------------
 'fat' <10> 'cat'

`` numnode(_`query`_ `tsquery`) returns `integer` ``

Returns the number of nodes (lexemes plus operators) in a `tsquery`. This function is useful to determine if the _`query`_ is meaningful (returns > 0), or contains only stop words (returns 0). Examples:

SELECT numnode(plainto\_tsquery('the any'));
NOTICE:  query contains only stopword(s) or doesn't contain lexeme(s), ignored
 numnode
---------
       0

SELECT numnode('foo & bar'::tsquery);
 numnode
---------
       3

`` querytree(_`query`_ `tsquery`) returns `text` ``

Returns the portion of a `tsquery` that can be used for searching an index. This function is useful for detecting unindexable queries, for example those containing only stop words or only negated terms. For example:

SELECT querytree(to\_tsquery('defined'));
 querytree
-----------
 'defin'

SELECT querytree(to\_tsquery('!defined'));
 querytree
-----------
 T

#### 12.4.2.1. Query Rewriting [#](#TEXTSEARCH-QUERY-REWRITING)

The `ts_rewrite` family of functions search a given `tsquery` for occurrences of a target subquery, and replace each occurrence with a substitute subquery. In essence this operation is a `tsquery`\-specific version of substring replacement. A target and substitute combination can be thought of as a _query rewrite rule_. A collection of such rewrite rules can be a powerful search aid. For example, you can expand the search using synonyms (e.g., `new york`, `big apple`, `nyc`, `gotham`) or narrow the search to direct the user to some hot topic. There is some overlap in functionality between this feature and thesaurus dictionaries ([Section 12.6.4](https://www.postgresql.org/docs/current/textsearch-dictionaries.html#TEXTSEARCH-THESAURUS "12.6.4. Thesaurus Dictionary")). However, you can modify a set of rewrite rules on-the-fly without reindexing, whereas updating a thesaurus requires reindexing to be effective.

`` ts_rewrite (_`query`_ `tsquery`, _`target`_ `tsquery`, _`substitute`_ `tsquery`) returns `tsquery` ``

This form of `ts_rewrite` simply applies a single rewrite rule: _`target`_ is replaced by _`substitute`_ wherever it appears in _`query`_. For example:

SELECT ts\_rewrite('a & b'::tsquery, 'a'::tsquery, 'c'::tsquery);
 ts\_rewrite
------------
 'b' & 'c'

`` ts_rewrite (_`query`_ `tsquery`, _`select`_ `text`) returns `tsquery` ``

This form of `ts_rewrite` accepts a starting _`query`_ and an SQL _`select`_ command, which is given as a text string. The _`select`_ must yield two columns of `tsquery` type. For each row of the _`select`_ result, occurrences of the first column value (the target) are replaced by the second column value (the substitute) within the current _`query`_ value. For example:

CREATE TABLE aliases (t tsquery PRIMARY KEY, s tsquery);
INSERT INTO aliases VALUES('a', 'c');

SELECT ts\_rewrite('a & b'::tsquery, 'SELECT t,s FROM aliases');
 ts\_rewrite
------------
 'b' & 'c'

Note that when multiple rewrite rules are applied in this way, the order of application can be important; so in practice you will want the source query to `ORDER BY` some ordering key.

Let's consider a real-life astronomical example. We'll expand query `supernovae` using table-driven rewriting rules:

CREATE TABLE aliases (t tsquery primary key, s tsquery);
INSERT INTO aliases VALUES(to\_tsquery('supernovae'), to\_tsquery('supernovae|sn'));

SELECT ts\_rewrite(to\_tsquery('supernovae & crab'), 'SELECT \* FROM aliases');
           ts\_rewrite
---------------------------------
 'crab' & ( 'supernova' | 'sn' )

We can change the rewriting rules just by updating the table:

UPDATE aliases
SET s = to\_tsquery('supernovae|sn & !nebulae')
WHERE t = to\_tsquery('supernovae');

SELECT ts\_rewrite(to\_tsquery('supernovae & crab'), 'SELECT \* FROM aliases');
                 ts\_rewrite
---------------------------------------------
 'crab' & ( 'supernova' | 'sn' & !'nebula' )

Rewriting can be slow when there are many rewriting rules, since it checks every rule for a possible match. To filter out obvious non-candidate rules we can use the containment operators for the `tsquery` type. In the example below, we select only those rules which might match the original query:

SELECT ts\_rewrite('a & b'::tsquery,
                  'SELECT t,s FROM aliases WHERE ''a & b''::tsquery @> t');
 ts\_rewrite
------------
 'b' & 'c'

### 12.4.3. Triggers for Automatic Updates [#](#TEXTSEARCH-UPDATE-TRIGGERS)

### Note

The method described in this section has been obsoleted by the use of stored generated columns, as described in [Section 12.2.2](https://www.postgresql.org/docs/current/textsearch-tables.html#TEXTSEARCH-TABLES-INDEX "12.2.2. Creating Indexes").

When using a separate column to store the `tsvector` representation of your documents, it is necessary to create a trigger to update the `tsvector` column when the document content columns change. Two built-in trigger functions are available for this, or you can write your own.

tsvector\_update\_trigger(_`tsvector_column_name`_,​ _`config_name`_, _`text_column_name`_ \[, ... \])
tsvector\_update\_trigger\_column(_`tsvector_column_name`_,​ _`config_column_name`_, _`text_column_name`_ \[, ... \])

These trigger functions automatically compute a `tsvector` column from one or more textual columns, under the control of parameters specified in the `CREATE TRIGGER` command. An example of their use is:

CREATE TABLE messages (
    title       text,
    body        text,
    tsv         tsvector
);

CREATE TRIGGER tsvectorupdate BEFORE INSERT OR UPDATE
ON messages FOR EACH ROW EXECUTE FUNCTION
tsvector\_update\_trigger(tsv, 'pg\_catalog.english', title, body);

INSERT INTO messages VALUES('title here', 'the body text is here');

SELECT \* FROM messages;
   title    |         body          |            tsv
------------+-----------------------+----------------------------
 title here | the body text is here | 'bodi':4 'text':5 'titl':1

SELECT title, body FROM messages WHERE tsv @@ to\_tsquery('title & body');
   title    |         body
------------+-----------------------
 title here | the body text is here

Having created this trigger, any change in `title` or `body` will automatically be reflected into `tsv`, without the application having to worry about it.

The first trigger argument must be the name of the `tsvector` column to be updated. The second argument specifies the text search configuration to be used to perform the conversion. For `tsvector_update_trigger`, the configuration name is simply given as the second trigger argument. It must be schema-qualified as shown above, so that the trigger behavior will not change with changes in `search_path`. For `tsvector_update_trigger_column`, the second trigger argument is the name of another table column, which must be of type `regconfig`. This allows a per-row selection of configuration to be made. The remaining argument(s) are the names of textual columns (of type `text`, `varchar`, or `char`). These will be included in the document in the order given. NULL values will be skipped (but the other columns will still be indexed).

A limitation of these built-in triggers is that they treat all the input columns alike. To process columns differently — for example, to weight title differently from body — it is necessary to write a custom trigger. Here is an example using PL/pgSQL as the trigger language:

CREATE FUNCTION messages\_trigger() RETURNS trigger AS $$
begin
  new.tsv :=
     setweight(to\_tsvector('pg\_catalog.english', coalesce(new.title,'')), 'A') ||
     setweight(to\_tsvector('pg\_catalog.english', coalesce(new.body,'')), 'D');
  return new;
end
$$ LANGUAGE plpgsql;

CREATE TRIGGER tsvectorupdate BEFORE INSERT OR UPDATE
    ON messages FOR EACH ROW EXECUTE FUNCTION messages\_trigger();

Keep in mind that it is important to specify the configuration name explicitly when creating `tsvector` values inside triggers, so that the column's contents will not be affected by changes to `default_text_search_config`. Failure to do this is likely to lead to problems such as search results changing after a dump and restore.

### 12.4.4. Gathering Document Statistics [#](#TEXTSEARCH-STATISTICS)

The function `ts_stat` is useful for checking your configuration and for finding stop-word candidates.

ts\_stat(_`sqlquery`_ `text`, \[ _`weights`_ `text`, \]
        OUT _`word`_ `text`, OUT _`ndoc`_ `integer`,
        OUT _`nentry`_ `integer`) returns `setof record`

_`sqlquery`_ is a text value containing an SQL query which must return a single `tsvector` column. `ts_stat` executes the query and returns statistics about each distinct lexeme (word) contained in the `tsvector` data. The columns returned are

*   _`word`_ `text` — the value of a lexeme
    
*   _`ndoc`_ `integer` — number of documents (`tsvector`s) the word occurred in
    
*   _`nentry`_ `integer` — total number of occurrences of the word
    

If _`weights`_ is supplied, only occurrences having one of those weights are counted.

For example, to find the ten most frequent words in a document collection:

SELECT \* FROM ts\_stat('SELECT vector FROM apod')
ORDER BY nentry DESC, ndoc DESC, word
LIMIT 10;

The same, but counting only word occurrences with weight `A` or `B`:

SELECT \* FROM ts\_stat('SELECT vector FROM apod', 'ab')
ORDER BY nentry DESC, ndoc DESC, word
LIMIT 10;
