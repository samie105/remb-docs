---
title: "Type-Safe SQL with Kysely"
source: "https://supabase.com/docs/guides/functions/kysely-postgres"
canonical_url: "https://supabase.com/docs/guides/functions/kysely-postgres"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:50.140Z"
content_hash: "bf20df760c134c8819aeaa3b674c56abd72086d1ba5b058c195afe465392998a"
menu_path: ["Edge Functions","Edge Functions","Third-Party Tools","Third-Party Tools","Type-Safe SQL with Kysely","Type-Safe SQL with Kysely"]
section_path: ["Edge Functions","Edge Functions","Third-Party Tools","Third-Party Tools","Type-Safe SQL with Kysely","Type-Safe SQL with Kysely"]
nav_prev: {"path": "supabase/docs/guides/functions/limits/index.md", "title": "Limits"}
nav_next: {"path": "supabase/docs/guides/functions/logging/index.md", "title": "Logging"}
---

# 

Type-Safe SQL with Kysely

* * *

Supabase Edge Functions can [connect directly to your Postgres database](/docs/guides/functions/connect-to-postgres) to execute SQL queries. [Kysely](https://github.com/kysely-org/kysely#kysely) is a type-safe and autocompletion-friendly typescript SQL query builder.

Combining Kysely with Deno Postgres gives you a convenient developer experience for interacting directly with your Postgres database.

## Code[#](#code)

Find the example on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/kysely-postgres)

Get your database connection credentials from the project's [**Connect** panel](/dashboard/project/_/?showConnect=true) and store them in an `.env` file:

```
1DB_HOSTNAME=2DB_PASSWORD=3DB_SSL_CERT="-----BEGIN CERTIFICATE-----4GET YOUR CERT FROM YOUR PROJECT DASHBOARD5-----END CERTIFICATE-----"
```

Create a `DenoPostgresDriver.ts` file to manage the connection to Postgres via [deno-postgres](https://deno-postgres.com/):

```
1import {2  CompiledQuery,3  DatabaseConnection,4  Driver,5  PostgresCursorConstructor,6  QueryResult,7  TransactionSettings,8} from 'https://esm.sh/kysely@0.23.4'9import { freeze, isFunction } from 'https://esm.sh/kysely@0.23.4/dist/esm/util/object-utils.js'10import { extendStackTrace } from 'https://esm.sh/kysely@0.23.4/dist/esm/util/stack-trace-utils.js'11import { Pool, PoolClient } from 'https://deno.land/x/postgres@v0.17.0/mod.ts'1213export interface PostgresDialectConfig {14  pool: Pool | (() => Promise<Pool>)15  cursor?: PostgresCursorConstructor16  onCreateConnection?: (connection: DatabaseConnection) => Promise<void>17}1819const PRIVATE_RELEASE_METHOD = Symbol()2021export class PostgresDriver implements Driver {22  readonly #config: PostgresDialectConfig23  readonly #connections = new WeakMap<PoolClient, DatabaseConnection>()24  #pool?: Pool2526  constructor(config: PostgresDialectConfig) {27    this.#config = freeze({ ...config })28  }2930  async init(): Promise<void> {31    this.#pool = isFunction(this.#config.pool) ? await this.#config.pool() : this.#config.pool32  }3334  async acquireConnection(): Promise<DatabaseConnection> {35    const client = await this.#pool!.connect()36    let connection = this.#connections.get(client)3738    if (!connection) {39      connection = new PostgresConnection(client, {40        cursor: this.#config.cursor ?? null,41      })42      this.#connections.set(client, connection)4344      // The driver must take care of calling `onCreateConnection` when a new45      // connection is created. The `pg` module doesn't provide an async hook46      // for the connection creation. We need to call the method explicitly.47      if (this.#config?.onCreateConnection) {48        await this.#config.onCreateConnection(connection)49      }50    }5152    return connection53  }5455  async beginTransaction(56    connection: DatabaseConnection,57    settings: TransactionSettings58  ): Promise<void> {59    if (settings.isolationLevel) {60      await connection.executeQuery(61        CompiledQuery.raw(`start transaction isolation level ${settings.isolationLevel}`)62      )63    } else {64      await connection.executeQuery(CompiledQuery.raw('begin'))65    }66  }6768  async commitTransaction(connection: DatabaseConnection): Promise<void> {69    await connection.executeQuery(CompiledQuery.raw('commit'))70  }7172  async rollbackTransaction(connection: DatabaseConnection): Promise<void> {73    await connection.executeQuery(CompiledQuery.raw('rollback'))74  }7576  async releaseConnection(connection: PostgresConnection): Promise<void> {77    connection[PRIVATE_RELEASE_METHOD]()78  }7980  async destroy(): Promise<void> {81    if (this.#pool) {82      const pool = this.#pool83      this.#pool = undefined84      await pool.end()85    }86  }87}8889interface PostgresConnectionOptions {90  cursor: PostgresCursorConstructor | null91}9293class PostgresConnection implements DatabaseConnection {94  #client: PoolClient95  #options: PostgresConnectionOptions9697  constructor(client: PoolClient, options: PostgresConnectionOptions) {98    this.#client = client99    this.#options = options100  }101102  async executeQuery<O>(compiledQuery: CompiledQuery): Promise<QueryResult<O>> {103    try {104      const result = await this.#client.queryObject<O>(compiledQuery.sql, [105        ...compiledQuery.parameters,106      ])107108      if (109        result.command === 'INSERT' ||110        result.command === 'UPDATE' ||111        result.command === 'DELETE'112      ) {113        const numAffectedRows = BigInt(result.rowCount || 0)114115        return {116          numUpdatedOrDeletedRows: numAffectedRows,117          numAffectedRows,118          rows: result.rows ?? [],119        } as any120      }121122      return {123        rows: result.rows ?? [],124      }125    } catch (err) {126      throw extendStackTrace(err, new Error())127    }128  }129130  async *streamQuery<O>(131    _compiledQuery: CompiledQuery,132    chunkSize: number133  ): AsyncIterableIterator<QueryResult<O>> {134    if (!this.#options.cursor) {135      throw new Error(136        "'cursor' is not present in your postgres dialect config. It's required to make streaming work in postgres."137      )138    }139140    if (!Number.isInteger(chunkSize) || chunkSize <= 0) {141      throw new Error('chunkSize must be a positive integer')142    }143144    // stream not available145    return null146  }147148  [PRIVATE_RELEASE_METHOD](): void {149    this.#client.release()150  }151}
```

Create an `index.ts` file to execute a query on incoming requests:

```
1import { serve } from 'https://deno.land/std@0.175.0/http/server.ts'2import { Pool } from 'https://deno.land/x/postgres@v0.17.0/mod.ts'3import {4  Kysely,5  Generated,6  PostgresAdapter,7  PostgresIntrospector,8  PostgresQueryCompiler,9} from 'https://esm.sh/kysely@0.23.4'10import { PostgresDriver } from './DenoPostgresDriver.ts'1112console.log(`Function "kysely-postgres" up and running!`)1314interface AnimalTable {15  id: Generated<bigint>16  animal: string17  created_at: Date18}1920// Keys of this interface are table names.21interface Database {22  animals: AnimalTable23}2425// Create a database pool with one connection.26const pool = new Pool(27  {28    tls: { caCertificates: [Deno.env.get('DB_SSL_CERT')!] },29    database: 'postgres',30    hostname: Deno.env.get('DB_HOSTNAME'),31    user: 'postgres',32    port: 5432,33    password: Deno.env.get('DB_PASSWORD'),34  },35  136)3738// You'd create one of these when you start your app.39const db = new Kysely<Database>({40  dialect: {41    createAdapter() {42      return new PostgresAdapter()43    },44    createDriver() {45      return new PostgresDriver({ pool })46    },47    createIntrospector(db: Kysely<unknown>) {48      return new PostgresIntrospector(db)49    },50    createQueryCompiler() {51      return new PostgresQueryCompiler()52    },53  },54})5556serve(async (_req) => {57  try {58    // Run a query59    const animals = await db.selectFrom('animals').select(['id', 'animal', 'created_at']).execute()6061    // Neat, it's properly typed \o/62    console.log(animals[0].created_at.getFullYear())6364    // Encode the result as pretty printed JSON65    const body = JSON.stringify(66      animals,67      (key, value) => (typeof value === 'bigint' ? value.toString() : value),68      269    )7071    // Return the response with the correct content type header72    return new Response(body, {73      status: 200,74      headers: {75        'Content-Type': 'application/json; charset=utf-8',76      },77    })78  } catch (err) {79    console.error(err)80    return new Response(String(err?.message ?? err), { status: 500 })81  }82})
```

