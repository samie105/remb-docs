---
title: "Enable CAPTCHA Protection"
source: "https://supabase.com/docs/guides/auth/auth-captcha"
canonical_url: "https://supabase.com/docs/guides/auth/auth-captcha"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:27.640Z"
content_hash: "ca3fb3aa10d09e60d1b82e80a8c1adac69024527de4ce036c6d542f86a91f7f4"
menu_path: ["Auth","Auth","Security","Security","Bot Detection (CAPTCHA)","Bot Detection (CAPTCHA)"]
section_path: ["Auth","Auth","Security","Security","Bot Detection (CAPTCHA)","Bot Detection (CAPTCHA)"]
nav_prev: {"path": "../auth-anonymous/index.md", "title": "Anonymous Sign-Ins"}
nav_next: {"path": "../auth-email-passwordless/index.md", "title": "Passwordless email logins"}
---

# 

Enable CAPTCHA Protection

* * *

Supabase provides you with the option of adding CAPTCHA to your sign-in, sign-up, and password reset forms. This keeps your website safe from bots and malicious scripts. Supabase authentication has support for [hCaptcha](https://www.hcaptcha.com/) and [Cloudflare Turnstile](https://www.cloudflare.com/application-services/products/turnstile/).

## Sign up for CAPTCHA[#](#sign-up-for-captcha)

Go to the [hCaptcha](https://www.hcaptcha.com/) website and sign up for an account. On the Welcome page, copy the **Sitekey** and **Secret key**.

If you have already signed up and didn't copy this information from the Welcome page, you can get the **Secret key** from the Settings page.

![site\_secret\_settings.png](/docs/img/guides/auth-captcha/site_secret_settings.png)

The **Sitekey** can be found in the **Settings** of the active site you created.

![sites\_dashboard.png](/docs/img/guides/auth-captcha/sites_dashboard.png)

In the Settings page, look for the **Sitekey** section and copy the key.

![sitekey\_settings.png](/docs/img/guides/auth-captcha/sitekey_settings.png)

## Enable CAPTCHA protection for your Supabase project[#](#enable-captcha-protection-for-your-supabase-project)

Navigate to the **[Auth](/dashboard/project/_/auth/protection)** section of your Project Settings in the Supabase Dashboard and find the **Enable CAPTCHA protection** toggle under Settings > Authentication > Bot and Abuse Protection > Enable CAPTCHA protection.

Select your CAPTCHA provider from the dropdown, enter your CAPTCHA **Secret key**, and click **Save**.

## Add the CAPTCHA frontend component[#](#add-the-captcha-frontend-component)

The frontend requires some changes to provide the CAPTCHA on-screen for the user. This example uses React and the corresponding CAPTCHA React component, but both CAPTCHA providers can be used with any JavaScript framework.

Install `@hcaptcha/react-hcaptcha` in your project as a dependency.

```
1npm install @hcaptcha/react-hcaptcha
```

Now import the `HCaptcha` component from the `@hcaptcha/react-hcaptcha` library.

```
1import HCaptcha from '@hcaptcha/react-hcaptcha'
```

Let's create a empty state to store our `captchaToken`

```
1const [captchaToken, setCaptchaToken] = useState()
```

Now lets add the `HCaptcha` component to the JSX section of our code

```
1<HCaptcha />
```

We will pass it the sitekey we copied from the hCaptcha website as a property along with a `onVerify` property which takes a callback function. This callback function will have a token as one of its properties. Let's set the token in the state using `setCaptchaToken`

```
1<HCaptcha2  sitekey="your-sitekey"3  onVerify={(token) => {4    setCaptchaToken(token)5  }}6/>
```

Now lets use the CAPTCHA token we receive in our Supabase signUp function.

```
1await supabase.auth.signUp({2  email,3  password,4  options: { captchaToken },5})
```

We will also need to reset the CAPTCHA challenge after we have made a call to the function above.

Create a ref to use on our `HCaptcha` component.

```
1const captcha = useRef()
```

Let's add a ref attribute on the `HCaptcha` component and assign the `captcha` constant to it.

```
1<HCaptcha2  ref={captcha}3  sitekey="your-sitekey"4  onVerify={(token) => {5    setCaptchaToken(token)6  }}7/>
```

Reset the `captcha` after the signUp function is called using the following code:

```
1captcha.current.resetCaptcha()
```

In order to test that this works locally we will need to use something like [ngrok](https://ngrok.com/) or add an entry to your hosts file. You can read more about this in the [hCaptcha docs](https://docs.hcaptcha.com/#local-development).

Run the application and you should now be provided with a CAPTCHA challenge.
