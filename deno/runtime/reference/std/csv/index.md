---
title: "@std/csv"
source: "https://docs.deno.com/runtime/reference/std/csv/"
canonical_url: "https://docs.deno.com/runtime/reference/std/csv/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:40:39.142Z"
content_hash: "5fe6c253df4d3ac07dcfd6b95c128fa64ba3277671e42c3937d49f3c407797ac"
menu_path: ["@std/csv"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/std/crypto/index.md", "title": "@std/crypto"}
nav_next: {"path": "deno/runtime/reference/std/data-structures/index.md", "title": "@std/data-structures"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

## Overview

Reads and writes comma-separated values (CSV) files.

## Parsing CSV

```js
import { parse } from "@std/csv/parse";
import { assertEquals } from "@std/assert";

const string = "a,b,c\nd,e,f";

// Parse as array of arrays (default)
assertEquals(parse(string, { skipFirstRow: false }), [["a", "b", "c"], ["d", "e", "f"]]);

// Parse csv file with headers into array of objects
assertEquals(parse(string, { skipFirstRow: true }), [{ a: "d", b: "e", c: "f" }]);

// Parse with custom column names
assertEquals(parse(string, { columns: ["x", "y", "z"] }), [
  { x: "a", y: "b", z: "c" },
  { x: "d", y: "e", z: "f" }
]);

// Parse tab-separated values
const tsvString = "name\tage\tcity\njohn\t30\tnew york\nmary\t25\tlos angeles";
assertEquals(parse(tsvString, { separator: "\t", skipFirstRow: true }), [
  { name: "john", age: "30", city: "new york" },
  { name: "mary", age: "25", city: "los angeles" }
]);

// Parse a CSV file which has comments
const csvWithComments = "# This is a comment\nname,age,city\n# Another comment\njohn,30,new york\nmary,25,los angeles";
assertEquals(parse(csvWithComments, { comment: "#", skipFirstRow: true }), [
  { name: "john", age: "30", city: "new york" },
  { name: "mary", age: "25", city: "los angeles" }
]);
```

## Parsing CSV from a Stream

```js
import { CsvParseStream } from "@std/csv/parse-stream";
import { assertEquals } from "@std/assert";

// Parse from a stream (useful for large files)
const source = ReadableStream.from([
  "name,age,city\n",
  "john,30,new york\n",
  "mary,25,los angeles\n"
]);

const csvStream = source
  .pipeThrough(new CsvParseStream({ skipFirstRow: true }));

const records = await Array.fromAsync(csvStream);
assertEquals(records, [
  { name: "john", age: "30", city: "new york" },
  { name: "mary", age: "25", city: "los angeles" }
]);

// Or process records one by one
// for await (const record of csvStream) {
//   console.log(record);
// }
```

## Stringifying Data to CSV

```js
import { stringify } from "@std/csv/stringify";
import { assertEquals } from "@std/assert";

// Convert array of arrays to CSV
const arrayData = [["name", "age", "city"], ["john", "30", "new york"], ["mary", "25", "los angeles"]];
const csvString = stringify(arrayData);
assertEquals(csvString, "name,age,city\r\njohn,30,new york\r\nmary,25,los angeles\r\n");

// Convert array of objects to CSV
const objectData = [
  { name: "john", age: "30", city: "new york" },
  { name: "mary", age: "25", city: "los angeles" }
];

// When using an array of objects, you must specify columns to use
const customColumns = stringify(objectData, { columns: ["city", "name", "age"] });
assertEquals(customColumns, "city,name,age\r\nnew york,john,30\r\nlos angeles,mary,25\r\n");
```

## Streaming Stringify Data to CSV

```js
import { CsvStringifyStream } from "@std/csv/stringify-stream";
import { assertEquals } from "@std/assert";

async function writeCsvToTempFile(): Promise<string> {
  const path = await Deno.makeTempFile();
  using file = await Deno.open(path, { write: true });

  const readable = ReadableStream.from([
    { id: 1, name: "one" },
    { id: 2, name: "two" },
    { id: 3, name: "three" },
  ]);

  await readable
    .pipeThrough(new CsvStringifyStream({ columns: ["id", "name"] }))
    .pipeThrough(new TextEncoderStream())
    .pipeTo(file.writable);

  return path;
}

const path = await writeCsvToTempFile();
const content = await Deno.readTextFile(path);
assertEquals(content, "id,name\r\n1,one\r\n2,two\r\n3,three\r\n");
```

## CSV Format Information

There are many kinds of CSV files; this module supports the format described in [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180.html).

A csv file contains zero or more records of one or more fields per record. Each record is separated by the newline character. The final record may optionally be followed by a newline character.

```js
field1,field2,field3
```

White space is considered part of a field.

Carriage returns before newline characters are silently removed.

Blank lines are ignored. A line with only whitespace characters (excluding the ending newline character) is not considered a blank line.

Fields which start and stop with the quote character " are called quoted-fields. The beginning and ending quote are not part of the field.

The source:

```js
normal string,"quoted-field"
```

results in the fields

```js
[`normal string`, `quoted-field`]
```

Within a quoted-field a quote character followed by a second quote character is considered a single quote.

```js
"the ""word"" is true","a ""quoted-field"""
```

results in

```js
[`the "word" is true`, `a "quoted-field"`]
```

Newlines and commas may be included in a quoted-field

```js
"Multi-line
field","comma is ,"
```

results in

```js
[`Multi-line
field`, `comma is ,`]
```

### Add to your project

\>\_

```sh
deno add jsr:@std/csv
```

[See all symbols in @std/csv on](https://jsr.io/@std/csv/doc)
