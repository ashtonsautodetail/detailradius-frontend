#!/usr/bin/env python3
"""Generate per-city SEO landing pages for DetailRadius (Netlify Drop static files)."""
import html

BASE = "https://serene-cupcake-78a254.netlify.app"

CITIES = [
    {
        "slug": "decatur", "city": "Decatur", "county": "Macon County",
        "lat": 39.8403, "lng": -88.9548,
        "areas": "Decatur, Mt. Zion, Forsyth, Argenta, Maroa, and Warrensburg",
        "blurb": "Decatur is where DetailRadius was born — our founder runs his own mobile detailing business right here. From Lake Decatur to Forsyth, get a professional detailer in your driveway without ever leaving home.",
        "faq_local": "Most Decatur bookings are mobile — the detailer comes to your home or workplace anywhere in the Decatur–Mt. Zion–Forsyth area with water and power self-supplied where needed."
    },
    {
        "slug": "springfield", "city": "Springfield", "county": "Sangamon County",
        "lat": 39.7817, "lng": -89.6501,
        "areas": "Springfield, Chatham, Rochester, Sherman, and Curran",
        "blurb": "From downtown Springfield to Chatham and Sherman, book a vetted mobile detailer who brings the shop to your driveway — upfront prices, secure deposit, no phone tag.",
        "faq_local": "Yes — detailers on DetailRadius serve the greater Springfield area including Chatham, Rochester, and Sherman, and most are fully mobile."
    },
    {
        "slug": "champaign-urbana", "city": "Champaign-Urbana", "county": "Champaign County",
        "lat": 40.1164, "lng": -88.2434,
        "areas": "Champaign, Urbana, Savoy, Mahomet, and Rantoul",
        "blurb": "Student car full of road-trip crumbs? Tailgate aftermath? Champaign-Urbana detailers on DetailRadius come to campus, your apartment, or your office — book online in minutes with upfront pricing.",
        "faq_local": "Absolutely — detailers serve UIUC campus, apartments, and offices across Champaign, Urbana, and Savoy. Book with a small deposit and pay the rest when the job's done."
    },
    {
        "slug": "bloomington-normal", "city": "Bloomington-Normal", "county": "McLean County",
        "lat": 40.4842, "lng": -88.9937,
        "areas": "Bloomington, Normal, Towanda, Downs, and Heyworth",
        "blurb": "Bloomington-Normal's easiest way to get your car detailed: pick a package, book with a deposit, and a local pro comes to you — home, office, or ISU campus.",
        "faq_local": "Yes — mobile detailers cover both Bloomington and Normal, including ISU campus and the surrounding towns."
    },
    {
        "slug": "peoria", "city": "Peoria", "county": "Peoria County",
        "lat": 40.6936, "lng": -89.5890,
        "areas": "Peoria, East Peoria, Washington, Morton, Bartonville, and Pekin",
        "blurb": "Peoria-area detailers on DetailRadius handle everything from express washes to ceramic coatings — at your home or office, with upfront pricing and secure online booking.",
        "faq_local": "Yes — detailers serve the whole Peoria metro: East Peoria, Washington, Morton, Bartonville, and Pekin."
    },
    {
        "slug": "chicago", "city": "Chicago", "county": "Cook County",
        "lat": 41.8781, "lng": -87.6298,
        "areas": "Chicago and nearby neighborhoods from Rogers Park to Hyde Park, plus Cicero and Oak Park",
        "blurb": "No garage? No hose? No problem. Chicago detailers on DetailRadius come to your street parking, garage spot, or office lot with everything self-contained — book online with upfront pricing.",
        "faq_local": "Yes — mobile detailers on DetailRadius work across Chicago neighborhoods and nearby suburbs, with self-contained water and power for street or garage detailing."
    },
    {
        "slug": "naperville-aurora", "city": "Naperville-Aurora", "county": "DuPage & Kane County",
        "lat": 41.7508, "lng": -88.1535,
        "areas": "Naperville, Aurora, Wheaton, Lisle, Warrenville, and Oswego",
        "blurb": "Naperville and Aurora's easiest way to a showroom-clean car: pick a vetted detailer, book with a secure deposit, and they handle the rest in your driveway.",
        "faq_local": "Yes — detailers cover Naperville, Aurora, Wheaton, and the surrounding western suburbs, coming to your home or workplace."
    },
    {
        "slug": "joliet", "city": "Joliet", "county": "Will County",
        "lat": 41.5250, "lng": -88.0817,
        "areas": "Joliet, Plainfield, Shorewood, Channahon, Lockport, and Romeoville",
        "blurb": "From daily drivers to semi cabs, Joliet-area detailers on DetailRadius come to you with upfront prices and secure online booking.",
        "faq_local": "Yes — mobile detailers serve Joliet and the surrounding Will County towns including Plainfield, Shorewood, and Lockport."
    },
    {
        "slug": "schaumburg", "city": "Schaumburg", "county": "Cook County (NW suburbs)",
        "lat": 42.0334, "lng": -88.0834,
        "areas": "Schaumburg, Arlington Heights, Palatine, Hoffman Estates, Elk Grove Village, and Streamwood",
        "blurb": "Northwest-suburb detailers come to your driveway or office park — pick a package, book with a deposit, done before your next meeting ends.",
        "faq_local": "Yes — detailers cover Schaumburg and the northwest suburbs including Arlington Heights, Palatine, and Hoffman Estates."
    },
    {
        "slug": "rockford", "city": "Rockford", "county": "Winnebago County",
        "lat": 42.2711, "lng": -89.0940,
        "areas": "Rockford, Loves Park, Machesney Park, Belvidere, and Roscoe",
        "blurb": "Rockford-area detailers on DetailRadius bring the full detail shop to your driveway — upfront prices from $70, secure booking, no phone tag.",
        "faq_local": "Yes — mobile detailers serve Rockford, Loves Park, Machesney Park, and nearby towns."
    },
]

PACKAGES = [
    ("Express Detail", "from $70", "Exterior hand wash, wheels & tires dressed, windows, interior vacuum & wipe-down. About 1–1.5 hrs."),
    ("Standard Detail", "from $150", "Everything in Express plus deep interior clean, shampoo spot-treatment, door jambs, full dress & shine. 2–3 hrs."),
    ("Premium Detail", "from $280", "Full interior extraction & shampoo, clay bar & machine wax, engine bay wipe-down, trim restored. Half a day."),
    ("Ceramic Coating", "from $400", "Multi-year paint protection: decontamination, machine polish, professional-grade ceramic coat."),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mobile Detailing in {city}, IL — Book Online | DetailRadius</title>
<meta name="description" content="Book trusted mobile auto detailing in {city}, Illinois. Upfront prices from $70, vetted local detailers, secure online booking — they come to your driveway. Serving {areas}.">
<link rel="canonical" href="{base}/mobile-detailing-{slug}-il.html">
<meta name="theme-color" content="#0F1116">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="icon" type="image/png" href="/icon-192.png">
<meta property="og:title" content="Mobile Detailing in {city}, IL — DetailRadius">
<meta property="og:description" content="Vetted local detailers come to you. Upfront prices, secure deposits, book in minutes.">
<meta property="og:type" content="website">
<meta property="og:url" content="{base}/mobile-detailing-{slug}-il.html">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Mobile auto detailing",
  "name": "Mobile Detailing in {city}, IL",
  "provider": {{
    "@type": "Organization",
    "name": "DetailRadius",
    "url": "{base}/"
  }},
  "areaServed": {{
    "@type": "City",
    "name": "{city}",
    "containedInPlace": {{ "@type": "AdministrativeArea", "name": "{county}, Illinois" }}
  }},
  "offers": [
    {{ "@type": "Offer", "name": "Express Detail", "price": "70", "priceCurrency": "USD" }},
    {{ "@type": "Offer", "name": "Standard Detail", "price": "150", "priceCurrency": "USD" }},
    {{ "@type": "Offer", "name": "Premium Detail", "price": "280", "priceCurrency": "USD" }},
    {{ "@type": "Offer", "name": "Ceramic Coating", "price": "400", "priceCurrency": "USD" }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "Do detailers come to me in {city}?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "{faq_local}" }}
    }},
    {{
      "@type": "Question",
      "name": "How much does mobile detailing cost in {city}, IL?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "Packages on DetailRadius start at $70 for an Express Detail, $150 for a Standard Detail, $280 for a Premium Detail, and $400 for ceramic coating. Final price depends on vehicle size and condition — every listing shows upfront pricing before you book." }}
    }},
    {{
      "@type": "Question",
      "name": "How does booking work?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "Pick a detailer, choose a service and time, and lock your spot with a small secure deposit through Stripe. You pay the balance when the job is done. Deposits protect both you and the detailer from no-shows." }}
    }}
  ]
}}
</script>
<style>
  :root {{ --navy:#0F1116; --navy2:#1A2028; --cyan:#C9CDD6; --ink:#1e293b; --muted:#556074; }}
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ font-family:'Segoe UI',system-ui,-apple-system,sans-serif; color:var(--ink); background:#f6f9ff; }}
  a {{ color:inherit; }}
  .hero {{ background:linear-gradient(150deg,#12161C 0%,#0F1116 55%,#1A2028 100%); color:#fff; padding:56px 20px 64px; text-align:center; }}
  .hero .logo {{ font-size:24px; font-weight:800; letter-spacing:-.5px; margin-bottom:26px; display:inline-flex; align-items:center; gap:9px; }}
  .hero .logo img {{ width:36px; height:36px; border-radius:8px; }}
  .hero .logo span {{ color:var(--cyan); }}
  .hero h1 {{ font-size:clamp(28px,5vw,44px); line-height:1.15; max-width:760px; margin:0 auto 14px; }}
  .hero p {{ color:#b9c6e2; max-width:640px; margin:0 auto 28px; font-size:17px; line-height:1.6; }}
  .cta {{ display:inline-block; background:linear-gradient(135deg,#F2F4F8,#B9C0CC); color:#0F1116; font-weight:800; font-size:17px; padding:15px 34px; border-radius:12px; text-decoration:none; box-shadow:0 14px 30px -8px rgba(15,17,22,.35); }}
  .cta:hover {{ filter:brightness(1.07); }}
  .badges {{ margin-top:22px; display:flex; gap:8px; justify-content:center; flex-wrap:wrap; }}
  .badge {{ font-size:12.5px; font-weight:600; background:rgba(56,189,248,.14); border:1px solid rgba(56,189,248,.32); color:#cfe4f6; padding:6px 13px; border-radius:999px; }}
  .wrap {{ max-width:960px; margin:0 auto; padding:52px 20px; }}
  h2 {{ font-size:26px; color:var(--navy); margin-bottom:10px; }}
  .sub {{ color:var(--muted); margin-bottom:26px; line-height:1.6; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(210px,1fr)); gap:16px; }}
  .card {{ background:#fff; border:1px solid #e3e9f6; border-radius:14px; padding:20px; box-shadow:0 6px 18px -10px rgba(15,32,84,.14); }}
  .card h3 {{ font-size:17px; color:var(--navy); }}
  .price {{ color:var(--cyan); font-weight:800; font-size:20px; margin:6px 0 8px; }}
  .card p {{ font-size:13.5px; color:var(--muted); line-height:1.55; }}
  .steps {{ counter-reset:s; display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:16px; }}
  .step {{ background:#fff; border:1px solid #e3e9f6; border-radius:14px; padding:20px; }}
  .step::before {{ counter-increment:s; content:"0" counter(s); font-weight:800; font-size:22px; color:var(--cyan); display:block; margin-bottom:6px; }}
  .faq {{ background:#fff; border:1px solid #e3e9f6; border-radius:14px; padding:6px 22px; }}
  .faq details {{ padding:15px 0; border-bottom:1px solid #edf1f9; }}
  .faq details:last-child {{ border-bottom:none; }}
  .faq summary {{ font-weight:700; color:var(--navy); cursor:pointer; }}
  .faq p {{ margin-top:9px; color:var(--muted); line-height:1.6; font-size:14.5px; }}
  .band {{ background:var(--navy); color:#fff; text-align:center; padding:48px 20px; }}
  .band h2 {{ color:#fff; }}
  .band p {{ color:#b9c6e2; margin:10px auto 24px; max-width:560px; line-height:1.6; }}
  footer {{ text-align:center; padding:26px 16px; font-size:13px; color:#7c8aa5; }}
  footer a {{ color:#5b7bb6; }}
</style>
</head>
<body>
<header class="hero">
  <div class="logo"><img src="/icon-192.png" alt="DetailRadius logo">Detail<span>Radius</span></div>
  <h1>Mobile Detailing in {city}, IL — Booked in Minutes</h1>
  <p>{blurb}</p>
  <a class="cta" href="/?city={slug}#find">Find a {city} Detailer →</a>
  <div class="badges">
    <span class="badge">Vetted local detailers</span>
    <span class="badge">Secure Stripe deposits</span>
    <span class="badge">They come to you</span>
    <span class="badge">Upfront pricing</span>
  </div>
</header>

<section class="wrap">
  <h2>Detailing packages &amp; prices in {city}</h2>
  <p class="sub">Real starting prices — the exact quote depends on your vehicle's size and condition, and every listing shows it upfront before you book. Serving {areas}.</p>
  <div class="grid">
    {package_cards}
  </div>
</section>

<section class="wrap" style="padding-top:0;">
  <h2>How it works</h2>
  <p class="sub">No phone tag, no "how much?" texts into the void.</p>
  <div class="steps">
    <div class="step"><strong>Pick your detailer.</strong><p class="sub" style="margin:6px 0 0;">Compare {city}-area detailers by distance, reviews, and price.</p></div>
    <div class="step"><strong>Book with a deposit.</strong><p class="sub" style="margin:6px 0 0;">Lock your time with a small secure deposit — it counts toward your total.</p></div>
    <div class="step"><strong>Sit back &amp; shine.</strong><p class="sub" style="margin:6px 0 0;">Your detailer comes to your driveway or office. Pay the balance when it's done.</p></div>
  </div>
</section>

<section class="wrap" style="padding-top:0;">
  <h2>Common questions</h2>
  <div class="faq">
    <details open><summary>Do detailers come to me in {city}?</summary><p>{faq_local}</p></details>
    <details><summary>How much does mobile detailing cost in {city}?</summary><p>Packages start at $70 (Express), $150 (Standard), $280 (Premium), and $400 (Ceramic Coating). Larger or heavily soiled vehicles may be quoted higher — always shown before you pay anything.</p></details>
    <details><summary>What if I need to cancel?</summary><p>Life happens — you can cancel your booking, and if the deposit payment was never completed the booking simply isn't confirmed. Your deposit and payment always stay protected inside DetailRadius.</p></details>
    <details><summary>I'm a detailer in {city} — can I join?</summary><p>Yes — that's the whole point. Free to join, no monthly fee, you keep 95% of every job (97% with Pro), and deposits kill no-shows. <a href="/#detailers">Become a detailer</a>.</p></details>
  </div>
</section>

<section class="wrap" style="padding-top:0;">
  <h2>Detailers serving {city} right now</h2>
  <p class="sub">Live from the DetailRadius network — updated the moment a new detailer joins.</p>
  <div id="proList" class="grid"><div style="color:#94a3b8; font-size:14px;">Checking who's nearby…</div></div>
</section>

<section class="band">
  <h2>Ready for that just-detailed feeling?</h2>
  <p>Book a trusted {city} detailer in under two minutes — upfront prices, secure payment, and they come to you.</p>
  <a class="cta" href="/?city={slug}#find">Book in {city} →</a>
</section>

<footer>© 2026 DetailRadius · <a href="/">DetailRadius home</a> · <a href="/for-detailers.html">For detailers</a> · <a href="/fleet.html">Fleet &amp; business</a> · <a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a></footer>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
  // Live detailer listing for {city} — real rows from the platform database.
  (function () {{
    var CITY_LAT = {lat}, CITY_LNG = {lng};
    var box = document.getElementById('proList');
    if (!box || !window.supabase) return;
    var sb = window.supabase.createClient(
      'https://asfqmjccfnjfrspvhnpt.supabase.co',
      'sb_publishable_pYFsa-rOViOifoGLrRSPiQ_e9-KAfd4'
    );
    function miles(lat1, lng1, lat2, lng2) {{
      var R = 3958.8, dLat = (lat2 - lat1) * Math.PI / 180, dLng = (lng2 - lng1) * Math.PI / 180;
      var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) * Math.sin(dLng / 2) * Math.sin(dLng / 2);
      return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    }}
    function esc(s) {{ return String(s == null ? '' : s).replace(/[<>&"]/g, function (c) {{ return {{'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;'}}[c]; }}); }}
    sb.from('detailers').select('id,name,price,rating,reviews,latitude,longitude,service_area,pro,featured')
      .then(function (res) {{
        var list = (res.data || []).map(function (d) {{
          d.dist = (d.latitude != null && d.longitude != null) ? miles(CITY_LAT, CITY_LNG, d.latitude, d.longitude) : null;
          return d;
        }}).filter(function (d) {{ return d.dist !== null && d.dist <= 45; }});
        list.sort(function (a, b) {{
          var f = ((b.pro || b.featured) ? 1 : 0) - ((a.pro || a.featured) ? 1 : 0);
          return f || (a.dist - b.dist);
        }});
        if (!list.length) {{
          box.innerHTML = '<div class="card" style="grid-column:1/-1; text-align:center; padding:28px;">' +
            '<h3 style="font-size:18px;">Be the first detailer in {city} 👑</h3>' +
            '<p style="margin:8px auto 14px; max-width:480px;">No detailers cover {city} yet — which means the founding spot is open. Founding detailers get featured placement, 0% platform fees on their first 10 jobs, and every booking from this page.</p>' +
            '<a class="cta" style="font-size:15px; padding:12px 26px;" href="/for-detailers.html">Claim {city} — join free →</a></div>';
          return;
        }}
        box.innerHTML = list.slice(0, 6).map(function (d) {{
          return '<div class="card">' +
            '<h3>' + esc(d.name) + ((d.pro || d.featured) ? ' <span style="font-size:11px; font-weight:800; color:#0369a1; background:#e0f2fe; padding:2px 8px; border-radius:999px; vertical-align:middle;">FEATURED</span>' : '') + '</h3>' +
            '<p style="margin:4px 0 2px;">⭐ ' + (d.rating || 'New') + ' (' + (d.reviews || 0) + ' reviews) · ' + d.dist.toFixed(1) + ' mi</p>' +
            (d.service_area ? '<p style="margin:0 0 6px;">' + esc(d.service_area) + '</p>' : '') +
            '<div class="price" style="font-size:16px;">from $' + (d.price || 70) + '</div>' +
            '<a class="cta" style="font-size:14px; padding:10px 20px; margin-top:8px; display:inline-block;" href="/?d=' + d.id + '#find">Book ' + esc((d.name || '').split(' ')[0]) + ' →</a>' +
            '</div>';
        }}).join('');
      }}, function () {{ box.innerHTML = ''; }});
  }})();
</script>
</body>
</html>
"""

card_tpl = '<div class="card"><h3>{n}</h3><div class="price">{p}</div><p>{d}</p></div>'
package_cards = "\n    ".join(card_tpl.format(n=n, p=p, d=d) for n, p, d in PACKAGES)

urls = []
for c in CITIES:
    page = TEMPLATE.format(base=BASE, package_cards=package_cards, **c)
    fn = f"/tmp/frontend/mobile-detailing-{c['slug']}-il.html"
    with open(fn, "w") as f:
        f.write(page)
    urls.append(f"{BASE}/mobile-detailing-{c['slug']}-il.html")
    print("wrote", fn, len(page), "bytes")

# Rebuild sitemap with all pages
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
      f'  <url><loc>{BASE}/</loc><lastmod>2026-07-22</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>']
for u in urls:
    sm.append(f'  <url><loc>{u}</loc><lastmod>2026-07-22</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>')
sm.append('</urlset>')
with open("/tmp/frontend/sitemap.xml", "w") as f:
    f.write("\n".join(sm) + "\n")
print("sitemap updated with", len(urls) + 1, "urls")
