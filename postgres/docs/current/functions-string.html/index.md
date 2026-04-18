---
title: "PostgreSQL: Documentation: 18: 9.4. String Functions and Operators"
source: "https://www.postgresql.org/docs/current/functions-string.html"
canonical_url: "https://www.postgresql.org/docs/current/functions-string.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:44.216Z"
content_hash: "524aad3d43ca18d3d667be8fe7c9123d37eeca2fc6a9e4b3caefb1df2c265d5b"
menu_path: ["PostgreSQL: Documentation: 18: 9.4. String Functions and Operators"]
section_path: []
---
`text` `^@` `text` → `boolean`

Returns true if the first string starts with the second string (equivalent to the `starts_with()` function).

`'alphabet' ^@ 'alph'` → `t`

`ascii` ( `text` ) → `integer`

Returns the numeric code of the first character of the argument. In UTF8 encoding, returns the Unicode code point of the character. In other multibyte encodings, the argument must be an ASCII character.

`ascii('x')` → `120`

`chr` ( `integer` ) → `text`

Returns the character with the given code. In UTF8 encoding the argument is treated as a Unicode code point. In other multibyte encodings the argument must designate an ASCII character. `chr(0)` is disallowed because text data types cannot store that character.

`chr(65)` → `A`

`concat` ( _`val1`_ `"any"` \[, _`val2`_ `"any"` \[, ...\] \] ) → `text`

Concatenates the text representations of all the arguments. NULL arguments are ignored.

`concat('abcde', 2, NULL, 22)` → `abcde222`

`concat_ws` ( _`sep`_ `text`, _`val1`_ `"any"` \[, _`val2`_ `"any"` \[, ...\] \] ) → `text`

Concatenates all but the first argument, with separators. The first argument is used as the separator string, and should not be NULL. Other NULL arguments are ignored.

`concat_ws(',', 'abcde', 2, NULL, 22)` → `abcde,2,22`

`format` ( _`formatstr`_ `text` \[, _`formatarg`_ `"any"` \[, ...\] \] ) → `text`

Formats arguments according to a format string; see [Section 9.4.1](https://www.postgresql.org/docs/current/functions-string.html#FUNCTIONS-STRING-FORMAT "9.4.1. format"). This function is similar to the C function `sprintf`.

`format('Hello %s, %1$s', 'World')` → `Hello World, World`

`initcap` ( `text` ) → `text`

Converts the first letter of each word to upper case and the rest to lower case. Words are sequences of alphanumeric characters separated by non-alphanumeric characters.

`initcap('hi THOMAS')` → `Hi Thomas`

`casefold` ( `text` ) → `text`

Performs case folding of the input string according to the collation. Case folding is similar to case conversion, but the purpose of case folding is to facilitate case-insensitive matching of strings, whereas the purpose of case conversion is to convert to a particular cased form. This function can only be used when the server encoding is `UTF8`.

Ordinarily, case folding simply converts to lowercase, but there may be exceptions depending on the collation. For instance, some characters have more than two lowercase variants, or fold to uppercase.

Case folding may change the length of the string. For instance, in the `PG_UNICODE_FAST` collation, `ß` (U+00DF) folds to `ss`.

`casefold` can be used for Unicode Default Caseless Matching. It does not always preserve the normalized form of the input string (see [normalize](https://www.postgresql.org/docs/current/functions-string.html#FUNCTION-NORMALIZE)).

The `libc` provider doesn't support case folding, so `casefold` is identical to [lower](https://www.postgresql.org/docs/current/functions-string.html#FUNCTION-LOWER).

`left` ( _`string`_ `text`, _`n`_ `integer` ) → `text`

Returns first _`n`_ characters in the string, or when _`n`_ is negative, returns all but last |_`n`_| characters.

`left('abcde', 2)` → `ab`

`length` ( `text` ) → `integer`

Returns the number of characters in the string.

`length('jose')` → `4`

`md5` ( `text` ) → `text`

Computes the MD5 [hash](https://www.postgresql.org/docs/current/functions-binarystring.html#FUNCTIONS-HASH-NOTE) of the argument, with the result written in hexadecimal.

`md5('abc')` → `900150983cd24fb0​d6963f7d28e17f72`

`parse_ident` ( _`qualified_identifier`_ `text` \[, _`strict_mode`_ `boolean` `DEFAULT` `true` \] ) → `text[]`

Splits _`qualified_identifier`_ into an array of identifiers, removing any quoting of individual identifiers. By default, extra characters after the last identifier are considered an error; but if the second parameter is `false`, then such extra characters are ignored. (This behavior is useful for parsing names for objects like functions.) Note that this function does not truncate over-length identifiers. If you want truncation you can cast the result to `name[]`.

`parse_ident('"SomeSchema".someTable')` → `{SomeSchema,sometable}`

`pg_client_encoding` ( ) → `name`

Returns current client encoding name.

`pg_client_encoding()` → `UTF8`

`quote_ident` ( `text` ) → `text`

Returns the given string suitably quoted to be used as an identifier in an SQL statement string. Quotes are added only if necessary (i.e., if the string contains non-identifier characters or would be case-folded). Embedded quotes are properly doubled. See also [Example 41.1](https://www.postgresql.org/docs/current/plpgsql-statements.html#PLPGSQL-QUOTE-LITERAL-EXAMPLE "Example 41.1. Quoting Values in Dynamic Queries").

`quote_ident('Foo bar')` → `"Foo bar"`

`quote_literal` ( `text` ) → `text`

Returns the given string suitably quoted to be used as a string literal in an SQL statement string. Embedded single-quotes and backslashes are properly doubled. Note that `quote_literal` returns null on null input; if the argument might be null, `quote_nullable` is often more suitable. See also [Example 41.1](https://www.postgresql.org/docs/current/plpgsql-statements.html#PLPGSQL-QUOTE-LITERAL-EXAMPLE "Example 41.1. Quoting Values in Dynamic Queries").

`quote_literal(E'O\'Reilly')` → `'O''Reilly'`

`quote_literal` ( `anyelement` ) → `text`

Converts the given value to text and then quotes it as a literal. Embedded single-quotes and backslashes are properly doubled.

`quote_literal(42.5)` → `'42.5'`

`quote_nullable` ( `text` ) → `text`

Returns the given string suitably quoted to be used as a string literal in an SQL statement string; or, if the argument is null, returns `NULL`. Embedded single-quotes and backslashes are properly doubled. See also [Example 41.1](https://www.postgresql.org/docs/current/plpgsql-statements.html#PLPGSQL-QUOTE-LITERAL-EXAMPLE "Example 41.1. Quoting Values in Dynamic Queries").

`quote_nullable(NULL)` → `NULL`

`quote_nullable` ( `anyelement` ) → `text`

Converts the given value to text and then quotes it as a literal; or, if the argument is null, returns `NULL`. Embedded single-quotes and backslashes are properly doubled.

`quote_nullable(42.5)` → `'42.5'`

`regexp_count` ( _`string`_ `text`, _`pattern`_ `text` \[, _`start`_ `integer` \[, _`flags`_ `text` \] \] ) → `integer`

Returns the number of times the POSIX regular expression _`pattern`_ matches in the _`string`_; see [Section 9.7.3](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP "9.7.3. POSIX Regular Expressions").

`regexp_count('123456789012', '\d\d\d', 2)` → `3`

`regexp_instr` ( _`string`_ `text`, _`pattern`_ `text` \[, _`start`_ `integer` \[, _`N`_ `integer` \[, _`endoption`_ `integer` \[, _`flags`_ `text` \[, _`subexpr`_ `integer` \] \] \] \] \] ) → `integer`

Returns the position within _`string`_ where the _`N`_'th match of the POSIX regular expression _`pattern`_ occurs, or zero if there is no such match; see [Section 9.7.3](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP "9.7.3. POSIX Regular Expressions").

`regexp_instr('ABCDEF', 'c(.)(..)', 1, 1, 0, 'i')` → `3`

`regexp_instr('ABCDEF', 'c(.)(..)', 1, 1, 0, 'i', 2)` → `5`

`regexp_like` ( _`string`_ `text`, _`pattern`_ `text` \[, _`flags`_ `text` \] ) → `boolean`

Checks whether a match of the POSIX regular expression _`pattern`_ occurs within _`string`_; see [Section 9.7.3](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP "9.7.3. POSIX Regular Expressions").

`regexp_like('Hello World', 'world$', 'i')` → `t`

`regexp_match` ( _`string`_ `text`, _`pattern`_ `text` \[, _`flags`_ `text` \] ) → `text[]`

Returns substrings within the first match of the POSIX regular expression _`pattern`_ to the _`string`_; see [Section 9.7.3](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP "9.7.3. POSIX Regular Expressions").

`regexp_match('foobarbequebaz', '(bar)(beque)')` → `{bar,beque}`

`regexp_matches` ( _`string`_ `text`, _`pattern`_ `text` \[, _`flags`_ `text` \] ) → `setof text[]`

Returns substrings within the first match of the POSIX regular expression _`pattern`_ to the _`string`_, or substrings within all such matches if the `g` flag is used; see [Section 9.7.3](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP "9.7.3. POSIX Regular Expressions").

`regexp_matches('foobarbequebaz', 'ba.', 'g')` →

 {bar}
 {baz}

`regexp_replace` ( _`string`_ `text`, _`pattern`_ `text`, _`replacement`_ `text` \[, _`flags`_ `text` \] ) → `text`

Replaces the substring that is the first match to the POSIX regular expression _`pattern`_, or all such matches if the `g` flag is used; see [Section 9.7.3](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP "9.7.3. POSIX Regular Expressions").

`regexp_replace('Thomas', '.[mN]a.', 'M')` → `ThM`

`regexp_replace` ( _`string`_ `text`, _`pattern`_ `text`, _`replacement`_ `text`, _`start`_ `integer` \[, _`N`_ `integer` \[, _`flags`_ `text` \] \] ) → `text`

Replaces the substring that is the _`N`_'th match to the POSIX regular expression _`pattern`_, or all such matches if _`N`_ is zero, with the search beginning at the _`start`_'th character of _`string`_. If _`N`_ is omitted, it defaults to 1. See [Section 9.7.3](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP "9.7.3. POSIX Regular Expressions").

`regexp_replace('Thomas', '.', 'X', 3, 2)` → `ThoXas`

`regexp_replace(string=>'hello world', pattern=>'l', replacement=>'XX', start=>1, "N"=>2)` → `helXXo world`

`regexp_split_to_array` ( _`string`_ `text`, _`pattern`_ `text` \[, _`flags`_ `text` \] ) → `text[]`

Splits _`string`_ using a POSIX regular expression as the delimiter, producing an array of results; see [Section 9.7.3](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP "9.7.3. POSIX Regular Expressions").

`regexp_split_to_array('hello world', '\s+')` → `{hello,world}`

`regexp_split_to_table` ( _`string`_ `text`, _`pattern`_ `text` \[, _`flags`_ `text` \] ) → `setof text`

Splits _`string`_ using a POSIX regular expression as the delimiter, producing a set of results; see [Section 9.7.3](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP "9.7.3. POSIX Regular Expressions").

`regexp_split_to_table('hello world', '\s+')` →

 hello
 world

`regexp_substr` ( _`string`_ `text`, _`pattern`_ `text` \[, _`start`_ `integer` \[, _`N`_ `integer` \[, _`flags`_ `text` \[, _`subexpr`_ `integer` \] \] \] \] ) → `text`

Returns the substring within _`string`_ that matches the _`N`_'th occurrence of the POSIX regular expression _`pattern`_, or `NULL` if there is no such match; see [Section 9.7.3](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP "9.7.3. POSIX Regular Expressions").

`regexp_substr('ABCDEF', 'c(.)(..)', 1, 1, 'i')` → `CDEF`

`regexp_substr('ABCDEF', 'c(.)(..)', 1, 1, 'i', 2)` → `EF`

`repeat` ( _`string`_ `text`, _`number`_ `integer` ) → `text`

Repeats _`string`_ the specified _`number`_ of times.

`repeat('Pg', 4)` → `PgPgPgPg`

`replace` ( _`string`_ `text`, _`from`_ `text`, _`to`_ `text` ) → `text`

Replaces all occurrences in _`string`_ of substring _`from`_ with substring _`to`_.

`replace('abcdefabcdef', 'cd', 'XX')` → `abXXefabXXef`

`reverse` ( `text` ) → `text`

Reverses the order of the characters in the string.

`reverse('abcde')` → `edcba`

`right` ( _`string`_ `text`, _`n`_ `integer` ) → `text`

Returns last _`n`_ characters in the string, or when _`n`_ is negative, returns all but first |_`n`_| characters.

`right('abcde', 2)` → `de`

`split_part` ( _`string`_ `text`, _`delimiter`_ `text`, _`n`_ `integer` ) → `text`

Splits _`string`_ at occurrences of _`delimiter`_ and returns the _`n`_'th field (counting from one), or when _`n`_ is negative, returns the |_`n`_|'th-from-last field.

`split_part('abc~@~def~@~ghi', '~@~', 2)` → `def`

`split_part('abc,def,ghi,jkl', ',', -2)` → `ghi`

`starts_with` ( _`string`_ `text`, _`prefix`_ `text` ) → `boolean`

Returns true if _`string`_ starts with _`prefix`_.

`starts_with('alphabet', 'alph')` → `t`

`string_to_array` ( _`string`_ `text`, _`delimiter`_ `text` \[, _`null_string`_ `text` \] ) → `text[]`

Splits the _`string`_ at occurrences of _`delimiter`_ and forms the resulting fields into a `text` array. If _`delimiter`_ is `NULL`, each character in the _`string`_ will become a separate element in the array. If _`delimiter`_ is an empty string, then the _`string`_ is treated as a single field. If _`null_string`_ is supplied and is not `NULL`, fields matching that string are replaced by `NULL`. See also [`array_to_string`](https://www.postgresql.org/docs/current/functions-array.html#FUNCTION-ARRAY-TO-STRING).

`string_to_array('xx~~yy~~zz', '~~', 'yy')` → `{xx,NULL,zz}`

`string_to_table` ( _`string`_ `text`, _`delimiter`_ `text` \[, _`null_string`_ `text` \] ) → `setof text`

Splits the _`string`_ at occurrences of _`delimiter`_ and returns the resulting fields as a set of `text` rows. If _`delimiter`_ is `NULL`, each character in the _`string`_ will become a separate row of the result. If _`delimiter`_ is an empty string, then the _`string`_ is treated as a single field. If _`null_string`_ is supplied and is not `NULL`, fields matching that string are replaced by `NULL`.

`string_to_table('xx~^~yy~^~zz', '~^~', 'yy')` →

 xx
 NULL
 zz

`strpos` ( _`string`_ `text`, _`substring`_ `text` ) → `integer`

Returns first starting index of the specified _`substring`_ within _`string`_, or zero if it's not present. (Same as ``position(_`substring`_ in _`string`_)``, but note the reversed argument order.)

`strpos('high', 'ig')` → `2`

`substr` ( _`string`_ `text`, _`start`_ `integer` \[, _`count`_ `integer` \] ) → `text`

Extracts the substring of _`string`_ starting at the _`start`_'th character, and extending for _`count`_ characters if that is specified. (Same as ``substring(_`string`_ from _`start`_ for _`count`_)``.)

`substr('alphabet', 3)` → `phabet`

`substr('alphabet', 3, 2)` → `ph`

`to_ascii` ( _`string`_ `text` ) → `text`

`to_ascii` ( _`string`_ `text`, _`encoding`_ `name` ) → `text`

`to_ascii` ( _`string`_ `text`, _`encoding`_ `integer` ) → `text`

Converts _`string`_ to ASCII from another encoding, which may be identified by name or number. If _`encoding`_ is omitted the database encoding is assumed (which in practice is the only useful case). The conversion consists primarily of dropping accents. Conversion is only supported from `LATIN1`, `LATIN2`, `LATIN9`, and `WIN1250` encodings. (See the [unaccent](https://www.postgresql.org/docs/current/unaccent.html "F.48. unaccent — a text search dictionary which removes diacritics") module for another, more flexible solution.)

`to_ascii('Karél')` → `Karel`

`to_bin` ( `integer` ) → `text`

`to_bin` ( `bigint` ) → `text`

Converts the number to its equivalent two's complement binary representation.

`to_bin(2147483647)` → `1111111111111111111111111111111`

`to_bin(-1234)` → `11111111111111111111101100101110`

`to_hex` ( `integer` ) → `text`

`to_hex` ( `bigint` ) → `text`

Converts the number to its equivalent two's complement hexadecimal representation.

`to_hex(2147483647)` → `7fffffff`

`to_hex(-1234)` → `fffffb2e`

`to_oct` ( `integer` ) → `text`

`to_oct` ( `bigint` ) → `text`

Converts the number to its equivalent two's complement octal representation.

`to_oct(2147483647)` → `17777777777`

`to_oct(-1234)` → `37777775456`

`translate` ( _`string`_ `text`, _`from`_ `text`, _`to`_ `text` ) → `text`

Replaces each character in _`string`_ that matches a character in the _`from`_ set with the corresponding character in the _`to`_ set. If _`from`_ is longer than _`to`_, occurrences of the extra characters in _`from`_ are deleted.

`translate('12345', '143', 'ax')` → `a2x5`

`unistr` ( `text` ) → `text`

Evaluate escaped Unicode characters in the argument. Unicode characters can be specified as ``\_`XXXX`_`` (4 hexadecimal digits), ``\+_`XXXXXX`_`` (6 hexadecimal digits), ``\u_`XXXX`_`` (4 hexadecimal digits), or ``\U_`XXXXXXXX`_`` (8 hexadecimal digits). To specify a backslash, write two backslashes. All other characters are taken literally.

If the server encoding is not UTF-8, the Unicode code point identified by one of these escape sequences is converted to the actual server encoding; an error is reported if that's not possible.

This function provides a (non-standard) alternative to string constants with Unicode escapes (see [Section 4.1.2.3](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-STRINGS-UESCAPE "4.1.2.3. String Constants with Unicode Escapes")).

`unistr('d\0061t\+000061')` → `data`

`unistr('d\u0061t\U00000061')` → `data`
