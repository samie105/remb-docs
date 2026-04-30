---
title: "Script language definition"
source: "https://docs.stripe.com/billing/scripts/script-language"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:13:07.088Z"
content_hash: "a53c9bca4257792902b0a140af158ed7d02a64d34ebad629db04ba95d58ad6d2"
---

Stripe’s scripting language is a subset of [TypeScript](https://www.typescriptlang.org/). While it maintains TypeScript’s features, it has some key differences including a [more restrictive set of allowed operations](#static-script-analysis). The scripting language can help prevent potential issues such as long runtimes and excessive memory consumption.

## Syntax

### Basic types and literals

The language supports these primitive types:

``// Numeric values let num: number = 42; let pi: number = 3.14159;  // Strings let greeting: string = "Hello, world!"; let multiline: string = `This is a multi-line string`;  // Booleans let active: boolean = true; let completed: boolean = false;  // Null let empty: null = null;``

### Variables and declarations

Declare variables using `let` or `const`:

`// Variable declarations let count: number = 0; let name: string = "John";  // Constants (must be initialized) const PI: number = 3.14159; const API_KEY: string = "abcd1234";`

Type annotations are optional but recommended:

`// Type inferred as number let score = 100;  // Explicitly typed let highScore: number = 0;`

### Functions and lambdas

Define functions in multiple ways:

`// Function declaration function add(a: number, b: number): number {   return a + b; }  // Arrow function (lambda) const multiply = (a: number, b: number): number => {   return a * b; };  // Inline arrow function const double = (x: number): number => x * 2;`

### Objects and arrays

Define objects and arrays similar to TypeScript:

`// Object literal let person = {   name: "Alice",   age: 30,   address: {     city: "Wonderland",     zipCode: "12345"   } };  // Array literal let numbers = [1, 2, 3, 4, 5]; let names: string[] = ["Alice", "Bob", "Charlie"];  // Array spread let moreNumbers = [...numbers, 6, 7, 8, 9, 10];  // Accessing properties let cityName = person.address.city; let firstNumber = numbers[0];`

### Control flow

Control flow statements include if-else, while, and for loops:

`// If-else statement if (score > 100) {   console.log("High score!"); } else if (score > 50) {   console.log("Good score!"); } else {   console.log("Try again!"); }  // While loop let i = 0; while (i < 5) {   console.log(i);   i++; }  // For loop for (let j = 0; j < 5; j++) {   console.log(j); }`

Break statements work as expected:

`// Break in a loop let i = 0; while (true) {   if (i >= 5) {     break;   }   i++; }`

### Operators

You can find standard supported operators below:

`// Arithmetic operators let sum = 5 + 3; let difference = 10 - 4; let product = 3 * 7; let quotient = 20 / 4; let remainder = 10 % 3;  // Modulo  // Comparison operators let equal = (5 == 5); let notEqual = (5 != 3); let greater = (10 > 5); let less = (5 < 10); let greaterOrEqual = (5 >= 5); let lessOrEqual = (4 <= 4);  // Logical operators let and = (true && false);  // false let or = (true || false);   // true let not = !true;            // false  // Compound assignment let value = 5; value += 3;  // value is now 8`

### Import and export

Organize your code into modules:

`// Importing modules import { DiscountableItem } from '@stripe/scripts/discounts';  // Export a function export function calculateTotal(items: DiscountableItem[]): number {   let sum = 0;   for (let i = 0; i < items.length; i++) {     sum += items[i].price;   }   return sum; }  // Default export export default function main() {   // Main function logic }`

We don’t support third-party libraries.

## Type system

### Type annotations

Specify types after a colon:

`let count: number = 0; let name: string = "John"; let active: boolean = true; let items: string[] = ["apple", "banana"];`

### Interfaces and object types

Define object types inline or as interfaces:

`// Inline object type let person: { name: string; age: number } = {   name: "Alice",   age: 30 };  // Interface definition interface Product {   id: string;   name: string;   price: number;   inStock?: boolean;  // Optional property }  // Using the interface let laptop: Product = {   id: "lt-001",   name: "Laptop",   price: 999.99,   inStock: true };`

### Union types

Union types allow a variable to have multiple types:

`// Union type let id: string | number;  id = "abc123";  // Valid id = 123;       // Also valid`

### Type declarations

Create type aliases:

`// Type alias type ID = string | number;  // Using the type alias let userId: ID = "user123"; let productId: ID = 456;  // Complex type declaration type ApiResponse = {   status: number;   data: {     items: any[];     count: number;   };   error?: string; };`

## Static analysis

Our script language includes static analysis to make sure scripts are reliable and efficient.

### Termination analysis

A key feature is termination checking, which guarantees that scripts always terminate when you run them on Stripe’s infrastructure, preventing infinite loops or recursion. Because not all terminating code can be proven to terminate, we reject some valid programs. Below are tips for writing terminating scripts.

The analyzer uses a coloring system:

*   **T (Terminating)**: Code that is proven to terminate.
*   **U (Unknown)**: Code that might not terminate.

`// Guaranteed to terminate - marked as T function countdown(n: number): void {   while (n > 0) {     n = n - 1;  // Decreasing counter   } }  // Not guaranteed to terminate - marked as U function infinite(): void {   while (true) {     console.log("This runs forever");   } }`

#### Well-founded recursion

The analyzer checks that recursive functions have a decreasing measure:

`// Safe recursion - marked as T function factorial(n: number): number {   if (n <= 1) return 1;   return n * factorial(n - 1);  // n decreases with each call }  // Unsafe recursion - marked as U function badRecursion(n: number): number {   return badRecursion(n + 1);  // n increases, no termination }`

### Common static analysis patterns

For loops with finite bounds are safe:

`// Safe loop pattern - marked as T for (let i = 0; i < array.length; i++) {   // Loop body with terminating operations }`

While loops need a decreasing counter:

`// Safe while loop - marked as T let counter = 10; while (counter > 0) {   // Do something   counter--;  // Counter decreases }`

### Writing termination-safe code

To make sure your code passes the termination checker, follow these guidelines:

*   Use for loops with clear, finite bounds
*   Make sure while loops have a decreasing counter or condition that eventually becomes `false`
*   Include a base case and decreasing argument in recursive functions
*   Avoid complex loop conditions, mutual recursion, or deep nesting of functions and loops

`// Good pattern for loops function processItems(items: any[]): void {   for (let i = 0; i < items.length; i++) {     processItem(items[i]);   } }`

## Runtime environment

The scripting language provides built-in objects that you can use in your scripts.

### Built-in objects

Several built-in objects are available:

#### Math object

`// Math operations let min = Math.min(5, 3, 7);  // 3 let max = Math.max(5, 3, 7);  // 7 let floor = Math.floor(3.7);  // 3 let ceil = Math.ceil(3.2);    // 4`

#### Arrays

`// Array creation let numbers = [1, 2, 3, 4, 5];  // Array properties let length = numbers.length;  // 5  // Array indexing let firstItem = numbers[0];  // 1 let lastItem = numbers[numbers.length - 1];  // 5  // Array methods let sorted = numbers.sort((a, b) => a - b);`

### String operations

``// String concatenation let firstName = "John"; let lastName = "Doe"; let fullName = firstName + " " + lastName;  // "John Doe"  // String with template literals let greeting = `Hello, ${firstName}!`;  // "Hello, John!"``

## Schema validation

You can annotate your types to provide basic validation for fields. Use this when you define the configuration schema for your scripts.

### String validations

`/** @minLength 0 @maxLength 10 */ type Greeting = string;`

`/** @pattern ^hello world$ */ type Greeting = string;`

### Number validations

inclusive\_range\_validation.ts

`/** @minimum 0 @maximum 100 */ type Percent = number;`

exclusive\_range\_validation.ts

`/** @exclusiveMinimum -1 @exclusiveMaximum 101 */ type Percent = number;`

### Array validations

length\_inclusive\_validation.ts

`/** @minItems 1 @maxItems 5 */ type Names = string[];`

`/** @uniqueItems */ type Names = string[];`

If we don’t support your validation use case, we recommend building the validation check into your function definition and contacting [scripts-preview@stripe.com](mailto:scripts-preview@stripe.com).

## Examples

### Percentage-off discount function

This example shows a discount function that gives a percentage off up to a maximum amount:

max\_amount\_percent\_off.ts

`/**  * Max Amount Percent Off Discount  *  * This discount function applies a percentage discount to the gross amount,  * but caps the total discount at a maximum amount. It calculates the discount  * as a percentage of the gross amount and then ensures it doesn't exceed the  * configured maximum.  *  * Configuration:  * - max_amount: The maximum monetary amount that can be discounted  * - percent: The percentage discount to apply  */ import { MonetaryAmount, Percent, RunContext } from '@stripe/scripts'; import {   ComputeDiscountsFunction,   DiscountCalculation,   DiscountableItem,   DiscountResult, } from '@stripe/scripts/discounts';  type Configuration = {   max_amount: MonetaryAmount;   percent: Percent; };  const maxAmountPercentOff: ComputeDiscountsFunction<Configuration> = (   context: RunContext,   configuration: Configuration,   item: DiscountableItem, ): DiscountResult => {   const { max_amount, percent } = configuration;   const discount_amount = Math.min(max_amount.amount, item.gross_amount.amount * (percent / 100));    return {     discount: {       amount: {         amount: discount_amount,         currency: item.gross_amount.currency,       },     },   }; };  const computeMaxAmountPercentOff: DiscountCalculation<Configuration> = {   computeDiscounts: maxAmountPercentOff, };  export default computeMaxAmountPercentOff;`

### Tiered discount based on quantity

This example shows a discount that applies different rates based on quantity:

`/**  * Tiered Discount  *  * This discount function applies percentage discounts based on quantity tiers.  * It sums the quantities across all line items and applies the discount percentage  * from the highest applicable tier. The discount is calculated on each line item's  * subtotal amount.  *  * Configuration:  * - tiers: Array of objects with minimum_quantity and discount_percent  *   The tiers are sorted by minimum_quantity in descending order to find  *   the highest applicable tier.  */ import type {   ComputeDiscountsFunction,   DiscountableItem,   DiscountResult,   DiscountCalculation, } from '@stripe/scripts/discounts'; import type {RunContext} from '@stripe/scripts';  /**  * Configuration for the discount calculator function  */ export type TieredPercentOffDiscountConfiguration = {   currency: string;   tier_1_minimum_spend_amount: number;   tier_1_discount_percent: number;   tier_2_minimum_spend_amount: number;   tier_2_discount_percent: number; };  /**  * Gives a percentage off based on minimum spend amount.  * It is assumed tier1 amount < tier2 amount  *  * @param {TieredPercentOffDiscountConfiguration} configuration - The config containing tier specifications  * @param {DiscountableItem} item - The items to apply discounts to  * @returns {DiscountResult} - The discounts applied to the items  */ const tieredPercentOffDiscountCalculator: ComputeDiscountsFunction<   TieredPercentOffDiscountConfiguration > = (   context: RunContext,   configuration: TieredPercentOffDiscountConfiguration,   discountable_item: DiscountableItem, ): DiscountResult => {   const {     currency,     tier_1_minimum_spend_amount,     tier_1_discount_percent,     tier_2_minimum_spend_amount,     tier_2_discount_percent,   } = configuration;   let discountAmount = 0;   let discountPercent = 0;   const invoiceTotal = discountable_item.gross_amount.amount;   if (     discountable_item.gross_amount.currency.toLowerCase().trim() ===     currency.toLowerCase().trim()   ) {     // Get discount percent based on gross amount     switch (true) {       case invoiceTotal >= tier_2_minimum_spend_amount:         discountPercent = tier_2_discount_percent;         break;       case invoiceTotal >= tier_1_minimum_spend_amount:         discountPercent = tier_1_discount_percent;         break;       default:         break;     }     discountAmount = (invoiceTotal * discountPercent) / 100;   }   return {     discount: {       amount: {         amount: discountAmount,         currency: discountable_item.gross_amount.currency,       },     },   }; };  const computeTieredPercentOffDiscountCalculator: DiscountCalculation<TieredPercentOffDiscountConfiguration> =   {     computeDiscounts: tieredPercentOffDiscountCalculator,   };  export default computeTieredPercentOffDiscountCalculator;`

## Debugging tips

### Common error patterns

If your script fails static analysis, check for these common issues:

1.  **Infinite loops**: Loops without a clear termination condition
    
    `// Problem: No clear exit condition while (x > 0) {   doSomething(); // x never changes }  // Fix: Add a decreasing counter while (x > 0) {   doSomething();   x--; }`
    
2.  **Non-terminating recursion**: Recursive calls without a decreasing measure
    
    `// Problem: No decreasing measure function process(data: any): void {   process(transformData(data)); }  // Fix: Add a depth limit and decreasing measure function process(data: any, depth: number = 10): void {   if (depth <= 0) return;   process(transformData(data), depth - 1); }`
