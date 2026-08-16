#!/usr/bin/env python3
"""Blog, industry guides, and the guard-jobs data-flow page."""

from __future__ import annotations

import generate_pages as gp

BLOGS = [
    {
        "slug": "hire-sled-licensed-security-guards-nsw",
        "title": "How to hire SLED-licensed security guards in NSW",
        "desc": "A practical NSW hiring brief: Master Licence, Class 1 licences, what to ask, and how to verify OnGuard Protection on the SLED register.",
        "date": "2026-08-17",
        "hero": "work-nowra",
        "kicker": "Hiring",
        "h1": "How to hire licensed security guards in NSW",
        "lead": "If the company cannot show a current Master Licence, stop. Everything else is a briefing problem.",
        "body": [
            "New South Wales treats security as a licensed trade. Crowd control, static guarding, patrols and most event work sit under the Security Industry Act 1997. The company needs a Master Licence. Each operative needs the right Class 1 subclass for the task.",
            "OnGuard Protection holds Master Licence 000110094. Check it on the SLED public register before you send a site map. Then ask three questions: which class is on the roster, who writes the brief, and who you call at 02:00 if the post fails.",
            "A good brief names the suburb, the hours, the asset, and the risk. “Need two guards Saturday” is not a brief. “Nowra rodeo, gates from 10:00, crowd estimate 4,000, radio to first aid” is a brief. We build that in the quote form so the roster matches the job.",
            "Same-day cover is possible along the Sydney–Hunter–South Coast–Canberra spine. Planned work is cheaper and safer. Call 0432 893 343 and we will tell you the same day whether we can stand the post.",
        ],
        "bullets": [
            "Verify the Master Licence on the SLED register",
            "Match Class 1A, 1C, 1D or other subclasses to the task",
            "Write hours, suburb, crowd and access into the brief",
            "Name an after-hours contact on both sides",
        ],
    },
    {
        "slug": "nsw-security-master-licence-explained",
        "title": "What a NSW Security Master Licence actually means",
        "desc": "Master Licence 000110094 explained in plain English. Why the company licence is not the same as a guard’s Class 1 card.",
        "date": "2026-08-16",
        "hero": "work-poster",
        "kicker": "Compliance",
        "h1": "What a NSW Master Licence actually means",
        "lead": "The company licence and the guard’s card are two different things. You need both.",
        "body": [
            "A Master Licence lets a business supply security activities in NSW. It does not mean every person on site is licensed. Each operative still carries an individual licence for the activity they perform.",
            "OnGuard’s Master Licence is 000110094. Clients can verify it on the NSW Police SLED public register. If a provider will not give you a number you can check, treat that as the answer.",
            "The Master Licence is also what stands behind incident reports, insurance and the roster. When something goes wrong at a venue or a compound, the paper trail starts with who was licensed to put people on that post.",
        ],
        "bullets": [
            "Master Licence = the company may supply the work",
            "Class 1 card = that person may do that activity",
            "OnGuard: Master Licence 000110094 — verify it",
        ],
    },
    {
        "slug": "nsw-security-licence-classes-1a-to-1f",
        "title": "NSW security licence classes 1A to 1F explained",
        "desc": "Class 1A unarmed guard, 1C crowd controller, 1D dog handler and the rest of the NSW Class 1 subclasses in one page.",
        "date": "2026-08-15",
        "hero": "work-k9",
        "kicker": "Licensing",
        "h1": "NSW Class 1 security licences, without the fog",
        "lead": "The letter on the card has to match the job. A 1A is not automatically a 1C.",
        "body": [
            "Class 1A covers unarmed guarding — static posts, patrols and a lot of commercial work. Class 1B is bodyguard work. Class 1C is crowd controller, which is what licensed venues and many events actually need. Class 1D is guard dog handler. Class 1E is cash-in-transit. Class 1F is armed guard.",
            "OnGuard only deploys the subclass the brief needs. A hotel door is 1C. A construction gate at night is usually 1A. A compound with a dog team needs 1D on the handler, not a borrowed animal and a 1A card.",
            "Class 2 licences cover consulting, selling or installing equipment, locksmithing and related work. If someone is controlling access or a crowd in NSW, ask for Class 1 — not a sales story.",
        ],
        "bullets": [
            "1A unarmed guard · 1B bodyguard · 1C crowd controller",
            "1D dog handler · 1E cash-in-transit · 1F armed guard",
            "Venues and rodeos usually need 1C on the door",
        ],
    },
    {
        "slug": "crowd-control-vs-event-security-nsw",
        "title": "Crowd control vs event security in NSW",
        "desc": "When you need licensed crowd controllers for a venue, and when you need a full event security plan for a rodeo or festival.",
        "date": "2026-08-14",
        "hero": "work-festival",
        "kicker": "Events",
        "h1": "Crowd control is not the same job as event security",
        "lead": "One is a door and a floor. The other is a site plan, a radio net and a close-out.",
        "body": [
            "Crowd control in NSW is a defined security activity. Hotels, RSLs, late venues and many private functions need licensed controllers at the door and on the floor. The product is access, RSA support and ejections that do not become a second incident.",
            "Event security is the larger machine: recce, written plan, gates, back-of-house, VIP, first-aid liaison and a radio net that still works when the crowd peaks. OnGuard has stood that work at the Nowra Annual Rodeo, Worrigee Equestrian Common and the Singleton Rodeo After Party.",
            "If you only need the door, say so. If you are running a record-attendance rodeo, say that too. We roster to the risk, not to a package name.",
        ],
        "bullets": [
            "Crowd control = licensed venue and floor work",
            "Event security = plan, gates, radio, close-out",
            "Proven OnGuard sites: Nowra, Worrigee, Singleton",
        ],
    },
    {
        "slug": "static-guards-vs-mobile-patrols",
        "title": "Static guards vs mobile patrols: which NSW sites need which",
        "desc": "A static post holds a gate. A patrol randomises after-hours checks. How to choose for construction, retail and warehouses in NSW.",
        "date": "2026-08-13",
        "hero": "work-patrol",
        "kicker": "Operations",
        "h1": "Static post or mobile patrol?",
        "lead": "If the asset can walk out a gate, you usually need a body on that gate. If the risk is after hours and spread, you need a vehicle and a random pattern.",
        "body": [
            "A static guard is a licensed person who stays. Construction compounds, loading docks, retail floors and residential desks are static jobs. The product is access control that still holds at 03:00.",
            "A mobile patrol is a licensed run between sites. Lock checks, external walks, alarm attendance and a written run-sheet. OnGuard randomises timing so the pattern is not the product. The chemist-and-warehouse belt after midnight is classic patrol work.",
            "Many high-value sites run both: a night static plus two randomised mobile checks. Ask for that combination if copper, plant or vehicles are the asset.",
        ],
        "bullets": [
            "Static = one post, continuous presence",
            "Patrol = multi-site, randomised, auditable",
            "High-value sites often need both",
        ],
    },
    {
        "slug": "alarm-response-after-hours-nsw",
        "title": "After-hours alarm response for NSW commercial sites",
        "desc": "What happens when an alarm hits at 02:00 in Sydney, the Hunter or the South Coast. Keyholding, attendance and the report you should get.",
        "date": "2026-08-12",
        "hero": "work-patrol",
        "kicker": "Patrols",
        "h1": "When the alarm hits after midnight",
        "lead": "Someone licensed has to attend, or the panel is just making noise.",
        "body": [
            "Alarm response is not a call-centre script. It is a licensed attendance, a walk of the building, and a decision: reset, hold, or escalate. Keyholding only works if the keys are logged and the person holding them is licensed.",
            "OnGuard covers alarm response along the same spine as our patrols: Sydney, Hornsby, Central Coast, Newcastle, the Hunter, Southern Highlands, South Coast and into Canberra. Confirm the suburb on 0432 893 343 before you assume a 20-minute drive.",
            "You should get a written run-sheet after the visit. If the provider cannot show you last month’s sheets, they are selling a phone tree.",
        ],
        "bullets": [
            "Licensed attendance, not just a phone call",
            "Keyholding with a logged set",
            "Run-sheet after every response",
        ],
    },
    {
        "slug": "construction-site-security-nsw",
        "title": "Construction site and compound security in NSW",
        "desc": "After-hours gates, plant protection and compound control for NSW construction. What a static night post actually does.",
        "date": "2026-08-11",
        "hero": "work-k9",
        "kicker": "Construction",
        "h1": "Construction security that holds the compound",
        "lead": "Copper, plant and vehicles leave through the same gate the day crew used. The night post is the job.",
        "body": [
            "NSW construction sites lose time and money through the gate, not through a theory. A licensed static guard on after-hours access, visitor logs and lock-up is the baseline. Layer a patrol if the yard is large or the plant is high-value.",
            "OnGuard stands construction gates across Parramatta, Liverpool, the Sydney fringe and regional jobs on the South Coast and Hunter corridor. We brief the post to the site rules — not a generic mall procedure.",
            "Shutdowns and long weekends need a written roster before the last tradie leaves. Call early. Short-notice cover is possible; planned cover is cleaner.",
        ],
        "bullets": [
            "After-hours gate and compound control",
            "Plant, copper and vehicle checks",
            "Works with or without a dog team",
        ],
    },
    {
        "slug": "rsa-venue-crowd-controllers",
        "title": "RSA, licensed venues and crowd controllers in NSW",
        "desc": "Why NSW hotels and clubs need licensed crowd controllers, not just RSA staff, and what OnGuard actually does on the door.",
        "date": "2026-08-10",
        "hero": "work-screening",
        "kicker": "Venues",
        "h1": "RSA is not a security licence",
        "lead": "Responsible service of alcohol is a hospitality card. Crowd control is a SLED activity.",
        "body": [
            "A venue can have perfect RSA and still be unlicensed for crowd control. If staff are controlling entry, removing people or managing a crowd, NSW treats that as security work. The company needs a Master Licence. The person on the door needs the right Class 1 card — usually 1C.",
            "OnGuard briefs the door, holds the floor and closes the night without turning the venue into a fight. ID, ejection protocols and an incident log that still makes sense the next morning are standard.",
            "Inner-Sydney, Newcastle hospitality and regional pubs are the same legal test. The drive time changes. The licence does not.",
        ],
        "bullets": [
            "Crowd control is a licensed security activity",
            "Door, ID, RSA support, ejections, logs",
            "Master Licence 000110094 behind the roster",
        ],
    },
    {
        "slug": "event-security-plan-rodeos-festivals",
        "title": "What a real event security plan includes",
        "desc": "Site recce, radio, medical liaison and close-out. How OnGuard plans rodeos, festivals and large NSW outdoor events.",
        "date": "2026-08-09",
        "hero": "work-nowra",
        "kicker": "Events",
        "h1": "The event plan is the product",
        "lead": "Bodies without a brief are just extra people in high-vis.",
        "body": [
            "A usable event plan names gates, stewarding, back-of-house, VIP, lost children, first aid and the police liaison. It is written before the first radio goes live. OnGuard has run that method at record-attendance rodeos on the South Coast and after-parties in the Hunter.",
            "Radio discipline matters when the crowd peaks. One net, named call-signs, a person who actually answers. We do not invent a second channel at 21:00 because someone forgot batteries.",
            "Close-out is part of the job: last patron, last vehicle, last lock, a short debrief. If your last provider vanished at last drinks, say so in the brief.",
        ],
        "bullets": [
            "Written plan after a site recce",
            "Radio net that works at peak",
            "Close-out and a debrief, not a disappearing act",
        ],
    },
    {
        "slug": "bag-search-access-screening-nsw",
        "title": "Bag search and access screening at NSW events",
        "desc": "How licensed screening at the gate should work: courtesy, speed, and a line that does not become the incident.",
        "date": "2026-08-08",
        "hero": "work-screening",
        "kicker": "Access",
        "h1": "Screening that does not stall the gate",
        "lead": "The search is a security activity. The queue is a crowd-control problem. You need both skills on the same table.",
        "body": [
            "Bag search only works if the person doing it is licensed, briefed on prohibited items, and fast enough that the line does not become a second crowd. OnGuard runs screening on event entries with the same uniformed standard as the floor team.",
            "A good brief lists what is banned, what is tagged and returned, and who makes the call when someone argues. Do not leave that to a volunteer with a torch.",
            "We pair screening with licensed crowd control so a refusal at the table does not turn into a fight in the car park.",
        ],
        "bullets": [
            "Licensed officers on the table",
            "A written prohibited-item list",
            "Crowd control standing the overflow",
        ],
    },
    {
        "slug": "corporate-concierge-security-nsw",
        "title": "Corporate concierge security for NSW offices",
        "desc": "Front-of-house that can greet a client and still stop a walk-in. Concierge-grade licensed officers for Sydney, Parramatta and Canberra.",
        "date": "2026-08-07",
        "hero": "work-screening",
        "kicker": "Corporate",
        "h1": "Concierge that is still licensed security",
        "lead": "If they control access in NSW, they need a licence. Hospitality manners are extra, not a substitute.",
        "body": [
            "Corporate lobbies fail in two directions: a guard who treats every visitor like a threat, or a greeter who lets anyone through. OnGuard places licensed concierge officers who can do both jobs — welcome and stop.",
            "Contractor sign-in, loading docks and after-hours lock-up sit on the same roster as the day lobby. We brief dress and tone to the building: corporate, industrial or hospitality.",
            "Parramatta, North Sydney and Canberra offices use the same method. The postcode changes. The Master Licence does not.",
        ],
        "bullets": [
            "Licensed access control with a lobby manner",
            "Contractor and dock sign-in",
            "After-hours corporate lock-up",
        ],
    },
    {
        "slug": "k9-asset-protection-nsw",
        "title": "Dog teams and high-value site protection in NSW",
        "desc": "When a generic static post is not enough: Class 1D handlers, compounds and layered night cover.",
        "date": "2026-08-06",
        "hero": "work-k9",
        "kicker": "Assets",
        "h1": "When the asset needs more than a chair at the gate",
        "lead": "A dog team is a licensed handler plus a trained animal. It is not a pet on a night shift.",
        "body": [
            "Class 1D is the NSW subclass for guard dog handlers. The handler is licensed. The deployment is briefed. OnGuard uses dog teams on high-value compounds, plant and restricted sites where a visible deterrent and a night walk both matter.",
            "Most clients combine 1D with a static 1A and a randomised patrol. Copper, vehicles and isolated industrial lots are the usual brief.",
            "Ask to see the handler’s card and the company’s Master Licence. Do not accept a story about “the dog is trained” without the paperwork.",
        ],
        "bullets": [
            "Class 1D on the handler",
            "Layered static plus patrol",
            "For compounds, plant and isolated lots",
        ],
    },
    {
        "slug": "how-fast-can-onguard-stand-a-post",
        "title": "How fast can OnGuard stand a licensed post in NSW?",
        "desc": "Same-day cover vs planned rosters from Sydney to Canberra. What we can confirm on 0432 893 343 the day you call.",
        "date": "2026-08-05",
        "hero": "work-singleton",
        "kicker": "Response",
        "h1": "How fast can we stand the post?",
        "lead": "Planned work is the default. Short-notice cover is a same-day yes or no — not a maybe that dies at 17:00.",
        "body": [
            "Call 0432 893 343. Give the suburb, the start time and the activity. We will tell you the same day whether a licensed roster can stand it. That is the product of a company already running Sydney, the Hunter, the South Coast and Canberra — not a Sydney-only firm guessing the drive to Nowra.",
            "Record events and multi-day construction shutdowns should be booked as soon as the date is real. Last-minute venue cover is common. We will not invent bodies we do not have.",
            "If we cannot take it, you will hear that. A late no is worse than an early no.",
        ],
        "bullets": [
            "Same-day confirmation on most briefs",
            "Spine: Sydney–Hunter–South Coast–Canberra",
            "We will say no if the roster is not there",
        ],
    },
    {
        "slug": "hunter-valley-event-security",
        "title": "Event and venue security in the Hunter Valley",
        "desc": "Newcastle hospitality, Singleton after-parties and Cessnock cellar-door crowds. How OnGuard covers the Hunter.",
        "date": "2026-08-04",
        "hero": "work-singleton",
        "kicker": "Hunter",
        "h1": "Hunter Valley security is late, local and licensed",
        "lead": "We have already stood the Singleton Rodeo After Party at the Imperial Hotel. That is not a sales suburb.",
        "body": [
            "The Hunter mixes night hospitality in Newcastle with seasonal cellar-door and rodeo work up the valley. OnGuard treats Newcastle, Singleton and Cessnock as one operating area. Same Master Licence. Same radio standard.",
            "Wine tourism weekends need crowd control that looks like hospitality. After-parties need a door that holds. Industrial nights around the port and the mines need a different brief. We write the brief to the site.",
            "If you want one company for a Newcastle venue and a Hunter event in the same week, that is a normal ask for us.",
        ],
        "bullets": [
            "Proven at Singleton Imperial Hotel",
            "Newcastle + valley on one roster",
            "Venue, event and industrial briefs",
        ],
    },
    {
        "slug": "south-coast-event-security-nowra-worrigee",
        "title": "South Coast event security: Nowra and Worrigee",
        "desc": "OnGuard’s real South Coast work — Nowra Annual Rodeo and Worrigee Equestrian Common — and how we cover the Illawarra down.",
        "date": "2026-08-03",
        "hero": "work-worrigee",
        "kicker": "South Coast",
        "h1": "South Coast work we have already stood",
        "lead": "Nowra and Worrigee are job sites, not SEO towns.",
        "body": [
            "OnGuard provided event security for the Nowra Annual Rodeo with the Nowra Rodeo Association, including a record-attendance day. We also stood licensed security at Worrigee Equestrian Common for attendees, staff and competitors.",
            "That means a South Coast brief starts with a team that already knows the drive, the ground and the close-out. Wollongong and the Highlands sit on the same corridor.",
            "Rodeos, gymkhanas, river events and regional venues are the usual mix. Bring the date and the crowd estimate. We will write the rest.",
        ],
        "bullets": [
            "Nowra Annual Rodeo — real job",
            "Worrigee Equestrian Common — real job",
            "Illawarra and Highlands on the same spine",
        ],
    },
    {
        "slug": "canberra-act-security-corridor",
        "title": "Canberra and ACT security on the NSW corridor",
        "desc": "How OnGuard covers Canberra / ACT from the Sydney–Highlands spine. What we confirm before we roster the job.",
        "date": "2026-08-02",
        "hero": "work-poster",
        "kicker": "ACT",
        "h1": "Canberra is on the published map",
        "lead": "We do not pretend an NSW Master Licence is an ACT one. We tell you how the job is licensed before we take it.",
        "body": [
            "OnGuard lists Canberra and the ACT on the coverage map: Hunter Valley through to Canberra regions. Corporate concierge, event security and construction static are the usual ACT-side briefs.",
            "Mutual recognition for individual operatives is a legal question, not a slogan. Confirm the site and we will tell you how we licence and roster it. No interstate Master Licence claim.",
            "The Highlands and South Coast already sit on the drive. That is why the corridor works as one company instead of two subcontractors.",
        ],
        "bullets": [
            "ACT is listed coverage — confirm the site",
            "No fabricated interstate master licence",
            "Same brief standard as NSW jobs",
        ],
    },
    {
        "slug": "what-to-put-in-a-security-brief",
        "title": "What to put in a security brief (NSW)",
        "desc": "Suburb, hours, asset, crowd, access and the 02:00 phone number. The short brief OnGuard actually uses.",
        "date": "2026-08-01",
        "hero": "work-festival",
        "kicker": "Briefs",
        "h1": "The brief is four facts and a phone number",
        "lead": "If we have to guess the risk, we will guess high or we will decline.",
        "body": [
            "Write the suburb and postcode. Write the start and finish, including bump-in. Write what is being protected — people, plant, a licensed venue, a gate. Write the crowd or the traffic if you know it. Write who we call when it goes wrong.",
            "OnGuard’s quote form builds that live: location, service, hours, then your details. The email that lands in admin@ogprotection.com.au should be enough to roster from.",
            "Photos of the gate or the floor help. A PDF site map helps more. A vibe does not.",
        ],
        "bullets": [
            "Where, when, what, how many, who to call",
            "Use the on-site brief form or call 0432 893 343",
            "Site maps beat adjectives",
        ],
    },
    {
        "slug": "incident-reporting-after-the-shift",
        "title": "Incident reporting that still makes sense tomorrow",
        "desc": "What a usable NSW security incident log contains, and why OnGuard treats the report as part of the shift.",
        "date": "2026-07-31",
        "hero": "work-screening",
        "kicker": "Reports",
        "h1": "If it is not written, it did not happen",
        "lead": "Venues, insurers and police do not work from a story told at 11:00 the next day.",
        "body": [
            "A usable log has time, location, people, what was seen, what was done, and who was told. It is written before the officer leaves the car park. OnGuard treats that as part of the paid hour, not homework.",
            "Ejections, medicals, thefts and alarm attendances all need the same spine. The tone is factual. No novels. No missing names.",
            "Ask your current provider for last Saturday’s logs. The quality of that page is the quality of the company.",
        ],
        "bullets": [
            "Time, place, people, action, notification",
            "Written before close-out",
            "Stands up to an insurer or a licensing check",
        ],
    },
    {
        "slug": "after-hours-commercial-lockup-nsw",
        "title": "After-hours commercial lock-up in NSW",
        "desc": "Who holds the keys, who walks the building, and what a lock-up run-sheet should show your facilities manager.",
        "date": "2026-07-30",
        "hero": "work-patrol",
        "kicker": "Lock-up",
        "h1": "Lock-up is a licensed walk, not a dash to the car",
        "lead": "The last person out is often the first gap in the building.",
        "body": [
            "Commercial lock-up is a circuit: doors, plant rooms, car park, alarm set, keys logged. OnGuard runs it as a named procedure for offices and retail, not a favour on the way home.",
            "Sydney CBD, Parramatta towers and regional high streets use the same checklist with different timings. Pair it with a later randomised patrol if the building sits empty until Monday.",
            "Keyholding stays with licensed officers. We do not leave a spare under a mat and call it a system.",
        ],
        "bullets": [
            "Written circuit and alarm set",
            "Licensed keyholding",
            "Optional second patrol after lock-up",
        ],
    },
    {
        "slug": "retail-loss-prevention-nsw",
        "title": "Retail security and loss prevention in NSW",
        "desc": "Floor presence, after-hours lock-up and patrols for NSW retail. How OnGuard works a shop without turning it into a fortress.",
        "date": "2026-07-29",
        "hero": "work-screening",
        "kicker": "Retail",
        "h1": "Retail security that still lets people shop",
        "lead": "Loss prevention is presence and process. It is not a tackle in the aisle.",
        "body": [
            "A licensed floor presence deters and observes. After hours, lock-up and patrols do the rest. OnGuard briefs retail posts to the brand: some sites want a visible vest, some want a quieter corporate look.",
            "Chatswood, Hornsby, Parramatta and regional strips are regular retail geography for us. The legal standard is the same as a construction gate — licensed people, written incidents.",
            "If you only want weekends, say so. If you want random night visits plus Saturday floor, say that. We will not upsell a 24/7 static you do not need.",
        ],
        "bullets": [
            "Licensed floor presence",
            "After-hours lock-up and patrols",
            "Briefed to the brand, not a generic mall script",
        ],
    },
    {
        "slug": "wedding-private-function-security-nsw",
        "title": "Wedding and private function security in NSW",
        "desc": "Discreet licensed cover for Highlands weddings, Hunter cellar doors and private Sydney functions.",
        "date": "2026-07-28",
        "hero": "work-festival",
        "kicker": "Functions",
        "h1": "Guests should notice the event, not the security plan",
        "lead": "Highlands and Hunter functions fail when security looks like a festival gate.",
        "body": [
            "Weddings, birthdays and cellar-door events still need licensed people if you are controlling access or a crowd. The brief is discreet: parking, gate, a quiet intervention, a named family contact.",
            "Bowral, Cessnock and inner-Sydney private rooms are typical. We match dress to the invitation — not a default high-vis if the host did not ask for it.",
            "Give us the guest count, the finish time and whether alcohol is the main risk. We will not bring a rodeo roster to a garden ceremony.",
        ],
        "bullets": [
            "Licensed, discreet, briefed to the host",
            "Highlands, Hunter and Sydney functions",
            "Dress standard agreed in the brief",
        ],
    },
    {
        "slug": "verify-security-company-sled-register",
        "title": "How to verify a NSW security company on the SLED register",
        "desc": "A three-step check of Master Licence 000110094 and why you should run it before any quote.",
        "date": "2026-07-27",
        "hero": "work-poster",
        "kicker": "Verify",
        "h1": "Check the register before you check the price",
        "lead": "The SLED public register is free. Use it.",
        "body": [
            "Go to the NSW Police SLED public register. Search the company or the Master Licence number. OnGuard Protection is 000110094. Confirm the name matches the invoice entity.",
            "Then ask for the individual licence classes that will be on your site. A valid company licence plus the wrong subclass on the door is still the wrong job.",
            "We link the register from the site header. If another provider makes you hunt for a PDF, that is information.",
        ],
        "bullets": [
            "SLED public register — free to search",
            "OnGuard Master Licence 000110094",
            "Then match Class 1 subclasses to the task",
        ],
    },
    {
        "slug": "247-vs-overnight-security-cover",
        "title": "24/7 cover vs overnight-only security",
        "desc": "When a NSW site needs a full-day roster and when overnight static plus patrols is the honest product.",
        "date": "2026-07-26",
        "hero": "work-k9",
        "kicker": "Rosters",
        "h1": "Do not buy 24/7 if the risk is a night gate",
        "lead": "Hours should follow the risk, not a brochure.",
        "body": [
            "24/7 is three shifts and a handover. Overnight-only is one post and a morning lock-open. Most construction compounds and many warehouses need the night, not the Tuesday afternoon.",
            "OnGuard will recommend overnight static, weekend cover or a full week after a short brief. We will not invent a 24/7 package because it invoices better.",
            "Multi-site clients often mix: a 24/7 lobby in the city and overnight patrols on the yard. One company can hold both if the spine already runs that way.",
        ],
        "bullets": [
            "Match hours to the risk",
            "Overnight + patrol is a common honest mix",
            "24/7 only when the site is actually live",
        ],
    },
    {
        "slug": "multi-site-security-sydney-to-canberra",
        "title": "Multi-site security quotes from Sydney to Canberra",
        "desc": "One licensed provider for a CBD lobby, a Hunter event and a South Coast compound. How OnGuard quotes a corridor.",
        "date": "2026-07-25",
        "hero": "work-poster",
        "kicker": "Coverage",
        "h1": "One spine, several posts, one invoice",
        "lead": "The point of a corridor company is that Campbelltown and Bowral are not two subcontractors.",
        "body": [
            "OnGuard already rosters Sydney, Hornsby, the Central Coast, Newcastle, the Hunter, the Highlands, the South Coast and Canberra. A multi-site brief is normal: a Parramatta lobby and a Nowra event in the same month, or a construction gate plus a weekend festival.",
            "We quote the sites together so you are not reconciling two Master Licences. The brief still has to be specific per site.",
            "Ask for a multi-site quote in the form. Name every suburb. We will tell you which we can stand and which we cannot.",
        ],
        "bullets": [
            "Sydney to Canberra is one operating spine",
            "Per-site briefs, one company",
            "We will decline a town we cannot honestly cover",
        ],
    },
    {
        "slug": "what-fully-insured-security-should-cover",
        "title": "What “fully insured” should mean on a NSW security quote",
        "desc": "Public liability, workers compensation and why a slogan is not a certificate of currency.",
        "date": "2026-07-24",
        "hero": "work-nowra",
        "kicker": "Insurance",
        "h1": "Ask for the certificate, not the adjective",
        "lead": "Fully insured is a claim. A current certificate of currency is evidence.",
        "body": [
            "NSW clients should see public liability and workers compensation that match the work. Event days and construction nights are not the same risk. Ask for the certificate dated for the period of the job.",
            "OnGuard’s legal pack sets out liability and ACL positions in writing. We will not hide behind “all care no responsibility”. That wording is unlawful if it tries to wipe consumer guarantees.",
            "If a quote is silent on insurance, treat the price as incomplete.",
        ],
        "bullets": [
            "Certificate of currency, not a slogan",
            "Liability + workers compensation",
            "Read the legal pack before you sign",
        ],
    },
    {
        "slug": "radio-comms-at-event-peak",
        "title": "Radio comms when the crowd peaks",
        "desc": "Why event radios fail at 21:00 and how OnGuard briefs a net that still answers.",
        "date": "2026-07-23",
        "hero": "work-nowra",
        "kicker": "Events",
        "h1": "If the radio dies at peak, the plan died first",
        "lead": "Batteries, call-signs and one person who is allowed to talk.",
        "body": [
            "Event radios fail from dead batteries, two nets, and everyone transmitting at once. The fix is boring: charged spares, named call-signs, a control point, and a rule about who speaks in a medical.",
            "OnGuard puts that in the written event plan. Nowra and Singleton jobs used the same method. The crowd size changed. The net did not.",
            "If your last event was “we used phones”, say so. We will not pretend a WhatsApp group is a radio net.",
        ],
        "bullets": [
            "One net, named call-signs",
            "Spares before gates open",
            "Control point for medicals and ejections",
        ],
    },
    {
        "slug": "residential-community-access-control",
        "title": "Residential community access control in NSW",
        "desc": "Concierge desks, boom gates and after-hours patrols for NSW residential communities without turning the lobby into a venue.",
        "date": "2026-07-22",
        "hero": "work-worrigee",
        "kicker": "Residential",
        "h1": "A residential desk is still a licensed post",
        "lead": "Residents want a person who knows the building. The law still wants a licence.",
        "body": [
            "Access control, visitor logs and after-hours patrols in a residential community are security activities when they control entry. OnGuard briefs these posts quieter than a festival gate and tighter than an unattended intercom.",
            "Growth corridors — Campbelltown, Western Sydney, Canberra apartments — are the usual mix. We can pair a day concierge with night patrols.",
            "Give us the access hardware and the by-laws that matter. We will not invent a nightclub ejection policy for a family lobby.",
        ],
        "bullets": [
            "Licensed concierge and after-hours patrols",
            "Visitor logs that match the building rules",
            "Quieter brief than a venue",
        ],
    },
    {
        "slug": "warehouse-logistics-night-patrols",
        "title": "Warehouse and logistics night patrols in NSW",
        "desc": "Randomised mobile patrols and alarm response for Western Sydney yards, South-west logistics and regional warehouses.",
        "date": "2026-07-21",
        "hero": "work-patrol",
        "kicker": "Logistics",
        "h1": "The yard is the asset after 18:00",
        "lead": "Trucks leave. Copper and batteries do not lock themselves.",
        "body": [
            "Logistics sites in Blacktown, Liverpool and the industrial edges of Newcastle fail after hours. OnGuard runs marked or unmarked patrols with randomised timing, lock checks and alarm attendance.",
            "A written run-sheet after every visit is the product you can audit. If you need a night static on the gate plus two mobile checks, say so in one brief.",
            "We already treat Western Sydney and the Hunter industrial belt as regular geography. Confirm the suburb. Do not assume a 2:00 attendance from a Sydney-only roster.",
        ],
        "bullets": [
            "Randomised multi-visit patrols",
            "Alarm response and lock checks",
            "Run-sheets you can show a loss-adjuster",
        ],
    },
    {
        "slug": "why-randomised-patrol-timing-matters",
        "title": "Why randomised patrol timing matters",
        "desc": "Fixed 02:00 visits train thieves. How OnGuard randomises NSW mobile patrols without missing the brief.",
        "date": "2026-07-20",
        "hero": "work-patrol",
        "kicker": "Patrols",
        "h1": "If they can set a watch by you, you are the product",
        "lead": "A patrol at the same minute every night is a timetable, not a deterrent.",
        "body": [
            "OnGuard randomises visit order and windows inside the contracted band. The site still gets the agreed number of visits. The pattern is not posted on the street.",
            "Run-sheets still show time on and time off, so you can audit us. Random does not mean missing. It means not predictable from the car park opposite.",
            "Ask any provider to show a week of actual times. If every visit is 02:04, you are paying for a habit.",
        ],
        "bullets": [
            "Agreed visit count, unagreed clock time",
            "Auditable run-sheets",
            "Harder to watch than a fixed loop",
        ],
    },
    {
        "slug": "first-shift-briefing-checklist",
        "title": "First-shift briefing checklist for NSW sites",
        "desc": "Access, hazards, radios, keys and the named client contact. What OnGuard walks before the first hour is billed.",
        "date": "2026-07-19",
        "hero": "work-worrigee",
        "kicker": "Briefs",
        "h1": "The first hour is a walk, not a sit",
        "lead": "If the officer has not walked the boundary, they are not on the post yet.",
        "body": [
            "A first shift needs keys or codes, a hazard list, the radio or phone tree, the toilet and tea rule, and the person who answers at 02:00. OnGuard writes that into the live brief so the officer is not inventing it at the gate.",
            "Construction, venues and offices use the same checklist with different hazards. A crane exclusion zone is not a dance floor. Both still need a named contact.",
            "Send photos and a PDF map with the quote if you have them. We will still walk it.",
        ],
        "bullets": [
            "Keys, hazards, comms, welfare, escalation",
            "Walk the boundary on hour one",
            "Named 02:00 contact on both sides",
        ],
    },
]

INDUSTRIES = [
    {
        "slug": "construction",
        "name": "Construction & compounds",
        "title": "Construction Site Security NSW | OnGuard Protection",
        "desc": "After-hours gates, plant protection and compound control for NSW construction. SLED licensed. Master Licence 000110094.",
        "hero": "work-k9",
        "lead": "The gate is the job. Plant and copper leave through it if nobody licensed is on it.",
        "body": "OnGuard stands construction statics and after-hours compounds from Sydney’s growth corridors through to regional jobs on the South Coast and Hunter spine. Access control, visitor logs and lock-up are the product — not a chair and a phone.",
    },
    {
        "slug": "hospitality",
        "name": "Hospitality & licensed venues",
        "title": "Hospitality & Venue Security NSW | OnGuard Protection",
        "desc": "Licensed crowd control for hotels, RSLs, late venues and functions across Sydney, Newcastle and regional NSW.",
        "hero": "work-screening",
        "lead": "The door is a licence test. RSA is not enough.",
        "body": "Class 1C crowd controllers for hotels, clubs and late rooms. We brief the door, hold the floor and close the night. Inner-Sydney, Newcastle hospitality and regional pubs use the same legal standard.",
    },
    {
        "slug": "events",
        "name": "Events, rodeos & festivals",
        "title": "Event Security for NSW Rodeos & Festivals | OnGuard",
        "desc": "Event plans, radios and licensed presence. Proven at Nowra, Worrigee and Singleton. Master Licence 000110094.",
        "hero": "work-nowra",
        "lead": "We have already held a record crowd on the South Coast.",
        "body": "Written plans, gates, screening and close-out for rodeos, festivals and private functions. Nowra Annual Rodeo, Worrigee Equestrian Common and the Singleton Rodeo After Party are work we have stood — not suburbs we invented.",
    },
    {
        "slug": "retail",
        "name": "Retail & shopping precincts",
        "title": "Retail Security Guards NSW | OnGuard Protection",
        "desc": "Licensed floor presence, lock-up and patrols for NSW retail precincts. Hornsby to regional high streets.",
        "hero": "work-screening",
        "lead": "Presence on the floor. Process after hours.",
        "body": "Retail posts are briefed to the brand. Day floor, weekend peaks and night lock-up can sit on one roster. Chatswood, Hornsby, Parramatta and regional strips are regular geography.",
    },
    {
        "slug": "logistics",
        "name": "Logistics, warehouses & yards",
        "title": "Warehouse & Logistics Security NSW | OnGuard Protection",
        "desc": "Night statics, randomised patrols and alarm response for NSW warehouses and logistics yards.",
        "hero": "work-patrol",
        "lead": "After 18:00 the yard is the asset.",
        "body": "Western Sydney, south-west logistics and Hunter industrial lots get randomised patrols, lock checks and alarm attendance. High-value yards often add a night static. Run-sheets come with the visit.",
    },
    {
        "slug": "corporate",
        "name": "Corporate offices",
        "title": "Corporate Office Security NSW & ACT | OnGuard Protection",
        "desc": "Licensed concierge and after-hours lock-up for offices in Sydney, Parramatta, Newcastle and Canberra.",
        "hero": "work-screening",
        "lead": "Greet the client. Stop the walk-in.",
        "body": "Corporate concierge is licensed access control with a lobby manner. Contractor sign-in, docks and night lock-up sit on the same brief. Dress standard matches the building.",
    },
    {
        "slug": "residential",
        "name": "Residential communities",
        "title": "Residential Community Security NSW | OnGuard Protection",
        "desc": "Concierge desks, access control and night patrols for NSW residential communities.",
        "hero": "work-worrigee",
        "lead": "A quieter post. Still a licensed one.",
        "body": "Visitor management and after-hours patrols for residential buildings and communities. Growth corridors in Western Sydney, Macarthur and Canberra apartments are typical. We brief to the by-laws, not a venue script.",
    },
    {
        "slug": "industrial",
        "name": "Industrial & high-value plant",
        "title": "Industrial & Plant Protection NSW | OnGuard Protection",
        "desc": "Layered static, patrol and dog-team options for high-value NSW industrial sites and compounds.",
        "hero": "work-k9",
        "lead": "A chair at the gate is not a treatment plan.",
        "body": "High-value plant, vehicles and isolated lots get a site-specific mix: night static, randomised patrol, Class 1D handler where the brief needs it. Custom procedures, not a roster dump.",
    },
    {
        "slug": "pharmacy-retail-nights",
        "name": "Pharmacy & late retail",
        "title": "Pharmacy & Late Retail Patrols NSW | OnGuard Protection",
        "desc": "Night mobile patrols and alarm response for NSW chemists and late retail. Marked patrol presence after hours.",
        "hero": "work-patrol",
        "lead": "Late retail is a patrol problem more often than a 24/7 static.",
        "body": "Chemists, late convenience and isolated retail pads get randomised mobile visits and alarm response. The marked ute is the deterrent. The run-sheet is the audit. Confirm the suburb — we already run this work on the night spine.",
    },
    {
        "slug": "government-adjacent",
        "name": "Government-adjacent sites",
        "title": "Government-Adjacent Security NSW & ACT | OnGuard",
        "desc": "Discreet licensed cover for government-adjacent offices, construction and events on the Sydney–Canberra corridor.",
        "hero": "work-poster",
        "lead": "Discreet. Licensed. No invented clearances.",
        "body": "Government-adjacent offices, construction and events need a company that will not invent Defence certificates. OnGuard states what we hold — Master Licence 000110094 — and how we licence an ACT-side job before we take it. Read the legal pack for the long version.",
    },
]


def _hero(stem: str) -> tuple[int, int, str]:
    return gp.HERO_META.get(stem, (gp.OG_W, gp.OG_H, gp.OG_ALT))


def write_blog_index() -> None:
    depth = 1
    url = f"{gp.SITE}/blog/"
    cards = ""
    for post in BLOGS:
        cards += f'''
        <article class="loc-card reveal">
          <a href="{post["slug"]}.html">
            <p class="eyebrow">{post["kicker"]} · {post["date"]}</p>
            <h2>{post["h1"]}</h2>
            <p>{post["lead"]}</p>
          </a>
        </article>'''
    item_list = {
        "@type": "ItemList",
        "name": "OnGuard Protection security guides",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": f"{gp.SITE}/blog/{p['slug']}.html", "name": p["title"]}
            for i, p in enumerate(BLOGS)
        ],
    }
    nav, footer = gp.chrome(depth, "blog")
    title = "NSW Security Guides & Briefs | OnGuard Protection"
    desc = "Plain-English NSW security guides: SLED licences, crowd control, patrols, event plans and how to brief a licensed post. Master Licence 000110094."
    html = f'''{gp.head(title, desc, url, depth, gp.OG_IMAGE, gp.OG_W, gp.OG_H, gp.OG_ALT, [gp.org_schema(), item_list])}
<body class="inner-page">
{nav}
<main id="main">
  <nav class="crumbs container" aria-label="Breadcrumb">
    <a href="../index.html">Home</a>
    <span aria-hidden="true">/</span>
    <span>Blog</span>
  </nav>
  <div class="container section-header loc-index-head">
    <p class="eyebrow">Guides</p>
    <h1>NSW security briefs you can actually use</h1>
    <p class="lead">Licensing, rosters and event plans — written the way we take a job, not as keyword filler.</p>
  </div>
  <div class="container loc-grid">{cards}</div>
  {gp.share_bar(url, title)}
  {gp.quote_form()}
</main>
{footer}
</body>
</html>'''
    out = gp.ROOT / "blog" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")


def write_blog_post(post: dict) -> None:
    depth = 1
    url = f"{gp.SITE}/blog/{post['slug']}.html"
    w, h, alt = _hero(post["hero"])
    crumbs = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{gp.SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{gp.SITE}/blog/"},
            {"@type": "ListItem", "position": 3, "name": post["h1"], "item": url},
        ],
    }
    article = {
        "@type": "BlogPosting",
        "headline": post["title"],
        "datePublished": post["date"],
        "dateModified": post["date"],
        "author": {"@type": "Organization", "name": "OnGuard Protection"},
        "publisher": {"@id": f"{gp.SITE}/#business"},
        "image": f"{gp.SITE}/{gp.OG_IMAGE}",
        "mainEntityOfPage": url,
        "inLanguage": "en-AU",
    }
    paras = "".join(f"<p>{p}</p>" for p in post["body"])
    bullets = "".join(f"<li>{b}</li>" for b in post["bullets"])
    more = "".join(
        f'<li><a href="{other["slug"]}.html">{other["h1"]}</a></li>'
        for other in BLOGS
        if other["slug"] != post["slug"]
    )
    nav, footer = gp.chrome(depth, "blog")
    extra = f'<link rel="preload" as="image" href="../assets/img/{post["hero"]}-800.webp" type="image/webp">'
    html = f'''{gp.head(post["title"], post["desc"], url, depth, gp.OG_IMAGE, gp.OG_W, gp.OG_H, gp.OG_ALT, [gp.org_schema(), crumbs, article], extra)}
<body class="inner-page">
{nav}
<main id="main">
  <nav class="crumbs container" aria-label="Breadcrumb">
    <a href="../index.html">Home</a>
    <span aria-hidden="true">/</span>
    <a href="index.html">Blog</a>
    <span aria-hidden="true">/</span>
    <span>{post["kicker"]}</span>
  </nav>
  <header class="page-hero">
    <div class="page-hero-media">
      {gp.img_tag(post["hero"], alt, w, h, depth, eager=True, sizes="100vw")}
    </div>
    <div class="container page-hero-copy hero-in">
      <p class="eyebrow">{post["kicker"]} · {post["date"]}</p>
      <h1>{post["h1"]}</h1>
      <p class="lead">{post["lead"]}</p>
    </div>
  </header>
  <article class="container prose reveal">
    <p class="answer-block">{post["lead"]}</p>
    {paras}
    <h2>Takeaways</h2>
    <ul>{bullets}</ul>
    <p>Need the post stood? Call <a href="tel:{gp.TEL}">{gp.PHONE}</a> or use the brief below. Master Licence {gp.LICENCE}.</p>
    {gp.share_bar(url, post["title"])}
    <h2>More guides</h2>
    <ul class="link-list">{more}</ul>
  </article>
  {gp.quote_form()}
</main>
{footer}
</body>
</html>'''
    (gp.ROOT / "blog" / f"{post['slug']}.html").write_text(html, encoding="utf-8")


def write_industries_index() -> None:
    depth = 1
    url = f"{gp.SITE}/industries/"
    cards = ""
    for ind in INDUSTRIES:
        cards += f'''
        <article class="loc-card reveal">
          <a href="{ind["slug"]}.html">
            <h2>{ind["name"]}</h2>
            <p>{ind["lead"]}</p>
          </a>
        </article>'''
    item_list = {
        "@type": "ItemList",
        "name": "OnGuard Protection industries",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": f"{gp.SITE}/industries/{ind['slug']}.html", "name": ind["name"]}
            for i, ind in enumerate(INDUSTRIES)
        ],
    }
    nav, footer = gp.chrome(depth, "industries")
    title = "Security by Industry NSW | OnGuard Protection"
    desc = "Licensed NSW security by industry: construction, hospitality, events, retail, logistics, corporate, residential and high-value plant. ML 000110094."
    html = f'''{gp.head(title, desc, url, depth, gp.OG_IMAGE, gp.OG_W, gp.OG_H, gp.OG_ALT, [gp.org_schema(), item_list])}
<body class="inner-page">
{nav}
<main id="main">
  <nav class="crumbs container" aria-label="Breadcrumb">
    <a href="../index.html">Home</a>
    <span aria-hidden="true">/</span>
    <span>Industries</span>
  </nav>
  <div class="container section-header loc-index-head">
    <p class="eyebrow">Sectors</p>
    <h1>Security briefed to the industry</h1>
    <p class="lead">The licence is the same. The post is not. Pick the sector that matches the risk.</p>
  </div>
  <div class="container loc-grid">{cards}</div>
  {gp.share_bar(url, title)}
  {gp.quote_form()}
</main>
{footer}
</body>
</html>'''
    out = gp.ROOT / "industries" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")


def write_industry(ind: dict) -> None:
    depth = 1
    url = f"{gp.SITE}/industries/{ind['slug']}.html"
    w, h, alt = _hero(ind["hero"])
    crumbs = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{gp.SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Industries", "item": f"{gp.SITE}/industries/"},
            {"@type": "ListItem", "position": 3, "name": ind["name"], "item": url},
        ],
    }
    service = {
        "@type": "Service",
        "name": f"{ind['name']} security — OnGuard Protection",
        "provider": {"@id": f"{gp.SITE}/#business"},
        "areaServed": ["NSW", "ACT"],
        "url": url,
    }
    svc_links = "".join(
        f'<li><a href="../services/{s["slug"]}.html">{s["name"]}</a></li>' for s in gp.SERVICES
    )
    others = "".join(
        f'<li><a href="{o["slug"]}.html">{o["name"]}</a></li>' for o in INDUSTRIES if o["slug"] != ind["slug"]
    )
    nav, footer = gp.chrome(depth, "industries")
    extra = f'<link rel="preload" as="image" href="../assets/img/{ind["hero"]}-800.webp" type="image/webp">'
    html = f'''{gp.head(ind["title"], ind["desc"], url, depth, gp.OG_IMAGE, gp.OG_W, gp.OG_H, gp.OG_ALT, [gp.org_schema(), crumbs, service], extra)}
<body class="inner-page">
{nav}
<main id="main">
  <nav class="crumbs container" aria-label="Breadcrumb">
    <a href="../index.html">Home</a>
    <span aria-hidden="true">/</span>
    <a href="index.html">Industries</a>
    <span aria-hidden="true">/</span>
    <span>{ind["name"]}</span>
  </nav>
  <header class="page-hero">
    <div class="page-hero-media">
      {gp.img_tag(ind["hero"], alt, w, h, depth, eager=True, sizes="100vw")}
    </div>
    <div class="container page-hero-copy hero-in">
      <p class="eyebrow">Industry brief</p>
      <h1>{ind["name"]}</h1>
      <p class="lead">{ind["lead"]}</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#quote">Quote this sector</a>
        <a class="btn btn-outline" href="tel:{gp.TEL}">Call {gp.PHONE}</a>
      </div>
    </div>
  </header>
  <article class="container prose reveal">
    <p class="answer-block"><strong>OnGuard Protection provides SLED-licensed security for {ind["name"].lower()} in NSW and the ACT.</strong> Master Licence {gp.LICENCE}.</p>
    <p>{ind["body"]}</p>
    <h2>Services we attach to this brief</h2>
    <ul class="link-list">{svc_links}</ul>
    <h2>Other sectors</h2>
    <ul class="link-list">{others}</ul>
    {gp.share_bar(url, ind["title"])}
  </article>
  {gp.quote_form()}
</main>
{footer}
</body>
</html>'''
    (gp.ROOT / "industries" / f"{ind['slug']}.html").write_text(html, encoding="utf-8")


def write_jobs_dfd() -> None:
    depth = 1
    url = f"{gp.SITE}/jobs/"
    title = "Guard jobs portal & data flow | OnGuard Protection"
    desc = "OnGuard guard portal: Firebase sign-in, verified-guard KYC, availability, super admin job delegation. Public roster after 10 verified guards."
    nav, footer = gp.chrome(depth, "jobs")
    crumbs = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{gp.SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Jobs", "item": url},
        ],
    }
    html = f'''{gp.head(title, desc, url, depth, gp.OG_IMAGE, gp.OG_W, gp.OG_H, gp.OG_ALT, [gp.org_schema(), crumbs])}
<body class="inner-page jobs-page">
{nav}
<main id="main">
  <nav class="crumbs container" aria-label="Breadcrumb">
    <a href="../index.html">Home</a>
    <span aria-hidden="true">/</span>
    <span>Jobs</span>
  </nav>
  <div class="container section-header loc-index-head">
    <p class="eyebrow">Guard portal · two tiers</p>
    <h1>Jobs system data flow</h1>
    <p class="lead">Tier 1 is the working core: sign-in, guard-only access, KYC, availability and super-admin delegation. Tier 2 — public roster and homepage search — waits until 10 verified guards are live.</p>
  </div>

  <section class="container dfd-legend" aria-label="How to read the diagram">
    <span class="dfd-pill dfd-pill-actor">Person</span>
    <span class="dfd-pill dfd-pill-sys">System</span>
    <span class="dfd-pill dfd-pill-store">Store</span>
    <span class="dfd-pill dfd-pill-t1">Tier 1 — build now</span>
    <span class="dfd-pill dfd-pill-t2">Tier 2 — after 10 verified guards</span>
  </section>

  <figure class="container dfd" aria-label="OnGuard jobs data flow diagram">
    <svg viewBox="0 0 1100 980" role="img" aria-labelledby="dfd-title dfd-desc">
      <title id="dfd-title">OnGuard Protection guard jobs data flow</title>
      <desc id="dfd-desc">Clients send job requests to super admin. Guards sign in with Firebase, pass guard-only verification and KYC, then manage availability. Super admin searches verified guards and delegates tasks. Public search is phase two.</desc>
      <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="#c22712"/>
        </marker>
        <marker id="arrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="#9aa3b5"/>
        </marker>
      </defs>

      <text x="20" y="28" fill="#9aa3b5" font-size="13" font-family="Barlow, sans-serif">TIER 1 — CORE (authentication, KYC, availability, delegation)</text>

      <rect x="20" y="48" width="160" height="64" rx="8" fill="#122556" stroke="#f3eee6"/>
      <text x="100" y="76" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">CLIENT</text>
      <text x="100" y="94" text-anchor="middle" fill="#9aa3b5" font-size="11">quote / job request</text>

      <rect x="260" y="48" width="200" height="64" rx="8" fill="#10182b" stroke="#c22712"/>
      <text x="360" y="76" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">SUPER ADMIN</text>
      <text x="360" y="94" text-anchor="middle" fill="#9aa3b5" font-size="11">search · delegate tasks</text>

      <rect x="540" y="48" width="200" height="64" rx="8" fill="#10182b" stroke="#c22712"/>
      <text x="640" y="76" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">JOB STORE</text>
      <text x="640" y="94" text-anchor="middle" fill="#9aa3b5" font-size="11">shifts · status · site brief</text>

      <rect x="820" y="48" width="260" height="64" rx="8" fill="#10182b" stroke="#c22712"/>
      <text x="950" y="76" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">NOTIFICATIONS</text>
      <text x="950" y="94" text-anchor="middle" fill="#9aa3b5" font-size="11">push / email / SMS to guard</text>

      <line x1="180" y1="80" x2="260" y2="80" stroke="#c22712" stroke-width="2" marker-end="url(#arrow)"/>
      <line x1="460" y1="80" x2="540" y2="80" stroke="#c22712" stroke-width="2" marker-end="url(#arrow)"/>
      <line x1="740" y1="80" x2="820" y2="80" stroke="#c22712" stroke-width="2" marker-end="url(#arrow)"/>

      <rect x="20" y="170" width="160" height="64" rx="8" fill="#122556" stroke="#f3eee6"/>
      <text x="100" y="198" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">GUARD</text>
      <text x="100" y="216" text-anchor="middle" fill="#9aa3b5" font-size="11">applicant / officer</text>

      <rect x="260" y="170" width="200" height="88" rx="8" fill="#10182b" stroke="#c22712"/>
      <text x="360" y="198" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">FIREBASE AUTH</text>
      <text x="360" y="216" text-anchor="middle" fill="#9aa3b5" font-size="11">Google · email · phone</text>
      <text x="360" y="234" text-anchor="middle" fill="#9aa3b5" font-size="11">session token</text>

      <rect x="540" y="170" width="200" height="88" rx="8" fill="#10182b" stroke="#c22712"/>
      <text x="640" y="198" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">GUARD GATE</text>
      <text x="640" y="216" text-anchor="middle" fill="#9aa3b5" font-size="11">verified guard only</text>
      <text x="640" y="234" text-anchor="middle" fill="#9aa3b5" font-size="11">else force logout</text>

      <rect x="820" y="170" width="260" height="88" rx="8" fill="#10182b" stroke="#c22712"/>
      <text x="950" y="198" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">KYC INTAKE</text>
      <text x="950" y="216" text-anchor="middle" fill="#9aa3b5" font-size="11">licence front + back</text>
      <text x="950" y="234" text-anchor="middle" fill="#9aa3b5" font-size="11">NSW classes · mobile · email</text>

      <line x1="180" y1="202" x2="260" y2="202" stroke="#c22712" stroke-width="2" marker-end="url(#arrow)"/>
      <line x1="460" y1="214" x2="540" y2="214" stroke="#c22712" stroke-width="2" marker-end="url(#arrow)"/>
      <line x1="740" y1="214" x2="820" y2="214" stroke="#c22712" stroke-width="2" marker-end="url(#arrow)"/>

      <rect x="20" y="320" width="240" height="88" rx="8" fill="#10182b" stroke="#c22712"/>
      <text x="140" y="348" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">KYC STORE</text>
      <text x="140" y="366" text-anchor="middle" fill="#9aa3b5" font-size="11">encrypted images + classes</text>
      <text x="140" y="384" text-anchor="middle" fill="#9aa3b5" font-size="11">approval state</text>

      <rect x="300" y="320" width="240" height="88" rx="8" fill="#10182b" stroke="#c22712"/>
      <text x="420" y="348" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">BANK VAULT</text>
      <text x="420" y="366" text-anchor="middle" fill="#9aa3b5" font-size="11">BSB + account (encrypted)</text>
      <text x="420" y="384" text-anchor="middle" fill="#9aa3b5" font-size="11">payroll use only</text>

      <rect x="580" y="320" width="240" height="88" rx="8" fill="#10182b" stroke="#c22712"/>
      <text x="700" y="348" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">SUPER API</text>
      <text x="700" y="366" text-anchor="middle" fill="#9aa3b5" font-size="11">fund / SuperStream</text>
      <text x="700" y="384" text-anchor="middle" fill="#9aa3b5" font-size="11">or USI if own fund</text>

      <rect x="860" y="320" width="220" height="88" rx="8" fill="#10182b" stroke="#c22712"/>
      <text x="970" y="348" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">GUARD ADMIN</text>
      <text x="970" y="366" text-anchor="middle" fill="#9aa3b5" font-size="11">week-by-week availability</text>
      <text x="970" y="384" text-anchor="middle" fill="#9aa3b5" font-size="11">profile / short bio</text>

      <line x1="950" y1="258" x2="140" y2="320" stroke="#c22712" stroke-width="1.5" marker-end="url(#arrow)"/>
      <line x1="950" y1="258" x2="420" y2="320" stroke="#c22712" stroke-width="1.5" marker-end="url(#arrow)"/>
      <line x1="950" y1="258" x2="700" y2="320" stroke="#c22712" stroke-width="1.5" marker-end="url(#arrow)"/>
      <line x1="740" y1="258" x2="970" y2="320" stroke="#c22712" stroke-width="1.5" marker-end="url(#arrow)"/>

      <line x1="970" y1="408" x2="950" y2="112" stroke="#c22712" stroke-width="1.5" marker-end="url(#arrow)"/>
      <line x1="360" y1="112" x2="360" y2="160" stroke="#9aa3b5" stroke-width="1.5" stroke-dasharray="4 3"/>
      <line x1="420" y1="408" x2="360" y2="408" stroke="#9aa3b5" stroke-width="1.5"/>
      <line x1="360" y1="408" x2="360" y2="258" stroke="#9aa3b5" stroke-width="1.5" marker-end="url(#arrow2)"/>

      <text x="20" y="460" fill="#9aa3b5" font-size="13" font-family="Barlow, sans-serif">TIER 2 — AFTER 10 VERIFIED GUARDS (not built in the first release)</text>

      <rect x="20" y="480" width="320" height="80" rx="8" fill="#070b14" stroke="#9aa3b5" stroke-dasharray="6 4"/>
      <text x="180" y="510" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">HOMEPAGE SEARCH</text>
      <text x="180" y="530" text-anchor="middle" fill="#9aa3b5" font-size="11">location · time · experience</text>
      <text x="180" y="546" text-anchor="middle" fill="#9aa3b5" font-size="11">clients filter available guards</text>

      <rect x="390" y="480" width="320" height="80" rx="8" fill="#070b14" stroke="#9aa3b5" stroke-dasharray="6 4"/>
      <text x="550" y="510" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">PUBLIC ROSTER</text>
      <text x="550" y="530" text-anchor="middle" fill="#9aa3b5" font-size="11">verified guards only</text>
      <text x="550" y="546" text-anchor="middle" fill="#9aa3b5" font-size="11">bio · licences · availability</text>

      <rect x="760" y="480" width="320" height="80" rx="8" fill="#070b14" stroke="#9aa3b5" stroke-dasharray="6 4"/>
      <text x="920" y="510" text-anchor="middle" fill="#f3eee6" font-size="14" font-family="Barlow Condensed, sans-serif">CLIENT BOOKING</text>
      <text x="920" y="530" text-anchor="middle" fill="#9aa3b5" font-size="11">request → super admin</text>
      <text x="920" y="546" text-anchor="middle" fill="#9aa3b5" font-size="11">then same Tier 1 delegation</text>

      <line x1="180" y1="560" x2="180" y2="620" stroke="#9aa3b5" stroke-width="1.5" stroke-dasharray="6 4"/>
      <line x1="180" y1="620" x2="550" y2="620" stroke="#9aa3b5" stroke-width="1.5" stroke-dasharray="6 4"/>
      <line x1="550" y1="560" x2="550" y2="620" stroke="#9aa3b5" stroke-width="1.5" stroke-dasharray="6 4"/>
      <line x1="920" y1="560" x2="920" y2="620" stroke="#9aa3b5" stroke-width="1.5" stroke-dasharray="6 4"/>
      <line x1="550" y1="620" x2="920" y2="620" stroke="#9aa3b5" stroke-width="1.5" stroke-dasharray="6 4"/>
      <line x1="640" y1="620" x2="640" y2="112" stroke="#9aa3b5" stroke-width="1.5" stroke-dasharray="6 4" marker-end="url(#arrow2)"/>

      <text x="20" y="670" fill="#9aa3b5" font-size="13" font-family="Barlow, sans-serif">NSW LICENCE CLASSES CAPTURED AT KYC</text>
      <text x="20" y="694" fill="#f3eee6" font-size="13" font-family="Barlow, sans-serif">1A Unarmed · 1B Bodyguard · 1C Crowd controller · 1D Dog handler · 1E Cash-in-transit · 1F Armed</text>
      <text x="20" y="716" fill="#f3eee6" font-size="13" font-family="Barlow, sans-serif">2A Consultant · 2B Seller · 2C Equipment specialist · 2D Locksmith · plus any current Class 2 subclass on the card</text>

      <text x="20" y="756" fill="#9aa3b5" font-size="13" font-family="Barlow, sans-serif">HARD RULES</text>
      <text x="20" y="780" fill="#f3eee6" font-size="13" font-family="Barlow, sans-serif">1. Non-guards are signed out immediately after auth. No KYC form, no admin panel.</text>
      <text x="20" y="802" fill="#f3eee6" font-size="13" font-family="Barlow, sans-serif">2. Bank BSB/account and licence images never appear in sitemaps, search, or the public roster.</text>
      <text x="20" y="824" fill="#f3eee6" font-size="13" font-family="Barlow, sans-serif">3. Super: call a SuperStream / fund-lookup API; if the guard has their own fund they enter the USI instead.</text>
      <text x="20" y="846" fill="#f3eee6" font-size="13" font-family="Barlow, sans-serif">4. Super admin sees only successfully registered (KYC-approved) guards, with search, then assigns jobs.</text>
      <text x="20" y="868" fill="#f3eee6" font-size="13" font-family="Barlow, sans-serif">5. Homepage search and public roster stay off until the verified-guard count is greater than 10.</text>
    </svg>
    <figcaption>Data moves left to right for a new guard, and right to left when a client job is delegated. Dashed lines are Tier 2.</figcaption>
  </figure>

  <article class="container prose reveal">
    <h2>Tier 1 — what we build first</h2>
    <ul>
      <li>Dedicated jobs page for available security positions.</li>
      <li>Firebase Authentication: Google, email, and phone.</li>
      <li>Guard-only gate. Anyone else is logged out.</li>
      <li>KYC: licence front and back, NSW classes held, mobile, email, BSB and account number.</li>
      <li>Superannuation via API, or USI if they have their own fund.</li>
      <li>Guard admin: week-by-week availability and notifications.</li>
      <li>Super admin: search all approved guards and delegate client jobs.</li>
    </ul>
    <h2>Tier 2 — after 10 verified guards</h2>
    <ul>
      <li>Public roster with a short self-written bio.</li>
      <li>Homepage search: location, time frame, experience, other filters.</li>
    </ul>
    <p>Guards who want on the first roster should call <a href="tel:{gp.TEL}">{gp.PHONE}</a> or email <a href="mailto:{gp.EMAIL}">{gp.EMAIL}</a>. Clients still use the quote brief until the public search ships.</p>
    {gp.share_bar(url, title)}
  </article>
  {gp.quote_form()}
</main>
{footer}
</body>
</html>'''
    out = gp.ROOT / "jobs" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")


def extra_urls() -> list[tuple[str, str, str]]:
    """(sitemap_name, url, priority)"""
    items = [
        ("core-blog-index", f"{gp.SITE}/blog/", "0.85"),
        ("core-industries-index", f"{gp.SITE}/industries/", "0.85"),
        ("core-jobs", f"{gp.SITE}/jobs/", "0.8"),
    ]
    for post in BLOGS:
        items.append((f"blog-{post['slug']}", f"{gp.SITE}/blog/{post['slug']}.html", "0.7"))
    for ind in INDUSTRIES:
        items.append((f"industry-{ind['slug']}", f"{gp.SITE}/industries/{ind['slug']}.html", "0.75"))
    return items


def write_all() -> None:
    write_blog_index()
    for post in BLOGS:
        write_blog_post(post)
    write_industries_index()
    for ind in INDUSTRIES:
        write_industry(ind)
    write_jobs_dfd()
    print(f"Wrote {len(BLOGS)} blog posts, {len(INDUSTRIES)} industry pages and the jobs data-flow page.")


if __name__ == "__main__":
    write_all()
