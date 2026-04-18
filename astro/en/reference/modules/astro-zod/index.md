---
title: "Zod API Reference"
source: "https://docs.astro.build/en/reference/modules/astro-zod/"
canonical_url: "https://docs.astro.build/en/reference/modules/astro-zod/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:51.321Z"
content_hash: "860a8abb3d351c4617718839a8e3a3070d090825e3ce4e28d26ceaadb9a560c2"
menu_path: ["Zod API Reference"]
section_path: []
nav_prev: {"path": "astro/en/reference/modules/astro-transitions/index.md", "title": "View Transitions Router API Reference"}
nav_next: {"path": "astro/en/reference/integrations-reference/index.md", "title": "Astro Integration API"}
---

# Zod API Reference

[Zod](https://github.com/colinhacks/zod) is a TypeScript-based schema declaration and validation library. This allows you to define schemas you can use to validate data and transform data, from a simple type (e.g. `string`, `number`) to complex data structures (e.g. nested objects).

The `astro/zod` module exposes a re-export of Zod that gives you access to all the features of Zod v4. By using this module, you do not need to install Zod yourself. This also ensures that your project uses the same API versions as Astro when using features such as [Content Collections](/en/guides/content-collections/) or [Actions](/en/guides/actions/).

See the [Zod website](https://zod.dev/) for complete documentation on how Zod works and what features are available.

## Imports from `astro/zod`

[Section titled “Imports from astro/zod”](#imports-from-astrozod)

```
import { z } from 'astro/zod';
```

### `z`

[Section titled “z”](#z)

**Type:** `object`

The `z` utility gives you access to validators for a wide range of data types, methods and types for working with your data.

Learn more about the `z` utility in [Zod documentation](https://zod.dev/basics)

#### Common data type validators

[Section titled “Common data type validators”](#common-data-type-validators)

With Zod, you can validate any type of data, such as [primitives](https://zod.dev/api#primitives), [objects](https://zod.dev/api#objects), [arrays](https://zod.dev/api#arrays) and more.

The following example shows a cheatsheet of many common Zod data types to create a `user` schema:

```
import { z } from 'astro/zod';
const user = z.object({  username: z.string(),  name: z.string().min(2),  email: z.email(),  role: z.enum(["admin", "editor"]),  language: z.enum(["en", "fr", "es"]).default("en"),  hobbies: z.array(z.string()),  age: z.number(),  isEmailConfirmed: z.boolean(),  inscriptionDate: z.date(),  website: z.url().optional(),});
```

#### Extracting a Typescript type

[Section titled “Extracting a Typescript type”](#extracting-a-typescript-type)

Zod allows you to create a Typescript type from any schema [using Zod type inference](https://zod.dev/basics#inferring-types). This can be useful for describing an expected data structure when [defining component props](/en/guides/typescript/#component-props).

The following example create a `User` type based on the previous schema:

```
type User = z.infer<typeof user>;
/* The `User` type will be: * type User = { *   username: string; *   name: string; *   email: string; *   role: "admin" | "editor"; *   language: "en" | "fr" | "es"; *   hobbies: string[]; *   age: number; *   isEmailConfirmed: boolean; *   inscriptionDate: Date; *   website?: string | undefined; * } */
```

#### Using Zod methods

[Section titled “Using Zod methods”](#using-zod-methods)

Zod provides various schema methods to [customize error messages](https://zod.dev/error-customization), [transform data](https://zod.dev/api#transforms), or create [custom validation logics](https://zod.dev/api#refinements).

```
// Customize the error messageconst nonEmptyStrings = z.array(z.string()).nonempty("Can't be empty!");
// Validate a data from a schemanonEmptyStrings.parse([]); // will throws our custom error
// Create an object from a URL for a decorative imgconst decorativeImg = z.string().transform((value) => {  return { src: value, alt: "" };});
// Create a custom validator and error message for a stringconst constrainedString = z  .string()  .refine((val) => val.length > 0 && val.length <= 255, {    error: "Must be between 1 and 255 characters.",  });
```

### Individual imports

[Section titled “Individual imports”](#individual-imports)

Alternatively, you can import all the Zod validators, methods and types available in the [`z` utility](#z) directly from the module.

The following example imports `coerce` to create a `Date` object from a date string:

```
import { coerce } from 'astro/zod';
const publishedOn = coerce.date();const publicationDate = publishedOn.parse("2025-12-03");
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


