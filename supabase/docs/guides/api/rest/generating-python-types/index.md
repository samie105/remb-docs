---
title: "Generating Python Types"
source: "https://supabase.com/docs/guides/api/rest/generating-python-types"
canonical_url: "https://supabase.com/docs/guides/api/rest/generating-python-types"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:28.208Z"
content_hash: "9aa3567e5ab498d6300be1133633ca93e048635aaf605ce137dceda4acfbfdf7"
menu_path: ["Data REST API","Data REST API","Guides","Guides","Generating Python Types","Generating Python Types"]
section_path: ["Data REST API","Data REST API","Guides","Guides","Generating Python Types","Generating Python Types"]
nav_prev: {"path": "../client-libs/index.md", "title": "Client Libraries"}
nav_next: {"path": "../generating-types/index.md", "title": "Generating TypeScript Types"}
---

# 

Generating Python Types

## 

How to generate Python types for your API and Supabase libraries.

* * *

Supabase APIs are generated from your database, which means that we can use database introspection to generate type-safe API definitions.

## Generating types using Supabase CLI[#](#generating-types-using-supabase-cli)

The Supabase CLI is a single binary Go application that provides everything you need to setup a local development environment.

You can [install the CLI](https://www.npmjs.com/package/supabase) via npm or other supported package managers. The minimum required version of the CLI is [v2.66.0](https://github.com/supabase/cli/releases).

```
1npm i supabase --save-dev
```

Login with your Personal Access Token:

```
1npx supabase login
```

Before generating types, ensure you initialize your Supabase project:

```
1npx supabase init
```

Generate types for your project to produce the `database_types.py` file:

```
1npx supabase gen types --lang=python --project-id "$PROJECT_REF" --schema public > database.types.py
```

or in case of local development:

```
1npx supabase gen types --lang=python --local > database_types.py
```

These types are generated from your database schema. Given a table `public.movies`, the generated types will look like:

```
1create table public.movies (2  id bigint generated always as identity primary key,3  name text not null,4  data jsonb null5);
```

```
1class PublicMovies(BaseModel):2    data: Optional[Json[Any]] = Field(alias="data")3    id: int = Field(alias="id")4    name: str = Field(alias="name")56class PublicMoviesInsert(TypedDict):7    data: NotRequired[Annotated[Json[Any], Field(alias="data")]]8    id: NotRequired[Annotated[int, Field(alias="id")]]9    name: Annotated[str, Field(alias="name")]1011class PublicMoviesUpdate(TypedDict):12    data: NotRequired[Annotated[Json[Any], Field(alias="data")]]13    id: NotRequired[Annotated[int, Field(alias="id")]]14    name: NotRequired[Annotated[str, Field(alias="name")]]
```

## Types for select, insert and update[#](#types-for-select-insert-and-update)

The `PublicMovies` class is used to parse `SELECT` results from the `movies` table, while `PublicMoviesInsert` and `PublicMoviesUpdate` are used to format and provide completion for arguments for `insert` and `update` respectively.

```
1from .database_types import PublicMovies, PublicMoviesInsert, PublicMoviesUpdate2from supabase import create_client34client = create_client("YOUR_SUPABASE_URL", "YOUR_SUPABASE_KEY")5movies = client.table("movies")67# Select8selected = [PublicMovies(m) for m in movies.select("*").execute().data]910# Insert11inserted = [PublicMovies(m) for m in movies.insert(PublicMoviesInsert(name="foo", data="bar")) \12                                          .execute().data]1314# Update15updated  = [PublicMovies(m) for m in movies.update(PublicMoviesUpdate(name="bar")) \16                                        .eq("id", 5) \17                                        .execute().data]
```

## Update types automatically with GitHub Actions[#](#update-types-automatically-with-github-actions)

One way to keep your type definitions in sync with your database is to set up a GitHub action that runs on a schedule.

Add the following script to your `package.json` to run it using `npm run update-types`

```
1"update-types": "npx supabase gen types --lang=python --project-id \"$PROJECT_REF\" > database_types.py"
```

Create a file `.github/workflows/update-types.yml` with the following snippet to define the action along with the environment variables. This script will commit new type changes to your repo every night.

```
1name: Update database types23on:4  schedule:5    # sets the action to run daily. You can modify this to run the action more or less frequently6    - cron: '0 0 * * *'78jobs:9  update:10    runs-on: ubuntu-latest11    permissions:12      contents: write13    env:14      SUPABASE_ACCESS_TOKEN: ${{ secrets.ACCESS_TOKEN }}15      PROJECT_REF: <your-project-id>16    steps:17      - uses: actions/checkout@v418        with:19          persist-credentials: false20          fetch-depth: 021      - uses: actions/setup-node@v422        with:23          node-version: 2224      - run: npm run update-types25      - name: check for file changes26        id: git_status27        run: |28          echo "status=$(git status -s)" >> $GITHUB_OUTPUT29      - name: Commit files30        if: ${{contains(steps.git_status.outputs.status, ' ')}}31        run: |32          git add database_types.py33          git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com"34          git config --local user.name "github-actions[bot]"35          git commit -m "Update database types" -a36      - name: Push changes37        if: ${{contains(steps.git_status.outputs.status, ' ')}}38        uses: ad-m/github-push-action@master39        with:40          github_token: ${{ secrets.GITHUB_TOKEN }}41          branch: ${{ github.ref }}
```

## Resources[#](#resources)

*   [Generating Supabase types with GitHub Actions](https://blog.esteetey.dev/how-to-create-and-test-a-github-action-that-generates-types-from-supabase-database)
*   [Generating TypeScript Types](/docs/guides/api/rest/generating-types)
