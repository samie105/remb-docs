---
title: "deno deploy"
source: "https://docs.deno.com/runtime/reference/cli/deploy/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/deploy/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:36.759Z"
content_hash: "a694a833ffee8e2e0b00a7e1f4fb5efc94bd54e4764306e5f3815122e80ec9e6"
menu_path: ["deno deploy"]
section_path: []
nav_prev: {"path": "deno/runtime/reference/cli/coverage/index.md", "title": "deno coverage"}
nav_next: {"path": "deno/deno/runtime/reference/cli/doc/index.md", "title": "deno doc"}
---

# Add a secret environment variable
deno deploy env add API_KEY "sk-secret-value" --secret
```

#### Update environment variable value

\>\_

```sh
deno deploy env update-value <variable> <value>
```

Updates the value of an existing environment variable.

\>\_

```sh
deno deploy env update-value API_KEY "new-api-key-value"
```

#### Specifying environment variable contexts

Environment variables can be made available to specific contexts such as Production, Preview, Local, and Build.

\>\_

```sh
deno deploy env update-contexts <variable> [contexts...]
```

Updates the contexts of an environment variable in the application:

#### Delete environment variable

\>\_

```sh
deno deploy env delete <variable>
```

Deletes an environment variable from the application.

\>\_

```sh
deno deploy env delete OLD_API_KEY
```

#### Load environment variables from file

\>\_

```sh
deno deploy env load <file>
```

Loads environment variables from a `.env` file into the application. The CLI automatically detects which variables are likely secrets based on their names (e.g. keys containing `SECRET`, `TOKEN`, `PASSWORD`, etc.) and marks them accordingly.

**Options:**

*   `--non-secrets <keys...>` - Keys from the `.env` file that should be treated as non-secrets, overriding the auto-detection

\>\_

```sh
deno deploy env load .env.production

# Load and treat specific keys as non-secrets
deno deploy env load .env.production --non-secrets PUBLIC_URL SITE_NAME
```

### Database management

Manage database instances for your organization.

\>\_

```sh
deno deploy database
```

**Options:**

*   `-h, --help` - Show help information
*   `--org <name>` - The name of the organization

#### Provision a database

\>\_

```sh
deno deploy database provision <name> --kind <denokv|prisma> [--region <region>]
```

Creates a new database instance.

**Options:**

*   `--kind <denokv|prisma>` - The type of database to provision (required)
*   `--region <region>` - The primary region for the database (required for Prisma)

\>\_

```sh
# Provision a Deno KV database
deno deploy database provision my-kv-db --kind denokv

# Provision a Prisma Postgres database
deno deploy database provision my-pg-db --kind prisma --region us-east-1
```

#### Link an external database

\>\_

```sh
deno deploy database link <name> [connectionString]
```

Links an external PostgreSQL database to your organization. You can provide a connection string or use individual flags.

**Options:**

*   `--hostname <host>` - Database hostname (conflicts with connection string)
*   `--username <user>` - Database username (conflicts with connection string)
*   `--password <pass>` - Database password (conflicts with connection string)
*   `--port <number>` - Database port (conflicts with connection string)
*   `--cert <cert>` - SSL certificate for the connection
*   `--dry-run` - Test the connection without actually linking

\>\_

```sh
# Link using a connection string
deno deploy database link my-db "postgres://user:pass@host:5432/mydb"

# Link using individual flags
deno deploy database link my-db \
  --hostname db.example.com \
  --username admin \
  --password secret \
  --port 5432

# Test the connection first
deno deploy database link my-db "postgres://user:pass@host:5432/mydb" --dry-run
```

#### Assign a database to an app

\>\_

```sh
deno deploy database assign <name> [--app <name>]
```

Assigns a database instance to an application. If `--app` is not provided, you will be prompted to select one interactively.

\>\_

```sh
deno deploy database assign my-db --app my-api
```

#### Detach a database from an app

\>\_

```sh
deno deploy database detach <name> [--app <name>]
```

Removes the connection between a database instance and an application.

\>\_

```sh
deno deploy database detach my-db --app my-api
```

#### Query a database

\>\_

```sh
deno deploy database query <name> <database> [query...]
```

Executes a SQL query against a database.

\>\_

```sh
deno deploy database query my-db mydb "SELECT * FROM users LIMIT 10"
```

#### List databases

\>\_

```sh
deno deploy database list [search]
```

Lists all database instances in the organization. Also available as `database ls`.

\>\_

```sh
# List all databases
deno deploy database list

# Filter by name
deno deploy database list my-db
```

#### Delete a database

\>\_

```sh
deno deploy database delete <name>
```

Permanently deletes a database instance. Also available as `database remove` or `database rm`.

\>\_

```sh
deno deploy database delete my-old-db
```

### Switch organization and application

Sets the default organization and application for subsequent commands, so you don't have to pass `--org` and `--app` every time.

\>\_

```sh
deno deploy switch [--org <name>] [--app <name>]
```

When run without flags, an interactive prompt lets you select the org and app.

**Options:**

*   `--org <name>` - The organization to switch to
*   `--app <name>` - The application to switch to

\>\_

```sh
# Switch interactively
deno deploy switch

# Switch to a specific org and app
deno deploy switch --org my-company --app my-api
```

### Logout

Removes the stored authentication token.

\>\_

```sh
deno deploy logout
```

### Application logs

Stream logs from a deployed application.

\>\_

```sh
deno deploy logs
```

**Options:**

*   `-h, --help` - Show help information
*   `--org <name>` - The name of the organization
*   `--app <name>` - The name of the application
*   `--start <date>` - The starting timestamp of the logs
*   `--end <date>` - The ending timestamp of the logs (requires --start)

\>\_

```sh
deno deploy logs --org my-org --app my-app --start "2024-01-01T00:00:00Z"
```

### Sandbox management

Interact with running sandboxes directly from the Deploy CLI.

\>\_

```sh
deno deploy sandbox --help
```

**Options:**

*   `-h, --help` - Show help information
*   `--token <token>` - Override the auth token used for sandbox operations
*   `--config <path>` - Custom path to a Deploy CLI config file
*   `--org <name>` - Organization that owns the sandboxes

#### List sandboxes

\>\_

```sh
deno deploy sandbox list --org my-org
```

Lists every sandbox in the organization along with status details.

#### Kill a sandbox

\>\_

```sh
deno deploy sandbox kill <sandbox-id> --org my-org
```

Immediately terminates the specified sandbox when you no longer need it.

#### SSH into a sandbox

\>\_

```sh
deno deploy sandbox ssh <sandbox-id> --org my-org
```

Starts an SSH session against a running sandbox for interactive debugging.

### Configure cloud connections

The `deploy` command includes tools to help you configure integrations for use as [Cloud Connections](/deploy/reference/cloud_connections/) in your applications.

#### AWS integration setup

[Configure AWS integration](/deploy/reference/cloud_connections/#aws%3A-easy-setup-with-deno-deploy-setup-aws) for use as a Cloud Connection in your application.

\>\_

```sh
deno deploy setup-aws --org <name> --app <name>
```

**Options:**

*   `-h, --help` - Show help information
*   `--org <name>` - The name of the organization (required)
*   `--app <name>` - The name of the application (required)

\>\_

```sh
deno deploy setup-aws --org my-org --app my-app
```

### Google Cloud Platform integration setup

[Configure Google Cloud Platform integration](/deploy/reference/cloud_connections/#setting-up-gcp) for use as a Cloud Connection in your application.

\>\_

```sh
deno deploy setup-gcp --org <name> --app <name>
```

**Options:**

*   `-h, --help` - Show help information
*   `--org <name>` - The name of the organization (required)
*   `--app <name>` - The name of the application (required)

\>\_

```sh
deno deploy setup-gcp --org my-org --app my-app
```

## Usage examples

### Basic deployment

\>\_

```sh
# Deploy current directory to production
deno deploy --prod

# Deploy with specific org and app
deno deploy --org my-company --app my-api --prod
```

### Creating applications

\>\_

```sh
# Start the interactive creation wizard
deno deploy create

# Create with a framework preset
deno deploy create --org my-company --app my-site \
  --source local --framework-preset fresh \
  --build-timeout 5 --build-memory-limit 1024 --region us

# Create a static site from a GitHub repo
deno deploy create --org my-company --app my-docs \
  --source github --owner my-github-org --repo my-docs-repo \
  --runtime-mode static --static-dir dist --single-page-app \
  --build-command "npm run build" \
  --build-timeout 10 --build-memory-limit 2048 --region global
```

### Switching context

\>\_

```sh
# Set a default org and app so you don't have to pass --org/--app every time
deno deploy switch --org my-company --app my-api

# Now these commands use the saved org and app automatically
deno deploy env list
deno deploy logs
```

### Database management

\>\_

```sh
# Provision a Deno KV database
deno deploy database provision my-kv --kind denokv --org my-company

# Link an external PostgreSQL database
deno deploy database link my-pg "postgres://user:pass@host:5432/db" --org my-company

# Assign a database to an app
deno deploy database assign my-kv --app my-api

# Query a database
deno deploy database query my-pg mydb "SELECT count(*) FROM users"
```

### Environment setup

\>\_

```sh
# Set up environment variables
deno deploy env add DATABASE_URL "postgresql://..." --secret
deno deploy env add SITE_NAME "My App"

# Load from .env file
deno deploy env load .env.production
```

### Monitoring

\>\_

```sh
# View recent logs
deno deploy logs --org my-company --app my-api

# View logs for specific time range
deno deploy logs --org my-company --app my-api \
  --start "2024-01-01T00:00:00Z" \
  --end "2024-01-01T23:59:59Z"
```

### Cloud integration

\>\_

```sh
# Set up AWS integration
deno deploy setup-aws --org my-company --app my-api

# Set up GCP integration
deno deploy setup-gcp --org my-company --app my-api
```

## Getting help

*   Use `deno deploy --help` for general help
*   Use `deno deploy <subcommand> --help` for specific subcommand help
*   Check the [Deno Deploy documentation](/deploy/) for platform-specific information

Command line usage:

```
deno deploy [OPTIONS] [args]...
```


