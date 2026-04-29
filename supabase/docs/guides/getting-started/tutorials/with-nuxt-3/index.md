---
title: "Build a User Management App with Nuxt 3"
source: "https://supabase.com/docs/guides/getting-started/tutorials/with-nuxt-3"
canonical_url: "https://supabase.com/docs/guides/getting-started/tutorials/with-nuxt-3"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:05.762Z"
content_hash: "d12c6caaeba0c80c83961f011149b1caf11df6804aa53c26c04e3fe8495da93f"
menu_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","Nuxt 3","Nuxt 3"]
section_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","Nuxt 3","Nuxt 3"]
nav_prev: {"path": "../with-nextjs/index.md", "title": "Build a User Management App with Next.js"}
nav_next: {"path": "../with-react/index.md", "title": "Build a User Management App with React"}
---

# 

Build a User Management App with Nuxt 3

* * *

##### Explore drop-in UI components for your Supabase app.

UI components built on shadcn/ui that connect to Supabase via a single command.

[Explore Components](https://supabase.com/ui)

This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/nuxt3-user-management).

## Project setup[#](#project-setup)

Before you start building you need to set up the Database and API. You can do this by starting a new Project in Supabase and then creating a "schema" inside the database.

### Create a project[#](#create-a-project)

1.  [Create a new project](/dashboard) in the Supabase Dashboard.
2.  Enter your project details.
3.  Wait for the new database to launch.

### Set up the database schema[#](#set-up-the-database-schema)

Now set up the database schema. You can use the "User Management Starter" quickstart in the SQL Editor, or you can copy/paste the SQL from below and run it.

1.  Go to the [SQL Editor](/dashboard/project/_/sql) page in the Dashboard.
2.  Click **User Management Starter** under the **Community > Quickstarts** tab.
3.  Click **Run**.

You can pull the database schema down to your local project by running the `db pull` command. Read the [local development docs](/docs/guides/cli/local-development#link-your-project) for detailed instructions.

```
1supabase link --project-ref <project-id>2# You can get <project-id> from your project's dashboard URL: https://supabase.com/dashboard/project/<project-id>3supabase db pull
```

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=nuxt).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=nuxt), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

## Building the app[#](#building-the-app)

Let's start building the Vue 3 app from scratch.

### Initialize a Nuxt 3 app[#](#initialize-a-nuxt-3-app)

We can use [`nuxi init`](https://nuxt.com/docs/getting-started/installation) to create an app called `nuxt-user-management`:

```
1npx nuxi init nuxt-user-management23cd nuxt-user-management
```

Then let's install the only additional dependency: [Nuxt Supabase](https://supabase.nuxtjs.org/). We only need to import Nuxt Supabase as a dev dependency.

```
1npm install @nuxtjs/supabase --save-dev
```

And finally we want to save the environment variables in a `.env`. All we need are the API URL and the key that you copied [earlier](#get-api-details).

```
1SUPABASE_URL="YOUR_SUPABASE_URL"2SUPABASE_KEY="YOUR_SUPABASE_PUBLISHABLE_KEY"
```

These variables will be exposed on the browser, and that's completely fine since we have [Row Level Security](/docs/guides/auth#row-level-security) enabled on our Database. Amazing thing about [Nuxt Supabase](https://supabase.nuxtjs.org/) is that setting environment variables is all we need to do in order to start using Supabase. No need to initialize Supabase. The library will take care of it automatically.

### App styling (optional)[#](#app-styling-optional)

An optional step is to update the CSS file `assets/main.css` to make the app look nice. You can find the full contents of this file [here](https://github.com/supabase-community/nuxt3-quickstarter/blob/main/assets/main.css).

```
1import { defineNuxtConfig } from 'nuxt'23// https://v3.nuxtjs.org/api/configuration/nuxt.config4export default defineNuxtConfig({5  modules: ['@nuxtjs/supabase'],6  css: ['@/assets/main.css'],7})
```

### Set up Auth component[#](#set-up-auth-component)

Let's set up a Vue component to manage logins and sign ups. We'll use Magic Links, so users can sign in with their email without using passwords.

```
1<script setup>2const supabase = useSupabaseClient()34const loading = ref(false)5const email = ref('')67const handleLogin = async () => {8  try {9    loading.value = true10    const { error } = await supabase.auth.signInWithOtp({ email: email.value })11    if (error) throw error12    alert('Check your email for the login link!')13  } catch (error) {14    alert(error.error_description || error.message)15  } finally {16    loading.value = false17  }18}19</script>2021<template>22  <form class="row flex-center flex" @submit.prevent="handleLogin">23    <div class="col-6 form-widget">24      <h1 class="header">Supabase + Nuxt 3</h1>25      <p class="description">Sign in via magic link with your email below</p>26      <div>27        <input class="inputField" type="email" placeholder="Your email" v-model="email" />28      </div>29      <div>30        <input31          type="submit"32          class="button block"33          :value="loading ? 'Loading' : 'Send magic link'"34          :disabled="loading"35        />36      </div>37    </div>38  </form>39</template>
```

### User state[#](#user-state)

To access the user information, use the composable [`useSupabaseUser`](https://supabase.nuxtjs.org/composables/usesupabaseuser) provided by the Supabase Nuxt module.

### Account component[#](#account-component)

After a user is signed in we can allow them to edit their profile details and manage their account. Let's create a new component for that called `Account.vue`.

```
1<script setup>2const supabase = useSupabaseClient()34const loading = ref(true)5const username = ref('')6const website = ref('')7const avatar_path = ref('')89loading.value = true10const user = useSupabaseUser()1112const { data } = await supabase13  .from('profiles')14  .select(`username, website, avatar_url`)15  .eq('id', user.value.id)16  .single()1718if (data) {19  username.value = data.username20  website.value = data.website21  avatar_path.value = data.avatar_url22}2324loading.value = false2526async function updateProfile() {27  try {28    loading.value = true29    const user = useSupabaseUser()3031    const updates = {32      id: user.value.id,33      username: username.value,34      website: website.value,35      avatar_url: avatar_path.value,36      updated_at: new Date(),37    }3839    const { error } = await supabase.from('profiles').upsert(updates, {40      returning: 'minimal', // Don't return the value after inserting41    })42    if (error) throw error43  } catch (error) {44    alert(error.message)45  } finally {46    loading.value = false47  }48}4950async function signOut() {51  try {52    loading.value = true53    const { error } = await supabase.auth.signOut()54    if (error) throw error55    user.value = null56  } catch (error) {57    alert(error.message)58  } finally {59    loading.value = false60  }61}62</script>6364<template>65  <form class="form-widget" @submit.prevent="updateProfile">66    <div>67      <label for="email">Email</label>68      <input id="email" type="text" :value="user.email" disabled />69    </div>70    <div>71      <label for="username">Username</label>72      <input id="username" type="text" v-model="username" />73    </div>74    <div>75      <label for="website">Website</label>76      <input id="website" type="url" v-model="website" />77    </div>7879    <div>80      <input81        type="submit"82        class="button primary block"83        :value="loading ? 'Loading ...' : 'Update'"84        :disabled="loading"85      />86    </div>8788    <div>89      <button class="button block" @click="signOut" :disabled="loading">Sign Out</button>90    </div>91  </form>92</template>
```

### Launch![#](#launch)

Now that we have all the components in place, let's update `app.vue`:

```
1<script setup>2const user = useSupabaseUser()3</script>45<template>6  <div class="container" style="padding: 50px 0 100px 0">7    <Account v-if="user" />8    <Auth v-else />9  </div>10</template>
```

Once that's done, run this in a terminal window:

```
1npm run dev
```

And then open the browser to [localhost:3000](http://localhost:3000) and you should see the completed app.

![Supabase Nuxt 3](/docs/img/supabase-vue-3-demo.png)

## Bonus: Profile photos[#](#bonus-profile-photos)

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.

### Create an upload widget[#](#create-an-upload-widget)

Let's create an avatar for the user so that they can upload a profile photo. We can start by creating a new component:

```
1<script setup>2const props = defineProps(['path'])3const { path } = toRefs(props)45const emit = defineEmits(['update:path', 'upload'])67const supabase = useSupabaseClient()89const uploading = ref(false)10const src = ref('')11const files = ref()1213const downloadImage = async () => {14  try {15    const { data, error } = await supabase.storage.from('avatars').download(path.value)16    if (error) throw error17    src.value = URL.createObjectURL(data)18  } catch (error) {19    console.error('Error downloading image: ', error.message)20  }21}2223const uploadAvatar = async (evt) => {24  files.value = evt.target.files25  try {26    uploading.value = true2728    if (!files.value || files.value.length === 0) {29      throw new Error('You must select an image to upload.')30    }3132    const file = files.value[0]33    const fileExt = file.name.split('.').pop()34    const fileName = `${Math.random()}.${fileExt}`35    const filePath = `${fileName}`3637    const { error: uploadError } = await supabase.storage.from('avatars').upload(filePath, file)3839    if (uploadError) throw uploadError4041    emit('update:path', filePath)42    emit('upload')43  } catch (error) {44    alert(error.message)45  } finally {46    uploading.value = false47  }48}4950downloadImage()5152watch(path, () => {53  if (path.value) {54    downloadImage()55  }56})57</script>5859<template>60  <div>61    <img62      v-if="src"63      :src="src"64      alt="Avatar"65      class="avatar image"66      style="width: 10em; height: 10em;"67    />68    <div v-else class="avatar no-image" :style="{ height: size, width: size }" />6970    <div style="width: 10em; position: relative;">71      <label class="button primary block" for="single">72        {{ uploading ? 'Uploading ...' : 'Upload' }}73      </label>74      <input75        style="position: absolute; visibility: hidden;"76        type="file"77        id="single"78        accept="image/*"79        @change="uploadAvatar"80        :disabled="uploading"81      />82    </div>83  </div>84</template>
```

### Add the new widget[#](#add-the-new-widget)

And then we can add the widget to the Account page:

```
1<script setup>2const supabase = useSupabaseClient()34const loading = ref(true)5const username = ref('')6const website = ref('')7const avatar_path = ref('')89loading.value = true10const user = useSupabaseUser()1112const { data } = await supabase13  .from('profiles')14  .select(`username, website, avatar_url`)15  .eq('id', user.value.id)16  .single()1718if (data) {19  username.value = data.username20  website.value = data.website21  avatar_path.value = data.avatar_url22}2324loading.value = false2526async function updateProfile() {27  try {28    loading.value = true29    const user = useSupabaseUser()3031    const updates = {32      id: user.value.id,33      username: username.value,34      website: website.value,35      avatar_url: avatar_path.value,36      updated_at: new Date(),37    }3839    const { error } = await supabase.from('profiles').upsert(updates, {40      returning: 'minimal', // Don't return the value after inserting41    })4243    if (error) throw error44  } catch (error) {45    alert(error.message)46  } finally {47    loading.value = false48  }49}5051async function signOut() {52  try {53    loading.value = true54    const { error } = await supabase.auth.signOut()55    if (error) throw error56  } catch (error) {57    alert(error.message)58  } finally {59    loading.value = false60  }61}62</script>6364<template>65  <form class="form-widget" @submit.prevent="updateProfile">66    <Avatar v-model:path="avatar_path" @upload="updateProfile" />67    <div>68      <label for="email">Email</label>69      <input id="email" type="text" :value="user.email" disabled />70    </div>71    <div>72      <label for="username">Name</label>73      <input id="username" type="text" v-model="username" />74    </div>75    <div>76      <label for="website">Website</label>77      <input id="website" type="url" v-model="website" />78    </div>7980    <div>81      <input82        type="submit"83        class="button primary block"84        :value="loading ? 'Loading ...' : 'Update'"85        :disabled="loading"86      />87    </div>8889    <div>90      <button class="button block" @click="signOut" :disabled="loading">Sign Out</button>91    </div>92  </form>93</template>
```

That is it! You should now be able to upload a profile photo to Supabase Storage and you have a fully functional application.
