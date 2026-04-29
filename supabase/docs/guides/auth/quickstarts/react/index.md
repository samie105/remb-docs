---
title: "Use Supabase Auth with React"
source: "https://supabase.com/docs/guides/auth/quickstarts/react"
canonical_url: "https://supabase.com/docs/guides/auth/quickstarts/react"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:43.017Z"
content_hash: "7c4956bc5f98e8d07cec7a3f9ce0a013af1bf9c1a674822bd1cafb007f266a05"
menu_path: ["Auth","Auth","Getting Started","Getting Started","React","React"]
section_path: ["Auth","Auth","Getting Started","Getting Started","React","React"]
nav_prev: {"path": "supabase/docs/guides/auth/quickstarts/nextjs/index.md", "title": "Use Supabase Auth with Next.js"}
nav_next: {"path": "supabase/docs/guides/auth/quickstarts/react-native/index.md", "title": "Use Supabase Auth with React Native"}
---

# 

Use Supabase Auth with React

## 

Learn how to use Supabase Auth with React.js.

* * *

1

### Create a new Supabase project

[Launch a new project](/dashboard) in the Supabase Dashboard.

Your new database has a table for storing your users. You can see that this table is currently empty by running some SQL in the [SQL Editor](/dashboard/project/_/sql).

###### SQL\_EDITOR

```
1select * from auth.users;
```

2

### Create a React app

Create a React app using a [Vite](https://vitejs.dev/guide/) template.

###### Terminal

```
1npm create vite@latest my-app -- --template react
```

3

### Install the Supabase client library

Navigate to the React app and install the Supabase libraries.

###### Terminal

```
1cd my-app && npm install @supabase/supabase-js
```

4

### Declare Supabase Environment Variables

Rename `.env.example` to `.env.local` and populate with your Supabase connection variables:

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

###### .env.local

```
1VITE_SUPABASE_URL=your-project-url2VITE_SUPABASE_PUBLISHABLE_KEY=your-publishable-key-or-anon-key
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/auth/quickstarts/react/.env.example)

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=react).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=react).

[Read the API keys docs](../../../api/api-keys/index.md) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=react), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

5

### Set up your login component

##### Explore drop-in UI components for your Supabase app.

UI components built on shadcn/ui that connect to Supabase via a single command.

[Explore Components](https://supabase.com/ui)

In `App.jsx`, create a Supabase client using your Project URL and key.

The code uses the [`getClaims`](/docs/reference/javascript/auth-getclaims) method in `App.jsx` to validate the local JWT before showing the signed-in user.

###### src/App.jsx

```
1import './index.css'2import { useState, useEffect } from 'react'3import { createClient } from '@supabase/supabase-js'45const supabase = createClient(6  import.meta.env.VITE_SUPABASE_URL,7  import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY8)910export default function App() {11  const [loading, setLoading] = useState(false)12  const [email, setEmail] = useState('')13  const [claims, setClaims] = useState(null)1415  // Check URL params on initial render16  const params = new URLSearchParams(window.location.search)17  const hasTokenHash = params.get('token_hash')1819  const [verifying, setVerifying] = useState(!!hasTokenHash)20  const [authError, setAuthError] = useState(null)21  const [authSuccess, setAuthSuccess] = useState(false)2223  useEffect(() => {24    // Check if we have token_hash in URL (magic link callback)25    const params = new URLSearchParams(window.location.search)26    const token_hash = params.get('token_hash')27    const type = params.get('type')2829    if (token_hash) {30      // Verify the OTP token31      supabase.auth32        .verifyOtp({33          token_hash,34          type: type || 'email',35        })36        .then(({ error }) => {37          if (error) {38            setAuthError(error.message)39          } else {40            setAuthSuccess(true)41            // Clear URL params42            window.history.replaceState({}, document.title, '/')43          }44          setVerifying(false)45        })46    }4748    // Check for existing session using getClaims49    supabase.auth.getClaims().then(({ data: { claims } }) => {50      setClaims(claims)51    })5253    // Listen for auth changes54    const {55      data: { subscription },56    } = supabase.auth.onAuthStateChange(() => {57      supabase.auth.getClaims().then(({ data: { claims } }) => {58        setClaims(claims)59      })60    })6162    return () => subscription.unsubscribe()63  }, [])6465  const handleLogin = async (event) => {66    event.preventDefault()67    setLoading(true)68    const { error } = await supabase.auth.signInWithOtp({69      email,70      options: {71        emailRedirectTo: window.location.origin,72      },73    })74    if (error) {75      alert(error.error_description || error.message)76    } else {77      alert('Check your email for the login link!')78    }79    setLoading(false)80  }8182  const handleLogout = async () => {83    await supabase.auth.signOut()84    setClaims(null)85  }8687  // Show verification state88  if (verifying) {89    return (90      <div>91        <h1>Authentication</h1>92        <p>Confirming your magic link...</p>93        <p>Loading...</p>94      </div>95    )96  }9798  // Show auth error99  if (authError) {100    return (101      <div>102        <h1>Authentication</h1>103        <p>✗ Authentication failed</p>104        <p>{authError}</p>105        <button106          onClick={() => {107            setAuthError(null)108            window.history.replaceState({}, document.title, '/')109          }}110        >111          Return to login112        </button>113      </div>114    )115  }116117  // Show auth success (briefly before claims load)118  if (authSuccess && !claims) {119    return (120      <div>121        <h1>Authentication</h1>122        <p>✓ Authentication successful!</p>123        <p>Loading your account...</p>124      </div>125    )126  }127128  // If user is logged in, show welcome screen129  if (claims) {130    return (131      <div>132        <h1>Welcome!</h1>133        <p>You are logged in as: {claims.email}</p>134        <button onClick={handleLogout}>Sign Out</button>135      </div>136    )137  }138139  // Show login form140  return (141    <div>142      <h1>Supabase + React</h1>143      <p>Sign in via magic link with your email below</p>144      <form onSubmit={handleLogin}>145        <input146          type="email"147          placeholder="Your email"148          value={email}149          required={true}150          onChange={(e) => setEmail(e.target.value)}151        />152        <button disabled={loading}>153          {loading ? <span>Loading</span> : <span>Send magic link</span>}154        </button>155      </form>156    </div>157  )158}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/auth/quickstarts/react/src/App.jsx)

6

### Customize email template

Before proceeding, change the email template to support support a server-side authentication flow that sends a token hash:

*   Go to the [Auth templates](/dashboard/project/_/auth/templates) page in your dashboard.
*   Select the Confirm sign up template.
*   Change `{{ .ConfirmationURL }}` to `{{ .SiteURL }}?token_hash={{ .TokenHash }}&type=email`.
*   Change your [Site URL](/dashboard/project/_/auth/url-configuration) to `https://localhost:5173`

7

### Start the app

Start the app, go to [http://localhost:5173](http://localhost:5173) in a browser, and open the browser console and you should be able to register and log in.

###### Terminal

```
1npm run dev
```
