---
title: "Add Stripe to your agentic workflows"
source: "https://docs.stripe.com/agents"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:48:52.865Z"
content_hash: "36a31836b4eaa62a08924aacc1fca0be32ba6bc83e684c14976bd114d0592b1c"
---

## Use financial services with agents.

Use Stripe to run your agent business and enhance your agents’ functionality. By enabling access to financial services and tools, you allow your agents to help you earn and spend funds, expanding their capabilities.

## Create Stripe objects

Use function calling to create and manage Stripe objects. For example, dynamically create [Payment Links](https://docs.stripe.com/payment-links) to accept funds, integrate into your support workflows to help customers, and scaffold test data.

The Stripe agent toolkit supports [OpenAI’s Agents SDK](https://github.com/openai/openai-agents-python), [Vercel’s AI SDK](https://sdk.vercel.ai/), [LangChain](https://www.langchain.com/), and [CrewAI](https://www.crewai.com/). It works with any LLM provider that supports function calling and is compatible with Python and TypeScript.

`import asyncio import os from agents import Agent, Runner from stripe_agent_toolkit.openai.toolkit import create_stripe_agent_toolkit  async def main():     # Initialize toolkit - use restricted key (rk_*) for better security     toolkit = await create_stripe_agent_toolkit(         secret_key=os.getenv("STRIPE_SECRET_KEY")     )      try:         agent = Agent(             name="Stripe Agent",             instructions="Integrate with Stripe effectively to support business needs.",             tools=toolkit.get_tools()         )          assignment = "Create a payment link for a new product called \"Test\" with a price of $100."         result = await Runner.run(agent, assignment)         print(result.final_output)     finally:         await toolkit.close()  if __name__ == "__main__":     asyncio.run(main())`

#### Developer preview

Learn how to use this SDK to integrate Stripe into agentic workflows. Because agent behavior is non-deterministic, use the SDK in a [sandbox](https://docs.stripe.com/sandboxes) and run evaluations to assess your application’s performance.

For security, we strongly recommend using [restricted API keys](https://docs.stripe.com/keys#create-restricted-api-secret-key) (`rk_*`) to limit your agent’s access to only the functionality it requires, especially in live mode. Tool availability is determined by the permissions you configure on the restricted key.

## Interested in adding Stripe to your agent workflows?

Enter your email address below.
