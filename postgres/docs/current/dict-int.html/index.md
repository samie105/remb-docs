---
title: "PostgreSQL: Documentation: 18: F.12. dict_int — example full-text search dictionary for integers"
source: "https://www.postgresql.org/docs/current/dict-int.html"
canonical_url: "https://www.postgresql.org/docs/current/dict-int.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:42:19.319Z"
content_hash: "58c7f34b3567047f74743cf2b794a801545f424751a68dfc4288e8642deb22fe"
menu_path: ["PostgreSQL: Documentation: 18: F.12. dict_int — example full-text search dictionary for integers"]
section_path: []
content_language: "en"
nav_prev: {"path": "../default-roles.html/index.md", "title": "PostgreSQL: Documentation: 18: O.2.\u00a0Default Roles Renamed to Predefined Roles"}
nav_next: {"path": "../docguide-style.html/index.md", "title": "PostgreSQL: Documentation: 18: J.6.\u00a0Style Guide"}
---

`dict_int` is an example of an add-on dictionary template for full-text search. The motivation for this example dictionary is to control the indexing of integers (signed and unsigned), allowing such numbers to be indexed while preventing excessive growth in the number of unique words, which greatly affects the performance of searching.

This module is considered “trusted”, that is, it can be installed by non-superusers who have `CREATE` privilege on the current database.

### F.12.1. Configuration [#](#DICT-INT-CONFIG)

The dictionary accepts three options:

-   The `maxlen` parameter specifies the maximum number of digits allowed in an integer word. The default value is 6.
    
-   The `rejectlong` parameter specifies whether an overlength integer should be truncated or ignored. If `rejectlong` is `false` (the default), the dictionary returns the first `maxlen` digits of the integer. If `rejectlong` is `true`, the dictionary treats an overlength integer as a stop word, so that it will not be indexed. Note that this also means that such an integer cannot be searched for.
    
-   The `absval` parameter specifies whether leading “`+`” or “`-`” signs should be removed from integer words. The default is `false`. When `true`, the sign is removed before `maxlen` is applied.
    

### F.12.2. Usage [#](#DICT-INT-USAGE)

Installing the `dict_int` extension creates a text search template `intdict_template` and a dictionary `intdict` based on it, with the default parameters. You can alter the parameters, for example

mydb# ALTER TEXT SEARCH DICTIONARY intdict (MAXLEN = 4, REJECTLONG = true);
ALTER TEXT SEARCH DICTIONARY

or create new dictionaries based on the template.

To test the dictionary, you can try

mydb# select ts\_lexize('intdict', '12345678');
 ts\_lexize
-----------
 {123456}

but real-world usage will involve including it in a text search configuration as described in [Chapter 12](https://www.postgresql.org/docs/current/textsearch.html "Chapter 12. Full Text Search"). That might look like this:

ALTER TEXT SEARCH CONFIGURATION english
    ALTER MAPPING FOR int, uint WITH intdict;
