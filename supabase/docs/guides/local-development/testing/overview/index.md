---
title: "Testing Overview"
source: "https://supabase.com/docs/guides/local-development/testing/overview"
canonical_url: "https://supabase.com/docs/guides/local-development/testing/overview"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:34.059Z"
content_hash: "d6070d373bf3053a6a13d8e0e479be5496e0d3242c8a13afa2e9654d1f58545c"
menu_path: ["Local Dev / CLI","Local Dev / CLI","Testing","Testing","Getting started","Getting started"]
section_path: ["Local Dev / CLI","Local Dev / CLI","Testing","Testing","Getting started","Getting started"]
nav_prev: {"path": "supabase/docs/guides/local-development/cli/testing-and-linting/index.md", "title": "Testing and linting"}
nav_next: {"path": "supabase/docs/guides/local-development/testing/pgtap-extended/index.md", "title": "Advanced pgTAP Testing"}
---

# 

Testing Overview

* * *

Testing is a critical part of database development, especially when working with features like Row Level Security (RLS) policies. This guide provides a comprehensive approach to testing your Supabase database.

## Testing approaches[#](#testing-approaches)

### Database unit testing with pgTAP[#](#database-unit-testing-with-pgtap)

[pgTAP](https://pgtap.org) is a unit testing framework for Postgres that allows testing:

*   Database structure: tables, columns, constraints
*   Row Level Security (RLS) policies
*   Functions and procedures
*   Data integrity

This example demonstrates setting up and testing RLS policies for a simple todo application:

1.  Create a test table with RLS enabled:
    
    ```
    1-- Create a simple todos table2create table todos (3id uuid primary key default gen_random_uuid(),4task text not null,5user_id uuid references auth.users not null,6completed boolean default false7);89-- Enable RLS10alter table todos enable row level security;1112-- Create a policy13create policy "Users can only access their own todos"14on todos for all -- this policy applies to all operations15to authenticated16using ((select auth.uid()) = user_id);
    ```
    
2.  Set up your testing environment:
    
    ```
    1# Create a new test for our policies using supabase cli2supabase test new todos_rls.test
    ```
    
3.  Write your RLS tests:
    
    ```
    1begin;2-- install tests utilities3-- install pgtap extension for testing4create extension if not exists pgtap with schema extensions;5-- Start declare we'll have 4 test cases in our test suite6select plan(4);78-- Setup our testing data9-- Set up auth.users entries10insert into auth.users (id, email) values11	('123e4567-e89b-12d3-a456-426614174000', 'user1@test.com'),12	('987fcdeb-51a2-43d7-9012-345678901234', 'user2@test.com');1314-- Create test todos15insert into public.todos (task, user_id) values16	('User 1 Task 1', '123e4567-e89b-12d3-a456-426614174000'),17	('User 1 Task 2', '123e4567-e89b-12d3-a456-426614174000'),18	('User 2 Task 1', '987fcdeb-51a2-43d7-9012-345678901234');1920-- as User 121set local role authenticated;22set local request.jwt.claim.sub = '123e4567-e89b-12d3-a456-426614174000';2324-- Test 1: User 1 should only see their own todos25select results_eq(26	'select count(*) from todos',27	ARRAY[2::bigint],28	'User 1 should only see their 2 todos'29);3031-- Test 2: User 1 can create their own todo32select lives_ok(33	$$insert into todos (task, user_id) values ('New Task', '123e4567-e89b-12d3-a456-426614174000'::uuid)$$,34	'User 1 can create their own todo'35);3637-- as User 238set local request.jwt.claim.sub = '987fcdeb-51a2-43d7-9012-345678901234';3940-- Test 3: User 2 should only see their own todos41select results_eq(42	'select count(*) from todos',43	ARRAY[1::bigint],44	'User 2 should only see their 1 todo'45);4647-- Test 4: User 2 cannot modify User 1's todo48SELECT results_ne(49	$$ update todos set task = 'Hacked!' where user_id = '123e4567-e89b-12d3-a456-426614174000'::uuid returning 1 $$,50	$$ values(1) $$,51	'User 2 cannot modify User 1 todos'52);5354select * from finish();55rollback;
    ```
    
4.  Run the tests:
    
    ```
    1supabase test db2psql:todos_rls.test.sql:4: NOTICE:  extension "pgtap" already exists, skipping3./todos_rls.test.sql .. ok4All tests successful.5Files=1, Tests=6,  0 wallclock secs ( 0.01 usr +  0.00 sys =  0.01 CPU)6Result: PASS
    ```
    

### Application-Level testing[#](#application-level-testing)

Testing through application code provides end-to-end verification. Unlike database-level testing with pgTAP, application-level tests cannot use transactions for isolation.

Application-level tests should not rely on a clean database state, as resetting the database before each test can be slow and makes tests difficult to parallelize. Instead, design your tests to be independent by using unique user IDs for each test case.

Here's an example using TypeScript that mirrors the pgTAP tests above:

```
1import { createClient } from '@supabase/supabase-js'2import { beforeAll, describe, expect, it } from 'vitest'3import crypto from 'crypto'45describe('Todos RLS', () => {6  // Generate unique IDs for this test suite to avoid conflicts with other tests7  const USER_1_ID = crypto.randomUUID()8  const USER_2_ID = crypto.randomUUID()910  const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_PUBLISHABLE_KEY!)1112  beforeAll(async () => {13    // Setup test data specific to this test suite14    const adminSupabase = createClient(process.env.SUPABASE_URL!, process.env.SERVICE_ROLE_KEY!)1516    // Create test users with unique IDs17    await adminSupabase.auth.admin.createUser({18      id: USER_1_ID,19      email: `user1-${USER_1_ID}@test.com`,20      password: 'password123',21      // We want the user to be usable right away without email confirmation22      email_confirm: true,23    })24    await adminSupabase.auth.admin.createUser({25      id: USER_2_ID,26      email: `user2-${USER_2_ID}@test.com`,27      password: 'password123',28      email_confirm: true,29    })3031    // Create initial todos32    await adminSupabase.from('todos').insert([33      { task: 'User 1 Task 1', user_id: USER_1_ID },34      { task: 'User 1 Task 2', user_id: USER_1_ID },35      { task: 'User 2 Task 1', user_id: USER_2_ID },36    ])37  })3839  it('should allow User 1 to only see their own todos', async () => {40    // Sign in as User 141    await supabase.auth.signInWithPassword({42      email: `user1-${USER_1_ID}@test.com`,43      password: 'password123',44    })4546    const { data: todos } = await supabase.from('todos').select('*')4748    expect(todos).toHaveLength(2)49    todos?.forEach((todo) => {50      expect(todo.user_id).toBe(USER_1_ID)51    })52  })5354  it('should allow User 1 to create their own todo', async () => {55    await supabase.auth.signInWithPassword({56      email: `user1-${USER_1_ID}@test.com`,57      password: 'password123',58    })5960    const { error } = await supabase.from('todos').insert({ task: 'New Task', user_id: USER_1_ID })6162    expect(error).toBeNull()63  })6465  it('should allow User 2 to only see their own todos', async () => {66    // Sign in as User 267    await supabase.auth.signInWithPassword({68      email: `user2-${USER_2_ID}@test.com`,69      password: 'password123',70    })7172    const { data: todos } = await supabase.from('todos').select('*')73    expect(todos).toHaveLength(1)74    todos?.forEach((todo) => {75      expect(todo.user_id).toBe(USER_2_ID)76    })77  })7879  it('should prevent User 2 from modifying User 1 todos', async () => {80    await supabase.auth.signInWithPassword({81      email: `user2-${USER_2_ID}@test.com`,82      password: 'password123',83    })8485    // Attempt to update the todos we shouldn't have access to86    // result will be a no-op87    await supabase.from('todos').update({ task: 'Hacked!' }).eq('user_id', USER_1_ID)8889    // Log back in as User 1 to verify their todos weren't changed90    await supabase.auth.signInWithPassword({91      email: `user1-${USER_1_ID}@test.com`,92      password: 'password123',93    })9495    // Fetch User 1's todos96    const { data: todos } = await supabase.from('todos').select('*')9798    // Verify that none of the todos were changed to "Hacked!"99    expect(todos).toBeDefined()100    todos?.forEach((todo) => {101      expect(todo.task).not.toBe('Hacked!')102    })103  })104})
```

#### Test isolation strategies[#](#test-isolation-strategies)

For application-level testing, consider these approaches for test isolation:

1.  **Unique Identifiers**: Generate unique IDs for each test suite to prevent data conflicts
2.  **Cleanup After Tests**: If necessary, clean up created data in an `afterAll` or `afterEach` hook
3.  **Isolated Data Sets**: Use prefixes or namespaces in data to separate test cases

### Continuous integration testing[#](#continuous-integration-testing)

Set up automated database testing in your CI pipeline:

1.  Create a GitHub Actions workflow `.github/workflows/db-tests.yml`:

```
1name: Database Tests23on:4  push:5    branches: [main]6  pull_request:7    branches: [main]89jobs:10  test:11    runs-on: ubuntu-latest1213    steps:14      - uses: actions/checkout@v41516      - name: Setup Supabase CLI17        uses: supabase/setup-cli@v11819      - name: Start Supabase20        run: supabase start2122      - name: Run Tests23        run: supabase test db
```

## Best practices[#](#best-practices)

1.  **Test Data Setup**
    
    *   Use begin and rollback to ensure test isolation
    *   Create realistic test data that covers edge cases
    *   Use different user roles and permissions in tests
2.  **RLS Policy Testing**
    
    *   Test Create, Read, Update, Delete operations
    *   Test with different user roles: anonymous and authenticated
    *   Test edge cases and potential security bypasses
    *   Always test negative cases: what users should not be able to do
3.  **CI/CD Integration**
    
    *   Run tests automatically on every pull request
    *   Include database tests in deployment pipeline
    *   Keep test runs fast using transactions

## Real-World examples[#](#real-world-examples)

For more complex, real-world examples of database testing, check out:

*   [Database Tests Example Repository](https://github.com/usebasejump/basejump/tree/main/supabase/tests/database) - A production-grade example of testing RLS policies
*   [RLS Guide and Best Practices](https://github.com/orgs/supabase/discussions/14576)

## Troubleshooting[#](#troubleshooting)

Common issues and solutions:

1.  **Test Failures Due to RLS**
    
    *   Ensure you've set the correct role `set local role authenticated;`
    *   Verify JWT claims are set `set local "request.jwt.claims"`
    *   Check policy definitions match your test assumptions
2.  **CI Pipeline Issues**
    
    *   Verify Supabase CLI is properly installed
    *   Ensure database migrations are run before tests
    *   Check for proper test isolation using transactions

## Additional resources[#](#additional-resources)

*   [pgTAP Documentation](https://pgtap.org)
*   [Supabase CLI Reference](/docs/reference/cli/supabase-test)
*   [pgTAP Supabase reference](/docs/guides/database/extensions/pgtap?queryGroups=database-method&database-method=sql#testing-rls-policies)
*   [Database testing reference](/docs/guides/database/testing)


