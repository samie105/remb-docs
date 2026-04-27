---
title: "PostgreSQL: Documentation: 18: 32.4. Asynchronous Command Processing"
source: "https://www.postgresql.org/docs/current/libpq-async.html"
canonical_url: "https://www.postgresql.org/docs/current/libpq-async.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:53:05.099Z"
content_hash: "47369a1a9d88f43df939c3f665bd1afdebf3a28e091797811ab5bd897c4e55e8"
menu_path: ["PostgreSQL: Documentation: 18: 32.4. Asynchronous Command Processing"]
section_path: []
content_language: "en"
---
The [`PQexec`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQEXEC) function is adequate for submitting commands in normal, synchronous applications. It has a few deficiencies, however, that can be of importance to some users:

-   [`PQexec`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQEXEC) waits for the command to be completed. The application might have other work to do (such as maintaining a user interface), in which case it won't want to block waiting for the response.
    
-   Since the execution of the client application is suspended while it waits for the result, it is hard for the application to decide that it would like to try to cancel the ongoing command. (It can be done from a signal handler, but not otherwise.)
    
-   [`PQexec`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQEXEC) can return only one `PGresult` structure. If the submitted command string contains multiple SQL commands, all but the last `PGresult` are discarded by [`PQexec`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQEXEC).
    
-   [`PQexec`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQEXEC) always collects the command's entire result, buffering it in a single `PGresult`. While this simplifies error-handling logic for the application, it can be impractical for results containing many rows.
    

Applications that do not like these limitations can instead use the underlying functions that [`PQexec`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQEXEC) is built from: [`PQsendQuery`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERY) and [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT). There are also [`PQsendQueryParams`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERYPARAMS), [`PQsendPrepare`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDPREPARE), [`PQsendQueryPrepared`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERYPREPARED), [`PQsendDescribePrepared`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDDESCRIBEPREPARED), [`PQsendDescribePortal`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDDESCRIBEPORTAL), [`PQsendClosePrepared`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDCLOSEPREPARED), and [`PQsendClosePortal`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDCLOSEPORTAL), which can be used with [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) to duplicate the functionality of [`PQexecParams`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQEXECPARAMS), [`PQprepare`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQPREPARE), [`PQexecPrepared`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQEXECPREPARED), [`PQdescribePrepared`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQDESCRIBEPREPARED), [`PQdescribePortal`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQDESCRIBEPORTAL), [`PQclosePrepared`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQCLOSEPREPARED), and [`PQclosePortal`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQCLOSEPORTAL) respectively.

`PQsendQuery` [#](#LIBPQ-PQSENDQUERY)

Submits a command to the server without waiting for the result(s). 1 is returned if the command was successfully dispatched and 0 if not (in which case, use [`PQerrorMessage`](https://www.postgresql.org/docs/current/libpq-status.html#LIBPQ-PQERRORMESSAGE) to get more information about the failure).

int PQsendQuery(PGconn \*conn, const char \*command);

After successfully calling [`PQsendQuery`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERY), call [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) one or more times to obtain the results. [`PQsendQuery`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERY) cannot be called again (on the same connection) until [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) has returned a null pointer, indicating that the command is done.

In pipeline mode, this function is disallowed.

`PQsendQueryParams` [#](#LIBPQ-PQSENDQUERYPARAMS)

Submits a command and separate parameters to the server without waiting for the result(s).

int PQsendQueryParams(PGconn \*conn,
                      const char \*command,
                      int nParams,
                      const Oid \*paramTypes,
                      const char \* const \*paramValues,
                      const int \*paramLengths,
                      const int \*paramFormats,
                      int resultFormat);

This is equivalent to [`PQsendQuery`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERY) except that query parameters can be specified separately from the query string. The function's parameters are handled identically to [`PQexecParams`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQEXECPARAMS). Like [`PQexecParams`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQEXECPARAMS), it allows only one command in the query string.

`PQsendPrepare` [#](#LIBPQ-PQSENDPREPARE)

Sends a request to create a prepared statement with the given parameters, without waiting for completion.

int PQsendPrepare(PGconn \*conn,
                  const char \*stmtName,
                  const char \*query,
                  int nParams,
                  const Oid \*paramTypes);

This is an asynchronous version of [`PQprepare`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQPREPARE): it returns 1 if it was able to dispatch the request, and 0 if not. After a successful call, call [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) to determine whether the server successfully created the prepared statement. The function's parameters are handled identically to [`PQprepare`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQPREPARE).

`PQsendQueryPrepared` [#](#LIBPQ-PQSENDQUERYPREPARED)

Sends a request to execute a prepared statement with given parameters, without waiting for the result(s).

int PQsendQueryPrepared(PGconn \*conn,
                        const char \*stmtName,
                        int nParams,
                        const char \* const \*paramValues,
                        const int \*paramLengths,
                        const int \*paramFormats,
                        int resultFormat);

This is similar to [`PQsendQueryParams`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERYPARAMS), but the command to be executed is specified by naming a previously-prepared statement, instead of giving a query string. The function's parameters are handled identically to [`PQexecPrepared`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQEXECPREPARED).

`PQsendDescribePrepared` [#](#LIBPQ-PQSENDDESCRIBEPREPARED)

Submits a request to obtain information about the specified prepared statement, without waiting for completion.

int PQsendDescribePrepared(PGconn \*conn, const char \*stmtName);

This is an asynchronous version of [`PQdescribePrepared`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQDESCRIBEPREPARED): it returns 1 if it was able to dispatch the request, and 0 if not. After a successful call, call [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) to obtain the results. The function's parameters are handled identically to [`PQdescribePrepared`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQDESCRIBEPREPARED).

`PQsendDescribePortal` [#](#LIBPQ-PQSENDDESCRIBEPORTAL)

Submits a request to obtain information about the specified portal, without waiting for completion.

int PQsendDescribePortal(PGconn \*conn, const char \*portalName);

This is an asynchronous version of [`PQdescribePortal`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQDESCRIBEPORTAL): it returns 1 if it was able to dispatch the request, and 0 if not. After a successful call, call [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) to obtain the results. The function's parameters are handled identically to [`PQdescribePortal`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQDESCRIBEPORTAL).

`PQsendClosePrepared` [#](#LIBPQ-PQSENDCLOSEPREPARED)

Submits a request to close the specified prepared statement, without waiting for completion.

int PQsendClosePrepared(PGconn \*conn, const char \*stmtName);

This is an asynchronous version of [`PQclosePrepared`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQCLOSEPREPARED): it returns 1 if it was able to dispatch the request, and 0 if not. After a successful call, call [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) to obtain the results. The function's parameters are handled identically to [`PQclosePrepared`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQCLOSEPREPARED).

`PQsendClosePortal` [#](#LIBPQ-PQSENDCLOSEPORTAL)

Submits a request to close specified portal, without waiting for completion.

int PQsendClosePortal(PGconn \*conn, const char \*portalName);

This is an asynchronous version of [`PQclosePortal`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQCLOSEPORTAL): it returns 1 if it was able to dispatch the request, and 0 if not. After a successful call, call [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) to obtain the results. The function's parameters are handled identically to [`PQclosePortal`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQCLOSEPORTAL).

`PQgetResult` [#](#LIBPQ-PQGETRESULT)

Waits for the next result from a prior [`PQsendQuery`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERY), [`PQsendQueryParams`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERYPARAMS), [`PQsendPrepare`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDPREPARE), [`PQsendQueryPrepared`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERYPREPARED), [`PQsendDescribePrepared`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDDESCRIBEPREPARED), [`PQsendDescribePortal`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDDESCRIBEPORTAL), [`PQsendClosePrepared`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDCLOSEPREPARED), [`PQsendClosePortal`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDCLOSEPORTAL), [`PQsendPipelineSync`](https://www.postgresql.org/docs/current/libpq-pipeline-mode.html#LIBPQ-PQSENDPIPELINESYNC), or [`PQpipelineSync`](https://www.postgresql.org/docs/current/libpq-pipeline-mode.html#LIBPQ-PQPIPELINESYNC) call, and returns it. A null pointer is returned when the command is complete and there will be no more results.

PGresult \*PQgetResult(PGconn \*conn);

[`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) must be called repeatedly until it returns a null pointer, indicating that the command is done. (If called when no command is active, [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) will just return a null pointer at once.) Each non-null result from [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) should be processed using the same `PGresult` accessor functions previously described. Don't forget to free each result object with [`PQclear`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQCLEAR) when done with it. Note that [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) will block only if a command is active and the necessary response data has not yet been read by [`PQconsumeInput`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQCONSUMEINPUT) .

In pipeline mode, `PQgetResult` will return normally unless an error occurs; for any subsequent query sent after the one that caused the error until (and excluding) the next synchronization point, a special result of type `PGRES_PIPELINE_ABORTED` will be returned, and a null pointer will be returned after it. When the pipeline synchronization point is reached, a result of type `PGRES_PIPELINE_SYNC` will be returned. The result of the next query after the synchronization point follows immediately (that is, no null pointer is returned after the synchronization point).

### Note

Even when [`PQresultStatus`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQRESULTSTATUS) indicates a fatal error, [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) should be called until it returns a null pointer, to allow libpq to process the error information completely.

Using [`PQsendQuery`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERY) and [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) solves one of [`PQexec`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQEXEC)'s problems: If a command string contains multiple SQL commands, the results of those commands can be obtained individually. (This allows a simple form of overlapped processing, by the way: the client can be handling the results of one command while the server is still working on later queries in the same command string.)

Another frequently-desired feature that can be obtained with [`PQsendQuery`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERY) and [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) is retrieving large query results a limited number of rows at a time. This is discussed in [Section 32.6](https://www.postgresql.org/docs/current/libpq-single-row-mode.html "32.6. Retrieving Query Results in Chunks").

By itself, calling [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) will still cause the client to block until the server completes the next SQL command. This can be avoided by proper use of two more functions:

`PQconsumeInput` [#](#LIBPQ-PQCONSUMEINPUT)

If input is available from the server, consume it.

int PQconsumeInput(PGconn \*conn);

[`PQconsumeInput`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQCONSUMEINPUT) normally returns 1 indicating “no error”, but returns 0 if there was some kind of trouble (in which case [`PQerrorMessage`](https://www.postgresql.org/docs/current/libpq-status.html#LIBPQ-PQERRORMESSAGE) can be consulted). Note that the result does not say whether any input data was actually collected. After calling [`PQconsumeInput`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQCONSUMEINPUT) , the application can check [`PQisBusy`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQISBUSY) and/or `PQnotifies` to see if their state has changed.

[`PQconsumeInput`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQCONSUMEINPUT) can be called even if the application is not prepared to deal with a result or notification just yet. The function will read available data and save it in a buffer, thereby causing a `select()` read-ready indication to go away. The application can thus use [`PQconsumeInput`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQCONSUMEINPUT) to clear the `select()` condition immediately, and then examine the results at leisure.

`PQisBusy` [#](#LIBPQ-PQISBUSY)

Returns 1 if a command is busy, that is, [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) would block waiting for input. A 0 return indicates that [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) can be called with assurance of not blocking.

int PQisBusy(PGconn \*conn);

[`PQisBusy`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQISBUSY) will not itself attempt to read data from the server; therefore [`PQconsumeInput`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQCONSUMEINPUT) must be invoked first, or the busy state will never end.

A typical application using these functions will have a main loop that uses `select()` or `poll()` to wait for all the conditions that it must respond to. One of the conditions will be input available from the server, which in terms of `select()` means readable data on the file descriptor identified by [`PQsocket`](https://www.postgresql.org/docs/current/libpq-status.html#LIBPQ-PQSOCKET). When the main loop detects input ready, it should call [`PQconsumeInput`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQCONSUMEINPUT) to read the input. It can then call [`PQisBusy`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQISBUSY), followed by [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) if [`PQisBusy`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQISBUSY) returns false (0). It can also call `PQnotifies` to detect `NOTIFY` messages (see [Section 32.9](https://www.postgresql.org/docs/current/libpq-notify.html "32.9. Asynchronous Notification")).

A client that uses [`PQsendQuery`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERY)/[`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT) can also attempt to cancel a command that is still being processed by the server; see [Section 32.7](https://www.postgresql.org/docs/current/libpq-cancel.html "32.7. Canceling Queries in Progress"). But regardless of the return value of [`PQcancelBlocking`](https://www.postgresql.org/docs/current/libpq-cancel.html#LIBPQ-PQCANCELBLOCKING), the application must continue with the normal result-reading sequence using [`PQgetResult`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQGETRESULT). A successful cancellation will simply cause the command to terminate sooner than it would have otherwise.

By using the functions described above, it is possible to avoid blocking while waiting for input from the database server. However, it is still possible that the application will block waiting to send output to the server. This is relatively uncommon but can happen if very long SQL commands or data values are sent. (It is much more probable if the application sends data via `COPY IN`, however.) To prevent this possibility and achieve completely nonblocking database operation, the following additional functions can be used.

`PQsetnonblocking` [#](#LIBPQ-PQSETNONBLOCKING)

Sets the nonblocking status of the connection.

int PQsetnonblocking(PGconn \*conn, int arg);

Sets the state of the connection to nonblocking if _`arg`_ is 1, or blocking if _`arg`_ is 0. Returns 0 if OK, -1 if error.

In the nonblocking state, successful calls to [`PQsendQuery`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQSENDQUERY), [`PQputline`](https://www.postgresql.org/docs/current/libpq-copy.html#LIBPQ-PQPUTLINE), [`PQputnbytes`](https://www.postgresql.org/docs/current/libpq-copy.html#LIBPQ-PQPUTNBYTES), [`PQputCopyData`](https://www.postgresql.org/docs/current/libpq-copy.html#LIBPQ-PQPUTCOPYDATA), and [`PQendcopy`](https://www.postgresql.org/docs/current/libpq-copy.html#LIBPQ-PQENDCOPY) will not block; their changes are stored in the local output buffer until they are flushed. Unsuccessful calls will return an error and must be retried.

Note that [`PQexec`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQEXEC) does not honor nonblocking mode; if it is called, it will act in blocking fashion anyway.

`PQisnonblocking` [#](#LIBPQ-PQISNONBLOCKING)

Returns the blocking status of the database connection.

int PQisnonblocking(const PGconn \*conn);

Returns 1 if the connection is set to nonblocking mode and 0 if blocking.

`PQflush` [#](#LIBPQ-PQFLUSH)

Attempts to flush any queued output data to the server. Returns 0 if successful (or if the send queue is empty), -1 if it failed for some reason, or 1 if it was unable to send all the data in the send queue yet (this case can only occur if the connection is nonblocking).

int PQflush(PGconn \*conn);

After sending any command or data on a nonblocking connection, call [`PQflush`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQFLUSH). If it returns 1, wait for the socket to become read- or write-ready. If it becomes write-ready, call [`PQflush`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQFLUSH) again. If it becomes read-ready, call [`PQconsumeInput`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQCONSUMEINPUT) , then call [`PQflush`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQFLUSH) again. Repeat until [`PQflush`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQFLUSH) returns 0. (It is necessary to check for read-ready and drain the input with [`PQconsumeInput`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQCONSUMEINPUT) , because the server can block trying to send us data, e.g., NOTICE messages, and won't read our data until we read its.) Once [`PQflush`](https://www.postgresql.org/docs/current/libpq-async.html#LIBPQ-PQFLUSH) returns 0, wait for the socket to be read-ready and then read the response as described above.
