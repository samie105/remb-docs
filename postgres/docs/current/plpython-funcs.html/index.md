---
title: "PostgreSQL: Documentation: 18: 44.1. PL/Python Functions"
source: "https://www.postgresql.org/docs/current/plpython-funcs.html"
canonical_url: "https://www.postgresql.org/docs/current/plpython-funcs.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:46.278Z"
content_hash: "64bce663ed52ef3aca94cb459ff666004f82bf62fc66dcaf3b1f6ba317e54652"
menu_path: ["PostgreSQL: Documentation: 18: 44.1. PL/Python Functions"]
section_path: []
nav_prev: {"path": "postgres/docs/current/server-start.html/index.md", "title": "PostgreSQL: Documentation: 18: 18.3.\u00a0Starting the Database Server"}
nav_next: {"path": "postgres/docs/current/sql-dropdatabase.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP DATABASE"}
---

Functions in PL/Python are declared via the standard [CREATE FUNCTION](https://www.postgresql.org/docs/current/sql-createfunction.html "CREATE FUNCTION") syntax:

CREATE FUNCTION _`funcname`_ (_`argument-list`_)
  RETURNS _`return-type`_
AS $$
  # PL/Python function body
$$ LANGUAGE plpython3u;

The body of a function is simply a Python script. When the function is called, its arguments are passed as elements of the list `args`; named arguments are also passed as ordinary variables to the Python script. Use of named arguments is usually more readable. The result is returned from the Python code in the usual way, with `return` or `yield` (in case of a result-set statement). If you do not provide a return value, Python returns the default `None`. PL/Python translates Python's `None` into the SQL null value. In a procedure, the result from the Python code must be `None` (typically achieved by ending the procedure without a `return` statement or by using a `return` statement without argument); otherwise, an error will be raised.

For example, a function to return the greater of two integers can be defined as:

CREATE FUNCTION pymax (a integer, b integer)
  RETURNS integer
AS $$
  if a > b:
    return a
  return b
$$ LANGUAGE plpython3u;

The Python code that is given as the body of the function definition is transformed into a Python function. For example, the above results in:

def \_\_plpython\_procedure\_pymax\_23456():
  if a > b:
    return a
  return b

assuming that 23456 is the OID assigned to the function by PostgreSQL.

The arguments are set as global variables. Because of the scoping rules of Python, this has the subtle consequence that an argument variable cannot be reassigned inside the function to the value of an expression that involves the variable name itself, unless the variable is redeclared as global in the block. For example, the following won't work:

CREATE FUNCTION pystrip(x text)
  RETURNS text
AS $$
  x = x.strip()  # error
  return x
$$ LANGUAGE plpython3u;

because assigning to `x` makes `x` a local variable for the entire block, and so the `x` on the right-hand side of the assignment refers to a not-yet-assigned local variable `x`, not the PL/Python function parameter. Using the `global` statement, this can be made to work:

CREATE FUNCTION pystrip(x text)
  RETURNS text
AS $$
  global x
  x = x.strip()  # ok now
  return x
$$ LANGUAGE plpython3u;

But it is advisable not to rely on this implementation detail of PL/Python. It is better to treat the function parameters as read-only.


