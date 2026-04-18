---
title: "inspector - Node documentation"
source: "https://docs.deno.com/api/node/inspector/"
canonical_url: "https://docs.deno.com/api/node/inspector/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:05.556Z"
content_hash: "abb0fe967df0b3eb1742a04e82f22919128742c93118bb24b4b7b3eff4d7fe5d"
menu_path: ["inspector - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/https/index.md", "title": "https - Node documentation"}
nav_next: {"path": "deno/deno/api/node/inspector/promises/index.md", "title": "inspector/promises - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:inspector";
```

Deno compatibility

`console` is supported. Other APIs are non-functional stubs.

The `node:inspector` module provides an API for interacting with the V8 inspector.

### Classes [#](#Classes)

c

[Session](.././inspector/~/Session "Session")

The `inspector.Session` is used for dispatching messages to the V8 inspector back-end and receiving message responses and notifications.

*   [addListener](.././inspector/~/Session#method_addlistener_0)
*   [connect](.././inspector/~/Session#method_connect_0)
*   [connectToMainThread](.././inspector/~/Session#method_connecttomainthread_0)
*   [disconnect](.././inspector/~/Session#method_disconnect_0)
*   [emit](.././inspector/~/Session#method_emit_0)
*   [on](.././inspector/~/Session#method_on_0)
*   [once](.././inspector/~/Session#method_once_0)
*   [post](.././inspector/~/Session#method_post_0)
*   [prependListener](.././inspector/~/Session#method_prependlistener_0)
*   [prependOnceListener](.././inspector/~/Session#method_prependoncelistener_0)

### Functions [#](#Functions)

f

[close](.././inspector/~/close "close")

Deactivate the inspector. Blocks until there are no active connections.

f

[Network.loadingFailed](.././inspector/~/Network.loadingFailed "Network.loadingFailed")

This feature is only available with the `--experimental-network-inspection` flag enabled.

f

[Network.loadingFinished](.././inspector/~/Network.loadingFinished "Network.loadingFinished")

This feature is only available with the `--experimental-network-inspection` flag enabled.

f

[Network.requestWillBeSent](.././inspector/~/Network.requestWillBeSent "Network.requestWillBeSent")

This feature is only available with the `--experimental-network-inspection` flag enabled.

f

[Network.responseReceived](.././inspector/~/Network.responseReceived "Network.responseReceived")

This feature is only available with the `--experimental-network-inspection` flag enabled.

f

[open](.././inspector/~/open "open")

Activate inspector on host and port. Equivalent to `node --inspect=[[host:]port]`, but can be done programmatically after node has started.

f

[url](.././inspector/~/url "url")

Return the URL of the active inspector, or `undefined` if there is none.

f

[waitForDebugger](.././inspector/~/waitForDebugger "waitForDebugger")

Blocks until a client (existing or connected later) has sent `Runtime.runIfWaitingForDebugger` command.

### Interfaces [#](#Interfaces)

I

[Console.ConsoleMessage](.././inspector/~/Console.ConsoleMessage "Console.ConsoleMessage")

Console message.

*   [column](.././inspector/~/Console.ConsoleMessage#property_column)
*   [level](.././inspector/~/Console.ConsoleMessage#property_level)
*   [line](.././inspector/~/Console.ConsoleMessage#property_line)
*   [source](.././inspector/~/Console.ConsoleMessage#property_source)
*   [text](.././inspector/~/Console.ConsoleMessage#property_text)
*   [url](.././inspector/~/Console.ConsoleMessage#property_url)

I

[Console.MessageAddedEventDataType](.././inspector/~/Console.MessageAddedEventDataType "Console.MessageAddedEventDataType")

No documentation available

*   [message](.././inspector/~/Console.MessageAddedEventDataType#property_message)

I

[Debugger.BreakLocation](.././inspector/~/Debugger.BreakLocation "Debugger.BreakLocation")

No documentation available

*   [columnNumber](.././inspector/~/Debugger.BreakLocation#property_columnnumber)
*   [lineNumber](.././inspector/~/Debugger.BreakLocation#property_linenumber)
*   [scriptId](.././inspector/~/Debugger.BreakLocation#property_scriptid)
*   [type](.././inspector/~/Debugger.BreakLocation#property_type)

I

[Debugger.BreakpointResolvedEventDataType](.././inspector/~/Debugger.BreakpointResolvedEventDataType "Debugger.BreakpointResolvedEventDataType")

No documentation available

*   [breakpointId](.././inspector/~/Debugger.BreakpointResolvedEventDataType#property_breakpointid)
*   [location](.././inspector/~/Debugger.BreakpointResolvedEventDataType#property_location)

I

[Debugger.CallFrame](.././inspector/~/Debugger.CallFrame "Debugger.CallFrame")

JavaScript call frame. Array of call frames form the call stack.

*   [callFrameId](.././inspector/~/Debugger.CallFrame#property_callframeid)
*   [functionLocation](.././inspector/~/Debugger.CallFrame#property_functionlocation)
*   [functionName](.././inspector/~/Debugger.CallFrame#property_functionname)
*   [location](.././inspector/~/Debugger.CallFrame#property_location)
*   [returnValue](.././inspector/~/Debugger.CallFrame#property_returnvalue)
*   [scopeChain](.././inspector/~/Debugger.CallFrame#property_scopechain)
*   [this](.././inspector/~/Debugger.CallFrame#property_this)
*   [url](.././inspector/~/Debugger.CallFrame#property_url)

I

[Debugger.ContinueToLocationParameterType](.././inspector/~/Debugger.ContinueToLocationParameterType "Debugger.ContinueToLocationParameterType")

No documentation available

*   [location](.././inspector/~/Debugger.ContinueToLocationParameterType#property_location)
*   [targetCallFrames](.././inspector/~/Debugger.ContinueToLocationParameterType#property_targetcallframes)

I

[Debugger.EnableReturnType](.././inspector/~/Debugger.EnableReturnType "Debugger.EnableReturnType")

No documentation available

*   [debuggerId](.././inspector/~/Debugger.EnableReturnType#property_debuggerid)

I

[Debugger.EvaluateOnCallFrameParameterType](.././inspector/~/Debugger.EvaluateOnCallFrameParameterType "Debugger.EvaluateOnCallFrameParameterType")

No documentation available

*   [callFrameId](.././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_callframeid)
*   [expression](.././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_expression)
*   [generatePreview](.././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_generatepreview)
*   [includeCommandLineAPI](.././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_includecommandlineapi)
*   [objectGroup](.././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_objectgroup)
*   [returnByValue](.././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_returnbyvalue)
*   [silent](.././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_silent)
*   [throwOnSideEffect](.././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_throwonsideeffect)

I

[Debugger.EvaluateOnCallFrameReturnType](.././inspector/~/Debugger.EvaluateOnCallFrameReturnType "Debugger.EvaluateOnCallFrameReturnType")

No documentation available

*   [exceptionDetails](.././inspector/~/Debugger.EvaluateOnCallFrameReturnType#property_exceptiondetails)
*   [result](.././inspector/~/Debugger.EvaluateOnCallFrameReturnType#property_result)

I

[Debugger.GetPossibleBreakpointsParameterType](.././inspector/~/Debugger.GetPossibleBreakpointsParameterType "Debugger.GetPossibleBreakpointsParameterType")

No documentation available

*   [end](.././inspector/~/Debugger.GetPossibleBreakpointsParameterType#property_end)
*   [restrictToFunction](.././inspector/~/Debugger.GetPossibleBreakpointsParameterType#property_restricttofunction)
*   [start](.././inspector/~/Debugger.GetPossibleBreakpointsParameterType#property_start)

I

[Debugger.GetPossibleBreakpointsReturnType](.././inspector/~/Debugger.GetPossibleBreakpointsReturnType "Debugger.GetPossibleBreakpointsReturnType")

No documentation available

*   [locations](.././inspector/~/Debugger.GetPossibleBreakpointsReturnType#property_locations)

I

[Debugger.GetScriptSourceParameterType](.././inspector/~/Debugger.GetScriptSourceParameterType "Debugger.GetScriptSourceParameterType")

No documentation available

*   [scriptId](.././inspector/~/Debugger.GetScriptSourceParameterType#property_scriptid)

I

[Debugger.GetScriptSourceReturnType](.././inspector/~/Debugger.GetScriptSourceReturnType "Debugger.GetScriptSourceReturnType")

No documentation available

*   [scriptSource](.././inspector/~/Debugger.GetScriptSourceReturnType#property_scriptsource)

I

[Debugger.GetStackTraceParameterType](.././inspector/~/Debugger.GetStackTraceParameterType "Debugger.GetStackTraceParameterType")

No documentation available

*   [stackTraceId](.././inspector/~/Debugger.GetStackTraceParameterType#property_stacktraceid)

I

[Debugger.GetStackTraceReturnType](.././inspector/~/Debugger.GetStackTraceReturnType "Debugger.GetStackTraceReturnType")

No documentation available

*   [stackTrace](.././inspector/~/Debugger.GetStackTraceReturnType#property_stacktrace)

I

[Debugger.Location](.././inspector/~/Debugger.Location "Debugger.Location")

Location in the source code.

*   [columnNumber](.././inspector/~/Debugger.Location#property_columnnumber)
*   [lineNumber](.././inspector/~/Debugger.Location#property_linenumber)
*   [scriptId](.././inspector/~/Debugger.Location#property_scriptid)

I

[Debugger.PausedEventDataType](.././inspector/~/Debugger.PausedEventDataType "Debugger.PausedEventDataType")

No documentation available

*   [asyncCallStackTraceId](.././inspector/~/Debugger.PausedEventDataType#property_asynccallstacktraceid)
*   [asyncStackTrace](.././inspector/~/Debugger.PausedEventDataType#property_asyncstacktrace)
*   [asyncStackTraceId](.././inspector/~/Debugger.PausedEventDataType#property_asyncstacktraceid)
*   [callFrames](.././inspector/~/Debugger.PausedEventDataType#property_callframes)
*   [data](.././inspector/~/Debugger.PausedEventDataType#property_data)
*   [hitBreakpoints](.././inspector/~/Debugger.PausedEventDataType#property_hitbreakpoints)
*   [reason](.././inspector/~/Debugger.PausedEventDataType#property_reason)

I

[Debugger.PauseOnAsyncCallParameterType](.././inspector/~/Debugger.PauseOnAsyncCallParameterType "Debugger.PauseOnAsyncCallParameterType")

No documentation available

*   [parentStackTraceId](.././inspector/~/Debugger.PauseOnAsyncCallParameterType#property_parentstacktraceid)

I

[Debugger.RemoveBreakpointParameterType](.././inspector/~/Debugger.RemoveBreakpointParameterType "Debugger.RemoveBreakpointParameterType")

No documentation available

*   [breakpointId](.././inspector/~/Debugger.RemoveBreakpointParameterType#property_breakpointid)

I

[Debugger.RestartFrameParameterType](.././inspector/~/Debugger.RestartFrameParameterType "Debugger.RestartFrameParameterType")

No documentation available

*   [callFrameId](.././inspector/~/Debugger.RestartFrameParameterType#property_callframeid)

I

[Debugger.RestartFrameReturnType](.././inspector/~/Debugger.RestartFrameReturnType "Debugger.RestartFrameReturnType")

No documentation available

*   [asyncStackTrace](.././inspector/~/Debugger.RestartFrameReturnType#property_asyncstacktrace)
*   [asyncStackTraceId](.././inspector/~/Debugger.RestartFrameReturnType#property_asyncstacktraceid)
*   [callFrames](.././inspector/~/Debugger.RestartFrameReturnType#property_callframes)

I

[Debugger.Scope](.././inspector/~/Debugger.Scope "Debugger.Scope")

Scope description.

*   [endLocation](.././inspector/~/Debugger.Scope#property_endlocation)
*   [name](.././inspector/~/Debugger.Scope#property_name)
*   [object](.././inspector/~/Debugger.Scope#property_object)
*   [startLocation](.././inspector/~/Debugger.Scope#property_startlocation)
*   [type](.././inspector/~/Debugger.Scope#property_type)

I

[Debugger.ScriptFailedToParseEventDataType](.././inspector/~/Debugger.ScriptFailedToParseEventDataType "Debugger.ScriptFailedToParseEventDataType")

No documentation available

*   [endColumn](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_endcolumn)
*   [endLine](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_endline)
*   [executionContextAuxData](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_executioncontextauxdata)
*   [executionContextId](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_executioncontextid)
*   [hasSourceURL](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_hassourceurl)
*   [hash](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_hash)
*   [isModule](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_ismodule)
*   [length](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_length)
*   [scriptId](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_scriptid)
*   [sourceMapURL](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_sourcemapurl)
*   [stackTrace](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_stacktrace)
*   [startColumn](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_startcolumn)
*   [startLine](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_startline)
*   [url](.././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_url)

I

[Debugger.ScriptParsedEventDataType](.././inspector/~/Debugger.ScriptParsedEventDataType "Debugger.ScriptParsedEventDataType")

No documentation available

*   [endColumn](.././inspector/~/Debugger.ScriptParsedEventDataType#property_endcolumn)
*   [endLine](.././inspector/~/Debugger.ScriptParsedEventDataType#property_endline)
*   [executionContextAuxData](.././inspector/~/Debugger.ScriptParsedEventDataType#property_executioncontextauxdata)
*   [executionContextId](.././inspector/~/Debugger.ScriptParsedEventDataType#property_executioncontextid)
*   [hasSourceURL](.././inspector/~/Debugger.ScriptParsedEventDataType#property_hassourceurl)
*   [hash](.././inspector/~/Debugger.ScriptParsedEventDataType#property_hash)
*   [isLiveEdit](.././inspector/~/Debugger.ScriptParsedEventDataType#property_isliveedit)
*   [isModule](.././inspector/~/Debugger.ScriptParsedEventDataType#property_ismodule)
*   [length](.././inspector/~/Debugger.ScriptParsedEventDataType#property_length)
*   [scriptId](.././inspector/~/Debugger.ScriptParsedEventDataType#property_scriptid)
*   [sourceMapURL](.././inspector/~/Debugger.ScriptParsedEventDataType#property_sourcemapurl)
*   [stackTrace](.././inspector/~/Debugger.ScriptParsedEventDataType#property_stacktrace)
*   [startColumn](.././inspector/~/Debugger.ScriptParsedEventDataType#property_startcolumn)
*   [startLine](.././inspector/~/Debugger.ScriptParsedEventDataType#property_startline)
*   [url](.././inspector/~/Debugger.ScriptParsedEventDataType#property_url)

I

[Debugger.ScriptPosition](.././inspector/~/Debugger.ScriptPosition "Debugger.ScriptPosition")

Location in the source code.

*   [columnNumber](.././inspector/~/Debugger.ScriptPosition#property_columnnumber)
*   [lineNumber](.././inspector/~/Debugger.ScriptPosition#property_linenumber)

I

[Debugger.SearchInContentParameterType](.././inspector/~/Debugger.SearchInContentParameterType "Debugger.SearchInContentParameterType")

No documentation available

*   [caseSensitive](.././inspector/~/Debugger.SearchInContentParameterType#property_casesensitive)
*   [isRegex](.././inspector/~/Debugger.SearchInContentParameterType#property_isregex)
*   [query](.././inspector/~/Debugger.SearchInContentParameterType#property_query)
*   [scriptId](.././inspector/~/Debugger.SearchInContentParameterType#property_scriptid)

I

[Debugger.SearchInContentReturnType](.././inspector/~/Debugger.SearchInContentReturnType "Debugger.SearchInContentReturnType")

No documentation available

*   [result](.././inspector/~/Debugger.SearchInContentReturnType#property_result)

I

[Debugger.SearchMatch](.././inspector/~/Debugger.SearchMatch "Debugger.SearchMatch")

Search match for resource.

*   [lineContent](.././inspector/~/Debugger.SearchMatch#property_linecontent)
*   [lineNumber](.././inspector/~/Debugger.SearchMatch#property_linenumber)

I

[Debugger.SetAsyncCallStackDepthParameterType](.././inspector/~/Debugger.SetAsyncCallStackDepthParameterType "Debugger.SetAsyncCallStackDepthParameterType")

No documentation available

*   [maxDepth](.././inspector/~/Debugger.SetAsyncCallStackDepthParameterType#property_maxdepth)

I

[Debugger.SetBlackboxedRangesParameterType](.././inspector/~/Debugger.SetBlackboxedRangesParameterType "Debugger.SetBlackboxedRangesParameterType")

No documentation available

*   [positions](.././inspector/~/Debugger.SetBlackboxedRangesParameterType#property_positions)
*   [scriptId](.././inspector/~/Debugger.SetBlackboxedRangesParameterType#property_scriptid)

I

[Debugger.SetBlackboxPatternsParameterType](.././inspector/~/Debugger.SetBlackboxPatternsParameterType "Debugger.SetBlackboxPatternsParameterType")

No documentation available

*   [patterns](.././inspector/~/Debugger.SetBlackboxPatternsParameterType#property_patterns)

I

[Debugger.SetBreakpointByUrlParameterType](.././inspector/~/Debugger.SetBreakpointByUrlParameterType "Debugger.SetBreakpointByUrlParameterType")

No documentation available

*   [columnNumber](.././inspector/~/Debugger.SetBreakpointByUrlParameterType#property_columnnumber)
*   [condition](.././inspector/~/Debugger.SetBreakpointByUrlParameterType#property_condition)
*   [lineNumber](.././inspector/~/Debugger.SetBreakpointByUrlParameterType#property_linenumber)
*   [scriptHash](.././inspector/~/Debugger.SetBreakpointByUrlParameterType#property_scripthash)
*   [url](.././inspector/~/Debugger.SetBreakpointByUrlParameterType#property_url)
*   [urlRegex](.././inspector/~/Debugger.SetBreakpointByUrlParameterType#property_urlregex)

I

[Debugger.SetBreakpointByUrlReturnType](.././inspector/~/Debugger.SetBreakpointByUrlReturnType "Debugger.SetBreakpointByUrlReturnType")

No documentation available

*   [breakpointId](.././inspector/~/Debugger.SetBreakpointByUrlReturnType#property_breakpointid)
*   [locations](.././inspector/~/Debugger.SetBreakpointByUrlReturnType#property_locations)

I

[Debugger.SetBreakpointParameterType](.././inspector/~/Debugger.SetBreakpointParameterType "Debugger.SetBreakpointParameterType")

No documentation available

*   [condition](.././inspector/~/Debugger.SetBreakpointParameterType#property_condition)
*   [location](.././inspector/~/Debugger.SetBreakpointParameterType#property_location)

I

[Debugger.SetBreakpointReturnType](.././inspector/~/Debugger.SetBreakpointReturnType "Debugger.SetBreakpointReturnType")

No documentation available

*   [actualLocation](.././inspector/~/Debugger.SetBreakpointReturnType#property_actuallocation)
*   [breakpointId](.././inspector/~/Debugger.SetBreakpointReturnType#property_breakpointid)

I

[Debugger.SetBreakpointsActiveParameterType](.././inspector/~/Debugger.SetBreakpointsActiveParameterType "Debugger.SetBreakpointsActiveParameterType")

No documentation available

*   [active](.././inspector/~/Debugger.SetBreakpointsActiveParameterType#property_active)

I

[Debugger.SetPauseOnExceptionsParameterType](.././inspector/~/Debugger.SetPauseOnExceptionsParameterType "Debugger.SetPauseOnExceptionsParameterType")

No documentation available

*   [state](.././inspector/~/Debugger.SetPauseOnExceptionsParameterType#property_state)

I

[Debugger.SetReturnValueParameterType](.././inspector/~/Debugger.SetReturnValueParameterType "Debugger.SetReturnValueParameterType")

No documentation available

*   [newValue](.././inspector/~/Debugger.SetReturnValueParameterType#property_newvalue)

I

[Debugger.SetScriptSourceParameterType](.././inspector/~/Debugger.SetScriptSourceParameterType "Debugger.SetScriptSourceParameterType")

No documentation available

*   [dryRun](.././inspector/~/Debugger.SetScriptSourceParameterType#property_dryrun)
*   [scriptId](.././inspector/~/Debugger.SetScriptSourceParameterType#property_scriptid)
*   [scriptSource](.././inspector/~/Debugger.SetScriptSourceParameterType#property_scriptsource)

I

[Debugger.SetScriptSourceReturnType](.././inspector/~/Debugger.SetScriptSourceReturnType "Debugger.SetScriptSourceReturnType")

No documentation available

*   [asyncStackTrace](.././inspector/~/Debugger.SetScriptSourceReturnType#property_asyncstacktrace)
*   [asyncStackTraceId](.././inspector/~/Debugger.SetScriptSourceReturnType#property_asyncstacktraceid)
*   [callFrames](.././inspector/~/Debugger.SetScriptSourceReturnType#property_callframes)
*   [exceptionDetails](.././inspector/~/Debugger.SetScriptSourceReturnType#property_exceptiondetails)
*   [stackChanged](.././inspector/~/Debugger.SetScriptSourceReturnType#property_stackchanged)

I

[Debugger.SetSkipAllPausesParameterType](.././inspector/~/Debugger.SetSkipAllPausesParameterType "Debugger.SetSkipAllPausesParameterType")

No documentation available

*   [skip](.././inspector/~/Debugger.SetSkipAllPausesParameterType#property_skip)

I

[Debugger.SetVariableValueParameterType](.././inspector/~/Debugger.SetVariableValueParameterType "Debugger.SetVariableValueParameterType")

No documentation available

*   [callFrameId](.././inspector/~/Debugger.SetVariableValueParameterType#property_callframeid)
*   [newValue](.././inspector/~/Debugger.SetVariableValueParameterType#property_newvalue)
*   [scopeNumber](.././inspector/~/Debugger.SetVariableValueParameterType#property_scopenumber)
*   [variableName](.././inspector/~/Debugger.SetVariableValueParameterType#property_variablename)

I

[Debugger.StepIntoParameterType](.././inspector/~/Debugger.StepIntoParameterType "Debugger.StepIntoParameterType")

No documentation available

*   [breakOnAsyncCall](.././inspector/~/Debugger.StepIntoParameterType#property_breakonasynccall)

I

[HeapProfiler.AddHeapSnapshotChunkEventDataType](.././inspector/~/HeapProfiler.AddHeapSnapshotChunkEventDataType "HeapProfiler.AddHeapSnapshotChunkEventDataType")

No documentation available

*   [chunk](.././inspector/~/HeapProfiler.AddHeapSnapshotChunkEventDataType#property_chunk)

I

[HeapProfiler.AddInspectedHeapObjectParameterType](.././inspector/~/HeapProfiler.AddInspectedHeapObjectParameterType "HeapProfiler.AddInspectedHeapObjectParameterType")

No documentation available

*   [heapObjectId](.././inspector/~/HeapProfiler.AddInspectedHeapObjectParameterType#property_heapobjectid)

I

[HeapProfiler.GetHeapObjectIdParameterType](.././inspector/~/HeapProfiler.GetHeapObjectIdParameterType "HeapProfiler.GetHeapObjectIdParameterType")

No documentation available

*   [objectId](.././inspector/~/HeapProfiler.GetHeapObjectIdParameterType#property_objectid)

I

[HeapProfiler.GetHeapObjectIdReturnType](.././inspector/~/HeapProfiler.GetHeapObjectIdReturnType "HeapProfiler.GetHeapObjectIdReturnType")

No documentation available

*   [heapSnapshotObjectId](.././inspector/~/HeapProfiler.GetHeapObjectIdReturnType#property_heapsnapshotobjectid)

I

[HeapProfiler.GetObjectByHeapObjectIdParameterType](.././inspector/~/HeapProfiler.GetObjectByHeapObjectIdParameterType "HeapProfiler.GetObjectByHeapObjectIdParameterType")

No documentation available

*   [objectGroup](.././inspector/~/HeapProfiler.GetObjectByHeapObjectIdParameterType#property_objectgroup)
*   [objectId](.././inspector/~/HeapProfiler.GetObjectByHeapObjectIdParameterType#property_objectid)

I

[HeapProfiler.GetObjectByHeapObjectIdReturnType](.././inspector/~/HeapProfiler.GetObjectByHeapObjectIdReturnType "HeapProfiler.GetObjectByHeapObjectIdReturnType")

No documentation available

*   [result](.././inspector/~/HeapProfiler.GetObjectByHeapObjectIdReturnType#property_result)

I

[HeapProfiler.GetSamplingProfileReturnType](.././inspector/~/HeapProfiler.GetSamplingProfileReturnType "HeapProfiler.GetSamplingProfileReturnType")

No documentation available

*   [profile](.././inspector/~/HeapProfiler.GetSamplingProfileReturnType#property_profile)

I

[HeapProfiler.HeapStatsUpdateEventDataType](.././inspector/~/HeapProfiler.HeapStatsUpdateEventDataType "HeapProfiler.HeapStatsUpdateEventDataType")

No documentation available

*   [statsUpdate](.././inspector/~/HeapProfiler.HeapStatsUpdateEventDataType#property_statsupdate)

I

[HeapProfiler.LastSeenObjectIdEventDataType](.././inspector/~/HeapProfiler.LastSeenObjectIdEventDataType "HeapProfiler.LastSeenObjectIdEventDataType")

No documentation available

*   [lastSeenObjectId](.././inspector/~/HeapProfiler.LastSeenObjectIdEventDataType#property_lastseenobjectid)
*   [timestamp](.././inspector/~/HeapProfiler.LastSeenObjectIdEventDataType#property_timestamp)

I

[HeapProfiler.ReportHeapSnapshotProgressEventDataType](.././inspector/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType "HeapProfiler.ReportHeapSnapshotProgressEventDataType")

No documentation available

*   [done](.././inspector/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType#property_done)
*   [finished](.././inspector/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType#property_finished)
*   [total](.././inspector/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType#property_total)

I

[HeapProfiler.SamplingHeapProfile](.././inspector/~/HeapProfiler.SamplingHeapProfile "HeapProfiler.SamplingHeapProfile")

Profile.

*   [head](.././inspector/~/HeapProfiler.SamplingHeapProfile#property_head)

I

[HeapProfiler.SamplingHeapProfileNode](.././inspector/~/HeapProfiler.SamplingHeapProfileNode "HeapProfiler.SamplingHeapProfileNode")

Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes.

*   [callFrame](.././inspector/~/HeapProfiler.SamplingHeapProfileNode#property_callframe)
*   [children](.././inspector/~/HeapProfiler.SamplingHeapProfileNode#property_children)
*   [selfSize](.././inspector/~/HeapProfiler.SamplingHeapProfileNode#property_selfsize)

I

[HeapProfiler.StartSamplingParameterType](.././inspector/~/HeapProfiler.StartSamplingParameterType "HeapProfiler.StartSamplingParameterType")

No documentation available

*   [samplingInterval](.././inspector/~/HeapProfiler.StartSamplingParameterType#property_samplinginterval)

I

[HeapProfiler.StartTrackingHeapObjectsParameterType](.././inspector/~/HeapProfiler.StartTrackingHeapObjectsParameterType "HeapProfiler.StartTrackingHeapObjectsParameterType")

No documentation available

*   [trackAllocations](.././inspector/~/HeapProfiler.StartTrackingHeapObjectsParameterType#property_trackallocations)

I

[HeapProfiler.StopSamplingReturnType](.././inspector/~/HeapProfiler.StopSamplingReturnType "HeapProfiler.StopSamplingReturnType")

No documentation available

*   [profile](.././inspector/~/HeapProfiler.StopSamplingReturnType#property_profile)

I

[HeapProfiler.StopTrackingHeapObjectsParameterType](.././inspector/~/HeapProfiler.StopTrackingHeapObjectsParameterType "HeapProfiler.StopTrackingHeapObjectsParameterType")

No documentation available

*   [reportProgress](.././inspector/~/HeapProfiler.StopTrackingHeapObjectsParameterType#property_reportprogress)

I

[HeapProfiler.TakeHeapSnapshotParameterType](.././inspector/~/HeapProfiler.TakeHeapSnapshotParameterType "HeapProfiler.TakeHeapSnapshotParameterType")

No documentation available

*   [reportProgress](.././inspector/~/HeapProfiler.TakeHeapSnapshotParameterType#property_reportprogress)

I

[InspectorConsole](.././inspector/~/InspectorConsole "InspectorConsole")

No documentation available

*   [assert](.././inspector/~/InspectorConsole#method_assert_0)
*   [clear](.././inspector/~/InspectorConsole#method_clear_0)
*   [count](.././inspector/~/InspectorConsole#method_count_0)
*   [countReset](.././inspector/~/InspectorConsole#method_countreset_0)
*   [debug](.././inspector/~/InspectorConsole#method_debug_0)
*   [dir](.././inspector/~/InspectorConsole#method_dir_0)
*   [dirxml](.././inspector/~/InspectorConsole#method_dirxml_0)
*   [error](.././inspector/~/InspectorConsole#method_error_0)
*   [group](.././inspector/~/InspectorConsole#method_group_0)
*   [groupCollapsed](.././inspector/~/InspectorConsole#method_groupcollapsed_0)
*   [groupEnd](.././inspector/~/InspectorConsole#method_groupend_0)
*   [info](.././inspector/~/InspectorConsole#method_info_0)
*   [log](.././inspector/~/InspectorConsole#method_log_0)
*   [profile](.././inspector/~/InspectorConsole#method_profile_0)
*   [profileEnd](.././inspector/~/InspectorConsole#method_profileend_0)
*   [table](.././inspector/~/InspectorConsole#method_table_0)
*   [time](.././inspector/~/InspectorConsole#method_time_0)
*   [timeLog](.././inspector/~/InspectorConsole#method_timelog_0)
*   [timeStamp](.././inspector/~/InspectorConsole#method_timestamp_0)
*   [trace](.././inspector/~/InspectorConsole#method_trace_0)
*   [warn](.././inspector/~/InspectorConsole#method_warn_0)

I

[InspectorNotification](.././inspector/~/InspectorNotification "InspectorNotification")

No documentation available

*   [method](.././inspector/~/InspectorNotification#property_method)
*   [params](.././inspector/~/InspectorNotification#property_params)

I

[Network.Headers](.././inspector/~/Network.Headers "Network.Headers")

Request / response headers as keys / values of JSON object.

I

[Network.LoadingFailedEventDataType](.././inspector/~/Network.LoadingFailedEventDataType "Network.LoadingFailedEventDataType")

No documentation available

*   [errorText](.././inspector/~/Network.LoadingFailedEventDataType#property_errortext)
*   [requestId](.././inspector/~/Network.LoadingFailedEventDataType#property_requestid)
*   [timestamp](.././inspector/~/Network.LoadingFailedEventDataType#property_timestamp)
*   [type](.././inspector/~/Network.LoadingFailedEventDataType#property_type)

I

[Network.LoadingFinishedEventDataType](.././inspector/~/Network.LoadingFinishedEventDataType "Network.LoadingFinishedEventDataType")

No documentation available

*   [requestId](.././inspector/~/Network.LoadingFinishedEventDataType#property_requestid)
*   [timestamp](.././inspector/~/Network.LoadingFinishedEventDataType#property_timestamp)

I

[Network.Request](.././inspector/~/Network.Request "Network.Request")

HTTP request data.

*   [headers](.././inspector/~/Network.Request#property_headers)
*   [method](.././inspector/~/Network.Request#property_method)
*   [url](.././inspector/~/Network.Request#property_url)

I

[Network.RequestWillBeSentEventDataType](.././inspector/~/Network.RequestWillBeSentEventDataType "Network.RequestWillBeSentEventDataType")

No documentation available

*   [request](.././inspector/~/Network.RequestWillBeSentEventDataType#property_request)
*   [requestId](.././inspector/~/Network.RequestWillBeSentEventDataType#property_requestid)
*   [timestamp](.././inspector/~/Network.RequestWillBeSentEventDataType#property_timestamp)
*   [wallTime](.././inspector/~/Network.RequestWillBeSentEventDataType#property_walltime)

I

[Network.Response](.././inspector/~/Network.Response "Network.Response")

HTTP response data.

*   [headers](.././inspector/~/Network.Response#property_headers)
*   [status](.././inspector/~/Network.Response#property_status)
*   [statusText](.././inspector/~/Network.Response#property_statustext)
*   [url](.././inspector/~/Network.Response#property_url)

I

[Network.ResponseReceivedEventDataType](.././inspector/~/Network.ResponseReceivedEventDataType "Network.ResponseReceivedEventDataType")

No documentation available

*   [requestId](.././inspector/~/Network.ResponseReceivedEventDataType#property_requestid)
*   [response](.././inspector/~/Network.ResponseReceivedEventDataType#property_response)
*   [timestamp](.././inspector/~/Network.ResponseReceivedEventDataType#property_timestamp)
*   [type](.././inspector/~/Network.ResponseReceivedEventDataType#property_type)

I

[NodeRuntime.NotifyWhenWaitingForDisconnectParameterType](.././inspector/~/NodeRuntime.NotifyWhenWaitingForDisconnectParameterType "NodeRuntime.NotifyWhenWaitingForDisconnectParameterType")

No documentation available

*   [enabled](.././inspector/~/NodeRuntime.NotifyWhenWaitingForDisconnectParameterType#property_enabled)

I

[NodeTracing.DataCollectedEventDataType](.././inspector/~/NodeTracing.DataCollectedEventDataType "NodeTracing.DataCollectedEventDataType")

No documentation available

*   [value](.././inspector/~/NodeTracing.DataCollectedEventDataType#property_value)

I

[NodeTracing.GetCategoriesReturnType](.././inspector/~/NodeTracing.GetCategoriesReturnType "NodeTracing.GetCategoriesReturnType")

No documentation available

*   [categories](.././inspector/~/NodeTracing.GetCategoriesReturnType#property_categories)

I

[NodeTracing.StartParameterType](.././inspector/~/NodeTracing.StartParameterType "NodeTracing.StartParameterType")

No documentation available

*   [traceConfig](.././inspector/~/NodeTracing.StartParameterType#property_traceconfig)

I

[NodeTracing.TraceConfig](.././inspector/~/NodeTracing.TraceConfig "NodeTracing.TraceConfig")

No documentation available

*   [includedCategories](.././inspector/~/NodeTracing.TraceConfig#property_includedcategories)
*   [recordMode](.././inspector/~/NodeTracing.TraceConfig#property_recordmode)

I

[NodeWorker.AttachedToWorkerEventDataType](.././inspector/~/NodeWorker.AttachedToWorkerEventDataType "NodeWorker.AttachedToWorkerEventDataType")

No documentation available

*   [sessionId](.././inspector/~/NodeWorker.AttachedToWorkerEventDataType#property_sessionid)
*   [waitingForDebugger](.././inspector/~/NodeWorker.AttachedToWorkerEventDataType#property_waitingfordebugger)
*   [workerInfo](.././inspector/~/NodeWorker.AttachedToWorkerEventDataType#property_workerinfo)

I

[NodeWorker.DetachedFromWorkerEventDataType](.././inspector/~/NodeWorker.DetachedFromWorkerEventDataType "NodeWorker.DetachedFromWorkerEventDataType")

No documentation available

*   [sessionId](.././inspector/~/NodeWorker.DetachedFromWorkerEventDataType#property_sessionid)

I

[NodeWorker.DetachParameterType](.././inspector/~/NodeWorker.DetachParameterType "NodeWorker.DetachParameterType")

No documentation available

*   [sessionId](.././inspector/~/NodeWorker.DetachParameterType#property_sessionid)

I

[NodeWorker.EnableParameterType](.././inspector/~/NodeWorker.EnableParameterType "NodeWorker.EnableParameterType")

No documentation available

*   [waitForDebuggerOnStart](.././inspector/~/NodeWorker.EnableParameterType#property_waitfordebuggeronstart)

I

[NodeWorker.ReceivedMessageFromWorkerEventDataType](.././inspector/~/NodeWorker.ReceivedMessageFromWorkerEventDataType "NodeWorker.ReceivedMessageFromWorkerEventDataType")

No documentation available

*   [message](.././inspector/~/NodeWorker.ReceivedMessageFromWorkerEventDataType#property_message)
*   [sessionId](.././inspector/~/NodeWorker.ReceivedMessageFromWorkerEventDataType#property_sessionid)

I

[NodeWorker.SendMessageToWorkerParameterType](.././inspector/~/NodeWorker.SendMessageToWorkerParameterType "NodeWorker.SendMessageToWorkerParameterType")

No documentation available

*   [message](.././inspector/~/NodeWorker.SendMessageToWorkerParameterType#property_message)
*   [sessionId](.././inspector/~/NodeWorker.SendMessageToWorkerParameterType#property_sessionid)

I

[NodeWorker.WorkerInfo](.././inspector/~/NodeWorker.WorkerInfo "NodeWorker.WorkerInfo")

No documentation available

*   [title](.././inspector/~/NodeWorker.WorkerInfo#property_title)
*   [type](.././inspector/~/NodeWorker.WorkerInfo#property_type)
*   [url](.././inspector/~/NodeWorker.WorkerInfo#property_url)
*   [workerId](.././inspector/~/NodeWorker.WorkerInfo#property_workerid)

I

[Profiler.ConsoleProfileFinishedEventDataType](.././inspector/~/Profiler.ConsoleProfileFinishedEventDataType "Profiler.ConsoleProfileFinishedEventDataType")

No documentation available

*   [id](.././inspector/~/Profiler.ConsoleProfileFinishedEventDataType#property_id)
*   [location](.././inspector/~/Profiler.ConsoleProfileFinishedEventDataType#property_location)
*   [profile](.././inspector/~/Profiler.ConsoleProfileFinishedEventDataType#property_profile)
*   [title](.././inspector/~/Profiler.ConsoleProfileFinishedEventDataType#property_title)

I

[Profiler.ConsoleProfileStartedEventDataType](.././inspector/~/Profiler.ConsoleProfileStartedEventDataType "Profiler.ConsoleProfileStartedEventDataType")

No documentation available

*   [id](.././inspector/~/Profiler.ConsoleProfileStartedEventDataType#property_id)
*   [location](.././inspector/~/Profiler.ConsoleProfileStartedEventDataType#property_location)
*   [title](.././inspector/~/Profiler.ConsoleProfileStartedEventDataType#property_title)

I

[Profiler.CoverageRange](.././inspector/~/Profiler.CoverageRange "Profiler.CoverageRange")

Coverage data for a source range.

*   [count](.././inspector/~/Profiler.CoverageRange#property_count)
*   [endOffset](.././inspector/~/Profiler.CoverageRange#property_endoffset)
*   [startOffset](.././inspector/~/Profiler.CoverageRange#property_startoffset)

I

[Profiler.FunctionCoverage](.././inspector/~/Profiler.FunctionCoverage "Profiler.FunctionCoverage")

Coverage data for a JavaScript function.

*   [functionName](.././inspector/~/Profiler.FunctionCoverage#property_functionname)
*   [isBlockCoverage](.././inspector/~/Profiler.FunctionCoverage#property_isblockcoverage)
*   [ranges](.././inspector/~/Profiler.FunctionCoverage#property_ranges)

I

[Profiler.GetBestEffortCoverageReturnType](.././inspector/~/Profiler.GetBestEffortCoverageReturnType "Profiler.GetBestEffortCoverageReturnType")

No documentation available

*   [result](.././inspector/~/Profiler.GetBestEffortCoverageReturnType#property_result)

I

[Profiler.PositionTickInfo](.././inspector/~/Profiler.PositionTickInfo "Profiler.PositionTickInfo")

Specifies a number of samples attributed to a certain source position.

*   [line](.././inspector/~/Profiler.PositionTickInfo#property_line)
*   [ticks](.././inspector/~/Profiler.PositionTickInfo#property_ticks)

I

[Profiler.Profile](.././inspector/~/Profiler.Profile "Profiler.Profile")

Profile.

*   [endTime](.././inspector/~/Profiler.Profile#property_endtime)
*   [nodes](.././inspector/~/Profiler.Profile#property_nodes)
*   [samples](.././inspector/~/Profiler.Profile#property_samples)
*   [startTime](.././inspector/~/Profiler.Profile#property_starttime)
*   [timeDeltas](.././inspector/~/Profiler.Profile#property_timedeltas)

I

[Profiler.ProfileNode](.././inspector/~/Profiler.ProfileNode "Profiler.ProfileNode")

Profile node. Holds callsite information, execution statistics and child nodes.

*   [callFrame](.././inspector/~/Profiler.ProfileNode#property_callframe)
*   [children](.././inspector/~/Profiler.ProfileNode#property_children)
*   [deoptReason](.././inspector/~/Profiler.ProfileNode#property_deoptreason)
*   [hitCount](.././inspector/~/Profiler.ProfileNode#property_hitcount)
*   [id](.././inspector/~/Profiler.ProfileNode#property_id)
*   [positionTicks](.././inspector/~/Profiler.ProfileNode#property_positionticks)

I

[Profiler.ScriptCoverage](.././inspector/~/Profiler.ScriptCoverage "Profiler.ScriptCoverage")

Coverage data for a JavaScript script.

*   [functions](.././inspector/~/Profiler.ScriptCoverage#property_functions)
*   [scriptId](.././inspector/~/Profiler.ScriptCoverage#property_scriptid)
*   [url](.././inspector/~/Profiler.ScriptCoverage#property_url)

I

[Profiler.SetSamplingIntervalParameterType](.././inspector/~/Profiler.SetSamplingIntervalParameterType "Profiler.SetSamplingIntervalParameterType")

No documentation available

*   [interval](.././inspector/~/Profiler.SetSamplingIntervalParameterType#property_interval)

I

[Profiler.StartPreciseCoverageParameterType](.././inspector/~/Profiler.StartPreciseCoverageParameterType "Profiler.StartPreciseCoverageParameterType")

No documentation available

*   [callCount](.././inspector/~/Profiler.StartPreciseCoverageParameterType#property_callcount)
*   [detailed](.././inspector/~/Profiler.StartPreciseCoverageParameterType#property_detailed)

I

[Profiler.StopReturnType](.././inspector/~/Profiler.StopReturnType "Profiler.StopReturnType")

No documentation available

*   [profile](.././inspector/~/Profiler.StopReturnType#property_profile)

I

[Profiler.TakePreciseCoverageReturnType](.././inspector/~/Profiler.TakePreciseCoverageReturnType "Profiler.TakePreciseCoverageReturnType")

No documentation available

*   [result](.././inspector/~/Profiler.TakePreciseCoverageReturnType#property_result)

I

[Runtime.AwaitPromiseParameterType](.././inspector/~/Runtime.AwaitPromiseParameterType "Runtime.AwaitPromiseParameterType")

No documentation available

*   [generatePreview](.././inspector/~/Runtime.AwaitPromiseParameterType#property_generatepreview)
*   [promiseObjectId](.././inspector/~/Runtime.AwaitPromiseParameterType#property_promiseobjectid)
*   [returnByValue](.././inspector/~/Runtime.AwaitPromiseParameterType#property_returnbyvalue)

I

[Runtime.AwaitPromiseReturnType](.././inspector/~/Runtime.AwaitPromiseReturnType "Runtime.AwaitPromiseReturnType")

No documentation available

*   [exceptionDetails](.././inspector/~/Runtime.AwaitPromiseReturnType#property_exceptiondetails)
*   [result](.././inspector/~/Runtime.AwaitPromiseReturnType#property_result)

I

[Runtime.CallArgument](.././inspector/~/Runtime.CallArgument "Runtime.CallArgument")

Represents function call argument. Either remote object id `objectId`, primitive `value`, unserializable primitive value or neither of (for undefined) them should be specified.

*   [objectId](.././inspector/~/Runtime.CallArgument#property_objectid)
*   [unserializableValue](.././inspector/~/Runtime.CallArgument#property_unserializablevalue)
*   [value](.././inspector/~/Runtime.CallArgument#property_value)

I

[Runtime.CallFrame](.././inspector/~/Runtime.CallFrame "Runtime.CallFrame")

Stack entry for runtime errors and assertions.

*   [columnNumber](.././inspector/~/Runtime.CallFrame#property_columnnumber)
*   [functionName](.././inspector/~/Runtime.CallFrame#property_functionname)
*   [lineNumber](.././inspector/~/Runtime.CallFrame#property_linenumber)
*   [scriptId](.././inspector/~/Runtime.CallFrame#property_scriptid)
*   [url](.././inspector/~/Runtime.CallFrame#property_url)

I

[Runtime.CallFunctionOnParameterType](.././inspector/~/Runtime.CallFunctionOnParameterType "Runtime.CallFunctionOnParameterType")

No documentation available

*   [arguments](.././inspector/~/Runtime.CallFunctionOnParameterType#property_arguments)
*   [awaitPromise](.././inspector/~/Runtime.CallFunctionOnParameterType#property_awaitpromise)
*   [executionContextId](.././inspector/~/Runtime.CallFunctionOnParameterType#property_executioncontextid)
*   [functionDeclaration](.././inspector/~/Runtime.CallFunctionOnParameterType#property_functiondeclaration)
*   [generatePreview](.././inspector/~/Runtime.CallFunctionOnParameterType#property_generatepreview)
*   [objectGroup](.././inspector/~/Runtime.CallFunctionOnParameterType#property_objectgroup)
*   [objectId](.././inspector/~/Runtime.CallFunctionOnParameterType#property_objectid)
*   [returnByValue](.././inspector/~/Runtime.CallFunctionOnParameterType#property_returnbyvalue)
*   [silent](.././inspector/~/Runtime.CallFunctionOnParameterType#property_silent)
*   [userGesture](.././inspector/~/Runtime.CallFunctionOnParameterType#property_usergesture)

I

[Runtime.CallFunctionOnReturnType](.././inspector/~/Runtime.CallFunctionOnReturnType "Runtime.CallFunctionOnReturnType")

No documentation available

*   [exceptionDetails](.././inspector/~/Runtime.CallFunctionOnReturnType#property_exceptiondetails)
*   [result](.././inspector/~/Runtime.CallFunctionOnReturnType#property_result)

I

[Runtime.CompileScriptParameterType](.././inspector/~/Runtime.CompileScriptParameterType "Runtime.CompileScriptParameterType")

No documentation available

*   [executionContextId](.././inspector/~/Runtime.CompileScriptParameterType#property_executioncontextid)
*   [expression](.././inspector/~/Runtime.CompileScriptParameterType#property_expression)
*   [persistScript](.././inspector/~/Runtime.CompileScriptParameterType#property_persistscript)
*   [sourceURL](.././inspector/~/Runtime.CompileScriptParameterType#property_sourceurl)

I

[Runtime.CompileScriptReturnType](.././inspector/~/Runtime.CompileScriptReturnType "Runtime.CompileScriptReturnType")

No documentation available

*   [exceptionDetails](.././inspector/~/Runtime.CompileScriptReturnType#property_exceptiondetails)
*   [scriptId](.././inspector/~/Runtime.CompileScriptReturnType#property_scriptid)

I

[Runtime.ConsoleAPICalledEventDataType](.././inspector/~/Runtime.ConsoleAPICalledEventDataType "Runtime.ConsoleAPICalledEventDataType")

No documentation available

*   [args](.././inspector/~/Runtime.ConsoleAPICalledEventDataType#property_args)
*   [context](.././inspector/~/Runtime.ConsoleAPICalledEventDataType#property_context)
*   [executionContextId](.././inspector/~/Runtime.ConsoleAPICalledEventDataType#property_executioncontextid)
*   [stackTrace](.././inspector/~/Runtime.ConsoleAPICalledEventDataType#property_stacktrace)
*   [timestamp](.././inspector/~/Runtime.ConsoleAPICalledEventDataType#property_timestamp)
*   [type](.././inspector/~/Runtime.ConsoleAPICalledEventDataType#property_type)

I

[Runtime.CustomPreview](.././inspector/~/Runtime.CustomPreview "Runtime.CustomPreview")

No documentation available

*   [bindRemoteObjectFunctionId](.././inspector/~/Runtime.CustomPreview#property_bindremoteobjectfunctionid)
*   [configObjectId](.././inspector/~/Runtime.CustomPreview#property_configobjectid)
*   [formatterObjectId](.././inspector/~/Runtime.CustomPreview#property_formatterobjectid)
*   [hasBody](.././inspector/~/Runtime.CustomPreview#property_hasbody)
*   [header](.././inspector/~/Runtime.CustomPreview#property_header)

I

[Runtime.EntryPreview](.././inspector/~/Runtime.EntryPreview "Runtime.EntryPreview")

No documentation available

*   [key](.././inspector/~/Runtime.EntryPreview#property_key)
*   [value](.././inspector/~/Runtime.EntryPreview#property_value)

I

[Runtime.EvaluateParameterType](.././inspector/~/Runtime.EvaluateParameterType "Runtime.EvaluateParameterType")

No documentation available

*   [awaitPromise](.././inspector/~/Runtime.EvaluateParameterType#property_awaitpromise)
*   [contextId](.././inspector/~/Runtime.EvaluateParameterType#property_contextid)
*   [expression](.././inspector/~/Runtime.EvaluateParameterType#property_expression)
*   [generatePreview](.././inspector/~/Runtime.EvaluateParameterType#property_generatepreview)
*   [includeCommandLineAPI](.././inspector/~/Runtime.EvaluateParameterType#property_includecommandlineapi)
*   [objectGroup](.././inspector/~/Runtime.EvaluateParameterType#property_objectgroup)
*   [returnByValue](.././inspector/~/Runtime.EvaluateParameterType#property_returnbyvalue)
*   [silent](.././inspector/~/Runtime.EvaluateParameterType#property_silent)
*   [userGesture](.././inspector/~/Runtime.EvaluateParameterType#property_usergesture)

I

[Runtime.EvaluateReturnType](.././inspector/~/Runtime.EvaluateReturnType "Runtime.EvaluateReturnType")

No documentation available

*   [exceptionDetails](.././inspector/~/Runtime.EvaluateReturnType#property_exceptiondetails)
*   [result](.././inspector/~/Runtime.EvaluateReturnType#property_result)

I

[Runtime.ExceptionDetails](.././inspector/~/Runtime.ExceptionDetails "Runtime.ExceptionDetails")

Detailed information about exception (or error) that was thrown during script compilation or execution.

*   [columnNumber](.././inspector/~/Runtime.ExceptionDetails#property_columnnumber)
*   [exception](.././inspector/~/Runtime.ExceptionDetails#property_exception)
*   [exceptionId](.././inspector/~/Runtime.ExceptionDetails#property_exceptionid)
*   [executionContextId](.././inspector/~/Runtime.ExceptionDetails#property_executioncontextid)
*   [lineNumber](.././inspector/~/Runtime.ExceptionDetails#property_linenumber)
*   [scriptId](.././inspector/~/Runtime.ExceptionDetails#property_scriptid)
*   [stackTrace](.././inspector/~/Runtime.ExceptionDetails#property_stacktrace)
*   [text](.././inspector/~/Runtime.ExceptionDetails#property_text)
*   [url](.././inspector/~/Runtime.ExceptionDetails#property_url)

I

[Runtime.ExceptionRevokedEventDataType](.././inspector/~/Runtime.ExceptionRevokedEventDataType "Runtime.ExceptionRevokedEventDataType")

No documentation available

*   [exceptionId](.././inspector/~/Runtime.ExceptionRevokedEventDataType#property_exceptionid)
*   [reason](.././inspector/~/Runtime.ExceptionRevokedEventDataType#property_reason)

I

[Runtime.ExceptionThrownEventDataType](.././inspector/~/Runtime.ExceptionThrownEventDataType "Runtime.ExceptionThrownEventDataType")

No documentation available

*   [exceptionDetails](.././inspector/~/Runtime.ExceptionThrownEventDataType#property_exceptiondetails)
*   [timestamp](.././inspector/~/Runtime.ExceptionThrownEventDataType#property_timestamp)

I

[Runtime.ExecutionContextCreatedEventDataType](.././inspector/~/Runtime.ExecutionContextCreatedEventDataType "Runtime.ExecutionContextCreatedEventDataType")

No documentation available

*   [context](.././inspector/~/Runtime.ExecutionContextCreatedEventDataType#property_context)

I

[Runtime.ExecutionContextDescription](.././inspector/~/Runtime.ExecutionContextDescription "Runtime.ExecutionContextDescription")

Description of an isolated world.

*   [auxData](.././inspector/~/Runtime.ExecutionContextDescription#property_auxdata)
*   [id](.././inspector/~/Runtime.ExecutionContextDescription#property_id)
*   [name](.././inspector/~/Runtime.ExecutionContextDescription#property_name)
*   [origin](.././inspector/~/Runtime.ExecutionContextDescription#property_origin)

I

[Runtime.ExecutionContextDestroyedEventDataType](.././inspector/~/Runtime.ExecutionContextDestroyedEventDataType "Runtime.ExecutionContextDestroyedEventDataType")

No documentation available

*   [executionContextId](.././inspector/~/Runtime.ExecutionContextDestroyedEventDataType#property_executioncontextid)

I

[Runtime.GetPropertiesParameterType](.././inspector/~/Runtime.GetPropertiesParameterType "Runtime.GetPropertiesParameterType")

No documentation available

*   [accessorPropertiesOnly](.././inspector/~/Runtime.GetPropertiesParameterType#property_accessorpropertiesonly)
*   [generatePreview](.././inspector/~/Runtime.GetPropertiesParameterType#property_generatepreview)
*   [objectId](.././inspector/~/Runtime.GetPropertiesParameterType#property_objectid)
*   [ownProperties](.././inspector/~/Runtime.GetPropertiesParameterType#property_ownproperties)

I

[Runtime.GetPropertiesReturnType](.././inspector/~/Runtime.GetPropertiesReturnType "Runtime.GetPropertiesReturnType")

No documentation available

*   [exceptionDetails](.././inspector/~/Runtime.GetPropertiesReturnType#property_exceptiondetails)
*   [internalProperties](.././inspector/~/Runtime.GetPropertiesReturnType#property_internalproperties)
*   [result](.././inspector/~/Runtime.GetPropertiesReturnType#property_result)

I

[Runtime.GlobalLexicalScopeNamesParameterType](.././inspector/~/Runtime.GlobalLexicalScopeNamesParameterType "Runtime.GlobalLexicalScopeNamesParameterType")

No documentation available

*   [executionContextId](.././inspector/~/Runtime.GlobalLexicalScopeNamesParameterType#property_executioncontextid)

I

[Runtime.GlobalLexicalScopeNamesReturnType](.././inspector/~/Runtime.GlobalLexicalScopeNamesReturnType "Runtime.GlobalLexicalScopeNamesReturnType")

No documentation available

*   [names](.././inspector/~/Runtime.GlobalLexicalScopeNamesReturnType#property_names)

I

[Runtime.InspectRequestedEventDataType](.././inspector/~/Runtime.InspectRequestedEventDataType "Runtime.InspectRequestedEventDataType")

No documentation available

*   [hints](.././inspector/~/Runtime.InspectRequestedEventDataType#property_hints)
*   [object](.././inspector/~/Runtime.InspectRequestedEventDataType#property_object)

I

[Runtime.InternalPropertyDescriptor](.././inspector/~/Runtime.InternalPropertyDescriptor "Runtime.InternalPropertyDescriptor")

Object internal property descriptor. This property isn't normally visible in JavaScript code.

*   [name](.././inspector/~/Runtime.InternalPropertyDescriptor#property_name)
*   [value](.././inspector/~/Runtime.InternalPropertyDescriptor#property_value)

I

[Runtime.ObjectPreview](.././inspector/~/Runtime.ObjectPreview "Runtime.ObjectPreview")

Object containing abbreviated remote object value.

*   [description](.././inspector/~/Runtime.ObjectPreview#property_description)
*   [entries](.././inspector/~/Runtime.ObjectPreview#property_entries)
*   [overflow](.././inspector/~/Runtime.ObjectPreview#property_overflow)
*   [properties](.././inspector/~/Runtime.ObjectPreview#property_properties)
*   [subtype](.././inspector/~/Runtime.ObjectPreview#property_subtype)
*   [type](.././inspector/~/Runtime.ObjectPreview#property_type)

I

[Runtime.PropertyDescriptor](.././inspector/~/Runtime.PropertyDescriptor "Runtime.PropertyDescriptor")

Object property descriptor.

*   [configurable](.././inspector/~/Runtime.PropertyDescriptor#property_configurable)
*   [enumerable](.././inspector/~/Runtime.PropertyDescriptor#property_enumerable)
*   [get](.././inspector/~/Runtime.PropertyDescriptor#property_get)
*   [isOwn](.././inspector/~/Runtime.PropertyDescriptor#property_isown)
*   [name](.././inspector/~/Runtime.PropertyDescriptor#property_name)
*   [set](.././inspector/~/Runtime.PropertyDescriptor#property_set)
*   [symbol](.././inspector/~/Runtime.PropertyDescriptor#property_symbol)
*   [value](.././inspector/~/Runtime.PropertyDescriptor#property_value)
*   [wasThrown](.././inspector/~/Runtime.PropertyDescriptor#property_wasthrown)
*   [writable](.././inspector/~/Runtime.PropertyDescriptor#property_writable)

I

[Runtime.PropertyPreview](.././inspector/~/Runtime.PropertyPreview "Runtime.PropertyPreview")

No documentation available

*   [name](.././inspector/~/Runtime.PropertyPreview#property_name)
*   [subtype](.././inspector/~/Runtime.PropertyPreview#property_subtype)
*   [type](.././inspector/~/Runtime.PropertyPreview#property_type)
*   [value](.././inspector/~/Runtime.PropertyPreview#property_value)
*   [valuePreview](.././inspector/~/Runtime.PropertyPreview#property_valuepreview)

I

[Runtime.QueryObjectsParameterType](.././inspector/~/Runtime.QueryObjectsParameterType "Runtime.QueryObjectsParameterType")

No documentation available

*   [prototypeObjectId](.././inspector/~/Runtime.QueryObjectsParameterType#property_prototypeobjectid)

I

[Runtime.QueryObjectsReturnType](.././inspector/~/Runtime.QueryObjectsReturnType "Runtime.QueryObjectsReturnType")

No documentation available

*   [objects](.././inspector/~/Runtime.QueryObjectsReturnType#property_objects)

I

[Runtime.ReleaseObjectGroupParameterType](.././inspector/~/Runtime.ReleaseObjectGroupParameterType "Runtime.ReleaseObjectGroupParameterType")

No documentation available

*   [objectGroup](.././inspector/~/Runtime.ReleaseObjectGroupParameterType#property_objectgroup)

I

[Runtime.ReleaseObjectParameterType](.././inspector/~/Runtime.ReleaseObjectParameterType "Runtime.ReleaseObjectParameterType")

No documentation available

*   [objectId](.././inspector/~/Runtime.ReleaseObjectParameterType#property_objectid)

I

[Runtime.RemoteObject](.././inspector/~/Runtime.RemoteObject "Runtime.RemoteObject")

Mirror object referencing original JavaScript object.

*   [className](.././inspector/~/Runtime.RemoteObject#property_classname)
*   [customPreview](.././inspector/~/Runtime.RemoteObject#property_custompreview)
*   [description](.././inspector/~/Runtime.RemoteObject#property_description)
*   [objectId](.././inspector/~/Runtime.RemoteObject#property_objectid)
*   [preview](.././inspector/~/Runtime.RemoteObject#property_preview)
*   [subtype](.././inspector/~/Runtime.RemoteObject#property_subtype)
*   [type](.././inspector/~/Runtime.RemoteObject#property_type)
*   [unserializableValue](.././inspector/~/Runtime.RemoteObject#property_unserializablevalue)
*   [value](.././inspector/~/Runtime.RemoteObject#property_value)

I

[Runtime.RunScriptParameterType](.././inspector/~/Runtime.RunScriptParameterType "Runtime.RunScriptParameterType")

No documentation available

*   [awaitPromise](.././inspector/~/Runtime.RunScriptParameterType#property_awaitpromise)
*   [executionContextId](.././inspector/~/Runtime.RunScriptParameterType#property_executioncontextid)
*   [generatePreview](.././inspector/~/Runtime.RunScriptParameterType#property_generatepreview)
*   [includeCommandLineAPI](.././inspector/~/Runtime.RunScriptParameterType#property_includecommandlineapi)
*   [objectGroup](.././inspector/~/Runtime.RunScriptParameterType#property_objectgroup)
*   [returnByValue](.././inspector/~/Runtime.RunScriptParameterType#property_returnbyvalue)
*   [scriptId](.././inspector/~/Runtime.RunScriptParameterType#property_scriptid)
*   [silent](.././inspector/~/Runtime.RunScriptParameterType#property_silent)

I

[Runtime.RunScriptReturnType](.././inspector/~/Runtime.RunScriptReturnType "Runtime.RunScriptReturnType")

No documentation available

*   [exceptionDetails](.././inspector/~/Runtime.RunScriptReturnType#property_exceptiondetails)
*   [result](.././inspector/~/Runtime.RunScriptReturnType#property_result)

I

[Runtime.SetCustomObjectFormatterEnabledParameterType](.././inspector/~/Runtime.SetCustomObjectFormatterEnabledParameterType "Runtime.SetCustomObjectFormatterEnabledParameterType")

No documentation available

*   [enabled](.././inspector/~/Runtime.SetCustomObjectFormatterEnabledParameterType#property_enabled)

I

[Runtime.StackTrace](.././inspector/~/Runtime.StackTrace "Runtime.StackTrace")

Call frames for assertions or error messages.

*   [callFrames](.././inspector/~/Runtime.StackTrace#property_callframes)
*   [description](.././inspector/~/Runtime.StackTrace#property_description)
*   [parent](.././inspector/~/Runtime.StackTrace#property_parent)
*   [parentId](.././inspector/~/Runtime.StackTrace#property_parentid)

I

[Runtime.StackTraceId](.././inspector/~/Runtime.StackTraceId "Runtime.StackTraceId")

If `debuggerId` is set stack trace comes from another debugger and can be resolved there. This allows to track cross-debugger calls. See `Runtime.StackTrace` and `Debugger.paused` for usages.

*   [debuggerId](.././inspector/~/Runtime.StackTraceId#property_debuggerid)
*   [id](.././inspector/~/Runtime.StackTraceId#property_id)

I

[Schema.Domain](.././inspector/~/Schema.Domain "Schema.Domain")

Description of the protocol domain.

*   [name](.././inspector/~/Schema.Domain#property_name)
*   [version](.././inspector/~/Schema.Domain#property_version)

I

[Schema.GetDomainsReturnType](.././inspector/~/Schema.GetDomainsReturnType "Schema.GetDomainsReturnType")

No documentation available

*   [domains](.././inspector/~/Schema.GetDomainsReturnType#property_domains)

### Namespaces [#](#Namespaces)

N

[Console](.././inspector/~/Console "Console")

No documentation available

N

[Debugger](.././inspector/~/Debugger "Debugger")

No documentation available

N

[HeapProfiler](.././inspector/~/HeapProfiler "HeapProfiler")

No documentation available

N

[Network](.././inspector/~/Network "Network")

No documentation available

N

[NodeRuntime](.././inspector/~/NodeRuntime "NodeRuntime")

No documentation available

N

[NodeTracing](.././inspector/~/NodeTracing "NodeTracing")

No documentation available

N

[NodeWorker](.././inspector/~/NodeWorker "NodeWorker")

No documentation available

N

[Profiler](.././inspector/~/Profiler "Profiler")

No documentation available

N

[Runtime](.././inspector/~/Runtime "Runtime")

No documentation available

N

[Schema](.././inspector/~/Schema "Schema")

No documentation available

### Type Aliases [#](<#Type Aliases>)

T

[Debugger.BreakpointId](.././inspector/~/Debugger.BreakpointId "Debugger.BreakpointId")

Breakpoint identifier.

T

[Debugger.CallFrameId](.././inspector/~/Debugger.CallFrameId "Debugger.CallFrameId")

Call frame identifier.

T

[HeapProfiler.HeapSnapshotObjectId](.././inspector/~/HeapProfiler.HeapSnapshotObjectId "HeapProfiler.HeapSnapshotObjectId")

Heap snapshot object id.

T

[Network.MonotonicTime](.././inspector/~/Network.MonotonicTime "Network.MonotonicTime")

Monotonically increasing time in seconds since an arbitrary point in the past.

T

[Network.RequestId](.././inspector/~/Network.RequestId "Network.RequestId")

Unique request identifier.

T

[Network.ResourceType](.././inspector/~/Network.ResourceType "Network.ResourceType")

Resource type as it was perceived by the rendering engine.

T

[Network.TimeSinceEpoch](.././inspector/~/Network.TimeSinceEpoch "Network.TimeSinceEpoch")

UTC time in seconds, counted from January 1, 1970.

T

[NodeWorker.SessionID](.././inspector/~/NodeWorker.SessionID "NodeWorker.SessionID")

Unique identifier of attached debugging session.

T

[NodeWorker.WorkerID](.././inspector/~/NodeWorker.WorkerID "NodeWorker.WorkerID")

No documentation available

T

[Runtime.ExecutionContextId](.././inspector/~/Runtime.ExecutionContextId "Runtime.ExecutionContextId")

Id of an execution context.

T

[Runtime.RemoteObjectId](.././inspector/~/Runtime.RemoteObjectId "Runtime.RemoteObjectId")

Unique object identifier.

T

[Runtime.ScriptId](.././inspector/~/Runtime.ScriptId "Runtime.ScriptId")

Unique script identifier.

T

[Runtime.Timestamp](.././inspector/~/Runtime.Timestamp "Runtime.Timestamp")

Number of milliseconds since epoch.

T

[Runtime.UniqueDebuggerId](.././inspector/~/Runtime.UniqueDebuggerId "Runtime.UniqueDebuggerId")

Unique identifier of current debugger.

T

[Runtime.UnserializableValue](.././inspector/~/Runtime.UnserializableValue "Runtime.UnserializableValue")

Primitive value which cannot be JSON-stringified.

### Variables [#](#Variables)

v

[console](.././inspector/~/console "console")

An object to send messages to the remote inspector console.
