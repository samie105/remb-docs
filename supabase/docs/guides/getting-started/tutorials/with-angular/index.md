---
title: "Build a User Management App with Angular"
source: "https://supabase.com/docs/guides/getting-started/tutorials/with-angular"
canonical_url: "https://supabase.com/docs/guides/getting-started/tutorials/with-angular"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:42.781Z"
content_hash: "a8d9642a40019d107b2026d706fb706be349c7cc40d39dc46de264e5cc27f833"
menu_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","Angular","Angular"]
section_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","Angular","Angular"]
nav_prev: {"path": "supabase/docs/guides/getting-started/quickstarts/vue/index.md", "title": "Use Supabase with Vue"}
nav_next: {"path": "supabase/docs/guides/getting-started/tutorials/with-expo-react-native/index.md", "title": "Build a User Management App with Expo React Native"}
---

# 

Build a User Management App with Angular

* * *

This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/angular-user-management).

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

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=ionicangular).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=ionicangular), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

## Building the app[#](#building-the-app)

Start with building the Angular app from scratch.

### Initialize an Angular app[#](#initialize-an-angular-app)

You can use the [Angular CLI](https://angular.io/cli) to initialize an app called `supabase-angular`. The command sets some defaults, that you change to suit your needs:

```
1npx ng new supabase-angular --routing false --style css --standalone false --ssr false2cd supabase-angular
```

Then, install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js)

```
1npm install @supabase/supabase-js
```

Finally, save the environment variables in a new `src/environments/environment.ts` file. You need to create the `src/environments` directory first. All you need are the API URL and the key that you copied [earlier](#get-api-details). The application exposes these variables in the browser, and that's fine as you have [Row Level Security](/docs/guides/auth#row-level-security) enabled on the Database.

###### src/environments/environment.ts

```
1export const environment = {2  production: false,3  supabaseUrl: 'YOUR_SUPABASE_URL',4  supabaseKey: 'YOUR_SUPABASE_KEY',5}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/angular-user-management/src/environments/environment.ts)

With the API credentials in place, create a `SupabaseService` with `ng g s supabase` and add the following code to initialize the Supabase client and implement functions to communicate with the Supabase API.

This uses the [`getUser`](/docs/reference/javascript/auth-getuser) method to get the current user details if there is an existing session. This method performs a network request to the Supabase Auth server.

###### src/app/supabase.service.ts

```
1import { Injectable } from '@angular/core'2import { AuthChangeEvent, createClient, Session, SupabaseClient, User } from '@supabase/supabase-js'3import { environment } from '../environments/environment'45export interface Profile {6  id?: string7  username: string8  website: string9  avatar_url: string10}1112@Injectable({13  providedIn: 'root',14})15export class SupabaseService {16  private supabase: SupabaseClient1718  constructor() {19    this.supabase = createClient(environment.supabaseUrl, environment.supabaseKey)20  }2122  async getUser(): Promise<User | null> {23    const { data, error } = await this.supabase.auth.getUser()24    if (error) {25      return null26    }27    return data.user28  }2930  profile(user: User) {31    return this.supabase32      .from('profiles')33      .select(`username, website, avatar_url`)34      .eq('id', user.id)35      .single()36  }3738  authChanges(callback: (event: AuthChangeEvent, session: Session | null) => void) {39    return this.supabase.auth.onAuthStateChange(callback)40  }4142  signIn(email: string) {43    return this.supabase.auth.signInWithOtp({ email })44  }4546  signOut() {47    return this.supabase.auth.signOut()48  }4950  updateProfile(profile: Profile) {51    const update = {52      ...profile,53      updated_at: new Date(),54    }5556    return this.supabase.from('profiles').upsert(update)57  }5859  downLoadImage(path: string) {60    return this.supabase.storage.from('avatars').download(path)61  }6263  uploadAvatar(filePath: string, file: File) {64    return this.supabase.storage.from('avatars').upload(filePath, file)65  }66}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/angular-user-management/src/app/supabase.service.ts)

Optionally, update `src/styles.css` to style the app. You can find the full contents of this file [in the example repository](https://github.com/supabase/supabase/tree/master/examples/user-management/angular-user-management/src/styles.css).

### Set up a login component[#](#set-up-a-login-component)

Next, set up an Angular component to manage logins and sign ups. The component uses [Magic Links](/docs/guides/auth/auth-email-passwordless#with-magic-link), so users can sign in with their email without using passwords.

Create an `AuthComponent` with the `ng g c auth` Angular CLI command and add the following code.

```
1import { Component } from '@angular/core'2import { FormBuilder, FormGroup } from '@angular/forms'3import { SupabaseService } from '../supabase.service'45@Component({6  selector: 'app-auth',7  templateUrl: './auth.component.html',8  styleUrls: ['./auth.component.css'],9  standalone: false,10})11export class AuthComponent {12  loading = false13  signInForm: FormGroup1415  constructor(16    private readonly supabase: SupabaseService,17    private readonly formBuilder: FormBuilder18  ) {19    this.signInForm = this.formBuilder.group({20      email: '',21    })22  }2324  async onSubmit(): Promise<void> {25    try {26      this.loading = true27      const email = this.signInForm.value.email as string28      const { error } = await this.supabase.signIn(email)29      if (error) throw error30      alert('Check your email for the login link!')31    } catch (error) {32      if (error instanceof Error) {33        alert(error.message)34      }35    } finally {36      this.signInForm.reset()37      this.loading = false38    }39  }40}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/angular-user-management/src/app/auth/auth.component.ts)

### Account page[#](#account-page)

Users also need a way to edit their profile details and manage their accounts after signing in. Create an `AccountComponent` with the `ng g c account` Angular CLI command and add the following code.

```
1import { Component, Input, OnInit } from '@angular/core'2import { FormBuilder, FormGroup } from '@angular/forms'3import { User } from '@supabase/supabase-js'4import { Profile, SupabaseService } from '../supabase.service'56@Component({7  selector: 'app-account',8  templateUrl: './account.component.html',9  styleUrls: ['./account.component.css'],10  standalone: false,11})12export class AccountComponent implements OnInit {13  loading = false14  profile!: Profile15  updateProfileForm!: FormGroup1617  get avatarUrl() {18    return this.updateProfileForm.value.avatar_url as string19  }2021  async updateAvatar(event: string): Promise<void> {22    this.updateProfileForm.patchValue({23      avatar_url: event,24    })25    await this.updateProfile()26  }2728  @Input()29  user!: User3031  constructor(32    private readonly supabase: SupabaseService,33    private formBuilder: FormBuilder34  ) {35    this.updateProfileForm = this.formBuilder.group({36      username: '',37      website: '',38      avatar_url: '',39    })40  }4142  async ngOnInit(): Promise<void> {43    await this.getProfile()4445    const { username, website, avatar_url } = this.profile46    this.updateProfileForm.patchValue({47      username,48      website,49      avatar_url,50    })51  }5253  async getProfile() {54    try {55      this.loading = true56      const { data: profile, error, status } = await this.supabase.profile(this.user)5758      if (error && status !== 406) {59        throw error60      }6162      if (profile) {63        this.profile = profile64      }65    } catch (error) {66      if (error instanceof Error) {67        alert(error.message)68      }69    } finally {70      this.loading = false71    }72  }7374  async updateProfile(): Promise<void> {75    try {76      this.loading = true7778      const username = this.updateProfileForm.value.username as string79      const website = this.updateProfileForm.value.website as string80      const avatar_url = this.updateProfileForm.value.avatar_url as string8182      const { error } = await this.supabase.updateProfile({83        id: this.user.id,84        username,85        website,86        avatar_url,87      })88      if (error) throw error89    } catch (error) {90      if (error instanceof Error) {91        alert(error.message)92      }93    } finally {94      this.loading = false95    }96  }9798  async signOut() {99    await this.supabase.signOut()100  }101}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/angular-user-management/src/app/account/account.component.ts)

## Profile photos[#](#profile-photos)

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.

### Create an upload widget[#](#create-an-upload-widget)

Create an avatar for the user so that they can upload a profile photo. Create an `AvatarComponent` with `ng g c avatar` Angular CLI command and add the following code.

```
1import { Component, EventEmitter, Input, Output } from '@angular/core'2import { SafeResourceUrl, DomSanitizer } from '@angular/platform-browser'3import { SupabaseService } from '../supabase.service'45@Component({6  selector: 'app-avatar',7  templateUrl: './avatar.component.html',8  styleUrls: ['./avatar.component.css'],9  standalone: false,10})11export class AvatarComponent {12  _avatarUrl: SafeResourceUrl | undefined13  uploading = false1415  @Input()16  set avatarUrl(url: string | null) {17    if (url) {18      this.downloadImage(url)19    }20  }2122  @Output() upload = new EventEmitter<string>()2324  constructor(25    private readonly supabase: SupabaseService,26    private readonly dom: DomSanitizer27  ) {}2829  async downloadImage(path: string) {30    try {31      const { data } = await this.supabase.downLoadImage(path)32      if (data instanceof Blob) {33        this._avatarUrl = this.dom.bypassSecurityTrustResourceUrl(URL.createObjectURL(data))34      }35    } catch (error) {36      if (error instanceof Error) {37        console.error('Error downloading image: ', error.message)38      }39    }40  }4142  async uploadAvatar(event: any) {43    try {44      this.uploading = true45      if (!event.target.files || event.target.files.length === 0) {46        throw new Error('You must select an image to upload.')47      }4849      const file = event.target.files[0]50      const fileExt = file.name.split('.').pop()51      const filePath = `${Math.random()}.${fileExt}`5253      await this.supabase.uploadAvatar(filePath, file)54      this.upload.emit(filePath)55    } catch (error) {56      if (error instanceof Error) {57        alert(error.message)58      }59    } finally {60      this.uploading = false61    }62  }63}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/angular-user-management/src/app/avatar/avatar.component.ts)

### Launch![#](#launch)

Now you have all the components in place, update `AppComponent`:

```
1import { Component, OnInit } from '@angular/core'2import { User } from '@supabase/supabase-js'3import { SupabaseService } from './supabase.service'45@Component({6  selector: 'app-root',7  templateUrl: './app.component.html',8  styleUrls: ['./app.component.css'],9  standalone: false,10})11export class AppComponent implements OnInit {12  constructor(private readonly supabase: SupabaseService) {}1314  title = 'angular-user-management'15  user: User | null = null1617  async ngOnInit() {18    this.user = await this.supabase.getUser()19    this.supabase.authChanges(async () => {20      this.user = await this.supabase.getUser()21    })22  }23}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/angular-user-management/src/app/app.component.ts)

You also need to change `app.module.ts` to include the `ReactiveFormsModule` from the `@angular/forms` package.

###### src/app/app.module.ts

```
1import { NgModule } from '@angular/core'2import { BrowserModule } from '@angular/platform-browser'3import { ReactiveFormsModule } from '@angular/forms'45import { AppComponent } from './app.component'6import { AuthComponent } from './auth/auth.component'7import { AccountComponent } from './account/account.component'8import { AvatarComponent } from './avatar/avatar.component'910@NgModule({11  declarations: [AppComponent, AuthComponent, AccountComponent, AvatarComponent],12  imports: [BrowserModule, ReactiveFormsModule],13  providers: [],14  bootstrap: [AppComponent],15})16export class AppModule {}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/angular-user-management/src/app/app.module.ts)

Once that's done, run the application in a terminal:

```
1npm run start
```

Open the browser to [localhost:4200](http://localhost:4200) and you should see the completed app.

![Screenshot of the Supabase Angular application running in a browser](/docs/img/supabase-angular-demo.png)

At this stage you have a fully functional application!
