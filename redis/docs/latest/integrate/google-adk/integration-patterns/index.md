---
title: "Memory integration patterns"
source: "https://redis.io/docs/latest/integrate/google-adk/integration-patterns/"
canonical_url: "https://redis.io/docs/latest/integrate/google-adk/integration-patterns/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:10.513Z"
content_hash: "1af3b75c1ab18c02712b2dc13957008e5311e1214e5e47732dbfebf40e5984f5"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis with Google Agent Development Kit (ADK)","→","Redis with Google Agent Development Kit (ADK)","→\n      \n        Memory integration patterns","→","Memory integration patterns"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis with Google Agent Development Kit (ADK)","→","Redis with Google Agent Development Kit (ADK)","→\n      \n        Memory integration patterns","→","Memory integration patterns"]
nav_prev: {"path": "redis/docs/latest/develop/ai/redisvl/install/index.md", "title": "Install RedisVL"}
nav_next: {"path": "redis/docs/latest/integrate/jedis/index.md", "title": "Java client for Redis"}
---

# Memory integration patterns

Three approaches for connecting Google ADK agents to Redis memory.

adk-redis offers three distinct approaches for connecting agents to memory. Each has different tradeoffs around control, complexity, and standardization.

## Comparison

Approach

Control

Complexity

Protocol

Best for

**ADK services**

Framework

Low

HTTP

Invisible infrastructure

**REST tools**

LLM

Medium

HTTP

Explicit memory management

**MCP tools**

LLM

Medium

SSE

Standardized, portable

## 1\. ADK services (framework-managed)

Configure `RedisWorkingMemorySessionService` and `RedisLongTermMemoryService`, pass them to the `Runner`, and the framework handles everything automatically. Memory extraction happens in the background. Search happens before each agent turn. The agent code never directly interacts with memory.

```python
from google.adk.runners import Runner
from adk_redis.sessions import (
    RedisWorkingMemorySessionService,
    RedisWorkingMemorySessionServiceConfig,
)
from adk_redis.memory import (
    RedisLongTermMemoryService,
    RedisLongTermMemoryServiceConfig,
)

runner = Runner(
    agent=agent,
    app_name="my_app",
    session_service=RedisWorkingMemorySessionService(
        config=RedisWorkingMemorySessionServiceConfig(
            api_base_url="http://localhost:8088",
            default_namespace="my_app",
        )
    ),
    memory_service=RedisLongTermMemoryService(
        config=RedisLongTermMemoryServiceConfig(
            api_base_url="http://localhost:8088",
            default_namespace="my_app",
        )
    ),
)
```

**Tradeoffs:** Simplest to implement, hardest to customize. The agent has no explicit control over what gets stored or when it searches.

## 2\. REST tools (LLM-controlled)

Give the agent explicit memory tools that the LLM calls like any other function. The LLM decides when to search memory, what to store, and what to update.

```python
from adk_redis.tools.memory import (
    SearchMemoryTool,
    CreateMemoryTool,
    UpdateMemoryTool,
    DeleteMemoryTool,
    MemoryToolConfig,
)

config = MemoryToolConfig(
    api_base_url="http://localhost:8088",
    default_namespace="my_app",
    recency_boost=True,
)

agent = Agent(
    model="gemini-2.5-flash",
    name="memory_agent",
    tools=[
        SearchMemoryTool(config=config),
        CreateMemoryTool(config=config),
        UpdateMemoryTool(config=config),
        DeleteMemoryTool(config=config),
    ],
)
```

**Tradeoffs:** Requires prompt engineering to teach the LLM memory management strategy, but gives the agent genuine autonomy over its own memory.

## 3\. MCP tools (Model Context Protocol)

Point ADK's `McpToolset` at the Agent Memory Server's SSE endpoint. Tool discovery happens automatically.

```python
from adk_redis.tools.mcp_memory import create_memory_mcp_toolset

memory_tools = create_memory_mcp_toolset(
    server_url="http://localhost:9000",
    tool_filter=["search_long_term_memory", "create_long_term_memories"],
)

agent = Agent(
    model="gemini-2.5-flash",
    name="mcp_agent",
    tools=[memory_tools],
)
```

Available MCP tools: `search_long_term_memory`, `create_long_term_memories`, `get_long_term_memory`, `edit_long_term_memory`, `delete_long_term_memories`, `memory_prompt`, `set_working_memory`.

**Tradeoffs:** Most standardized and portable approach. Swap memory backends without changing agent code. Requires Agent Memory Server with MCP support on a separate port.

## Hybrid approach

The most powerful configuration combines framework services with REST tools. Framework services handle session persistence and automatic background extraction. REST tools give the LLM explicit CRUD control on top.

```python
# LLM-controlled tools on the Agent
agent = Agent(
    model="gemini-2.5-flash",
    name="hybrid_agent",
    tools=[
        SearchMemoryTool(config=config),
        CreateMemoryTool(config=config),
        UpdateMemoryTool(config=config),
        DeleteMemoryTool(config=config),
    ],
)

# Framework-managed services on the Runner
runner = Runner(
    agent=agent,
    app_name="my_app",
    session_service=session_service,   # Auto session management
    memory_service=memory_service,     # Auto memory search
)
```

The [travel\_agent\_memory\_hybrid](https://github.com/redis-developer/adk-redis/tree/main/examples/travel_agent_memory_hybrid) example demonstrates this pattern.

## More info

*   [simple\_redis\_memory](https://github.com/redis-developer/adk-redis/tree/main/examples/simple_redis_memory): Framework-managed services
*   [travel\_agent\_memory\_tools](https://github.com/redis-developer/adk-redis/tree/main/examples/travel_agent_memory_tools): REST tools only
*   [fitness\_coach\_mcp](https://github.com/redis-developer/adk-redis/tree/main/examples/fitness_coach_mcp): MCP tools
*   [Car dealership tutorial](https://redis.io/tutorials/build-a-car-dealership-agent-with-google-adk-and-redis-agent-memory/)

## On this page

