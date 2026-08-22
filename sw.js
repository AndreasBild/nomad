/**
 * Service Worker for Katrin Neumann (Nomad)
 * Provides offline caching and instant page loads
 */

const CACHE_NAME = 'nomad-v1';
const PRECACHE_ASSETS = [
    '/',
    '/index.html',
    '/impressum.html',
    '/datenschutz.html',
    '/site.webmanifest',
    '/css/bootstrap.min.css',
    '/css/aos.css',
    '/css/templatemo-nomad-force.css',
    '/css/katrin.css',
    '/js/bootstrap.bundle.min.js',
    '/js/aos.js',
    '/js/custom.js',
    '/images/Katrin-Neumann-Moderatorin.webp',
    '/images/Katrin-Neumann-Moderatorin-768.webp',
    '/images/Instagram_logo.png',
    '/favicon.ico',
    '/favicon-32x32.png',
    '/favicon-16x16.png',
    '/apple-touch-icon.png'
];

// 1. Install: Precache static app shell
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(PRECACHE_ASSETS);
        }).then(() => self.skipWaiting())
    );
});

// 2. Activate: Clean up previous caches
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

// 3. Fetch: Stale-While-Revalidate / Cache-First strategy
self.addEventListener('fetch', (event) => {
    // Only handle GET requests for same-origin or http/https
    if (event.request.method !== 'GET' || !event.request.url.startsWith('http')) {
        return;
    }

    event.respondWith(
        caches.match(event.request).then((cachedResponse) => {
            if (cachedResponse) {
                // Fetch in background to update cache (Stale-While-Revalidate)
                fetch(event.request).then((networkResponse) => {
                    if (networkResponse && networkResponse.status === 200) {
                        caches.open(CACHE_NAME).then((cache) => {
                            cache.put(event.request, networkResponse);
                        });
                    }
                }).catch(() => {
                    // Ignore network errors in background revalidation
                });
                return cachedResponse;
            }

            // Fallback to network
            return fetch(event.request).then((networkResponse) => {
                if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
                    return networkResponse;
                }

                const responseToCache = networkResponse.clone();
                caches.open(CACHE_NAME).then((cache) => {
                    cache.put(event.request, responseToCache);
                });

                return networkResponse;
            });
        })
    );
});
