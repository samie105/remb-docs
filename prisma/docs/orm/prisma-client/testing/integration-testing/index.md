---
title: "Integration testing"
source: "https://www.prisma.io/docs/orm/prisma-client/testing/integration-testing"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/testing/integration-testing"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:58.045Z"
content_hash: "4271e2f25892631c3e24445add22e8b8eac6b83b3885fee12d8b9f5de70cf774"
menu_path: ["Integration testing"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/special-fields-and-types/working-with-geometry-fields/index.md", "title": "Working with geometry fields"}
nav_next: {"path": "prisma/docs/orm/prisma-client/testing/unit-testing/index.md", "title": "Unit testing"}
---

# Set the version of docker compose to use
version: "3.9"

# The containers that compose the project
services:
  db:
    image: postgres:13
    restart: always
    container_name: integration-tests-prisma
    ports:
      - "5433:5432"
    environment:
      POSTGRES_USER: prisma
      POSTGRES_PASSWORD: prisma
      POSTGRES_DB: tests
```

> **Note**: The compose version used here (`3.9`) is the latest at the time of writing, if you are following along be sure to use the same version for consistency.

The `docker-compose.yml` file defines the following:

*   The Postgres image (`postgres`) and version tag (`:13`). This will be downloaded if you do not have it locally available.
*   The port `5433` is mapped to the internal (Postgres default) port `5432`. This will be the port number the database is exposed on externally.
*   The database user credentials are set and the database given a name.

2.  To connect to the database in the container, create a new connection string with the credentials defined in the `docker-compose.yml` file. For example:

```
DATABASE_URL="postgresql://prisma:prisma@localhost:5433/tests"
```

3.  To create the container in a detached state so that you can continue to use the terminal tab, run the following command:

```
docker compose up -d
```

4.  Next you can check that the database has been created by executing a `psql` command inside the container. Make a note of the container id.
    
    ```
    docker ps
    ```
    
    ```
    CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS        PORTS                    NAMES
    1322e42d833f   postgres:13       "docker-entrypoint.s…"   2 seconds ago   Up 1 second   0.0.0.0:5433->5432/tcp   integration-tests-prisma
    ```
    

> **Note**: The container id is unique to each container, you will see a different id displayed.

5.  Using the container id from the previous step, run `psql` in the container, login with the created user and check the database is created:
    
    ```
    docker exec -it 1322e42d833f psql -U prisma tests
    ```
    
    ```
    tests=# \l
                                  List of databases
       Name    | Owner  | Encoding |  Collate   |   Ctype    | Access privileges
    
     postgres  | prisma | UTF8     | en_US.utf8 | en_US.utf8 |
     template0 | prisma | UTF8     | en_US.utf8 | en_US.utf8 | =c/prisma        +
               |        |          |            |            | prisma=CTc/prisma
     template1 | prisma | UTF8     | en_US.utf8 | en_US.utf8 | =c/prisma        +
               |        |          |            |            | prisma=CTc/prisma
     tests     | prisma | UTF8     | en_US.utf8 | en_US.utf8 |
    (4 rows)
    ```
    

Integration tests will be run against a database in a **dedicated test environment** instead of the production or development environments.

### [The flow of operations](#the-flow-of-operations)

The flow for running said tests goes as follows:

1.  Start the container and create the database
2.  Migrate the schema
3.  Run the tests
4.  Destroy the container

Each test suite will seed the database before all the test are run. After all the tests in the suite have finished, the data from all the tables will be dropped and the connection terminated.

### [The function to test](#the-function-to-test)

The ecommerce application you are testing has a function which creates an order. This function does the following:

*   Accepts input about the customer making the order
*   Accepts input about the product being ordered
*   Checks if the customer has an existing account
*   Checks if the product is in stock
*   Returns an "Out of stock" message if the product doesn't exist
*   Creates an account if the customer doesn't exist in the database
*   Create the order

An example of how such a function might look can be seen below:

```
import prisma from "../client";

export interface Customer {
  id?: number;
  name?: string;
  email: string;
  address?: string;
}

export interface OrderInput {
  customer: Customer;
  productId: number;
  quantity: number;
}

/**
 * Creates an order with customer.
 * @param input The order parameters
 */
export async function createOrder(input: OrderInput) {
  const { productId, quantity, customer } = input;
  const { name, email, address } = customer;

  // Get the product
  const product = await prisma.product.findUnique({
    where: {
      id: productId,
    },
  });

  // If the product is null its out of stock, return error.
  if (!product) return new Error("Out of stock");

  // If the customer is new then create the record, otherwise connect via their unique email
  await prisma.customerOrder.create({
    data: {
      customer: {
        connectOrCreate: {
          create: {
            name,
            email,
            address,
          },
          where: {
            email,
          },
        },
      },
      orderDetails: {
        create: {
          total: product.price,
          quantity,
          products: {
            connect: {
              id: product.id,
            },
          },
        },
      },
    },
  });
}
```

### [The test suite](#the-test-suite)

The following tests will check if the `createOrder` function works as it should do. They will test:

*   Creating a new order with a new customer
*   Creating an order with an existing customer
*   Show an "Out of stock" error message if a product doesn't exist

Before the test suite is run the database is seeded with data. After the test suite has finished a [`deleteMany`](prisma/docs/orm/reference/prisma-client-reference/index.md#deletemany) is used to clear the database of its data.

```
import prisma from "../src/client";
import { createOrder, Customer, OrderInput } from "../src/functions/index";

beforeAll(async () => {
  // create product categories
  await prisma.category.createMany({
    data: [{ name: "Wand" }, { name: "Broomstick" }],
  });

  console.log("✨ 2 categories successfully created!");

  // create products
  await prisma.product.createMany({
    data: [
      {
        name: 'Holly, 11", phoenix feather',
        description: "Harry Potters wand",
        price: 100,
        sku: 1,
        categoryId: 1,
      },
      {
        name: "Nimbus 2000",
        description: "Harry Potters broom",
        price: 500,
        sku: 2,
        categoryId: 2,
      },
    ],
  });

  console.log("✨ 2 products successfully created!");

  // create the customer
  await prisma.customer.create({
    data: {
      name: "Harry Potter",
      email: "harry@hogwarts.io",
      address: "4 Privet Drive",
    },
  });

  console.log("✨ 1 customer successfully created!");
});

afterAll(async () => {
  const deleteOrderDetails = prisma.orderDetails.deleteMany();
  const deleteProduct = prisma.product.deleteMany();
  const deleteCategory = prisma.category.deleteMany();
  const deleteCustomerOrder = prisma.customerOrder.deleteMany();
  const deleteCustomer = prisma.customer.deleteMany();

  await prisma.$transaction([
    deleteOrderDetails,
    deleteProduct,
    deleteCategory,
    deleteCustomerOrder,
    deleteCustomer,
  ]);

  await prisma.$disconnect();
});

it("should create 1 new customer with 1 order", async () => {
  // The new customers details
  const customer: Customer = {
    id: 2,
    name: "Hermione Granger",
    email: "hermione@hogwarts.io",
    address: "2 Hampstead Heath",
  };
  // The new orders details
  const order: OrderInput = {
    customer,
    productId: 1,
    quantity: 1,
  };

  // Create the order and customer
  await createOrder(order);

  // Check if the new customer was created by filtering on unique email field
  const newCustomer = await prisma.customer.findUnique({
    where: {
      email: customer.email,
    },
  });

  // Check if the new order was created by filtering on unique email field of the customer
  const newOrder = await prisma.customerOrder.findFirst({
    where: {
      customer: {
        email: customer.email,
      },
    },
  });

  // Expect the new customer to have been created and match the input
  expect(newCustomer).toEqual(customer);
  // Expect the new order to have been created and contain the new customer
  expect(newOrder).toHaveProperty("customerId", 2);
});

it("should create 1 order with an existing customer", async () => {
  // The existing customers email
  const customer: Customer = {
    email: "harry@hogwarts.io",
  };
  // The new orders details
  const order: OrderInput = {
    customer,
    productId: 1,
    quantity: 1,
  };

  // Create the order and connect the existing customer
  await createOrder(order);

  // Check if the new order was created by filtering on unique email field of the customer
  const newOrder = await prisma.customerOrder.findFirst({
    where: {
      customer: {
        email: customer.email,
      },
    },
  });

  // Expect the new order to have been created and contain the existing customer with an id of 1 (Harry Potter from the seed script)
  expect(newOrder).toHaveProperty("customerId", 1);
});

it("should show 'Out of stock' message if productId doesn't exit", async () => {
  // The existing customers email
  const customer: Customer = {
    email: "harry@hogwarts.io",
  };
  // The new orders details
  const order: OrderInput = {
    customer,
    productId: 3,
    quantity: 1,
  };

  // The productId supplied doesn't exit so the function should return an "Out of stock" message
  await expect(createOrder(order)).resolves.toEqual(new Error("Out of stock"));
});
```

This setup isolates a real world scenario so that you can test your applications functionality against real data in a controlled environment.

You can add some scripts to your projects `package.json` file which will setup the database and run the tests, then afterwards manually destroy the container.

```
  "scripts": {
    "docker:up": "docker compose up -d",
    "docker:down": "docker compose down",
    "test": "yarn docker:up && yarn prisma migrate deploy && jest -i"
  },
```

The `test` script does the following:

1.  Runs `docker compose up -d` to create the container with the Postgres image and database.
2.  Applies the migrations found in `./prisma/migrations/` directory to the database, this creates the tables in the container's database.
3.  Executes the tests.

Once you are satisfied you can run `yarn docker:down` to destroy the container, its database and any test data.

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/testing/integration-testing.mdx)

