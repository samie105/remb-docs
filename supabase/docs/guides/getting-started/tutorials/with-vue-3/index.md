---
title: "Build a User Management App with Vue 3"
source: "https://supabase.com/docs/guides/getting-started/tutorials/with-vue-3"
canonical_url: "https://supabase.com/docs/guides/getting-started/tutorials/with-vue-3"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:27.584Z"
content_hash: "318c627025340b8f4d9a61b71f3e164a86a8ff32d6d98dbd9005746679884d46"
menu_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","Vue 3","Vue 3"]
section_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","Vue 3","Vue 3"]
nav_prev: {"path": "supabase/docs/guides/getting-started/tutorials/with-swift/index.md", "title": "Build a User Management App with Swift and SwiftUI"}
nav_next: {"path": "supabase/docs/guides/local-development/cli/getting-started/index.md", "title": "Supabase CLI"}
---

# 

Build a User Management App with Vue 3

* * *

##### Explore drop-in UI components for your Supabase app.

UI components built on shadcn/ui that connect to Supabase via a single command.

[Explore Components](https://supabase.com/ui)

This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/vue3-user-management).

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

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=vuejs).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=vuejs), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

## Building the app[#](#building-the-app)

Start building the Vue 3 app from scratch.

### Initialize a Vue 3 app[#](#initialize-a-vue-3-app)

This guide uses [Vite with Vue 3 Template](https://vitejs.dev/guide/#scaffolding-your-first-vite-project) to initialize an app called `supabase-vue-3`:

```
1# npm 6.x2npm create vite@latest supabase-vue-3 --template vue34# npm 7+, extra double-dash is needed:5npm create vite@latest supabase-vue-3 -- --template vue67cd supabase-vue-3
```

Then install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js)

```
1npm install @supabase/supabase-js
```

And finally save the environment variables in a `.env` file, you need the API URL and the key that you copied [earlier](#get-api-details).

```
1VITE_SUPABASE_URL=YOUR_SUPABASE_URL2VITE_SUPABASE_PUBLISHABLE_KEY=YOUR_SUPABASE_PUBLISHABLE_KEY
```

With the API credentials in place, create an `src/supabase.js` helper file to initialize the Supabase client. These variables are exposed on the browser, and that's fine since you have [Row Level Security](/docs/guides/auth#row-level-security) enabled on the Database.

###### src/supabase.js

```
1import { createClient } from '@supabase/supabase-js'23const supabaseUrl = import.meta.env.VITE_SUPABASE_URL4const supabasePublishableKey = import.meta.env.VITE_SUPABASE_KEY56export const supabase = createClient(supabaseUrl, supabasePublishableKey)
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/vue3-user-management/src/supabase.js)

Optionally, update [src/style.css](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/vue3-user-management/src/style.css) to style the app.

### Set up a login component[#](#set-up-a-login-component)

Set up an `src/components/Auth.vue` component to manage to add Magic Links as an option, so users can sign in with their email without using passwords.

###### src/components/Auth.vue

```
1<script setup>2import { ref } from 'vue'3import { supabase } from '../supabase'45const loading = ref(false)6const email = ref('')78const handleLogin = async () => {9    try {10        loading.value = true11        const { error } = await supabase.auth.signInWithOtp({ email: email.value })12        if (error) throw error13        alert('Check your email for the login link!')14    } catch (error) {15        if (error instanceof Error) {16            alert(error.message)17        }18    } finally {19        loading.value = false20    }21}22</script>2324<template>25    <form class="row flex-center flex" @submit.prevent="handleLogin">26        <div class="col-6 form-widget">27            <h1 class="header">Supabase + Vue 3</h1>28            <p class="description">Sign in via magic link with your email below</p>29            <div>30                <input class="inputField" type="email" placeholder="Your email" v-model="email" />31            </div>32            <div>33                <input type="submit" class="button block" :value="loading ? 'Loading' : 'Send magic link'"34                    :disabled="loading" />35            </div>36        </div>37    </form>38</template>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/vue3-user-management/src/components/Auth.vue)

### Account page[#](#account-page)

After a user signs in, allow them to edit their profile details and manage their account. Create a new `src/components/Account.vue` component to handle this.

###### src/components/Account.vue

```
1<script setup>2import { supabase } from '../supabase'3import { onMounted, ref, toRefs } from 'vue'4import Avatar from './Avatar.vue';56const props = defineProps(['claims'])7const { claims } = toRefs(props)89const loading = ref(true)10const username = ref('')11const website = ref('')12const avatar_url = ref('')1314onMounted(() => {15    getProfile()16})1718async function getProfile() {19    try {20        loading.value = true21        let { data, error, status } = await supabase22            .from('profiles')23            .select(`username, website, avatar_url`)24            .eq('id', claims.value.sub)25            .single()2627        if (error && status !== 406) throw error2829        if (data) {30            username.value = data.username31            website.value = data.website32            avatar_url.value = data.avatar_url33        }34    } catch (error) {35        alert(error.message)36    } finally {37        loading.value = false38    }39}4041async function updateProfile() {42    try {43        loading.value = true44        const updates = {45            id: claims.value.sub,46            username: username.value,47            website: website.value,48            avatar_url: avatar_url.value,49            updated_at: new Date(),50        }5152        let { error } = await supabase.from('profiles').upsert(updates)5354        if (error) throw error55    } catch (error) {56        alert(error.message)57    } finally {58        loading.value = false59    }60}6162async function signOut() {63    try {64        loading.value = true65        let { error } = await supabase.auth.signOut()66        if (error) throw error67    } catch (error) {68        alert(error.message)69    } finally {70        loading.value = false71    }72}73</script>7475<template>76    <form class="form-widget" @submit.prevent="updateProfile">77        <Avatar v-model:path="avatar_url" @upload="updateProfile" size="10" />78        <div>79            <label for="email">Email</label>80            <input id="email" type="text" :value="claims.email" disabled />81        </div>82        <div>83            <label for="username">Name</label>84            <input id="username" type="text" v-model="username" />85        </div>86        <div>87            <label for="website">Website</label>88            <input id="website" type="url" v-model="website" />89        </div>9091        <div>92            <input type="submit" class="button primary block" :value="loading ? 'Loading ...' : 'Update'"93                :disabled="loading" />94        </div>9596        <div>97            <button class="button block" @click="signOut" :disabled="loading">98                Sign Out99            </button>100        </div>101    </form>102</template>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/vue3-user-management/src/components/Account.vue)

### Launch![#](#launch)

With all the components in place, update `App.vue`:

###### src/App.vue

```
1<script setup>2import { onMounted, ref } from 'vue'3import Account from './components/Account.vue'4import Auth from './components/Auth.vue'5import { supabase } from './supabase'67const claims = ref()89onMounted(() => {10  supabase.auth.getClaims().then(({ data }) => {11    claims.value = data.claims12  })1314  supabase.auth.onAuthStateChange(async () => {15    const { data } = await supabase.auth.getClaims()16    claims.value = data.claims17  })18})19</script>2021<template>22  <div class="container" style="padding: 50px 0 100px 0">23    <Account v-if="claims" :claims="claims" />24    <Auth v-else />25  </div>26</template>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/vue3-user-management/src/App.vue)

Once that's done, run this in a terminal window:

```
1npm run dev
```

And then open the browser to [localhost:5173](http://localhost:5173) and you should see the completed app.

![Supabase Vue 3](/docs/img/supabase-vue-3-demo.png)

## Bonus: Profile photos[#](#bonus-profile-photos)

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.

### Create an upload widget[#](#create-an-upload-widget)

Create a new `src/components/Avatar.vue` component that allows users to upload profile photos:

###### src/components/Avatar.vue

```
1<script setup>2import { ref, toRefs, watch } from 'vue'3import { supabase } from '../supabase'45const prop = defineProps(['path', 'size'])6const { path, size } = toRefs(prop)78const emit = defineEmits(['upload', 'update:path'])9const uploading = ref(false)10const src = ref('')11const files = ref()1213const downloadImage = async () => {14    try {15        const { data, error } = await supabase.storage16            .from('avatars')17            .download(path.value)18        if (error) throw error19        src.value = URL.createObjectURL(data)20    } catch (error) {21        console.error('Error downloading image: ', error.message)22    }23}2425const uploadAvatar = async (evt) => {26    files.value = evt.target.files27    try {28        uploading.value = true29        if (!files.value || files.value.length === 0) {30            throw new Error('You must select an image to upload.')31        }3233        const file = files.value[0]34        const fileExt = file.name.split('.').pop()35        const filePath = `${Math.random()}.${fileExt}`3637        let { error: uploadError } = await supabase.storage38            .from('avatars')39            .upload(filePath, file)4041        if (uploadError) throw uploadError42        emit('update:path', filePath)43        emit('upload')44    } catch (error) {45        alert(error.message)46    } finally {47        uploading.value = false48    }49}5051watch(path, () => {52    if (path.value) downloadImage()53})54</script>5556<template>57    <div>58        <img v-if="src" :src="src" alt="Avatar" class="avatar image"59            :style="{ height: size + 'em', width: size + 'em' }" />60        <div v-else class="avatar no-image" :style="{ height: size + 'em', width: size + 'em' }" />6162        <div :style="{ width: size + 'em' }">63            <label class="button primary block" for="single">64                {{ uploading ? "Uploading ..." : "Upload" }}65            </label>66            <input style="visibility: hidden; position: absolute" type="file" id="single" accept="image/*"67                @change="uploadAvatar" :disabled="uploading" />68        </div>69    </div>70</template>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/vue3-user-management/src/components/Avatar.vue)

### Add the new widget[#](#add-the-new-widget)

Finally, add the widget to the Account page.

The `Account.vue` component [shown earlier](#account-page) already includes the `Avatar` component.

At this stage you have a fully functional application!

