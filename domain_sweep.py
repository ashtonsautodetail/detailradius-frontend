#!/usr/bin/env python3
"""DOMAIN-DAY SWEEP — run the moment detailradius.com is connected to Netlify.

Usage:  python3 domain_sweep.py            (defaults to https://detailradius.com)
        python3 domain_sweep.py https://www.detailradius.com   (if www is primary)

Swaps every frontend URL from the Netlify subdomain to the real domain, adds the
Organization logo to schema, regenerates city pages + sitemap (with statics), and
rebuilds the deploy zip + repo staging. Backend URLs (detailradius-backend.netlify.app)
are NOT touched — the backend keeps its own subdomain.

After running: bump sw VERSION manually if this script says so, deploy zip via
Netlify Drop, commit staged files to GitHub, and update Stripe success/cancel URLs
NOTHING here changes the backend env (SITE_URL there may need updating in Netlify
env settings if functions build absolute links).
"""
import glob, os, re, subprocess, sys

OLD = 'https://serene-cupcake-78a254.netlify.app'
NEW = (sys.argv[1] if len(sys.argv) > 1 else 'https://detailradius.com').rstrip('/')
os.chdir('/tmp/frontend')

files = (['index.html', 'links.html', 'locations.html', 'fleet.html', 'for-detailers.html',
          'privacy.html', 'terms.html', 'llms.txt', 'sitemap.xml', 'robots.txt',
          'make_city_pages.py', 'manifest.webmanifest']
         + sorted(glob.glob('mobile-detailing-*.html')))

changed = 0
for f in files:
    if not os.path.exists(f):
        print('skip (missing):', f); continue
    s = open(f).read()
    n = s.replace(OLD, NEW)
    if n != s:
        open(f, 'w').write(n); changed += 1
print(f'swapped domain in {changed} files -> {NEW}')

# Organization schema logo (idempotent)
s = open('index.html').read()
if '"logo"' not in s:
    s = s.replace('"name": "DetailRadius",\n    "url": "' + NEW + '/",',
                  '"name": "DetailRadius",\n    "url": "' + NEW + '/",\n    "logo": "' + NEW + '/icon-512.png",', 1)
    open('index.html', 'w').write(s)
    print('org logo added to schema')

# regenerate city pages with new BASE, then re-append statics + locations to sitemap
subprocess.run(['python3', 'make_city_pages.py'], check=True)
sm = open('sitemap.xml').read()
extra = ''.join(f'  <url><loc>{NEW}/{p}</loc><changefreq>monthly</changefreq><priority>0.5</priority></url>\n'
                for p in ['for-detailers.html', 'fleet.html', 'privacy.html', 'terms.html'])
extra += f'  <url><loc>{NEW}/locations.html</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>\n'
sm = sm.replace('</urlset>', extra + '</urlset>')
open('sitemap.xml', 'w').write(sm)
print('sitemap urls:', sm.count('<url>'))

# outreach docs {SITE} placeholders + hard-coded subdomain links
for doc in glob.glob('/mnt/user-data/outputs/DetailRadius-*.md'):
    s = open(doc).read()
    n = s.replace('{SITE}', NEW).replace(OLD, NEW)
    if n != s:
        open(doc, 'w').write(n); print('updated doc:', os.path.basename(doc))

# rebuild deploy zip + repo staging
zipname = '/mnt/user-data/outputs/detailradius-site.zip'
if os.path.exists(zipname): os.remove(zipname)
deploy = ['index.html', 'sw.js', 'manifest.webmanifest', 'sitemap.xml', 'robots.txt', 'llms.txt',
          'links.html', 'locations.html', 'og-image.png', 'icon-192.png', 'icon-512.png',
          'icon-512-maskable.png', 'apple-touch-icon.png', 'fleet.html', 'for-detailers.html',
          'privacy.html', 'terms.html'] + sorted(glob.glob('mobile-detailing-*.html'))
subprocess.run(['zip', '-q', zipname] + deploy, check=True)
for f in deploy + ['make_city_pages.py']:
    subprocess.run(['cp', '-f', f, '/mnt/user-data/outputs/frontend-repo/' + f])
print('zip rebuilt + repo staged.')
print('REMINDERS: 1) bump sw.js VERSION before deploying  2) Netlify Drop the zip')
print('3) commit staged files  4) verify', NEW, 'serves and old subdomain redirects')
print('5) Netlify auto-redirects the old subdomain once custom domain is primary')
