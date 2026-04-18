---
title: "PostgreSQL: Documentation: 18: Chapter 44. PL/Python — Python Procedural Language"
source: "https://www.postgresql.org/docs/current/plpython.html"
canonical_url: "https://www.postgresql.org/docs/current/plpython.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:39.730Z"
content_hash: "c125789e5018d3ac0344af231af164b649ff83c08f5a3ab42bfb86358eaecd46"
menu_path: ["PostgreSQL: Documentation: 18: Chapter 44. PL/Python — Python Procedural Language"]
section_path: []
---
The PL/Python procedural language allows PostgreSQL functions and procedures to be written in the [Python language](https://www.python.org/).

To install PL/Python in a particular database, use `CREATE EXTENSION plpython3u`.

### Tip

If a language is installed into `template1`, all subsequently created databases will have the language installed automatically.

PL/Python is only available as an “untrusted” language, meaning it does not offer any way of restricting what users can do in it and is therefore named `plpython3u`. A trusted variant `plpython` might become available in the future if a secure execution mechanism is developed in Python. The writer of a function in untrusted PL/Python must take care that the function cannot be used to do anything unwanted, since it will be able to do anything that could be done by a user logged in as the database administrator. Only superusers can create functions in untrusted languages such as `plpython3u`.

### Note

Users of source packages must specially enable the build of PL/Python during the installation process. (Refer to the installation instructions for more information.) Users of binary packages might find PL/Python in a separate subpackage.
