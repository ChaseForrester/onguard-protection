#!/usr/bin/env python3
"""Generate suburb/service pages, sitemaps, and agent-readable SEO files."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape as xml_escape

ROOT = Path(__file__).resolve().parent
SITE = "https://www.ogprotection.com.au"
PHONE = "0432 893 343"
TEL = "+61432893343"
EMAIL = "admin@ogprotection.com.au"
LICENCE = "000110094"
TODAY = date.today().isoformat()
HOME_TITLE = "OnGuard Protection | Licensed & Insured Security Guards NSW"
OG_IMAGE = "assets/social/og-cover.jpg"
OG_W = 1792
OG_H = 1008
OG_ALT = (
    "OnGuard Protection — licensed and fully insured NSW security. "
    "Festival and venue control, access screening and K9 perimeter patrol. Free quote."
)
HERO_META = {
    "work-nowra": (1440, 1080, "OnGuard Protection event security officers at the Nowra Annual Rodeo, South Coast NSW"),
    "work-worrigee": (1170, 1169, "OnGuard Protection team providing licensed security at Worrigee Equestrian Common Rodeo"),
    "work-singleton": (720, 405, "OnGuard Protection venue security at the Singleton Rodeo After Party, Imperial Hotel"),
    "work-poster": (1539, 1925, "OnGuard Protection NSW coverage poster listing Sydney, Hunter Valley, Newcastle and Canberra"),
    "work-k9": (367, 411, "OnGuard Protection Class 1D dog handler standing a night static post at a NSW industrial gate"),
    "work-festival": (370, 417, "OnGuard Protection Class 1A officers running crowd control on a live NSW festival barrier"),
    "work-screening": (368, 415, "OnGuard Protection officer conducting a bag search at a licensed NSW event entry"),
    "work-patrol": (1328, 1416, "OnGuard Protection marked patrol ute on a night mobile patrol outside a NSW chemist"),
    "work-tiguan": (890, 795, "OnGuard Protection marked VW Tiguan patrol vehicle, plates OGPROT, Master Licence 000110094"),
}
INDEX_ROBOTS = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
NOINDEX_ROBOTS = "noindex, follow"
GA_MEASUREMENT_ID = "G-BCCYLJFLXP"
GTAG = f'''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_MEASUREMENT_ID}');
</script>'''

SERVICES = [
    {
        "slug": "crowd-control",
        "name": "Crowd Control & Venue Security",
        "short": "Crowd control",
        "h1": "Licensed crowd control and venue security in NSW",
        "title": "Crowd Control & Venue Security NSW | OnGuard Protection",
        "description": "SLED-licensed crowd control for pubs, clubs, rodeos and functions across Sydney, the Hunter and Canberra. Master Licence 000110094.",
        "keyword": "crowd control NSW",
        "img": "industry-hospitality",
        "img_w": 1600,
        "img_h": 900,
        "alt": "Night entrance of a NSW licensed venue — the door OnGuard crowd controllers hold",
        "lead": "Entry, floor and close-out covered by licensed controllers who keep venues open and incidents closed.",
        "body": "OnGuard Protection deploys SLED-licensed crowd controllers for hotels, RSLs, festivals, rodeos and private functions. We brief the door, hold the floor and close the night without turning your venue into a fight. Radio comms, incident logs and a visible uniformed presence are standard.",
        "bullets": [
            "Class 1A security officers for licensed venues and crowd control",
            "Door, ID, RSA support and ejection protocols",
            "Festival, rodeo and private-function deployments",
            "Incident reporting that stands up after the shift",
        ],
        "faq": [
            ("Do I need licensed crowd controllers in NSW?", "Yes. Crowd control is a defined security activity under the Security Industry Act 1997 (NSW). OnGuard holds Master Licence 000110094 and only deploys licensed operatives."),
            ("Can you cover a last-minute venue shift?", "Short-notice cover is available across the Sydney–Hunter–South Coast–Canberra spine. Call 0432 893 343 and we will tell you the same day if we can stand the post."),
        ],
    },
    {
        "slug": "event-security",
        "name": "Event Security Operations",
        "short": "Event security",
        "h1": "Event security operations across NSW and the ACT",
        "title": "Event Security NSW | Rodeos, Festivals & Venues | OnGuard",
        "description": "Event security for NSW rodeos, festivals and venues. Briefings, radio comms and licensed presence. Proven at Nowra, Worrigee and Singleton. ML 000110094.",
        "keyword": "event security NSW",
        "img": "industry-events",
        "img_w": 1600,
        "img_h": 900,
        "alt": "NSW rodeo and festival ground at dusk — the event sites OnGuard stands",
        "lead": "Full event plans — briefings, radio, medical liaison and a presence the crowd can see.",
        "body": "We have stood event security at the Nowra Annual Rodeo, Worrigee Equestrian Common and the Singleton Rodeo After Party at the Imperial Hotel. Same method every time: a written brief, licensed operators, and a radio net that actually works when the crowd peaks.",
        "bullets": [
            "Site recce and a written event security plan",
            "Stewarding, gates, back-of-house and VIP",
            "Liaison with first aid, traffic and local police",
            "Proven on South Coast and Hunter Valley events",
        ],
        "faq": [
            ("What size events can OnGuard cover?", "From hotel after-parties to record-attendance rodeos. We scale the roster to the risk, not the other way around."),
            ("Do you work with event organisers or just supply guards?", "Both. We can drop licensed bodies onto your plan or write the security plan with you."),
        ],
    },
    {
        "slug": "static-guards",
        "name": "Static Guarding & Site Security",
        "short": "Static guards",
        "h1": "Static guards and site security for NSW workplaces",
        "title": "Static Security Guards NSW | OnGuard Protection",
        "description": "Uniformed static security guards for construction, retail and commercial NSW sites. Access control that holds. Master Licence 000110094.",
        "keyword": "static security guards NSW",
        "img": "industry-construction",
        "img_w": 1600,
        "img_h": 900,
        "alt": "NSW construction compound at night — a static gate post after hours",
        "lead": "Uniformed guards on construction, retail, commercial and residential sites.",
        "body": "A static post only works if the person on it is licensed, briefed and still awake at 03:00. OnGuard stands construction gates, loading docks, retail floors and residential concierge desks across NSW. Access control, visitor logs and after-hours lockdown are the job — not extras.",
        "bullets": [
            "Day and night static posts",
            "Construction gate and compound control",
            "Retail and commercial lobby presence",
            "Visitor management and lock-up procedures",
        ],
        "faq": [
            ("Are your static guards SLED licensed?", "Yes. Every operative carries a current NSW security licence. The company Master Licence is 000110094 — check it on the SLED public register."),
            ("Can you cover a construction site after hours?", "Yes. After-hours static and alarm response are core work, including weekends and shutdown periods."),
        ],
    },
    {
        "slug": "mobile-patrols",
        "name": "Mobile Patrols & Alarm Response",
        "short": "Mobile patrols",
        "h1": "Mobile patrols and alarm response across NSW",
        "title": "Mobile Patrol Security NSW | Alarm Response | OnGuard Protection",
        "description": "Random and scheduled mobile patrols plus rapid alarm response for NSW commercial, retail and construction sites. SLED licensed. Call 0432 893 343.",
        "keyword": "mobile patrols NSW",
        "img": "industry-logistics",
        "img_w": 1600,
        "img_h": 900,
        "alt": "Floodlit NSW warehouse yard after hours — mobile patrol and alarm response ground",
        "lead": "Random and scheduled NSW patrols. Lock checks and rapid alarm response when no one else is on site.",
        "body": "Most break-ins happen after hours. OnGuard runs marked and unmarked mobile patrols with randomised timing so the pattern is not the product. Lock checks, external walks, alarm attendance and a written run-sheet after every visit.",
        "bullets": [
            "Randomised multi-visit patrols",
            "Alarm response and keyholding",
            "Construction and warehouse lock checks",
            "Digital run-sheets you can audit",
        ],
        "faq": [
            ("How many patrol visits do I need?", "That depends on the site risk, not a package name. We will recommend a visit pattern after a short brief — not sell you a number first."),
            ("Which suburbs do you patrol?", "Sydney, Hornsby, Central Coast, Newcastle, the Hunter, Southern Highlands, South Coast and into Canberra / ACT."),
        ],
    },
    {
        "slug": "corporate-security",
        "name": "Corporate Security & Concierge",
        "short": "Corporate security",
        "h1": "Corporate security and concierge for NSW offices",
        "title": "Corporate Security & Concierge NSW | OnGuard Protection",
        "description": "Front-of-house corporate security and concierge for offices, logistics and hospitality across Sydney, Parramatta, Newcastle and Canberra. Licensed and discreet.",
        "keyword": "corporate security NSW",
        "img": "industry-corporate",
        "img_w": 1600,
        "img_h": 900,
        "alt": "Sydney office lobby after hours — corporate concierge and access control",
        "lead": "Front-of-house presence that looks like hospitality and acts like security.",
        "body": "Corporate sites need someone who can greet a client and still stop an unauthorised walk-in. OnGuard places licensed concierge and corporate officers in offices, logistics hubs and hospitality foyers. Discreet, uniformed, and trained for the unexpected.",
        "bullets": [
            "Lobby concierge and access control",
            "Loading dock and contractor sign-in",
            "After-hours corporate lock-up",
            "Discreet incident handling",
        ],
        "faq": [
            ("Is concierge security actually licensed security?", "If they are controlling access or performing a defined security activity in NSW, they must be licensed. Ours are."),
            ("Can you match our building dress standard?", "Yes. We brief uniform and tone to the site — corporate, industrial or hospitality."),
        ],
    },
    {
        "slug": "asset-protection",
        "name": "Defence & Asset Protection",
        "short": "Asset protection",
        "h1": "Defence and asset protection for high-value NSW sites",
        "title": "Asset Protection & Site Defence NSW | OnGuard Protection",
        "description": "High-value plant, compounds and sensitive site protection across NSW and the ACT. Custom security when a generic guard post is not enough. ML 000110094.",
        "keyword": "asset protection security NSW",
        "img": "industry-industrial",
        "img_w": 1600,
        "img_h": 900,
        "alt": "High-value NSW industrial plant at night — layered static and patrol protection",
        "lead": "High-value plant, compounds and sensitive sites. Custom solutions, not a generic post.",
        "body": "When the asset is plant, copper, vehicles or a restricted compound, the job is prevention plus a response plan. OnGuard builds site-specific protection for construction compounds, logistics yards and sensitive facilities along the Sydney to Canberra corridor.",
        "bullets": [
            "Compound and plant protection",
            "Layered static plus patrol",
            "After-hours asset checks",
            "Tailored procedures, not a roster dump",
        ],
        "faq": [
            ("Do you cover construction compounds?", "Yes. Construction site and compound protection is a listed OnGuard service, including after-hours."),
            ("Can this be combined with patrols?", "Yes. Many high-value sites run a night static plus randomised mobile checks."),
        ],
    },
]

LOCATIONS = [
    {
        "slug": "sydney",
        "name": "Sydney",
        "state": "NSW",
        "postcode": "2000",
        "region": "Sydney CBD & inner city",
        "lat": -33.8688,
        "lng": 151.2093,
        "nearby": ["surry-hills", "chatswood", "parramatta", "hornsby"],
        "hero": "work-nowra",
        "proof": None,
        "industries": "CBD offices, late-night venues, retail strips, construction towers and waterfront events",
        "angle": "Sydney security is a density problem: more people, more doors, less room to get the brief wrong.",
        "unique": "OnGuard Protection deploys licensed guards across the Sydney CBD and inner suburbs for corporate lobbies, licensed venues, construction sites and event overlays. We treat the city as a corridor that runs north to Hornsby, west to Parramatta and south toward the Highlands — not a single postcode.",
        "need": "After-hours commercial lock-up, venue crowd control and construction gates are the three briefs we take most in Sydney.",
        "faq_local": "How fast can you get a licensed guard into the Sydney CBD?",
        "faq_ans": "For planned work we roster in advance. For short-notice Sydney cover, call 0432 893 343 — we will confirm the same day whether we can stand the post.",
    },
    {
        "slug": "surry-hills",
        "name": "Surry Hills",
        "state": "NSW",
        "postcode": "2010",
        "region": "Inner Sydney",
        "lat": -33.8832,
        "lng": 151.2110,
        "nearby": ["sydney", "parramatta", "chatswood"],
        "hero": "work-screening",
        "proof": None,
        "industries": "Hospitality, creative offices, late venues and mixed-use residential",
        "angle": "Surry Hills mixes offices, bars and apartment entries on the same block. The security brief has to hold all three.",
        "unique": "We cover Surry Hills venues and commercial sites with licensed crowd controllers and concierge-grade officers who can work a tight inner-city footprint without blocking trade.",
        "need": "Friday-night venue control, loading-dock access and residential concierge are the usual Surry Hills mix.",
        "faq_local": "Do you provide crowd control for Surry Hills venues?",
        "faq_ans": "Yes. Licensed crowd control and venue security for inner-Sydney hotels, bars and private functions, including Surry Hills.",
    },
    {
        "slug": "hornsby",
        "name": "Hornsby",
        "state": "NSW",
        "postcode": "2077",
        "region": "Upper North Shore",
        "lat": -33.7045,
        "lng": 151.0993,
        "nearby": ["chatswood", "gosford", "sydney"],
        "hero": "work-k9",
        "proof": None,
        "industries": "Retail precinct, rail interchange, commercial suites and residential communities",
        "angle": "Hornsby sits on the Sydney–Central Coast spine. Sites here need a company that already works both directions.",
        "unique": "Hornsby is named on OnGuard’s own coverage map. We run static, patrol and retail protection for the North Shore interchange and the commercial streets around it, with the same licensed standard we use in the CBD.",
        "need": "Shopping-centre and retail patrols, after-hours commercial checks and residential community access control.",
        "faq_local": "Is Hornsby inside OnGuard’s regular coverage?",
        "faq_ans": "Yes. Hornsby is a listed OnGuard coverage suburb on the Sydney to Central Coast corridor.",
    },
    {
        "slug": "chatswood",
        "name": "Chatswood",
        "state": "NSW",
        "postcode": "2067",
        "region": "Lower North Shore",
        "lat": -33.7969,
        "lng": 151.1833,
        "nearby": ["hornsby", "sydney", "parramatta"],
        "hero": "work-screening",
        "proof": None,
        "industries": "Retail malls, commercial towers and high-density residential",
        "angle": "Chatswood is a retail and office node. Loss prevention and lobby control matter more here than a rural gate.",
        "unique": "OnGuard places licensed corporate and retail officers in Chatswood for mall-adjacent sites, commercial towers and residential concierge. North Shore clients use us because we already cover Hornsby and the CBD on the same roster.",
        "need": "Retail presence, corporate concierge and after-hours tower lock-up.",
        "faq_local": "Can you cover a Chatswood office after hours?",
        "faq_ans": "Yes. Corporate lock-up, concierge and alarm response are available for Chatswood and the Lower North Shore.",
    },
    {
        "slug": "parramatta",
        "name": "Parramatta",
        "state": "NSW",
        "postcode": "2150",
        "region": "Western Sydney",
        "lat": -33.8150,
        "lng": 151.0011,
        "nearby": ["blacktown", "penrith", "sydney", "liverpool"],
        "hero": "work-k9",
        "proof": None,
        "industries": "Government offices, construction, hospitality and riverfront events",
        "angle": "Parramatta is a second CBD. The briefs look like Sydney — towers, venues, cranes — with Western Sydney travel times.",
        "unique": "OnGuard covers Parramatta commercial, construction and venue work as part of the greater Sydney deployment. Licensed static guards and crowd controllers for the civic precinct, river events and the construction pipeline around it.",
        "need": "Construction gates, corporate lobbies and event overlays in the Parramatta CBD.",
        "faq_local": "Do you supply construction security in Parramatta?",
        "faq_ans": "Yes. Static gate control and after-hours compound protection for Parramatta and Western Sydney construction sites.",
    },
    {
        "slug": "blacktown",
        "name": "Blacktown",
        "state": "NSW",
        "postcode": "2148",
        "region": "Western Sydney",
        "lat": -33.7668,
        "lng": 150.9050,
        "nearby": ["parramatta", "penrith", "liverpool"],
        "hero": "work-k9",
        "proof": None,
        "industries": "Retail, logistics, light industrial and community venues",
        "angle": "Blacktown sites are often logistics and retail — hours are long and the yard is the asset.",
        "unique": "We run mobile patrols, alarm response and static cover for Blacktown industrial and retail sites. Western Sydney clients use OnGuard when they want one licensed provider from Parramatta through to Penrith.",
        "need": "Yard patrols, retail after-hours and industrial alarm response.",
        "faq_local": "Can you patrol a Blacktown warehouse at night?",
        "faq_ans": "Yes. Randomised mobile patrols and alarm response are available across Blacktown and Western Sydney.",
    },
    {
        "slug": "penrith",
        "name": "Penrith",
        "state": "NSW",
        "postcode": "2750",
        "region": "Western Sydney",
        "lat": -33.7511,
        "lng": 150.6942,
        "nearby": ["blacktown", "parramatta", "campbelltown"],
        "hero": "work-festival",
        "proof": None,
        "industries": "Sporting venues, retail, riverside events and industrial estates",
        "angle": "Penrith pulls big crowds to sport and river events, then goes quiet around the industrial estates. Both need a roster.",
        "unique": "OnGuard covers Penrith event security and industrial static work on the western edge of Sydney. Same licensed operators we deploy toward the Highlands and the CBD.",
        "need": "Stadium and event support, industrial night static, retail patrols.",
        "faq_local": "Do you do event security in Penrith?",
        "faq_ans": "Yes. Licensed event security and crowd control for Penrith venues, sport and riverside functions.",
    },
    {
        "slug": "liverpool",
        "name": "Liverpool",
        "state": "NSW",
        "postcode": "2170",
        "region": "South-west Sydney",
        "lat": -33.9200,
        "lng": 150.9230,
        "nearby": ["campbelltown", "parramatta", "blacktown"],
        "hero": "work-k9",
        "proof": None,
        "industries": "Health precinct, retail, construction and logistics",
        "angle": "Liverpool’s growth is construction plus logistics. Gates and compounds are the product.",
        "unique": "OnGuard supplies static guards and mobile patrols for Liverpool construction, retail and warehouse sites. South-west Sydney is on our regular Sydney–Highlands corridor.",
        "need": "Construction access control, warehouse nights and retail lock-up.",
        "faq_local": "Are you licensed for Liverpool construction sites?",
        "faq_ans": "Yes. SLED-licensed static and after-hours cover for Liverpool and south-west Sydney construction.",
    },
    {
        "slug": "campbelltown",
        "name": "Campbelltown",
        "state": "NSW",
        "postcode": "2560",
        "region": "Macarthur",
        "lat": -34.0650,
        "lng": 150.8142,
        "nearby": ["liverpool", "bowral", "wollongong"],
        "hero": "work-k9",
        "proof": None,
        "industries": "Retail, residential growth corridors, light industrial",
        "angle": "Campbelltown sits between Sydney’s south-west and the Southern Highlands. One provider should cover both.",
        "unique": "We treat Campbelltown as the hinge between Western Sydney and the Highlands. Licensed patrols, static posts and venue cover for Macarthur sites that do not want a Sydney-only company.",
        "need": "Residential community access, industrial patrols and retail nights.",
        "faq_local": "Can one quote cover Campbelltown and Bowral?",
        "faq_ans": "Yes. Both sit on our Sydney–Southern Highlands–South Coast spine. Ask for a multi-site brief.",
    },
    {
        "slug": "gosford",
        "name": "Gosford",
        "state": "NSW",
        "postcode": "2250",
        "region": "Central Coast",
        "lat": -33.4267,
        "lng": 151.3417,
        "nearby": ["hornsby", "newcastle", "sydney"],
        "hero": "work-k9",
        "proof": None,
        "industries": "Hospitality, retail, waterfront events and commercial precincts",
        "angle": "The Central Coast is not a Sydney add-on. It needs a company already running Hornsby to Newcastle.",
        "unique": "OnGuard lists the Central Coast as an expansion and coverage region. Gosford is the hub: venue security, retail patrols and commercial static between the North Shore and the Hunter.",
        "need": "Hospitality crowd control, waterfront events and after-hours commercial checks.",
        "faq_local": "Do you cover the whole Central Coast or only Gosford?",
        "faq_ans": "Gosford is the hub. We take Central Coast briefs along the Hornsby–Newcastle corridor — confirm the suburb on 0432 893 343.",
    },
    {
        "slug": "newcastle",
        "name": "Newcastle",
        "state": "NSW",
        "postcode": "2300",
        "region": "Hunter",
        "lat": -32.9283,
        "lng": 151.7817,
        "nearby": ["singleton", "cessnock", "gosford"],
        "hero": "work-singleton",
        "proof": "Hunter Valley after-party security at Singleton sits one hour up the valley from Newcastle — same company, same licence.",
        "industries": "Harbour industry, hospitality, events, student precincts and construction",
        "angle": "Newcastle is a night-time hospitality city with a heavy industrial hinterland. You need both skill sets.",
        "unique": "Newcastle is on OnGuard’s published coverage. We deploy licensed crowd control for the hospitality strip and static or patrol cover for industrial and construction sites, with Hunter Valley event work already on the books.",
        "need": "Venue controllers, waterfront events and industrial night static.",
        "faq_local": "Can you cover a Newcastle venue and a Hunter site in the same week?",
        "faq_ans": "Yes. Newcastle, Singleton and the Hunter Valley are one operating area for OnGuard.",
    },
    {
        "slug": "singleton",
        "name": "Singleton",
        "state": "NSW",
        "postcode": "2330",
        "region": "Hunter Valley",
        "lat": -32.5674,
        "lng": 151.1748,
        "nearby": ["cessnock", "newcastle", "gosford"],
        "hero": "work-singleton",
        "proof": "OnGuard provided security for the Singleton Rodeo After Party at the Imperial Hotel Singleton.",
        "industries": "Mining services, pubs, rodeos and town-centre hospitality",
        "angle": "Singleton briefs are late, loud and local. We have already done the after-party.",
        "unique": "This is not a hypothetical suburb page. OnGuard stood licensed security at the Singleton Rodeo After Party, Imperial Hotel. Hunter Valley venue and event work is proven work, not a sales claim.",
        "need": "Hotel and after-party crowd control, event days, industrial static.",
        "faq_local": "Have you actually worked in Singleton?",
        "faq_ans": "Yes. Event and venue security for the Singleton Rodeo After Party at the Imperial Hotel. Ask us for the same standard on your next Hunter brief.",
    },
    {
        "slug": "cessnock",
        "name": "Cessnock",
        "state": "NSW",
        "postcode": "2325",
        "region": "Hunter Valley",
        "lat": -32.8325,
        "lng": 151.3560,
        "nearby": ["singleton", "newcastle", "gosford"],
        "hero": "work-nowra",
        "proof": None,
        "industries": "Wine tourism, events, hospitality and regional industry",
        "angle": "Cessnock’s risk is seasonal: cellar-door crowds, weddings and festival weekends.",
        "unique": "OnGuard covers the Hunter Valley as a listed region. Cessnock event and venue security uses the same licensed operators who already worked Singleton and Newcastle briefs.",
        "need": "Winery and festival crowd control, wedding security, town-centre patrols.",
        "faq_local": "Can you staff a Hunter Valley wedding or cellar-door event?",
        "faq_ans": "Yes. Licensed event and venue security across Cessnock, Singleton and the wider Hunter.",
    },
    {
        "slug": "bowral",
        "name": "Bowral",
        "state": "NSW",
        "postcode": "2576",
        "region": "Southern Highlands",
        "lat": -34.4792,
        "lng": 150.4181,
        "nearby": ["campbelltown", "wollongong", "nowra"],
        "hero": "work-festival",
        "proof": None,
        "industries": "Tourism, weddings, retail villages and weekender residential",
        "angle": "Highlands work is discreet. Guests should notice the event, not the security plan.",
        "unique": "The Southern Highlands is a named OnGuard expansion region. Bowral, as the hub, gets licensed event, wedding and retail security from a company that already works Nowra and Sydney — so you are not hiring a one-town operator.",
        "need": "Wedding and festival security, retail weekends, residential community patrols.",
        "faq_local": "Do you travel to the Southern Highlands for one-off events?",
        "faq_ans": "Yes. The Highlands sit on our Sydney–South Coast corridor. One-off and seasonal event cover is standard.",
    },
    {
        "slug": "wollongong",
        "name": "Wollongong",
        "state": "NSW",
        "postcode": "2500",
        "region": "Illawarra",
        "lat": -34.4278,
        "lng": 150.8931,
        "nearby": ["bowral", "nowra", "campbelltown"],
        "hero": "work-k9",
        "proof": None,
        "industries": "Port and industrial, university precinct, hospitality and beach events",
        "angle": "Wollongong needs industrial discipline and hospitality manners on the same roster.",
        "unique": "Illawarra sits between our Highlands and South Coast work. OnGuard covers Wollongong static, patrol and event security so a Port Kembla night shift and a Crown Street venue can come from one licensed company.",
        "need": "Industrial nights, venue crowd control, campus and event days.",
        "faq_local": "Do you cover Wollongong and Nowra together?",
        "faq_ans": "Yes. Both are on the South Coast / Illawarra side of our coverage. Multi-site quotes are available.",
    },
    {
        "slug": "nowra",
        "name": "Nowra",
        "state": "NSW",
        "postcode": "2541",
        "region": "South Coast",
        "lat": -34.8740,
        "lng": 150.6027,
        "nearby": ["worrigee", "wollongong", "bowral"],
        "hero": "work-nowra",
        "proof": "OnGuard provided event security for the Nowra Annual Rodeo with the Nowra Rodeo Association — record attendance.",
        "industries": "Regional events, retail, defence-adjacent industry and river precinct",
        "angle": "Nowra is proven ground. We have already held a record crowd here.",
        "unique": "This page is built on a real job. OnGuard Protection provided event security at the Nowra Annual Rodeo, working with the Nowra Rodeo Association. South Coast clients get a company that has already stood the post in town, not a Sydney firm guessing the drive time.",
        "need": "Rodeos and regional events, venue control, commercial and construction static.",
        "faq_local": "Have you worked events in Nowra before?",
        "faq_ans": "Yes. Licensed event security for the Nowra Annual Rodeo, including a record-breaking attendance day.",
    },
    {
        "slug": "worrigee",
        "name": "Worrigee",
        "state": "NSW",
        "postcode": "2540",
        "region": "South Coast",
        "lat": -34.9000,
        "lng": 150.6380,
        "nearby": ["nowra", "wollongong", "bowral"],
        "hero": "work-worrigee",
        "proof": "OnGuard provided event security at the Worrigee Equestrian Common Rodeo for attendees, staff and competitors.",
        "industries": "Equestrian events, regional functions and Nowra-adjacent commercial",
        "angle": "Worrigee is a specific site, not a suburb we invented for SEO. We worked the Common.",
        "unique": "OnGuard Protection provided licensed event security at Worrigee Equestrian Common. If you run a rodeo, gymkhana or outdoor event on the South Coast, you are talking to a team that has already walked that ground.",
        "need": "Equestrian and outdoor event security, plus Nowra-adjacent static and patrol.",
        "faq_local": "Can you secure another event at Worrigee Equestrian Common?",
        "faq_ans": "Yes. We have already provided licensed security at the Common and can return with a site-familiar crew.",
    },
    {
        "slug": "canberra",
        "name": "Canberra",
        "state": "ACT",
        "postcode": "2600",
        "region": "ACT & Canberra corridor",
        "lat": -35.2809,
        "lng": 149.1300,
        "nearby": ["bowral", "nowra", "sydney"],
        "hero": "work-poster",
        "proof": None,
        "industries": "Government-adjacent offices, venues, construction and residential communities",
        "angle": "Canberra is on the published OnGuard map: Hunter Valley to Canberra regions.",
        "unique": "OnGuard Protection is seeking and covering contract work through to Canberra and the ACT. Licensed NSW operators working the corridor from Sydney and the Highlands, with the same Master Licence 000110094 behind every brief.",
        "need": "Corporate concierge, event security and construction static on the ACT side of the corridor.",
        "faq_local": "Do you operate in the ACT as well as NSW?",
        "faq_ans": "Yes. Canberra / ACT is listed on OnGuard’s coverage. Confirm the site and we will tell you how we licence and roster the job.",
    },
]

for _loc in LOCATIONS:
    _loc["hero"] = f"town-{_loc['slug']}"
    HERO_META[_loc["hero"]] = (
        1600,
        900,
        f"{_loc['name']} {_loc['state']} — {_loc['region']}",
    )


def asset(name: str, depth: int) -> str:
    return f"{'../' * depth}assets/{name}"


def img_tag(
    stem: str,
    alt: str,
    w: int,
    h: int,
    depth: int,
    *,
    eager: bool = False,
    sizes: str = "(max-width: 700px) 100vw, 720px",
    extra: str = "",
) -> str:
    prefix = "../" * depth
    loading = "eager" if eager else "lazy"
    prio = ' fetchpriority="high"' if eager else ""
    return f'''<picture>
  <source type="image/webp" srcset="{prefix}assets/img/{stem}-800.webp 800w, {prefix}assets/img/{stem}.webp {w}w" sizes="{sizes}">
  <img src="{prefix}assets/img/{stem}-800.jpg" srcset="{prefix}assets/img/{stem}-800.jpg 800w" sizes="{sizes}" width="{w}" height="{h}" alt="{alt}" loading="{loading}" decoding="async"{prio}{extra}>
</picture>'''


def og_mime(path: str) -> str:
    lower = path.lower()
    if lower.endswith(".png"):
        return "image/png"
    if lower.endswith(".webp"):
        return "image/webp"
    return "image/jpeg"


def head(
    title: str,
    description: str,
    canonical: str,
    depth: int,
    og_image: str,
    og_w: int,
    og_h: int,
    og_alt: str,
    json_ld: list[dict],
    extra: str = "",
    robots: str = INDEX_ROBOTS,
) -> str:
    prefix = "../" * depth
    og_abs = f"{SITE}/{og_image}"
    googlebot = "noindex, follow" if "noindex" in robots else "index, follow"
    return f'''<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  {GTAG}
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="{robots}">
  <meta name="googlebot" content="{googlebot}">
  <meta name="author" content="OnGuard Protection">
  <meta name="geo.region" content="AU-NSW">
  <meta name="geo.placename" content="Sydney">
  <meta name="ICBM" content="-33.8688, 151.2093">
  <meta name="theme-color" content="#070b14">
  <meta name="format-detection" content="telephone=yes">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" href="{canonical}" hreflang="en-AU">
  <link rel="alternate" href="{canonical}" hreflang="x-default">
  <link rel="alternate" type="text/markdown" href="{prefix}llms.txt" title="LLM instructions">
  <link rel="icon" href="{prefix}assets/img/favicon-32.png" type="image/png" sizes="32x32">
  <link rel="icon" href="{prefix}assets/img/favicon-64.png" type="image/png" sizes="64x64">
  <link rel="icon" href="{prefix}assets/img/favicon-16.png" type="image/png" sizes="16x16">
  <link rel="apple-touch-icon" href="{prefix}assets/img/apple-touch-icon.png" sizes="180x180">
  <link rel="manifest" href="{prefix}site.webmanifest">
  <link rel="sitemap" type="application/xml" href="{prefix}sitemap.xml">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="OnGuard Protection">
  <meta property="og:locale" content="en_AU">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_abs}">
  <meta property="og:image:secure_url" content="{og_abs}">
  <meta property="og:image:type" content="{og_mime(og_image)}">
  <meta property="og:image:width" content="{og_w}">
  <meta property="og:image:height" content="{og_h}">
  <meta property="og:image:alt" content="{og_alt}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{og_abs}">
  <meta name="twitter:image:alt" content="{og_alt}">
  <link rel="preload" href="{prefix}assets/fonts/barlowcond-800.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{prefix}assets/fonts/fonts.css">
  <link rel="stylesheet" href="{prefix}styles.css">
  {extra}
  <script type="application/ld+json">{json.dumps(json_ld, ensure_ascii=False)}</script>
</head>'''


def chrome(depth: int, current: str = "") -> tuple[str, str]:
    prefix = "../" * depth
    home = f"{prefix}index.html"
    loc_idx = f"{prefix}locations/index.html"
    quote = f"{home}#quote"
    on = lambda name: " class='active'" if current == name else ""
    svc_open = ""
    svc_btn = " active" if current == "services" else ""
    svc_items = "\n".join(
        f'              <li><a href="{prefix}services/{svc["slug"]}.html">{svc["short"]}</a></li>'
        for svc in SERVICES
    )
    nav = f'''
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="top-bar">
    <div class="container top-bar-content">
      <p class="top-bar-live"><span class="pulse" aria-hidden="true"></span> 24/7 NSW response</p>
      <p class="top-bar-licence">SLED Master Licence {LICENCE} <a href="https://verify.licence.nsw.gov.au/home/Security" target="_blank" rel="noopener noreferrer">Verify</a></p>
      <div class="top-bar-end">
        <a class="top-bar-admin" href="{prefix}super/">Staff</a>
        <a class="top-bar-phone" href="tel:{TEL}">{PHONE}</a>
      </div>
    </div>
  </div>
  <header class="site-header">
    <div class="container">
      <nav class="main-nav" aria-label="Primary">
        <a href="{home}" class="logo">
          <img src="{prefix}assets/brand/onguard-nav-560.webp" srcset="{prefix}assets/brand/onguard-nav-560.webp 560w, {prefix}assets/brand/onguard-nav.webp 2048w" sizes="200px" width="560" height="229" alt="OnGuard Protection logo — NSW SLED licensed security company" decoding="async">
        </a>
        <button class="mobile-menu-btn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav">
          <span></span><span></span><span></span>
        </button>
        <div class="nav-links" id="site-nav">
          <ul class="nav-list">
            <li><a href="{home}"{on("home")}>Home</a></li>
            <li class="has-sub{svc_open}">
              <button type="button" class="nav-sub-toggle{svc_btn}" aria-expanded="false" aria-controls="nav-services">Services</button>
              <ul class="nav-sub" id="nav-services">
{svc_items}
                <li><a href="{home}#services">All services</a></li>
              </ul>
            </li>
            <li><a href="{loc_idx}"{on("locations")}>Locations</a></li>
            <li><a href="{prefix}industries/index.html"{on("industries")}>Industries</a></li>
            <li><a href="{prefix}blog/index.html"{on("blog")}>Blog</a></li>
            <li><a href="{prefix}jobs/index.html"{on("jobs")}>Jobs</a></li>
          </ul>
          <div class="nav-actions">
            <a href="{prefix}login/" class="btn btn-login{' active' if current=='login' else ''}">
              <img src="{prefix}assets/brand/icon-google.svg" width="16" height="16" alt="">
              Guard login
            </a>
            <a href="{quote}" class="btn btn-primary">Get a quote</a>
          </div>
        </div>
      </nav>
    </div>
  </header>'''
    footer = f'''
  <footer class="site-footer" id="contact">
    <div class="container footer-grid">
      <div class="footer-brand">
        <img src="{prefix}assets/brand/onguard-lockup-480.webp" width="220" height="90" alt="OnGuard Protection logo — licensed NSW security" class="footer-logo" loading="lazy" decoding="async">
        <p>We don’t just show up. We stand guard. Licensed NSW security from Sydney to the Hunter, South Coast and Canberra.</p>
        <div class="social-links">
          <a href="https://www.facebook.com/ogprotection/" target="_blank" rel="noopener noreferrer" aria-label="OnGuard Protection on Facebook">
            <img src="{prefix}assets/brand/icon-facebook.svg" width="22" height="22" alt="Facebook">
          </a>
          <a href="https://www.instagram.com/onguard_protection/" target="_blank" rel="noopener noreferrer" aria-label="OnGuard Protection on Instagram">
            <img src="{prefix}assets/brand/icon-instagram.svg" width="22" height="22" alt="Instagram">
          </a>
          <a href="https://www.google.com/search?q=OnGuard+Protection+NSW+security" target="_blank" rel="noopener noreferrer" aria-label="OnGuard Protection on Google">
            <img src="{prefix}assets/brand/icon-google.svg" width="22" height="22" alt="Google">
          </a>
        </div>
        <a class="tech-aid-badge" href="https://www.techaidaustralia.com.au/" target="_blank" rel="noopener noreferrer" aria-label="Powered by Tech Aid Australia">
          <img class="tech-aid-badge__mark" src="{prefix}assets/img/tech-aid-logo.png" alt="Tech Aid Australia logo" width="40" height="40" decoding="async" loading="lazy">
          <span class="tech-aid-badge__text">
            <span class="tech-aid-badge__kicker">Powered by</span>
            <span class="tech-aid-badge__name">Tech Aid Australia</span>
          </span>
        </a>
      </div>
      <div>
        <h2>Contact</h2>
        <ul class="footer-contact">
          <li><a href="tel:{TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Sydney NSW · Hunter · South Coast</li>
        </ul>
      </div>
      <div>
        <h2>Licence</h2>
        <ul class="footer-contact">
          <li>Master Licence {LICENCE}</li>
          <li><a href="https://verify.licence.nsw.gov.au/home/Security" target="_blank" rel="noopener noreferrer">Verify on SLED register</a></li>
          <li><a href="{prefix}locations/index.html">Suburb coverage</a></li>
          <li><a href="{prefix}blog/index.html">Security guides</a></li>
          <li><a href="{prefix}industries/index.html">Industries</a></li>
          <li><a href="{prefix}jobs/index.html">Guard jobs portal</a></li>
          <li><a href="{prefix}apply/">Apply without login</a></li>
          <li><a href="{prefix}login/">Guard login</a></li>
          <li><a href="{prefix}legal/index.html">Legal &amp; compliance</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <div class="footer-legal">
        <p>© {date.today().year} OnGuard Protection. All rights reserved.</p>
        <p>NSW Security Industry Act 1997 · SLED licensed</p>
      </div>
      <div class="footer-credits">
        <span>Developed by <a href="https://www.linkedin.com/in/chaseforrester/" target="_blank" rel="noopener noreferrer">Chase Forrester</a></span>
        <span class="footer-credits__sep" aria-hidden="true">·</span>
        <a class="footer-credits__tech-aid" href="https://www.techaidaustralia.com.au/" target="_blank" rel="noopener noreferrer">
          <img src="{prefix}assets/img/tech-aid-logo.png" alt="Tech Aid Australia" width="22" height="22" decoding="async" loading="lazy">
          <span>Powered by <strong>Tech Aid Australia</strong></span>
        </a>
      </div>
    </div>
  </footer>
  <div class="mobile-cta">
    <a href="tel:{TEL}">Call {PHONE}</a>
    <a href="#quote" class="mobile-cta-primary">Get a quote</a>
  </div>
  <div class="lightbox" id="lightbox" hidden>
    <button class="lightbox-close" type="button" aria-label="Close image">×</button>
    <img src="" alt="">
    <p></p>
  </div>
  <script src="{prefix}script.js" defer></script>'''
    return nav, footer


def share_bar(url: str, title: str) -> str:
    u = quote(url, safe="")
    t = quote(title, safe="")
    text = quote(f"{title} — OnGuard Protection", safe="")
    return f'''
<aside class="share-bar" aria-label="Share this page">
  <p class="share-bar-kicker">Share</p>
  <ul class="share-bar-list">
    <li><a class="share-fb" href="https://www.facebook.com/sharer/sharer.php?u={u}" target="_blank" rel="noopener noreferrer" aria-label="Share on Facebook">Facebook</a></li>
    <li><a class="share-x" href="https://twitter.com/intent/tweet?url={u}&amp;text={t}" target="_blank" rel="noopener noreferrer" aria-label="Share on X">X</a></li>
    <li><a class="share-li" href="https://www.linkedin.com/sharing/share-offsite/?url={u}" target="_blank" rel="noopener noreferrer" aria-label="Share on LinkedIn">LinkedIn</a></li>
    <li><a class="share-wa" href="https://wa.me/?text={text}%20{u}" target="_blank" rel="noopener noreferrer" aria-label="Share on WhatsApp">WhatsApp</a></li>
    <li><a class="share-tg" href="https://t.me/share/url?url={u}&amp;text={t}" target="_blank" rel="noopener noreferrer" aria-label="Share on Telegram">Telegram</a></li>
    <li><a class="share-em" href="mailto:?subject={t}&amp;body={u}" aria-label="Share by email">Email</a></li>
    <li><a class="share-rd" href="https://www.reddit.com/submit?url={u}&amp;title={t}" target="_blank" rel="noopener noreferrer" aria-label="Share on Reddit">Reddit</a></li>
    <li><a class="share-th" href="https://www.threads.net/intent/post?text={text}%20{u}" target="_blank" rel="noopener noreferrer" aria-label="Share on Threads">Threads</a></li>
    <li><a class="share-pin" href="https://pinterest.com/pin/create/button/?url={u}&amp;description={t}" target="_blank" rel="noopener noreferrer" aria-label="Share on Pinterest">Pinterest</a></li>
  </ul>
  <p class="share-bar-follow">Follow
    <a href="https://www.facebook.com/ogprotection/" target="_blank" rel="noopener noreferrer">Facebook</a>
    <a href="https://www.instagram.com/onguard_protection/" target="_blank" rel="noopener noreferrer">Instagram</a>
    <a href="https://www.google.com/search?q=OnGuard+Protection+NSW+security" target="_blank" rel="noopener noreferrer">Google</a>
  </p>
</aside>'''


def quote_form(prefill_suburb: str = "", prefill_service: str = "") -> str:
    options = "\n".join(
        f'<option value="{loc["name"]}"{" selected" if loc["name"]==prefill_suburb else ""}>{loc["name"]} {loc["state"]} {loc["postcode"]}</option>'
        for loc in LOCATIONS
    )
    svc_cards = ""
    for i, svc in enumerate(SERVICES):
        checked = " checked" if svc["name"] == prefill_service or svc["short"] == prefill_service else ""
        svc_cards += f'''
        <label class="svc-card">
          <input type="radio" name="service" value="{svc["name"]}" required{checked}>
          <span class="svc-card-body">
            <strong>{svc["short"]}</strong>
            <em>{svc["name"]}</em>
          </span>
        </label>'''
    return f'''
<section id="quote" class="quote quote-dynamic">
  <div class="container quote-grid">
    <div class="quote-copy">
      <p class="eyebrow">Get us on the job</p>
      <h2>Need a site stood up?</h2>
      <p>Four short steps. We build the brief as you go — then it lands in our inbox, not a black hole.</p>
      <div class="brief-live" id="brief-live" aria-live="polite">
        <p class="brief-kicker">Live brief</p>
        <p id="brief-text">Pick a suburb and a service to start the brief.</p>
      </div>
    </div>
    <form class="quote-form wizard" id="quote-form" action="https://formsubmit.co/{EMAIL}" method="POST" novalidate>
      <input type="hidden" name="_subject" value="OnGuard Protection — new quote request">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_next" value="{SITE}/thanks.html">
      <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <ol class="wizard-progress" aria-label="Quote steps">
        <li class="is-active" data-step-dot="1"><span>1</span> Where</li>
        <li data-step-dot="2"><span>2</span> What</li>
        <li data-step-dot="3"><span>3</span> Job</li>
        <li data-step-dot="4"><span>4</span> You</li>
      </ol>
      <p class="form-error" id="form-error" hidden role="alert"></p>
      <noscript><p class="field-hint">JavaScript is off — send the full brief in one go.</p></noscript>
      <fieldset class="wizard-step is-active" data-step="1">
        <legend>Where is the site?</legend>
        <label>
          Suburb
          <input type="text" name="location" id="suburb-input" list="suburb-list" value="{prefill_suburb}" placeholder="Start typing a suburb" required autocomplete="address-level2" enterkeyhint="next">
        </label>
        <datalist id="suburb-list">{options}</datalist>
        <p class="field-hint">We already roster Sydney, Hornsby, the Hunter, South Coast and Canberra.</p>
        <button type="button" class="btn btn-primary wizard-next">Next — choose the work</button>
      </fieldset>
      <fieldset class="wizard-step" data-step="2">
        <legend>What do you need?</legend>
        <div class="svc-grid">{svc_cards}</div>
        <div class="wizard-nav">
          <button type="button" class="btn btn-ghost wizard-back">Back</button>
          <button type="button" class="btn btn-primary wizard-next">Next — job details</button>
        </div>
      </fieldset>
      <fieldset class="wizard-step" data-step="3">
        <legend>Tell us the job</legend>
        <div class="form-row">
          <label>Start date
            <input type="date" name="start_date" enterkeyhint="next">
          </label>
          <label>Hours
            <select name="hours">
              <option value="">Not sure yet</option>
              <option>One-off / under 8 hours</option>
              <option>Overnight</option>
              <option>Weekend</option>
              <option>Ongoing nights</option>
              <option>Ongoing 24/7</option>
            </select>
          </label>
        </div>
        <label class="cond" data-for="event,crowd">Expected crowd
          <input type="number" name="crowd" min="1" inputmode="numeric" placeholder="e.g. 800">
        </label>
        <label class="cond" data-for="static,asset">Site type
          <select name="site_type">
            <option value="">Select</option>
            <option>Construction</option>
            <option>Commercial / office</option>
            <option>Retail</option>
            <option>Warehouse / yard</option>
            <option>Residential</option>
          </select>
        </label>
        <label class="cond" data-for="mobile,patrol">Nights per week
          <select name="nights">
            <option value="">Select</option>
            <option>1–2</option>
            <option>3–5</option>
            <option>7 nights</option>
          </select>
        </label>
        <label>Anything we should know?
          <textarea name="message" rows="3" placeholder="Dates, risks, access, dress standard." required></textarea>
        </label>
        <div class="wizard-nav">
          <button type="button" class="btn btn-ghost wizard-back">Back</button>
          <button type="button" class="btn btn-primary wizard-next">Next — your details</button>
        </div>
      </fieldset>
      <fieldset class="wizard-step" data-step="4">
        <legend>How do we reach you?</legend>
        <div class="form-row">
          <label>Name
            <input type="text" name="name" required autocomplete="name" enterkeyhint="next">
          </label>
          <label>Phone
            <input type="tel" name="phone" required autocomplete="tel" inputmode="tel" enterkeyhint="next">
          </label>
        </div>
        <label>Email
          <input type="email" name="email" required autocomplete="email" enterkeyhint="send">
        </label>
        <div class="wizard-nav">
          <button type="button" class="btn btn-ghost wizard-back">Back</button>
          <button type="submit" class="btn btn-primary btn-large">Send the brief</button>
        </div>
        <p class="form-note">Goes to {EMAIL}. Same-day reply on most briefs.</p>
      </fieldset>
    </form>
  </div>
</section>'''


def org_schema() -> dict:
    return {
        "@type": "SecurityService",
        "@id": f"{SITE}/#business",
        "name": "OnGuard Protection",
        "url": SITE,
        "image": [f"{SITE}/{OG_IMAGE}", f"{SITE}/assets/brand/onguard-lockup.png"],
        "logo": f"{SITE}/assets/brand/onguard-mark.png",
        "telephone": TEL,
        "email": EMAIL,
        "priceRange": "$$",
        "areaServed": [{"@type": "AdministrativeArea", "name": x} for x in ["New South Wales", "Australian Capital Territory"]],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Sydney",
            "addressRegion": "NSW",
            "addressCountry": "AU",
        },
        "identifier": {"@type": "PropertyValue", "name": "NSW Security Master Licence", "value": LICENCE},
        "sameAs": [
            "https://www.facebook.com/ogprotection/",
            "https://www.instagram.com/onguard_protection/",
        ],
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00",
            "closes": "23:59",
        },
    }


def loc_by_slug(slug: str) -> dict:
    return next(l for l in LOCATIONS if l["slug"] == slug)


def write_location(loc: dict) -> None:
    depth = 1
    url = f"{SITE}/locations/{loc['slug']}.html"
    hero = loc["hero"]
    w, h, alt = HERO_META[hero]
    title = f"Security Guards {loc['name']} {loc['state']} {loc['postcode']} | OnGuard Protection"
    desc = f"SLED-licensed security guards in {loc['name']} {loc['state']} {loc['postcode']}. Crowd control, static guards, mobile patrols and event security. Master Licence {LICENCE}. Call {PHONE}."
    if len(desc) > 160:
        desc = desc[:157] + "..."
    crumbs = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Locations", "item": f"{SITE}/locations/"},
            {"@type": "ListItem", "position": 3, "name": loc["name"], "item": url},
        ],
    }
    faq = {
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": loc["faq_local"],
                "acceptedAnswer": {"@type": "Answer", "text": loc["faq_ans"]},
            },
            {
                "@type": "Question",
                "name": f"Is OnGuard Protection licensed to work in {loc['name']}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"Yes. OnGuard Protection holds NSW Security Master Licence {LICENCE}. Licensed operatives cover {loc['name']} and the {loc['region']}.",
                },
            },
            {
                "@type": "Question",
                "name": f"What security services are available in {loc['name']}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"Crowd control, event security, static guards, mobile patrols, corporate concierge and asset protection in {loc['name']} {loc['state']}.",
                },
            },
        ],
    }
    speakable = {
        "@type": "WebPage",
        "@id": f"{url}#webpage",
        "url": url,
        "name": title,
        "dateModified": TODAY,
        "inLanguage": "en-AU",
        "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".answer-block", "h1", ".lead"]},
        "about": {"@id": f"{SITE}/#business"},
        "primaryImageOfPage": {
            "@type": "ImageObject",
            "url": f"{SITE}/assets/{hero}.jpg",
            "width": w,
            "height": h,
            "caption": alt,
        },
    }
    local = {
        "@type": "SecurityService",
        "name": f"OnGuard Protection — {loc['name']}",
        "url": url,
        "telephone": TEL,
        "email": EMAIL,
        "image": f"{SITE}/assets/{hero}.jpg",
        "areaServed": {
            "@type": "City",
            "name": loc["name"],
            "containedInPlace": {"@type": "State", "name": "New South Wales" if loc["state"] == "NSW" else "Australian Capital Territory"},
            "geo": {"@type": "GeoCoordinates", "latitude": loc["lat"], "longitude": loc["lng"]},
        },
        "provider": {"@id": f"{SITE}/#business"},
    }
    nearby_html = ""
    for slug in loc["nearby"]:
        n = loc_by_slug(slug)
        nearby_html += f'<li><a href="{n["slug"]}.html">Security guards {n["name"]} {n["state"]}</a></li>'
    svc_html = ""
    for svc in SERVICES:
        svc_html += f'<li><a href="{loc["slug"]}/{svc["slug"]}.html">{svc["name"]} in {loc["name"]}</a></li>'
    proof = f'<p class="proof-callout">{loc["proof"]}</p>' if loc["proof"] else ""
    nav, footer = chrome(depth, "locations")
    extra = f'<link rel="preload" as="image" href="../assets/img/{hero}-800.webp" type="image/webp">'
    html = f'''{head(title, desc, url, depth, OG_IMAGE, OG_W, OG_H, OG_ALT, [org_schema(), crumbs, faq, speakable, local], extra)}
<body class="inner-page">
{nav}
<main id="main">
  <nav class="crumbs container" aria-label="Breadcrumb">
    <a href="../index.html">Home</a>
    <span aria-hidden="true">/</span>
    <a href="index.html">Locations</a>
    <span aria-hidden="true">/</span>
    <span>{loc["name"]}</span>
  </nav>
  <header class="page-hero">
    <div class="page-hero-media">
      {img_tag(hero, alt, w, h, depth, eager=True, sizes="100vw")}
    </div>
    <div class="container page-hero-copy hero-in">
      <p class="eyebrow">{loc["region"]} · {loc["postcode"]}</p>
      <h1>Security guards in {loc["name"]} {loc["state"]}</h1>
      <p class="lead">{loc["angle"]}</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#quote">Quote {loc["name"]} security</a>
        <a class="btn btn-outline" href="tel:{TEL}">Call {PHONE}</a>
      </div>
    </div>
  </header>
  <article class="container prose reveal">
    <p class="answer-block" id="who-covers-{loc["slug"]}"><strong>OnGuard Protection provides SLED-licensed security in {loc["name"]} {loc["state"]} {loc["postcode"]}.</strong> Crowd control, static guards, mobile patrols and event operations. Master Licence {LICENCE}.</p>
    {proof}
    <h2>Licensed security for {loc["industries"]}</h2>
    <p>{loc["unique"]}</p>
    <h2>What {loc["name"]} sites usually need</h2>
    <p>{loc["need"]}</p>
    <h2>Services we deploy in {loc["name"]}</h2>
    <ul class="link-list">{svc_html}</ul>
    <section class="faq" aria-labelledby="faq-{loc["slug"]}">
      <h2 id="faq-{loc["slug"]}">Questions people ask about security in {loc["name"]}</h2>
      <details open>
        <summary>{loc["faq_local"]}</summary>
        <p class="answer-block">{loc["faq_ans"]}</p>
      </details>
      <details>
        <summary>Is OnGuard Protection licensed to work in {loc["name"]}?</summary>
        <p class="answer-block">Yes. NSW Security Master Licence {LICENCE}. Check the SLED public register before you hire anyone.</p>
      </details>
      <details>
        <summary>How do I get a {loc["name"]} security quote?</summary>
        <p class="answer-block">Use the brief below or call {PHONE}. Tell us the suburb, the hours and the risk.</p>
      </details>
    </section>
    <h2>Nearby coverage</h2>
    <ul class="link-list">{nearby_html}</ul>
    {share_bar(url, title)}
  </article>
  {quote_form(prefill_suburb=loc["name"])}
</main>
{footer}
</body>
</html>'''
    out = ROOT / "locations" / f"{loc['slug']}.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")


def write_service(svc: dict) -> None:
    depth = 1
    url = f"{SITE}/services/{svc['slug']}.html"
    title = svc["title"]
    desc = svc["description"]
    crumbs = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Services", "item": f"{SITE}/#services"},
            {"@type": "ListItem", "position": 3, "name": svc["name"], "item": url},
        ],
    }
    faq = {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in svc["faq"]
        ],
    }
    service = {
        "@type": "Service",
        "name": svc["name"],
        "serviceType": svc["keyword"],
        "provider": {"@id": f"{SITE}/#business"},
        "areaServed": ["NSW", "ACT"],
        "url": url,
        "image": f"{SITE}/assets/{svc['img']}.jpg",
    }
    loc_links = "".join(
        f'<a class="suburb-chip" href="../locations/{loc["slug"]}/{svc["slug"]}.html">{loc["name"]}<span>{loc["state"]} {loc["postcode"]}</span></a>'
        for loc in LOCATIONS
    )
    bullets = "".join(f"<li>{b}</li>" for b in svc["bullets"])
    faq_html = "".join(
        f'<details><summary>{q}</summary><p class="answer-block">{a}</p></details>'
        for q, a in svc["faq"]
    )
    switcher = "".join(
        '<a href="{slug}.html"{current}>{short}</a>'.format(
            slug=other["slug"],
            short=other["short"],
            current=' class="is-current"' if other["slug"] == svc["slug"] else "",
        )
        for other in SERVICES
    )
    nav, footer = chrome(depth, "services")
    extra = f'<link rel="preload" as="image" href="../assets/img/{svc["img"]}-800.webp" type="image/webp">'
    html = f'''{head(title, desc, url, depth, OG_IMAGE, OG_W, OG_H, OG_ALT, [org_schema(), crumbs, faq, service], extra)}
<body class="inner-page service-page">
{nav}
<main id="main">
  <nav class="crumbs container" aria-label="Breadcrumb">
    <a href="../index.html">Home</a>
    <span aria-hidden="true">/</span>
    <a href="../index.html#services">Services</a>
    <span aria-hidden="true">/</span>
    <span>{svc["name"]}</span>
  </nav>
  <nav class="svc-switcher container" aria-label="All services">
    {switcher}
  </nav>
  <header class="page-hero">
    <div class="page-hero-media">
      {img_tag(svc["img"], svc["alt"], svc["img_w"], svc["img_h"], depth, eager=True, sizes="100vw")}
    </div>
    <div class="container page-hero-copy hero-in">
      <p class="eyebrow">{svc["keyword"]}</p>
      <h1>{svc["h1"]}</h1>
      <p class="lead">{svc["lead"]}</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#quote">Quote this service</a>
        <a class="btn btn-outline" href="tel:{TEL}">Call {PHONE}</a>
      </div>
    </div>
  </header>
  <div class="container service-layout">
    <article class="prose reveal">
      <p class="answer-block">{svc["body"]}</p>
      <h2>What you get</h2>
      <ul class="check-list">{bullets}</ul>
      <section class="faq">
        <h2>Questions about {svc["short"].lower()}</h2>
        {faq_html}
      </section>
      <h2>{svc["short"]} by suburb</h2>
      <p class="muted-line">Same licence. Local brief. Pick the town.</p>
      <div class="suburb-chip-grid">{loc_links}</div>
      {share_bar(url, title)}
    </article>
    <aside class="service-aside">
      <div class="service-aside-card">
        <p class="eyebrow">Stand this post</p>
        <h2>Need {svc["short"].lower()}?</h2>
        <p>Tell us the suburb and the hours. Same-day reply on most briefs.</p>
        <a class="btn btn-primary" href="#quote">Start a quote</a>
        <a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a>
        <p class="form-note">Master Licence {LICENCE} · NSW Class 1 only</p>
      </div>
    </aside>
  </div>
  {quote_form(prefill_service=svc["name"])}
</main>
{footer}
</body>
</html>'''
    out = ROOT / "services" / f"{svc['slug']}.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")


def write_combo(loc: dict, svc: dict) -> None:
    depth = 2
    url = f"{SITE}/locations/{loc['slug']}/{svc['slug']}.html"
    title = f"{svc['short']} {loc['name']} {loc['state']} {loc['postcode']} | OnGuard Protection"
    desc = (
        f"SLED-licensed {svc['short'].lower()} in {loc['name']} {loc['state']} {loc['postcode']}. "
        f"{loc['need']} Master Licence {LICENCE}. Call {PHONE}."
    )
    if len(desc) > 160:
        desc = desc[:157] + "..."
    if len(desc) < 120:
        desc = (
            f"SLED-licensed {svc['short'].lower()} for {loc['industries']} in {loc['name']} "
            f"{loc['state']} {loc['postcode']}. Master Licence {LICENCE}. Call {PHONE}."
        )
        if len(desc) > 160:
            desc = desc[:157] + "..."
    crumbs = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Locations", "item": f"{SITE}/locations/"},
            {"@type": "ListItem", "position": 3, "name": loc["name"], "item": f"{SITE}/locations/{loc['slug']}.html"},
            {"@type": "ListItem", "position": 4, "name": svc["short"], "item": url},
        ],
    }
    faq = {
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"Do you provide {svc['short'].lower()} in {loc['name']}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"Yes. OnGuard Protection deploys licensed {svc['short'].lower()} in {loc['name']} {loc['state']} under Master Licence {LICENCE}.",
                },
            },
            {
                "@type": "Question",
                "name": loc["faq_local"],
                "acceptedAnswer": {"@type": "Answer", "text": loc["faq_ans"]},
            },
            {"@type": "Question", "name": svc["faq"][0][0], "acceptedAnswer": {"@type": "Answer", "text": svc["faq"][0][1]}},
        ],
    }
    service = {
        "@type": "Service",
        "name": f"{svc['name']} — {loc['name']}",
        "serviceType": svc["keyword"],
        "provider": {"@id": f"{SITE}/#business"},
        "areaServed": {
            "@type": "City",
            "name": loc["name"],
            "containedInPlace": {
                "@type": "State",
                "name": "New South Wales" if loc["state"] == "NSW" else "Australian Capital Territory",
            },
            "geo": {"@type": "GeoCoordinates", "latitude": loc["lat"], "longitude": loc["lng"]},
        },
        "url": url,
        "image": f"{SITE}/{OG_IMAGE}",
    }
    other_svc = "".join(
        f'<li><a href="{other["slug"]}.html">{other["name"]} in {loc["name"]}</a></li>'
        for other in SERVICES
        if other["slug"] != svc["slug"]
    )
    nearby_html = ""
    for slug in loc["nearby"]:
        n = loc_by_slug(slug)
        nearby_html += f'<li><a href="../{n["slug"]}/{svc["slug"]}.html">{svc["short"]} in {n["name"]}</a></li>'
    bullets = "".join(f"<li>{b}</li>" for b in svc["bullets"])
    proof = f'<p class="proof-callout">{loc["proof"]}</p>' if loc["proof"] else ""
    nav, footer = chrome(depth, "locations")
    extra = f'<link rel="preload" as="image" href="../../assets/img/{svc["img"]}-800.webp" type="image/webp">'
    w, h, alt = HERO_META[svc["img"]] if svc["img"] in HERO_META else (svc["img_w"], svc["img_h"], svc["alt"])
    html = f'''{head(title, desc, url, depth, OG_IMAGE, OG_W, OG_H, OG_ALT, [org_schema(), crumbs, faq, service], extra)}
<body class="inner-page">
{nav}
<main id="main">
  <nav class="crumbs container" aria-label="Breadcrumb">
    <a href="../../index.html">Home</a>
    <span aria-hidden="true">/</span>
    <a href="../index.html">Locations</a>
    <span aria-hidden="true">/</span>
    <a href="../{loc["slug"]}.html">{loc["name"]}</a>
    <span aria-hidden="true">/</span>
    <span>{svc["short"]}</span>
  </nav>
  <header class="page-hero">
    <div class="page-hero-media">
      {img_tag(svc["img"], svc["alt"], svc["img_w"], svc["img_h"], depth, eager=True, sizes="100vw")}
    </div>
    <div class="container page-hero-copy hero-in">
      <p class="eyebrow">{loc["region"]} · {svc["keyword"]}</p>
      <h1>{svc["short"]} in {loc["name"]} {loc["state"]}</h1>
      <p class="lead">{loc["angle"]} {svc["lead"]}</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#quote">Quote {svc["short"].lower()} in {loc["name"]}</a>
        <a class="btn btn-outline" href="tel:{TEL}">Call {PHONE}</a>
      </div>
    </div>
  </header>
  <article class="container prose reveal">
    <p class="answer-block"><strong>OnGuard Protection provides SLED-licensed {svc["short"].lower()} in {loc["name"]} {loc["state"]} {loc["postcode"]}.</strong> Master Licence {LICENCE}.</p>
    {proof}
    <h2>{svc["name"]} for {loc["industries"]}</h2>
    <p>{loc["unique"]}</p>
    <p>{svc["body"]}</p>
    <h2>What {loc["name"]} sites usually need</h2>
    <p>{loc["need"]}</p>
    <h2>What you get</h2>
    <ul>{bullets}</ul>
    <section class="faq">
      <h2>Questions about {svc["short"].lower()} in {loc["name"]}</h2>
      <details open>
        <summary>Do you provide {svc["short"].lower()} in {loc["name"]}?</summary>
        <p class="answer-block">Yes. Licensed {svc["short"].lower()} in {loc["name"]} {loc["state"]} under Master Licence {LICENCE}. Call {PHONE}.</p>
      </details>
      <details>
        <summary>{loc["faq_local"]}</summary>
        <p class="answer-block">{loc["faq_ans"]}</p>
      </details>
      <details>
        <summary>{svc["faq"][0][0]}</summary>
        <p class="answer-block">{svc["faq"][0][1]}</p>
      </details>
    </section>
    <h2>Other {loc["name"]} services</h2>
    <ul class="link-list">{other_svc}</ul>
    <p><a href="../{loc["slug"]}.html">All security services in {loc["name"]}</a> · <a href="../../services/{svc["slug"]}.html">{svc["name"]} across NSW</a></p>
    <h2>{svc["short"]} nearby</h2>
    <ul class="link-list">{nearby_html}</ul>
    {share_bar(url, title)}
  </article>
  {quote_form(prefill_suburb=loc["name"], prefill_service=svc["name"])}
</main>
{footer}
</body>
</html>'''
    out = ROOT / "locations" / loc["slug"] / f"{svc['slug']}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def write_locations_index() -> None:
    depth = 1
    url = f"{SITE}/locations/"
    cards = ""
    for loc in LOCATIONS:
        stem = loc["hero"]
        w, h, alt = HERO_META[stem]
        search = " ".join([loc["name"], loc["region"], loc["state"], loc["postcode"], loc["angle"]]).lower()
        cards += f'''
        <article class="loc-card loc-card-photo reveal" data-search="{xml_escape(search)}">
          <a href="{loc["slug"]}.html">
            <div class="loc-card-media">
              {img_tag(stem, alt, w, h, 1, sizes="(max-width: 700px) 100vw, 360px")}
            </div>
            <div class="loc-card-body">
              <h2>Security guards {loc["name"]}</h2>
              <p>{loc["region"]} · {loc["state"]} {loc["postcode"]}</p>
              <p>{loc["angle"]}</p>
            </div>
          </a>
        </article>'''
    item_list = {
        "@type": "ItemList",
        "name": "OnGuard Protection NSW and ACT coverage suburbs",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": f"{SITE}/locations/{loc['slug']}.html", "name": loc["name"]}
            for i, loc in enumerate(LOCATIONS)
        ],
    }
    nav, footer = chrome(depth, "locations")
    title = "NSW & ACT Security Guard Locations | OnGuard Protection"
    desc = "Find SLED-licensed OnGuard Protection security guards by suburb — Sydney, Hornsby, Newcastle, Nowra, Singleton, Canberra and the full NSW corridor. ML 000110094."
    html = f'''{head(title, desc, url, depth, OG_IMAGE, OG_W, OG_H, OG_ALT, [org_schema(), item_list])}
<body class="inner-page">
{nav}
<main id="main">
  <nav class="crumbs container" aria-label="Breadcrumb">
    <a href="../index.html">Home</a>
    <span aria-hidden="true">/</span>
    <span>Locations</span>
  </nav>
  <div class="container section-header loc-index-head">
    <p class="eyebrow">Suburb coverage</p>
    <h1>Security guards by suburb — NSW &amp; ACT</h1>
    <p class="lead">Eighteen coverage suburbs, each with dedicated service pages. Real towns we roster — not a generated list.</p>
    <form class="place-search" role="search" action="index.html" method="get">
      <label for="place-search">Search a suburb or postcode</label>
      <input type="search" id="place-search" name="q" placeholder="Sydney, Nowra, 2541…" autocomplete="off">
    </form>
    <p class="place-search-empty" id="place-search-empty" hidden>No suburb matches that search. Try a nearby town or call 0432 893 343.</p>
  </div>
  <div class="container loc-grid">{cards}</div>
  {quote_form()}
</main>
{footer}
</body>
</html>'''
    (ROOT / "locations" / "index.html").write_text(html, encoding="utf-8")


def write_thanks() -> None:
    nav, footer = chrome(0)
    title = "Brief received | OnGuard Protection"
    desc = "Your OnGuard Protection security brief has been sent. We reply on 0432 893 343 and admin@ogprotection.com.au."
    html = f'''{head(title, desc, f"{SITE}/thanks.html", 0, OG_IMAGE, OG_W, OG_H, OG_ALT, [org_schema()], robots=NOINDEX_ROBOTS)}
<body class="inner-page">
{nav}
<main id="main" class="container prose thanks-page">
  <p class="eyebrow">Sent</p>
  <h1>Brief received. We are on it.</h1>
  <p class="lead">If it is urgent, call <a href="tel:{TEL}">{PHONE}</a> now. Otherwise we will reply to the email you left.</p>
  <p><a class="btn btn-primary" href="index.html">Back to home</a></p>
</main>
{footer}
</body>
</html>'''
    (ROOT / "thanks.html").write_text(html, encoding="utf-8")


def write_404() -> None:
    nav, footer = chrome(0)
    html = f'''{head("Page not found | OnGuard Protection", "That page is not on OnGuard Protection. Browse NSW suburb security pages or request a quote.", f"{SITE}/404.html", 0, OG_IMAGE, OG_W, OG_H, OG_ALT, [org_schema()], robots=NOINDEX_ROBOTS)}
<body class="inner-page">
{nav}
<main id="main" class="container prose thanks-page">
  <h1>This post is not stood.</h1>
  <p>Try the <a href="locations/index.html">suburb list</a> or <a href="index.html#quote">request a quote</a>.</p>
</main>
{footer}
</body>
</html>'''
    (ROOT / "404.html").write_text(html, encoding="utf-8")


def write_url_entry(
    loc: str,
    *,
    changefreq: str = "weekly",
    priority: str = "0.8",
    images: list[tuple[str, str]] | None = None,
) -> str:
    parts = [
        "  <url>",
        f"    <loc>{xml_escape(loc)}</loc>",
        f"    <lastmod>{TODAY}</lastmod>",
        f"    <changefreq>{xml_escape(changefreq)}</changefreq>",
        f"    <priority>{priority}</priority>",
    ]
    for img_path, img_title in images or []:
        parts.extend(
            [
                "    <image:image>",
                f"      <image:loc>{xml_escape(SITE + '/' + img_path)}</image:loc>",
                f"      <image:title>{xml_escape(img_title)}</image:title>",
                f"      <image:caption>{xml_escape(img_title)}</image:caption>",
                "    </image:image>",
            ]
        )
    parts.append("  </url>")
    return "\n".join(parts)


def write_urlset(path: Path, entries: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
        + "\n".join(entries)
        + "\n</urlset>\n"
    )
    path.write_text(xml, encoding="utf-8")


def write_sitemap_index(children: list[str]) -> None:
    body = "\n".join(
        "  <sitemap>\n"
        f"    <loc>{xml_escape(SITE + '/' + child)}</loc>\n"
        f"    <lastmod>{TODAY}</lastmod>\n"
        "  </sitemap>"
        for child in children
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + body
        + "\n</sitemapindex>\n"
    )
    (ROOT / "sitemap-index.xml").write_text(xml, encoding="utf-8")


def write_sitemaps() -> list[str]:
    """Write a sitemap index plus one child sitemap per real URL group.

    Each indexable URL appears in exactly one child sitemap. 404, thanks,
    and noindex pages are omitted. Images are attached to the page they
    actually appear on so the homepage is not listed repeatedly.
    """
    out_dir = ROOT / "sitemaps"
    if out_dir.exists():
        for old in out_dir.glob("*.xml"):
            old.unlink()
    out_dir.mkdir(exist_ok=True)

    children: list[str] = []
    all_entries: list[str] = []

    def add(name: str, entries: list[str]) -> None:
        rel = f"sitemaps/{name}.xml"
        write_urlset(ROOT / rel, entries)
        children.append(rel)
        all_entries.extend(entries)

    add(
        "core-home",
        [
            write_url_entry(
                f"{SITE}/",
                changefreq="weekly",
                priority="1.0",
                images=[
                    (OG_IMAGE, OG_ALT),
                    ("assets/brand/onguard-lockup.png", "OnGuard Protection logo — NSW SLED licensed security company"),
                    ("assets/work-nowra.jpg", "OnGuard Protection event security at the Nowra Annual Rodeo"),
                    ("assets/work-worrigee.jpg", "OnGuard Protection team at Worrigee Equestrian Common Rodeo"),
                    ("assets/work-singleton.jpg", "OnGuard Protection at Singleton Rodeo After Party, Imperial Hotel"),
                    ("assets/work-poster.jpg", "OnGuard Protection NSW and ACT services and coverage poster"),
                    ("assets/work-k9.jpg", "OnGuard Protection dog handler on a NSW industrial night static"),
                    ("assets/work-festival.jpg", "OnGuard Protection crowd control at a NSW festival"),
                    ("assets/work-screening.jpg", "OnGuard Protection bag search at a NSW event entry"),
                    ("assets/work-patrol.jpg", "OnGuard Protection marked patrol ute on a night mobile patrol outside a NSW chemist"),
                    ("assets/work-tiguan.jpg", "OnGuard Protection marked VW Tiguan patrol vehicle, plates OGPROT, Master Licence 000110094"),
                ],
            )
        ],
    )
    add(
        "core-locations-index",
        [write_url_entry(f"{SITE}/locations/", changefreq="weekly", priority="0.9", images=[(OG_IMAGE, OG_ALT)])],
    )
    add(
        "legal-page",
        [write_url_entry(f"{SITE}/legal/", changefreq="monthly", priority="0.7", images=[(OG_IMAGE, OG_ALT)])],
    )
    add(
        "legal-pdf",
        [
            write_url_entry(
                f"{SITE}/legal/OnGuard-Protection-Legal-Compliance-Pack.pdf",
                changefreq="monthly",
                priority="0.6",
            )
        ],
    )

    for svc in SERVICES:
        add(
            f"service-{svc['slug']}",
            [
                write_url_entry(
                    f"{SITE}/services/{svc['slug']}.html",
                    changefreq="weekly",
                    priority="0.85",
                    images=[
                        (OG_IMAGE, OG_ALT),
                        (f"assets/{svc['img']}.jpg", svc["alt"]),
                    ],
                )
            ],
        )

    for loc in LOCATIONS:
        hero = loc["hero"]
        _w, _h, hero_alt = HERO_META[hero]
        add(
            f"location-{loc['slug']}",
            [
                write_url_entry(
                    f"{SITE}/locations/{loc['slug']}.html",
                    changefreq="weekly",
                    priority="0.8",
                    images=[
                        (OG_IMAGE, OG_ALT),
                        (f"assets/{hero}.jpg", hero_alt),
                    ],
                )
            ],
        )
        for svc in SERVICES:
            add(
                f"location-{loc['slug']}-{svc['slug']}",
                [
                    write_url_entry(
                        f"{SITE}/locations/{loc['slug']}/{svc['slug']}.html",
                        changefreq="weekly",
                        priority="0.7",
                        images=[
                            (OG_IMAGE, OG_ALT),
                            (f"assets/{svc['img']}.jpg", svc["alt"]),
                        ],
                    )
                ],
            )

    import expand_site

    for name, loc, prio in expand_site.extra_urls():
        add(
            name,
            [write_url_entry(loc, changefreq="weekly", priority=prio, images=[(OG_IMAGE, OG_ALT)])],
        )

    write_sitemap_index(children)
    # Search Console is already pointed at /sitemap.xml. A single urlset on
    # the live host is what actually fills "discovered URLs".
    write_urlset(ROOT / "sitemap.xml", all_entries)
    return children


def write_tech() -> None:
    write_sitemaps()

    robots = f'''User-agent: *
Allow: /
Allow: /sitemaps/
Disallow: /thanks.html
Disallow: /404.html
Disallow: /login/
Disallow: /super/
Disallow: /platform/

User-agent: Googlebot
Allow: /
Allow: /sitemaps/

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: {SITE}/sitemap.xml
Sitemap: {SITE}/sitemap-index.xml
# LLM crawl map
# {SITE}/llms.txt
'''
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")

    llms = f'''# OnGuard Protection

> SLED-licensed NSW security company covering Sydney, the Hunter, South Coast and Canberra. Master Licence {LICENCE}. Crowd control, static guards, mobile patrols and event operations.

OnGuard Protection deploys licensed operatives for venues, construction, commercial sites and events. Contact [{PHONE}](tel:{TEL}) or [{EMAIL}](mailto:{EMAIL}).

## Docs

- [Home]({SITE}/): NSW licensed security overview and quote brief
- [Suburb coverage]({SITE}/locations/): Security guards by NSW and ACT suburb
- [Sydney security guards]({SITE}/locations/sydney.html): CBD and inner-Sydney coverage
- [Nowra event security]({SITE}/locations/nowra.html): Nowra Annual Rodeo and South Coast work
- [Worrigee security]({SITE}/locations/worrigee.html): Worrigee Equestrian Common
- [Singleton security]({SITE}/locations/singleton.html): Imperial Hotel after-party and Hunter Valley
- [Newcastle security]({SITE}/locations/newcastle.html): Hospitality and industrial cover
- [Canberra security]({SITE}/locations/canberra.html): ACT corridor coverage
- [Crowd control]({SITE}/services/crowd-control.html): Licensed venue and crowd controllers
- [Event security]({SITE}/services/event-security.html): Rodeos, festivals and venue operations
- [Static guards]({SITE}/services/static-guards.html): Construction and commercial posts
- [Mobile patrols]({SITE}/services/mobile-patrols.html): After-hours patrols and alarm response
- [Corporate security]({SITE}/services/corporate-security.html): Concierge and lobby control
- [Asset protection]({SITE}/services/asset-protection.html): Plant and compound protection
- [Guides]({SITE}/blog/): NSW security briefs and licence explainers
- [Industries]({SITE}/industries/): Construction, venues, events, logistics
- [Jobs data flow]({SITE}/jobs/): Guard portal architecture
- [Verify licence](https://verify.licence.nsw.gov.au/home/Security): NSW SLED public register for Master Licence {LICENCE}
- [Sitemap]({SITE}/sitemap.xml): Machine-readable page list

## Optional

- [Instagram](https://www.instagram.com/onguard_protection/): Field photos and job updates
- [Facebook](https://www.facebook.com/ogprotection/): OnGuard Protection page
- [Tech Aid Australia](https://www.techaidaustralia.com.au/): Website development partner
'''
    (ROOT / "llms.txt").write_text(llms, encoding="utf-8")

    agentix = {
        "agentix_score_target": 3,
        "entity": {
            "@id": f"{SITE}/#business",
            "name": "OnGuard Protection",
            "licence": LICENCE,
            "telephone": TEL,
            "email": EMAIL,
        },
        "citeable_answers": [
            {
                "id": "who",
                "question": "Who is OnGuard Protection?",
                "answer": f"OnGuard Protection is a SLED-licensed NSW security company (Master Licence {LICENCE}) covering Sydney, the Hunter, South Coast and Canberra.",
            },
            {
                "id": "licence",
                "question": "What is OnGuard Protection's security licence number?",
                "answer": f"NSW Security Master Licence {LICENCE}.",
            },
            {
                "id": "phone",
                "question": "How do I contact OnGuard Protection?",
                "answer": f"Call {PHONE} or email {EMAIL}.",
            },
        ],
        "locations": [f"{SITE}/locations/{l['slug']}.html" for l in LOCATIONS],
        "services": [f"{SITE}/services/{s['slug']}.html" for s in SERVICES],
        "location_services": [
            f"{SITE}/locations/{l['slug']}/{s['slug']}.html" for l in LOCATIONS for s in SERVICES
        ],
        "sitemap_index": f"{SITE}/sitemap.xml",
    }
    (ROOT / "agentix.json").write_text(json.dumps(agentix, indent=2), encoding="utf-8")

    (ROOT / "site.webmanifest").write_text(
        json.dumps(
            {
                "name": "OnGuard Protection",
                "short_name": "OnGuard",
                "description": "SLED-licensed NSW security. Sydney to Canberra.",
                "start_url": "/",
                "display": "standalone",
                "background_color": "#070b14",
                "theme_color": "#070b14",
                "lang": "en-AU",
                "icons": [
                    {"src": "assets/img/favicon-32.png", "sizes": "32x32", "type": "image/png"},
                    {"src": "assets/img/favicon-64.png", "sizes": "64x64", "type": "image/png"},
                    {"src": "assets/img/favicon-128.png", "sizes": "128x128", "type": "image/png"},
                    {"src": "assets/img/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"},
                    {"src": "assets/img/favicon-192.png", "sizes": "192x192", "type": "image/png"},
                    {"src": "assets/img/favicon-512.png", "sizes": "512x512", "type": "image/png"},
                ],
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    (ROOT / "humans.txt").write_text(
        f"/* TEAM */\nOnGuard Protection\nContact: {EMAIL}\nLocation: Sydney, NSW\nLicence: {LICENCE}\n",
        encoding="utf-8",
    )


def url_to_path(url: str) -> Path | None:
    if not url.startswith(SITE + "/"):
        return None
    rel = url[len(SITE) + 1 :]
    if rel == "":
        return ROOT / "index.html"
    if rel.endswith("/"):
        candidate = ROOT / rel / "index.html"
        if candidate.exists():
            return candidate
        return ROOT / rel.rstrip("/")
    return ROOT / rel


def validate_sitemaps() -> None:
    import xml.etree.ElementTree as ET

    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    master = ET.parse(ROOT / "sitemap.xml").getroot()
    if not master.tag.endswith("urlset"):
        raise SystemExit("sitemap.xml must be a urlset of every indexable URL")
    master_urls = [el.text or "" for el in master.findall("sm:url/sm:loc", ns)]
    if len(master_urls) != len(set(master_urls)):
        raise SystemExit("duplicate URL in sitemap.xml")

    tree = ET.parse(ROOT / "sitemap-index.xml")
    root = tree.getroot()
    if not root.tag.endswith("sitemapindex"):
        raise SystemExit("sitemap-index.xml must be a sitemapindex")
    child_locs = [el.text or "" for el in root.findall("sm:sitemap/sm:loc", ns)]
    if not child_locs:
        raise SystemExit("sitemap index has no children")
    if len(child_locs) != len(set(child_locs)):
        raise SystemExit("duplicate child sitemap listed in index")

    seen: list[str] = []
    errors: list[str] = []
    for loc in child_locs:
        if not loc.startswith(f"{SITE}/sitemaps/") or not loc.endswith(".xml"):
            errors.append(f"child sitemap outside /sitemaps/: {loc}")
            continue
        rel = loc[len(SITE) + 1 :]
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"missing child sitemap file: {rel}")
            continue
        child = ET.parse(path).getroot()
        if not child.tag.endswith("urlset"):
            errors.append(f"{rel} is not a urlset")
            continue
        urls = [el.text or "" for el in child.findall("sm:url/sm:loc", ns)]
        if not urls:
            errors.append(f"{rel} has no URLs")
        for url in urls:
            if not url.startswith(SITE + "/"):
                errors.append(f"off-site URL in {rel}: {url}")
            if url in seen:
                errors.append(f"duplicate URL {url}")
            seen.append(url)
            if any(bad in url for bad in ("thanks.html", "404.html")):
                errors.append(f"noindex URL listed: {url}")
            disk = url_to_path(url)
            if disk is None or not disk.exists():
                errors.append(f"sitemap URL has no file: {url}")

    expected = {f"{SITE}/", f"{SITE}/locations/", f"{SITE}/legal/", f"{SITE}/legal/OnGuard-Protection-Legal-Compliance-Pack.pdf"}
    expected.update(f"{SITE}/locations/{loc['slug']}.html" for loc in LOCATIONS)
    expected.update(f"{SITE}/services/{svc['slug']}.html" for svc in SERVICES)
    expected.update(f"{SITE}/locations/{loc['slug']}/{svc['slug']}.html" for loc in LOCATIONS for svc in SERVICES)
    import expand_site

    expected.update(url for _name, url, _p in expand_site.extra_urls())
    missing = sorted(expected - set(seen))
    extra = sorted(set(seen) - expected)
    if missing:
        errors.append("indexable pages missing from sitemaps: " + ", ".join(missing[:12]))
    if extra:
        errors.append("unexpected sitemap URLs: " + ", ".join(extra[:12]))
    if set(master_urls) != expected:
        errors.append("sitemap.xml urlset does not match the full indexable set")
    bad_host = [u for u in master_urls if not u.startswith(SITE + "/")]
    if bad_host:
        errors.append("sitemap.xml has off-host URLs: " + ", ".join(bad_host[:6]))
    if errors:
        raise SystemExit("Sitemap validation failed:\n- " + "\n- ".join(errors))
    print(f"Validated {len(child_locs)} sitemaps and {len(seen)} unique indexable URLs.")


def main() -> None:
    for loc in LOCATIONS:
        write_location(loc)
        for svc in SERVICES:
            write_combo(loc, svc)
    for svc in SERVICES:
        write_service(svc)
    write_locations_index()
    write_thanks()
    write_404()
    import expand_site

    expand_site.write_all()
    write_tech()
    validate_sitemaps()
    combos = len(LOCATIONS) * len(SERVICES)
    print(
        f"Wrote {len(LOCATIONS)} location pages, {len(SERVICES)} service pages, "
        f"{combos} suburb-service pages, plus blog/industry/jobs pages, sitemaps and agent files."
    )


if __name__ == "__main__":
    main()
