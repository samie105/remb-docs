---
title: "PostgreSQL: Documentation: 18: 31.3. Variant Comparison Files"
source: "https://www.postgresql.org/docs/current/regress-variant.html"
canonical_url: "https://www.postgresql.org/docs/current/regress-variant.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:49.857Z"
content_hash: "f7c0c3039371976145b50819a60a65f83303f346177308f1218f1a20704ae67c"
menu_path: ["PostgreSQL: Documentation: 18: 31.3. Variant Comparison Files"]
section_path: []
nav_prev: {"path": "postgres/docs/current/infoschema-role-usage-grants.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.39.\u00a0role_usage_grants"}
nav_next: {"path": "postgres/docs/current/pgarchivecleanup.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_archivecleanup"}
---

Since some of the tests inherently produce environment-dependent results, we have provided ways to specify alternate “expected” result files. Each regression test can have several comparison files showing possible results on different platforms. There are two independent mechanisms for determining which comparison file is used for each test.

The first mechanism allows comparison files to be selected for specific platforms. There is a mapping file, `src/test/regress/resultmap`, that defines which comparison file to use for each platform. To eliminate bogus test “failures” for a particular platform, you first choose or make a variant result file, and then add a line to the `resultmap` file.

Each line in the mapping file is of the form

testname:output:platformpattern=comparisonfilename

The test name is just the name of the particular regression test module. The output value indicates which output file to check. For the standard regression tests, this is always `out`. The value corresponds to the file extension of the output file. The platform pattern is a pattern in the style of the Unix tool `expr` (that is, a regular expression with an implicit `^` anchor at the start). It is matched against the platform name as printed by `config.guess`. The comparison file name is the base name of the substitute result comparison file.

For example: some systems lack a working `strtof` function, for which our workaround causes rounding errors in the `float4` regression test. Therefore, we provide a variant comparison file, `float4-misrounded-input.out`, which includes the results to be expected on these systems. To silence the bogus “failure” message on Cygwin platforms, `resultmap` includes:

float4:out:.\*-.\*-cygwin.\*=float4-misrounded-input.out

which will trigger on any machine where the output of `config.guess` matches `.*-.*-cygwin.*`. Other lines in `resultmap` select the variant comparison file for other platforms where it's appropriate.

The second selection mechanism for variant comparison files is much more automatic: it simply uses the “best match” among several supplied comparison files. The regression test driver script considers both the standard comparison file for a test, ``_`testname`_.out``, and variant files named ``_`testname`___`digit`_.out`` (where the _`digit`_ is any single digit `0`\-`9`). If any such file is an exact match, the test is considered to pass; otherwise, the one that generates the shortest diff is used to create the failure report. (If `resultmap` includes an entry for the particular test, then the base _`testname`_ is the substitute name given in `resultmap`.)

For example, for the `char` test, the comparison file `char.out` contains results that are expected in the `C` and `POSIX` locales, while the file `char_1.out` contains results sorted as they appear in many other locales.

The best-match mechanism was devised to cope with locale-dependent results, but it can be used in any situation where the test results cannot be predicted easily from the platform name alone. A limitation of this mechanism is that the test driver cannot tell which variant is actually “correct” for the current environment; it will just pick the variant that seems to work best. Therefore it is safest to use this mechanism only for variant results that you are willing to consider equally valid in all contexts.
