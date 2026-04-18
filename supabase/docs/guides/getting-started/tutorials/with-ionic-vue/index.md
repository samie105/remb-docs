---
title: "Build a User Management App with Ionic Vue"
source: "https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue"
canonical_url: "https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:57.360Z"
content_hash: "2c32a886e79fd712939584d6859bec2398d82bf3c8d9403805d9fbac4e014d0c"
menu_path: ["Start with Supabase","Start with Supabase","Mobile tutorials","Mobile tutorials","Ionic Vue","Ionic Vue"]
section_path: ["Start with Supabase","Start with Supabase","Mobile tutorials","Mobile tutorials","Ionic Vue","Ionic Vue"]
nav_prev: {"path": "supabase/docs/guides/getting-started/tutorials/with-ionic-angular/index.md", "title": "Build a User Management App with Ionic Angular"}
nav_next: {"path": "supabase/docs/guides/getting-started/tutorials/with-nextjs/index.md", "title": "Build a User Management App with Next.js"}
---

# 

Build a User Management App with Ionic Vue

* * *

This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/ionic-demos/ionic-angular-account.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/ionic-vue-user-management).

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

Start by building the Vue app from scratch.

### Initialize an Ionic Vue app[#](#initialize-an-ionic-vue-app)

Use the [Ionic CLI](https://ionicframework.com/docs/cli) to initialize an app called `supabase-ionic-vue`:

```
1npm install -g @ionic/cli2ionic start supabase-ionic-vue blank --type vue3cd supabase-ionic-vue
```

Install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js)

```
1npm install @supabase/supabase-js
```

Save the environment variables in a `.env` file, including the API URL and key that you copied [earlier](#get-api-details).

```
1VUE_APP_SUPABASE_URL=YOUR_SUPABASE_URL2VUE_APP_SUPABASE_KEY=YOUR_SUPABASE_KEY
```

With the API credentials in place, create a helper file to initialize the Supabase client. These variables will be exposed on the browser, and that's fine since Supabase enables [Row Level Security](/docs/guides/auth#row-level-security) on Databases by default.

###### src/supabase.ts

```
1import { createClient } from '@supabase/supabase-js'23const supabaseUrl = process.env.VUE_APP_SUPABASE_URL4const supabaseKey = process.env.VUE_APP_SUPABASE_KEY56if (!supabaseUrl) {7  throw new Error(8    'Environment variable VUE_APP_SUPABASE_URL is not set. Please define it before starting the application.'9  )10}1112if (!supabaseKey) {13  throw new Error(14    'Environment variable VUE_APP_SUPABASE_KEY is not set. Please define it before starting the application.'15  )16}1718export const supabase = createClient(supabaseUrl, supabaseKey)
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-vue-user-management/src/supabase.ts)

### Set up a login route[#](#set-up-a-login-route)

Create a Vue component to manage logins and sign ups that uses Magic Links, so users can sign in with their email without using passwords.

###### src/views/Login.vue

```
1<template>2  <ion-page>3    <ion-header>4      <ion-toolbar>5        <ion-title>Login</ion-title>6      </ion-toolbar>7    </ion-header>89    <ion-content>10      <div class="ion-padding">11        <h1>Supabase + Ionic Vue</h1>12        <p>Sign in via magic link with your email below</p>13      </div>14      <ion-list inset="true">15        <form @submit.prevent="handleLogin">16          <ion-item>17            <ion-input18              v-model="email"19              label="Email"20              label-placement="stacked"21              name="email"22              autocomplete="email"23              type="email"24            ></ion-input>25          </ion-item>26          <div class="ion-text-center">27            <ion-button type="submit" fill="clear">Login</ion-button>28          </div>29        </form>30      </ion-list>31      <p>{{ email }}</p>32    </ion-content>33  </ion-page>34</template>3536<script setup lang="ts">37import { supabase } from '../supabase';38import {39  IonContent,40  IonHeader,41  IonPage,42  IonTitle,43  IonToolbar,44  IonList,45  IonItem,46  IonInput,47  IonButton,48  toastController,49  loadingController,50} from '@ionic/vue';51import { ref } from 'vue';5253const email = ref('');5455const handleLogin = async () => {56  const loader = await loadingController.create({});57  const toast = await toastController.create({ duration: 5000 });5859  try {60    await loader.present();61    const { error } = await supabase.auth.signInWithOtp({ email: email.value });6263    if (error) throw error;6465    toast.message = 'Check your email for the login link!';66    await toast.present();67  } catch (error: any) {68    toast.message = error.error_description || error.message;69    await toast.present();70  } finally {71    await loader.dismiss();72  }73};74</script>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-vue-user-management/src/views/Login.vue)

### Account page[#](#account-page)

After a user has signed in, let them edit their profile details and manage their account with a new component called `Account.vue`.

###### src/views/Account.vue

```
1<template>2  <ion-page>3    <ion-header>4      <ion-toolbar>5        <ion-title>Account</ion-title>6      </ion-toolbar>7    </ion-header>89    <ion-content>10      <avatar v-model:path="profile.avatar_url" @upload="updateProfile"></avatar>11      <form @submit.prevent="updateProfile">12        <ion-item>13          <ion-label>14            <p>Email</p>15            <p>{{ store.user?.email }}</p>16          </ion-label>17        </ion-item>1819        <ion-item>20          <ion-input21            type="text"22            name="username"23            label="Name"24            label-placement="stacked"25            v-model="profile.username"26          ></ion-input>27        </ion-item>2829        <ion-item>30          <ion-input31            type="url"32            name="website"33            label="Website"34            label-placement="stacked"35            v-model="profile.website"36          ></ion-input>37        </ion-item>38        <div class="ion-text-center">39          <ion-button fill="clear" type="submit">Update Profile</ion-button>40        </div>41      </form>4243      <div class="ion-text-center">44        <ion-button fill="clear" @click="signOut">Log Out</ion-button>45      </div>46    </ion-content>47  </ion-page>48</template>4950<script setup lang="ts">51import { store } from '@/store';52import { supabase } from '@/supabase';53import {54  IonContent,55  IonHeader,56  IonPage,57  IonTitle,58  IonToolbar,59  toastController,60  loadingController,61  IonInput,62  IonItem,63  IonButton,64  IonLabel,65} from '@ionic/vue';66import { onMounted, ref } from 'vue';67import { useRouter } from 'vue-router';68import Avatar from '../components/Avatar.vue';6970const router = useRouter();7172const profile = ref({73  username: '',74  website: '',75  avatar_url: '',76});7778async function getProfile() {79  const loader = await loadingController.create({});80  const toast = await toastController.create({ duration: 5000 });81  await loader.present();82  try {83    const { data: { claims } } = await supabase.auth.getClaims();84    if (!claims) throw new Error('No user logged in');8586    const { data, error, status } = await supabase87      .from('profiles')88      .select(`username, website, avatar_url`)89      .eq('id', claims.sub)90      .single();9192    if (error && status !== 406) throw error;9394    if (data) {95      profile.value = {96        username: data.username,97        website: data.website,98        avatar_url: data.avatar_url,99      };100    }101  } catch (error: any) {102    toast.message = error.message;103    await toast.present();104  } finally {105    await loader.dismiss();106  }107}108109const updateProfile = async () => {110  const loader = await loadingController.create({});111  const toast = await toastController.create({ duration: 5000 });112  try {113    await loader.present();114    const { data: { claims } } = await supabase.auth.getClaims();115    if (!claims) throw new Error('No user logged in');116117    const updates = {118      id: claims.sub,119      ...profile.value,120      updated_at: new Date(),121    };122123    const { error } = await supabase.from('profiles').upsert(updates);124125    if (error) throw error;126  } catch (error: any) {127    toast.message = error.message;128    await toast.present();129  } finally {130    await loader.dismiss();131  }132};133134async function signOut() {135  const loader = await loadingController.create({});136  const toast = await toastController.create({ duration: 5000 });137  await loader.present();138  try {139    const { error } = await supabase.auth.signOut();140    if (error) throw error;141    await router.push('/');142  } catch (error: any) {143    toast.message = error.message;144    await toast.present();145  } finally {146    await loader.dismiss();147  }148}149150onMounted(() => {151  getProfile();152});153</script>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-vue-user-management/src/views/Account.vue)

### Launch![#](#launch)

With all the components in place, update `App.vue` and the app routes:

###### src/router/index.ts

```
1import { createRouter, createWebHistory } from '@ionic/vue-router'2import { RouteRecordRaw } from 'vue-router'3import LoginPage from '../views/Login.vue'4import AccountPage from '../views/Account.vue'5const routes: Array<RouteRecordRaw> = [6  {7    path: '/',8    name: 'Login',9    component: LoginPage,10  },11  {12    path: '/account',13    name: 'Account',14    component: AccountPage,15  },16]1718const router = createRouter({19  history: createWebHistory(process.env.BASE_URL),20  routes,21})2223export default router
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-vue-user-management/src/router/index.ts)

###### src/App.vue

```
1<template>2  <ion-app>3    <ion-router-outlet />4  </ion-app>5</template>67<script setup lang="ts">8import { IonApp, IonRouterOutlet, useIonRouter } from '@ionic/vue';9import { onUnmounted } from 'vue';10import { store } from './store';11import { supabase } from './supabase';1213const router = useIonRouter();1415supabase.auth.getClaims().then(({ data: { claims } }) => {16  store.user = claims;17});1819const {20  data: { subscription },21} = supabase.auth.onAuthStateChange((_event, session) => {22  store.user = session?.user ?? null;23  if (session?.user) {24    router.replace('/account');25  } else {26    router.replace('/');27  }28});2930onUnmounted(() => {31  subscription.unsubscribe();32});33</script>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-vue-user-management/src/App.vue)

Once that's done, run this in a terminal window:

```
1ionic serve
```

And then open the browser to [localhost:8100](http://localhost:8100) and you should see the completed app.

![Supabase Ionic Vue](/docs/img/ionic-demos/ionic-vue.png)

## Bonus: Profile photos[#](#bonus-profile-photos)

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.

### Create an upload widget[#](#create-an-upload-widget)

First install two packages to interact with the user's camera.

```
1npm install @ionic/pwa-elements @capacitor/camera
```

[Capacitor](https://capacitorjs.com) is a cross-platform native runtime from Ionic that enables you to deploy web apps to app stores and provides access to native device API.

Ionic PWA elements is a companion package that polyfills certain browser APIs that provide no user interface with custom Ionic UI.

With those packages installed, update `main.ts` to include an additional bootstrapping call for the Ionic PWA Elements.

###### src/main.ts

```
1import { createApp } from 'vue'2import App from './App.vue'3import router from './router'45import { IonicVue } from '@ionic/vue'6/* Core CSS required for Ionic components to work properly */7import '@ionic/vue/css/ionic.bundle.css'89/* Theme variables */10import './theme/variables.css'1112import { defineCustomElements } from '@ionic/pwa-elements/loader'13defineCustomElements(window)14const app = createApp(App).use(IonicVue).use(router)1516router.isReady().then(() => {17  app.mount('#app')18})
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-vue-user-management/src/main.ts)

Then create an `AvatarComponent`.

###### src/components/Avatar.vue

```
1<template>2  <div class="avatar">3    <div class="avatar_wrapper" @click="uploadAvatar">4      <img v-if="avatarUrl" :src="avatarUrl" />5      <ion-icon v-else :icon="person" class="no-avatar"></ion-icon>6    </div>7  </div>8</template>910<script setup lang="ts">11import { ref, toRef, watch } from 'vue';12import { supabase } from '../supabase';13import { Camera, CameraResultType } from '@capacitor/camera';14import { IonIcon } from '@ionic/vue';15import { person } from 'ionicons/icons';1617const props = defineProps<{ path?: string }>();18const emit = defineEmits<{19  upload: [];20  'update:path': [value: string];21}>();2223const path = toRef(props, 'path');24const avatarUrl = ref('');2526const downloadImage = async () => {27  try {28    const { data, error } = await supabase.storage29      .from('avatars')30      .download(path.value!);31    if (error) throw error;32    avatarUrl.value = URL.createObjectURL(data!);33  } catch (error: any) {34    console.error('Error downloading image: ', error.message);35  }36};3738const uploadAvatar = async () => {39  try {40    const photo = await Camera.getPhoto({41      resultType: CameraResultType.DataUrl,42    });4344    if (photo.dataUrl) {45      const file = await fetch(photo.dataUrl)46        .then((res) => res.blob())47        .then(48          (blob) =>49            new File([blob], 'my-file', { type: `image/${photo.format}` })50        );5152      const fileName = `${Math.random()}-${new Date().getTime()}.${53        photo.format54      }`;55      const { error: uploadError } = await supabase.storage56        .from('avatars')57        .upload(fileName, file);58      if (uploadError) {59        throw uploadError;60      }61      emit('update:path', fileName);62      emit('upload');63    }64  } catch (error) {65    console.log(error);66  }67};6869watch(path, () => {70  if (path.value) downloadImage();71});72</script>7374<style>75.avatar {76  display: block;77  margin: auto;78  min-height: 150px;79}80.avatar .avatar_wrapper {81  margin: 16px auto 16px;82  border-radius: 50%;83  overflow: hidden;84  height: 150px;85  aspect-ratio: 1;86  background: var(--ion-color-step-50);87  border: thick solid var(--ion-color-step-200);88}89.avatar .avatar_wrapper:hover {90  cursor: pointer;91}92.avatar .avatar_wrapper ion-icon.no-avatar {93  width: 100%;94  height: 115%;95}96.avatar img {97  display: block;98  object-fit: cover;99  width: 100%;100  height: 100%;101}102</style>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-vue-user-management/src/components/Avatar.vue)

### Add the new widget[#](#add-the-new-widget)

Add the widget to the Account page (already included in the Account.vue code above since the example includes the Avatar component by default).

At this stage you have a fully functional application!


