---
title: "PostgreSQL: Documentation: 18: 12.10. psql Support"
source: "https://www.postgresql.org/docs/current/textsearch-psql.html"
canonical_url: "https://www.postgresql.org/docs/current/textsearch-psql.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:36.836Z"
content_hash: "63bdeb170c02f1a40edc24ae4fb77b1eb5faab2535ad8ca3b388a8f8a96054e7"
menu_path: ["PostgreSQL: Documentation: 18: 12.10. psql Support"]
section_path: []
nav_prev: {"path": "../textsearch-parsers.html/index.md", "title": "PostgreSQL: Documentation: 18: 12.5.\u00a0Parsers"}
nav_next: {"path": "../trigger-interface.html/index.md", "title": "PostgreSQL: Documentation: 18: 37.3.\u00a0Writing Trigger Functions in C"}
---

Information about text search configuration objects can be obtained in psql using a set of commands:

\\dF{d,p,t}\[+\] \[PATTERN\]

An optional `+` produces more details.

The optional parameter _`PATTERN`_ can be the name of a text search object, optionally schema-qualified. If _`PATTERN`_ is omitted then information about all visible objects will be displayed. _`PATTERN`_ can be a regular expression and can provide _separate_ patterns for the schema and object names. The following examples illustrate this:

\=> \\dF \*fulltext\*
       List of text search configurations
 Schema |  Name        | Description
--------+--------------+-------------
 public | fulltext\_cfg |

\=> \\dF \*.fulltext\*
       List of text search configurations
 Schema   |  Name        | Description
----------+----------------------------
 fulltext | fulltext\_cfg |
 public   | fulltext\_cfg |

The available commands are:

`\dF[+] [PATTERN]`

List text search configurations (add `+` for more detail).

\=> \\dF russian
            List of text search configurations
   Schema   |  Name   |            Description
------------+---------+------------------------------------
 pg\_catalog | russian | configuration for russian language

=> \\dF+ russian
Text search configuration "pg\_catalog.russian"
Parser: "pg\_catalog.default"
      Token      | Dictionaries
-----------------+--------------
 asciihword      | english\_stem
 asciiword       | english\_stem
 email           | simple
 file            | simple
 float           | simple
 host            | simple
 hword           | russian\_stem
 hword\_asciipart | english\_stem
 hword\_numpart   | simple
 hword\_part      | russian\_stem
 int             | simple
 numhword        | simple
 numword         | simple
 sfloat          | simple
 uint            | simple
 url             | simple
 url\_path        | simple
 version         | simple
 word            | russian\_stem

`\dFd[+] [PATTERN]`

List text search dictionaries (add `+` for more detail).

\=> \\dFd
                             List of text search dictionaries
   Schema   |      Name       |                        Description
------------+-----------------+-----------------------------------------------------------
 pg\_catalog | arabic\_stem     | snowball stemmer for arabic language
 pg\_catalog | armenian\_stem   | snowball stemmer for armenian language
 pg\_catalog | basque\_stem     | snowball stemmer for basque language
 pg\_catalog | catalan\_stem    | snowball stemmer for catalan language
 pg\_catalog | danish\_stem     | snowball stemmer for danish language
 pg\_catalog | dutch\_stem      | snowball stemmer for dutch language
 pg\_catalog | english\_stem    | snowball stemmer for english language
 pg\_catalog | estonian\_stem   | snowball stemmer for estonian language
 pg\_catalog | finnish\_stem    | snowball stemmer for finnish language
 pg\_catalog | french\_stem     | snowball stemmer for french language
 pg\_catalog | german\_stem     | snowball stemmer for german language
 pg\_catalog | greek\_stem      | snowball stemmer for greek language
 pg\_catalog | hindi\_stem      | snowball stemmer for hindi language
 pg\_catalog | hungarian\_stem  | snowball stemmer for hungarian language
 pg\_catalog | indonesian\_stem | snowball stemmer for indonesian language
 pg\_catalog | irish\_stem      | snowball stemmer for irish language
 pg\_catalog | italian\_stem    | snowball stemmer for italian language
 pg\_catalog | lithuanian\_stem | snowball stemmer for lithuanian language
 pg\_catalog | nepali\_stem     | snowball stemmer for nepali language
 pg\_catalog | norwegian\_stem  | snowball stemmer for norwegian language
 pg\_catalog | portuguese\_stem | snowball stemmer for portuguese language
 pg\_catalog | romanian\_stem   | snowball stemmer for romanian language
 pg\_catalog | russian\_stem    | snowball stemmer for russian language
 pg\_catalog | serbian\_stem    | snowball stemmer for serbian language
 pg\_catalog | simple          | simple dictionary: just lower case and check for stopword
 pg\_catalog | spanish\_stem    | snowball stemmer for spanish language
 pg\_catalog | swedish\_stem    | snowball stemmer for swedish language
 pg\_catalog | tamil\_stem      | snowball stemmer for tamil language
 pg\_catalog | turkish\_stem    | snowball stemmer for turkish language
 pg\_catalog | yiddish\_stem    | snowball stemmer for yiddish language

`\dFp[+] [PATTERN]`

List text search parsers (add `+` for more detail).

\=> \\dFp
        List of text search parsers
   Schema   |  Name   |     Description
------------+---------+---------------------
 pg\_catalog | default | default word parser
=> \\dFp+
    Text search parser "pg\_catalog.default"
     Method      |    Function    | Description
-----------------+----------------+-------------
 Start parse     | prsd\_start     |
 Get next token  | prsd\_nexttoken |
 End parse       | prsd\_end       |
 Get headline    | prsd\_headline  |
 Get token types | prsd\_lextype   |

        Token types for parser "pg\_catalog.default"
   Token name    |               Description
-----------------+------------------------------------------
 asciihword      | Hyphenated word, all ASCII
 asciiword       | Word, all ASCII
 blank           | Space symbols
 email           | Email address
 entity          | XML entity
 file            | File or path name
 float           | Decimal notation
 host            | Host
 hword           | Hyphenated word, all letters
 hword\_asciipart | Hyphenated word part, all ASCII
 hword\_numpart   | Hyphenated word part, letters and digits
 hword\_part      | Hyphenated word part, all letters
 int             | Signed integer
 numhword        | Hyphenated word, letters and digits
 numword         | Word, letters and digits
 protocol        | Protocol head
 sfloat          | Scientific notation
 tag             | XML tag
 uint            | Unsigned integer
 url             | URL
 url\_path        | URL path
 version         | Version number
 word            | Word, all letters
(23 rows)

`\dFt[+] [PATTERN]`

List text search templates (add `+` for more detail).

\=> \\dFt
                           List of text search templates
   Schema   |   Name    |                        Description
------------+-----------+-----------------------------------------------------------
 pg\_catalog | ispell    | ispell dictionary
 pg\_catalog | simple    | simple dictionary: just lower case and check for stopword
 pg\_catalog | snowball  | snowball stemmer
 pg\_catalog | synonym   | synonym dictionary: replace word by its synonym
 pg\_catalog | thesaurus | thesaurus dictionary: phrase by phrase substitution
