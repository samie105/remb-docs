---
title: "Postgres Roles"
source: "https://supabase.com/docs/guides/database/postgres/roles"
canonical_url: "https://supabase.com/docs/guides/database/postgres/roles"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:40.804Z"
content_hash: "d974b18fc666cf52647cd826d75ccec0acc0f77ee6f2f6de9df9ae94f2f63a7e"
menu_path: ["Database","Database","Access and security","Access and security","Managing Postgres Roles","Managing Postgres Roles"]
section_path: ["Database","Database","Access and security","Access and security","Managing Postgres Roles","Managing Postgres Roles"]
nav_prev: {"path": "supabase/docs/guides/database/postgres/indexes/index.md", "title": "Managing Indexes in Postgres"}
nav_next: {"path": "supabase/docs/guides/database/postgres/roles-superuser/index.md", "title": "Roles, superuser access and unsupported operations"}
---

# 

Postgres Roles

## 

Managing access to your Postgres database and configuring permissions.

* * *

Postgres manages database access permissions using the concept of roles. Generally you wouldn't use these roles for your own application - they are mostly for configuring _system access_ to your database. If you want to configure _application access_, then you should use [Row Level Security](../row-level-security/index.md) (RLS). You can also implement [Role-based Access Control](../../../api/custom-claims-and-role-based-access-control-rbac/index.md) on top of RLS.

## Users vs roles[#](#users-vs-roles)

In Postgres, roles can function as users or groups of users. Users are roles with login privileges, while groups (also known as role groups) are roles that don't have login privileges but can be used to manage permissions for multiple users.

## Creating roles[#](#creating-roles)

You can create a role using the `create role` command:

```
1create role "role_name";
```

## Creating users[#](#creating-users)

Roles and users are essentially the same in Postgres, however if you want to use password-logins for a specific role, then you can use `WITH LOGIN PASSWORD`:

```
1create role "role_name" with login password 'extremely_secure_password';
```

## Passwords[#](#passwords)

Your Postgres database is the core of your Supabase project, so it's important that every role has a strong, secure password at all times. Here are some tips for creating a secure password:

*   Use a password manager to generate it.
*   Make a long password (12 characters at least).
*   Don't use any common dictionary words.
*   Use both upper and lower case characters, numbers, and special symbols.

### Special symbols in passwords[#](#special-symbols-in-passwords)

If you use special symbols in your Postgres password, you must remember to [percent-encode](https://en.wikipedia.org/wiki/Percent-encoding) your password later if using the Postgres connection string, for example, `postgresql://postgres.projectref:p%3Dword@aws-0-us-east-1.pooler.supabase.com:6543/postgres`

### Changing your project password[#](#changing-your-project-password)

When you created your project you were also asked to enter a password. This is the password for the `postgres` role in your database. You can update this from the Dashboard under the [Database Settings](/dashboard/project/_/database/settings) page. You should _never_ give this to third-party service unless you absolutely trust them. Instead, we recommend that you create a new user for every service that you want to give access too. This will also help you with debugging - you can see every query that each role is executing in your database within `pg_stat_statements`.

Changing the password does not result in any downtime. All connected services, such as PostgREST, PgBouncer, and other Supabase managed services, are automatically updated to use the latest password to ensure availability. However, if you have any external services connecting to the Supabase database using hardcoded username/password credentials, a manual update will be required.

## Granting permissions[#](#granting-permissions)

Roles can be granted various permissions on database objects using the `GRANT` command. Permissions include `SELECT`, `INSERT`, `UPDATE`, and `DELETE`. You can configure access to almost any object inside your database - including tables, views, functions, and triggers.

## Revoking permissions[#](#revoking-permissions)

Permissions can be revoked using the `REVOKE` command:

```
1REVOKE permission_type ON object_name FROM role_name;
```

## Role hierarchy[#](#role-hierarchy)

Roles can be organized in a hierarchy, where one role can inherit permissions from another. This simplifies permission management, as you can define permissions at a higher level and have them automatically apply to all child roles.

### Role inheritance[#](#role-inheritance)

To create a role hierarchy, you first need to create the parent and child roles. The child role will inherit permissions from its parent. Child roles can be added using the INHERIT option when creating the role:

```
1create role "child_role_name" inherit "parent_role_name";
```

### Preventing inheritance[#](#preventing-inheritance)

In some cases, you might want to prevent a role from having a child relationship (typically superuser roles). You can prevent inheritance relations using `NOINHERIT`:

```
1alter role "child_role_name" noinherit;
```

## Supabase roles[#](#supabase-roles)

Postgres comes with a set of [predefined roles](https://www.postgresql.org/docs/current/predefined-roles.html). Supabase extends this with a default set of roles which are configured on your database when you start a new project:

### `postgres`[#](#postgres)

The default Postgres role. This has admin privileges.

### `anon`[#](#anon)

For unauthenticated, public access. This is the role which the API (PostgREST) will use when a user _is not_ logged in.

### `authenticator`[#](#authenticator)

A special role for the API (PostgREST). It has very limited access, and is used to validate a JWT and then "change into" another role determined by the JWT verification.

### `authenticated`[#](#authenticated)

For "authenticated access." This is the role which the API (PostgREST) will use when a user _is_ logged in.

### `service_role`[#](#servicerole)

For elevated access. This role is used by the API (PostgREST) to bypass Row Level Security.

### `supabase_auth_admin`[#](#supabaseauthadmin)

Used by the Auth middleware to connect to the database and run migration. Access is scoped to the `auth` schema.

### `supabase_storage_admin`[#](#supabasestorageadmin)

Used by the Auth middleware to connect to the database and run migration. Access is scoped to the `storage` schema.

### `supabase_etl_admin`[#](#supabaseetladmin)

Used by [Replication powered by Supabase ETL](../../replication/index.md) to replicate database changes to external destinations. Has read-all access and replication privileges for change data capture, bypasses Row Level Security, and can write to the `etl` schema.

### `dashboard_user`[#](#dashboarduser)

For running commands via the Supabase UI.

### `supabase_admin`[#](#supabaseadmin)

An internal role Supabase uses for administrative tasks, such as running upgrades and automations.

## Resources[#](#resources)

*   Official Postgres docs: [Database Roles](https://www.postgresql.org/docs/current/database-roles.html)
*   Official Postgres docs: [Role Membership](https://www.postgresql.org/docs/current/role-membership.html)
*   Official Postgres docs: [Function Permissions](https://www.postgresql.org/docs/current/perm-functions.html)
