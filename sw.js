/* DetailRadius service worker — v1
   Strategy: NETWORK-FIRST for everything, cache as fallback for offline.
   Never caches API traffic (Supabase / Stripe / Netlify functions), so live
   data, auth, and payments always hit the network. Bump VERSION on deploys
   that must invalidate old caches. */
const VERSION = 'dr-v29';
const OFFLINE_URLS = ['/', '/icon-192.png', '/icon-512.png', '/manifest.webmanifest'];

// Hosts that must NEVER be cached or intercepted meaningfully
const BYPASS = [
  'supabase.co', 'supabase.in',
  'stripe.com', 'stripe.network',
  'netlify.app/.netlify',          // backend functions
  'detailradius-backend',
  'tile.openstreetmap.org'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(VERSION).then((c) => c.addAll(OFFLINE_URLS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;                       // never touch POST/PUT (bookings, auth)
  const url = req.url;
  if (BYPASS.some((h) => url.includes(h))) return;        // live data straight to network

  e.respondWith(
    fetch(req)
      .then((res) => {
        // Cache good same-origin + CDN responses for offline fallback
        if (res && res.status === 200 && (res.type === 'basic' || res.type === 'cors')) {
          const copy = res.clone();
          caches.open(VERSION).then((c) => c.put(req, copy));
        }
        return res;
      })
      .catch(() =>
        caches.match(req).then((hit) => hit || (req.mode === 'navigate' ? caches.match('/') : undefined))
      )
  );
});
