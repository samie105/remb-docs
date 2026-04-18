---
title: "How to implement Incremental Static Regeneration (ISR)"
source: "https://nextjs.org/docs/app/guides/incremental-static-regeneration"
canonical_url: "https://nextjs.org/docs/app/guides/incremental-static-regeneration"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:14:48.370Z"
content_hash: "df96ddb9ac2ae50ad70e84f033169856ca8156c75b226f97f7334875a1af4bc2"
menu_path: ["How to implement Incremental Static Regeneration (ISR)"]
section_path: []
---
Menu

Using App Router

Features available in /app

Latest Version

16.2.4

*   [
    
    Getting Started
    
    ](/docs/app/getting-started)
    
    *   [
        
        Installation
        
        ](/docs/app/getting-started/installation)
    *   [
        
        Project Structure
        
        ](/docs/app/getting-started/project-structure)
    *   [
        
        Layouts and Pages
        
        ](/docs/app/getting-started/layouts-and-pages)
    *   [
        
        Linking and Navigating
        
        ](/docs/app/getting-started/linking-and-navigating)
    *   [
        
        Server and Client Components
        
        ](/docs/app/getting-started/server-and-client-components)
    *   [
        
        Fetching Data
        
        ](/docs/app/getting-started/fetching-data)
    *   [
        
        Mutating Data
        
        ](/docs/app/getting-started/mutating-data)
    *   [
        
        Caching
        
        ](/docs/app/getting-started/caching)
    *   [
        
        Revalidating
        
        ](/docs/app/getting-started/revalidating)
    *   [
        
        Error Handling
        
        ](/docs/app/getting-started/error-handling)
    *   [
        
        CSS
        
        ](/docs/app/getting-started/css)
    *   [
        
        Image Optimization
        
        ](/docs/app/getting-started/images)
    *   [
        
        Font Optimization
        
        ](/docs/app/getting-started/fonts)
    *   [
        
        Metadata and OG images
        
        ](/docs/app/getting-started/metadata-and-og-images)
    *   [
        
        Route Handlers
        
        ](/docs/app/getting-started/route-handlers)
    *   [
        
        Proxy
        
        ](/docs/app/getting-started/proxy)
    *   [
        
        Deploying
        
        ](/docs/app/getting-started/deploying)
    *   [
        
        Upgrading
        
        ](/docs/app/getting-started/upgrading)
    

*   [
    
    Guides
    
    ](/docs/app/guides)
    
    *   [
        
        AI Coding Agents
        
        ](/docs/app/guides/ai-agents)
    *   [
        
        Analytics
        
        ](/docs/app/guides/analytics)
    *   [
        
        Authentication
        
        ](/docs/app/guides/authentication)
    *   [
        
        Backend for Frontend
        
        ](/docs/app/guides/backend-for-frontend)
    *   [
        
        Caching (Previous Model)
        
        ](/docs/app/guides/caching-without-cache-components)
    *   [
        
        CDN Caching
        
        ](/docs/app/guides/cdn-caching)
    *   [
        
        CI Build Caching
        
        ](/docs/app/guides/ci-build-caching)
    *   [
        
        Content Security Policy
        
        ](/docs/app/guides/content-security-policy)
    *   [
        
        CSS-in-JS
        
        ](/docs/app/guides/css-in-js)
    *   [
        
        Custom Server
        
        ](/docs/app/guides/custom-server)
    *   [
        
        Data Security
        
        ](/docs/app/guides/data-security)
    *   [
        
        Debugging
        
        ](/docs/app/guides/debugging)
    *   [
        
        Deploying to Platforms
        
        ](/docs/app/guides/deploying-to-platforms)
    *   [
        
        Draft Mode
        
        ](/docs/app/guides/draft-mode)
    *   [
        
        Environment Variables
        
        ](/docs/app/guides/environment-variables)
    *   [
        
        Forms
        
        ](/docs/app/guides/forms)
    *   [
        
        How Revalidation Works
        
        ](/docs/app/guides/how-revalidation-works)
    *   [
        
        ISR
        
        ](/docs/app/guides/incremental-static-regeneration)
    *   [
        
        Instrumentation
        
        ](/docs/app/guides/instrumentation)
    *   [
        
        Internationalization
        
        ](/docs/app/guides/internationalization)
    *   [
        
        JSON-LD
        
        ](/docs/app/guides/json-ld)
    *   [
        
        Lazy Loading
        
        ](/docs/app/guides/lazy-loading)
    *   [
        
        Development Environment
        
        ](/docs/app/guides/local-development)
    *   [
        
        Next.js MCP Server
        
        ](/docs/app/guides/mcp)
    *   [
        
        MDX
        
        ](/docs/app/guides/mdx)
    *   [
        
        Memory Usage
        
        ](/docs/app/guides/memory-usage)
    *   [
        
        Migrating
        
        ](/docs/app/guides/migrating)
        
        *   [
            
            App Router
            
            ](/docs/app/guides/migrating/app-router-migration)
        *   [
            
            Create React App
            
            ](/docs/app/guides/migrating/from-create-react-app)
        *   [
            
            Vite
            
            ](/docs/app/guides/migrating/from-vite)
        
    *   [
        
        Migrating to Cache Components
        
        ](/docs/app/guides/migrating-to-cache-components)
    *   [
        
        Multi-tenant
        
        ](/docs/app/guides/multi-tenant)
    *   [
        
        Multi-zones
        
        ](/docs/app/guides/multi-zones)
    *   [
        
        OpenTelemetry
        
        ](/docs/app/guides/open-telemetry)
    *   [
        
        Package Bundling
        
        ](/docs/app/guides/package-bundling)
    *   [
        
        PPR Platform Guide
        
        ](/docs/app/guides/ppr-platform-guide)
    *   [
        
        Prefetching
        
        ](/docs/app/guides/prefetching)
    *   [
        
        Preserving UI state
        
        ](/docs/app/guides/preserving-ui-state)
    *   [
        
        Production
        
        ](/docs/app/guides/production-checklist)
    *   [
        
        PWAs
        
        ](/docs/app/guides/progressive-web-apps)
    *   [
        
        Public pages
        
        ](/docs/app/guides/public-static-pages)
    *   [
        
        Redirecting
        
        ](/docs/app/guides/redirecting)
    *   [
        
        Rendering Philosophy
        
        ](/docs/app/guides/rendering-philosophy)
    *   [
        
        Sass
        
        ](/docs/app/guides/sass)
    *   [
        
        Scripts
        
        ](/docs/app/guides/scripts)
    *   [
        
        Self-Hosting
        
        ](/docs/app/guides/self-hosting)
    *   [
        
        SPAs
        
        ](/docs/app/guides/single-page-applications)
    *   [
        
        Static Exports
        
        ](/docs/app/guides/static-exports)
    *   [
        
        Streaming
        
        ](/docs/app/guides/streaming)
    *   [
        
        Tailwind CSS v3
        
        ](/docs/app/guides/tailwind-v3-css)
    *   [
        
        Testing
        
        ](/docs/app/guides/testing)
        
        *   [
            
            Cypress
            
            ](/docs/app/guides/testing/cypress)
        *   [
            
            Jest
            
            ](/docs/app/guides/testing/jest)
        *   [
            
            Playwright
            
            ](/docs/app/guides/testing/playwright)
        *   [
            
            Vitest
            
            ](/docs/app/guides/testing/vitest)
        
    *   [
        
        Third Party Libraries
        
        ](/docs/app/guides/third-party-libraries)
    *   [
        
        Upgrading
        
        ](/docs/app/guides/upgrading)
        
        *   [
            
            Codemods
            
            ](/docs/app/guides/upgrading/codemods)
        *   [
            
            Version 14
            
            ](/docs/app/guides/upgrading/version-14)
        *   [
            
            Version 15
            
            ](/docs/app/guides/upgrading/version-15)
        *   [
            
            Version 16
            
            ](/docs/app/guides/upgrading/version-16)
        
    *   [
        
        Videos
        
        ](/docs/app/guides/videos)
    *   [
        
        View transitions
        
        ](/docs/app/guides/view-transitions)
    

*   [
    
    API Reference
    
    ](/docs/app/api-reference)
    
    *   [
        
        Directives
        
        ](/docs/app/api-reference/directives)
        
        *   [
            
            use cache
            
            ](/docs/app/api-reference/directives/use-cache)
        *   [
            
            use cache: private
            
            ](/docs/app/api-reference/directives/use-cache-private)
        *   [
            
            use cache: remote
            
            ](/docs/app/api-reference/directives/use-cache-remote)
        *   [
            
            use client
            
            ](/docs/app/api-reference/directives/use-client)
        *   [
            
            use server
            
            ](/docs/app/api-reference/directives/use-server)
        
    *   [
        
        Components
        
        ](/docs/app/api-reference/components)
        
        *   [
            
            Font
            
            ](/docs/app/api-reference/components/font)
        *   [
            
            Form Component
            
            ](/docs/app/api-reference/components/form)
        *   [
            
            Image Component
            
            ](/docs/app/api-reference/components/image)
        *   [
            
            Link Component
            
            ](/docs/app/api-reference/components/link)
        *   [
            
            Script Component
            
            ](/docs/app/api-reference/components/script)
        
    *   [
        
        File-system conventions
        
        ](/docs/app/api-reference/file-conventions)
        
        *   [
            
            default.js
            
            ](/docs/app/api-reference/file-conventions/default)
        *   [
            
            Dynamic Segments
            
            ](/docs/app/api-reference/file-conventions/dynamic-routes)
        *   [
            
            error.js
            
            ](/docs/app/api-reference/file-conventions/error)
        *   [
            
            forbidden.js
            
            ](/docs/app/api-reference/file-conventions/forbidden)
        *   [
            
            instrumentation.js
            
            ](/docs/app/api-reference/file-conventions/instrumentation)
        *   [
            
            instrumentation-client.js
            
            ](/docs/app/api-reference/file-conventions/instrumentation-client)
        *   [
            
            Intercepting Routes
            
            ](/docs/app/api-reference/file-conventions/intercepting-routes)
        *   [
            
            layout.js
            
            ](/docs/app/api-reference/file-conventions/layout)
        *   [
            
            loading.js
            
            ](/docs/app/api-reference/file-conventions/loading)
        *   [
            
            mdx-components.js
            
            ](/docs/app/api-reference/file-conventions/mdx-components)
        *   [
            
            not-found.js
            
            ](/docs/app/api-reference/file-conventions/not-found)
        *   [
            
            page.js
            
            ](/docs/app/api-reference/file-conventions/page)
        *   [
            
            Parallel Routes
            
            ](/docs/app/api-reference/file-conventions/parallel-routes)
        *   [
            
            proxy.js
            
            ](/docs/app/api-reference/file-conventions/proxy)
        *   [
            
            public
            
            ](/docs/app/api-reference/file-conventions/public-folder)
        *   [
            
            route.js
            
            ](/docs/app/api-reference/file-conventions/route)
            
            *   [
                
                dynamicParams
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams)
            *   [
                
                maxDuration
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/maxDuration)
            *   [
                
                preferredRegion
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/preferredRegion)
            *   [
                
                runtime
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/runtime)
            
        *   [
            
            Route Groups
            
            ](/docs/app/api-reference/file-conventions/route-groups)
        *   [
            
            src
            
            ](/docs/app/api-reference/file-conventions/src-folder)
        *   [
            
            template.js
            
            ](/docs/app/api-reference/file-conventions/template)
        *   [
            
            unauthorized.js
            
            ](/docs/app/api-reference/file-conventions/unauthorized)
        *   [
            
            Metadata Files
            
            ](/docs/app/api-reference/file-conventions/metadata)
            
            *   [
                
                favicon, icon, and apple-icon
                
                ](/docs/app/api-reference/file-conventions/metadata/app-icons)
            *   [
                
                manifest.json
                
                ](/docs/app/api-reference/file-conventions/metadata/manifest)
            *   [
                
                opengraph-image and twitter-image
                
                ](/docs/app/api-reference/file-conventions/metadata/opengraph-image)
            *   [
                
                robots.txt
                
                ](/docs/app/api-reference/file-conventions/metadata/robots)
            *   [
                
                sitemap.xml
                
                ](/docs/app/api-reference/file-conventions/metadata/sitemap)
            
        *   [
            
            Route Segment Config
            
            ](/docs/app/api-reference/file-conventions/route-segment-config)
            
            *   [
                
                dynamicParams
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams)
            *   [
                
                maxDuration
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/maxDuration)
            *   [
                
                preferredRegion
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/preferredRegion)
            *   [
                
                runtime
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/runtime)
            
        
    *   [
        
        Functions
        
        ](/docs/app/api-reference/functions)
        
        *   [
            
            after
            
            ](/docs/app/api-reference/functions/after)
        *   [
            
            cacheLife
            
            ](/docs/app/api-reference/functions/cacheLife)
        *   [
            
            cacheTag
            
            ](/docs/app/api-reference/functions/cacheTag)
        *   [
            
            unstable\_catchError
            
            ](/docs/app/api-reference/functions/catchError)
        *   [
            
            connection
            
            ](/docs/app/api-reference/functions/connection)
        *   [
            
            cookies
            
            ](/docs/app/api-reference/functions/cookies)
        *   [
            
            draftMode
            
            ](/docs/app/api-reference/functions/draft-mode)
        *   [
            
            fetch
            
            ](/docs/app/api-reference/functions/fetch)
        *   [
            
            forbidden
            
            ](/docs/app/api-reference/functions/forbidden)
        *   [
            
            generateImageMetadata
            
            ](/docs/app/api-reference/functions/generate-image-metadata)
        *   [
            
            generateMetadata
            
            ](/docs/app/api-reference/functions/generate-metadata)
        *   [
            
            generateSitemaps
            
            ](/docs/app/api-reference/functions/generate-sitemaps)
        *   [
            
            generateStaticParams
            
            ](/docs/app/api-reference/functions/generate-static-params)
        *   [
            
            generateViewport
            
            ](/docs/app/api-reference/functions/generate-viewport)
        *   [
            
            headers
            
            ](/docs/app/api-reference/functions/headers)
        *   [
            
            ImageResponse
            
            ](/docs/app/api-reference/functions/image-response)
        *   [
            
            NextRequest
            
            ](/docs/app/api-reference/functions/next-request)
        *   [
            
            NextResponse
            
            ](/docs/app/api-reference/functions/next-response)
        *   [
            
            notFound
            
            ](/docs/app/api-reference/functions/not-found)
        *   [
            
            permanentRedirect
            
            ](/docs/app/api-reference/functions/permanentRedirect)
        *   [
            
            redirect
            
            ](/docs/app/api-reference/functions/redirect)
        *   [
            
            refresh
            
            ](/docs/app/api-reference/functions/refresh)
        *   [
            
            revalidatePath
            
            ](/docs/app/api-reference/functions/revalidatePath)
        *   [
            
            revalidateTag
            
            ](/docs/app/api-reference/functions/revalidateTag)
        *   [
            
            unauthorized
            
            ](/docs/app/api-reference/functions/unauthorized)
        *   [
            
            unstable\_cache
            
            ](/docs/app/api-reference/functions/unstable_cache)
        *   [
            
            unstable\_noStore
            
            ](/docs/app/api-reference/functions/unstable_noStore)
        *   [
            
            unstable\_rethrow
            
            ](/docs/app/api-reference/functions/unstable_rethrow)
        *   [
            
            updateTag
            
            ](/docs/app/api-reference/functions/updateTag)
        *   [
            
            useLinkStatus
            
            ](/docs/app/api-reference/functions/use-link-status)
        *   [
            
            useParams
            
            ](/docs/app/api-reference/functions/use-params)
        *   [
            
            usePathname
            
            ](/docs/app/api-reference/functions/use-pathname)
        *   [
            
            useReportWebVitals
            
            ](/docs/app/api-reference/functions/use-report-web-vitals)
        *   [
            
            useRouter
            
            ](/docs/app/api-reference/functions/use-router)
        *   [
            
            useSearchParams
            
            ](/docs/app/api-reference/functions/use-search-params)
        *   [
            
            useSelectedLayoutSegment
            
            ](/docs/app/api-reference/functions/use-selected-layout-segment)
        *   [
            
            useSelectedLayoutSegments
            
            ](/docs/app/api-reference/functions/use-selected-layout-segments)
        *   [
            
            userAgent
            
            ](/docs/app/api-reference/functions/userAgent)
        
    *   [
        
        Configuration
        
        ](/docs/app/api-reference/config)
        
        *   [
            
            next.config.js
            
            ](/docs/app/api-reference/config/next-config-js)
            
            *   [
                
                adapterPath
                
                ](/docs/app/api-reference/config/next-config-js/adapterPath)
            *   [
                
                allowedDevOrigins
                
                ](/docs/app/api-reference/config/next-config-js/allowedDevOrigins)
            *   [
                
                appDir
                
                ](/docs/app/api-reference/config/next-config-js/appDir)
            *   [
                
                assetPrefix
                
                ](/docs/app/api-reference/config/next-config-js/assetPrefix)
            *   [
                
                authInterrupts
                
                ](/docs/app/api-reference/config/next-config-js/authInterrupts)
            *   [
                
                basePath
                
                ](/docs/app/api-reference/config/next-config-js/basePath)
            *   [
                
                cacheComponents
                
                ](/docs/app/api-reference/config/next-config-js/cacheComponents)
            *   [
                
                cacheHandlers
                
                ](/docs/app/api-reference/config/next-config-js/cacheHandlers)
            *   [
                
                cacheLife
                
                ](/docs/app/api-reference/config/next-config-js/cacheLife)
            *   [
                
                compress
                
                ](/docs/app/api-reference/config/next-config-js/compress)
            *   [
                
                crossOrigin
                
                ](/docs/app/api-reference/config/next-config-js/crossOrigin)
            *   [
                
                cssChunking
                
                ](/docs/app/api-reference/config/next-config-js/cssChunking)
            *   [
                
                deploymentId
                
                ](/docs/app/api-reference/config/next-config-js/deploymentId)
            *   [
                
                devIndicators
                
                ](/docs/app/api-reference/config/next-config-js/devIndicators)
            *   [
                
                distDir
                
                ](/docs/app/api-reference/config/next-config-js/distDir)
            *   [
                
                env
                
                ](/docs/app/api-reference/config/next-config-js/env)
            *   [
                
                expireTime
                
                ](/docs/app/api-reference/config/next-config-js/expireTime)
            *   [
                
                exportPathMap
                
                ](/docs/app/api-reference/config/next-config-js/exportPathMap)
            *   [
                
                generateBuildId
                
                ](/docs/app/api-reference/config/next-config-js/generateBuildId)
            *   [
                
                generateEtags
                
                ](/docs/app/api-reference/config/next-config-js/generateEtags)
            *   [
                
                headers
                
                ](/docs/app/api-reference/config/next-config-js/headers)
            *   [
                
                htmlLimitedBots
                
                ](/docs/app/api-reference/config/next-config-js/htmlLimitedBots)
            *   [
                
                httpAgentOptions
                
                ](/docs/app/api-reference/config/next-config-js/httpAgentOptions)
            *   [
                
                images
                
                ](/docs/app/api-reference/config/next-config-js/images)
            *   [
                
                cacheHandler
                
                ](/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath)
            *   [
                
                inlineCss
                
                ](/docs/app/api-reference/config/next-config-js/inlineCss)
            *   [
                
                logging
                
                ](/docs/app/api-reference/config/next-config-js/logging)
            *   [
                
                mdxRs
                
                ](/docs/app/api-reference/config/next-config-js/mdxRs)
            *   [
                
                onDemandEntries
                
                ](/docs/app/api-reference/config/next-config-js/onDemandEntries)
            *   [
                
                optimizePackageImports
                
                ](/docs/app/api-reference/config/next-config-js/optimizePackageImports)
            *   [
                
                output
                
                ](/docs/app/api-reference/config/next-config-js/output)
            *   [
                
                pageExtensions
                
                ](/docs/app/api-reference/config/next-config-js/pageExtensions)
            *   [
                
                poweredByHeader
                
                ](/docs/app/api-reference/config/next-config-js/poweredByHeader)
            *   [
                
                productionBrowserSourceMaps
                
                ](/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps)
            *   [
                
                proxyClientMaxBodySize
                
                ](/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize)
            *   [
                
                reactCompiler
                
                ](/docs/app/api-reference/config/next-config-js/reactCompiler)
            *   [
                
                reactMaxHeadersLength
                
                ](/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength)
            *   [
                
                reactStrictMode
                
                ](/docs/app/api-reference/config/next-config-js/reactStrictMode)
            *   [
                
                redirects
                
                ](/docs/app/api-reference/config/next-config-js/redirects)
            *   [
                
                rewrites
                
                ](/docs/app/api-reference/config/next-config-js/rewrites)
            *   [
                
                sassOptions
                
                ](/docs/app/api-reference/config/next-config-js/sassOptions)
            *   [
                
                serverActions
                
                ](/docs/app/api-reference/config/next-config-js/serverActions)
            *   [
                
                serverComponentsHmrCache
                
                ](/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache)
            *   [
                
                serverExternalPackages
                
                ](/docs/app/api-reference/config/next-config-js/serverExternalPackages)
            *   [
                
                staleTimes
                
                ](/docs/app/api-reference/config/next-config-js/staleTimes)
            *   [
                
                staticGeneration\*
                
                ](/docs/app/api-reference/config/next-config-js/staticGeneration)
            *   [
                
                taint
                
                ](/docs/app/api-reference/config/next-config-js/taint)
            *   [
                
                trailingSlash
                
                ](/docs/app/api-reference/config/next-config-js/trailingSlash)
            *   [
                
                transpilePackages
                
                ](/docs/app/api-reference/config/next-config-js/transpilePackages)
            *   [
                
                turbopack
                
                ](/docs/app/api-reference/config/next-config-js/turbopack)
            *   [
                
                turbopackFileSystemCache
                
                ](/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache)
            *   [
                
                turbopack.ignoreIssue
                
                ](/docs/app/api-reference/config/next-config-js/turbopackIgnoreIssue)
            *   [
                
                typedRoutes
                
                ](/docs/app/api-reference/config/next-config-js/typedRoutes)
            *   [
                
                typescript
                
                ](/docs/app/api-reference/config/next-config-js/typescript)
            *   [
                
                urlImports
                
                ](/docs/app/api-reference/config/next-config-js/urlImports)
            *   [
                
                useLightningcss
                
                ](/docs/app/api-reference/config/next-config-js/useLightningcss)
            *   [
                
                viewTransition
                
                ](/docs/app/api-reference/config/next-config-js/viewTransition)
            *   [
                
                webpack
                
                ](/docs/app/api-reference/config/next-config-js/webpack)
            *   [
                
                webVitalsAttribution
                
                ](/docs/app/api-reference/config/next-config-js/webVitalsAttribution)
            
        *   [
            
            TypeScript
            
            ](/docs/app/api-reference/config/typescript)
        *   [
            
            ESLint
            
            ](/docs/app/api-reference/config/eslint)
        
    *   [
        
        CLI
        
        ](/docs/app/api-reference/cli)
        
        *   [
            
            create-next-app
            
            ](/docs/app/api-reference/cli/create-next-app)
        *   [
            
            next CLI
            
            ](/docs/app/api-reference/cli/next)
        
    *   [
        
        Adapters
        
        ](/docs/app/api-reference/adapters)
        
        *   [
            
            Configuration
            
            ](/docs/app/api-reference/adapters/configuration)
        *   [
            
            Creating an Adapter
            
            ](/docs/app/api-reference/adapters/creating-an-adapter)
        *   [
            
            API Reference
            
            ](/docs/app/api-reference/adapters/api-reference)
        *   [
            
            Testing Adapters
            
            ](/docs/app/api-reference/adapters/testing-adapters)
        *   [
            
            Routing with @next/routing
            
            ](/docs/app/api-reference/adapters/routing-with-next-routing)
        *   [
            
            Implementing PPR in an Adapter
            
            ](/docs/app/api-reference/adapters/implementing-ppr-in-an-adapter)
        *   [
            
            Runtime Integration
            
            ](/docs/app/api-reference/adapters/runtime-integration)
        *   [
            
            Invoking Entrypoints
            
            ](/docs/app/api-reference/adapters/invoking-entrypoints)
        *   [
            
            Output Types
            
            ](/docs/app/api-reference/adapters/output-types)
        *   [
            
            Routing Information
            
            ](/docs/app/api-reference/adapters/routing-information)
        *   [
            
            Use Cases
            
            ](/docs/app/api-reference/adapters/use-cases)
        
    *   [
        
        Edge Runtime
        
        ](/docs/app/api-reference/edge)
    *   [
        
        Turbopack
        
        ](/docs/app/api-reference/turbopack)
    

*   [
    
    Glossary
    
    ](/docs/app/glossary)

*   [
    
    Getting Started
    
    ](/docs/pages/getting-started)
    
    *   [
        
        Installation
        
        ](/docs/pages/getting-started/installation)
    *   [
        
        Project Structure
        
        ](/docs/pages/getting-started/project-structure)
    *   [
        
        Images
        
        ](/docs/pages/getting-started/images)
    *   [
        
        Fonts
        
        ](/docs/pages/getting-started/fonts)
    *   [
        
        CSS
        
        ](/docs/pages/getting-started/css)
    *   [
        
        Deploying
        
        ](/docs/pages/getting-started/deploying)
    

*   [
    
    Guides
    
    ](/docs/pages/guides)
    
    *   [
        
        Analytics
        
        ](/docs/pages/guides/analytics)
    *   [
        
        Authentication
        
        ](/docs/pages/guides/authentication)
    *   [
        
        Babel
        
        ](/docs/pages/guides/babel)
    *   [
        
        CI Build Caching
        
        ](/docs/pages/guides/ci-build-caching)
    *   [
        
        Content Security Policy
        
        ](/docs/pages/guides/content-security-policy)
    *   [
        
        CSS-in-JS
        
        ](/docs/pages/guides/css-in-js)
    *   [
        
        Custom Server
        
        ](/docs/pages/guides/custom-server)
    *   [
        
        Debugging
        
        ](/docs/pages/guides/debugging)
    *   [
        
        Draft Mode
        
        ](/docs/pages/guides/draft-mode)
    *   [
        
        Environment Variables
        
        ](/docs/pages/guides/environment-variables)
    *   [
        
        Forms
        
        ](/docs/pages/guides/forms)
    *   [
        
        ISR
        
        ](/docs/pages/guides/incremental-static-regeneration)
    *   [
        
        Instrumentation
        
        ](/docs/pages/guides/instrumentation)
    *   [
        
        Internationalization
        
        ](/docs/pages/guides/internationalization)
    *   [
        
        Lazy Loading
        
        ](/docs/pages/guides/lazy-loading)
    *   [
        
        MDX
        
        ](/docs/pages/guides/mdx)
    *   [
        
        Migrating
        
        ](/docs/pages/guides/migrating)
        
        *   [
            
            App Router
            
            ](/docs/pages/guides/migrating/app-router-migration)
        *   [
            
            Create React App
            
            ](/docs/pages/guides/migrating/from-create-react-app)
        *   [
            
            Vite
            
            ](/docs/pages/guides/migrating/from-vite)
        
    *   [
        
        Multi-Zones
        
        ](/docs/pages/guides/multi-zones)
    *   [
        
        OpenTelemetry
        
        ](/docs/pages/guides/open-telemetry)
    *   [
        
        Package Bundling
        
        ](/docs/pages/guides/package-bundling)
    *   [
        
        PostCSS
        
        ](/docs/pages/guides/post-css)
    *   [
        
        Preview Mode
        
        ](/docs/pages/guides/preview-mode)
    *   [
        
        Production
        
        ](/docs/pages/guides/production-checklist)
    *   [
        
        Redirecting
        
        ](/docs/pages/guides/redirecting)
    *   [
        
        Sass
        
        ](/docs/pages/guides/sass)
    *   [
        
        Scripts
        
        ](/docs/pages/guides/scripts)
    *   [
        
        Self-Hosting
        
        ](/docs/pages/guides/self-hosting)
    *   [
        
        Static Exports
        
        ](/docs/pages/guides/static-exports)
    *   [
        
        Tailwind CSS
        
        ](/docs/pages/guides/tailwind-v3-css)
    *   [
        
        Testing
        
        ](/docs/pages/guides/testing)
        
        *   [
            
            Cypress
            
            ](/docs/pages/guides/testing/cypress)
        *   [
            
            Jest
            
            ](/docs/pages/guides/testing/jest)
        *   [
            
            Playwright
            
            ](/docs/pages/guides/testing/playwright)
        *   [
            
            Vitest
            
            ](/docs/pages/guides/testing/vitest)
        
    *   [
        
        Third Party Libraries
        
        ](/docs/pages/guides/third-party-libraries)
    *   [
        
        Upgrading
        
        ](/docs/pages/guides/upgrading)
        
        *   [
            
            Codemods
            
            ](/docs/pages/guides/upgrading/codemods)
        *   [
            
            Version 10
            
            ](/docs/pages/guides/upgrading/version-10)
        *   [
            
            Version 11
            
            ](/docs/pages/guides/upgrading/version-11)
        *   [
            
            Version 12
            
            ](/docs/pages/guides/upgrading/version-12)
        *   [
            
            Version 13
            
            ](/docs/pages/guides/upgrading/version-13)
        *   [
            
            Version 14
            
            ](/docs/pages/guides/upgrading/version-14)
        *   [
            
            Version 9
            
            ](/docs/pages/guides/upgrading/version-9)
        
    

*   [
    
    Building Your Application
    
    ](/docs/pages/building-your-application)
    
    *   [
        
        Routing
        
        ](/docs/pages/building-your-application/routing)
        
        *   [
            
            Pages and Layouts
            
            ](/docs/pages/building-your-application/routing/pages-and-layouts)
        *   [
            
            Dynamic Routes
            
            ](/docs/pages/building-your-application/routing/dynamic-routes)
        *   [
            
            Linking and Navigating
            
            ](/docs/pages/building-your-application/routing/linking-and-navigating)
        *   [
            
            Custom App
            
            ](/docs/pages/building-your-application/routing/custom-app)
        *   [
            
            Custom Document
            
            ](/docs/pages/building-your-application/routing/custom-document)
        *   [
            
            API Routes
            
            ](/docs/pages/building-your-application/routing/api-routes)
        *   [
            
            Custom Errors
            
            ](/docs/pages/building-your-application/routing/custom-error)
        
    *   [
        
        Rendering
        
        ](/docs/pages/building-your-application/rendering)
        
        *   [
            
            Server-side Rendering (SSR)
            
            ](/docs/pages/building-your-application/rendering/server-side-rendering)
        *   [
            
            Static Site Generation (SSG)
            
            ](/docs/pages/building-your-application/rendering/static-site-generation)
        *   [
            
            Automatic Static Optimization
            
            ](/docs/pages/building-your-application/rendering/automatic-static-optimization)
        *   [
            
            Client-side Rendering (CSR)
            
            ](/docs/pages/building-your-application/rendering/client-side-rendering)
        
    *   [
        
        Data Fetching
        
        ](/docs/pages/building-your-application/data-fetching)
        
        *   [
            
            getStaticProps
            
            ](/docs/pages/building-your-application/data-fetching/get-static-props)
        *   [
            
            getStaticPaths
            
            ](/docs/pages/building-your-application/data-fetching/get-static-paths)
        *   [
            
            Forms and Mutations
            
            ](/docs/pages/building-your-application/data-fetching/forms-and-mutations)
        *   [
            
            getServerSideProps
            
            ](/docs/pages/building-your-application/data-fetching/get-server-side-props)
        *   [
            
            Client-side Fetching
            
            ](/docs/pages/building-your-application/data-fetching/client-side)
        
    *   [
        
        Configuring
        
        ](/docs/pages/building-your-application/configuring)
        
        *   [
            
            Error Handling
            
            ](/docs/pages/building-your-application/configuring/error-handling)
        
    

*   [
    
    API Reference
    
    ](/docs/pages/api-reference)
    
    *   [
        
        Components
        
        ](/docs/pages/api-reference/components)
        
        *   [
            
            Font
            
            ](/docs/pages/api-reference/components/font)
        *   [
            
            Form
            
            ](/docs/pages/api-reference/components/form)
        *   [
            
            Head
            
            ](/docs/pages/api-reference/components/head)
        *   [
            
            Image
            
            ](/docs/pages/api-reference/components/image)
        *   [
            
            Image (Legacy)
            
            ](/docs/pages/api-reference/components/image-legacy)
        *   [
            
            Link
            
            ](/docs/pages/api-reference/components/link)
        *   [
            
            Script
            
            ](/docs/pages/api-reference/components/script)
        
    *   [
        
        File-system conventions
        
        ](/docs/pages/api-reference/file-conventions)
        
        *   [
            
            instrumentation.js
            
            ](/docs/pages/api-reference/file-conventions/instrumentation)
        *   [
            
            Proxy
            
            ](/docs/pages/api-reference/file-conventions/proxy)
        *   [
            
            public
            
            ](/docs/pages/api-reference/file-conventions/public-folder)
        *   [
            
            src Directory
            
            ](/docs/pages/api-reference/file-conventions/src-folder)
        
    *   [
        
        Functions
        
        ](/docs/pages/api-reference/functions)
        
        *   [
            
            getInitialProps
            
            ](/docs/pages/api-reference/functions/get-initial-props)
        *   [
            
            getServerSideProps
            
            ](/docs/pages/api-reference/functions/get-server-side-props)
        *   [
            
            getStaticPaths
            
            ](/docs/pages/api-reference/functions/get-static-paths)
        *   [
            
            getStaticProps
            
            ](/docs/pages/api-reference/functions/get-static-props)
        *   [
            
            NextRequest
            
            ](/docs/pages/api-reference/functions/next-request)
        *   [
            
            NextResponse
            
            ](/docs/pages/api-reference/functions/next-response)
        *   [
            
            useParams
            
            ](/docs/pages/api-reference/functions/use-params)
        *   [
            
            useReportWebVitals
            
            ](/docs/pages/api-reference/functions/use-report-web-vitals)
        *   [
            
            useRouter
            
            ](/docs/pages/api-reference/functions/use-router)
        *   [
            
            useSearchParams
            
            ](/docs/pages/api-reference/functions/use-search-params)
        *   [
            
            userAgent
            
            ](/docs/pages/api-reference/functions/userAgent)
        
    *   [
        
        Configuration
        
        ](/docs/pages/api-reference/config)
        
        *   [
            
            next.config.js Options
            
            ](/docs/pages/api-reference/config/next-config-js)
            
            *   [
                
                adapterPath
                
                ](/docs/pages/api-reference/config/next-config-js/adapterPath)
            *   [
                
                allowedDevOrigins
                
                ](/docs/pages/api-reference/config/next-config-js/allowedDevOrigins)
            *   [
                
                assetPrefix
                
                ](/docs/pages/api-reference/config/next-config-js/assetPrefix)
            *   [
                
                basePath
                
                ](/docs/pages/api-reference/config/next-config-js/basePath)
            *   [
                
                bundlePagesRouterDependencies
                
                ](/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies)
            *   [
                
                compress
                
                ](/docs/pages/api-reference/config/next-config-js/compress)
            *   [
                
                crossOrigin
                
                ](/docs/pages/api-reference/config/next-config-js/crossOrigin)
            *   [
                
                deploymentId
                
                ](/docs/pages/api-reference/config/next-config-js/deploymentId)
            *   [
                
                devIndicators
                
                ](/docs/pages/api-reference/config/next-config-js/devIndicators)
            *   [
                
                distDir
                
                ](/docs/pages/api-reference/config/next-config-js/distDir)
            *   [
                
                env
                
                ](/docs/pages/api-reference/config/next-config-js/env)
            *   [
                
                exportPathMap
                
                ](/docs/pages/api-reference/config/next-config-js/exportPathMap)
            *   [
                
                generateBuildId
                
                ](/docs/pages/api-reference/config/next-config-js/generateBuildId)
            *   [
                
                generateEtags
                
                ](/docs/pages/api-reference/config/next-config-js/generateEtags)
            *   [
                
                headers
                
                ](/docs/pages/api-reference/config/next-config-js/headers)
            *   [
                
                httpAgentOptions
                
                ](/docs/pages/api-reference/config/next-config-js/httpAgentOptions)
            *   [
                
                images
                
                ](/docs/pages/api-reference/config/next-config-js/images)
            *   [
                
                logging
                
                ](/docs/pages/api-reference/config/next-config-js/logging)
            *   [
                
                onDemandEntries
                
                ](/docs/pages/api-reference/config/next-config-js/onDemandEntries)
            *   [
                
                optimizePackageImports
                
                ](/docs/pages/api-reference/config/next-config-js/optimizePackageImports)
            *   [
                
                output
                
                ](/docs/pages/api-reference/config/next-config-js/output)
            *   [
                
                pageExtensions
                
                ](/docs/pages/api-reference/config/next-config-js/pageExtensions)
            *   [
                
                poweredByHeader
                
                ](/docs/pages/api-reference/config/next-config-js/poweredByHeader)
            *   [
                
                productionBrowserSourceMaps
                
                ](/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps)
            *   [
                
                experimental.proxyClientMaxBodySize
                
                ](/docs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize)
            *   [
                
                reactStrictMode
                
                ](/docs/pages/api-reference/config/next-config-js/reactStrictMode)
            *   [
                
                redirects
                
                ](/docs/pages/api-reference/config/next-config-js/redirects)
            *   [
                
                rewrites
                
                ](/docs/pages/api-reference/config/next-config-js/rewrites)
            *   [
                
                serverExternalPackages
                
                ](/docs/pages/api-reference/config/next-config-js/serverExternalPackages)
            *   [
                
                trailingSlash
                
                ](/docs/pages/api-reference/config/next-config-js/trailingSlash)
            *   [
                
                transpilePackages
                
                ](/docs/pages/api-reference/config/next-config-js/transpilePackages)
            *   [
                
                turbopack
                
                ](/docs/pages/api-reference/config/next-config-js/turbopack)
            *   [
                
                typescript
                
                ](/docs/pages/api-reference/config/next-config-js/typescript)
            *   [
                
                urlImports
                
                ](/docs/pages/api-reference/config/next-config-js/urlImports)
            *   [
                
                useLightningcss
                
                ](/docs/pages/api-reference/config/next-config-js/useLightningcss)
            *   [
                
                webpack
                
                ](/docs/pages/api-reference/config/next-config-js/webpack)
            *   [
                
                webVitalsAttribution
                
                ](/docs/pages/api-reference/config/next-config-js/webVitalsAttribution)
            
        *   [
            
            TypeScript
            
            ](/docs/pages/api-reference/config/typescript)
        *   [
            
            ESLint
            
            ](/docs/pages/api-reference/config/eslint)
        
    *   [
        
        CLI
        
        ](/docs/pages/api-reference/cli)
        
        *   [
            
            create-next-app CLI
            
            ](/docs/pages/api-reference/cli/create-next-app)
        *   [
            
            next CLI
            
            ](/docs/pages/api-reference/cli/next)
        
    *   [
        
        Adapters
        
        ](/docs/pages/api-reference/adapters)
        
        *   [
            
            Configuration
            
            ](/docs/pages/api-reference/adapters/configuration)
        *   [
            
            Creating an Adapter
            
            ](/docs/pages/api-reference/adapters/creating-an-adapter)
        *   [
            
            API Reference
            
            ](/docs/pages/api-reference/adapters/api-reference)
        *   [
            
            Testing Adapters
            
            ](/docs/pages/api-reference/adapters/testing-adapters)
        *   [
            
            Routing with @next/routing
            
            ](/docs/pages/api-reference/adapters/routing-with-next-routing)
        *   [
            
            Implementing PPR in an Adapter
            
            ](/docs/pages/api-reference/adapters/implementing-ppr-in-an-adapter)
        *   [
            
            Runtime Integration
            
            ](/docs/pages/api-reference/adapters/runtime-integration)
        *   [
            
            Invoking Entrypoints
            
            ](/docs/pages/api-reference/adapters/invoking-entrypoints)
        *   [
            
            Output Types
            
            ](/docs/pages/api-reference/adapters/output-types)
        *   [
            
            Routing Information
            
            ](/docs/pages/api-reference/adapters/routing-information)
        *   [
            
            Use Cases
            
            ](/docs/pages/api-reference/adapters/use-cases)
        
    *   [
        
        Edge Runtime
        
        ](/docs/pages/api-reference/edge)
    *   [
        
        Turbopack
        
        ](/docs/pages/api-reference/turbopack)
    

*   [
    
    Architecture
    
    ](/docs/architecture)
    
    *   [
        
        Accessibility
        
        ](/docs/architecture/accessibility)
    *   [
        
        Fast Refresh
        
        ](/docs/architecture/fast-refresh)
    *   [
        
        Next.js Compiler
        
        ](/docs/architecture/nextjs-compiler)
    *   [
        
        Supported Browsers
        
        ](/docs/architecture/supported-browsers)
    

*   [
    
    Community
    
    ](/docs/community)
    
    *   [
        
        Contribution Guide
        
        ](/docs/community/contribution-guide)
    *   [
        
        Rspack
        
        ](/docs/community/rspack)
    

Using App Router

Features available in /app

Latest Version

16.2.4

*   [
    
    Getting Started
    
    ](/docs/app/getting-started)
    
    *   [
        
        Installation
        
        ](/docs/app/getting-started/installation)
    *   [
        
        Project Structure
        
        ](/docs/app/getting-started/project-structure)
    *   [
        
        Layouts and Pages
        
        ](/docs/app/getting-started/layouts-and-pages)
    *   [
        
        Linking and Navigating
        
        ](/docs/app/getting-started/linking-and-navigating)
    *   [
        
        Server and Client Components
        
        ](/docs/app/getting-started/server-and-client-components)
    *   [
        
        Fetching Data
        
        ](/docs/app/getting-started/fetching-data)
    *   [
        
        Mutating Data
        
        ](/docs/app/getting-started/mutating-data)
    *   [
        
        Caching
        
        ](/docs/app/getting-started/caching)
    *   [
        
        Revalidating
        
        ](/docs/app/getting-started/revalidating)
    *   [
        
        Error Handling
        
        ](/docs/app/getting-started/error-handling)
    *   [
        
        CSS
        
        ](/docs/app/getting-started/css)
    *   [
        
        Image Optimization
        
        ](/docs/app/getting-started/images)
    *   [
        
        Font Optimization
        
        ](/docs/app/getting-started/fonts)
    *   [
        
        Metadata and OG images
        
        ](/docs/app/getting-started/metadata-and-og-images)
    *   [
        
        Route Handlers
        
        ](/docs/app/getting-started/route-handlers)
    *   [
        
        Proxy
        
        ](/docs/app/getting-started/proxy)
    *   [
        
        Deploying
        
        ](/docs/app/getting-started/deploying)
    *   [
        
        Upgrading
        
        ](/docs/app/getting-started/upgrading)
    

*   [
    
    Guides
    
    ](/docs/app/guides)
    
    *   [
        
        AI Coding Agents
        
        ](/docs/app/guides/ai-agents)
    *   [
        
        Analytics
        
        ](/docs/app/guides/analytics)
    *   [
        
        Authentication
        
        ](/docs/app/guides/authentication)
    *   [
        
        Backend for Frontend
        
        ](/docs/app/guides/backend-for-frontend)
    *   [
        
        Caching (Previous Model)
        
        ](/docs/app/guides/caching-without-cache-components)
    *   [
        
        CDN Caching
        
        ](/docs/app/guides/cdn-caching)
    *   [
        
        CI Build Caching
        
        ](/docs/app/guides/ci-build-caching)
    *   [
        
        Content Security Policy
        
        ](/docs/app/guides/content-security-policy)
    *   [
        
        CSS-in-JS
        
        ](/docs/app/guides/css-in-js)
    *   [
        
        Custom Server
        
        ](/docs/app/guides/custom-server)
    *   [
        
        Data Security
        
        ](/docs/app/guides/data-security)
    *   [
        
        Debugging
        
        ](/docs/app/guides/debugging)
    *   [
        
        Deploying to Platforms
        
        ](/docs/app/guides/deploying-to-platforms)
    *   [
        
        Draft Mode
        
        ](/docs/app/guides/draft-mode)
    *   [
        
        Environment Variables
        
        ](/docs/app/guides/environment-variables)
    *   [
        
        Forms
        
        ](/docs/app/guides/forms)
    *   [
        
        How Revalidation Works
        
        ](/docs/app/guides/how-revalidation-works)
    *   [
        
        ISR
        
        ](/docs/app/guides/incremental-static-regeneration)
    *   [
        
        Instrumentation
        
        ](/docs/app/guides/instrumentation)
    *   [
        
        Internationalization
        
        ](/docs/app/guides/internationalization)
    *   [
        
        JSON-LD
        
        ](/docs/app/guides/json-ld)
    *   [
        
        Lazy Loading
        
        ](/docs/app/guides/lazy-loading)
    *   [
        
        Development Environment
        
        ](/docs/app/guides/local-development)
    *   [
        
        Next.js MCP Server
        
        ](/docs/app/guides/mcp)
    *   [
        
        MDX
        
        ](/docs/app/guides/mdx)
    *   [
        
        Memory Usage
        
        ](/docs/app/guides/memory-usage)
    *   [
        
        Migrating
        
        ](/docs/app/guides/migrating)
        
        *   [
            
            App Router
            
            ](/docs/app/guides/migrating/app-router-migration)
        *   [
            
            Create React App
            
            ](/docs/app/guides/migrating/from-create-react-app)
        *   [
            
            Vite
            
            ](/docs/app/guides/migrating/from-vite)
        
    *   [
        
        Migrating to Cache Components
        
        ](/docs/app/guides/migrating-to-cache-components)
    *   [
        
        Multi-tenant
        
        ](/docs/app/guides/multi-tenant)
    *   [
        
        Multi-zones
        
        ](/docs/app/guides/multi-zones)
    *   [
        
        OpenTelemetry
        
        ](/docs/app/guides/open-telemetry)
    *   [
        
        Package Bundling
        
        ](/docs/app/guides/package-bundling)
    *   [
        
        PPR Platform Guide
        
        ](/docs/app/guides/ppr-platform-guide)
    *   [
        
        Prefetching
        
        ](/docs/app/guides/prefetching)
    *   [
        
        Preserving UI state
        
        ](/docs/app/guides/preserving-ui-state)
    *   [
        
        Production
        
        ](/docs/app/guides/production-checklist)
    *   [
        
        PWAs
        
        ](/docs/app/guides/progressive-web-apps)
    *   [
        
        Public pages
        
        ](/docs/app/guides/public-static-pages)
    *   [
        
        Redirecting
        
        ](/docs/app/guides/redirecting)
    *   [
        
        Rendering Philosophy
        
        ](/docs/app/guides/rendering-philosophy)
    *   [
        
        Sass
        
        ](/docs/app/guides/sass)
    *   [
        
        Scripts
        
        ](/docs/app/guides/scripts)
    *   [
        
        Self-Hosting
        
        ](/docs/app/guides/self-hosting)
    *   [
        
        SPAs
        
        ](/docs/app/guides/single-page-applications)
    *   [
        
        Static Exports
        
        ](/docs/app/guides/static-exports)
    *   [
        
        Streaming
        
        ](/docs/app/guides/streaming)
    *   [
        
        Tailwind CSS v3
        
        ](/docs/app/guides/tailwind-v3-css)
    *   [
        
        Testing
        
        ](/docs/app/guides/testing)
        
        *   [
            
            Cypress
            
            ](/docs/app/guides/testing/cypress)
        *   [
            
            Jest
            
            ](/docs/app/guides/testing/jest)
        *   [
            
            Playwright
            
            ](/docs/app/guides/testing/playwright)
        *   [
            
            Vitest
            
            ](/docs/app/guides/testing/vitest)
        
    *   [
        
        Third Party Libraries
        
        ](/docs/app/guides/third-party-libraries)
    *   [
        
        Upgrading
        
        ](/docs/app/guides/upgrading)
        
        *   [
            
            Codemods
            
            ](/docs/app/guides/upgrading/codemods)
        *   [
            
            Version 14
            
            ](/docs/app/guides/upgrading/version-14)
        *   [
            
            Version 15
            
            ](/docs/app/guides/upgrading/version-15)
        *   [
            
            Version 16
            
            ](/docs/app/guides/upgrading/version-16)
        
    *   [
        
        Videos
        
        ](/docs/app/guides/videos)
    *   [
        
        View transitions
        
        ](/docs/app/guides/view-transitions)
    

*   [
    
    API Reference
    
    ](/docs/app/api-reference)
    
    *   [
        
        Directives
        
        ](/docs/app/api-reference/directives)
        
        *   [
            
            use cache
            
            ](/docs/app/api-reference/directives/use-cache)
        *   [
            
            use cache: private
            
            ](/docs/app/api-reference/directives/use-cache-private)
        *   [
            
            use cache: remote
            
            ](/docs/app/api-reference/directives/use-cache-remote)
        *   [
            
            use client
            
            ](/docs/app/api-reference/directives/use-client)
        *   [
            
            use server
            
            ](/docs/app/api-reference/directives/use-server)
        
    *   [
        
        Components
        
        ](/docs/app/api-reference/components)
        
        *   [
            
            Font
            
            ](/docs/app/api-reference/components/font)
        *   [
            
            Form Component
            
            ](/docs/app/api-reference/components/form)
        *   [
            
            Image Component
            
            ](/docs/app/api-reference/components/image)
        *   [
            
            Link Component
            
            ](/docs/app/api-reference/components/link)
        *   [
            
            Script Component
            
            ](/docs/app/api-reference/components/script)
        
    *   [
        
        File-system conventions
        
        ](/docs/app/api-reference/file-conventions)
        
        *   [
            
            default.js
            
            ](/docs/app/api-reference/file-conventions/default)
        *   [
            
            Dynamic Segments
            
            ](/docs/app/api-reference/file-conventions/dynamic-routes)
        *   [
            
            error.js
            
            ](/docs/app/api-reference/file-conventions/error)
        *   [
            
            forbidden.js
            
            ](/docs/app/api-reference/file-conventions/forbidden)
        *   [
            
            instrumentation.js
            
            ](/docs/app/api-reference/file-conventions/instrumentation)
        *   [
            
            instrumentation-client.js
            
            ](/docs/app/api-reference/file-conventions/instrumentation-client)
        *   [
            
            Intercepting Routes
            
            ](/docs/app/api-reference/file-conventions/intercepting-routes)
        *   [
            
            layout.js
            
            ](/docs/app/api-reference/file-conventions/layout)
        *   [
            
            loading.js
            
            ](/docs/app/api-reference/file-conventions/loading)
        *   [
            
            mdx-components.js
            
            ](/docs/app/api-reference/file-conventions/mdx-components)
        *   [
            
            not-found.js
            
            ](/docs/app/api-reference/file-conventions/not-found)
        *   [
            
            page.js
            
            ](/docs/app/api-reference/file-conventions/page)
        *   [
            
            Parallel Routes
            
            ](/docs/app/api-reference/file-conventions/parallel-routes)
        *   [
            
            proxy.js
            
            ](/docs/app/api-reference/file-conventions/proxy)
        *   [
            
            public
            
            ](/docs/app/api-reference/file-conventions/public-folder)
        *   [
            
            route.js
            
            ](/docs/app/api-reference/file-conventions/route)
            
            *   [
                
                dynamicParams
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams)
            *   [
                
                maxDuration
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/maxDuration)
            *   [
                
                preferredRegion
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/preferredRegion)
            *   [
                
                runtime
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/runtime)
            
        *   [
            
            Route Groups
            
            ](/docs/app/api-reference/file-conventions/route-groups)
        *   [
            
            src
            
            ](/docs/app/api-reference/file-conventions/src-folder)
        *   [
            
            template.js
            
            ](/docs/app/api-reference/file-conventions/template)
        *   [
            
            unauthorized.js
            
            ](/docs/app/api-reference/file-conventions/unauthorized)
        *   [
            
            Metadata Files
            
            ](/docs/app/api-reference/file-conventions/metadata)
            
            *   [
                
                favicon, icon, and apple-icon
                
                ](/docs/app/api-reference/file-conventions/metadata/app-icons)
            *   [
                
                manifest.json
                
                ](/docs/app/api-reference/file-conventions/metadata/manifest)
            *   [
                
                opengraph-image and twitter-image
                
                ](/docs/app/api-reference/file-conventions/metadata/opengraph-image)
            *   [
                
                robots.txt
                
                ](/docs/app/api-reference/file-conventions/metadata/robots)
            *   [
                
                sitemap.xml
                
                ](/docs/app/api-reference/file-conventions/metadata/sitemap)
            
        *   [
            
            Route Segment Config
            
            ](/docs/app/api-reference/file-conventions/route-segment-config)
            
            *   [
                
                dynamicParams
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams)
            *   [
                
                maxDuration
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/maxDuration)
            *   [
                
                preferredRegion
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/preferredRegion)
            *   [
                
                runtime
                
                ](/docs/app/api-reference/file-conventions/route-segment-config/runtime)
            
        
    *   [
        
        Functions
        
        ](/docs/app/api-reference/functions)
        
        *   [
            
            after
            
            ](/docs/app/api-reference/functions/after)
        *   [
            
            cacheLife
            
            ](/docs/app/api-reference/functions/cacheLife)
        *   [
            
            cacheTag
            
            ](/docs/app/api-reference/functions/cacheTag)
        *   [
            
            unstable\_catchError
            
            ](/docs/app/api-reference/functions/catchError)
        *   [
            
            connection
            
            ](/docs/app/api-reference/functions/connection)
        *   [
            
            cookies
            
            ](/docs/app/api-reference/functions/cookies)
        *   [
            
            draftMode
            
            ](/docs/app/api-reference/functions/draft-mode)
        *   [
            
            fetch
            
            ](/docs/app/api-reference/functions/fetch)
        *   [
            
            forbidden
            
            ](/docs/app/api-reference/functions/forbidden)
        *   [
            
            generateImageMetadata
            
            ](/docs/app/api-reference/functions/generate-image-metadata)
        *   [
            
            generateMetadata
            
            ](/docs/app/api-reference/functions/generate-metadata)
        *   [
            
            generateSitemaps
            
            ](/docs/app/api-reference/functions/generate-sitemaps)
        *   [
            
            generateStaticParams
            
            ](/docs/app/api-reference/functions/generate-static-params)
        *   [
            
            generateViewport
            
            ](/docs/app/api-reference/functions/generate-viewport)
        *   [
            
            headers
            
            ](/docs/app/api-reference/functions/headers)
        *   [
            
            ImageResponse
            
            ](/docs/app/api-reference/functions/image-response)
        *   [
            
            NextRequest
            
            ](/docs/app/api-reference/functions/next-request)
        *   [
            
            NextResponse
            
            ](/docs/app/api-reference/functions/next-response)
        *   [
            
            notFound
            
            ](/docs/app/api-reference/functions/not-found)
        *   [
            
            permanentRedirect
            
            ](/docs/app/api-reference/functions/permanentRedirect)
        *   [
            
            redirect
            
            ](/docs/app/api-reference/functions/redirect)
        *   [
            
            refresh
            
            ](/docs/app/api-reference/functions/refresh)
        *   [
            
            revalidatePath
            
            ](/docs/app/api-reference/functions/revalidatePath)
        *   [
            
            revalidateTag
            
            ](/docs/app/api-reference/functions/revalidateTag)
        *   [
            
            unauthorized
            
            ](/docs/app/api-reference/functions/unauthorized)
        *   [
            
            unstable\_cache
            
            ](/docs/app/api-reference/functions/unstable_cache)
        *   [
            
            unstable\_noStore
            
            ](/docs/app/api-reference/functions/unstable_noStore)
        *   [
            
            unstable\_rethrow
            
            ](/docs/app/api-reference/functions/unstable_rethrow)
        *   [
            
            updateTag
            
            ](/docs/app/api-reference/functions/updateTag)
        *   [
            
            useLinkStatus
            
            ](/docs/app/api-reference/functions/use-link-status)
        *   [
            
            useParams
            
            ](/docs/app/api-reference/functions/use-params)
        *   [
            
            usePathname
            
            ](/docs/app/api-reference/functions/use-pathname)
        *   [
            
            useReportWebVitals
            
            ](/docs/app/api-reference/functions/use-report-web-vitals)
        *   [
            
            useRouter
            
            ](/docs/app/api-reference/functions/use-router)
        *   [
            
            useSearchParams
            
            ](/docs/app/api-reference/functions/use-search-params)
        *   [
            
            useSelectedLayoutSegment
            
            ](/docs/app/api-reference/functions/use-selected-layout-segment)
        *   [
            
            useSelectedLayoutSegments
            
            ](/docs/app/api-reference/functions/use-selected-layout-segments)
        *   [
            
            userAgent
            
            ](/docs/app/api-reference/functions/userAgent)
        
    *   [
        
        Configuration
        
        ](/docs/app/api-reference/config)
        
        *   [
            
            next.config.js
            
            ](/docs/app/api-reference/config/next-config-js)
            
            *   [
                
                adapterPath
                
                ](/docs/app/api-reference/config/next-config-js/adapterPath)
            *   [
                
                allowedDevOrigins
                
                ](/docs/app/api-reference/config/next-config-js/allowedDevOrigins)
            *   [
                
                appDir
                
                ](/docs/app/api-reference/config/next-config-js/appDir)
            *   [
                
                assetPrefix
                
                ](/docs/app/api-reference/config/next-config-js/assetPrefix)
            *   [
                
                authInterrupts
                
                ](/docs/app/api-reference/config/next-config-js/authInterrupts)
            *   [
                
                basePath
                
                ](/docs/app/api-reference/config/next-config-js/basePath)
            *   [
                
                cacheComponents
                
                ](/docs/app/api-reference/config/next-config-js/cacheComponents)
            *   [
                
                cacheHandlers
                
                ](/docs/app/api-reference/config/next-config-js/cacheHandlers)
            *   [
                
                cacheLife
                
                ](/docs/app/api-reference/config/next-config-js/cacheLife)
            *   [
                
                compress
                
                ](/docs/app/api-reference/config/next-config-js/compress)
            *   [
                
                crossOrigin
                
                ](/docs/app/api-reference/config/next-config-js/crossOrigin)
            *   [
                
                cssChunking
                
                ](/docs/app/api-reference/config/next-config-js/cssChunking)
            *   [
                
                deploymentId
                
                ](/docs/app/api-reference/config/next-config-js/deploymentId)
            *   [
                
                devIndicators
                
                ](/docs/app/api-reference/config/next-config-js/devIndicators)
            *   [
                
                distDir
                
                ](/docs/app/api-reference/config/next-config-js/distDir)
            *   [
                
                env
                
                ](/docs/app/api-reference/config/next-config-js/env)
            *   [
                
                expireTime
                
                ](/docs/app/api-reference/config/next-config-js/expireTime)
            *   [
                
                exportPathMap
                
                ](/docs/app/api-reference/config/next-config-js/exportPathMap)
            *   [
                
                generateBuildId
                
                ](/docs/app/api-reference/config/next-config-js/generateBuildId)
            *   [
                
                generateEtags
                
                ](/docs/app/api-reference/config/next-config-js/generateEtags)
            *   [
                
                headers
                
                ](/docs/app/api-reference/config/next-config-js/headers)
            *   [
                
                htmlLimitedBots
                
                ](/docs/app/api-reference/config/next-config-js/htmlLimitedBots)
            *   [
                
                httpAgentOptions
                
                ](/docs/app/api-reference/config/next-config-js/httpAgentOptions)
            *   [
                
                images
                
                ](/docs/app/api-reference/config/next-config-js/images)
            *   [
                
                cacheHandler
                
                ](/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath)
            *   [
                
                inlineCss
                
                ](/docs/app/api-reference/config/next-config-js/inlineCss)
            *   [
                
                logging
                
                ](/docs/app/api-reference/config/next-config-js/logging)
            *   [
                
                mdxRs
                
                ](/docs/app/api-reference/config/next-config-js/mdxRs)
            *   [
                
                onDemandEntries
                
                ](/docs/app/api-reference/config/next-config-js/onDemandEntries)
            *   [
                
                optimizePackageImports
                
                ](/docs/app/api-reference/config/next-config-js/optimizePackageImports)
            *   [
                
                output
                
                ](/docs/app/api-reference/config/next-config-js/output)
            *   [
                
                pageExtensions
                
                ](/docs/app/api-reference/config/next-config-js/pageExtensions)
            *   [
                
                poweredByHeader
                
                ](/docs/app/api-reference/config/next-config-js/poweredByHeader)
            *   [
                
                productionBrowserSourceMaps
                
                ](/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps)
            *   [
                
                proxyClientMaxBodySize
                
                ](/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize)
            *   [
                
                reactCompiler
                
                ](/docs/app/api-reference/config/next-config-js/reactCompiler)
            *   [
                
                reactMaxHeadersLength
                
                ](/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength)
            *   [
                
                reactStrictMode
                
                ](/docs/app/api-reference/config/next-config-js/reactStrictMode)
            *   [
                
                redirects
                
                ](/docs/app/api-reference/config/next-config-js/redirects)
            *   [
                
                rewrites
                
                ](/docs/app/api-reference/config/next-config-js/rewrites)
            *   [
                
                sassOptions
                
                ](/docs/app/api-reference/config/next-config-js/sassOptions)
            *   [
                
                serverActions
                
                ](/docs/app/api-reference/config/next-config-js/serverActions)
            *   [
                
                serverComponentsHmrCache
                
                ](/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache)
            *   [
                
                serverExternalPackages
                
                ](/docs/app/api-reference/config/next-config-js/serverExternalPackages)
            *   [
                
                staleTimes
                
                ](/docs/app/api-reference/config/next-config-js/staleTimes)
            *   [
                
                staticGeneration\*
                
                ](/docs/app/api-reference/config/next-config-js/staticGeneration)
            *   [
                
                taint
                
                ](/docs/app/api-reference/config/next-config-js/taint)
            *   [
                
                trailingSlash
                
                ](/docs/app/api-reference/config/next-config-js/trailingSlash)
            *   [
                
                transpilePackages
                
                ](/docs/app/api-reference/config/next-config-js/transpilePackages)
            *   [
                
                turbopack
                
                ](/docs/app/api-reference/config/next-config-js/turbopack)
            *   [
                
                turbopackFileSystemCache
                
                ](/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache)
            *   [
                
                turbopack.ignoreIssue
                
                ](/docs/app/api-reference/config/next-config-js/turbopackIgnoreIssue)
            *   [
                
                typedRoutes
                
                ](/docs/app/api-reference/config/next-config-js/typedRoutes)
            *   [
                
                typescript
                
                ](/docs/app/api-reference/config/next-config-js/typescript)
            *   [
                
                urlImports
                
                ](/docs/app/api-reference/config/next-config-js/urlImports)
            *   [
                
                useLightningcss
                
                ](/docs/app/api-reference/config/next-config-js/useLightningcss)
            *   [
                
                viewTransition
                
                ](/docs/app/api-reference/config/next-config-js/viewTransition)
            *   [
                
                webpack
                
                ](/docs/app/api-reference/config/next-config-js/webpack)
            *   [
                
                webVitalsAttribution
                
                ](/docs/app/api-reference/config/next-config-js/webVitalsAttribution)
            
        *   [
            
            TypeScript
            
            ](/docs/app/api-reference/config/typescript)
        *   [
            
            ESLint
            
            ](/docs/app/api-reference/config/eslint)
        
    *   [
        
        CLI
        
        ](/docs/app/api-reference/cli)
        
        *   [
            
            create-next-app
            
            ](/docs/app/api-reference/cli/create-next-app)
        *   [
            
            next CLI
            
            ](/docs/app/api-reference/cli/next)
        
    *   [
        
        Adapters
        
        ](/docs/app/api-reference/adapters)
        
        *   [
            
            Configuration
            
            ](/docs/app/api-reference/adapters/configuration)
        *   [
            
            Creating an Adapter
            
            ](/docs/app/api-reference/adapters/creating-an-adapter)
        *   [
            
            API Reference
            
            ](/docs/app/api-reference/adapters/api-reference)
        *   [
            
            Testing Adapters
            
            ](/docs/app/api-reference/adapters/testing-adapters)
        *   [
            
            Routing with @next/routing
            
            ](/docs/app/api-reference/adapters/routing-with-next-routing)
        *   [
            
            Implementing PPR in an Adapter
            
            ](/docs/app/api-reference/adapters/implementing-ppr-in-an-adapter)
        *   [
            
            Runtime Integration
            
            ](/docs/app/api-reference/adapters/runtime-integration)
        *   [
            
            Invoking Entrypoints
            
            ](/docs/app/api-reference/adapters/invoking-entrypoints)
        *   [
            
            Output Types
            
            ](/docs/app/api-reference/adapters/output-types)
        *   [
            
            Routing Information
            
            ](/docs/app/api-reference/adapters/routing-information)
        *   [
            
            Use Cases
            
            ](/docs/app/api-reference/adapters/use-cases)
        
    *   [
        
        Edge Runtime
        
        ](/docs/app/api-reference/edge)
    *   [
        
        Turbopack
        
        ](/docs/app/api-reference/turbopack)
    

*   [
    
    Glossary
    
    ](/docs/app/glossary)

*   [
    
    Getting Started
    
    ](/docs/pages/getting-started)
    
    *   [
        
        Installation
        
        ](/docs/pages/getting-started/installation)
    *   [
        
        Project Structure
        
        ](/docs/pages/getting-started/project-structure)
    *   [
        
        Images
        
        ](/docs/pages/getting-started/images)
    *   [
        
        Fonts
        
        ](/docs/pages/getting-started/fonts)
    *   [
        
        CSS
        
        ](/docs/pages/getting-started/css)
    *   [
        
        Deploying
        
        ](/docs/pages/getting-started/deploying)
    

*   [
    
    Guides
    
    ](/docs/pages/guides)
    
    *   [
        
        Analytics
        
        ](/docs/pages/guides/analytics)
    *   [
        
        Authentication
        
        ](/docs/pages/guides/authentication)
    *   [
        
        Babel
        
        ](/docs/pages/guides/babel)
    *   [
        
        CI Build Caching
        
        ](/docs/pages/guides/ci-build-caching)
    *   [
        
        Content Security Policy
        
        ](/docs/pages/guides/content-security-policy)
    *   [
        
        CSS-in-JS
        
        ](/docs/pages/guides/css-in-js)
    *   [
        
        Custom Server
        
        ](/docs/pages/guides/custom-server)
    *   [
        
        Debugging
        
        ](/docs/pages/guides/debugging)
    *   [
        
        Draft Mode
        
        ](/docs/pages/guides/draft-mode)
    *   [
        
        Environment Variables
        
        ](/docs/pages/guides/environment-variables)
    *   [
        
        Forms
        
        ](/docs/pages/guides/forms)
    *   [
        
        ISR
        
        ](/docs/pages/guides/incremental-static-regeneration)
    *   [
        
        Instrumentation
        
        ](/docs/pages/guides/instrumentation)
    *   [
        
        Internationalization
        
        ](/docs/pages/guides/internationalization)
    *   [
        
        Lazy Loading
        
        ](/docs/pages/guides/lazy-loading)
    *   [
        
        MDX
        
        ](/docs/pages/guides/mdx)
    *   [
        
        Migrating
        
        ](/docs/pages/guides/migrating)
        
        *   [
            
            App Router
            
            ](/docs/pages/guides/migrating/app-router-migration)
        *   [
            
            Create React App
            
            ](/docs/pages/guides/migrating/from-create-react-app)
        *   [
            
            Vite
            
            ](/docs/pages/guides/migrating/from-vite)
        
    *   [
        
        Multi-Zones
        
        ](/docs/pages/guides/multi-zones)
    *   [
        
        OpenTelemetry
        
        ](/docs/pages/guides/open-telemetry)
    *   [
        
        Package Bundling
        
        ](/docs/pages/guides/package-bundling)
    *   [
        
        PostCSS
        
        ](/docs/pages/guides/post-css)
    *   [
        
        Preview Mode
        
        ](/docs/pages/guides/preview-mode)
    *   [
        
        Production
        
        ](/docs/pages/guides/production-checklist)
    *   [
        
        Redirecting
        
        ](/docs/pages/guides/redirecting)
    *   [
        
        Sass
        
        ](/docs/pages/guides/sass)
    *   [
        
        Scripts
        
        ](/docs/pages/guides/scripts)
    *   [
        
        Self-Hosting
        
        ](/docs/pages/guides/self-hosting)
    *   [
        
        Static Exports
        
        ](/docs/pages/guides/static-exports)
    *   [
        
        Tailwind CSS
        
        ](/docs/pages/guides/tailwind-v3-css)
    *   [
        
        Testing
        
        ](/docs/pages/guides/testing)
        
        *   [
            
            Cypress
            
            ](/docs/pages/guides/testing/cypress)
        *   [
            
            Jest
            
            ](/docs/pages/guides/testing/jest)
        *   [
            
            Playwright
            
            ](/docs/pages/guides/testing/playwright)
        *   [
            
            Vitest
            
            ](/docs/pages/guides/testing/vitest)
        
    *   [
        
        Third Party Libraries
        
        ](/docs/pages/guides/third-party-libraries)
    *   [
        
        Upgrading
        
        ](/docs/pages/guides/upgrading)
        
        *   [
            
            Codemods
            
            ](/docs/pages/guides/upgrading/codemods)
        *   [
            
            Version 10
            
            ](/docs/pages/guides/upgrading/version-10)
        *   [
            
            Version 11
            
            ](/docs/pages/guides/upgrading/version-11)
        *   [
            
            Version 12
            
            ](/docs/pages/guides/upgrading/version-12)
        *   [
            
            Version 13
            
            ](/docs/pages/guides/upgrading/version-13)
        *   [
            
            Version 14
            
            ](/docs/pages/guides/upgrading/version-14)
        *   [
            
            Version 9
            
            ](/docs/pages/guides/upgrading/version-9)
        
    

*   [
    
    Building Your Application
    
    ](/docs/pages/building-your-application)
    
    *   [
        
        Routing
        
        ](/docs/pages/building-your-application/routing)
        
        *   [
            
            Pages and Layouts
            
            ](/docs/pages/building-your-application/routing/pages-and-layouts)
        *   [
            
            Dynamic Routes
            
            ](/docs/pages/building-your-application/routing/dynamic-routes)
        *   [
            
            Linking and Navigating
            
            ](/docs/pages/building-your-application/routing/linking-and-navigating)
        *   [
            
            Custom App
            
            ](/docs/pages/building-your-application/routing/custom-app)
        *   [
            
            Custom Document
            
            ](/docs/pages/building-your-application/routing/custom-document)
        *   [
            
            API Routes
            
            ](/docs/pages/building-your-application/routing/api-routes)
        *   [
            
            Custom Errors
            
            ](/docs/pages/building-your-application/routing/custom-error)
        
    *   [
        
        Rendering
        
        ](/docs/pages/building-your-application/rendering)
        
        *   [
            
            Server-side Rendering (SSR)
            
            ](/docs/pages/building-your-application/rendering/server-side-rendering)
        *   [
            
            Static Site Generation (SSG)
            
            ](/docs/pages/building-your-application/rendering/static-site-generation)
        *   [
            
            Automatic Static Optimization
            
            ](/docs/pages/building-your-application/rendering/automatic-static-optimization)
        *   [
            
            Client-side Rendering (CSR)
            
            ](/docs/pages/building-your-application/rendering/client-side-rendering)
        
    *   [
        
        Data Fetching
        
        ](/docs/pages/building-your-application/data-fetching)
        
        *   [
            
            getStaticProps
            
            ](/docs/pages/building-your-application/data-fetching/get-static-props)
        *   [
            
            getStaticPaths
            
            ](/docs/pages/building-your-application/data-fetching/get-static-paths)
        *   [
            
            Forms and Mutations
            
            ](/docs/pages/building-your-application/data-fetching/forms-and-mutations)
        *   [
            
            getServerSideProps
            
            ](/docs/pages/building-your-application/data-fetching/get-server-side-props)
        *   [
            
            Client-side Fetching
            
            ](/docs/pages/building-your-application/data-fetching/client-side)
        
    *   [
        
        Configuring
        
        ](/docs/pages/building-your-application/configuring)
        
        *   [
            
            Error Handling
            
            ](/docs/pages/building-your-application/configuring/error-handling)
        
    

*   [
    
    API Reference
    
    ](/docs/pages/api-reference)
    
    *   [
        
        Components
        
        ](/docs/pages/api-reference/components)
        
        *   [
            
            Font
            
            ](/docs/pages/api-reference/components/font)
        *   [
            
            Form
            
            ](/docs/pages/api-reference/components/form)
        *   [
            
            Head
            
            ](/docs/pages/api-reference/components/head)
        *   [
            
            Image
            
            ](/docs/pages/api-reference/components/image)
        *   [
            
            Image (Legacy)
            
            ](/docs/pages/api-reference/components/image-legacy)
        *   [
            
            Link
            
            ](/docs/pages/api-reference/components/link)
        *   [
            
            Script
            
            ](/docs/pages/api-reference/components/script)
        
    *   [
        
        File-system conventions
        
        ](/docs/pages/api-reference/file-conventions)
        
        *   [
            
            instrumentation.js
            
            ](/docs/pages/api-reference/file-conventions/instrumentation)
        *   [
            
            Proxy
            
            ](/docs/pages/api-reference/file-conventions/proxy)
        *   [
            
            public
            
            ](/docs/pages/api-reference/file-conventions/public-folder)
        *   [
            
            src Directory
            
            ](/docs/pages/api-reference/file-conventions/src-folder)
        
    *   [
        
        Functions
        
        ](/docs/pages/api-reference/functions)
        
        *   [
            
            getInitialProps
            
            ](/docs/pages/api-reference/functions/get-initial-props)
        *   [
            
            getServerSideProps
            
            ](/docs/pages/api-reference/functions/get-server-side-props)
        *   [
            
            getStaticPaths
            
            ](/docs/pages/api-reference/functions/get-static-paths)
        *   [
            
            getStaticProps
            
            ](/docs/pages/api-reference/functions/get-static-props)
        *   [
            
            NextRequest
            
            ](/docs/pages/api-reference/functions/next-request)
        *   [
            
            NextResponse
            
            ](/docs/pages/api-reference/functions/next-response)
        *   [
            
            useParams
            
            ](/docs/pages/api-reference/functions/use-params)
        *   [
            
            useReportWebVitals
            
            ](/docs/pages/api-reference/functions/use-report-web-vitals)
        *   [
            
            useRouter
            
            ](/docs/pages/api-reference/functions/use-router)
        *   [
            
            useSearchParams
            
            ](/docs/pages/api-reference/functions/use-search-params)
        *   [
            
            userAgent
            
            ](/docs/pages/api-reference/functions/userAgent)
        
    *   [
        
        Configuration
        
        ](/docs/pages/api-reference/config)
        
        *   [
            
            next.config.js Options
            
            ](/docs/pages/api-reference/config/next-config-js)
            
            *   [
                
                adapterPath
                
                ](/docs/pages/api-reference/config/next-config-js/adapterPath)
            *   [
                
                allowedDevOrigins
                
                ](/docs/pages/api-reference/config/next-config-js/allowedDevOrigins)
            *   [
                
                assetPrefix
                
                ](/docs/pages/api-reference/config/next-config-js/assetPrefix)
            *   [
                
                basePath
                
                ](/docs/pages/api-reference/config/next-config-js/basePath)
            *   [
                
                bundlePagesRouterDependencies
                
                ](/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies)
            *   [
                
                compress
                
                ](/docs/pages/api-reference/config/next-config-js/compress)
            *   [
                
                crossOrigin
                
                ](/docs/pages/api-reference/config/next-config-js/crossOrigin)
            *   [
                
                deploymentId
                
                ](/docs/pages/api-reference/config/next-config-js/deploymentId)
            *   [
                
                devIndicators
                
                ](/docs/pages/api-reference/config/next-config-js/devIndicators)
            *   [
                
                distDir
                
                ](/docs/pages/api-reference/config/next-config-js/distDir)
            *   [
                
                env
                
                ](/docs/pages/api-reference/config/next-config-js/env)
            *   [
                
                exportPathMap
                
                ](/docs/pages/api-reference/config/next-config-js/exportPathMap)
            *   [
                
                generateBuildId
                
                ](/docs/pages/api-reference/config/next-config-js/generateBuildId)
            *   [
                
                generateEtags
                
                ](/docs/pages/api-reference/config/next-config-js/generateEtags)
            *   [
                
                headers
                
                ](/docs/pages/api-reference/config/next-config-js/headers)
            *   [
                
                httpAgentOptions
                
                ](/docs/pages/api-reference/config/next-config-js/httpAgentOptions)
            *   [
                
                images
                
                ](/docs/pages/api-reference/config/next-config-js/images)
            *   [
                
                logging
                
                ](/docs/pages/api-reference/config/next-config-js/logging)
            *   [
                
                onDemandEntries
                
                ](/docs/pages/api-reference/config/next-config-js/onDemandEntries)
            *   [
                
                optimizePackageImports
                
                ](/docs/pages/api-reference/config/next-config-js/optimizePackageImports)
            *   [
                
                output
                
                ](/docs/pages/api-reference/config/next-config-js/output)
            *   [
                
                pageExtensions
                
                ](/docs/pages/api-reference/config/next-config-js/pageExtensions)
            *   [
                
                poweredByHeader
                
                ](/docs/pages/api-reference/config/next-config-js/poweredByHeader)
            *   [
                
                productionBrowserSourceMaps
                
                ](/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps)
            *   [
                
                experimental.proxyClientMaxBodySize
                
                ](/docs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize)
            *   [
                
                reactStrictMode
                
                ](/docs/pages/api-reference/config/next-config-js/reactStrictMode)
            *   [
                
                redirects
                
                ](/docs/pages/api-reference/config/next-config-js/redirects)
            *   [
                
                rewrites
                
                ](/docs/pages/api-reference/config/next-config-js/rewrites)
            *   [
                
                serverExternalPackages
                
                ](/docs/pages/api-reference/config/next-config-js/serverExternalPackages)
            *   [
                
                trailingSlash
                
                ](/docs/pages/api-reference/config/next-config-js/trailingSlash)
            *   [
                
                transpilePackages
                
                ](/docs/pages/api-reference/config/next-config-js/transpilePackages)
            *   [
                
                turbopack
                
                ](/docs/pages/api-reference/config/next-config-js/turbopack)
            *   [
                
                typescript
                
                ](/docs/pages/api-reference/config/next-config-js/typescript)
            *   [
                
                urlImports
                
                ](/docs/pages/api-reference/config/next-config-js/urlImports)
            *   [
                
                useLightningcss
                
                ](/docs/pages/api-reference/config/next-config-js/useLightningcss)
            *   [
                
                webpack
                
                ](/docs/pages/api-reference/config/next-config-js/webpack)
            *   [
                
                webVitalsAttribution
                
                ](/docs/pages/api-reference/config/next-config-js/webVitalsAttribution)
            
        *   [
            
            TypeScript
            
            ](/docs/pages/api-reference/config/typescript)
        *   [
            
            ESLint
            
            ](/docs/pages/api-reference/config/eslint)
        
    *   [
        
        CLI
        
        ](/docs/pages/api-reference/cli)
        
        *   [
            
            create-next-app CLI
            
            ](/docs/pages/api-reference/cli/create-next-app)
        *   [
            
            next CLI
            
            ](/docs/pages/api-reference/cli/next)
        
    *   [
        
        Adapters
        
        ](/docs/pages/api-reference/adapters)
        
        *   [
            
            Configuration
            
            ](/docs/pages/api-reference/adapters/configuration)
        *   [
            
            Creating an Adapter
            
            ](/docs/pages/api-reference/adapters/creating-an-adapter)
        *   [
            
            API Reference
            
            ](/docs/pages/api-reference/adapters/api-reference)
        *   [
            
            Testing Adapters
            
            ](/docs/pages/api-reference/adapters/testing-adapters)
        *   [
            
            Routing with @next/routing
            
            ](/docs/pages/api-reference/adapters/routing-with-next-routing)
        *   [
            
            Implementing PPR in an Adapter
            
            ](/docs/pages/api-reference/adapters/implementing-ppr-in-an-adapter)
        *   [
            
            Runtime Integration
            
            ](/docs/pages/api-reference/adapters/runtime-integration)
        *   [
            
            Invoking Entrypoints
            
            ](/docs/pages/api-reference/adapters/invoking-entrypoints)
        *   [
            
            Output Types
            
            ](/docs/pages/api-reference/adapters/output-types)
        *   [
            
            Routing Information
            
            ](/docs/pages/api-reference/adapters/routing-information)
        *   [
            
            Use Cases
            
            ](/docs/pages/api-reference/adapters/use-cases)
        
    *   [
        
        Edge Runtime
        
        ](/docs/pages/api-reference/edge)
    *   [
        
        Turbopack
        
        ](/docs/pages/api-reference/turbopack)
    

*   [
    
    Architecture
    
    ](/docs/architecture)
    
    *   [
        
        Accessibility
        
        ](/docs/architecture/accessibility)
    *   [
        
        Fast Refresh
        
        ](/docs/architecture/fast-refresh)
    *   [
        
        Next.js Compiler
        
        ](/docs/architecture/nextjs-compiler)
    *   [
        
        Supported Browsers
        
        ](/docs/architecture/supported-browsers)
    

*   [
    
    Community
    
    ](/docs/community)
    
    *   [
        
        Contribution Guide
        
        ](/docs/community/contribution-guide)
    *   [
        
        Rspack
        
        ](/docs/community/rspack)
    

{"@context":"https://schema.org","author":{"@type":"Organization","name":"Vercel"},"headline":"Guides: ISR","description":"Learn how to create or update static pages at runtime with Incremental Static Regeneration.","url":"https://nextjs.org/docs/app/guides/incremental-static-regeneration","image":"https://nextjs.org/api/docs-og?title=Guides: ISR&amp;sig=b62e0eedaccd33dc","dateModified":"2026-04-15","@type":"TechArticle"}

On this page

*   [Reference](#reference)
*   [Route segment config](#route-segment-config)
*   [Functions](#functions)
*   [Examples](#examples)
*   [Time-based revalidation](#time-based-revalidation)
*   [On-demand revalidation with revalidatePath](#on-demand-revalidation-with-revalidatepath)
*   [On-demand revalidation with revalidateTag](#on-demand-revalidation-with-revalidatetag)
*   [Handling uncaught exceptions](#handling-uncaught-exceptions)
*   [Customizing the cache location](#customizing-the-cache-location)
*   [Troubleshooting](#troubleshooting)
*   [Debugging cached data in local development](#debugging-cached-data-in-local-development)
*   [Verifying correct production behavior](#verifying-correct-production-behavior)
*   [Caveats](#caveats)
*   [Platform Support](#platform-support)
*   [Version history](#version-history)

[Edit this page on GitHub](https://github.com/vercel/next.js/edit/canary/docs/01-app/02-guides/incremental-static-regeneration.mdx) Scroll to top

[App Router](/docs/app)[Guides](/docs/app/guides)ISR

Copy page

# How to implement Incremental Static Regeneration (ISR)

Last updated April 15, 2026

Examples

*   [Next.js Commerce](https://vercel.com/templates/next.js/nextjs-commerce)
*   [On-Demand ISR](https://on-demand-isr.vercel.app)
*   [Next.js Forms](https://github.com/vercel/next.js/tree/canary/examples/next-forms)

Incremental Static Regeneration (ISR) enables you to:

*   Update static content without rebuilding the entire site
*   Reduce server load by serving prerendered, static pages for most requests
*   Ensure proper `cache-control` headers are automatically added to pages
*   Handle large amounts of content pages without long `next build` times

Here's a minimal example:

app/blog/\[id\]/page.tsx

TypeScript

JavaScriptTypeScript

```
interface Post {
  id: string
  title: string
  content: string
}
 
// Next.js will invalidate the cache when a
// request comes in, at most once every 60 seconds.
export const revalidate = 60
 
export async function generateStaticParams() {
  const posts: Post[] = await fetch('https://api.vercel.app/blog').then((res) =>
    res.json()
  )
  return posts.map((post) => ({
    id: String(post.id),
  }))
}
 
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const post: Post = await fetch(`https://api.vercel.app/blog/${id}`).then(
    (res) => res.json()
  )
  return (
    <main>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </main>
  )
}
```

Here's how this example works:

1.  During `next build`, all known blog posts are generated
2.  All requests made to these pages (e.g. `/blog/1`) are cached and instantaneous
3.  After 60 seconds has passed, the next request will still return the cached (now stale) page
4.  The cache is invalidated and a new version of the page begins generating in the background
5.  Once generated successfully, the next request will return the updated page and cache it for subsequent requests
6.  If `/blog/26` is requested, and it exists, the page will be generated on-demand. This behavior can be changed by using a different [dynamicParams](/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams) value. However, if the post does not exist, then 404 is returned.

## Reference[](#reference)

### Route segment config[](#route-segment-config)

*   [`revalidate`](/docs/app/guides/caching-without-cache-components#route-segment-config-revalidate)
*   [`dynamicParams`](/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams)

### Functions[](#functions)

*   [`revalidatePath`](/docs/app/api-reference/functions/revalidatePath)
*   [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag)

## Examples[](#examples)

### Time-based revalidation[](#time-based-revalidation)

This fetches and displays a list of blog posts on /blog. After an hour has passed, the next visitor will still receive the cached (stale) version of the page immediately for a fast response. Simultaneously, Next.js triggers regeneration of a fresh version in the background. Once the new version is successfully generated, it replaces the cached version, and subsequent visitors will receive the updated content.

app/blog/page.tsx

TypeScript

JavaScriptTypeScript

```
interface Post {
  id: string
  title: string
  content: string
}
 
export const revalidate = 3600 // invalidate every hour
 
export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog')
  const posts: Post[] = await data.json()
  return (
    <main>
      <h1>Blog Posts</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </main>
  )
}
```

We recommend setting a high revalidation time. For instance, 1 hour instead of 1 second. If you need more precision, consider using on-demand revalidation. If you need real-time data, consider switching to [dynamic rendering](/docs/app/glossary#dynamic-rendering).

### On-demand revalidation with `revalidatePath`[](#on-demand-revalidation-with-revalidatepath)

For a more precise method of revalidation, invalidate cached pages on-demand with the `revalidatePath` function.

For example, this Server Action would get called after adding a new post. Regardless of how you retrieve your data in your Server Component, either using `fetch` or connecting to a database, this will invalidate the cache for the entire route. The next request to that route will trigger regeneration and serve fresh data, which will then be cached for subsequent requests.

> **Note:** `revalidatePath` invalidates the cache entries but regeneration happens on the next request. If you want to eagerly regenerate the cache entry immediately instead of waiting for the next request, you can use the Pages router [`res.revalidate`](/docs/pages/guides/incremental-static-regeneration#on-demand-validation-with-resrevalidate) method. We're working on adding new methods to provide eager regeneration capabilities for the App Router.

app/actions.ts

TypeScript

JavaScriptTypeScript

```
'use server'
 
import { revalidatePath } from 'next/cache'
 
export async function createPost() {
  // Invalidate the cache for the /posts route
  revalidatePath('/posts')
}
```

[View a demo](https://on-demand-isr.vercel.app) and [explore the source code](https://github.com/vercel/on-demand-isr).

### On-demand revalidation with `revalidateTag`[](#on-demand-revalidation-with-revalidatetag)

For most use cases, prefer revalidating entire paths. If you need more granular control, you can use the `revalidateTag` function. For example, you can tag individual `fetch` calls:

app/blog/page.tsx

TypeScript

JavaScriptTypeScript

```
export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog', {
    next: { tags: ['posts'] },
  })
  const posts = await data.json()
  // ...
}
```

If you are using an ORM or connecting to a database, you can use `unstable_cache`:

app/blog/page.tsx

TypeScript

JavaScriptTypeScript

```
import { unstable_cache } from 'next/cache'
import { db, posts } from '@/lib/db'
 
const getCachedPosts = unstable_cache(
  async () => {
    return await db.select().from(posts)
  },
  ['posts'],
  { revalidate: 3600, tags: ['posts'] }
)
 
export default async function Page() {
  const posts = getCachedPosts()
  // ...
}
```

You can then use `revalidateTag` in a [Server Actions](/docs/app/getting-started/mutating-data) or [Route Handler](/docs/app/api-reference/file-conventions/route):

app/actions.ts

TypeScript

JavaScriptTypeScript

```
'use server'
 
import { revalidateTag } from 'next/cache'
 
export async function createPost() {
  // Invalidate all data tagged with 'posts'
  revalidateTag('posts')
}
```

### Handling uncaught exceptions[](#handling-uncaught-exceptions)

If an error is thrown while attempting to revalidate data, the last successfully generated data will continue to be served from the cache. On the next subsequent request, Next.js will retry revalidating the data. [Learn more about error handling](/docs/app/getting-started/error-handling).

### Customizing the cache location[](#customizing-the-cache-location)

You can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application. [Learn more](/docs/app/guides/self-hosting#caching-and-isr).

## Troubleshooting[](#troubleshooting)

### Debugging cached data in local development[](#debugging-cached-data-in-local-development)

If you are using the `fetch` API, you can add additional logging to understand which requests are cached or uncached. [Learn more about the `logging` option](/docs/app/api-reference/config/next-config-js/logging).

next.config.js

```
module.exports = {
  logging: {
    fetches: {
      fullUrl: true,
    },
  },
}
```

### Verifying correct production behavior[](#verifying-correct-production-behavior)

To verify your pages are cached and revalidated correctly in production, you can test locally by running `next build` and then `next start` to run the production Next.js server.

This will allow you to test ISR behavior as it would work in a production environment. For further debugging, add the following environment variable to your `.env` file:

.env

```
NEXT_PRIVATE_DEBUG_CACHE=1
```

This will make the Next.js server console log ISR cache hits and misses. You can inspect the output to see which pages are generated during `next build`, as well as how pages are updated as paths are accessed on-demand.

## Caveats[](#caveats)

*   ISR is only supported when using the Node.js runtime (default).
*   ISR is not supported when creating a [Static Export](/docs/app/guides/static-exports).
*   If you have multiple `fetch` requests in a prerendered route, and each has a different `revalidate` frequency, the lowest time will be used for ISR. However, those revalidate frequencies will still be respected by the [cache](/docs/app/getting-started/caching).
*   If any of the `fetch` requests used on a route have a `revalidate` time of `0`, or an explicit `no-store`, the route will be dynamically rendered.
*   Proxy won't be executed for on-demand ISR requests, meaning any path rewrites or logic in Proxy will not be applied. Ensure you are revalidating the exact path. For example, `/post/1` instead of a rewritten `/post-1`.
*   When running multiple instances, the default file-system cache is per-instance. On-demand revalidation only invalidates the instance that receives the call. Use a shared [custom cache handler](/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath) to coordinate across instances. See [How Revalidation Works](/docs/app/guides/how-revalidation-works) for the full architecture.
*   Background regeneration (stale-while-revalidate) runs on the instance that receives the triggering request. On platforms with per-request billing, this background work counts as additional compute.
*   You can use the `x-nextjs-cache` response header to observe cache behavior. Values are `HIT` (served from cache), `STALE` (served from cache, revalidating in background), `MISS` (not in cache, rendered fresh), or `REVALIDATED` (regenerated via on-demand revalidation).

## Platform Support[](#platform-support)

Deployment Option

Supported

[Node.js server](/docs/app/getting-started/deploying#nodejs-server)

Yes

[Docker container](/docs/app/getting-started/deploying#docker)

Yes

[Static export](/docs/app/getting-started/deploying#static-export)

No

[Adapters](/docs/app/getting-started/deploying#adapters)

Platform-specific

Learn how to [configure ISR](/docs/app/guides/self-hosting#caching-and-isr) when self-hosting Next.js.

## Version history[](#version-history)

Version

Changes

`v14.1.0`

Custom `cacheHandler` is stable.

`v13.0.0`

App Router is introduced.

`v12.2.0`

Pages Router: On-Demand ISR is stable

`v12.0.0`

Pages Router: [Bot-aware ISR fallback](/blog/next-12#bot-aware-isr-fallback) added.

`v9.5.0`

Pages Router: [Stable ISR introduced](/blog/next-9-5).

[Previous

How Revalidation Works

](/docs/app/guides/how-revalidation-works)

[Next

Instrumentation

](/docs/app/guides/instrumentation)

Was this helpful?

supported.

Send
