#!/usr/bin/env python3
"""Writes the site's HTML (index, help, one page per face) from the content below. Run: python3 build.py"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
EMAIL = "watchfaces@thesako.com"

# Store page per face once it is live, e.g. "https://apps.garmin.com/apps/<app id>". None = not live yet.
STORE = {}

WATCHES = ["Venu® 4 45 mm", "Venu® 4 41 mm", "Instinct® 3 AMOLED 50 mm", "Instinct® 3 AMOLED 45 mm"]
SIZES = [("venu445mm", "Venu 4 45 mm", 454), ("venu441mm", "Venu 4 41 mm", 390),
         ("instinct3amoled50mm", "Instinct 3 AMOLED 50 mm", 416), ("instinct3amoled45mm", "Instinct 3 AMOLED 45 mm", 390)]
GENERIC = ["Original", "Cyan", "Lime", "Mono"]

FACES = [
    dict(slug="range-card", key="rangecard", name="Range Card", accent="#C2410C",
         tagline="A digital face with thirteen data slots around a big, clear time.",
         intro=["Range Card is laid out like a field data card. A light band across the top carries the date. Under the time "
                "sits a ruled grid of six cells, a small step-goal dial, a weather line with today's high and low, and a status line. "
                "Two thin gauges run up the left and right edges."],
         shows=["Time with solid hours, outlined minutes and seconds in active mode",
                "Top band: the date, or military date-time, your next calendar event, weather, training status or ISO week",
                "Status line (notifications to start with) and a weather line with the high and low",
                "Step-goal dial with a progress ring",
                "A 3 + 3 grid: heart rate, battery days, calories, floors, altitude and intensity minutes to start with",
                "Footer, sunset to start with",
                "Edge gauges with their names printed along them: Body Battery™ on the left, stress on the right"],
         change="All 13 slots can be set from your phone, and most can be left empty: activity, health, battery, weather and time data, "
                "depending on the slot and your watch.",
         themes=GENERIC, alts=[1, 2]),
    dict(slug="signal-box", key="signalbox", name="Signal Box", accent="#B91C1C",
         tagline="A retro instrument-panel face with a heart-rate dial and segment bars.",
         intro=["Signal Box borrows from old control panels: a heart-rate dial with its own ring, a date block, a wide tabular time, "
                "two labelled segment bars and a row of block gauges along the lower rim."],
         shows=["Heart-rate dial, its ring showing how close you are to your maximum heart rate",
                "Date block with the current temperature and conditions",
                "Large time with outlined minutes and seconds in active mode",
                "Two segment bars: steps and battery days left to start with",
                "Two block gauges on the rim: Body Battery™ and stress to start with",
                "Footer line, sunset to start with"],
         change="Seven slots can be changed from your phone: the dial, the weather line, both bars, both rim gauges and the footer. "
                "Most can also be switched off.",
         themes=GENERIC, alts=[1, 2]),
    dict(slug="field-kit", key="fieldkit", name="Field Kit", accent="#B45309",
         tagline="Sunrise, sunset, Body Battery™ and a large time on one screen, for days outside.",
         intro=["Field Kit was drawn for hiking and long days out. The top holds a chamfered date tag and a small ringed dial, "
                "set to Body Battery™ to start with. The time is big enough to read on the move."],
         shows=["Date tag with the day, weekday and month",
                "Ringed dial, Body Battery™ to start with",
                "Sun line with sunrise and sunset",
                "Three chamfered tiles: heart rate, steps and temperature to start with",
                "Battery gauge showing days left, percent or just the icon"],
         change="The dial, both sides of the sun line, each tile and the battery display can be changed from your phone, "
                "and most can be turned off.",
         themes=GENERIC, alts=[1, 2]),
    dict(slug="conduit", key="conduit", name="Conduit", accent="#0F766E",
         tagline="Your last four hours of heart rate as a bar chart, under a two-tone time.",
         intro=["Conduit is the technical one in the set. Your heart rate sits at the top next to a 12-bar chart of the past four hours, "
                "and angled divider lines split the face."],
         shows=["Heart rate and a 12-bar chart of the last four hours",
                "Time with outlined hours, solid accent minutes and seconds in active mode",
                "Date with the temperature or feels-like",
                "Small ringed dial, battery days left to start with",
                "Sun line with sunrise and sunset",
                "Two arc gauges rising from 6 o'clock: Body Battery™ and steps to start with"],
         change="The heart-rate chart stays put. The dial, the date line, both sides of the sun line and both arcs can be changed "
                "from your phone, and the heart-rate value, date-line value and sun line can be hidden.",
         themes=GENERIC, alts=[1, 2]),
    dict(slug="week-grid", key="weekgrid", name="Week Grid", accent="#0369A1",
         tagline="Seven days of steps in one strip, today highlighted, above a six-cell data grid.",
         intro=["The top of Week Grid is a bar for each of the last seven days, with today lit up. It shows steps, "
                "or intensity minutes or floors if you prefer."],
         shows=["Week strip of the last seven days",
                "Date with the current temperature and conditions",
                "Large time with outlined minutes and seconds in active mode",
                "A ruled 3 + 3 grid: heart rate, steps, notifications, calories, distance and floors to start with",
                "Battery with days left, percent or the icon only",
                "Two curved side gauges: Body Battery™ and stress to start with"],
         change="Both gauges, the week strip, the weather line, all six cells and the battery display can be changed from your phone. "
                "Most can be switched off.",
         themes=GENERIC, alts=[1, 2]),
    dict(slug="gold-rule", key="goldrule", name="Gold Rule", accent="#8A6116",
         tagline="A quiet, gold-accented digital face with two ruled rows of data.",
         intro=["Gold Rule is the dressier face in the set. The full date sits at the top, the time between two ruled rows of "
                "three values, with a pair of values below and two slim arcs at the sides."],
         shows=["Full date, such as TUE 14 OCTOBER",
                "Time with solid hours, gold outlined minutes and seconds in active mode",
                "Top row: heart rate, steps and battery days left to start with",
                "Bottom row: distance, temperature and intensity minutes to start with",
                "Footer pair: notifications and calories to start with",
                "Two labelled arcs: Body Battery™ and stress to start with"],
         change="All ten data slots can be changed from your phone, and most can be left empty.",
         themes=GENERIC, alts=[1, 2]),
    dict(slug="track-hybrid", key="trackhybrid", name="Track Hybrid", accent="#B45309",
         tagline="Hands over a seven-segment time, in the colours of old CRT, VFD, Nixie and LED displays.",
         intro=["Track Hybrid puts outline analog hands over a seven-segment time. Its colour presets are named after the "
                "display technology they copy. Pick one and the whole face follows."],
         shows=["Analog hands over a seven-segment time, with seconds in active mode",
                "Top field: the date, or ISO week, a second time zone, your next event, sunrise, sunset, temperature or weather",
                "Two band gauges inside the minute track, names curved along them: Body Battery™ and stress to start with",
                "Four data fields: heart rate, battery days, temperature and notifications to start with",
                "Footer, calories to start with"],
         change="Every field and gauge can be changed from your phone, and most can be switched off for a cleaner dial.",
         themes=["Amber CRT", "EL yellow-green", "Yellow mono", "VFD", "Nixie", "Red LED", "EL blue-green"], alts=[3, 4]),
    dict(slug="gauge-glass", key="gaugeglass", name="Gauge Glass", accent="#0E7490",
         tagline="Skeleton hands over an LCD time, with four glass level gauges for your data.",
         intro=["Gauge Glass mixes two kinds of watch. Skeleton hands sweep over a tick ring, and behind them sits an LCD-style "
                "panel with a seven-segment time and a 14-segment date line. Four pill-shaped gauges fill up like the level glass "
                "on a tank."],
         shows=["Skeleton hands and a seconds hand over a tick ring",
                "Seven-segment time with seconds and a 14-segment date line",
                "Four level gauges: steps (% of goal), battery days left, Body Battery™ and stress to start with"],
         change="Each gauge and the date line can show a different reading, or nothing. The gauges take readings that fill a level: "
                "steps, floors, intensity minutes, Body Battery™, stress, Pulse Ox, sleep score, battery, battery days, rain chance "
                "or solar intensity. The date line shows the date, ISO week, a second time zone or your next calendar event.",
         themes=GENERIC, alts=[1, 2]),
    dict(slug="duo-dial", key="duodial", name="Duo Dial", accent="#15803D",
         tagline="Analog hands and an LCD window on one dial, like the analog-digital sports watches of the 80s and 90s.",
         intro=["Duo Dial is an analog-digital face. The hands run over a textured dial, with a date window, two sub-dials "
                "and an LCD window with segment digits set into it."],
         shows=["Hour, minute and seconds hands over a textured dial",
                "Date window: the date, the ISO week or a second time zone",
                "Two sub-dials with a needle and value: Body Battery™ and stress to start with",
                "LCD window with the digital time, two values and status icons for Bluetooth, alarms, notifications and do not disturb",
                "Battery with days left or percent"],
         change="The sub-dials take readings that fill a scale: steps, floors, intensity minutes, Body Battery™, stress, Pulse Ox, "
                "sleep score, battery, battery days, rain chance or solar intensity. The LCD window's two values, the date window "
                "and the battery display are set from your phone too.",
         themes=["Midnight navy", "Petrol teal", "Racing green", "Anthracite slate", "Oxblood", "Chocolate", "Deep violet", "Black"],
         alts=[1, 4]),
]

COMMON = ("Also in the phone settings: 12 or 24 hour time or the watch's setting, a leading zero for 12 h, seconds on or off, "
          "the date style (TUE 14 OCT, 14 OCT TUE, TUE 10/14 or 2026-10-14), the always-on style (Rich, Minimal or Time only), "
          "units, the first day of the week and a second time zone. On a Venu 4, touch and hold a field to open the matching "
          "screen on the watch.")


def e(s):
    return escape(s, quote=True)


def page(title, desc, body, path, image="/assets/faces/duodial/hero-1440x720.jpg"):
    url = "https://watchfaces.thesako.com" + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="https://watchfaces.thesako.com{image}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/saira.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<header class="top">
  <a class="mark" href="/"><b>thesako</b> watch faces</a>
  <nav><a href="/#faces">Faces</a><a href="/help/">Help</a></nav>
</header>
<main>
{body}
</main>
<footer class="foot">
  <p>Made by thesako. Questions: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p>Not affiliated with or endorsed by Garmin. Garmin, Connect IQ, Venu, Instinct, Body Battery and D2 are trademarks of Garmin Ltd. or its subsidiaries. Set in Saira, under the <a href="/assets/fonts/OFL.txt">SIL Open Font License</a>.</p>
</footer>
</body>
</html>
"""


def store(f):
    url = STORE.get(f["slug"])
    if not url:
        return '<p class="soon">Coming soon to the Connect IQ Store. Free.</p>'
    return f'<p class="store"><a href="{e(url)}">Get {e(f["name"])} on the Connect IQ Store</a> Free.</p>'


def img(f, file):
    return f"/assets/faces/{f['key']}/{file}"


def index():
    cards = "\n".join(f"""  <li>
    <a href="/{f['slug']}/">
      <img class="dial" src="{img(f, 'venu445mm.png')}" width="454" height="454" alt="{e(f['name'])} watch face">
      <h2>{e(f['name'])}</h2>
    </a>
    <p>{e(f['tagline'])}</p>
  </li>""" for f in FACES)
    body = f"""<section class="intro">
  <h1>Watch faces for the Venu 4 and Instinct 3 AMOLED</h1>
  <p>Nine faces, free on the Connect IQ Store. Each one has a dimmed always-on view, and you choose most of what it shows from your phone.</p>
</section>
<ul class="grid" id="faces">
{cards}
</ul>"""
    return page("thesako watch faces", "Nine free watch faces for the Garmin Venu 4 and Instinct 3 AMOLED.", body, "/")


def face(f):
    themes = [0] + f["alts"]
    swatches = "\n".join(
        f'      <button type="button" data-active="{img(f, "venu445mm.png" if t == 0 else f"venu445mm-theme{t}.png")}" '
        f'aria-pressed="{"true" if t == 0 else "false"}"><img src="{img(f, "venu445mm.png" if t == 0 else f"venu445mm-theme{t}.png")}" '
        f'width="64" height="64" alt="">{e(f["themes"][t])}</button>' for t in themes)
    sizes = "\n".join(
        f'    <figure><img class="dial" src="{img(f, p + ".png")}" width="{px}" height="{px}" style="width:{px * 100 / 454:.1f}%" '
        f'alt="{e(f["name"])} on the {e(label)}"><figcaption>{e(label)}</figcaption></figure>' for p, label, px in SIZES)
    body = f"""<article class="face" style="--accent:{f['accent']}">
  <div class="show">
    <img class="dial big" id="dial" src="{img(f, 'venu445mm.png')}" width="454" height="454" alt="{e(f['name'])} watch face, active">
    <div class="mode" role="group" aria-label="Screen mode">
      <button type="button" id="active" aria-pressed="true">Active</button>
      <button type="button" id="aod" data-src="{img(f, 'venu445mm-aod.png')}" aria-pressed="false">Always-on</button>
    </div>
  </div>
  <div class="about">
    <h1>{e(f['name'])}</h1>
    <p class="lede">{e(f['tagline'])}</p>
    {store(f)}
    {''.join(f'<p>{e(p)}</p>' for p in f['intro'])}
    <div class="colours" role="group" aria-label="Colours">
{swatches}
    </div>
    <p class="note">In {len(f['themes'])} colours: {e(', '.join(f['themes']))}.</p>
  </div>
  <section class="detail">
    <h2>On the face</h2>
    <ul>{''.join(f'<li>{e(s)}</li>' for s in f['shows'])}</ul>
    <h2>What you can change</h2>
    <p>{e(f['change'])}</p>
    <p>{e(COMMON)}</p>
    <p>Settings are changed in the Connect IQ Store app or the Garmin Connect app on your phone. <a href="/help/">How settings, always-on mode and missing values work</a>.</p>
    <h2>Watches</h2>
    <p>{e(', '.join(WATCHES))}. The D2™ Air X15 runs it too.</p>
  </section>
  <section class="sizes">
    <h2>On each screen size</h2>
    <div class="row">
{sizes}
    </div>
  </section>
  <p class="back"><a href="/#faces">All faces</a></p>
</article>
<script src="/assets/face.js"></script>"""
    return page(f"{f['name']}, a watch face for Venu 4 and Instinct 3 AMOLED", f["tagline"], body, f"/{f['slug']}/",
                img(f, "hero-1440x720.jpg"))


def help_page():
    watches = "".join(f"<li>{e(w)}</li>" for w in WATCHES)
    body = f"""<article class="help">
  <h1>Help</h1>
  <p class="lede">Answers for all nine faces. If yours isn't here, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

  <h2 id="settings">Changing a face's settings</h2>
  <p>Settings live on your phone, not on the watch. Open the Connect IQ Store app or the Garmin Connect app, find the face among the watch faces installed on your watch, and open its settings. The watch picks up the changes at its next sync with the phone.</p>
  <p>The faces have no settings menu on the watch itself in this version.</p>

  <h2 id="install">Installing and switching faces</h2>
  <p>Install a face from the Connect IQ Store app on your phone, or from the store on the web. It then appears in the watch's list of watch faces, where you can select it.</p>
  <p>If a face looks wrong after an update, switch to another face and back. If that doesn't fix it, remove the face and install it again. Removing a face resets its settings.</p>

  <h2 id="missing">A field shows "--"</h2>
  <p>The watch has no value to show yet. The usual reasons:</p>
  <ul>
    <li>Weather and temperature come from the forecast your watch last synced from your phone. Without a recent sync they show "--".</li>
    <li>Your watch doesn't record that value, such as Pulse Ox, sleep score or solar intensity on some models.</li>
    <li>Nothing has been recorded yet, for example sleep score before your first night with the watch.</li>
  </ul>

  <h2 id="battery">Battery in days or percent</h2>
  <p>Battery shows the days left, such as 6D, when the watch has an estimate. It shows percent while charging, when less than a day is left, or when the watch has no estimate. Most faces let you pick percent instead.</p>

  <h2 id="always-on">Always-on mode</h2>
  <p>When the watch is set to keep the screen on, each face switches to a dimmed, simpler view when you lower your wrist. It updates once a minute and moves a few pixels now and then to protect the AMOLED screen. Seconds only show while the watch is active. Each face has three always-on styles: Rich, Minimal and Time only.</p>

  <h2 id="touch">Touch and hold</h2>
  <p>On a Venu 4, touch and hold a field to open the matching screen on the watch, such as heart rate or Body Battery. The Instinct 3 AMOLED has no touch screen, so this doesn't apply there.</p>

  <h2 id="watches">Supported watches</h2>
  <ul>{watches}<li>D2™ Air X15, which shares the Venu 4 45 mm profile</li></ul>

  <h2 id="privacy">Privacy</h2>
  <p>The faces collect nothing and send nothing; they only show data the watch already has. This site sets no cookies and runs no analytics.</p>
  <p>Health readings on the faces are for general information and not for medical use.</p>

  <h2 id="contact">Contact</h2>
  <p>Write to <a href="mailto:{EMAIL}">{EMAIL}</a>. Say which face and which watch you have, and what you see. A photo of the watch helps.</p>
</article>"""
    return page("Help: thesako watch faces", "Settings, always-on mode, missing values and contact for the thesako watch faces.", body, "/help/")


def write(rel, html):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html)


write("index.html", index())
write("help/index.html", help_page())
for f in FACES:
    write(f"{f['slug']}/index.html", face(f))
