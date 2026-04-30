---
title: "Build agentic AI SaaS Billing workflows"
source: "https://docs.stripe.com/agents-billing-workflows"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:44:53.752Z"
content_hash: "eb7d5ab7cb719a8fa5b29c19151f752001fa2c54e340784c230dbe8bc42cfde4"
---

You can enable your AI agents to create and manage subscription-based SaaS Billing programs with Stripe. In this guide, you’ll learn how to:

*   Provision a new customer and subscription
*   Respond to subscription lifecycle events using webhooks
*   Invoke billing actions from an AI agent using the agent toolkit

## Before you begin

This guide assumes you have a working agent toolkit setup and a Stripe account. You’ll link to these resources throughout:

*   [Agent toolkit](https://docs.stripe.com/agents)
*   [Adding payments to your agentic workflows](http://stripe.dev/blog/adding-payments-to-your-agentic-workflows)
*   [Building subscriptions](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
*   [Subscriptions](https://docs.stripe.com/subscriptions)
*   [Webhooks](https://docs.stripe.com/webhooks)
*   [Testing your integration](https://docs.stripe.com/testing)

Additionally, make sure that you have the following:

*   Node.js 14 or later and an existing agent toolkit project
*   A Stripe test account with API keys
*   Either the Stripe Agent Toolkit installed or [Model Context Protocol (MCP)](https://docs.stripe.com/mcp) server configured to talk to your Stripe account

[](#provisions)

To provision customers and subscriptions, your agent needs to create a new customer and attach a subscription. Here’s an example using the Stripe Node.js SDK:

`import Stripe from 'stripe'; const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);  // Create a customer and subscription async function createSubscription(customerInfo, priceId) {   // 1. Create or fetch the customer   const customer = await stripe.customers.create({     email: customerInfo.email,     name: customerInfo.name,   });    // 2. Create the subscription   const subscription = await stripe.subscriptions.create({     customer: customer.id,     items: [{ price: priceId }],     expand: ['latest_invoice.payment_intent'],   }); }`

See [Build subscriptions](https://docs.stripe.com/billing/subscriptions/build-subscriptions) for pricing and trial options.

[](#webhooks)

Subscriptions in your application trigger various events such as renewals, failed payments, and cancellations. Some billing events are asynchronous, and you need your agent to respond to them. For example, if a subscription cancels, have your agent follow up with the customer or make an offer to retain them.

To manage these events, use [webhooks](https://docs.stripe.com/webhooks) to listen for and respond to these triggers.

The code example below demonstrates how to set up an Express server that listens for Stripe webhook events, validates incoming requests, and handles specific event types such as successful payments, failed payments, and subscription cancellations. After you capture these events, call into an agent to react accordingly.

``import express from 'express'; import Stripe from 'stripe';  const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, { apiVersion: '2022-11-15' }); const endpointSecret = process.env.STRIPE_WEBHOOK_SECRET;  const app = express(); app.post('/webhooks', express.raw({ type: 'application/json' }), (req, res) => {   let event;    try {     event = stripe.webhooks.constructEvent(req.body, req.headers['stripe-signature'], endpointSecret);   } catch (err) {     return res.status(400).send(`Webhook Error: ${err.message}`);   }    switch (event.type) {     case 'invoice.payment_succeeded':       // Handle successful payment       break;     case 'invoice.payment_failed':       // Call agent to retry or gather information to communicate with the buyer       break;     case 'customer.subscription.deleted':       // Clean up access       break;     default:       // Unexpected event   }    res.status(200).json({ received: true }); });  app.listen(4242, () => console.log('Webhook listener running on port 4242'));``

[](#agent-toolkit)

You can use the [agent toolkit](https://docs.stripe.com/agents) to enable AI agents to automatically initiate billing flows.

You can implement this directly in code or in an application such as Claude or an MCP server.

Here’s an example using Vercel’s [AI SDK](https://ai-sdk.dev/):

`import { StripeAgentToolkit } from '@stripe/agent-toolkit/ai-sdk'; import { openai } from '@ai-sdk/openai'; import { generateText } from 'ai';  const stripeAgentToolkit = new StripeAgentToolkit({   secretKey: process.env.STRIPE_SECRET_KEY!,   configuration: {     actions: {       prices: {         read: true,       },       customers: {         create: true,       },       subscriptions: {         create: true,       },     },   }, });  const result = await generateText({   model: openai('gpt-4o'),   tools: {     ...stripeAgentToolkit.getTools(),   },   maxSteps: 5,   prompt: 'Sign up jenny.rosen@example.com to the Premium plan', });`

Here’s an example using Stripe’s MCP server with OpenAI’s Responses API:

`curl https://api.openai.com/v1/responses -i \  -H "Content-Type: application/json" \  -H "Authorization: Bearer $OPENAI_API_KEY" \  -d '{     "model": "gpt-5",     "tools": [         {             "type": "mcp",             "server_label": "Stripe",             "server_url": "https://mcp.stripe.com",             "require_approval": "never"         }     ],     "input": "Sign up jenny.rosen@example.com to the Premium plan" }'`

To view the full actions, see [Add Stripe to your agentic workflows](https://docs.stripe.com/agents). Learn more about how to [add payments to your LLM agentic workflows](https://stripe.dev/blog/adding-payments-to-your-agentic-workflows).

[](#testing)

You can test your integration using [Sandboxes](https://docs.stripe.com/sandboxes). This allows you to simulate payment processing and other features without affecting your live account or data.
