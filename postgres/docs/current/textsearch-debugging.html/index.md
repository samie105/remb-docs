---
title: "PostgreSQL: Documentation: 18: 12.8. Testing and Debugging Text Search"
source: "https://www.postgresql.org/docs/current/textsearch-debugging.html"
canonical_url: "https://www.postgresql.org/docs/current/textsearch-debugging.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:58.233Z"
content_hash: "798a9f4963297f0612e80a411cd76ae8365a9e28c0b0512379d5f7214bd58a4a"
menu_path: ["PostgreSQL: Documentation: 18: 12.8. Testing and Debugging Text Search"]
section_path: []
nav_prev: {"path": "postgres/docs/current/pgtestfsync.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_test_fsync"}
nav_next: {"path": "postgres/docs/current/sql-explain.html/index.md", "title": "PostgreSQL: Documentation: 18: EXPLAIN"}
---

The behavior of a custom text search configuration can easily become confusing. The functions described in this section are useful for testing text search objects. You can test a complete configuration, or test parsers and dictionaries separately.

### 12.8.1. Configuration Testing [#](#TEXTSEARCH-CONFIGURATION-TESTING)

The function `ts_debug` allows easy testing of a text search configuration.

ts\_debug(\[ _`config`_ `regconfig`, \] _`document`_ `text`,
         OUT _`alias`_ `text`,
         OUT _`description`_ `text`,
         OUT _`token`_ `text`,
         OUT _`dictionaries`_ `regdictionary[]`,
         OUT _`dictionary`_ `regdictionary`,
         OUT _`lexemes`_ `text[]`)
         returns setof record

`ts_debug` displays information about every token of _`document`_ as produced by the parser and processed by the configured dictionaries. It uses the configuration specified by _`config`_, or `default_text_search_config` if that argument is omitted.

`ts_debug` returns one row for each token identified in the text by the parser. The columns returned are

*   _`alias`_ `text` — short name of the token type
    
*   _`description`_ `text` — description of the token type
    
*   _`token`_ `text` — text of the token
    
*   _`dictionaries`_ `regdictionary[]` — the dictionaries selected by the configuration for this token type
    
*   _`dictionary`_ `regdictionary` — the dictionary that recognized the token, or `NULL` if none did
    
*   _`lexemes`_ `text[]` — the lexeme(s) produced by the dictionary that recognized the token, or `NULL` if none did; an empty array (`{}`) means it was recognized as a stop word
    

Here is a simple example:

SELECT \* FROM ts\_debug('english', 'a fat  cat sat on a mat - it ate a fat rats');
   alias   |   description   | token |  dictionaries  |  dictionary  | lexemes
-----------+-----------------+-------+----------------+--------------+---------
 asciiword | Word, all ASCII | a     | {english\_stem} | english\_stem | {}
 blank     | Space symbols   |       | {}             |              |
 asciiword | Word, all ASCII | fat   | {english\_stem} | english\_stem | {fat}
 blank     | Space symbols   |       | {}             |              |
 asciiword | Word, all ASCII | cat   | {english\_stem} | english\_stem | {cat}
 blank     | Space symbols   |       | {}             |              |
 asciiword | Word, all ASCII | sat   | {english\_stem} | english\_stem | {sat}
 blank     | Space symbols   |       | {}             |              |
 asciiword | Word, all ASCII | on    | {english\_stem} | english\_stem | {}
 blank     | Space symbols   |       | {}             |              |
 asciiword | Word, all ASCII | a     | {english\_stem} | english\_stem | {}
 blank     | Space symbols   |       | {}             |              |
 asciiword | Word, all ASCII | mat   | {english\_stem} | english\_stem | {mat}
 blank     | Space symbols   |       | {}             |              |
 blank     | Space symbols   | -     | {}             |              |
 asciiword | Word, all ASCII | it    | {english\_stem} | english\_stem | {}
 blank     | Space symbols   |       | {}             |              |
 asciiword | Word, all ASCII | ate   | {english\_stem} | english\_stem | {ate}
 blank     | Space symbols   |       | {}             |              |
 asciiword | Word, all ASCII | a     | {english\_stem} | english\_stem | {}
 blank     | Space symbols   |       | {}             |              |
 asciiword | Word, all ASCII | fat   | {english\_stem} | english\_stem | {fat}
 blank     | Space symbols   |       | {}             |              |
 asciiword | Word, all ASCII | rats  | {english\_stem} | english\_stem | {rat}

For a more extensive demonstration, we first create a `public.english` configuration and Ispell dictionary for the English language:

CREATE TEXT SEARCH CONFIGURATION public.english ( COPY = pg\_catalog.english );

CREATE TEXT SEARCH DICTIONARY english\_ispell (
    TEMPLATE = ispell,
    DictFile = english,
    AffFile = english,
    StopWords = english
);

ALTER TEXT SEARCH CONFIGURATION public.english
   ALTER MAPPING FOR asciiword WITH english\_ispell, english\_stem;

SELECT \* FROM ts\_debug('public.english', 'The Brightest supernovaes');
   alias   |   description   |    token    |         dictionaries          |   dictionary   |   lexemes
-----------+-----------------+-------------+-------------------------------+----------------+-------------
 asciiword | Word, all ASCII | The         | {english\_ispell,english\_stem} | english\_ispell | {}
 blank     | Space symbols   |             | {}                            |                |
 asciiword | Word, all ASCII | Brightest   | {english\_ispell,english\_stem} | english\_ispell | {bright}
 blank     | Space symbols   |             | {}                            |                |
 asciiword | Word, all ASCII | supernovaes | {english\_ispell,english\_stem} | english\_stem   | {supernova}

In this example, the word `Brightest` was recognized by the parser as an `ASCII word` (alias `asciiword`). For this token type the dictionary list is `english_ispell` and `english_stem`. The word was recognized by `english_ispell`, which reduced it to the noun `bright`. The word `supernovaes` is unknown to the `english_ispell` dictionary so it was passed to the next dictionary, and, fortunately, was recognized (in fact, `english_stem` is a Snowball dictionary which recognizes everything; that is why it was placed at the end of the dictionary list).

The word `The` was recognized by the `english_ispell` dictionary as a stop word ([Section 12.6.1](https://www.postgresql.org/docs/current/textsearch-dictionaries.html#TEXTSEARCH-STOPWORDS "12.6.1. Stop Words")) and will not be indexed. The spaces are discarded too, since the configuration provides no dictionaries at all for them.

You can reduce the width of the output by explicitly specifying which columns you want to see:

SELECT alias, token, dictionary, lexemes
FROM ts\_debug('public.english', 'The Brightest supernovaes');
   alias   |    token    |   dictionary   |   lexemes
-----------+-------------+----------------+-------------
 asciiword | The         | english\_ispell | {}
 blank     |             |                |
 asciiword | Brightest   | english\_ispell | {bright}
 blank     |             |                |
 asciiword | supernovaes | english\_stem   | {supernova}

### 12.8.2. Parser Testing [#](#TEXTSEARCH-PARSER-TESTING)

The following functions allow direct testing of a text search parser.

ts\_parse(_`parser_name`_ `text`, _`document`_ `text`,
         OUT _`tokid`_ `integer`, OUT _`token`_ `text`) returns `setof record`
ts\_parse(_`parser_oid`_ `oid`, _`document`_ `text`,
         OUT _`tokid`_ `integer`, OUT _`token`_ `text`) returns `setof record`

`ts_parse` parses the given _`document`_ and returns a series of records, one for each token produced by parsing. Each record includes a `tokid` showing the assigned token type and a `token` which is the text of the token. For example:

SELECT \* FROM ts\_parse('default', '123 - a number');
 tokid | token
-------+--------
    22 | 123
    12 |
    12 | -
     1 | a
    12 |
     1 | number

ts\_token\_type(_`parser_name`_ `text`, OUT _`tokid`_ `integer`,
              OUT _`alias`_ `text`, OUT _`description`_ `text`) returns `setof record`
ts\_token\_type(_`parser_oid`_ `oid`, OUT _`tokid`_ `integer`,
              OUT _`alias`_ `text`, OUT _`description`_ `text`) returns `setof record`

`ts_token_type` returns a table which describes each type of token the specified parser can recognize. For each token type, the table gives the integer `tokid` that the parser uses to label a token of that type, the `alias` that names the token type in configuration commands, and a short `description`. For example:

SELECT \* FROM ts\_token\_type('default');
 tokid |      alias      |               description
-------+-----------------+------------------------------------------
     1 | asciiword       | Word, all ASCII
     2 | word            | Word, all letters
     3 | numword         | Word, letters and digits
     4 | email           | Email address
     5 | url             | URL
     6 | host            | Host
     7 | sfloat          | Scientific notation
     8 | version         | Version number
     9 | hword\_numpart   | Hyphenated word part, letters and digits
    10 | hword\_part      | Hyphenated word part, all letters
    11 | hword\_asciipart | Hyphenated word part, all ASCII
    12 | blank           | Space symbols
    13 | tag             | XML tag
    14 | protocol        | Protocol head
    15 | numhword        | Hyphenated word, letters and digits
    16 | asciihword      | Hyphenated word, all ASCII
    17 | hword           | Hyphenated word, all letters
    18 | url\_path        | URL path
    19 | file            | File or path name
    20 | float           | Decimal notation
    21 | int             | Signed integer
    22 | uint            | Unsigned integer
    23 | entity          | XML entity

### 12.8.3. Dictionary Testing [#](#TEXTSEARCH-DICTIONARY-TESTING)

The `ts_lexize` function facilitates dictionary testing.

ts\_lexize(_`dict`_ `regdictionary`, _`token`_ `text`) returns `text[]`

`ts_lexize` returns an array of lexemes if the input _`token`_ is known to the dictionary, or an empty array if the token is known to the dictionary but it is a stop word, or `NULL` if it is an unknown word.

Examples:

SELECT ts\_lexize('english\_stem', 'stars');
 ts\_lexize
-----------
 {star}

SELECT ts\_lexize('english\_stem', 'a');
 ts\_lexize
-----------
 {}

### Note

The `ts_lexize` function expects a single _token_, not text. Here is a case where this can be confusing:

SELECT ts\_lexize('thesaurus\_astro', 'supernovae stars') is null;
 ?column?
----------
 t

The thesaurus dictionary `thesaurus_astro` does know the phrase `supernovae stars`, but `ts_lexize` fails since it does not parse the input text but treats it as a single token. Use `plainto_tsquery` or `to_tsvector` to test thesaurus dictionaries, for example:

SELECT plainto\_tsquery('supernovae stars');
 plainto\_tsquery
-----------------
 'sn'


