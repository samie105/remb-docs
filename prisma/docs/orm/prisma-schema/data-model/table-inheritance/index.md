---
title: "Table inheritance"
source: "https://www.prisma.io/docs/orm/prisma-schema/data-model/table-inheritance"
canonical_url: "https://www.prisma.io/docs/orm/prisma-schema/data-model/table-inheritance"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:31.311Z"
content_hash: "f225fdeed1a9596cbe167dc549198eb77745916ad34bb5ecf38fcac3f52dc53e"
menu_path: ["Table inheritance"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-schema/data-model/unsupported-database-features/index.md", "title": "Unsupported database features (Prisma Schema)"}
nav_next: {"path": "prisma/docs/orm/prisma-schema/data-model/views/index.md", "title": "Views"}
---

Learn about the use cases and patterns for table inheritance in Prisma ORM that enable usage of union types or polymorphic structures in your application.

Table inheritance is a software design pattern that allows the modeling of hierarchical relationships between entities. Using table inheritance on the database level can also enable the use of union types in your JavaScript/TypeScript application or share a set of common properties across multiple models.

This page introduces two approaches to table inheritance and explains how to use them with Prisma ORM.

A common use case for table inheritance may be when an application needs to display a _feed_ of some kind of _content activities_. A content activity in this case, could be a _video_ or an _article_. As an example, let's assume that:

*   a content activity always has an `id` and a `url`
*   in addition to `id` and a `url`, a video also has a `duration` (modeled as an `Int`)
*   in addition to `id` and a `url`, an article also a `body` (modeled as a `String`)

### [Use cases](#use-cases)

#### [Union types](#union-types)

Union types are a convenient feature in TypeScript that allows developers to work more flexibly with the types in their data model.

In TypeScript, union types look as follows:

```
type Activity = Video | Article;
```

While [it's currently not possible to model union types in the Prisma schema](https://github.com/prisma/prisma/issues/2505), you can use them with Prisma ORM by using table inheritance and some additional type definitions.

#### [Sharing properties across multiple models](#sharing-properties-across-multiple-models)

If you have a use case where multiple models should share a particular set of properties, you can model this using table inheritance as well.

For example, if both the `Video` and `Article` models from above should have a shared `title` property, you can achieve this with table inheritance as well.

### [Example](#example)

In a simple Prisma schema, this would look as follows. Note that we're adding a `User` model as well to illustrate how this can work with relations:

```
model Video {
  id       Int    @id
  url      String @unique
  duration Int

  user   User @relation(fields: [userId], references: [id])
  userId Int
}

model Article {
  id   Int    @id
  url  String @unique
  body String

  user   User @relation(fields: [userId], references: [id])
  userId Int
}

model User {
  id       Int       @id
  name     String
  videos   Video[]
  articles Article[]
}
```

Let's investigate how we can model this using table inheritance.

### [Single-table vs multi-table inheritance](#single-table-vs-multi-table-inheritance)

Here is a quick comparison of the two main approaches for table inheritance:

*   **Single-table inheritance (STI)**: Uses a _single_ table to store data of _all_ the different entities in one location. In our example, there'd be a single `Activity` table with the `id`, `url` as well as the `duration` and `body` column. It also uses a `type` column that indicates whether an _activity_ is a _video_ or an _article_.
*   **Multi-table inheritance (MTI)**: Uses _multiple_ tables to store the data of the different entities separately and links them via foreign keys. In our example, there'd be an `Activity` table with the `id`, `url` column, a `Video` table with the `duration` and a foreign key to `Activity` as well as an `Article` table with the `body` and a foreign key. There is also a `type` column that acts as a discriminator and indicates whether an _activity_ is a _video_ or an _article_. Note that multi-table inheritance is also sometimes called _delegated types_.

You can learn about the tradeoffs of both approaches [below](#tradeoffs-between-sti-and-mti).

### [Data model](#data-model)

Using STI, the above scenario can be modeled as follows:

```
model Activity {
  id       Int          @id // shared
  url      String       @unique // shared
  duration Int? // video-only
  body     String? // article-only
  type     ActivityType // discriminator

  owner   User @relation(fields: [ownerId], references: [id])
  ownerId Int
}

enum ActivityType {
  Video
  Article
}

model User {
  id         Int        @id @default(autoincrement())
  name       String?
  activities Activity[]
}
```

A few things to note:

*   The model-specific properties `duration` and `body` must be marked as optional (i.e., with `?`). That's because a record in the `Activity` table that represents a _video_ must not have a value for `body`. Conversely, an `Activity` record representing an _article_ can never have a `duration` set.
*   The `type` discriminator column indicates whether each record represents a _video_ or an _article_ item.

### [Prisma Client API](#prisma-client-api)

Due to how Prisma ORM generates types and an API for the data model, there will only to be an `Activity` type and the CRUD queries that belong to it (`create`, `update`, `delete`, ...) available to you.

#### [Querying for videos and articles](#querying-for-videos-and-articles)

You can now query for only _videos_ or _articles_ by filtering on the `type` column. For example:

```
// Query all videos
const videos = await prisma.activity.findMany({
  where: { type: "Video" },
});

// Query all articles
const articles = await prisma.activity.findMany({
  where: { type: "Article" },
});
```

#### [Defining dedicated types](#defining-dedicated-types)

When querying for videos and articles like that, TypeScript will still only recognize an `Activity` type. That can be annoying because even the objects in `videos` will have (optional) `body` and the objects in `articles` will have (optional) `duration` fields.

If you want to have type safety for these objects, you need to define dedicated types for them. You can do this, for example, by using the generated `Activity` type and the TypeScript `Omit` utility type to remove properties from it:

```
import { Activity } from "../prisma/generated/client";

type Video = Omit<Activity, "body" | "type">;
type Article = Omit<Activity, "duration" | "type">;
```

In addition, it will be helpful to create mapping functions that convert an object of type `Activity` to the `Video` and `Article` types:

```
function activityToVideo(activity: Activity): Video {
  return {
    url: activity.url,
    duration: activity.duration ? activity.duration : -1,
    ownerId: activity.ownerId,
  } as Video;
}

function activityToArticle(activity: Activity): Article {
  return {
    url: activity.url,
    body: activity.body ? activity.body : "",
    ownerId: activity.ownerId,
  } as Article;
}
```

Now you can turn an `Activity` into a more specific type (i.e., `Article` or `Video`) after querying:

```
const videoActivities = await prisma.activity.findMany({
  where: { type: "Video" },
});
const videos: Video[] = videoActivities.map(activityToVideo);
```

#### [Using Prisma Client extension for a more convenient API](#using-prisma-client-extension-for-a-more-convenient-api)

You can use [Prisma Client extensions](prisma/docs/orm/prisma-client/client-extensions/index.md) to create a more convenient API for the table structures in your database.

### [Data model](#data-model-1)

Using MTI, the above scenario can be modeled as follows:

```
model Activity {
  id   Int          @id @default(autoincrement())
  url  String // shared
  type ActivityType // discriminator

  video   Video? // model-specific 1-1 relation
  article Article? // model-specific 1-1 relation

  owner   User @relation(fields: [ownerId], references: [id])
  ownerId Int
}

model Video {
  id         Int      @id @default(autoincrement())
  duration   Int // video-only
  activityId Int      @unique
  activity   Activity @relation(fields: [activityId], references: [id])
}

model Article {
  id         Int      @id @default(autoincrement())
  body       String // article-only
  activityId Int      @unique
  activity   Activity @relation(fields: [activityId], references: [id])
}

enum ActivityType {
  Video
  Article
}

model User {
  id         Int        @id @default(autoincrement())
  name       String?
  activities Activity[]
}
```

A few things to note:

*   A 1-1 relation is needed between `Activity` and `Video` as well as `Activity` and `Article`. This relationship is used to fetch the specific information about a record when needed.
*   The model-specific properties `duration` and `body` can be made _required_ with this approach.
*   The `type` discriminator column indicates whether each record represents a _video_ or an _article_ item.

### [Prisma Client API](#prisma-client-api-1)

This time, you can query for videos and articles directly via the `video` and `article` properties on your `PrismaClient` instance.

#### [Querying for videos and articles](#querying-for-videos-and-articles-1)

If you want to access the shared properties, you need to use `include` to fetch the relation to `Activity`.

```
// Query all videos
const videos = await prisma.video.findMany({
  include: { activity: true },
});

// Query all articles
const articles = await prisma.article.findMany({
  include: { activity: true },
});
```

Depending on your needs, you may also query the other way around by filtering on the `type` discriminator column:

```
// Query all videos
const videoActivities = await prisma.activity.findMany({
  where: { type: 'Video' }
  include: { video: true }
})
```

#### [Defining dedicated types](#defining-dedicated-types-1)

While a bit more convenient in terms of types compared to STI, the generated typings likely still won't fit all your needs.

Here's how you can define `Video` and `Article` types by combining Prisma ORM's generated `Video` and `Article` types with the `Activity` type. These combinations create a new type with the desired properties. Note that we're also omitting the `type` discriminator column because that's not needed anymore on the specific types:

```
import { Video as VideoDB, Article as ArticleDB, Activity } from "../prisma/generated/client";

type Video = Omit<VideoDB & Activity, "type">;
type Article = Omit<ArticleDB & Activity, "type">;
```

Once these types are defined, you can define mapping functions to convert the types you receive from the queries above into the desired `Video` and `Article` types. Here's the example for the `Video` type:

```
import { Prisma, Video as VideoDB, Activity } from "../prisma/generated/client";

type Video = Omit<VideoDB & Activity, "type">;

// Create `VideoWithActivity` typings for the objects returned above
const videoWithActivity = Prisma.validator<Prisma.VideoDefaultArgs>()({
  include: { activity: true },
});
type VideoWithActivity = Prisma.VideoGetPayload<typeof videoWithActivity>;

// Map to `Video` type
function toVideo(a: VideoWithActivity): Video {
  return {
    id: a.id,
    url: a.activity.url,
    ownerId: a.activity.ownerId,
    duration: a.duration,
    activityId: a.activity.id,
  };
}
```

Now you can take the objects returned by the queries above and transform them using `toVideo`:

```
const videoWithActivities = await prisma.video.findMany({
  include: { activity: true },
});
const videos: Video[] = videoWithActivities.map(toVideo);
```

#### [Using Prisma Client extension for a more convenient API](#using-prisma-client-extension-for-a-more-convenient-api-1)

You can use [Prisma Client extensions](prisma/docs/orm/prisma-client/client-extensions/index.md) to create a more convenient API for the table structures in your database.

*   **Data model**: The data model may feel more clean with MTI. With STI, you may end up with very wide rows and lots of columns that have `NULL` values in them.
*   **Performance**: MTI may come with a performance cost because you need to join the parent and child tables to access _all_ properties relevant for a model.
*   **Typings**: With Prisma ORM, MTI gives you proper typings for the specific models (i.e., `Article` and `Video` in the examples above) already, while you need to create these from scratch with STI.
*   **IDs / Primary keys**: With MTI, records have two IDs (one on the parent and another on the child table) that may not match. You need to consider this in the business logic of your application.

While Prisma ORM doesn't natively support union types or polymorphism at the moment, you can check out [Zenstack](https://github.com/zenstackhq/zenstack) which is adding an extra layer of features to the Prisma schema. Read their [blog post about polymorphism in Prisma ORM](https://zenstack.dev/blog/polymorphism) to learn more.

