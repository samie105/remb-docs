---
title: "Testing your Edge Functions"
source: "https://supabase.com/docs/guides/functions/unit-test"
canonical_url: "https://supabase.com/docs/guides/functions/unit-test"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:41.126Z"
content_hash: "093898e491191c82d41f7a24f8857916bde04ee4e67693cc5b6fd42c2bbf7d84"
menu_path: ["Edge Functions","Edge Functions","Debugging","Debugging","Testing your Functions","Testing your Functions"]
section_path: ["Edge Functions","Edge Functions","Debugging","Debugging","Testing your Functions","Testing your Functions"]
nav_prev: {"path": "supabase/docs/guides/functions/storage-caching/index.md", "title": "Integrating with Supabase Storage"}
nav_next: {"path": "supabase/docs/guides/functions/wasm/index.md", "title": "Using Wasm modules"}
---

# 

Testing your Edge Functions

## 

Writing Unit Tests for Edge Functions using Deno Test

* * *

Testing is an essential step in the development process to ensure the correctness and performance of your Edge Functions.

* * *

## Testing in Deno[#](#testing-in-deno)

Deno has a built-in test runner that you can use for testing JavaScript or TypeScript code. You can read the [official documentation](https://docs.deno.com/runtime/manual/basics/testing/) for more information and details about the available testing functions.

* * *

## Folder structure[#](#folder-structure)

We recommend creating your testing in a `supabase/functions/tests` directory, using the same name as the Function followed by `-test.ts`:

```
1└── supabase2    ├── functions3    │   ├── function-one4    │   │   └── index.ts5    │   └── function-two6    │   │   └── index.ts7    │   └── tests8    │       └── function-one-test.ts  # Tests for function-one9    │       └── function-two-test.ts  # Tests for function-two10    └── config.toml
```

* * *

## Example[#](#example)

The following script is a good example to get started with testing your Edge Functions:

```
1// Import required libraries and modules2import { assert, assertEquals } from 'jsr:@std/assert@1'3import { createClient, SupabaseClient } from 'npm:@supabase/supabase-js@2'45// Will load the .env file to Deno.env6import 'jsr:@std/dotenv/load'78// Set up the configuration for the Supabase client9const supabaseUrl = Deno.env.get('SUPABASE_URL') ?? ''10const supabaseKey = Deno.env.get('SUPABASE_PUBLISHABLE_KEY') ?? ''11const options = {12  auth: {13    autoRefreshToken: false,14    persistSession: false,15    detectSessionInUrl: false,16  },17}1819// Test the creation and functionality of the Supabase client20const testClientCreation = async () => {21  var client: SupabaseClient = createClient(supabaseUrl, supabaseKey, options)2223  // Verify if the Supabase URL and key are provided24  if (!supabaseUrl) throw new Error('supabaseUrl is required.')25  if (!supabaseKey) throw new Error('supabaseKey is required.')2627  // Test a simple query to the database28  const { data: table_data, error: table_error } = await client29    .from('my_table')30    .select('*')31    .limit(1)32  if (table_error) {33    throw new Error('Invalid Supabase client: ' + table_error.message)34  }35  assert(table_data, 'Data should be returned from the query.')36}3738// Test the 'hello-world' function39const testHelloWorld = async () => {40  var client: SupabaseClient = createClient(supabaseUrl, supabaseKey, options)4142  // Invoke the 'hello-world' function with a parameter43  const { data: func_data, error: func_error } = await client.functions.invoke('hello-world', {44    body: { name: 'bar' },45  })4647  // Check for errors from the function invocation48  if (func_error) {49    throw new Error('Invalid response: ' + func_error.message)50  }5152  // Log the response from the function53  console.log(JSON.stringify(func_data, null, 2))5455  // Assert that the function returned the expected result56  assertEquals(func_data.message, 'Hello bar!')57}5859// Register and run the tests60Deno.test('Client Creation Test', testClientCreation)61Deno.test('Hello-world Function Test', testHelloWorld)
```

This test case consists of two parts.

1.  The first part tests the client library and verifies that the database can be connected to and returns values from a table (`my_table`).
2.  The second part tests the edge function and checks if the received value matches the expected value. Here's a brief overview of the code:
    *   We import various testing functions from the Deno standard library, including `assert`, `assertExists`, and `assertEquals`.
    *   We import the `createClient` and `SupabaseClient` classes from the `@supabase/supabase-js` library to interact with the Supabase client.
    *   We define the necessary configuration for the Supabase client, including the Supabase URL, API key, and authentication options.
    *   The `testClientCreation` function tests the creation of a Supabase client instance and queries the database for data from a table. It verifies that data is returned from the query.
    *   The `testHelloWorld` function tests the "Hello-world" Edge Function by invoking it using the Supabase client's `functions.invoke` method. It checks if the response message matches the expected greeting.
    *   We run the tests using the `Deno.test` function, providing a descriptive name for each test case and the corresponding test function.

Make sure to replace the placeholders (`supabaseUrl`, `supabaseKey`, `my_table`) with the actual values relevant to your Supabase setup.

* * *

## Running Edge Functions locally[#](#running-edge-functions-locally)

To locally test and debug Edge Functions, you can utilize the Supabase CLI. Let's explore how to run Edge Functions locally using the Supabase CLI:

1.  Ensure that the Supabase server is running by executing the following command:
    
    ```
    1supabase start
    ```
    
2.  In your terminal, use the following command to serve the Edge Functions locally:
    
    ```
    1supabase functions serve
    ```
    
    This command starts a local server that runs your Edge Functions, enabling you to test and debug them in a development environment.
    
3.  Create the environment variables file:
    
    ```
    1# creates the file2touch .env3# adds the SUPABASE_URL secret4echo "SUPABASE_URL=http://localhost:54321" >> .env5# adds the SUPABASE_PUBLISHABLE_KEY secret6echo "SUPABASE_PUBLISHABLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0" >> .env7# Alternatively, you can open it in your editor:8open .env
    ```
    
4.  To run the tests, use the following command in your terminal:
    
    ```
    1deno test --allow-all supabase/functions/tests/function-one-test.ts
    ```
    

* * *

## Resources[#](#resources)

*   Full guide on Testing Supabase Edge Functions on [Mansueli's tips](https://blog.mansueli.com/testing-supabase-edge-functions-with-deno-test)

