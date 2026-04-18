---
title: "Middleware Upgrade Guide"
source: "https://nextjs.org/docs/messages/middleware-upgrade-guide"
canonical_url: "https://nextjs.org/docs/messages/middleware-upgrade-guide"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:17:52.001Z"
content_hash: "8b5d1e54a32a4dbc5ebd998e414f62e771e614b416b52f9100afc7342b235b85"
menu_path: ["Middleware Upgrade Guide"]
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
    

[Docs](/docs)[Errors](/docs)Middleware Upgrade Guide

# Middleware Upgrade Guide

As we work on improving Middleware for General Availability (GA), we've made some changes to the Middleware APIs (and how you define Middleware in your application) based on your feedback.

This upgrade guide will help you understand the changes, why they were made, and how to migrate your existing Middleware to the new API. The guide is for Next.js developers who:

*   Currently use the beta Next.js Middleware features
*   Choose to upgrade to the next stable version of Next.js (`v12.2`)

You can start upgrading your Middleware usage today with the latest release (`npm i next@latest`).

> **Note**: These changes described in this guide are included in Next.js `12.2`. You can keep your current site structure, including nested Middleware, until you move to `12.2` (or a `canary` build of Next.js).

If you have ESLint configured, you will need to run `npm i eslint-config-next@latest --save-dev` to upgrade your ESLint configuration to ensure the same version is being used as the Next.js version. You might also need to restart VSCode for the changes to take effect.

## Using Next.js Middleware on Vercel[](#using-nextjs-middleware-on-vercel)

If you're using Next.js on Vercel, your existing deploys using Middleware will continue to work, and you can continue to deploy your site using Middleware. When you upgrade your site to the next stable version of Next.js (`v12.2`), you will need to follow this upgrade guide to update your Middleware.

## Breaking changes[](#breaking-changes)

1.  [No Nested Middleware](#no-nested-middleware)
2.  [No Response Body](#no-response-body)
3.  [Cookies API Revamped](#cookies-api-revamped)
4.  [New User-Agent Helper](#new-user-agent-helper)
5.  [No More Page Match Data](#no-more-page-match-data)
6.  [Executing Middleware on Internal Next.js Requests](#executing-middleware-on-internal-nextjs-requests)

## No Nested Middleware[](#no-nested-middleware)

### Summary of changes[](#summary-of-changes)

*   Define a single Middleware file next to your `pages` folder
*   No need to prefix the file with an underscore
*   A custom matcher can be used to define matching routes using an exported config object

### Explanation[](#explanation)

Previously, you could create a `_middleware.ts` file under the `pages` directory at any level. Middleware execution was based on the file path where it was created.

Based on customer feedback, we have replaced this API with a single root Middleware, which provides the following improvements:

*   **Faster execution with lower latency**: With nested Middleware, a single request could invoke multiple Middleware functions. A single Middleware means a single function execution, which is more efficient.
*   **Less expensive**: Middleware usage is billed per invocation. Using nested Middleware, a single request could invoke multiple Middleware functions, meaning multiple Middleware charges per request. A single Middleware means a single invocation per request and is more cost effective.
*   **Middleware can conveniently filter on things besides routes**: With nested Middleware, the Middleware files were located in the `pages` directory and Middleware was executed based on request paths. By moving to a single root Middleware, you can still execute code based on request paths, but you can now more conveniently execute Middleware based on other conditions, like `cookies` or the presence of a request header.
*   **Deterministic execution ordering**: With nested Middleware, a single request could match multiple Middleware functions. For example, a request to `/dashboard/users/*` would invoke Middleware defined in both `/dashboard/users/_middleware.ts` and `/dashboard/_middleware.js`. However, the execution order is difficult to reason about. Moving to a single, root Middleware more explicitly defines execution order.
*   **Supports Next.js Layouts (RFC)**: Moving to a single, root Middleware helps support the new [Layouts (RFC) in Next.js](/blog/layouts-rfc).

### How to upgrade[](#how-to-upgrade)

You should declare **one single Middleware file** in your application, which should be located next to the `pages` directory and named **without** an `_` prefix. Your Middleware file can still have either a `.ts` or `.js` extension.

Middleware will be invoked for **every route in the app**, and a custom matcher can be used to define matching filters. The following is an example for a Middleware that triggers for `/about/*` and `/dashboard/:path*`, the custom matcher is defined in an exported config object:

middleware.ts

```
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
 
export function middleware(request: NextRequest) {
  return NextResponse.rewrite(new URL('/about-2', request.url))
}
 
// Supports both a single string value or an array of matchers
export const config = {
  matcher: ['/about/:path*', '/dashboard/:path*'],
}
```

The matcher config also allows full regex so matching like negative lookaheads or character matching is supported. An example of a negative lookahead to match all except specific paths can be seen here:

middleware.ts

```
export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - favicon.ico (favicon file)
     */
    '/((?!api|_next/static|favicon.ico).*)',
  ],
}
```

While the config option is preferred since it doesn't get invoked on every request, you can also use conditional statements to only run the Middleware when it matches specific paths. One advantage of using conditionals is defining explicit ordering for when Middleware executes. The following example shows how you can merge two previously nested Middleware:

middleware.ts

```
import type { NextRequest } from 'next/server'
 
export function middleware(request: NextRequest) {
  if (request.nextUrl.pathname.startsWith('/about')) {
    // This logic is only applied to /about
  }
 
  if (request.nextUrl.pathname.startsWith('/dashboard')) {
    // This logic is only applied to /dashboard
  }
}
```

## No Response Body[](#no-response-body)

### Summary of changes[](#summary-of-changes-1)

*   Middleware can no longer produce a response body
*   If your Middleware _does_ respond with a body, a runtime error will be thrown
*   Migrate to using `rewrite`/`redirect` to pages/APIs handling a response

### Explanation[](#explanation-1)

To respect the differences in client-side and server-side navigation, and to help ensure that developers do not build insecure Middleware, we are removing the ability to send response bodies in Middleware. This ensures that Middleware is only used to `rewrite`, `redirect`, or modify the incoming request (e.g. [setting cookies](#cookies-api-revamped)).

The following patterns will no longer work:

```
new Response('a text value')
new Response(streamOrBuffer)
new Response(JSON.stringify(obj), { headers: 'application/json' })
NextResponse.json()
```

### How to upgrade[](#how-to-upgrade-1)

For cases where Middleware is used to respond (such as authorization), you should migrate to use `rewrite`/`redirect` to pages that show an authorization error, login forms, or to an API Route.

#### Before[](#before)

pages/\_middleware.ts

```
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import { isAuthValid } from './lib/auth'
 
export function middleware(request: NextRequest) {
  // Example function to validate auth
  if (isAuthValid(request)) {
    return NextResponse.next()
  }
 
  return NextResponse.json({ message: 'Auth required' }, { status: 401 })
}
```

#### After[](#after)

middleware.ts

```
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import { isAuthValid } from './lib/auth'
 
export function middleware(request: NextRequest) {
  // Example function to validate auth
  if (isAuthValid(request)) {
    return NextResponse.next()
  }
 
  const loginUrl = new URL('/login', request.url)
  loginUrl.searchParams.set('from', request.nextUrl.pathname)
 
  return NextResponse.redirect(loginUrl)
}
```

#### Edge API Routes[](#edge-api-routes)

If you were previously using Middleware to forward headers to an external API, you can now use [Edge API Routes](/docs/pages/building-your-application/routing/api-routes):

pages/api/proxy.ts

```
import { type NextRequest } from 'next/server'
 
export const config = {
  runtime: 'edge',
}
 
export default async function handler(req: NextRequest) {
  const authorization = req.cookies.get('authorization')
  return fetch('https://backend-api.com/api/protected', {
    method: req.method,
    headers: {
      authorization,
    },
    redirect: 'manual',
  })
}
```

## Cookies API Revamped[](#cookies-api-revamped)

### Summary of changes[](#summary-of-changes-2)

Added

Removed

`cookies.set`

`cookie`

`cookies.delete`

`clearCookie`

`cookies.getWithOptions`

`cookies`

### Explanation[](#explanation-2)

Based on beta feedback, we are changing the Cookies API in `NextRequest` and `NextResponse` to align more to a `get`/`set` model. The `Cookies` API extends Map, including methods like [entries](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Map/entries) and [values](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Map/entries).

### How to upgrade[](#how-to-upgrade-2)

`NextResponse` now has a `cookies` instance with:

*   `cookies.delete`
*   `cookies.set`
*   `cookies.getWithOptions`

As well as other extended methods from `Map`.

#### Before[](#before-1)

pages/\_middleware.ts

```
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
 
export function middleware(request: NextRequest) {
  // create an instance of the class to access the public methods. This uses `next()`,
  // you could use `redirect()` or `rewrite()` as well
  let response = NextResponse.next()
  // get the cookies from the request
  let cookieFromRequest = request.cookies['my-cookie']
  // set the `cookie`
  response.cookie('hello', 'world')
  // set the `cookie` with options
  const cookieWithOptions = response.cookie('hello', 'world', {
    path: '/',
    maxAge: 1000 * 60 * 60 * 24 * 7,
    httpOnly: true,
    sameSite: 'strict',
    domain: 'example.com',
  })
  // clear the `cookie`
  response.clearCookie('hello')
 
  return response
}
```

#### After[](#after-1)

middleware.ts

```
export function middleware() {
  const response = new NextResponse()
 
  // set a cookie
  response.cookies.set('vercel', 'fast')
 
  // set another cookie with options
  response.cookies.set('nextjs', 'awesome', { path: '/test' })
 
  // get all the details of a cookie
  const { value, ...options } = response.cookies.getWithOptions('vercel')
  console.log(value) // => 'fast'
  console.log(options) // => { name: 'vercel', Path: '/test' }
 
  // deleting a cookie will mark it as expired
  response.cookies.delete('vercel')
 
  return response
}
```

## New User-Agent Helper[](#new-user-agent-helper)

### Summary of changes[](#summary-of-changes-3)

*   Accessing the user agent is no longer available on the request object
*   We've added a new `userAgent` helper to reduce Middleware size by `17kb`

### Explanation[](#explanation-3)

To help reduce the size of your Middleware, we have extracted the user agent from the request object and created a new helper `userAgent`.

The helper is imported from `next/server` and allows you to opt in to using the user agent. The helper gives you access to the same properties that were available from the request object.

### How to upgrade[](#how-to-upgrade-3)

*   Import the `userAgent` helper from `next/server`
*   Destructure the properties you need to work with

#### Before[](#before-2)

pages/\_middleware.ts

```
import { NextRequest, NextResponse } from 'next/server'
 
export function middleware(request: NextRequest) {
  const url = request.nextUrl
  const viewport = request.ua.device.type === 'mobile' ? 'mobile' : 'desktop'
  url.searchParams.set('viewport', viewport)
  return NextResponse.rewrite(url)
}
```

#### After[](#after-2)

middleware.ts

```
import { NextRequest, NextResponse, userAgent } from 'next/server'
 
export function middleware(request: NextRequest) {
  const url = request.nextUrl
  const { device } = userAgent(request)
  const viewport = device.type === 'mobile' ? 'mobile' : 'desktop'
  url.searchParams.set('viewport', viewport)
  return NextResponse.rewrite(url)
}
```

## No More Page Match Data[](#no-more-page-match-data)

### Summary of changes[](#summary-of-changes-4)

*   Use [`URLPattern`](https://developer.mozilla.org/docs/Web/API/URLPattern) to check if a Middleware is being invoked for a certain page match

### Explanation[](#explanation-4)

Currently, Middleware estimates whether you are serving an asset of a Page based on the Next.js routes manifest (internal configuration). This value is surfaced through `request.page`.

To make page and asset matching more accurate, we are now using the web standard `URLPattern` API.

### How to upgrade[](#how-to-upgrade-4)

Use [`URLPattern`](https://developer.mozilla.org/docs/Web/API/URLPattern) to check if a Middleware is being invoked for a certain page match.

#### Before[](#before-3)

pages/\_middleware.ts

```
import { NextResponse } from 'next/server'
import type { NextRequest, NextFetchEvent } from 'next/server'
 
export function middleware(request: NextRequest, event: NextFetchEvent) {
  const { params } = event.request.page
  const { locale, slug } = params
 
  if (locale && slug) {
    const { search, protocol, host } = request.nextUrl
    const url = new URL(`${protocol}//${locale}.${host}/${slug}${search}`)
    return NextResponse.redirect(url)
  }
}
```

#### After[](#after-3)

middleware.ts

```
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
 
const PATTERNS = [
  [
    new URLPattern({ pathname: '/:locale/:slug' }),
    ({ pathname }) => pathname.groups,
  ],
]
 
const params = (url) => {
  const input = url.split('?')[0]
  let result = {}
 
  for (const [pattern, handler] of PATTERNS) {
    const patternResult = pattern.exec(input)
    if (patternResult !== null && 'pathname' in patternResult) {
      result = handler(patternResult)
      break
    }
  }
  return result
}
 
export function middleware(request: NextRequest) {
  const { locale, slug } = params(request.url)
 
  if (locale && slug) {
    const { search, protocol, host } = request.nextUrl
    const url = new URL(`${protocol}//${locale}.${host}/${slug}${search}`)
    return NextResponse.redirect(url)
  }
}
```

## Executing Middleware on Internal Next.js Requests[](#executing-middleware-on-internal-nextjs-requests)

### Summary of changes[](#summary-of-changes-5)

*   Middleware will be executed for _all_ requests, including `_next`

### Explanation[](#explanation-5)

Prior to Next.js `v12.2`, Middleware was not executed for `_next` requests.

For cases where Middleware is used for authorization, you should migrate to use `rewrite`/`redirect` to Pages that show an authorization error, login forms, or to an API Route.

See [No Response Body](#no-response-body) for an example of how to migrate to use `rewrite`/`redirect`.

Was this helpful?

supported.

Send
