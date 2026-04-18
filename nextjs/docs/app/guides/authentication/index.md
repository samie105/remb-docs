---
title: "How to implement authentication in Next.js"
source: "https://nextjs.org/docs/app/guides/authentication"
canonical_url: "https://nextjs.org/docs/app/guides/authentication"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:14:06.473Z"
content_hash: "e7f821e7aa16598637e07520ecc8ae36d9355675b7049f1431901567ec0c39c3"
menu_path: ["How to implement authentication in Next.js"]
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
    

{"@context":"https://schema.org","author":{"@type":"Organization","name":"Vercel"},"headline":"Guides: Authentication","description":"Learn how to implement authentication in your Next.js application.","url":"https://nextjs.org/docs/app/guides/authentication","image":"https://nextjs.org/api/docs-og?title=Guides: Authentication&amp;sig=208875cbd9a9e893","dateModified":"2026-04-15","@type":"TechArticle"}

On this page

*   [Authentication](#authentication)
*   [Sign-up and login functionality](#sign-up-and-login-functionality)
*   [1\. Capture user credentials](#1-capture-user-credentials)
*   [2\. Validate form fields on the server](#2-validate-form-fields-on-the-server)
*   [3\. Create a user or check user credentials](#3-create-a-user-or-check-user-credentials)
*   [Session Management](#session-management)
*   [Stateless Sessions](#stateless-sessions)
*   [1\. Generating a secret key](#1-generating-a-secret-key)
*   [2\. Encrypting and decrypting sessions](#2-encrypting-and-decrypting-sessions)
*   [3\. Setting cookies (recommended options)](#3-setting-cookies-recommended-options)
*   [Updating (or refreshing) sessions](#updating-or-refreshing-sessions)
*   [Deleting the session](#deleting-the-session)
*   [Database Sessions](#database-sessions)
*   [Authorization](#authorization)
*   [Optimistic checks with Proxy (Optional)](#optimistic-checks-with-proxy-optional)
*   [Creating a Data Access Layer (DAL)](#creating-a-data-access-layer-dal)
*   [Using Data Transfer Objects (DTO)](#using-data-transfer-objects-dto)
*   [Server Components](#server-components)
*   [Layouts and auth checks](#layouts-and-auth-checks)
*   [Auth checks in page components](#auth-checks-in-page-components)
*   [Auth checks in leaf components](#auth-checks-in-leaf-components)
*   [Server Actions](#server-actions)
*   [Route Handlers](#route-handlers)
*   [Context Providers](#context-providers)
*   [Resources](#resources)
*   [Auth Libraries](#auth-libraries)
*   [Session Management Libraries](#session-management-libraries)
*   [Further Reading](#further-reading)

[Edit this page on GitHub](https://github.com/vercel/next.js/edit/canary/docs/01-app/02-guides/authentication.mdx) Scroll to top

[App Router](/docs/app)[Guides](/docs/app/guides)Authentication

Copy page

# How to implement authentication in Next.js

Last updated April 15, 2026

Understanding authentication is crucial for protecting your application's data. This page will guide you through what React and Next.js features to use to implement auth.

Before starting, it helps to break down the process into three concepts:

1.  **[Authentication](#authentication)**: Verifies if the user is who they say they are. It requires the user to prove their identity with something they have, such as a username and password.
2.  **[Session Management](#session-management)**: Tracks the user's auth state across requests.
3.  **[Authorization](#authorization)**: Decides what routes and data the user can access.

This diagram shows the authentication flow using React and Next.js features:

![Diagram showing the authentication flow with React and Next.js features](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fauthentication-overview.png&w=3840&q=75)![Diagram showing the authentication flow with React and Next.js features](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fauthentication-overview.png&w=3840&q=75)

The examples on this page walk through basic username and password auth for educational purposes. While you can implement a custom auth solution, for increased security and simplicity, we recommend using an authentication library. These offer built-in solutions for authentication, session management, and authorization, as well as additional features such as social logins, multi-factor authentication, and role-based access control. You can find a list in the [Auth Libraries](#auth-libraries) section.

## Authentication[](#authentication)

### Sign-up and login functionality[](#sign-up-and-login-functionality)

You can use the [`<form>`](https://react.dev/reference/react-dom/components/form) element with React's [Server Actions](/docs/app/getting-started/mutating-data) and `useActionState` to capture user credentials, validate form fields, and call your Authentication Provider's API or database.

Since Server Actions always execute on the server, they provide a secure environment for handling authentication logic.

Here are the steps to implement signup/login functionality:

#### 1\. Capture user credentials[](#1-capture-user-credentials)

To capture user credentials, create a form that invokes a Server Action on submission. For example, a signup form that accepts the user's name, email, and password:

app/ui/signup-form.tsx

TypeScript

JavaScriptTypeScript

```
import { signup } from '@/app/actions/auth'
 
export function SignupForm() {
  return (
    <form action={signup}>
      <div>
        <label htmlFor="name">Name</label>
        <input id="name" name="name" placeholder="Name" />
      </div>
      <div>
        <label htmlFor="email">Email</label>
        <input id="email" name="email" type="email" placeholder="Email" />
      </div>
      <div>
        <label htmlFor="password">Password</label>
        <input id="password" name="password" type="password" />
      </div>
      <button type="submit">Sign Up</button>
    </form>
  )
}
```

app/actions/auth.ts

TypeScript

JavaScriptTypeScript

```
export async function signup(formData: FormData) {}
```

#### 2\. Validate form fields on the server[](#2-validate-form-fields-on-the-server)

Use the Server Action to validate the form fields on the server. If your authentication provider doesn't provide form validation, you can use a schema validation library like [Zod](https://zod.dev/) or [Yup](https://github.com/jquense/yup).

Using Zod as an example, you can define a form schema with appropriate error messages:

app/lib/definitions.ts

TypeScript

JavaScriptTypeScript

```
import * as z from 'zod'
 
export const SignupFormSchema = z.object({
  name: z
    .string()
    .min(2, { error: 'Name must be at least 2 characters long.' })
    .trim(),
  email: z.email({ error: 'Please enter a valid email.' }).trim(),
  password: z
    .string()
    .min(8, { error: 'Be at least 8 characters long' })
    .regex(/[a-zA-Z]/, { error: 'Contain at least one letter.' })
    .regex(/[0-9]/, { error: 'Contain at least one number.' })
    .regex(/[^a-zA-Z0-9]/, {
      error: 'Contain at least one special character.',
    })
    .trim(),
})
 
export type FormState =
  | {
      errors?: {
        name?: string[]
        email?: string[]
        password?: string[]
      }
      message?: string
    }
  | undefined
```

To prevent unnecessary calls to your authentication provider's API or database, you can `return` early in the Server Action if any form fields do not match the defined schema.

app/actions/auth.ts

TypeScript

JavaScriptTypeScript

```
import { SignupFormSchema, FormState } from '@/app/lib/definitions'
 
export async function signup(state: FormState, formData: FormData) {
  // Validate form fields
  const validatedFields = SignupFormSchema.safeParse({
    name: formData.get('name'),
    email: formData.get('email'),
    password: formData.get('password'),
  })
 
  // If any form fields are invalid, return early
  if (!validatedFields.success) {
    return {
      errors: validatedFields.error.flatten().fieldErrors,
    }
  }
 
  // Call the provider or db to create a user...
}
```

Back in your `<SignupForm />`, you can use React's `useActionState` hook to display validation errors while the form is submitting:

app/ui/signup-form.tsx

TypeScript

JavaScriptTypeScript

```
'use client'
 
import { signup } from '@/app/actions/auth'
import { useActionState } from 'react'
 
export default function SignupForm() {
  const [state, action, pending] = useActionState(signup, undefined)
 
  return (
    <form action={action}>
      <div>
        <label htmlFor="name">Name</label>
        <input id="name" name="name" placeholder="Name" />
      </div>
      {state?.errors?.name && <p>{state.errors.name}</p>}
 
      <div>
        <label htmlFor="email">Email</label>
        <input id="email" name="email" placeholder="Email" />
      </div>
      {state?.errors?.email && <p>{state.errors.email}</p>}
 
      <div>
        <label htmlFor="password">Password</label>
        <input id="password" name="password" type="password" />
      </div>
      {state?.errors?.password && (
        <div>
          <p>Password must:</p>
          <ul>
            {state.errors.password.map((error) => (
              <li key={error}>- {error}</li>
            ))}
          </ul>
        </div>
      )}
      <button disabled={pending} type="submit">
        Sign Up
      </button>
    </form>
  )
}
```

> **Good to know:**
> 
> *   In React 19, `useFormStatus` includes additional keys on the returned object, like data, method, and action. If you are not using React 19, only the `pending` key is available.
> *   Before mutating data, you should always ensure a user is also authorized to perform the action. See [Authentication and Authorization](#authorization).

#### 3\. Create a user or check user credentials[](#3-create-a-user-or-check-user-credentials)

After validating form fields, you can create a new user account or check if the user exists by calling your authentication provider's API or database.

Continuing from the previous example:

app/actions/auth.tsx

TypeScript

JavaScriptTypeScript

```
export async function signup(state: FormState, formData: FormData) {
  // 1. Validate form fields
  // ...
 
  // 2. Prepare data for insertion into database
  const { name, email, password } = validatedFields.data
  // e.g. Hash the user's password before storing it
  const hashedPassword = await bcrypt.hash(password, 10)
 
  // 3. Insert the user into the database or call an Auth Library's API
  const data = await db
    .insert(users)
    .values({
      name,
      email,
      password: hashedPassword,
    })
    .returning({ id: users.id })
 
  const user = data[0]
 
  if (!user) {
    return {
      message: 'An error occurred while creating your account.',
    }
  }
 
  // TODO:
  // 4. Create user session
  // 5. Redirect user
}
```

After successfully creating the user account or verifying the user credentials, you can create a session to manage the user's auth state. Depending on your session management strategy, the session can be stored in a cookie or database, or both. Continue to the [Session Management](#session-management) section to learn more.

> **Tips:**
> 
> *   The example above is verbose since it breaks down the authentication steps for the purpose of education. This highlights that implementing your own secure solution can quickly become complex. Consider using an [Auth Library](#auth-libraries) to simplify the process.
> *   To improve the user experience, you may want to check for duplicate emails or usernames earlier in the registration flow. For example, as the user types in a username or the input field loses focus. This can help prevent unnecessary form submissions and provide immediate feedback to the user. You can debounce requests with libraries such as [use-debounce](https://www.npmjs.com/package/use-debounce) to manage the frequency of these checks.

## Session Management[](#session-management)

Session management ensures that the user's authenticated state is preserved across requests. It involves creating, storing, refreshing, and deleting sessions or tokens.

There are two types of sessions:

1.  [**Stateless**](#stateless-sessions): Session data (or a token) is stored in the browser's cookies. The cookie is sent with each request, allowing the session to be verified on the server. This method is simpler, but can be less secure if not implemented correctly.
2.  [**Database**](#database-sessions): Session data is stored in a database, with the user's browser only receiving the encrypted session ID. This method is more secure, but can be complex and use more server resources.

> **Good to know:** While you can use either method, or both, we recommend using a session management library such as [iron-session](https://github.com/vvo/iron-session) or [Jose](https://github.com/panva/jose).

### Stateless Sessions[](#stateless-sessions)

To create and manage stateless sessions, there are a few steps you need to follow:

1.  Generate a secret key, which will be used to sign your session, and store it as an [environment variable](/docs/app/guides/environment-variables).
2.  Write logic to encrypt/decrypt session data using a session management library.
3.  Manage cookies using the Next.js [`cookies`](/docs/app/api-reference/functions/cookies) API.

In addition to the above, consider adding functionality to [update (or refresh)](#updating-or-refreshing-sessions) the session when the user returns to the application, and [delete](#deleting-the-session) the session when the user logs out.

> **Good to know:** Check if your [auth library](#auth-libraries) includes session management.

#### 1\. Generating a secret key[](#1-generating-a-secret-key)

There are a few ways you can generate secret key to sign your session. For example, you may choose to use the `openssl` command in your terminal:

terminal

```
openssl rand -base64 32
```

This command generates a 32-character random string that you can use as your secret key and store in your [environment variables file](/docs/app/guides/environment-variables):

.env

```
SESSION_SECRET=your_secret_key
```

You can then reference this key in your session management logic:

app/lib/session.js

```
const secretKey = process.env.SESSION_SECRET
```

#### 2\. Encrypting and decrypting sessions[](#2-encrypting-and-decrypting-sessions)

Next, you can use your preferred [session management library](#session-management-libraries) to encrypt and decrypt sessions. Continuing from the previous example, we'll use [Jose](https://www.npmjs.com/package/jose) (compatible with the [Edge Runtime](/docs/app/api-reference/edge)) and React's [`server-only`](https://www.npmjs.com/package/server-only) package to ensure that your session management logic is only executed on the server.

app/lib/session.ts

TypeScript

JavaScriptTypeScript

```
import 'server-only'
import { SignJWT, jwtVerify } from 'jose'
import { SessionPayload } from '@/app/lib/definitions'
 
const secretKey = process.env.SESSION_SECRET
const encodedKey = new TextEncoder().encode(secretKey)
 
export async function encrypt(payload: SessionPayload) {
  return new SignJWT(payload)
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('7d')
    .sign(encodedKey)
}
 
export async function decrypt(session: string | undefined = '') {
  try {
    const { payload } = await jwtVerify(session, encodedKey, {
      algorithms: ['HS256'],
    })
    return payload
  } catch (error) {
    console.log('Failed to verify session')
  }
}
```

> **Tips**:
> 
> *   The payload should contain the **minimum**, unique user data that'll be used in subsequent requests, such as the user's ID, role, etc. It should not contain personally identifiable information like phone number, email address, credit card information, etc, or sensitive data like passwords.

#### 3\. Setting cookies (recommended options)[](#3-setting-cookies-recommended-options)

To store the session in a cookie, use the Next.js [`cookies`](/docs/app/api-reference/functions/cookies) API. The cookie should be set on the server, and include the recommended options:

*   **HttpOnly**: Prevents client-side JavaScript from accessing the cookie.
*   **Secure**: Use https to send the cookie.
*   **SameSite**: Specify whether the cookie can be sent with cross-site requests.
*   **Max-Age or Expires**: Delete the cookie after a certain period.
*   **Path**: Define the URL path for the cookie.

Please refer to [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies) for more information on each of these options.

app/lib/session.ts

TypeScript

JavaScriptTypeScript

```
import 'server-only'
import { cookies } from 'next/headers'
 
export async function createSession(userId: string) {
  const expiresAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
  const session = await encrypt({ userId, expiresAt })
  const cookieStore = await cookies()
 
  cookieStore.set('session', session, {
    httpOnly: true,
    secure: true,
    expires: expiresAt,
    sameSite: 'lax',
    path: '/',
  })
}
```

Back in your Server Action, you can invoke the `createSession()` function, and use the [`redirect()`](/docs/app/guides/redirecting) API to redirect the user to the appropriate page:

app/actions/auth.ts

TypeScript

JavaScriptTypeScript

```
import { createSession } from '@/app/lib/session'
 
export async function signup(state: FormState, formData: FormData) {
  // Previous steps:
  // 1. Validate form fields
  // 2. Prepare data for insertion into database
  // 3. Insert the user into the database or call an Library API
 
  // Current steps:
  // 4. Create user session
  await createSession(user.id)
  // 5. Redirect user
  redirect('/profile')
}
```

> **Tips**:
> 
> *   **Cookies should be set on the server** to prevent client-side tampering.
> *   🎥 Watch: Learn more about stateless sessions and authentication with Next.js → [YouTube (11 minutes)](https://www.youtube.com/watch?v=DJvM2lSPn6w).

#### Updating (or refreshing) sessions[](#updating-or-refreshing-sessions)

You can also extend the session's expiration time. This is useful for keeping the user logged in after they access the application again. For example:

app/lib/session.ts

TypeScript

JavaScriptTypeScript

```
import 'server-only'
import { cookies } from 'next/headers'
import { decrypt } from '@/app/lib/session'
 
export async function updateSession() {
  const session = (await cookies()).get('session')?.value
  const payload = await decrypt(session)
 
  if (!session || !payload) {
    return null
  }
 
  const expires = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
 
  const cookieStore = await cookies()
  cookieStore.set('session', session, {
    httpOnly: true,
    secure: true,
    expires: expires,
    sameSite: 'lax',
    path: '/',
  })
}
```

> **Tip:** Check if your auth library supports refresh tokens, which can be used to extend the user's session.

#### Deleting the session[](#deleting-the-session)

To delete the session, you can delete the cookie:

app/lib/session.ts

TypeScript

JavaScriptTypeScript

```
import 'server-only'
import { cookies } from 'next/headers'
 
export async function deleteSession() {
  const cookieStore = await cookies()
  cookieStore.delete('session')
}
```

Then you can reuse the `deleteSession()` function in your application, for example, on logout:

app/actions/auth.ts

TypeScript

JavaScriptTypeScript

```
import { cookies } from 'next/headers'
import { deleteSession } from '@/app/lib/session'
 
export async function logout() {
  await deleteSession()
  redirect('/login')
}
```

### Database Sessions[](#database-sessions)

To create and manage database sessions, you'll need to follow these steps:

1.  Create a table in your database to store session and data (or check if your Auth Library handles this).
2.  Implement functionality to insert, update, and delete sessions
3.  Encrypt the session ID before storing it in the user's browser, and ensure the database and cookie stay in sync (this is optional, but recommended for optimistic auth checks in [Proxy](#optimistic-checks-with-proxy-optional)).

For example:

app/lib/session.ts

TypeScript

JavaScriptTypeScript

```
import cookies from 'next/headers'
import { db } from '@/app/lib/db'
import { encrypt } from '@/app/lib/session'
 
export async function createSession(id: number) {
  const expiresAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
 
  // 1. Create a session in the database
  const data = await db
    .insert(sessions)
    .values({
      userId: id,
      expiresAt,
    })
    // Return the session ID
    .returning({ id: sessions.id })
 
  const sessionId = data[0].id
 
  // 2. Encrypt the session ID
  const session = await encrypt({ sessionId, expiresAt })
 
  // 3. Store the session in cookies for optimistic auth checks
  const cookieStore = await cookies()
  cookieStore.set('session', session, {
    httpOnly: true,
    secure: true,
    expires: expiresAt,
    sameSite: 'lax',
    path: '/',
  })
}
```

> **Tips**:
> 
> *   For faster access, you may consider adding server caching for the lifetime of the session. You can also keep the session data in your primary database, and combine data requests to reduce the number of queries.
> *   You may opt to use database sessions for more advanced use cases, such as keeping track of the last time a user logged in, or number of active devices, or give users the ability to log out of all devices.

After implementing session management, you'll need to add authorization logic to control what users can access and do within your application. Continue to the [Authorization](#authorization) section to learn more.

## Authorization[](#authorization)

Once a user is authenticated and a session is created, you can implement authorization to control what the user can access and do within your application.

There are two main types of authorization checks:

1.  **Optimistic**: Checks if the user is authorized to access a route or perform an action using the session data stored in the cookie. These checks are useful for quick operations, such as showing/hiding UI elements or redirecting users based on permissions or roles.
2.  **Secure**: Checks if the user is authorized to access a route or perform an action using the session data stored in the database. These checks are more secure and are used for operations that require access to sensitive data or actions.

For both cases, we recommend:

*   Creating a [Data Access Layer](#creating-a-data-access-layer-dal) to centralize your authorization logic
*   Using [Data Transfer Objects (DTO)](#using-data-transfer-objects-dto) to only return the necessary data
*   Optionally use [Proxy](#optimistic-checks-with-proxy-optional) to perform optimistic checks.

### Optimistic checks with Proxy (Optional)[](#optimistic-checks-with-proxy-optional)

There are some cases where you may want to use [Proxy](/docs/app/api-reference/file-conventions/proxy) and redirect users based on permissions:

*   To perform optimistic checks. Since Proxy runs on every route, it's a good way to centralize redirect logic and pre-filter unauthorized users.
*   To protect static routes that share data between users (e.g. content behind a paywall).

However, since Proxy runs on every route, including [prefetched](/docs/app/getting-started/linking-and-navigating#prefetching) routes, it's important to only read the session from the cookie (optimistic checks), and avoid database checks to prevent performance issues.

For example:

proxy.ts

TypeScript

JavaScriptTypeScript

```
import { NextRequest, NextResponse } from 'next/server'
import { decrypt } from '@/app/lib/session'
import { cookies } from 'next/headers'
 
// 1. Specify protected and public routes
const protectedRoutes = ['/dashboard']
const publicRoutes = ['/login', '/signup', '/']
 
export default async function proxy(req: NextRequest) {
  // 2. Check if the current route is protected or public
  const path = req.nextUrl.pathname
  const isProtectedRoute = protectedRoutes.includes(path)
  const isPublicRoute = publicRoutes.includes(path)
 
  // 3. Decrypt the session from the cookie
  const cookie = (await cookies()).get('session')?.value
  const session = await decrypt(cookie)
 
  // 4. Redirect to /login if the user is not authenticated
  if (isProtectedRoute && !session?.userId) {
    return NextResponse.redirect(new URL('/login', req.nextUrl))
  }
 
  // 5. Redirect to /dashboard if the user is authenticated
  if (
    isPublicRoute &&
    session?.userId &&
    !req.nextUrl.pathname.startsWith('/dashboard')
  ) {
    return NextResponse.redirect(new URL('/dashboard', req.nextUrl))
  }
 
  return NextResponse.next()
}
 
// Routes Proxy should not run on
export const config = {
  matcher: ['/((?!api|_next/static|_next/image|.*\\.png$).*)'],
}
```

While Proxy can be useful for initial checks, it should not be your only line of defense in protecting your data. The majority of security checks should be performed as close as possible to your data source, see [Data Access Layer](#creating-a-data-access-layer-dal) for more information.

> **Tips**:
> 
> *   In Proxy, you can also read cookies using `req.cookies.get('session').value`.
> *   Proxy uses the Node.js runtime, check if your Auth library and session management library are compatible. You may need to use [Middleware](https://github.com/vercel/next.js/blob/v15.5.6/docs/01-app/03-api-reference/03-file-conventions/middleware.mdx) if your Auth library only supports [Edge Runtime](/docs/app/api-reference/edge)
> *   You can use the `matcher` property in the Proxy to specify which routes Proxy should run on. Although, for auth, it's recommended Proxy runs on all routes.

### Creating a Data Access Layer (DAL)[](#creating-a-data-access-layer-dal)

We recommend creating a DAL to centralize your data requests and authorization logic.

The DAL should include a function that verifies the user's session as they interact with your application. At the very least, the function should check if the session is valid, then redirect or return the user information needed to make further requests.

For example, create a separate file for your DAL that includes a `verifySession()` function. Then use React's [cache](https://react.dev/reference/react/cache) API to memoize the return value of the function during a React render pass:

app/lib/dal.ts

TypeScript

JavaScriptTypeScript

```
import 'server-only'
 
import { cookies } from 'next/headers'
import { decrypt } from '@/app/lib/session'
 
export const verifySession = cache(async () => {
  const cookie = (await cookies()).get('session')?.value
  const session = await decrypt(cookie)
 
  if (!session?.userId) {
    redirect('/login')
  }
 
  return { isAuth: true, userId: session.userId }
})
```

You can then invoke the `verifySession()` function in your data requests, Server Actions, Route Handlers:

app/lib/dal.ts

TypeScript

JavaScriptTypeScript

```
export const getUser = cache(async () => {
  const session = await verifySession()
  if (!session) return null
 
  try {
    const data = await db.query.users.findMany({
      where: eq(users.id, session.userId),
      // Explicitly return the columns you need rather than the whole user object
      columns: {
        id: true,
        name: true,
        email: true,
      },
    })
 
    const user = data[0]
 
    return user
  } catch (error) {
    console.log('Failed to fetch user')
    return null
  }
})
```

> **Tip**:
> 
> *   A DAL can be used to protect data fetched at request time. However, for static routes that share data between users, data will be fetched at build time and not at request time. Use [Proxy](#optimistic-checks-with-proxy-optional) to protect static routes.
> *   For secure checks, you can check if the session is valid by comparing the session ID with your database. Use React's [cache](https://react.dev/reference/react/cache) function to avoid unnecessary duplicate requests to the database during a render pass.
> *   You may wish to consolidate related data requests in a JavaScript class that runs `verifySession()` before any methods.

### Using Data Transfer Objects (DTO)[](#using-data-transfer-objects-dto)

When retrieving data, it's recommended you return only the necessary data that will be used in your application, and not entire objects. For example, if you're fetching user data, you might only return the user's ID and name, rather than the entire user object which could contain passwords, phone numbers, etc.

However, if you have no control over the returned data structure, or are working in a team where you want to avoid whole objects being passed to the client, you can use strategies such as specifying what fields are safe to be exposed to the client.

app/lib/dto.ts

TypeScript

JavaScriptTypeScript

```
import 'server-only'
import { getUser } from '@/app/lib/dal'
 
function canSeeUsername(viewer: User) {
  return true
}
 
function canSeePhoneNumber(viewer: User, team: string) {
  return viewer.isAdmin || team === viewer.team
}
 
export async function getProfileDTO(slug: string) {
  const data = await db.query.users.findMany({
    where: eq(users.slug, slug),
    // Return specific columns here
  })
  const user = data[0]
 
  const currentUser = await getUser(user.id)
 
  // Or return only what's specific to the query here
  return {
    username: canSeeUsername(currentUser) ? user.username : null,
    phonenumber: canSeePhoneNumber(currentUser, user.team)
      ? user.phonenumber
      : null,
  }
}
```

By centralizing your data requests and authorization logic in a DAL and using DTOs, you can ensure that all data requests are secure and consistent, making it easier to maintain, audit, and debug as your application scales.

> **Good to know**:
> 
> *   There are a couple of different ways you can define a DTO, from using `toJSON()`, to individual functions like the example above, or JS classes. Since these are JavaScript patterns and not a React or Next.js feature, we recommend doing some research to find the best pattern for your application.
> *   Learn more about security best practices in our [Security in Next.js article](/blog/security-nextjs-server-components-actions).

### Server Components[](#server-components)

Auth check in [Server Components](/docs/app/getting-started/server-and-client-components) are useful for role-based access. For example, to conditionally render components based on the user's role:

app/dashboard/page.tsx

TypeScript

JavaScriptTypeScript

```
import { verifySession } from '@/app/lib/dal'
 
export default async function Dashboard() {
  const session = await verifySession()
  const userRole = session?.user?.role // Assuming 'role' is part of the session object
 
  if (userRole === 'admin') {
    return <AdminDashboard />
  } else if (userRole === 'user') {
    return <UserDashboard />
  } else {
    redirect('/login')
  }
}
```

In the example, we use the `verifySession()` function from our DAL to check for 'admin', 'user', and unauthorized roles. This pattern ensures that each user interacts only with components appropriate to their role.

### Layouts and auth checks[](#layouts-and-auth-checks)

Due to [Partial Rendering](/docs/app/getting-started/linking-and-navigating#client-side-transitions), be cautious when doing checks in [Layouts](/docs/app/api-reference/file-conventions/layout) as these don't re-render on navigation, meaning the user session won't be checked on every route change.

Instead, you should do the checks close to your data source or the component that'll be conditionally rendered.

For example, consider a shared layout that fetches the user data and displays the user image in a nav. Instead of doing the auth check in the layout, you should fetch the user data (`getUser()`) in the layout and do the auth check in your DAL.

This guarantees that wherever `getUser()` is called within your application, the auth check is performed, and prevents developers forgetting to check the user is authorized to access the data.

#### Auth checks in page components[](#auth-checks-in-page-components)

For example, in a dashboard page, you can verify the user session and fetch the user data:

app/dashboard/page.tsx

TypeScript

JavaScriptTypeScript

```
import { verifySession } from '@/app/lib/dal'
 
export default async function DashboardPage() {
  const session = await verifySession()
 
  // Fetch user-specific data from your database or data source
  const user = await getUserData(session.userId)
 
  return (
    <div>
      <h1>Welcome, {user.name}</h1>
      {/* Dashboard content */}
    </div>
  )
}
```

#### Auth checks in leaf components[](#auth-checks-in-leaf-components)

You can also perform auth checks in leaf components that conditionally render UI elements based on user permissions. For example, a component that displays admin-only actions:

app/ui/admin-actions.tsx

TypeScript

JavaScriptTypeScript

```
import { verifySession } from '@/app/lib/dal'
 
export default async function AdminActions() {
  const session = await verifySession()
  const userRole = session?.user?.role
 
  if (userRole !== 'admin') {
    return null
  }
 
  return (
    <div>
      <button>Delete User</button>
      <button>Edit Settings</button>
    </div>
  )
}
```

This pattern allows you to show or hide UI elements based on user permissions while ensuring the auth check happens at render time in each component.

> **Good to know:**
> 
> *   A common pattern in SPAs is to `return null` in a layout or a top-level component if a user is not authorized. This pattern is **not recommended** since Next.js applications have multiple entry points, which will not prevent nested route segments and Server Actions from being accessed.
> *   Ensure that any Server Actions called from these components also perform their own authorization checks, as client-side UI restrictions alone are not sufficient for security.

### Server Actions[](#server-actions)

Treat [Server Actions](/docs/app/getting-started/mutating-data) with the same security considerations as public-facing API endpoints, and verify if the user is allowed to perform a mutation.

In the example below, we check the user's role before allowing the action to proceed:

app/lib/actions.ts

TypeScript

JavaScriptTypeScript

```
'use server'
import { verifySession } from '@/app/lib/dal'
 
export async function serverAction(formData: FormData) {
  const session = await verifySession()
  const userRole = session?.user?.role
 
  // Return early if user is not authorized to perform the action
  if (userRole !== 'admin') {
    return null
  }
 
  // Proceed with the action for authorized users
}
```

### Route Handlers[](#route-handlers)

Treat [Route Handlers](/docs/app/api-reference/file-conventions/route) with the same security considerations as public-facing API endpoints, and verify if the user is allowed to access the Route Handler.

For example:

app/api/route.ts

TypeScript

JavaScriptTypeScript

```
import { verifySession } from '@/app/lib/dal'
 
export async function GET() {
  // User authentication and role verification
  const session = await verifySession()
 
  // Check if the user is authenticated
  if (!session) {
    // User is not authenticated
    return new Response(null, { status: 401 })
  }
 
  // Check if the user has the 'admin' role
  if (session.user.role !== 'admin') {
    // User is authenticated but does not have the right permissions
    return new Response(null, { status: 403 })
  }
 
  // Continue for authorized users
}
```

The example above demonstrates a Route Handler with a two-tier security check. It first checks for an active session, and then verifies if the logged-in user is an 'admin'.

## Context Providers[](#context-providers)

Using context providers for auth works due to [interleaving](/docs/app/getting-started/server-and-client-components#interleaving-server-and-client-components). However, React `context` is not supported in Server Components, making them only applicable to Client Components.

This works, but any child Server Components will be rendered on the server first, and will not have access to the context provider’s session data:

app/layout.ts

TypeScript

JavaScriptTypeScript

```
import { ContextProvider } from 'auth-lib'
 
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <ContextProvider>{children}</ContextProvider>
      </body>
    </html>
  )
}
```

```
'use client';
 
import { useSession } from "auth-lib";
 
export default function Profile() {
  const { userId } = useSession();
  const { data } = useSWR(`/api/user/${userId}`, fetcher)
 
  return (
    // ...
  );
}
```

If session data is needed in Client Components (e.g. for client-side data fetching), use React’s [`taintUniqueValue`](https://react.dev/reference/react/experimental_taintUniqueValue) API to prevent sensitive session data from being exposed to the client.

## Resources[](#resources)

Now that you've learned about authentication in Next.js, here are Next.js-compatible libraries and resources to help you implement secure authentication and session management:

### Auth Libraries[](#auth-libraries)

*   [Auth0](https://auth0.com/docs/quickstart/webapp/nextjs)
*   [Better Auth](https://www.better-auth.com/docs/integrations/next)
*   [Clerk](https://clerk.com/docs/quickstarts/nextjs)
*   [Descope](https://docs.descope.com/getting-started/nextjs)
*   [Kinde](https://kinde.com/docs/developer-tools/nextjs-sdk)
*   [Logto](https://docs.logto.io/quick-starts/next-app-router)
*   [NextAuth.js](https://authjs.dev/getting-started/installation?framework=next.js)
*   [Ory](https://www.ory.sh/docs/getting-started/integrate-auth/nextjs)
*   [Stack Auth](https://docs.stack-auth.com/getting-started/setup)
*   [Supabase](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs)
*   [Stytch](https://stytch.com/docs/guides/quickstarts/nextjs)
*   [WorkOS](https://workos.com/docs/user-management/nextjs)

### Session Management Libraries[](#session-management-libraries)

*   [Iron Session](https://github.com/vvo/iron-session)
*   [Jose](https://github.com/panva/jose)

## Further Reading[](#further-reading)

To continue learning about authentication and security, check out the following resources:

*   [How to think about security in Next.js](/blog/security-nextjs-server-components-actions)
*   [Understanding XSS Attacks](https://vercel.com/guides/understanding-xss-attacks)
*   [Understanding CSRF Attacks](https://vercel.com/guides/understanding-csrf-attacks)
*   [The Copenhagen Book](https://thecopenhagenbook.com/)

[Previous

Analytics

](/docs/app/guides/analytics)

[Next

Backend for Frontend

](/docs/app/guides/backend-for-frontend)

Was this helpful?

supported.

Send
