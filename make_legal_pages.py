#!/usr/bin/env python3
"""Generate privacy.html and terms.html for DetailRadius."""
BASE = "https://serene-cupcake-78a254.netlify.app"

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | DetailRadius</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{base}/{fn}">
<meta name="theme-color" content="#0B1533">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="icon" type="image/png" href="/icon-192.png">
<style>
  :root {{ --navy:#0B1533; --cyan:#38BDF8; --ink:#1e293b; --muted:#556074; }}
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ font-family:'Segoe UI',system-ui,-apple-system,sans-serif; color:var(--ink); background:#f6f9ff; }}
  header {{ background:var(--navy); color:#fff; padding:26px 20px; }}
  header .logo {{ font-weight:800; font-size:20px; display:flex; align-items:center; gap:9px; max-width:820px; margin:0 auto; }}
  header .logo img {{ width:30px; height:30px; border-radius:7px; }}
  header .logo span {{ color:var(--cyan); }}
  header a {{ color:inherit; text-decoration:none; }}
  main {{ max-width:820px; margin:0 auto; padding:44px 20px 60px; background:#fff; }}
  h1 {{ color:var(--navy); font-size:30px; margin-bottom:6px; }}
  .updated {{ color:var(--muted); font-size:13px; margin-bottom:28px; }}
  h2 {{ color:var(--navy); font-size:19px; margin:28px 0 8px; }}
  p, li {{ line-height:1.7; font-size:15px; color:#334155; margin-bottom:10px; }}
  ul {{ padding-left:22px; }}
  footer {{ text-align:center; padding:24px 16px; font-size:13px; color:#7c8aa5; }}
  footer a {{ color:#5b7bb6; }}
</style>
</head>
<body>
<header><div class="logo"><a href="/" style="display:flex;align-items:center;gap:9px;"><img src="/icon-192.png" alt="">Detail<span>Radius</span></a></div></header>
<main>
<h1>{title}</h1>
<div class="updated">Last updated: July 22, 2026</div>
{body}
</main>
<footer>© 2026 DetailRadius · <a href="/">Home</a> · <a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a></footer>
</body>
</html>
"""

PRIVACY = """
<p>DetailRadius ("we", "us") connects customers with independent auto detailing professionals. This policy explains what information we collect, why, and what we do with it. The short version: we collect only what's needed to run bookings and payments, we never sell your data, and your card details never touch our servers.</p>

<h2>Information we collect</h2>
<ul>
  <li><strong>Booking details</strong> — your name, email, phone (optional), vehicle description, service address, and requested date/time, so your detailer can do the job.</li>
  <li><strong>Detailer account details</strong> — business name, service area, prices, photos, and login email for detailers who list on the platform.</li>
  <li><strong>Payment information</strong> — handled entirely by <a href="https://stripe.com/privacy">Stripe</a>. We never see or store your card number. Detailer payout details are likewise held by Stripe, not us.</li>
  <li><strong>Location</strong> — if you choose to share it, we use your device location once to sort detailers by distance. It is not stored or tracked.</li>
  <li><strong>Messages</strong> — chat between customers and detailers is stored so both sides have a record. To keep everyone protected, our systems automatically screen messages for contact details and off-platform payment arrangements.</li>
</ul>

<h2>How we use it</h2>
<p>To create and manage bookings, process deposits and payments, pay detailers, show reviews, prevent fraud and abuse, and (if enabled) send booking notifications. That's it. We do not sell or rent personal information to anyone.</p>

<h2>Who we share it with</h2>
<p>Only service providers required to run the platform: <strong>Stripe</strong> (payments and payouts), <strong>Supabase</strong> (secure database hosting), and <strong>Netlify</strong> (website hosting). Your booking details are shared with the detailer you book, and a detailer's public listing is visible to customers. Map tiles are loaded from OpenStreetMap.</p>

<h2>Cookies &amp; storage</h2>
<p>We use minimal browser storage to keep you signed in and remember basic preferences. We do not run third-party advertising trackers.</p>

<h2>Your choices</h2>
<p>You can request a copy of your data or ask us to delete your account and associated personal information by contacting us. Detailers can edit or remove their listing at any time from their dashboard.</p>

<h2>Children</h2>
<p>DetailRadius is not directed at children under 13, and we do not knowingly collect their information.</p>

<h2>Changes &amp; contact</h2>
<p>If this policy changes materially, we'll update this page and the date above. Questions or requests: <a href="mailto:ashtons.autodetail4@gmail.com">ashtons.autodetail4@gmail.com</a>.</p>
"""

TERMS = """
<p>Welcome to DetailRadius. These terms keep things fair for customers, detailers, and the platform. By using DetailRadius you agree to them.</p>

<h2>What DetailRadius is</h2>
<p>DetailRadius is a marketplace that connects customers with independent auto detailing professionals. Detailers on the platform are independent businesses — not our employees — and are responsible for the quality, safety, and completion of their work. We provide the booking, messaging, and payment infrastructure.</p>

<h2>Bookings &amp; deposits</h2>
<p>When you book, you pay a deposit (typically 25% of the service price) through Stripe to confirm your appointment. The deposit counts toward your total. A booking is not confirmed until the deposit payment completes. The remaining balance is due when the job is done, paid through the platform.</p>

<h2>Cancellations</h2>
<p>Plans change — cancel as early as you can so your detailer can rebook the slot. If a deposit payment was never completed, the booking simply expires. Repeated no-shows (by customers or detailers) can lead to removal from the platform.</p>

<h2>Payments stay on the platform</h2>
<p>All payments for services booked through DetailRadius must go through DetailRadius. This is what funds deposit protection, dispute support, verified reviews, and the guarantee that detailers actually get paid. Soliciting or making payment outside the platform for a booking that originated here (cash, Venmo, Zelle, etc.) violates these terms, voids any platform protection for that job, and can lead to account removal.</p>

<h2>For detailers</h2>
<p>Listing is free. DetailRadius retains a 10% platform fee on completed jobs; you keep 90%, paid out via Stripe to your connected account. You're responsible for the accuracy of your listing and prices, holding any required licenses or insurance, and performing services professionally. Fake reviews, misrepresented services, or off-platform payment steering can lead to removal.</p>

<h2>Reviews</h2>
<p>Reviews must reflect a genuine booking experience. We may remove content that is fraudulent, abusive, or unrelated to the service.</p>

<h2>Liability</h2>
<p>DetailRadius provides the marketplace "as is." To the maximum extent permitted by law, we are not liable for damage arising from services performed by independent detailers; claims about a specific job should first go through the detailer and our dispute support. Nothing in these terms limits liability that cannot lawfully be limited.</p>

<h2>Changes &amp; contact</h2>
<p>We may update these terms as the platform grows; material changes will be reflected on this page with a new date. Questions: <a href="mailto:ashtons.autodetail4@gmail.com">ashtons.autodetail4@gmail.com</a>.</p>
"""

for fn, title, desc, body in [
    ("privacy.html", "Privacy Policy", "How DetailRadius collects, uses, and protects your information.", PRIVACY),
    ("terms.html", "Terms of Service", "The terms that keep DetailRadius fair for customers and detailers.", TERMS),
]:
    with open(f"/tmp/frontend/{fn}", "w") as f:
        f.write(SHELL.format(title=title, desc=desc, fn=fn, base=BASE, body=body))
    print("wrote", fn)

# Append to sitemap
import re
sm = open("/tmp/frontend/sitemap.xml").read()
add = "".join(
    f'  <url><loc>{BASE}/{p}</loc><lastmod>2026-07-22</lastmod><changefreq>yearly</changefreq><priority>0.3</priority></url>\n'
    for p in ("privacy.html", "terms.html"))
sm = sm.replace("</urlset>", add + "</urlset>")
open("/tmp/frontend/sitemap.xml", "w").write(sm)
print("sitemap now has", sm.count("<loc>"), "urls")
