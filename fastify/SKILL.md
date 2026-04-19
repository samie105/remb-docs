# Fastify Skill File

## Overview

Fastify is a high-performance web framework for Node.js focused on developer productivity, extensibility, and low overhead. It offers a robust plugin architecture, automatic JSON schema validation/serialization, and support for modern HTTP features, making it ideal for building scalable APIs and web applications.

## Key Concepts

- **Plugin Architecture**: Fastify operates with a modular plugin system, encouraging encapsulation and reusability.
- **Schema-based Validation & Serialization**: All routes leverage JSON schemas for validating incoming requests and serializing responses, improving reliability and speed.
- **Encapsulation**: Plugins and registered routes are isolated from each other unless explicitly shared, preventing accidental pollution of the global scope.
- **Lifecycle Hooks**: Customizable hooks let you tie into request/response processing for logging, authentication, etc.
- **TypeScript Support**: Type-safe development with supported type-providers and definitions.
- **Ecosystem & Extensibility**: Rich ecosystem of official and community plugins (database, authentication, serverless, etc.).
- **Serverless & HTTP2**: Supports serverless deployment paradigms, as well as HTTP2 protocols.

## Navigation Guide

- **Getting Started / Intro**: Begin at [Introduction](fastify/docs/latest/index.md) and [Getting-Started](fastify/docs/latest/Guides/Getting-Started/index.md) for initial concepts, installation, and first app.
- **Common Tasks / How-Tos**: Use [Guides](fastify/docs/latest/Guides/index.md) for practical workflows (plugins, database, testing, migrations).
- **API Reference / Deep Dives**: Consult [Reference](fastify/docs/latest/Reference/index.md) for in-depth details on Fastify internals, API surfaces, hooks, lifecycle, and advanced options.
- **Plugin/Ecosystem**: [Ecosystem](fastify/docs/latest/Guides/Ecosystem/index.md) lists official/core and community plugins.
- **Migrations**: See migration guides for breaking changes between versions.
- **TypeScript**: [TypeScript](fastify/docs/latest/Reference/TypeScript/index.md) and [Write-Type-Provider](fastify/docs/latest/Guides/Write-Type-Provider/index.md) cover TS integrations.

## Top 15 Important Pages

1. [Introduction](fastify/docs/latest/index.md)  
   Overview of Fastify, key features, and philosophy.
2. [Getting-Started](fastify/docs/latest/Guides/Getting-Started/index.md)  
   Step-by-step instructions for setting up your first Fastify app.
3. [Guides](fastify/docs/latest/Guides/index.md)  
   Collection of practical guides for major use-cases.
4. [Plugins-Guide](fastify/docs/latest/Guides/Plugins-Guide/index.md)  
   How to create, use, and understand Fastify plugins.
5. [Ecosystem](fastify/docs/latest/Guides/Ecosystem/index.md)  
   List and description of core and community plugins.
6. [Validation-and-Serialization](fastify/docs/latest/Reference/Validation-and-Serialization/index.md)  
   How schema-based request validation and response serialization work.
7. [ContentTypeParser](fastify/docs/latest/Reference/ContentTypeParser/index.md)  
   Customizing how Fastify parses incoming content types.
8. [Encapsulation](fastify/docs/latest/Reference/Encapsulation/index.md)  
   Explains plugin isolation, scope, and encapsulation rules.
9. [Hooks](fastify/docs/latest/Reference/Hooks/index.md)  
   Comprehensive list of lifecycle hooks for customizing behavior.
10. [Logging](fastify/docs/latest/Reference/Logging/index.md)  
    How to enable, configure, and use Fastify's logging system.
11. [Database](fastify/docs/latest/Guides/Database/index.md)  
    Guidance for connecting to popular databases, plugin recommendations.
12. [Serverless](fastify/docs/latest/Guides/Serverless/index.md)  
    Running Fastify on serverless infrastructure like AWS Lambda.
13. [TypeScript](fastify/docs/latest/Reference/TypeScript/index.md)  
    Guidance on using Fastify with TypeScript, typings, and type-providers.
14. [Testing](fastify/docs/latest/Guides/Testing/index.md)  
    Strategies and recommended tools for testing Fastify applications.
15. [Migration-Guide-V5](fastify/docs/latest/Guides/Migration-Guide-V5/index.md)  
    Reference for migrating to the latest major version (v5).

## Gotchas & Doc Structure Quirks

- **Plugin Docs**: Plugin concepts live both in [Plugins-Guide](fastify/docs/latest/Guides/Plugins-Guide/index.md) and scattered throughout [Reference], especially in [Encapsulation](fastify/docs/latest/Reference/Encapsulation/index.md) and [Decorators](fastify/docs/latest/Reference/Decorators/index.md).
- **Schema Usage**: Schema guidance integrates with several pages (mainly [Validation-and-Serialization](fastify/docs/latest/Reference/Validation-and-Serialization/index.md) and [Fluent-Schema](fastify/docs/latest/Guides/Fluent-Schema/index.md)).
- **Breaking Changes**: Migration guides ([Migration-Guide-V3](fastify/docs/latest/Guides/Migration-Guide-V3/index.md), [Migration-Guide-V4](fastify/docs/latest/Guides/Migration-Guide-V4/index.md), [Migration-Guide-V5](fastify/docs/latest/Guides/Migration-Guide-V5/index.md)) are critical for major upgrades.
- **Non-obvious API details**: Lifecycle and hooks ([Lifecycle](fastify/docs/latest/Reference/Lifecycle/index.md), [Hooks](fastify/docs/latest/Reference/Hooks/index.md)) are split between Reference pages.
- **Long Term Support (LTS)**: See [LTS](fastify/docs/latest/Reference/LTS/index.md) for supported release timelines.