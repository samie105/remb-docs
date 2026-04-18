---
title: "How to set up Jest with Next.js"
source: "https://nextjs.org/docs/app/guides/testing/jest"
canonical_url: "https://nextjs.org/docs/app/guides/testing/jest"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:16:39.116Z"
content_hash: "174995aa37cc9b851d4b87572fe05d7bbe2550a3ba44ade8805b9c6f0a37a366"
menu_path: ["How to set up Jest with Next.js"]
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
    

{"@context":"https://schema.org","author":{"@type":"Organization","name":"Vercel"},"headline":"Testing: Jest","description":"Learn how to set up Jest with Next.js for Unit Testing and Snapshot Testing.","url":"https://nextjs.org/docs/app/guides/testing/jest","image":"https://nextjs.org/api/docs-og?title=Testing: Jest&amp;sig=e0f7231ecec193a2","dateModified":"2026-04-15","@type":"TechArticle"}

On this page

*   [Quickstart](#quickstart)
*   [Manual setup](#manual-setup)
*   [Optional: Handling Absolute Imports and Module Path Aliases](#optional-handling-absolute-imports-and-module-path-aliases)
*   [Optional: Extend Jest with custom matchers](#optional-extend-jest-with-custom-matchers)
*   [Add a test script to package.json](#add-a-test-script-to-packagejson)
*   [Creating your first test](#creating-your-first-test)
*   [Running your tests](#running-your-tests)
*   [Additional Resources](#additional-resources)

[Edit this page on GitHub](https://github.com/vercel/next.js/edit/canary/docs/01-app/02-guides/testing/jest.mdx) Scroll to top

[Guides](/docs/app/guides)[Testing](/docs/app/guides/testing)Jest

Copy page

# How to set up Jest with Next.js

Last updated April 15, 2026

Jest and React Testing Library are frequently used together for **Unit Testing** and **Snapshot Testing**. This guide will show you how to set up Jest with Next.js and write your first tests.

> **Good to know:** Since `async` Server Components are new to the React ecosystem, Jest currently does not support them. While you can still run **unit tests** for synchronous Server and Client Components, we recommend using an **E2E tests** for `async` components.

## Quickstart[](#quickstart)

You can use `create-next-app` with the Next.js [with-jest](https://github.com/vercel/next.js/tree/canary/examples/with-jest) example to quickly get started:

pnpmnpmyarnbun

Terminal

```
pnpm create next-app --example with-jest with-jest-app
```

## Manual setup[](#manual-setup)

Since the release of [Next.js 12](https://nextjs.org/blog/next-12), Next.js now has built-in configuration for Jest.

To set up Jest, install `jest` and the following packages as dev dependencies:

pnpmnpmyarnbun

Terminal

```
pnpm add -D jest jest-environment-jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom ts-node @types/jest
```

Generate a basic Jest configuration file by running the following command:

pnpmnpmyarnbun

Terminal

```
pnpm create jest@latest
```

This will take you through a series of prompts to setup Jest for your project, including automatically creating a `jest.config.ts|js` file.

Update your config file to use `next/jest`. This transformer has all the necessary configuration options for Jest to work with Next.js:

jest.config.ts

TypeScript

JavaScriptTypeScript

```
import type { Config } from 'jest'
import nextJest from 'next/jest.js'
 
const createJestConfig = nextJest({
  // Provide the path to your Next.js app to load next.config.js and .env files in your test environment
  dir: './',
})
 
// Add any custom config to be passed to Jest
const config: Config = {
  coverageProvider: 'v8',
  testEnvironment: 'jsdom',
  // Add more setup options before each test is run
  // setupFilesAfterEnv: ['<rootDir>/jest.setup.ts'],
}
 
// createJestConfig is exported this way to ensure that next/jest can load the Next.js config which is async
export default createJestConfig(config)
```

Under the hood, `next/jest` is automatically configuring Jest for you, including:

*   Setting up `transform` using the [Next.js Compiler](/docs/architecture/nextjs-compiler).
*   Auto mocking stylesheets (`.css`, `.module.css`, and their scss variants), image imports and [`next/font`](/docs/app/api-reference/components/font).
*   Loading `.env` (and all variants) into `process.env`.
*   Ignoring `node_modules` from test resolving and transforms.
*   Ignoring `.next` from test resolving.
*   Loading `next.config.js` for flags that enable SWC transforms.

> **Good to know**: To test environment variables directly, load them manually in a separate setup script or in your `jest.config.ts` file. For more information, please see [Test Environment Variables](/docs/app/guides/environment-variables#test-environment-variables).

## Optional: Handling Absolute Imports and Module Path Aliases[](#optional-handling-absolute-imports-and-module-path-aliases)

If your project is using [Module Path Aliases](/docs/app/getting-started/installation#set-up-absolute-imports-and-module-path-aliases), you will need to configure Jest to resolve the imports by matching the paths option in the `jsconfig.json` file with the `moduleNameMapper` option in the `jest.config.js` file. For example:

tsconfig.json or jsconfig.json

```
{
  "compilerOptions": {
    "module": "esnext",
    "moduleResolution": "bundler",
    "baseUrl": "./",
    "paths": {
      "@/components/*": ["components/*"]
    }
  }
}
```

jest.config.js

```
moduleNameMapper: {
  // ...
  '^@/components/(.*)$': '<rootDir>/components/$1',
}
```

## Optional: Extend Jest with custom matchers[](#optional-extend-jest-with-custom-matchers)

`@testing-library/jest-dom` includes a set of convenient [custom matchers](https://github.com/testing-library/jest-dom#custom-matchers) such as `.toBeInTheDocument()` making it easier to write tests. You can import the custom matchers for every test by adding the following option to the Jest configuration file:

jest.config.ts

TypeScript

JavaScriptTypeScript

```
setupFilesAfterEnv: ['<rootDir>/jest.setup.ts']
```

Then, inside `jest.setup`, add the following import:

jest.setup.ts

TypeScript

JavaScriptTypeScript

```
import '@testing-library/jest-dom'
```

> **Good to know:** [`extend-expect` was removed in `v6.0`](https://github.com/testing-library/jest-dom/releases/tag/v6.0.0), so if you are using `@testing-library/jest-dom` before version 6, you will need to import `@testing-library/jest-dom/extend-expect` instead.

If you need to add more setup options before each test, you can add them to the `jest.setup` file above.

## Add a test script to `package.json`[](#add-a-test-script-to-packagejson)

Finally, add a Jest `test` script to your `package.json` file:

package.json

```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "test": "jest",
    "test:watch": "jest --watch"
  }
}
```

`jest --watch` will re-run tests when a file is changed. For more Jest CLI options, please refer to the [Jest Docs](https://jestjs.io/docs/cli#reference).

### Creating your first test[](#creating-your-first-test)

Your project is now ready to run tests. Create a folder called `__tests__` in your project's root directory.

For example, we can add a test to check if the `<Page />` component successfully renders a heading:

app/page.js

```
import Link from 'next/link'
 
export default function Page() {
  return (
    <div>
      <h1>Home</h1>
      <Link href="/about">About</Link>
    </div>
  )
}
```

\_\_tests\_\_/page.test.jsx

```
import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import Page from '../app/page'
 
describe('Page', () => {
  it('renders a heading', () => {
    render(<Page />)
 
    const heading = screen.getByRole('heading', { level: 1 })
 
    expect(heading).toBeInTheDocument()
  })
})
```

Optionally, add a [snapshot test](https://jestjs.io/docs/snapshot-testing) to keep track of any unexpected changes in your component:

\_\_tests\_\_/snapshot.js

```
import { render } from '@testing-library/react'
import Page from '../app/page'
 
it('renders homepage unchanged', () => {
  const { container } = render(<Page />)
  expect(container).toMatchSnapshot()
})
```

## Running your tests[](#running-your-tests)

Then, run the following command to run your tests:

pnpmnpmyarnbun

Terminal

```
pnpm test
```

## Additional Resources[](#additional-resources)

For further reading, you may find these resources helpful:

*   [Next.js with Jest example](https://github.com/vercel/next.js/tree/canary/examples/with-jest)
*   [Jest Docs](https://jestjs.io/docs/getting-started)
*   [React Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)
*   [Testing Playground](https://testing-playground.com/) - use good testing practices to match elements.

[Previous

Cypress

](/docs/app/guides/testing/cypress)

[Next

Playwright

](/docs/app/guides/testing/playwright)

Was this helpful?

supported.

Send
