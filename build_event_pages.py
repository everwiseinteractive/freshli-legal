#!/usr/bin/env python3
"""
Build static event landing pages for freshli.app/events/<slug>.

Each page serves three purposes:

  1. Universal-link FALLBACK: if the user taps the link without the app
     installed, Safari opens this page rather than 404-ing.
  2. App Review reviewer page: when Apple's reviewer tests the deep link
     in a browser before approving the IAE, they should see something
     branded that matches the event.
  3. SEO + social share preview: <meta> tags drive Twitter/iMessage rich
     previews that link to the App Store.

Each page also embeds an `apple-itunes-app` smart banner so iOS will offer
to open the link in the Freshli app if it's installed.

Run:  python3 build_event_pages.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
APP_STORE_ID = "0000000000"   # TODO: replace with the real numeric App Store ID once 1.0.1 is approved.

EVENTS = [
    {
        "slug":     "spring-pantry-reset",
        "title":    "Spring Pantry Reset",
        "tagline":  "Reset your fridge in 14 days. Master your kitchen.",
        "subhead":  "A 14-day rescue challenge. Save £25, drop 2.4 kg of CO₂, and earn the Spring Reset badge.",
        "live":     "12 – 25 May 2026",
        "accent":   "#22C55E",
        "bg_a":     "#06180D",
        "bg_b":     "#103820",
    },
    {
        "slug":     "world-environment-day",
        "title":    "World Environment Day Sprint",
        "tagline":  "One day. One rescue. One planet.",
        "subhead":  "A one-day global sprint on 5 June. Log your save and watch the live rescue wave hit one million.",
        "live":     "5 June 2026",
        "accent":   "#10B981",
        "bg_a":     "#031027",
        "bg_b":     "#062B5C",
    },
    {
        "slug":     "plastic-free-july",
        "title":    "Plastic Free July",
        "tagline":  "31 days. Zero plastic. Total mastery.",
        "subhead":  "Refuse single-use plastic, rescue every pantry item, earn the Plastic-Free Hero badge.",
        "live":     "1 – 31 July 2026",
        "accent":   "#06B6D4",
        "bg_a":     "#021A2A",
        "bg_b":     "#063855",
    },
    {
        "slug":     "bbq-saver",
        "title":    "Bank Holiday BBQ Saver",
        "tagline":  "Don't waste the feast. Share the leftovers.",
        "subhead":  "Track every BBQ leftover, list a Magic Bag, and earn bonus karma over the August Bank Holiday.",
        "live":     "22 – 31 August 2026",
        "accent":   "#F59E0B",
        "bg_a":     "#2A0F00",
        "bg_b":     "#5C2A00",
    },
    {
        "slug":     "lunch-lab",
        "title":    "Lunch Lab. Back to School.",
        "tagline":  "Pack 14 lunches in 14 minutes with Apple Intelligence.",
        "subhead":  "Apple Intelligence designs a fortnight of lunch boxes from your pantry. Auto shopping lists. Two weeks sorted.",
        "live":     "1 – 14 September 2026",
        "accent":   "#8B5CF6",
        "bg_a":     "#10082A",
        "bg_b":     "#231157",
    },
    {
        "slug":     "world-food-day",
        "title":    "World Food Day Sprint",
        "tagline":  "One day. One billion items rescued. Worldwide.",
        "subhead":  "Join Freshli's global rescue sprint on World Food Day. Log your saves. Hit one billion together.",
        "live":     "16 October 2026",
        "accent":   "#FACC15",
        "bg_a":     "#1A0E00",
        "bg_b":     "#3B2300",
    },
    {
        "slug":     "holiday-pantry-hero",
        "title":    "Holiday Pantry Hero",
        "tagline":  "Don't waste the feast. Share the love. Earn 2x karma.",
        "subhead":  "Holidays = 5x food waste. Track every leftover, share surplus with neighbours, become a Hero.",
        "live":     "18 – 31 December 2026",
        "accent":   "#DC2626",
        "bg_a":     "#1F0508",
        "bg_b":     "#4A0E16",
    },
]


def page_html(e: dict) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{e['title']} · Freshli</title>
<meta name="description" content="{e['subhead']}">

<!-- iOS smart banner: opens the Freshli app if installed, otherwise links to the App Store. -->
<meta name="apple-itunes-app" content="app-id={APP_STORE_ID}, app-argument=freshli://events/{e['slug']}">

<!-- Open Graph / Twitter card -->
<meta property="og:title"        content="{e['title']} · Freshli">
<meta property="og:description"  content="{e['subhead']}">
<meta property="og:url"          content="https://freshli.app/events/{e['slug']}.html">
<meta property="og:type"         content="website">
<meta property="og:image"        content="https://freshli.app/events/og/{e['slug']}.png">
<meta name="twitter:card"        content="summary_large_image">
<meta name="twitter:title"       content="{e['title']} · Freshli">
<meta name="twitter:description" content="{e['subhead']}">
<meta name="twitter:image"       content="https://freshli.app/events/og/{e['slug']}.png">

<link rel="canonical" href="https://freshli.app/events/{e['slug']}.html">

<style>
  :root {{
    --accent:  {e['accent']};
    --bg-a:    {e['bg_a']};
    --bg-b:    {e['bg_b']};
  }}
  * {{ margin:0; padding:0; box-sizing:border-box; -webkit-font-smoothing: antialiased; }}
  html, body {{ min-height: 100vh; background: var(--bg-a); color: #fff;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', system-ui, sans-serif;
    line-height: 1.5;
  }}
  body {{
    background:
      radial-gradient(ellipse 90% 50% at 30% 25%, color-mix(in srgb, var(--accent) 35%, transparent) 0%, transparent 65%),
      linear-gradient(160deg, var(--bg-a) 0%, var(--bg-b) 60%, var(--bg-a) 100%);
    background-attachment: fixed;
    min-height: 100vh; padding: 64px 24px;
  }}
  .wrap {{ max-width: 720px; margin: 0 auto; }}
  .badge {{ display: inline-flex; align-items: center; gap: 12px;
    padding: 10px 22px; border-radius: 999px;
    background: rgba(255,255,255,0.10);
    border: 1.5px solid rgba(255,255,255,0.22);
    font-size: 14px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase;
    color: #fff; margin-bottom: 28px;
  }}
  .badge::before {{ content: ''; width: 10px; height: 10px; border-radius: 50%;
    background: var(--accent); box-shadow: 0 0 14px var(--accent); }}
  h1 {{ font-size: clamp(40px, 7vw, 64px); font-weight: 900; line-height: 1.05; letter-spacing: -0.025em;
    margin-bottom: 18px;
    background: linear-gradient(160deg, #FFFFFF 0%, var(--accent) 100%);
    -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
  }}
  .tag {{ font-size: clamp(20px, 3vw, 26px); font-weight: 700;
    color: rgba(255,255,255,0.92); margin-bottom: 18px; }}
  .sub {{ font-size: 17px; color: rgba(255,255,255,0.72); max-width: 580px; margin-bottom: 32px; }}
  .live {{ display: inline-block; padding: 8px 16px; border-radius: 8px;
    background: rgba(255,255,255,0.10); font-size: 14px; font-weight: 600;
    color: rgba(255,255,255,0.85); margin-bottom: 48px; }}

  .cta-row {{ display: flex; flex-wrap: wrap; gap: 14px; margin-bottom: 48px; }}
  .btn {{ display: inline-flex; align-items: center; justify-content: center;
    padding: 14px 28px; border-radius: 999px; font-size: 16px; font-weight: 700;
    text-decoration: none; transition: transform 0.15s ease;
  }}
  .btn:hover {{ transform: translateY(-1px); }}
  .btn-primary {{ background: #FFFFFF; color: var(--bg-a);
    box-shadow: 0 12px 32px rgba(0,0,0,0.35); }}
  .btn-secondary {{ background: rgba(255,255,255,0.10); color: #FFFFFF;
    border: 1.5px solid rgba(255,255,255,0.25); }}

  .why {{ padding: 28px 30px; background: rgba(255,255,255,0.06);
    border: 1.5px solid rgba(255,255,255,0.12); border-radius: 24px;
    margin-bottom: 32px; backdrop-filter: blur(20px); }}
  .why h2 {{ font-size: 14px; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--accent); margin-bottom: 12px; }}
  .why p {{ font-size: 16px; color: rgba(255,255,255,0.85); }}

  footer {{ margin-top: 64px; padding-top: 32px;
    border-top: 1px solid rgba(255,255,255,0.10);
    font-size: 14px; color: rgba(255,255,255,0.45); }}
  footer a {{ color: rgba(255,255,255,0.7); text-decoration: none; }}
  footer a:hover {{ color: #FFFFFF; }}
</style>
</head>
<body>
<main class="wrap">
  <span class="badge">Freshli In-App Event</span>
  <h1>{e['title']}</h1>
  <p class="tag">{e['tagline']}</p>
  <p class="sub">{e['subhead']}</p>
  <p class="live">Live {e['live']}</p>

  <div class="cta-row">
    <a class="btn btn-primary" href="freshli://events/{e['slug']}">Open in Freshli</a>
    <a class="btn btn-secondary" href="https://apps.apple.com/app/id{APP_STORE_ID}">Get Freshli on the App Store</a>
  </div>

  <div class="why">
    <h2>What is Freshli?</h2>
    <p>Freshli is a private, on-device food rescue companion. Track everything in your fridge, cook from what's about to expire with Apple Intelligence, and share surplus with neighbours — all from your iPhone, iPad, and Apple Watch.</p>
  </div>

  <footer>
    <a href="/">freshli.app</a> •
    <a href="/privacy-policy.html">Privacy</a> •
    <a href="/terms-of-use.html">Terms</a> •
    <a href="/support.html">Support</a>
  </footer>
</main>
</body>
</html>
"""


for e in EVENTS:
    out = HERE / f"{e['slug']}.html"
    out.write_text(page_html(e), encoding="utf-8")
    print(f"  wrote events/{e['slug']}.html ({out.stat().st_size // 1024} KB)")

print(f"\nDone. {len(EVENTS)} pages generated. Deploy by committing the freshli-legal/ folder.")
