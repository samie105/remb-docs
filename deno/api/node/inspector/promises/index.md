---
title: "inspector/promises - Node documentation"
source: "https://docs.deno.com/api/node/inspector/promises/"
canonical_url: "https://docs.deno.com/api/node/inspector/promises/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:08:26.638Z"
content_hash: "aefd157ac56ec77edb0dc2720100caf456ad3a6d0b0f0852b65024b8f07f7f8a"
menu_path: ["inspector/promises - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "../index.md", "title": "inspector - Node documentation"}
nav_next: {"path": "../../module/index.md", "title": "module - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:inspector/promises";
```

The `node:inspector/promises` module provides an API for interacting with the V8 inspector.

c

[Session](../.././inspector/promises/~/Session "Session")

The `inspector.Session` is used for dispatching messages to the V8 inspector back-end and receiving message responses and notifications.

-   [addListener](../.././inspector/promises/~/Session#method_addlistener_0)
-   [connect](../.././inspector/promises/~/Session#method_connect_0)
-   [connectToMainThread](../.././inspector/promises/~/Session#method_connecttomainthread_0)
-   [disconnect](../.././inspector/promises/~/Session#method_disconnect_0)
-   [emit](../.././inspector/promises/~/Session#method_emit_0)
-   [on](../.././inspector/promises/~/Session#method_on_0)
-   [once](../.././inspector/promises/~/Session#method_once_0)
-   [post](../.././inspector/promises/~/Session#method_post_0)
-   [prependListener](../.././inspector/promises/~/Session#method_prependlistener_0)
-   [prependOnceListener](../.././inspector/promises/~/Session#method_prependoncelistener_0)

f

[close](../.././inspector/~/close "close")

Deactivate the inspector. Blocks until there are no active connections.

f

[Network.loadingFailed](../.././inspector/promises/~/Network.loadingFailed "Network.loadingFailed")

This feature is only available with the `--experimental-network-inspection` flag enabled.

f

[Network.loadingFinished](../.././inspector/promises/~/Network.loadingFinished "Network.loadingFinished")

This feature is only available with the `--experimental-network-inspection` flag enabled.

f

[Network.requestWillBeSent](../.././inspector/promises/~/Network.requestWillBeSent "Network.requestWillBeSent")

This feature is only available with the `--experimental-network-inspection` flag enabled.

f

[Network.responseReceived](../.././inspector/promises/~/Network.responseReceived "Network.responseReceived")

This feature is only available with the `--experimental-network-inspection` flag enabled.

f

[open](../.././inspector/~/open "open")

Activate inspector on host and port. Equivalent to `node --inspect=[[host:]port]`, but can be done programmatically after node has started.

f

[url](../.././inspector/~/url "url")

Return the URL of the active inspector, or `undefined` if there is none.

f

[waitForDebugger](../.././inspector/~/waitForDebugger "waitForDebugger")

Blocks until a client (existing or connected later) has sent `Runtime.runIfWaitingForDebugger` command.

I

[Console.ConsoleMessage](../.././inspector/promises/~/Console.ConsoleMessage "Console.ConsoleMessage")

Console message.

-   [column](../.././inspector/promises/~/Console.ConsoleMessage#property_column)
-   [level](../.././inspector/promises/~/Console.ConsoleMessage#property_level)
-   [line](../.././inspector/promises/~/Console.ConsoleMessage#property_line)
-   [source](../.././inspector/promises/~/Console.ConsoleMessage#property_source)
-   [text](../.././inspector/promises/~/Console.ConsoleMessage#property_text)
-   [url](../.././inspector/promises/~/Console.ConsoleMessage#property_url)

I

[Console.MessageAddedEventDataType](../.././inspector/promises/~/Console.MessageAddedEventDataType "Console.MessageAddedEventDataType")

No documentation available

-   [message](../.././inspector/promises/~/Console.MessageAddedEventDataType#property_message)

I

[Debugger.BreakLocation](../.././inspector/promises/~/Debugger.BreakLocation "Debugger.BreakLocation")

No documentation available

-   [columnNumber](../.././inspector/promises/~/Debugger.BreakLocation#property_columnnumber)
-   [lineNumber](../.././inspector/promises/~/Debugger.BreakLocation#property_linenumber)
-   [scriptId](../.././inspector/promises/~/Debugger.BreakLocation#property_scriptid)
-   [type](../.././inspector/promises/~/Debugger.BreakLocation#property_type)

I

[Debugger.BreakpointResolvedEventDataType](../.././inspector/promises/~/Debugger.BreakpointResolvedEventDataType "Debugger.BreakpointResolvedEventDataType")

No documentation available

-   [breakpointId](../.././inspector/promises/~/Debugger.BreakpointResolvedEventDataType#property_breakpointid)
-   [location](../.././inspector/promises/~/Debugger.BreakpointResolvedEventDataType#property_location)

I

[Debugger.CallFrame](../.././inspector/promises/~/Debugger.CallFrame "Debugger.CallFrame")

JavaScript call frame. Array of call frames form the call stack.

-   [callFrameId](../.././inspector/promises/~/Debugger.CallFrame#property_callframeid)
-   [functionLocation](../.././inspector/promises/~/Debugger.CallFrame#property_functionlocation)
-   [functionName](../.././inspector/promises/~/Debugger.CallFrame#property_functionname)
-   [location](../.././inspector/promises/~/Debugger.CallFrame#property_location)
-   [returnValue](../.././inspector/promises/~/Debugger.CallFrame#property_returnvalue)
-   [scopeChain](../.././inspector/promises/~/Debugger.CallFrame#property_scopechain)
-   [this](../.././inspector/promises/~/Debugger.CallFrame#property_this)
-   [url](../.././inspector/promises/~/Debugger.CallFrame#property_url)

I

[Debugger.ContinueToLocationParameterType](../.././inspector/promises/~/Debugger.ContinueToLocationParameterType "Debugger.ContinueToLocationParameterType")

No documentation available

-   [location](../.././inspector/promises/~/Debugger.ContinueToLocationParameterType#property_location)
-   [targetCallFrames](../.././inspector/promises/~/Debugger.ContinueToLocationParameterType#property_targetcallframes)

I

[Debugger.EnableReturnType](../.././inspector/promises/~/Debugger.EnableReturnType "Debugger.EnableReturnType")

No documentation available

-   [debuggerId](../.././inspector/promises/~/Debugger.EnableReturnType#property_debuggerid)

I

[Debugger.EvaluateOnCallFrameParameterType](../.././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType "Debugger.EvaluateOnCallFrameParameterType")

No documentation available

-   [callFrameId](../.././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_callframeid)
-   [expression](../.././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_expression)
-   [generatePreview](../.././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_generatepreview)
-   [includeCommandLineAPI](../.././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_includecommandlineapi)
-   [objectGroup](../.././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_objectgroup)
-   [returnByValue](../.././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_returnbyvalue)
-   [silent](../.././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_silent)
-   [throwOnSideEffect](../.././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_throwonsideeffect)

I

[Debugger.EvaluateOnCallFrameReturnType](../.././inspector/promises/~/Debugger.EvaluateOnCallFrameReturnType "Debugger.EvaluateOnCallFrameReturnType")

No documentation available

-   [exceptionDetails](../.././inspector/promises/~/Debugger.EvaluateOnCallFrameReturnType#property_exceptiondetails)
-   [result](../.././inspector/promises/~/Debugger.EvaluateOnCallFrameReturnType#property_result)

I

[Debugger.GetPossibleBreakpointsParameterType](../.././inspector/promises/~/Debugger.GetPossibleBreakpointsParameterType "Debugger.GetPossibleBreakpointsParameterType")

No documentation available

-   [end](../.././inspector/promises/~/Debugger.GetPossibleBreakpointsParameterType#property_end)
-   [restrictToFunction](../.././inspector/promises/~/Debugger.GetPossibleBreakpointsParameterType#property_restricttofunction)
-   [start](../.././inspector/promises/~/Debugger.GetPossibleBreakpointsParameterType#property_start)

I

[Debugger.GetPossibleBreakpointsReturnType](../.././inspector/promises/~/Debugger.GetPossibleBreakpointsReturnType "Debugger.GetPossibleBreakpointsReturnType")

No documentation available

-   [locations](../.././inspector/promises/~/Debugger.GetPossibleBreakpointsReturnType#property_locations)

I

[Debugger.GetScriptSourceParameterType](../.././inspector/promises/~/Debugger.GetScriptSourceParameterType "Debugger.GetScriptSourceParameterType")

No documentation available

-   [scriptId](../.././inspector/promises/~/Debugger.GetScriptSourceParameterType#property_scriptid)

I

[Debugger.GetScriptSourceReturnType](../.././inspector/promises/~/Debugger.GetScriptSourceReturnType "Debugger.GetScriptSourceReturnType")

No documentation available

-   [scriptSource](../.././inspector/promises/~/Debugger.GetScriptSourceReturnType#property_scriptsource)

I

[Debugger.GetStackTraceParameterType](../.././inspector/promises/~/Debugger.GetStackTraceParameterType "Debugger.GetStackTraceParameterType")

No documentation available

-   [stackTraceId](../.././inspector/promises/~/Debugger.GetStackTraceParameterType#property_stacktraceid)

I

[Debugger.GetStackTraceReturnType](../.././inspector/promises/~/Debugger.GetStackTraceReturnType "Debugger.GetStackTraceReturnType")

No documentation available

-   [stackTrace](../.././inspector/promises/~/Debugger.GetStackTraceReturnType#property_stacktrace)

I

[Debugger.Location](../.././inspector/promises/~/Debugger.Location "Debugger.Location")

Location in the source code.

-   [columnNumber](../.././inspector/promises/~/Debugger.Location#property_columnnumber)
-   [lineNumber](../.././inspector/promises/~/Debugger.Location#property_linenumber)
-   [scriptId](../.././inspector/promises/~/Debugger.Location#property_scriptid)

I

[Debugger.PausedEventDataType](../.././inspector/promises/~/Debugger.PausedEventDataType "Debugger.PausedEventDataType")

No documentation available

-   [asyncCallStackTraceId](../.././inspector/promises/~/Debugger.PausedEventDataType#property_asynccallstacktraceid)
-   [asyncStackTrace](../.././inspector/promises/~/Debugger.PausedEventDataType#property_asyncstacktrace)
-   [asyncStackTraceId](../.././inspector/promises/~/Debugger.PausedEventDataType#property_asyncstacktraceid)
-   [callFrames](../.././inspector/promises/~/Debugger.PausedEventDataType#property_callframes)
-   [data](../.././inspector/promises/~/Debugger.PausedEventDataType#property_data)
-   [hitBreakpoints](../.././inspector/promises/~/Debugger.PausedEventDataType#property_hitbreakpoints)
-   [reason](../.././inspector/promises/~/Debugger.PausedEventDataType#property_reason)

I

[Debugger.PauseOnAsyncCallParameterType](../.././inspector/promises/~/Debugger.PauseOnAsyncCallParameterType "Debugger.PauseOnAsyncCallParameterType")

No documentation available

-   [parentStackTraceId](../.././inspector/promises/~/Debugger.PauseOnAsyncCallParameterType#property_parentstacktraceid)

I

[Debugger.RemoveBreakpointParameterType](../.././inspector/promises/~/Debugger.RemoveBreakpointParameterType "Debugger.RemoveBreakpointParameterType")

No documentation available

-   [breakpointId](../.././inspector/promises/~/Debugger.RemoveBreakpointParameterType#property_breakpointid)

I

[Debugger.RestartFrameParameterType](../.././inspector/promises/~/Debugger.RestartFrameParameterType "Debugger.RestartFrameParameterType")

No documentation available

-   [callFrameId](../.././inspector/promises/~/Debugger.RestartFrameParameterType#property_callframeid)

I

[Debugger.RestartFrameReturnType](../.././inspector/promises/~/Debugger.RestartFrameReturnType "Debugger.RestartFrameReturnType")

No documentation available

-   [asyncStackTrace](../.././inspector/promises/~/Debugger.RestartFrameReturnType#property_asyncstacktrace)
-   [asyncStackTraceId](../.././inspector/promises/~/Debugger.RestartFrameReturnType#property_asyncstacktraceid)
-   [callFrames](../.././inspector/promises/~/Debugger.RestartFrameReturnType#property_callframes)

I

[Debugger.Scope](../.././inspector/promises/~/Debugger.Scope "Debugger.Scope")

Scope description.

-   [endLocation](../.././inspector/promises/~/Debugger.Scope#property_endlocation)
-   [name](../.././inspector/promises/~/Debugger.Scope#property_name)
-   [object](../.././inspector/promises/~/Debugger.Scope#property_object)
-   [startLocation](../.././inspector/promises/~/Debugger.Scope#property_startlocation)
-   [type](../.././inspector/promises/~/Debugger.Scope#property_type)

I

[Debugger.ScriptFailedToParseEventDataType](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType "Debugger.ScriptFailedToParseEventDataType")

No documentation available

-   [endColumn](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_endcolumn)
-   [endLine](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_endline)
-   [executionContextAuxData](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_executioncontextauxdata)
-   [executionContextId](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_executioncontextid)
-   [hasSourceURL](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_hassourceurl)
-   [hash](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_hash)
-   [isModule](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_ismodule)
-   [length](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_length)
-   [scriptId](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_scriptid)
-   [sourceMapURL](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_sourcemapurl)
-   [stackTrace](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_stacktrace)
-   [startColumn](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_startcolumn)
-   [startLine](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_startline)
-   [url](../.././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_url)

I

[Debugger.ScriptParsedEventDataType](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType "Debugger.ScriptParsedEventDataType")

No documentation available

-   [endColumn](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_endcolumn)
-   [endLine](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_endline)
-   [executionContextAuxData](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_executioncontextauxdata)
-   [executionContextId](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_executioncontextid)
-   [hasSourceURL](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_hassourceurl)
-   [hash](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_hash)
-   [isLiveEdit](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_isliveedit)
-   [isModule](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_ismodule)
-   [length](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_length)
-   [scriptId](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_scriptid)
-   [sourceMapURL](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_sourcemapurl)
-   [stackTrace](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_stacktrace)
-   [startColumn](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_startcolumn)
-   [startLine](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_startline)
-   [url](../.././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_url)

I

[Debugger.ScriptPosition](../.././inspector/promises/~/Debugger.ScriptPosition "Debugger.ScriptPosition")

Location in the source code.

-   [columnNumber](../.././inspector/promises/~/Debugger.ScriptPosition#property_columnnumber)
-   [lineNumber](../.././inspector/promises/~/Debugger.ScriptPosition#property_linenumber)

I

[Debugger.SearchInContentParameterType](../.././inspector/promises/~/Debugger.SearchInContentParameterType "Debugger.SearchInContentParameterType")

No documentation available

-   [caseSensitive](../.././inspector/promises/~/Debugger.SearchInContentParameterType#property_casesensitive)
-   [isRegex](../.././inspector/promises/~/Debugger.SearchInContentParameterType#property_isregex)
-   [query](../.././inspector/promises/~/Debugger.SearchInContentParameterType#property_query)
-   [scriptId](../.././inspector/promises/~/Debugger.SearchInContentParameterType#property_scriptid)

I

[Debugger.SearchInContentReturnType](../.././inspector/promises/~/Debugger.SearchInContentReturnType "Debugger.SearchInContentReturnType")

No documentation available

-   [result](../.././inspector/promises/~/Debugger.SearchInContentReturnType#property_result)

I

[Debugger.SearchMatch](../.././inspector/promises/~/Debugger.SearchMatch "Debugger.SearchMatch")

Search match for resource.

-   [lineContent](../.././inspector/promises/~/Debugger.SearchMatch#property_linecontent)
-   [lineNumber](../.././inspector/promises/~/Debugger.SearchMatch#property_linenumber)

I

[Debugger.SetAsyncCallStackDepthParameterType](../.././inspector/promises/~/Debugger.SetAsyncCallStackDepthParameterType "Debugger.SetAsyncCallStackDepthParameterType")

No documentation available

-   [maxDepth](../.././inspector/promises/~/Debugger.SetAsyncCallStackDepthParameterType#property_maxdepth)

I

[Debugger.SetBlackboxedRangesParameterType](../.././inspector/promises/~/Debugger.SetBlackboxedRangesParameterType "Debugger.SetBlackboxedRangesParameterType")

No documentation available

-   [positions](../.././inspector/promises/~/Debugger.SetBlackboxedRangesParameterType#property_positions)
-   [scriptId](../.././inspector/promises/~/Debugger.SetBlackboxedRangesParameterType#property_scriptid)

I

[Debugger.SetBlackboxPatternsParameterType](../.././inspector/promises/~/Debugger.SetBlackboxPatternsParameterType "Debugger.SetBlackboxPatternsParameterType")

No documentation available

-   [patterns](../.././inspector/promises/~/Debugger.SetBlackboxPatternsParameterType#property_patterns)

I

[Debugger.SetBreakpointByUrlParameterType](../.././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType "Debugger.SetBreakpointByUrlParameterType")

No documentation available

-   [columnNumber](../.././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType#property_columnnumber)
-   [condition](../.././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType#property_condition)
-   [lineNumber](../.././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType#property_linenumber)
-   [scriptHash](../.././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType#property_scripthash)
-   [url](../.././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType#property_url)
-   [urlRegex](../.././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType#property_urlregex)

I

[Debugger.SetBreakpointByUrlReturnType](../.././inspector/promises/~/Debugger.SetBreakpointByUrlReturnType "Debugger.SetBreakpointByUrlReturnType")

No documentation available

-   [breakpointId](../.././inspector/promises/~/Debugger.SetBreakpointByUrlReturnType#property_breakpointid)
-   [locations](../.././inspector/promises/~/Debugger.SetBreakpointByUrlReturnType#property_locations)

I

[Debugger.SetBreakpointParameterType](../.././inspector/promises/~/Debugger.SetBreakpointParameterType "Debugger.SetBreakpointParameterType")

No documentation available

-   [condition](../.././inspector/promises/~/Debugger.SetBreakpointParameterType#property_condition)
-   [location](../.././inspector/promises/~/Debugger.SetBreakpointParameterType#property_location)

I

[Debugger.SetBreakpointReturnType](../.././inspector/promises/~/Debugger.SetBreakpointReturnType "Debugger.SetBreakpointReturnType")

No documentation available

-   [actualLocation](../.././inspector/promises/~/Debugger.SetBreakpointReturnType#property_actuallocation)
-   [breakpointId](../.././inspector/promises/~/Debugger.SetBreakpointReturnType#property_breakpointid)

I

[Debugger.SetBreakpointsActiveParameterType](../.././inspector/promises/~/Debugger.SetBreakpointsActiveParameterType "Debugger.SetBreakpointsActiveParameterType")

No documentation available

-   [active](../.././inspector/promises/~/Debugger.SetBreakpointsActiveParameterType#property_active)

I

[Debugger.SetPauseOnExceptionsParameterType](../.././inspector/promises/~/Debugger.SetPauseOnExceptionsParameterType "Debugger.SetPauseOnExceptionsParameterType")

No documentation available

-   [state](../.././inspector/promises/~/Debugger.SetPauseOnExceptionsParameterType#property_state)

I

[Debugger.SetReturnValueParameterType](../.././inspector/promises/~/Debugger.SetReturnValueParameterType "Debugger.SetReturnValueParameterType")

No documentation available

-   [newValue](../.././inspector/promises/~/Debugger.SetReturnValueParameterType#property_newvalue)

I

[Debugger.SetScriptSourceParameterType](../.././inspector/promises/~/Debugger.SetScriptSourceParameterType "Debugger.SetScriptSourceParameterType")

No documentation available

-   [dryRun](../.././inspector/promises/~/Debugger.SetScriptSourceParameterType#property_dryrun)
-   [scriptId](../.././inspector/promises/~/Debugger.SetScriptSourceParameterType#property_scriptid)
-   [scriptSource](../.././inspector/promises/~/Debugger.SetScriptSourceParameterType#property_scriptsource)

I

[Debugger.SetScriptSourceReturnType](../.././inspector/promises/~/Debugger.SetScriptSourceReturnType "Debugger.SetScriptSourceReturnType")

No documentation available

-   [asyncStackTrace](../.././inspector/promises/~/Debugger.SetScriptSourceReturnType#property_asyncstacktrace)
-   [asyncStackTraceId](../.././inspector/promises/~/Debugger.SetScriptSourceReturnType#property_asyncstacktraceid)
-   [callFrames](../.././inspector/promises/~/Debugger.SetScriptSourceReturnType#property_callframes)
-   [exceptionDetails](../.././inspector/promises/~/Debugger.SetScriptSourceReturnType#property_exceptiondetails)
-   [stackChanged](../.././inspector/promises/~/Debugger.SetScriptSourceReturnType#property_stackchanged)

I

[Debugger.SetSkipAllPausesParameterType](../.././inspector/promises/~/Debugger.SetSkipAllPausesParameterType "Debugger.SetSkipAllPausesParameterType")

No documentation available

-   [skip](../.././inspector/promises/~/Debugger.SetSkipAllPausesParameterType#property_skip)

I

[Debugger.SetVariableValueParameterType](../.././inspector/promises/~/Debugger.SetVariableValueParameterType "Debugger.SetVariableValueParameterType")

No documentation available

-   [callFrameId](../.././inspector/promises/~/Debugger.SetVariableValueParameterType#property_callframeid)
-   [newValue](../.././inspector/promises/~/Debugger.SetVariableValueParameterType#property_newvalue)
-   [scopeNumber](../.././inspector/promises/~/Debugger.SetVariableValueParameterType#property_scopenumber)
-   [variableName](../.././inspector/promises/~/Debugger.SetVariableValueParameterType#property_variablename)

I

[Debugger.StepIntoParameterType](../.././inspector/promises/~/Debugger.StepIntoParameterType "Debugger.StepIntoParameterType")

No documentation available

-   [breakOnAsyncCall](../.././inspector/promises/~/Debugger.StepIntoParameterType#property_breakonasynccall)

I

[HeapProfiler.AddHeapSnapshotChunkEventDataType](../.././inspector/promises/~/HeapProfiler.AddHeapSnapshotChunkEventDataType "HeapProfiler.AddHeapSnapshotChunkEventDataType")

No documentation available

-   [chunk](../.././inspector/promises/~/HeapProfiler.AddHeapSnapshotChunkEventDataType#property_chunk)

I

[HeapProfiler.AddInspectedHeapObjectParameterType](../.././inspector/promises/~/HeapProfiler.AddInspectedHeapObjectParameterType "HeapProfiler.AddInspectedHeapObjectParameterType")

No documentation available

-   [heapObjectId](../.././inspector/promises/~/HeapProfiler.AddInspectedHeapObjectParameterType#property_heapobjectid)

I

[HeapProfiler.GetHeapObjectIdParameterType](../.././inspector/promises/~/HeapProfiler.GetHeapObjectIdParameterType "HeapProfiler.GetHeapObjectIdParameterType")

No documentation available

-   [objectId](../.././inspector/promises/~/HeapProfiler.GetHeapObjectIdParameterType#property_objectid)

I

[HeapProfiler.GetHeapObjectIdReturnType](../.././inspector/promises/~/HeapProfiler.GetHeapObjectIdReturnType "HeapProfiler.GetHeapObjectIdReturnType")

No documentation available

-   [heapSnapshotObjectId](../.././inspector/promises/~/HeapProfiler.GetHeapObjectIdReturnType#property_heapsnapshotobjectid)

I

[HeapProfiler.GetObjectByHeapObjectIdParameterType](../.././inspector/promises/~/HeapProfiler.GetObjectByHeapObjectIdParameterType "HeapProfiler.GetObjectByHeapObjectIdParameterType")

No documentation available

-   [objectGroup](../.././inspector/promises/~/HeapProfiler.GetObjectByHeapObjectIdParameterType#property_objectgroup)
-   [objectId](../.././inspector/promises/~/HeapProfiler.GetObjectByHeapObjectIdParameterType#property_objectid)

I

[HeapProfiler.GetObjectByHeapObjectIdReturnType](../.././inspector/promises/~/HeapProfiler.GetObjectByHeapObjectIdReturnType "HeapProfiler.GetObjectByHeapObjectIdReturnType")

No documentation available

-   [result](../.././inspector/promises/~/HeapProfiler.GetObjectByHeapObjectIdReturnType#property_result)

I

[HeapProfiler.GetSamplingProfileReturnType](../.././inspector/promises/~/HeapProfiler.GetSamplingProfileReturnType "HeapProfiler.GetSamplingProfileReturnType")

No documentation available

-   [profile](../.././inspector/promises/~/HeapProfiler.GetSamplingProfileReturnType#property_profile)

I

[HeapProfiler.HeapStatsUpdateEventDataType](../.././inspector/promises/~/HeapProfiler.HeapStatsUpdateEventDataType "HeapProfiler.HeapStatsUpdateEventDataType")

No documentation available

-   [statsUpdate](../.././inspector/promises/~/HeapProfiler.HeapStatsUpdateEventDataType#property_statsupdate)

I

[HeapProfiler.LastSeenObjectIdEventDataType](../.././inspector/promises/~/HeapProfiler.LastSeenObjectIdEventDataType "HeapProfiler.LastSeenObjectIdEventDataType")

No documentation available

-   [lastSeenObjectId](../.././inspector/promises/~/HeapProfiler.LastSeenObjectIdEventDataType#property_lastseenobjectid)
-   [timestamp](../.././inspector/promises/~/HeapProfiler.LastSeenObjectIdEventDataType#property_timestamp)

I

[HeapProfiler.ReportHeapSnapshotProgressEventDataType](../.././inspector/promises/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType "HeapProfiler.ReportHeapSnapshotProgressEventDataType")

No documentation available

-   [done](../.././inspector/promises/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType#property_done)
-   [finished](../.././inspector/promises/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType#property_finished)
-   [total](../.././inspector/promises/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType#property_total)

I

[HeapProfiler.SamplingHeapProfile](../.././inspector/promises/~/HeapProfiler.SamplingHeapProfile "HeapProfiler.SamplingHeapProfile")

Profile.

-   [head](../.././inspector/promises/~/HeapProfiler.SamplingHeapProfile#property_head)

I

[HeapProfiler.SamplingHeapProfileNode](../.././inspector/promises/~/HeapProfiler.SamplingHeapProfileNode "HeapProfiler.SamplingHeapProfileNode")

Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes.

-   [callFrame](../.././inspector/promises/~/HeapProfiler.SamplingHeapProfileNode#property_callframe)
-   [children](../.././inspector/promises/~/HeapProfiler.SamplingHeapProfileNode#property_children)
-   [selfSize](../.././inspector/promises/~/HeapProfiler.SamplingHeapProfileNode#property_selfsize)

I

[HeapProfiler.StartSamplingParameterType](../.././inspector/promises/~/HeapProfiler.StartSamplingParameterType "HeapProfiler.StartSamplingParameterType")

No documentation available

-   [samplingInterval](../.././inspector/promises/~/HeapProfiler.StartSamplingParameterType#property_samplinginterval)

I

[HeapProfiler.StartTrackingHeapObjectsParameterType](../.././inspector/promises/~/HeapProfiler.StartTrackingHeapObjectsParameterType "HeapProfiler.StartTrackingHeapObjectsParameterType")

No documentation available

-   [trackAllocations](../.././inspector/promises/~/HeapProfiler.StartTrackingHeapObjectsParameterType#property_trackallocations)

I

[HeapProfiler.StopSamplingReturnType](../.././inspector/promises/~/HeapProfiler.StopSamplingReturnType "HeapProfiler.StopSamplingReturnType")

No documentation available

-   [profile](../.././inspector/promises/~/HeapProfiler.StopSamplingReturnType#property_profile)

I

[HeapProfiler.StopTrackingHeapObjectsParameterType](../.././inspector/promises/~/HeapProfiler.StopTrackingHeapObjectsParameterType "HeapProfiler.StopTrackingHeapObjectsParameterType")

No documentation available

-   [reportProgress](../.././inspector/promises/~/HeapProfiler.StopTrackingHeapObjectsParameterType#property_reportprogress)

I

[HeapProfiler.TakeHeapSnapshotParameterType](../.././inspector/promises/~/HeapProfiler.TakeHeapSnapshotParameterType "HeapProfiler.TakeHeapSnapshotParameterType")

No documentation available

-   [reportProgress](../.././inspector/promises/~/HeapProfiler.TakeHeapSnapshotParameterType#property_reportprogress)

I

[InspectorNotification](../.././inspector/~/InspectorNotification "InspectorNotification")

No documentation available

-   [method](../.././inspector/~/InspectorNotification#property_method)
-   [params](../.././inspector/~/InspectorNotification#property_params)

I

[Network.Headers](../.././inspector/promises/~/Network.Headers "Network.Headers")

Request / response headers as keys / values of JSON object.

I

[Network.LoadingFailedEventDataType](../.././inspector/promises/~/Network.LoadingFailedEventDataType "Network.LoadingFailedEventDataType")

No documentation available

-   [errorText](../.././inspector/promises/~/Network.LoadingFailedEventDataType#property_errortext)
-   [requestId](../.././inspector/promises/~/Network.LoadingFailedEventDataType#property_requestid)
-   [timestamp](../.././inspector/promises/~/Network.LoadingFailedEventDataType#property_timestamp)
-   [type](../.././inspector/promises/~/Network.LoadingFailedEventDataType#property_type)

I

[Network.LoadingFinishedEventDataType](../.././inspector/promises/~/Network.LoadingFinishedEventDataType "Network.LoadingFinishedEventDataType")

No documentation available

-   [requestId](../.././inspector/promises/~/Network.LoadingFinishedEventDataType#property_requestid)
-   [timestamp](../.././inspector/promises/~/Network.LoadingFinishedEventDataType#property_timestamp)

I

[Network.Request](../.././inspector/promises/~/Network.Request "Network.Request")

HTTP request data.

-   [headers](../.././inspector/promises/~/Network.Request#property_headers)
-   [method](../.././inspector/promises/~/Network.Request#property_method)
-   [url](../.././inspector/promises/~/Network.Request#property_url)

I

[Network.RequestWillBeSentEventDataType](../.././inspector/promises/~/Network.RequestWillBeSentEventDataType "Network.RequestWillBeSentEventDataType")

No documentation available

-   [request](../.././inspector/promises/~/Network.RequestWillBeSentEventDataType#property_request)
-   [requestId](../.././inspector/promises/~/Network.RequestWillBeSentEventDataType#property_requestid)
-   [timestamp](../.././inspector/promises/~/Network.RequestWillBeSentEventDataType#property_timestamp)
-   [wallTime](../.././inspector/promises/~/Network.RequestWillBeSentEventDataType#property_walltime)

I

[Network.Response](../.././inspector/promises/~/Network.Response "Network.Response")

HTTP response data.

-   [headers](../.././inspector/promises/~/Network.Response#property_headers)
-   [status](../.././inspector/promises/~/Network.Response#property_status)
-   [statusText](../.././inspector/promises/~/Network.Response#property_statustext)
-   [url](../.././inspector/promises/~/Network.Response#property_url)

I

[Network.ResponseReceivedEventDataType](../.././inspector/promises/~/Network.ResponseReceivedEventDataType "Network.ResponseReceivedEventDataType")

No documentation available

-   [requestId](../.././inspector/promises/~/Network.ResponseReceivedEventDataType#property_requestid)
-   [response](../.././inspector/promises/~/Network.ResponseReceivedEventDataType#property_response)
-   [timestamp](../.././inspector/promises/~/Network.ResponseReceivedEventDataType#property_timestamp)
-   [type](../.././inspector/promises/~/Network.ResponseReceivedEventDataType#property_type)

I

[NodeRuntime.NotifyWhenWaitingForDisconnectParameterType](../.././inspector/promises/~/NodeRuntime.NotifyWhenWaitingForDisconnectParameterType "NodeRuntime.NotifyWhenWaitingForDisconnectParameterType")

No documentation available

-   [enabled](../.././inspector/promises/~/NodeRuntime.NotifyWhenWaitingForDisconnectParameterType#property_enabled)

I

[NodeTracing.DataCollectedEventDataType](../.././inspector/promises/~/NodeTracing.DataCollectedEventDataType "NodeTracing.DataCollectedEventDataType")

No documentation available

-   [value](../.././inspector/promises/~/NodeTracing.DataCollectedEventDataType#property_value)

I

[NodeTracing.GetCategoriesReturnType](../.././inspector/promises/~/NodeTracing.GetCategoriesReturnType "NodeTracing.GetCategoriesReturnType")

No documentation available

-   [categories](../.././inspector/promises/~/NodeTracing.GetCategoriesReturnType#property_categories)

I

[NodeTracing.StartParameterType](../.././inspector/promises/~/NodeTracing.StartParameterType "NodeTracing.StartParameterType")

No documentation available

-   [traceConfig](../.././inspector/promises/~/NodeTracing.StartParameterType#property_traceconfig)

I

[NodeTracing.TraceConfig](../.././inspector/promises/~/NodeTracing.TraceConfig "NodeTracing.TraceConfig")

No documentation available

-   [includedCategories](../.././inspector/promises/~/NodeTracing.TraceConfig#property_includedcategories)
-   [recordMode](../.././inspector/promises/~/NodeTracing.TraceConfig#property_recordmode)

I

[NodeWorker.AttachedToWorkerEventDataType](../.././inspector/promises/~/NodeWorker.AttachedToWorkerEventDataType "NodeWorker.AttachedToWorkerEventDataType")

No documentation available

-   [sessionId](../.././inspector/promises/~/NodeWorker.AttachedToWorkerEventDataType#property_sessionid)
-   [waitingForDebugger](../.././inspector/promises/~/NodeWorker.AttachedToWorkerEventDataType#property_waitingfordebugger)
-   [workerInfo](../.././inspector/promises/~/NodeWorker.AttachedToWorkerEventDataType#property_workerinfo)

I

[NodeWorker.DetachedFromWorkerEventDataType](../.././inspector/promises/~/NodeWorker.DetachedFromWorkerEventDataType "NodeWorker.DetachedFromWorkerEventDataType")

No documentation available

-   [sessionId](../.././inspector/promises/~/NodeWorker.DetachedFromWorkerEventDataType#property_sessionid)

I

[NodeWorker.DetachParameterType](../.././inspector/promises/~/NodeWorker.DetachParameterType "NodeWorker.DetachParameterType")

No documentation available

-   [sessionId](../.././inspector/promises/~/NodeWorker.DetachParameterType#property_sessionid)

I

[NodeWorker.EnableParameterType](../.././inspector/promises/~/NodeWorker.EnableParameterType "NodeWorker.EnableParameterType")

No documentation available

-   [waitForDebuggerOnStart](../.././inspector/promises/~/NodeWorker.EnableParameterType#property_waitfordebuggeronstart)

I

[NodeWorker.ReceivedMessageFromWorkerEventDataType](../.././inspector/promises/~/NodeWorker.ReceivedMessageFromWorkerEventDataType "NodeWorker.ReceivedMessageFromWorkerEventDataType")

No documentation available

-   [message](../.././inspector/promises/~/NodeWorker.ReceivedMessageFromWorkerEventDataType#property_message)
-   [sessionId](../.././inspector/promises/~/NodeWorker.ReceivedMessageFromWorkerEventDataType#property_sessionid)

I

[NodeWorker.SendMessageToWorkerParameterType](../.././inspector/promises/~/NodeWorker.SendMessageToWorkerParameterType "NodeWorker.SendMessageToWorkerParameterType")

No documentation available

-   [message](../.././inspector/promises/~/NodeWorker.SendMessageToWorkerParameterType#property_message)
-   [sessionId](../.././inspector/promises/~/NodeWorker.SendMessageToWorkerParameterType#property_sessionid)

I

[NodeWorker.WorkerInfo](../.././inspector/promises/~/NodeWorker.WorkerInfo "NodeWorker.WorkerInfo")

No documentation available

-   [title](../.././inspector/promises/~/NodeWorker.WorkerInfo#property_title)
-   [type](../.././inspector/promises/~/NodeWorker.WorkerInfo#property_type)
-   [url](../.././inspector/promises/~/NodeWorker.WorkerInfo#property_url)
-   [workerId](../.././inspector/promises/~/NodeWorker.WorkerInfo#property_workerid)

I

[Profiler.ConsoleProfileFinishedEventDataType](../.././inspector/promises/~/Profiler.ConsoleProfileFinishedEventDataType "Profiler.ConsoleProfileFinishedEventDataType")

No documentation available

-   [id](../.././inspector/promises/~/Profiler.ConsoleProfileFinishedEventDataType#property_id)
-   [location](../.././inspector/promises/~/Profiler.ConsoleProfileFinishedEventDataType#property_location)
-   [profile](../.././inspector/promises/~/Profiler.ConsoleProfileFinishedEventDataType#property_profile)
-   [title](../.././inspector/promises/~/Profiler.ConsoleProfileFinishedEventDataType#property_title)

I

[Profiler.ConsoleProfileStartedEventDataType](../.././inspector/promises/~/Profiler.ConsoleProfileStartedEventDataType "Profiler.ConsoleProfileStartedEventDataType")

No documentation available

-   [id](../.././inspector/promises/~/Profiler.ConsoleProfileStartedEventDataType#property_id)
-   [location](../.././inspector/promises/~/Profiler.ConsoleProfileStartedEventDataType#property_location)
-   [title](../.././inspector/promises/~/Profiler.ConsoleProfileStartedEventDataType#property_title)

I

[Profiler.CoverageRange](../.././inspector/promises/~/Profiler.CoverageRange "Profiler.CoverageRange")

Coverage data for a source range.

-   [count](../.././inspector/promises/~/Profiler.CoverageRange#property_count)
-   [endOffset](../.././inspector/promises/~/Profiler.CoverageRange#property_endoffset)
-   [startOffset](../.././inspector/promises/~/Profiler.CoverageRange#property_startoffset)

I

[Profiler.FunctionCoverage](../.././inspector/promises/~/Profiler.FunctionCoverage "Profiler.FunctionCoverage")

Coverage data for a JavaScript function.

-   [functionName](../.././inspector/promises/~/Profiler.FunctionCoverage#property_functionname)
-   [isBlockCoverage](../.././inspector/promises/~/Profiler.FunctionCoverage#property_isblockcoverage)
-   [ranges](../.././inspector/promises/~/Profiler.FunctionCoverage#property_ranges)

I

[Profiler.GetBestEffortCoverageReturnType](../.././inspector/promises/~/Profiler.GetBestEffortCoverageReturnType "Profiler.GetBestEffortCoverageReturnType")

No documentation available

-   [result](../.././inspector/promises/~/Profiler.GetBestEffortCoverageReturnType#property_result)

I

[Profiler.PositionTickInfo](../.././inspector/promises/~/Profiler.PositionTickInfo "Profiler.PositionTickInfo")

Specifies a number of samples attributed to a certain source position.

-   [line](../.././inspector/promises/~/Profiler.PositionTickInfo#property_line)
-   [ticks](../.././inspector/promises/~/Profiler.PositionTickInfo#property_ticks)

I

[Profiler.Profile](../.././inspector/promises/~/Profiler.Profile "Profiler.Profile")

Profile.

-   [endTime](../.././inspector/promises/~/Profiler.Profile#property_endtime)
-   [nodes](../.././inspector/promises/~/Profiler.Profile#property_nodes)
-   [samples](../.././inspector/promises/~/Profiler.Profile#property_samples)
-   [startTime](../.././inspector/promises/~/Profiler.Profile#property_starttime)
-   [timeDeltas](../.././inspector/promises/~/Profiler.Profile#property_timedeltas)

I

[Profiler.ProfileNode](../.././inspector/promises/~/Profiler.ProfileNode "Profiler.ProfileNode")

Profile node. Holds callsite information, execution statistics and child nodes.

-   [callFrame](../.././inspector/promises/~/Profiler.ProfileNode#property_callframe)
-   [children](../.././inspector/promises/~/Profiler.ProfileNode#property_children)
-   [deoptReason](../.././inspector/promises/~/Profiler.ProfileNode#property_deoptreason)
-   [hitCount](../.././inspector/promises/~/Profiler.ProfileNode#property_hitcount)
-   [id](../.././inspector/promises/~/Profiler.ProfileNode#property_id)
-   [positionTicks](../.././inspector/promises/~/Profiler.ProfileNode#property_positionticks)

I

[Profiler.ScriptCoverage](../.././inspector/promises/~/Profiler.ScriptCoverage "Profiler.ScriptCoverage")

Coverage data for a JavaScript script.

-   [functions](../.././inspector/promises/~/Profiler.ScriptCoverage#property_functions)
-   [scriptId](../.././inspector/promises/~/Profiler.ScriptCoverage#property_scriptid)
-   [url](../.././inspector/promises/~/Profiler.ScriptCoverage#property_url)

I

[Profiler.SetSamplingIntervalParameterType](../.././inspector/promises/~/Profiler.SetSamplingIntervalParameterType "Profiler.SetSamplingIntervalParameterType")

No documentation available

-   [interval](../.././inspector/promises/~/Profiler.SetSamplingIntervalParameterType#property_interval)

I

[Profiler.StartPreciseCoverageParameterType](../.././inspector/promises/~/Profiler.StartPreciseCoverageParameterType "Profiler.StartPreciseCoverageParameterType")

No documentation available

-   [callCount](../.././inspector/promises/~/Profiler.StartPreciseCoverageParameterType#property_callcount)
-   [detailed](../.././inspector/promises/~/Profiler.StartPreciseCoverageParameterType#property_detailed)

I

[Profiler.StopReturnType](../.././inspector/promises/~/Profiler.StopReturnType "Profiler.StopReturnType")

No documentation available

-   [profile](../.././inspector/promises/~/Profiler.StopReturnType#property_profile)

I

[Profiler.TakePreciseCoverageReturnType](../.././inspector/promises/~/Profiler.TakePreciseCoverageReturnType "Profiler.TakePreciseCoverageReturnType")

No documentation available

-   [result](../.././inspector/promises/~/Profiler.TakePreciseCoverageReturnType#property_result)

I

[Runtime.AwaitPromiseParameterType](../.././inspector/promises/~/Runtime.AwaitPromiseParameterType "Runtime.AwaitPromiseParameterType")

No documentation available

-   [generatePreview](../.././inspector/promises/~/Runtime.AwaitPromiseParameterType#property_generatepreview)
-   [promiseObjectId](../.././inspector/promises/~/Runtime.AwaitPromiseParameterType#property_promiseobjectid)
-   [returnByValue](../.././inspector/promises/~/Runtime.AwaitPromiseParameterType#property_returnbyvalue)

I

[Runtime.AwaitPromiseReturnType](../.././inspector/promises/~/Runtime.AwaitPromiseReturnType "Runtime.AwaitPromiseReturnType")

No documentation available

-   [exceptionDetails](../.././inspector/promises/~/Runtime.AwaitPromiseReturnType#property_exceptiondetails)
-   [result](../.././inspector/promises/~/Runtime.AwaitPromiseReturnType#property_result)

I

[Runtime.CallArgument](../.././inspector/promises/~/Runtime.CallArgument "Runtime.CallArgument")

Represents function call argument. Either remote object id `objectId`, primitive `value`, unserializable primitive value or neither of (for undefined) them should be specified.

-   [objectId](../.././inspector/promises/~/Runtime.CallArgument#property_objectid)
-   [unserializableValue](../.././inspector/promises/~/Runtime.CallArgument#property_unserializablevalue)
-   [value](../.././inspector/promises/~/Runtime.CallArgument#property_value)

I

[Runtime.CallFrame](../.././inspector/promises/~/Runtime.CallFrame "Runtime.CallFrame")

Stack entry for runtime errors and assertions.

-   [columnNumber](../.././inspector/promises/~/Runtime.CallFrame#property_columnnumber)
-   [functionName](../.././inspector/promises/~/Runtime.CallFrame#property_functionname)
-   [lineNumber](../.././inspector/promises/~/Runtime.CallFrame#property_linenumber)
-   [scriptId](../.././inspector/promises/~/Runtime.CallFrame#property_scriptid)
-   [url](../.././inspector/promises/~/Runtime.CallFrame#property_url)

I

[Runtime.CallFunctionOnParameterType](../.././inspector/promises/~/Runtime.CallFunctionOnParameterType "Runtime.CallFunctionOnParameterType")

No documentation available

-   [arguments](../.././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_arguments)
-   [awaitPromise](../.././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_awaitpromise)
-   [executionContextId](../.././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_executioncontextid)
-   [functionDeclaration](../.././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_functiondeclaration)
-   [generatePreview](../.././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_generatepreview)
-   [objectGroup](../.././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_objectgroup)
-   [objectId](../.././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_objectid)
-   [returnByValue](../.././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_returnbyvalue)
-   [silent](../.././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_silent)
-   [userGesture](../.././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_usergesture)

I

[Runtime.CallFunctionOnReturnType](../.././inspector/promises/~/Runtime.CallFunctionOnReturnType "Runtime.CallFunctionOnReturnType")

No documentation available

-   [exceptionDetails](../.././inspector/promises/~/Runtime.CallFunctionOnReturnType#property_exceptiondetails)
-   [result](../.././inspector/promises/~/Runtime.CallFunctionOnReturnType#property_result)

I

[Runtime.CompileScriptParameterType](../.././inspector/promises/~/Runtime.CompileScriptParameterType "Runtime.CompileScriptParameterType")

No documentation available

-   [executionContextId](../.././inspector/promises/~/Runtime.CompileScriptParameterType#property_executioncontextid)
-   [expression](../.././inspector/promises/~/Runtime.CompileScriptParameterType#property_expression)
-   [persistScript](../.././inspector/promises/~/Runtime.CompileScriptParameterType#property_persistscript)
-   [sourceURL](../.././inspector/promises/~/Runtime.CompileScriptParameterType#property_sourceurl)

I

[Runtime.CompileScriptReturnType](../.././inspector/promises/~/Runtime.CompileScriptReturnType "Runtime.CompileScriptReturnType")

No documentation available

-   [exceptionDetails](../.././inspector/promises/~/Runtime.CompileScriptReturnType#property_exceptiondetails)
-   [scriptId](../.././inspector/promises/~/Runtime.CompileScriptReturnType#property_scriptid)

I

[Runtime.ConsoleAPICalledEventDataType](../.././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType "Runtime.ConsoleAPICalledEventDataType")

No documentation available

-   [args](../.././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType#property_args)
-   [context](../.././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType#property_context)
-   [executionContextId](../.././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType#property_executioncontextid)
-   [stackTrace](../.././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType#property_stacktrace)
-   [timestamp](../.././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType#property_timestamp)
-   [type](../.././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType#property_type)

I

[Runtime.CustomPreview](../.././inspector/promises/~/Runtime.CustomPreview "Runtime.CustomPreview")

No documentation available

-   [bindRemoteObjectFunctionId](../.././inspector/promises/~/Runtime.CustomPreview#property_bindremoteobjectfunctionid)
-   [configObjectId](../.././inspector/promises/~/Runtime.CustomPreview#property_configobjectid)
-   [formatterObjectId](../.././inspector/promises/~/Runtime.CustomPreview#property_formatterobjectid)
-   [hasBody](../.././inspector/promises/~/Runtime.CustomPreview#property_hasbody)
-   [header](../.././inspector/promises/~/Runtime.CustomPreview#property_header)

I

[Runtime.EntryPreview](../.././inspector/promises/~/Runtime.EntryPreview "Runtime.EntryPreview")

No documentation available

-   [key](../.././inspector/promises/~/Runtime.EntryPreview#property_key)
-   [value](../.././inspector/promises/~/Runtime.EntryPreview#property_value)

I

[Runtime.EvaluateParameterType](../.././inspector/promises/~/Runtime.EvaluateParameterType "Runtime.EvaluateParameterType")

No documentation available

-   [awaitPromise](../.././inspector/promises/~/Runtime.EvaluateParameterType#property_awaitpromise)
-   [contextId](../.././inspector/promises/~/Runtime.EvaluateParameterType#property_contextid)
-   [expression](../.././inspector/promises/~/Runtime.EvaluateParameterType#property_expression)
-   [generatePreview](../.././inspector/promises/~/Runtime.EvaluateParameterType#property_generatepreview)
-   [includeCommandLineAPI](../.././inspector/promises/~/Runtime.EvaluateParameterType#property_includecommandlineapi)
-   [objectGroup](../.././inspector/promises/~/Runtime.EvaluateParameterType#property_objectgroup)
-   [returnByValue](../.././inspector/promises/~/Runtime.EvaluateParameterType#property_returnbyvalue)
-   [silent](../.././inspector/promises/~/Runtime.EvaluateParameterType#property_silent)
-   [userGesture](../.././inspector/promises/~/Runtime.EvaluateParameterType#property_usergesture)

I

[Runtime.EvaluateReturnType](../.././inspector/promises/~/Runtime.EvaluateReturnType "Runtime.EvaluateReturnType")

No documentation available

-   [exceptionDetails](../.././inspector/promises/~/Runtime.EvaluateReturnType#property_exceptiondetails)
-   [result](../.././inspector/promises/~/Runtime.EvaluateReturnType#property_result)

I

[Runtime.ExceptionDetails](../.././inspector/promises/~/Runtime.ExceptionDetails "Runtime.ExceptionDetails")

Detailed information about exception (or error) that was thrown during script compilation or execution.

-   [columnNumber](../.././inspector/promises/~/Runtime.ExceptionDetails#property_columnnumber)
-   [exception](../.././inspector/promises/~/Runtime.ExceptionDetails#property_exception)
-   [exceptionId](../.././inspector/promises/~/Runtime.ExceptionDetails#property_exceptionid)
-   [executionContextId](../.././inspector/promises/~/Runtime.ExceptionDetails#property_executioncontextid)
-   [lineNumber](../.././inspector/promises/~/Runtime.ExceptionDetails#property_linenumber)
-   [scriptId](../.././inspector/promises/~/Runtime.ExceptionDetails#property_scriptid)
-   [stackTrace](../.././inspector/promises/~/Runtime.ExceptionDetails#property_stacktrace)
-   [text](../.././inspector/promises/~/Runtime.ExceptionDetails#property_text)
-   [url](../.././inspector/promises/~/Runtime.ExceptionDetails#property_url)

I

[Runtime.ExceptionRevokedEventDataType](../.././inspector/promises/~/Runtime.ExceptionRevokedEventDataType "Runtime.ExceptionRevokedEventDataType")

No documentation available

-   [exceptionId](../.././inspector/promises/~/Runtime.ExceptionRevokedEventDataType#property_exceptionid)
-   [reason](../.././inspector/promises/~/Runtime.ExceptionRevokedEventDataType#property_reason)

I

[Runtime.ExceptionThrownEventDataType](../.././inspector/promises/~/Runtime.ExceptionThrownEventDataType "Runtime.ExceptionThrownEventDataType")

No documentation available

-   [exceptionDetails](../.././inspector/promises/~/Runtime.ExceptionThrownEventDataType#property_exceptiondetails)
-   [timestamp](../.././inspector/promises/~/Runtime.ExceptionThrownEventDataType#property_timestamp)

I

[Runtime.ExecutionContextCreatedEventDataType](../.././inspector/promises/~/Runtime.ExecutionContextCreatedEventDataType "Runtime.ExecutionContextCreatedEventDataType")

No documentation available

-   [context](../.././inspector/promises/~/Runtime.ExecutionContextCreatedEventDataType#property_context)

I

[Runtime.ExecutionContextDescription](../.././inspector/promises/~/Runtime.ExecutionContextDescription "Runtime.ExecutionContextDescription")

Description of an isolated world.

-   [auxData](../.././inspector/promises/~/Runtime.ExecutionContextDescription#property_auxdata)
-   [id](../.././inspector/promises/~/Runtime.ExecutionContextDescription#property_id)
-   [name](../.././inspector/promises/~/Runtime.ExecutionContextDescription#property_name)
-   [origin](../.././inspector/promises/~/Runtime.ExecutionContextDescription#property_origin)

I

[Runtime.ExecutionContextDestroyedEventDataType](../.././inspector/promises/~/Runtime.ExecutionContextDestroyedEventDataType "Runtime.ExecutionContextDestroyedEventDataType")

No documentation available

-   [executionContextId](../.././inspector/promises/~/Runtime.ExecutionContextDestroyedEventDataType#property_executioncontextid)

I

[Runtime.GetPropertiesParameterType](../.././inspector/promises/~/Runtime.GetPropertiesParameterType "Runtime.GetPropertiesParameterType")

No documentation available

-   [accessorPropertiesOnly](../.././inspector/promises/~/Runtime.GetPropertiesParameterType#property_accessorpropertiesonly)
-   [generatePreview](../.././inspector/promises/~/Runtime.GetPropertiesParameterType#property_generatepreview)
-   [objectId](../.././inspector/promises/~/Runtime.GetPropertiesParameterType#property_objectid)
-   [ownProperties](../.././inspector/promises/~/Runtime.GetPropertiesParameterType#property_ownproperties)

I

[Runtime.GetPropertiesReturnType](../.././inspector/promises/~/Runtime.GetPropertiesReturnType "Runtime.GetPropertiesReturnType")

No documentation available

-   [exceptionDetails](../.././inspector/promises/~/Runtime.GetPropertiesReturnType#property_exceptiondetails)
-   [internalProperties](../.././inspector/promises/~/Runtime.GetPropertiesReturnType#property_internalproperties)
-   [result](../.././inspector/promises/~/Runtime.GetPropertiesReturnType#property_result)

I

[Runtime.GlobalLexicalScopeNamesParameterType](../.././inspector/promises/~/Runtime.GlobalLexicalScopeNamesParameterType "Runtime.GlobalLexicalScopeNamesParameterType")

No documentation available

-   [executionContextId](../.././inspector/promises/~/Runtime.GlobalLexicalScopeNamesParameterType#property_executioncontextid)

I

[Runtime.GlobalLexicalScopeNamesReturnType](../.././inspector/promises/~/Runtime.GlobalLexicalScopeNamesReturnType "Runtime.GlobalLexicalScopeNamesReturnType")

No documentation available

-   [names](../.././inspector/promises/~/Runtime.GlobalLexicalScopeNamesReturnType#property_names)

I

[Runtime.InspectRequestedEventDataType](../.././inspector/promises/~/Runtime.InspectRequestedEventDataType "Runtime.InspectRequestedEventDataType")

No documentation available

-   [hints](../.././inspector/promises/~/Runtime.InspectRequestedEventDataType#property_hints)
-   [object](../.././inspector/promises/~/Runtime.InspectRequestedEventDataType#property_object)

I

[Runtime.InternalPropertyDescriptor](../.././inspector/promises/~/Runtime.InternalPropertyDescriptor "Runtime.InternalPropertyDescriptor")

Object internal property descriptor. This property isn't normally visible in JavaScript code.

-   [name](../.././inspector/promises/~/Runtime.InternalPropertyDescriptor#property_name)
-   [value](../.././inspector/promises/~/Runtime.InternalPropertyDescriptor#property_value)

I

[Runtime.ObjectPreview](../.././inspector/promises/~/Runtime.ObjectPreview "Runtime.ObjectPreview")

Object containing abbreviated remote object value.

-   [description](../.././inspector/promises/~/Runtime.ObjectPreview#property_description)
-   [entries](../.././inspector/promises/~/Runtime.ObjectPreview#property_entries)
-   [overflow](../.././inspector/promises/~/Runtime.ObjectPreview#property_overflow)
-   [properties](../.././inspector/promises/~/Runtime.ObjectPreview#property_properties)
-   [subtype](../.././inspector/promises/~/Runtime.ObjectPreview#property_subtype)
-   [type](../.././inspector/promises/~/Runtime.ObjectPreview#property_type)

I

[Runtime.PropertyDescriptor](../.././inspector/promises/~/Runtime.PropertyDescriptor "Runtime.PropertyDescriptor")

Object property descriptor.

-   [configurable](../.././inspector/promises/~/Runtime.PropertyDescriptor#property_configurable)
-   [enumerable](../.././inspector/promises/~/Runtime.PropertyDescriptor#property_enumerable)
-   [get](../.././inspector/promises/~/Runtime.PropertyDescriptor#property_get)
-   [isOwn](../.././inspector/promises/~/Runtime.PropertyDescriptor#property_isown)
-   [name](../.././inspector/promises/~/Runtime.PropertyDescriptor#property_name)
-   [set](../.././inspector/promises/~/Runtime.PropertyDescriptor#property_set)
-   [symbol](../.././inspector/promises/~/Runtime.PropertyDescriptor#property_symbol)
-   [value](../.././inspector/promises/~/Runtime.PropertyDescriptor#property_value)
-   [wasThrown](../.././inspector/promises/~/Runtime.PropertyDescriptor#property_wasthrown)
-   [writable](../.././inspector/promises/~/Runtime.PropertyDescriptor#property_writable)

I

[Runtime.PropertyPreview](../.././inspector/promises/~/Runtime.PropertyPreview "Runtime.PropertyPreview")

No documentation available

-   [name](../.././inspector/promises/~/Runtime.PropertyPreview#property_name)
-   [subtype](../.././inspector/promises/~/Runtime.PropertyPreview#property_subtype)
-   [type](../.././inspector/promises/~/Runtime.PropertyPreview#property_type)
-   [value](../.././inspector/promises/~/Runtime.PropertyPreview#property_value)
-   [valuePreview](../.././inspector/promises/~/Runtime.PropertyPreview#property_valuepreview)

I

[Runtime.QueryObjectsParameterType](../.././inspector/promises/~/Runtime.QueryObjectsParameterType "Runtime.QueryObjectsParameterType")

No documentation available

-   [prototypeObjectId](../.././inspector/promises/~/Runtime.QueryObjectsParameterType#property_prototypeobjectid)

I

[Runtime.QueryObjectsReturnType](../.././inspector/promises/~/Runtime.QueryObjectsReturnType "Runtime.QueryObjectsReturnType")

No documentation available

-   [objects](../.././inspector/promises/~/Runtime.QueryObjectsReturnType#property_objects)

I

[Runtime.ReleaseObjectGroupParameterType](../.././inspector/promises/~/Runtime.ReleaseObjectGroupParameterType "Runtime.ReleaseObjectGroupParameterType")

No documentation available

-   [objectGroup](../.././inspector/promises/~/Runtime.ReleaseObjectGroupParameterType#property_objectgroup)

I

[Runtime.ReleaseObjectParameterType](../.././inspector/promises/~/Runtime.ReleaseObjectParameterType "Runtime.ReleaseObjectParameterType")

No documentation available

-   [objectId](../.././inspector/promises/~/Runtime.ReleaseObjectParameterType#property_objectid)

I

[Runtime.RemoteObject](../.././inspector/promises/~/Runtime.RemoteObject "Runtime.RemoteObject")

Mirror object referencing original JavaScript object.

-   [className](../.././inspector/promises/~/Runtime.RemoteObject#property_classname)
-   [customPreview](../.././inspector/promises/~/Runtime.RemoteObject#property_custompreview)
-   [description](../.././inspector/promises/~/Runtime.RemoteObject#property_description)
-   [objectId](../.././inspector/promises/~/Runtime.RemoteObject#property_objectid)
-   [preview](../.././inspector/promises/~/Runtime.RemoteObject#property_preview)
-   [subtype](../.././inspector/promises/~/Runtime.RemoteObject#property_subtype)
-   [type](../.././inspector/promises/~/Runtime.RemoteObject#property_type)
-   [unserializableValue](../.././inspector/promises/~/Runtime.RemoteObject#property_unserializablevalue)
-   [value](../.././inspector/promises/~/Runtime.RemoteObject#property_value)

I

[Runtime.RunScriptParameterType](../.././inspector/promises/~/Runtime.RunScriptParameterType "Runtime.RunScriptParameterType")

No documentation available

-   [awaitPromise](../.././inspector/promises/~/Runtime.RunScriptParameterType#property_awaitpromise)
-   [executionContextId](../.././inspector/promises/~/Runtime.RunScriptParameterType#property_executioncontextid)
-   [generatePreview](../.././inspector/promises/~/Runtime.RunScriptParameterType#property_generatepreview)
-   [includeCommandLineAPI](../.././inspector/promises/~/Runtime.RunScriptParameterType#property_includecommandlineapi)
-   [objectGroup](../.././inspector/promises/~/Runtime.RunScriptParameterType#property_objectgroup)
-   [returnByValue](../.././inspector/promises/~/Runtime.RunScriptParameterType#property_returnbyvalue)
-   [scriptId](../.././inspector/promises/~/Runtime.RunScriptParameterType#property_scriptid)
-   [silent](../.././inspector/promises/~/Runtime.RunScriptParameterType#property_silent)

I

[Runtime.RunScriptReturnType](../.././inspector/promises/~/Runtime.RunScriptReturnType "Runtime.RunScriptReturnType")

No documentation available

-   [exceptionDetails](../.././inspector/promises/~/Runtime.RunScriptReturnType#property_exceptiondetails)
-   [result](../.././inspector/promises/~/Runtime.RunScriptReturnType#property_result)

I

[Runtime.SetCustomObjectFormatterEnabledParameterType](../.././inspector/promises/~/Runtime.SetCustomObjectFormatterEnabledParameterType "Runtime.SetCustomObjectFormatterEnabledParameterType")

No documentation available

-   [enabled](../.././inspector/promises/~/Runtime.SetCustomObjectFormatterEnabledParameterType#property_enabled)

I

[Runtime.StackTrace](../.././inspector/promises/~/Runtime.StackTrace "Runtime.StackTrace")

Call frames for assertions or error messages.

-   [callFrames](../.././inspector/promises/~/Runtime.StackTrace#property_callframes)
-   [description](../.././inspector/promises/~/Runtime.StackTrace#property_description)
-   [parent](../.././inspector/promises/~/Runtime.StackTrace#property_parent)
-   [parentId](../.././inspector/promises/~/Runtime.StackTrace#property_parentid)

I

[Runtime.StackTraceId](../.././inspector/promises/~/Runtime.StackTraceId "Runtime.StackTraceId")

If `debuggerId` is set stack trace comes from another debugger and can be resolved there. This allows to track cross-debugger calls. See `Runtime.StackTrace` and `Debugger.paused` for usages.

-   [debuggerId](../.././inspector/promises/~/Runtime.StackTraceId#property_debuggerid)
-   [id](../.././inspector/promises/~/Runtime.StackTraceId#property_id)

I

[Schema.Domain](../.././inspector/promises/~/Schema.Domain "Schema.Domain")

Description of the protocol domain.

-   [name](../.././inspector/promises/~/Schema.Domain#property_name)
-   [version](../.././inspector/promises/~/Schema.Domain#property_version)

I

[Schema.GetDomainsReturnType](../.././inspector/promises/~/Schema.GetDomainsReturnType "Schema.GetDomainsReturnType")

No documentation available

-   [domains](../.././inspector/promises/~/Schema.GetDomainsReturnType#property_domains)

N

[Console](../.././inspector/promises/~/Console "Console")

No documentation available

N

[Debugger](../.././inspector/promises/~/Debugger "Debugger")

No documentation available

N

[HeapProfiler](../.././inspector/promises/~/HeapProfiler "HeapProfiler")

No documentation available

N

[Network](../.././inspector/promises/~/Network "Network")

No documentation available

N

[NodeRuntime](../.././inspector/promises/~/NodeRuntime "NodeRuntime")

No documentation available

N

[NodeTracing](../.././inspector/promises/~/NodeTracing "NodeTracing")

No documentation available

N

[NodeWorker](../.././inspector/promises/~/NodeWorker "NodeWorker")

No documentation available

N

[Profiler](../.././inspector/promises/~/Profiler "Profiler")

No documentation available

N

[Runtime](../.././inspector/promises/~/Runtime "Runtime")

No documentation available

N

[Schema](../.././inspector/promises/~/Schema "Schema")

No documentation available

T

[Debugger.BreakpointId](../.././inspector/promises/~/Debugger.BreakpointId "Debugger.BreakpointId")

Breakpoint identifier.

T

[Debugger.CallFrameId](../.././inspector/promises/~/Debugger.CallFrameId "Debugger.CallFrameId")

Call frame identifier.

T

[HeapProfiler.HeapSnapshotObjectId](../.././inspector/promises/~/HeapProfiler.HeapSnapshotObjectId "HeapProfiler.HeapSnapshotObjectId")

Heap snapshot object id.

T

[Network.MonotonicTime](../.././inspector/promises/~/Network.MonotonicTime "Network.MonotonicTime")

Monotonically increasing time in seconds since an arbitrary point in the past.

T

[Network.RequestId](../.././inspector/promises/~/Network.RequestId "Network.RequestId")

Unique request identifier.

T

[Network.ResourceType](../.././inspector/promises/~/Network.ResourceType "Network.ResourceType")

Resource type as it was perceived by the rendering engine.

T

[Network.TimeSinceEpoch](../.././inspector/promises/~/Network.TimeSinceEpoch "Network.TimeSinceEpoch")

UTC time in seconds, counted from January 1, 1970.

T

[NodeWorker.SessionID](../.././inspector/promises/~/NodeWorker.SessionID "NodeWorker.SessionID")

Unique identifier of attached debugging session.

T

[NodeWorker.WorkerID](../.././inspector/promises/~/NodeWorker.WorkerID "NodeWorker.WorkerID")

No documentation available

T

[Runtime.ExecutionContextId](../.././inspector/promises/~/Runtime.ExecutionContextId "Runtime.ExecutionContextId")

Id of an execution context.

T

[Runtime.RemoteObjectId](../.././inspector/promises/~/Runtime.RemoteObjectId "Runtime.RemoteObjectId")

Unique object identifier.

T

[Runtime.ScriptId](../.././inspector/promises/~/Runtime.ScriptId "Runtime.ScriptId")

Unique script identifier.

T

[Runtime.Timestamp](../.././inspector/promises/~/Runtime.Timestamp "Runtime.Timestamp")

Number of milliseconds since epoch.

T

[Runtime.UniqueDebuggerId](../.././inspector/promises/~/Runtime.UniqueDebuggerId "Runtime.UniqueDebuggerId")

Unique identifier of current debugger.

T

[Runtime.UnserializableValue](../.././inspector/promises/~/Runtime.UnserializableValue "Runtime.UnserializableValue")

Primitive value which cannot be JSON-stringified.

v

[console](../.././inspector/~/console "console")

An object to send messages to the remote inspector console.
