#!/usr/bin/env python3
"""Writes the site's HTML (index, help, one page per face) from the content below. Run: python3 build.py"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
EMAIL = "watchfaces@thesako.com"

# Store page per face once it is live, e.g. "https://apps.garmin.com/apps/<app id>". None = not live yet.
STORE = {   # Connect IQ Store listings, all approved 1.0.0 (2026-10-23)
    "range-card": "https://apps.garmin.com/apps/6c57c55c-b3fb-4cad-ade0-dd7f837776be",
    "signal-box": "https://apps.garmin.com/apps/9dc61c19-2285-4a63-b4bf-71d9b0b2a200",
    "field-kit": "https://apps.garmin.com/apps/f1fb15ff-639c-4b35-8d0b-65592755a69e",
    "conduit": "https://apps.garmin.com/apps/b8085dd1-800e-4def-b005-6077ea7ec815",
    "week-grid": "https://apps.garmin.com/apps/8ecffb50-8316-46db-b0dd-816a1d264cc9",
    "gold-rule": "https://apps.garmin.com/apps/fa0992ca-6094-404b-91ef-dba249592ae3",
    "track-hybrid": "https://apps.garmin.com/apps/d4b8252c-26a8-441c-8cea-15db26b29808",
    "gauge-glass": "https://apps.garmin.com/apps/72649362-53da-43d1-afdc-57e1d0586af6",
    "duo-dial": "https://apps.garmin.com/apps/36290366-f1c0-4e9e-bd33-a482f75a0fa9",
    "day-frame": "https://apps.garmin.com/apps/0681619e-a415-405e-b667-569fb2671e02",
    "split-ring": "https://apps.garmin.com/apps/e3c83ae5-2b55-486a-8385-f32e3f446126",
    "day-wheel": "https://apps.garmin.com/apps/9b67efeb-1af5-4684-85bf-ea9359fa1d5e",
    "full-tank": "https://apps.garmin.com/apps/42193442-c192-4e58-8e6b-f804b2a74985",
    "last-light": "https://apps.garmin.com/apps/8152b284-475a-43ca-a994-556e15cd8a85",
    "zone-arc": "https://apps.garmin.com/apps/4e8d4bf2-6ccb-4cca-b230-b6c11b95e6a9",
}

WATCHES = ["Venu® 4 45 mm", "Venu® 4 41 mm", "Instinct® 3 AMOLED 50 mm", "Instinct® 3 AMOLED 45 mm"]
SIZES = [("venu445mm", "Venu 4 45 mm", 454), ("venu441mm", "Venu 4 41 mm", 390),
         ("instinct3amoled50mm", "Instinct 3 AMOLED 50 mm", 416), ("instinct3amoled45mm", "Instinct 3 AMOLED 45 mm", 390)]
APPROACH_WATCHES = ["Approach® S70 47 mm", "Approach® S70 42 mm", "Approach® S72 47 mm", "Approach® S72 43 mm"]
APPROACH_SIZES = [("approachs7047mm", "Approach S70 47 mm", 454), ("approachs7042mm", "Approach S70 42 mm", 390),
                  ("approachs7247mm", "Approach S72 47 mm", 454), ("approachs7243mm", "Approach S72 43 mm", 416)]
GENERIC = ["Original", "Cyan", "Lime", "Mono"]

HYBRID_COMMON = ("Also in the phone settings: the colour and seconds on or off. The digital time follows your watch's 12 or 24 hour setting, "
                 "and units follow the watch too. On a touch watch, touch and hold a field to open the matching screen on the watch.")
ANALOG_COMMON = ("Also in the phone settings: the colour and seconds on or off. Units follow your watch's setting. "
                 "On a touch watch, touch and hold a field to open the matching screen on the watch.")

FACES = [
    dict(slug="day-frame", key="dayframe", name="Day Frame", accent="#C2410C",
         tagline="Day, date, weather and your next event on a framed analog dial with a digital time.",
         intro=["Day Frame is an analog-digital hybrid for the working day. Baton hands run over a dark dial with a minute track, "
                "with two sub-dials on either side of the centre and a digital time at 6 o'clock."],
         shows=["Hour, minute and seconds hands. The minute hand moves every second, as on a real watch",
                "Day and date windows under 12",
                "Current weather and a top line: your next calendar event to start with",
                "Two sub-dials with needles: battery days and steps to start with",
                "Digital time with seconds, a phone-connected icon and a notification bell"],
         change="The top line and both sub-dials can be changed from your phone, and each can be switched off. The top line takes your next event, "
                "sunset, sunrise, temperature, heart rate, resting heart rate, Body Battery™ or stress. The sub-dials take battery, steps, "
                "Body Battery™, stress, intensity minutes, floors or sleep score.",
         common=HYBRID_COMMON, themes=["Orange", "Amber", "Blue", "Lime"]),
    dict(slug="split-ring", key="splitring", name="Split Ring", accent="#C2410C",
         tagline="Steps and battery fill a segmented ring around analog hands and a digital time.",
         intro=["Split Ring is built around one wide segmented ring. The left half fills with steps toward your goal and the right half "
                "with battery days, with the values printed beside it."],
         shows=["Hour, minute and seconds hands over a fine patterned dial. The minute hand moves every second, as on a real watch",
                "Segmented ring: steps on the left and battery days on the right to start with",
                "Temperature with the day's high and low",
                "Digital time with seconds, a phone-connected icon and a notification bell",
                "Weekday and date, and a pill with heart rate to start with"],
         change="Each side of the ring and the bottom pill can be changed from your phone, and each can be switched off. The ring takes steps, battery, "
                "Body Battery™, stress, intensity minutes, floors or sleep score. The pill takes heart rate, resting heart rate, intensity minutes, "
                "floors, respiration or VO2 max.",
         common=HYBRID_COMMON, themes=["Orange", "Red", "Teal", "Lime"]),
    dict(slug="day-wheel", key="daywheel", name="Day Wheel", accent="#B91C1C",
         tagline="A weekday wheel, two rings and a digital time around broad rounded hands.",
         intro=["Day Wheel has a tool-watch feel. Broad rounded hands run over a dark dial, and a wheel at 3 o'clock lists the week around the date, "
                "with today marked."],
         shows=["Hour, minute and seconds hands. The minute hand moves every second, as on a real watch",
                "Weekday wheel with the date in the middle, always Monday to Sunday",
                "Two rings: steps toward your goal and Body Battery™ to start with",
                "Digital time with seconds, a phone-connected icon and a notification bell",
                "Two values below it: heart rate and battery days to start with"],
         change="Both rings and both bottom values can be changed from your phone, and each can be switched off. The rings take steps, battery, "
                "Body Battery™, stress, intensity minutes, floors or sleep score. The bottom values take heart rate, resting heart rate, distance, "
                "intensity minutes, respiration, VO2 max or battery days.",
         common=HYBRID_COMMON, themes=["Red", "Orange", "Blue", "Amber"]),
    dict(slug="full-tank", key="fulltank", name="Full Tank", accent="#B91C1C",
         tagline="A big Body Battery™ gauge beside analog hands, for seeing how much you have left today.",
         intro=["Full Tank reads like a fuel gauge. A long curved scale on the left shows Body Battery™ with a pointer, and the value sits large beside it."],
         shows=["Hour, minute and seconds hands. The minute hand moves every second, as on a real watch",
                "Curved Body Battery™ gauge with its value",
                "Weekday and date, with resting heart rate under them to start with",
                "Stress to the right of centre to start with",
                "A bottom ring that fills with steps toward your goal, with your heart rate above the count"],
         change="The line under the date, the value right of centre and the bottom ring can be changed from your phone, and each can be switched off. "
                "The two values take sunset, sunrise, temperature, resting heart rate, stress or battery days, among others. The ring takes steps, battery, "
                "stress, intensity minutes, floors, sleep score or Pulse Ox.",
         common=ANALOG_COMMON, themes=["Red", "Amber", "Teal", "Blue"]),
    dict(slug="last-light", key="lastlight", name="Last Light", accent="#B45309",
         tagline="A 24-hour sun bezel and the daylight you have left, on an olive analog dial.",
         intro=["Last Light is for planning a day outside. A 24-hour bezel shows day and night with a marker for the sun, and the dial counts down "
                "the daylight left. After sunset it counts the night instead."],
         shows=["Hour, minute and seconds hands. The minute hand moves every second, as on a real watch",
                "24-hour day and night bezel with a sun marker",
                "Daylight left and the sunset time",
                "Barometric pressure in hPa with eight hours of trend bars",
                "A sub-dial with altitude and your ascent today to start with",
                "Digital time with seconds, a phone-connected icon and a notification bell",
                "Weekday and date, and a pill with heart rate to start with"],
         change="The right sub-dial and the bottom pill can be changed from your phone, and both can be switched off. The sub-dial takes altitude, temperature, "
                "heart rate, resting heart rate, Body Battery™, stress, battery days or calories. The pill takes heart rate, resting heart rate, distance, "
                "intensity minutes, floors, Pulse Ox, respiration or VO2 max.",
         common=HYBRID_COMMON, themes=["Orange", "Amber", "Coral", "Teal"]),
    dict(slug="zone-arc", key="zonearc", name="Zone Arc", accent="#4D7C0F",
         tagline="Your heart-rate zone on a coloured arc beside analog hands and four data dials.",
         intro=["Zone Arc is for days you train. A coloured arc on the left is split into heart-rate zones 1 to 5, with a pointer showing where you are now."],
         shows=["Hour, minute and seconds hands. The minute hand moves every second, as on a real watch",
                "Heart-rate zone arc with a pointer",
                "Four small dials: Body Battery™, heart rate with its zone, the date and steps",
                "Battery days along the bottom to start with"],
         change="The top dial, the bottom dial and the bottom line can be changed from your phone, and each can be switched off. The dials take Body Battery™, "
                "battery days, stress, intensity minutes, floors, sleep score or steps. The bottom line takes battery days, sunset, sunrise, temperature, "
                "resting heart rate, Body Battery™, stress or steps.",
         common=ANALOG_COMMON, themes=["Lime", "Teal", "Amber", "Orange"]),
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
         themes=GENERIC),
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
         themes=GENERIC),
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
         themes=GENERIC),
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
         themes=GENERIC),
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
         themes=GENERIC),
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
         themes=GENERIC),
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
         themes=["Amber CRT", "EL yellow-green", "Yellow mono", "VFD", "Nixie", "Red LED", "EL blue-green"]),
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
         themes=GENERIC),
    dict(slug="duo-dial", key="duodial", name="Duo Dial", accent="#15803D",
         tagline="Analog hands and an LCD window on one dial, like the analog-digital sports watches of the 80s and 90s.",
         intro=["Duo Dial is an analog-digital face. The hands run over a textured dial, with a date window, two sub-dials "
                "and an LCD window with segment digits set into it."],
         approach=True,
         shows=["Hour, minute and seconds hands over a textured dial, open or filled. The minute hand moves every second, as on a real watch",
                "Date window: the date, the ISO week or a second time zone",
                "Two sub-dials with a needle and value: Body Battery™ and stress to start with",
                "LCD window with the digital time, two values and status icons for Bluetooth, alarms, notifications and do not disturb",
                "Battery with days left or percent"],
         change="The sub-dials take readings that fill a scale: steps, floors, intensity minutes, Body Battery™, stress, Pulse Ox, "
                "sleep score, battery, battery days, rain chance or solar intensity. The LCD window's two values, the date window "
                "and the battery display are set from your phone too, and so is the hand style, open or filled.",
         themes=["Midnight navy", "Petrol teal", "Racing green", "Anthracite slate", "Oxblood", "Chocolate", "Deep violet", "Black"]),
]

COMMON = ("Also in the phone settings: 12 or 24 hour time or the watch's setting, a leading zero for 12 h, seconds on or off, "
          "the date style (TUE 14 OCT, 14 OCT TUE, TUE 10/14 or 2026-10-14), the always-on style (Rich, Minimal or Time only), "
          "units, the first day of the week and a second time zone: pick a city and it follows daylight saving, or set your own offset. "
          "On a touch watch, touch and hold a field to open the matching screen on the watch.")


def e(s):
    return escape(s, quote=True).replace(" mm", "\u00a0mm")


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
  <p>Not affiliated with or endorsed by Garmin. Garmin, Connect IQ, Venu, Instinct, Approach, Body Battery and D2 are trademarks of Garmin Ltd. or its subsidiaries. Set in Saira, under the <a href="/assets/fonts/OFL.txt">SIL Open Font License</a>.</p>
</footer>
</body>
</html>
"""


def store(f):
    url = STORE.get(f["slug"])
    if not url:
        return '<p class="soon">Coming soon to the Connect IQ Store. Free.</p>'
    return f'<p class="store"><a class="get" href="{e(url)}">Get {e(f["name"])} on the Connect IQ Store</a> <span>Free</span></p>'


def img(f, file):
    return f"/assets/faces/{f['key']}/{file}"


def index():
    cards = "\n".join(f"""  <li>
    <a href="/{f['slug']}/">
      <img class="dial" src="{img(f, 'venu445mm.png')}" width="454" height="454" alt="{e(f['name'])} watch face">
      <h2>{e(f['name'])}</h2>
    </a>
    <p>{e(f['tagline'])}{'' if STORE.get(f['slug']) else ' Coming soon.'}</p>
  </li>""" for f in FACES)
    body = f"""<section class="intro">
  <h1>Free watch faces for Garmin watches</h1>
  <p>Fifteen faces on the Connect IQ Store. Each one has a dimmed always-on view, and you choose most of what it shows from your phone. Each face&#39;s page lists the watches it runs on.</p>
</section>
<ul class="grid" id="faces">
{cards}
</ul>"""
    return page("thesako watch faces", "Fifteen free watch faces for Garmin watches, on the Connect IQ Store.", body, "/")


def face(f):
    themes = range(len(f["themes"]))
    swatches = "\n".join(
        f'      <button type="button" data-active="{img(f, "venu445mm.png" if t == 0 else f"venu445mm-theme{t}.png")}" '
        f'aria-pressed="{"true" if t == 0 else "false"}"><img src="{img(f, "venu445mm.png" if t == 0 else f"venu445mm-theme{t}.png")}" '
        f'width="64" height="64" alt="">{" ".join(f"<span class=nw>{e(w)}</span>" if "-" in w else e(w) for w in f["themes"][t].split())}</button>' for t in themes)
    sizes = "\n".join(
        f'    <figure><img class="dial" src="{img(f, p + ".png")}" width="{px}" height="{px}" style="width:{px * 100 / 454:.1f}%" '
        f'alt="{e(f["name"])} on the {e(label)}"><figcaption>{e(label)}</figcaption></figure>' for p, label, px in SIZES + (APPROACH_SIZES if f.get("approach") else []))
    i = FACES.index(f)
    prev, nxt = FACES[i - 1], FACES[(i + 1) % len(FACES)]
    body = f"""<article class="face" style="--accent:{f['accent']}">
 <div class="head">
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
    <div class="colours" role="group" aria-label="Colours ({len(f['themes'])})">
{swatches}
    </div>
  <section class="detail">
    <h2>On the face</h2>
    <ul>{''.join(f'<li>{e(s)}</li>' for s in f['shows'])}</ul>
    <h2>What you can change</h2>
    <p>{e(f['change'])}</p>
    <p>{e(f.get('common', COMMON))}</p>
    <p>Settings are changed in the Connect IQ Store app or the Garmin Connect app on your phone. <a href="/help/">How settings, always-on mode and missing values work</a>.</p>
    <h2>Watches</h2>
    <p>{e(', '.join(WATCHES + (APPROACH_WATCHES if f.get("approach") else [])))}. The D2™ Air X15 runs it too.</p>
  </section>
  </div>
 </div>
  <section class="sizes">
    <h2>On each screen size</h2>
    <div class="row">
{sizes}
    </div>
  </section>
  <nav class="pager" aria-label="Other faces">
    <a href="/{prev['slug']}/">Previous: {e(prev['name'])}</a>
    <a href="/#faces">All faces</a>
    <a href="/{nxt['slug']}/">Next: {e(nxt['name'])}</a>
  </nav>
</article>
<script src="/assets/face.js"></script>"""
    return page(f"{f['name']}, a watch face for Venu 4{', Instinct 3 AMOLED and Approach S70 and S72' if f.get('approach') else ' and Instinct 3 AMOLED'}", f["tagline"], body, f"/{f['slug']}/",
                img(f, "hero-1440x720.jpg"))


def help_page():
    watches = "".join(f"<li>{e(w)}</li>" for w in WATCHES)
    body = f"""<article class="help">
  <h1>Help</h1>
  <p class="lede">Answers for all the faces. If yours isn't here, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

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
  <p>When the watch is set to keep the screen on, each face switches to a dimmed, simpler view when you lower your wrist. It updates once a minute and moves a few pixels now and then to protect the AMOLED screen. Seconds only show while the watch is active. Most faces have three always-on styles: Rich, Minimal and Time only. Day Frame, Split Ring, Day Wheel, Full Tank, Last Light and Zone Arc have one, with outline hands and no data.</p>

  <h2 id="touch">Touch and hold</h2>
  <p>On a Venu 4, or an Approach S70 or S72 with Duo Dial, touch and hold a field to open the matching screen on the watch, such as heart rate or Body Battery. The Instinct 3 AMOLED has no touch screen, so this doesn't apply there.</p>

  <h2 id="time-zone">Second time zone</h2>
  <p>In a face's settings, pick a city and the second time zone follows that city's daylight saving by itself. For anywhere else, choose a custom offset and a label of up to four letters. A custom offset doesn't change with daylight saving. Day Frame, Split Ring, Day Wheel, Full Tank, Last Light and Zone Arc have no second time zone.</p>

  <h2 id="watches">Supported watches</h2>
  <ul>{watches}<li>D2™ Air X15, which shares the Venu 4 45 mm profile</li></ul>
  <p>Duo Dial also runs on the Approach S70 42 mm and 47 mm and the Approach S72 43 mm and 47 mm.</p>

  <h2 id="privacy">Privacy</h2>
  <p>The faces collect nothing and send nothing; they only show data the watch already has. This site sets no cookies and runs no analytics.</p>
  <p>The store lists a "Communication &amp; Data Transmission" permission for the faces. That is the store's name for reading data other apps provide on the watch, such as the values in a field. The faces use no internet connection.</p>
  <p>Health readings on the faces are for general information and not for medical use.</p>

  <h2 id="contact">Contact</h2>
  <p>Write to <a href="mailto:{EMAIL}">{EMAIL}</a>. Say which face and which watch you have, and what you see. A photo of the watch helps.</p>
  <p>I read every email and usually reply within a few days. Fixes reach you as updates through the Connect IQ Store.</p>
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
