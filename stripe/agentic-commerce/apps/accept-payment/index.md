---
title: "Accept a payment"
source: "https://docs.stripe.com/agentic-commerce/apps/accept-payment"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:47:34.257Z"
content_hash: "8f8594895847b7c1ae956a2cd8fe3e8803e8992dafb0d206c36275bcac4d6122"
---

## Securely accept payments with your MCP App.

You can collect payments outside your app with a prebuilt Stripe-hosted Checkout page. This guide shows how to:

*   Define Model Context Protocol (MCP) tools to display products and let customers select items to buy
*   Collect payment details with [a prebuilt Stripe-hosted Checkout page](https://docs.stripe.com/payments/checkout)
*   Monitor webhooks after a successful payment

[](#set-up-stripe)

To set up Stripe, add the Stripe API library to your back end.

`# Available as a gem sudo gem install stripe`

`# If you use bundler, you can add this line to your Gemfile gem 'stripe'`

[](#checkout-mcp-tool)

Register an MCP tool that creates a [Checkout Session](https://docs.stripe.com/api/checkout/sessions) for a set of [Prices](https://docs.stripe.com/api/prices). You call this tool from the MCP app in a later step.

`import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js"; import {   registerAppTool,   registerAppResource,   RESOURCE_MIME_TYPE, } from "@modelcontextprotocol/ext-apps/server"; import { readFileSync } from "node:fs"; import Stripe from "stripe"; import { z } from "zod";  // Follow [https://docs.stripe.com/keys-best-practices](https://docs.stripe.com/keys-best-practices) to protect your Stripe API keys. const stripe = new Stripe(process.env.STRIPE_API_KEY); const server = new McpServer({ name: "my-mcp-server", version: "1.0.0" }); const resourceUri = "ui://list-products.html";  async function createCheckoutSession(priceIds) {   const lineItems = priceIds.map((price) => ({ price, quantity: 1 }));    const session = await stripe.checkout.sessions.`

`create`

``({     mode: "payment",     line_items: lineItems,     success_url: "[https://example.com/checkout/success](https://example.com/checkout/success)",   });    return session; }  // Register the tool that creates a checkout session server.registerTool(   "buy-products",   {     title: "Buy products",     description:       "Create a checkout page link for purchasing the selected products",     inputSchema: { priceIds: z.array(z.string()) },   },   async ({ priceIds }) => {     const session = await createCheckoutSession(priceIds);      return {       content: [         {           type: "text",           text: `[Complete your purchase here](${session.url})`,         },       ],       structuredContent: {         checkoutSessionId: session.id,         checkoutSessionUrl: session.url,       },     };   } );``

[](#chatgpt-ui)

Set up the UI for your MCP app by registering an MCP tool and resource. This UI:

1.  Displays a list of products
2.  Lets the customer select products to buy
3.  Redirects to Stripe Checkout to complete payment

### Register a list products MCP tool

Create a list products MCP tool. Its callback returns the price IDs for the products to display in the UI.

`registerAppTool(   server,   "list-products",   {     title: "List products",     description: "List the products available for purchase",     _meta: { ui: { resourceUri } },   },   async () => {     const suggestedProducts = [       // The price IDs from the earlier step       { priceId:` 

`"{{PRICE_ID}}"`

`, name: "Test product 1" },       { priceId:   "{{PRICE_ID}}"  , name: "Test product 2" },     ];      return {       structuredContent: { products: suggestedProducts },       content: [],     };   } );`

### Register a list products UI resource

Create an MCP resource for the product list widget. It defines the UI code that displays the products.

`// Register the resource that serves the bundled HTML registerAppResource(   server,   "list-products-widget",   resourceUri,   { mimeType: RESOURCE_MIME_TYPE },   async () => {     const html = readFileSync("dist/ui/list-products.html", "utf8");      return {       contents: [         {           uri: resourceUri,           mimeType: RESOURCE_MIME_TYPE,           text: html,         },       ],     };   } );`

This example uses minimal markup. In a production app, you can use a framework such as React. See the [MCP Apps documentation](https://modelcontextprotocol.github.io/ext-apps/) for additional examples.

`<div id="root"></div> <script type="module" src="/ui/mcp-app.js"></script>`

``import { App } from "@modelcontextprotocol/ext-apps";  const app = new App({ name: "ProductList", version: "1.0.0" });  // Establish communication with the host await app.connect();  /**   * UI markup and event handlers   */ const renderProduct = (product) => {   return `     <label>       <input type="checkbox" name="cart[]" value="${product.priceId}">       ${product.name}     </label>   `; };  const handleSubmit = async (event) => {   // We'll fill this in next }  const renderApp = (products) => {   const root = document.querySelector("#root");    root.innerHTML = `     <h1>Select products to purchase</h1>     <form id="product-form">       ${products.map(renderProduct).join("")}       <button type="submit">Buy</button>     </form>   `;    document     .querySelector("#product-form")     ?.addEventListener("submit", handleSubmit); };  /**  * Render the list of products from the tool's structuredContent  */ app.ontoolresult = (params) => {   const { products } = params.structuredContent ?? {};   if (products) {     renderApp(products);   } };``

[](#redirect)

When the customer clicks **Buy** in the MCP app:

1.  Call the tool that you created that buys product to create a Checkout Session URL.
2.  Open the Checkout Session URL.

Update the `handleSubmit` function:

`const handleSubmit = async (event) => {   event.preventDefault();   const formData = new FormData(event.target);   const priceIds = Array.from(formData.values());    // Call the buy-products tool to create a Checkout Session   const { structuredContent } = await app.callServerTool({     name: "buy-products",     arguments: { priceIds },   });    if (typeof structuredContent?.checkoutSessionUrl === "string") {     await app.openLink({ url: structuredContent.checkoutSessionUrl });   } };`

[](#fulfillment)

You can handle successful orders by listening to `checkout.session.completed` (and `checkout.session.async_payment_succeeded` for delayed methods) and calling an idempotent fulfillment function that retrieves the Checkout Session (expand `line_items`), verifies payment\_status, and fulfills the items.

Use a `success_url` landing page to trigger fulfillment immediately after redirecting, but rely on webhooks to make sure that every payment is fulfilled.

Then, you can test locally with the Stripe CLI, and deploy your webhook endpoint.

Learn more about how to [fulfill payments received with the Checkout Sessions API](https://docs.stripe.com/checkout/fulfillment?payment-ui=stripe-hosted).

## See also

*   [Collect taxes](https://docs.stripe.com/payments/checkout/taxes)
*   [Collect shipping and other customer info](https://docs.stripe.com/payments/checkout/collect-additional-info)
*   [Customize your branding](https://docs.stripe.com/payments/checkout/customization)
*   [Customize your success page](https://docs.stripe.com/payments/checkout/custom-success-page)
