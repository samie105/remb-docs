---
title: "Native Mobile Deep Linking"
source: "https://supabase.com/docs/guides/auth/native-mobile-deep-linking"
canonical_url: "https://supabase.com/docs/guides/auth/native-mobile-deep-linking"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:22.897Z"
content_hash: "760dfc4fbbcca5ef802bce332384233664e502271b753c79b6124d0bf22bccf6"
menu_path: ["Auth","Auth","Flows (How-tos)","Flows (How-tos)","Mobile Deep Linking","Mobile Deep Linking"]
section_path: ["Auth","Auth","Flows (How-tos)","Flows (How-tos)","Mobile Deep Linking","Mobile Deep Linking"]
nav_prev: {"path": "supabase/docs/guides/auth/managing-user-data/index.md", "title": "User Management"}
nav_next: {"path": "supabase/docs/guides/auth/oauth-server/index.md", "title": "OAuth 2.1 Server"}
---

# 

Native Mobile Deep Linking

## 

Set up Deep Linking for mobile applications.

* * *

Many Auth methods involve a redirect to your app. For example:

*   Signup confirmation emails, Magic Link signins, and password reset emails contain a link that redirects to your app.
*   In OAuth signins, an automatic redirect occurs to your app.

With Deep Linking, you can configure this redirect to open a specific page. This is necessary if, for example, you need to display a form for [password reset](../passwords/index.md#resetting-a-users-password-forgot-password), or to manually exchange a token hash.

## Setting up deep linking[#](#setting-up-deep-linking)

To link to your development build or standalone app, you need to specify a custom URL scheme for your app. You can register a scheme in your app config (app.json, app.config.js) by adding a string under the `scheme` key:

```
1{2  "expo": {3    "scheme": "com.supabase"4  }5}
```

In your project's [auth settings](/dashboard/project/_/auth/url-configuration) add the redirect URL, e.g. `com.supabase://**`.

Finally, implement the OAuth and linking handlers. See the [supabase-js reference](/docs/reference/javascript/initializing?example=react-native-options-async-storage) for instructions on initializing the supabase-js client in React Native.

```
1import { Button } from "react-native";2import { makeRedirectUri } from "expo-auth-session";3import * as QueryParams from "expo-auth-session/build/QueryParams";4import * as WebBrowser from "expo-web-browser";5import * as Linking from "expo-linking";6import { supabase } from "app/utils/supabase";78WebBrowser.maybeCompleteAuthSession(); // required for web only9const redirectTo = makeRedirectUri();1011const createSessionFromUrl = async (url: string) => {12  const { params, errorCode } = QueryParams.getQueryParams(url);1314  if (errorCode) throw new Error(errorCode);15  const { access_token, refresh_token } = params;1617  if (!access_token) return;1819  const { data, error } = await supabase.auth.setSession({20    access_token,21    refresh_token,22  });23  if (error) throw error;24  return data.session;25};2627const performOAuth = async () => {28  const { data, error } = await supabase.auth.signInWithOAuth({29    provider: "github",30    options: {31      redirectTo,32      skipBrowserRedirect: true,33    },34  });35  if (error) throw error;3637  const res = await WebBrowser.openAuthSessionAsync(38    data?.url ?? "",39    redirectTo40  );4142  if (res.type === "success") {43    const { url } = res;44    await createSessionFromUrl(url);45  }46};4748const sendMagicLink = async () => {49  const { error } = await supabase.auth.signInWithOtp({50    email: "valid.email@supabase.io",51    options: {52      emailRedirectTo: redirectTo,53    },54  });5556  if (error) throw error;57  // Email sent.58};5960export default function Auth() {61  // Handle linking into app from email app.62  const url = Linking.useLinkingURL();63  if (url) createSessionFromUrl(url);6465  return (66    <>67      <Button onPress={performOAuth} title="Sign in with GitHub" />68      <Button onPress={sendMagicLink} title="Send Magic Link" />69    </>70  );71}
```

For the best user experience it is recommended to use universal links which require a more elaborate setup. You can find the detailed setup instructions in the [Expo docs](https://docs.expo.dev/guides/deep-linking/).
