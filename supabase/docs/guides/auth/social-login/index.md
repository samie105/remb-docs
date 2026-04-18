---
title: "Social Login"
source: "https://supabase.com/docs/guides/auth/social-login"
canonical_url: "https://supabase.com/docs/guides/auth/social-login"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:26.249Z"
content_hash: "f20f5b763c98a7b8a3bf2665400fa313b816f0af57f405ee967dd7e5dacc6a0e"
menu_path: ["Auth","Auth","More","More","More","Social Login (OAuth)","Social Login (OAuth)","Overview","Overview"]
section_path: ["Auth","Auth","More","More","More","Social Login (OAuth)","Social Login (OAuth)","Overview","Overview"]
nav_prev: {"path": "supabase/docs/guides/auth/signing-keys/index.md", "title": "JWT Signing Keys"}
nav_next: {"path": "supabase/docs/guides/auth/users/index.md", "title": "Users"}
---

# 

Social Login

* * *

Social Login (OAuth) is an open standard for authentication that allows users to log in to one website or application using their credentials from another website or application. OAuth allows users to grant third-party applications access to their online accounts without sharing their passwords. OAuth is commonly used for things like logging in to a social media account from a third-party app. It is a secure and convenient way to authenticate users and share information between applications.

## Benefits[#](#benefits)

There are several reasons why you might want to add social login to your applications:

*   **Improved user experience**: Users can register and log in to your application using their existing social media accounts, which can be faster and more convenient than creating a new account from scratch. This makes it easier for users to access your application, improving their overall experience.
    
*   **Better user engagement**: You can access additional data and insights about your users, such as their interests, demographics, and social connections. This can help you tailor your content and marketing efforts to better engage with your users and provide a more personalized experience.
    
*   **Increased security**: Social login can improve the security of your application by leveraging the security measures and authentication protocols of the social media platforms that your users are logging in with. This can help protect against unauthorized access and account takeovers.
    

## Set up a social provider with Supabase Auth[#](#set-up-a-social-provider-with-supabase-auth)

Supabase supports a suite of social providers. Follow these guides to configure a social provider for your platform.

[

![Google Icon](/docs/img/icons/google-icon.svg)

##### Google

](/docs/guides/auth/social-login/auth-google)[

![Facebook Icon](/docs/img/icons/facebook-icon.svg)

##### Facebook

](/docs/guides/auth/social-login/auth-facebook)[

![Apple Icon](/docs/img/icons/apple-icon.svg)

##### Apple

](/docs/guides/auth/social-login/auth-apple)[

![Azure (Microsoft) Icon](/docs/img/icons/microsoft-icon.svg)

##### Azure (Microsoft)

](/docs/guides/auth/social-login/auth-azure)[

![Twitter Icon](/docs/img/icons/twitter-icon-light.svg)

##### Twitter

](/docs/guides/auth/social-login/auth-twitter)[

![GitHub Icon](/docs/img/icons/github-icon-light.svg)

##### GitHub

](/docs/guides/auth/social-login/auth-github)[

![Gitlab Icon](/docs/img/icons/gitlab-icon.svg)

##### Gitlab

](/docs/guides/auth/social-login/auth-gitlab)[

![Bitbucket Icon](/docs/img/icons/bitbucket-icon.svg)

##### Bitbucket

](/docs/guides/auth/social-login/auth-bitbucket)[

![Discord Icon](/docs/img/icons/discord-icon.svg)

##### Discord

](/docs/guides/auth/social-login/auth-discord)[

![Figma Icon](/docs/img/icons/figma-icon.svg)

##### Figma

](/docs/guides/auth/social-login/auth-figma)[

![Kakao Icon](/docs/img/icons/kakao-icon.svg)

##### Kakao

](/docs/guides/auth/social-login/auth-kakao)[

![Keycloak Icon](/docs/img/icons/keycloak-icon.svg)

##### Keycloak

](/docs/guides/auth/social-login/auth-keycloak)[

![LinkedIn Icon](/docs/img/icons/linkedin-icon.svg)

##### LinkedIn

](/docs/guides/auth/social-login/auth-linkedin)[

![Notion Icon](/docs/img/icons/notion-icon.svg)

##### Notion

](/docs/guides/auth/social-login/auth-notion)[

![Slack Icon](/docs/img/icons/slack-icon.svg)

##### Slack

](/docs/guides/auth/social-login/auth-slack)[

![Spotify Icon](/docs/img/icons/spotify-icon.svg)

##### Spotify

](/docs/guides/auth/social-login/auth-spotify)[

![Twitch Icon](/docs/img/icons/twitch-icon.svg)

##### Twitch

](/docs/guides/auth/social-login/auth-twitch)[

![WorkOS Icon](/docs/img/icons/workos-icon.svg)

##### WorkOS

](/docs/guides/auth/social-login/auth-workos)[

![Zoom Icon](/docs/img/icons/zoom-icon.svg)

##### Zoom

](/docs/guides/auth/social-login/auth-zoom)

Need to integrate with a provider not listed here? You can add any OAuth2 or OIDC-compatible provider using [Custom OAuth/OIDC Providers](/docs/guides/auth/custom-oauth-providers).

## Provider tokens[#](#provider-tokens)

You can use the provider token and provider refresh token returned to make API calls to the OAuth provider. For example, you can use the Google provider token to access Google APIs on behalf of your user.

Supabase Auth does not manage refreshing the provider token for the user. Your application will need to use the provider refresh token to obtain a new provider token. If no provider refresh token is returned, then it could mean one of the following:

*   The OAuth provider does not return a refresh token
*   Additional scopes need to be specified in order for the OAuth provider to return a refresh token.

Provider tokens are intentionally not stored in your project's database. This is because provider tokens give access to potentially sensitive user data in third-party systems. Different applications have different needs, and one application's OAuth scopes may be significantly more permissive than another. If you want to use the provider token outside of the browser that completed the OAuth flow, it is recommended to send it to a trusted and secure server you control.


