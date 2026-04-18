---
title: "PostgreSQL: Documentation: 18: 41.9. Errors and Messages"
source: "https://www.postgresql.org/docs/current/plpgsql-errors-and-messages.html"
canonical_url: "https://www.postgresql.org/docs/current/plpgsql-errors-and-messages.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:59.708Z"
content_hash: "f6a267ecc2653b75bcd53d63ca282e2ea1714aed76c51f2677e32dbf5386c982"
menu_path: ["PostgreSQL: Documentation: 18: 41.9. Errors and Messages"]
section_path: []
nav_prev: {"path": "postgres/docs/current/infoschema-foreign-servers.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.29.\u00a0foreign_servers"}
nav_next: {"path": "postgres/docs/current/lo-funcs.html/index.md", "title": "PostgreSQL: Documentation: 18: 33.4.\u00a0Server-Side Functions"}
---

### 41.9.1. Reporting Errors and Messages [#](#PLPGSQL-STATEMENTS-RAISE)

Use the `RAISE` statement to report messages and raise errors.

RAISE \[ _`level`_ \] '_`format`_' \[, _`expression`_ \[, ... \]\] \[ USING _`option`_ { = | := } _`expression`_ \[, ... \] \];
RAISE \[ _`level`_ \] _`condition_name`_ \[ USING _`option`_ { = | := } _`expression`_ \[, ... \] \];
RAISE \[ _`level`_ \] SQLSTATE '_`sqlstate`_' \[ USING _`option`_ { = | := } _`expression`_ \[, ... \] \];
RAISE \[ _`level`_ \] USING _`option`_ { = | := } _`expression`_ \[, ... \];
RAISE ;

The _`level`_ option specifies the error severity. Allowed levels are `DEBUG`, `LOG`, `INFO`, `NOTICE`, `WARNING`, and `EXCEPTION`, with `EXCEPTION` being the default. `EXCEPTION` raises an error (which normally aborts the current transaction); the other levels only generate messages of different priority levels. Whether messages of a particular priority are reported to the client, written to the server log, or both is controlled by the [log\_min\_messages](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-MIN-MESSAGES) and [client\_min\_messages](postgres/docs/current/runtime-config-client.html/index.md#GUC-CLIENT-MIN-MESSAGES) configuration variables. See [Chapter 19](https://www.postgresql.org/docs/current/runtime-config.html "Chapter 19. Server Configuration") for more information.

In the first syntax variant, after the _`level`_ if any, write a _`format`_ string (which must be a simple string literal, not an expression). The format string specifies the error message text to be reported. The format string can be followed by optional argument expressions to be inserted into the message. Inside the format string, `%` is replaced by the string representation of the next optional argument's value. Write `%%` to emit a literal `%`. The number of arguments must match the number of `%` placeholders in the format string, or an error is raised during the compilation of the function.

In this example, the value of `v_job_id` will replace the `%` in the string:

RAISE NOTICE 'Calling cs\_create\_job(%)', v\_job\_id;

In the second and third syntax variants, _`condition_name`_ and _`sqlstate`_ specify an error condition name or a five-character SQLSTATE code, respectively. See [Appendix A](https://www.postgresql.org/docs/current/errcodes-appendix.html "Appendix A. PostgreSQL Error Codes") for the valid error condition names and the predefined SQLSTATE codes.

Here are examples of _`condition_name`_ and _`sqlstate`_ usage:

RAISE division\_by\_zero;
RAISE WARNING SQLSTATE '22012';

In any of these syntax variants, you can attach additional information to the error report by writing `USING` followed by _`option`_ = _`expression`_ items. Each _`expression`_ can be any string-valued expression. The allowed _`option`_ key words are:

`MESSAGE` [#](#RAISE-USING-OPTION-MESSAGE)

Sets the error message text. This option can't be used in the first syntax variant, since the message is already supplied.

`DETAIL` [#](#RAISE-USING-OPTION-DETAIL)

Supplies an error detail message.

`HINT` [#](#RAISE-USING-OPTION-HINT)

Supplies a hint message.

`ERRCODE` [#](#RAISE-USING-OPTION-ERRCODE)

Specifies the error code (SQLSTATE) to report, either by condition name, as shown in [Appendix A](https://www.postgresql.org/docs/current/errcodes-appendix.html "Appendix A. PostgreSQL Error Codes"), or directly as a five-character SQLSTATE code. This option can't be used in the second or third syntax variant, since the error code is already supplied.

`COLUMN`  
`CONSTRAINT`  
`DATATYPE`  
`TABLE`  
`SCHEMA` [#](#RAISE-USING-OPTION-COLUMN)

Supplies the name of a related object.

This example will abort the transaction with the given error message and hint:

RAISE EXCEPTION 'Nonexistent ID --> %', user\_id
      USING HINT = 'Please check your user ID';

These two examples show equivalent ways of setting the SQLSTATE:

RAISE 'Duplicate user ID: %', user\_id USING ERRCODE = 'unique\_violation';
RAISE 'Duplicate user ID: %', user\_id USING ERRCODE = '23505';

Another way to produce the same result is:

RAISE unique\_violation USING MESSAGE = 'Duplicate user ID: ' || user\_id;

As shown in the fourth syntax variant, it is also possible to write `RAISE USING` or ``RAISE _`level`_ USING`` and put everything else into the `USING` list.

The last variant of `RAISE` has no parameters at all. This form can only be used inside a `BEGIN` block's `EXCEPTION` clause; it causes the error currently being handled to be re-thrown.

### Note

Before PostgreSQL 9.1, `RAISE` without parameters was interpreted as re-throwing the error from the block containing the active exception handler. Thus an `EXCEPTION` clause nested within that handler could not catch it, even if the `RAISE` was within the nested `EXCEPTION` clause's block. This was deemed surprising as well as being incompatible with Oracle's PL/SQL.

If no condition name nor SQLSTATE is specified in a `RAISE EXCEPTION` command, the default is to use `raise_exception` (`P0001`). If no message text is specified, the default is to use the condition name or SQLSTATE as message text.

### Note

When specifying an error code by SQLSTATE code, you are not limited to the predefined error codes, but can select any error code consisting of five digits and/or upper-case ASCII letters, other than `00000`. It is recommended that you avoid throwing error codes that end in three zeroes, because these are category codes and can only be trapped by trapping the whole category.

### 41.9.2. Checking Assertions [#](#PLPGSQL-STATEMENTS-ASSERT)

The `ASSERT` statement is a convenient shorthand for inserting debugging checks into PL/pgSQL functions.

ASSERT _`condition`_ \[ , _`message`_ \];

The _`condition`_ is a Boolean expression that is expected to always evaluate to true; if it does, the `ASSERT` statement does nothing further. If the result is false or null, then an `ASSERT_FAILURE` exception is raised. (If an error occurs while evaluating the _`condition`_, it is reported as a normal error.)

If the optional _`message`_ is provided, it is an expression whose result (if not null) replaces the default error message text “assertion failed”, should the _`condition`_ fail. The _`message`_ expression is not evaluated in the normal case where the assertion succeeds.

Testing of assertions can be enabled or disabled via the configuration parameter `plpgsql.check_asserts`, which takes a Boolean value; the default is `on`. If this parameter is `off` then `ASSERT` statements do nothing.

Note that `ASSERT` is meant for detecting program bugs, not for reporting ordinary error conditions. Use the `RAISE` statement, described above, for that.

