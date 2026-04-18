---
title: "How revalidation works in Next.js"
source: "https://nextjs.org/docs/app/guides/how-revalidation-works"
canonical_url: "https://nextjs.org/docs/app/guides/how-revalidation-works"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:14:47.275Z"
content_hash: "6468539221986f688c807522e19de8ca9f184a60531cc593dddb3f449b60e85a"
menu_path: ["How revalidation works in Next.js"]
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
    

{"@context":"https://schema.org","author":{"@type":"Organization","name":"Vercel"},"headline":"Guides: How Revalidation Works","description":"A deep dive into how Next.js revalidates cached content, including the tag system, cache consistency, and multi-instance coordination.","url":"https://nextjs.org/docs/app/guides/how-revalidation-works","image":"https://nextjs.org/api/docs-og?title=Guides: How Revalidation Works&amp;sig=7ad649ea5411d62e","dateModified":"2026-04-15","@type":"TechArticle"}

On this page

*   [The Revalidation Model](#the-revalidation-model)
*   [What Gets Revalidated](#what-gets-revalidated)
*   [What happens if they get out of sync](#what-happens-if-they-get-out-of-sync)
*   [Tag System Architecture](#tag-system-architecture)
*   [Explicit tags](#explicit-tags)
*   [Soft tags](#soft-tags)
*   [Multi-Instance Considerations](#multi-instance-considerations)
*   [Implementation Patterns for Platforms](#implementation-patterns-for-platforms)
*   [Single instance](#single-instance)
*   [Multi-instance with shared cache](#multi-instance-with-shared-cache)
*   [CDN integration](#cdn-integration)
*   [Graceful Degradation](#graceful-degradation)

[Edit this page on GitHub](https://github.com/vercel/next.js/edit/canary/docs/01-app/02-guides/how-revalidation-works.mdx) Scroll to top

[App Router](/docs/app)[Guides](/docs/app/guides)How Revalidation Works

Copy page

# How revalidation works in Next.js

Last updated April 15, 2026

The [Caching](/docs/app/getting-started/caching) page covers how to use `use cache`, `cacheTag`, and `cacheLife`. This page explains **how revalidation works internally**, for platform engineers and advanced users who need to understand the system to implement [custom cache handlers](/docs/app/api-reference/config/next-config-js/cacheHandlers) or debug revalidation behavior.

## The Revalidation Model[](#the-revalidation-model)

Most routes in Next.js can be revalidated on demand. This includes App Router routes and Pages Router routes that produce ISR/prerender cache entries. Pages Router routes that are automatically statically optimized (pure static output) are not revalidated on demand. The ability to update cached content without redeploying is a core part of Next.js's [rendering model](/docs/app/guides/rendering-philosophy).

There are two types of revalidation:

*   **Time-based revalidation** uses a stale-while-revalidate pattern. The cached content is served immediately, and a background regeneration is triggered when the content's age exceeds the [`cacheLife`](/docs/app/api-reference/functions/cacheLife) or `revalidate` duration. The stale content continues to be served until the fresh content is ready.
*   **On-demand revalidation** explicitly invalidates cached content by calling [`revalidateTag()`](/docs/app/api-reference/functions/revalidateTag) or [`revalidatePath()`](/docs/app/api-reference/functions/revalidatePath). The next request to that content triggers a fresh render.

> **Good to know:** Pages Router on-demand ISR APIs (for example `res.revalidate()` and the `x-prerender-revalidate` flow) are still supported and use the server cache handler (`cacheHandler`, singular). The `cacheHandlers` option (plural) is for `'use cache'` directives.

## What Gets Revalidated[](#what-gets-revalidated)

When a route is revalidated, Next.js regenerates **both** the HTML response and the RSC payload (React Server Components payload) from the same React component tree. Both artifacts are stored together in the same cache entry.

This consistency matters because the RSC payload is used for client-side navigations. Browser navigations and client-side navigations should hold the same content.

### What happens if they get out of sync[](#what-happens-if-they-get-out-of-sync)

If a platform's cache serves HTML from one render and an RSC payload from a different render, users may see stale or mismatched content during client-side navigation. The primary mitigation is to cache HTML and RSC responses together with the same TTL and invalidation policy, and to respect the [`Vary` header](/docs/app/guides/cdn-caching) that Next.js sets. See [CDN Caching](/docs/app/guides/cdn-caching) for details.

A separate but related problem is **cross-deployment skew**: during rolling deployments, a client built with deploy A may receive responses from a server running deploy B. [`deploymentId`](/docs/app/api-reference/config/next-config-js/deploymentId) mitigates this: when the client detects a different deployment ID from the server, it triggers a hard navigation to fetch consistent content.

## Tag System Architecture[](#tag-system-architecture)

Next.js uses a tag-based system to track which cached content needs to be invalidated. There are two types of tags:

### Explicit tags[](#explicit-tags)

Explicit tags are set by the developer using [`cacheTag()`](/docs/app/api-reference/functions/cacheTag) inside a `use cache` function, or via `next: { tags: [...] }` on a `fetch` call. When [`revalidateTag('my-tag')`](/docs/app/api-reference/functions/revalidateTag) is called, all cache entries with that tag are invalidated.

### Soft tags[](#soft-tags)

Soft tags are automatically generated by Next.js based on the route path, prefixed with `_N_T_`. For example, the route `/blog/hello` generates soft tags like `_N_T_/layout`, `_N_T_/blog/layout`, `_N_T_/blog/hello/layout`, and `_N_T_/blog/hello`. Each segment in the path gets a layout tag, plus the leaf route itself.

Soft tags enable [`revalidatePath()`](/docs/app/api-reference/functions/revalidatePath) to work through the same tag-based system. When `revalidatePath('/blog/hello')` is called, it invalidates cache entries associated with that path's leaf route tag and its ancestor layout soft tags (for example `_N_T_/layout`, `_N_T_/blog/layout`, `_N_T_/blog/hello/layout`, and `_N_T_/blog/hello`).

In the [cache handler API](/docs/app/api-reference/config/next-config-js/cacheHandlers), soft tags are passed to the `get()` method as the `softTags` parameter. Your handler should check whether any soft tag has been invalidated after the cache entry's timestamp. The `getExpiration()` method returns the most recent revalidation timestamp across all provided tags, or `0` if none have been revalidated. Your handler should treat an entry as stale if the returned timestamp is newer than the entry's own timestamp. See the [cache handler API reference](/docs/app/api-reference/config/next-config-js/cacheHandlers#getexpiration) for the full semantics.

## Multi-Instance Considerations[](#multi-instance-considerations)

When running multiple Next.js instances behind a load balancer, revalidation events are local by default. Calling `revalidateTag()` on instance A only invalidates the cache on that instance. Other instances continue serving the stale content until they learn about the invalidation.

The cache handler API provides two hooks for distributed coordination:

*   **`updateTags()`** is called when `revalidateTag()` is invoked. Your handler should write the invalidation event to shared storage (for example, Redis or a database) so other instances can discover it.
*   **`refreshTags()`** is called periodically, but always before starting a new request. Your handler should check shared storage for recent invalidation events and update its local tag state accordingly.

For implementation details and a Redis example, see [Custom Cache Handlers](/docs/app/api-reference/config/next-config-js/cacheHandlers).

## Implementation Patterns for Platforms[](#implementation-patterns-for-platforms)

### Single instance[](#single-instance)

The default file-system cache handles consistency automatically. Cache writes are atomic on the local filesystem, and tag state is maintained in memory. No additional configuration is needed.

### Multi-instance with shared cache[](#multi-instance-with-shared-cache)

Without coordination, each instance independently serves content and handles revalidation using only its local cache. Different users may see different content depending on which instance serves their request, and on-demand revalidation only takes effect on the instance that received the call.

To reduce this window and ensure revalidation propagates across instances:

1.  Store tag invalidation timestamps in a shared service (Redis, DynamoDB, or a simple HTTP API).
2.  Implement `updateTags()` to write to the shared service.
3.  Implement `refreshTags()` to read from the shared service. Your handler must catch errors in `refreshTags()`: if it throws, the exception propagates as a request failure. Catching the error allows requests to continue with the last known local tag state, serving potentially stale content until connectivity is restored.
4.  Store cache entries (HTML + RSC payload) in shared storage. Atomic writes reduce the mismatch window further but are not required for correctness.

### CDN integration[](#cdn-integration)

If a CDN caches Next.js responses, it should respect the `Vary` header and the `Cache-Control` directives that Next.js sets. Do not cache HTML and RSC payload responses separately with different TTLs. See [CDN Caching](/docs/app/guides/cdn-caching) for details.

## Graceful Degradation[](#graceful-degradation)

The revalidation system prioritizes availability over strict consistency. Content is always served, even when infrastructure guarantees cannot be fully met:

*   **Cache write failure**: the response is still served to the user because writes are asynchronous. The cache entry is lost, and the next request triggers a fresh render.
*   **Cache read failure**: your handler should catch internal errors and return `undefined` (the cache miss signal). The route is then server-rendered fresh. The framework does not wrap `get()` in a try/catch, so unhandled exceptions will propagate as render errors.
*   **HTML/RSC cache inconsistency**: if a CDN caches HTML and RSC responses with different TTLs or invalidation timing, users may see mismatched content during client-side navigation. Cache them together and respect the `Vary` header to avoid this.
*   **Cross-deployment skew**: during rolling deployments, configure [`deploymentId`](/docs/app/api-reference/config/next-config-js/deploymentId) so that a build ID change triggers a hard navigation to fetch consistent content.

Cache failures result in degraded performance (stale content, extra renders), not broken applications.

Related guides and references.

[

### Caching

Learn how to cache data and UI in Next.js

](/docs/app/getting-started/caching)[

### ISR

Learn how to create or update static pages at runtime with Incremental Static Regeneration.

](/docs/app/guides/incremental-static-regeneration)[

### cacheHandlers

Configure custom cache handlers for use cache directives in Next.js.

](/docs/app/api-reference/config/next-config-js/cacheHandlers)[

### revalidateTag

API Reference for the revalidateTag function.

](/docs/app/api-reference/functions/revalidateTag)

[Previous

Forms

](/docs/app/guides/forms)

[Next

ISR

](/docs/app/guides/incremental-static-regeneration)

Was this helpful?

supported.

Send
