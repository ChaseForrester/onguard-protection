#!/usr/bin/env python3
"""Build the OnGuard Protection Legal, Liability and Compliance Pack (A4 PDF)."""

from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    CondPageBreak,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    Image,
    HRFlowable,
    Flowable,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent / "OnGuard-Protection-Legal-Compliance-Pack.pdf"
LOCKUP = ROOT / "assets/brand/onguard-lockup.png"
MARK = ROOT / "assets/brand/onguard-mark.png"
NAVY = colors.HexColor("#122556")
RED = colors.HexColor("#c22712")
CREAM = colors.HexColor("#f3eee6")
INK = colors.HexColor("#1a1f2e")
MUTED = colors.HexColor("#4b5568")
LINE = colors.HexColor("#d1d5db")
TODAY = "17 August 2026"
DOC_ID = "OG-LEG-2026-001"
VERSION = "1.0 (corrected & expanded 17 August 2026)"
PREPARED = "Tech Aid Australia — ABN 33 959 110 665 (Stormy Chase Forrester)"


class RuleBar(Flowable):
    def __init__(self, width=None, color=RED, height=3):
        super().__init__()
        self.rule_width = width
        self.color = color
        self.height = height

    def wrap(self, aw, ah):
        self.rule_width = aw
        return aw, self.height

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.rule_width, self.height, stroke=0, fill=1)


def styles():
    base = getSampleStyleSheet()
    s = {
        "cover_kicker": ParagraphStyle("ck", parent=base["Normal"], fontName="Times-Bold", fontSize=9, textColor=RED, tracking=1.2, alignment=TA_CENTER, spaceAfter=8),
        "cover_title": ParagraphStyle("ct", parent=base["Title"], fontName="Times-Bold", fontSize=26, leading=30, textColor=NAVY, alignment=TA_CENTER, spaceAfter=8),
        "cover_sub": ParagraphStyle("cs", parent=base["Normal"], fontName="Times-Roman", fontSize=12, leading=16, textColor=INK, alignment=TA_CENTER, spaceAfter=6),
        "h1": ParagraphStyle("h1", parent=base["Heading1"], fontName="Times-Bold", fontSize=16, leading=20, textColor=NAVY, spaceBefore=14, spaceAfter=8),
        "h2": ParagraphStyle("h2", parent=base["Heading2"], fontName="Times-Bold", fontSize=13, leading=16, textColor=RED, spaceBefore=11, spaceAfter=6),
        "h3": ParagraphStyle("h3", parent=base["Heading3"], fontName="Times-Bold", fontSize=11, leading=14, textColor=NAVY, spaceBefore=8, spaceAfter=4),
        "body": ParagraphStyle("bd", parent=base["Normal"], fontName="Times-Roman", fontSize=9.5, leading=13, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6),
        "small": ParagraphStyle("sm", parent=base["Normal"], fontName="Times-Roman", fontSize=8, leading=11, textColor=MUTED, alignment=TA_JUSTIFY, spaceAfter=4),
        "bullet": ParagraphStyle("bu", parent=base["Normal"], fontName="Times-Roman", fontSize=9.5, leading=12.5, textColor=INK, leftIndent=12, spaceAfter=2),
        "cell": ParagraphStyle("cell", parent=base["Normal"], fontName="Times-Roman", fontSize=8, leading=10.5, textColor=INK),
        "cellb": ParagraphStyle("cellb", parent=base["Normal"], fontName="Times-Bold", fontSize=8, leading=10.5, textColor=NAVY),
        "toc": ParagraphStyle("toc", parent=base["Normal"], fontName="Times-Roman", fontSize=10, leading=15, textColor=INK),
        "footer": ParagraphStyle("ft", parent=base["Normal"], fontName="Times-Roman", fontSize=7.5, textColor=MUTED),
        "notice": ParagraphStyle("nt", parent=base["Normal"], fontName="Times-Bold", fontSize=9, leading=12, textColor=NAVY, alignment=TA_LEFT, spaceAfter=4),
        "center": ParagraphStyle("cen", parent=base["Normal"], fontName="Times-Roman", fontSize=9, leading=12, alignment=TA_CENTER, textColor=INK),
        "link": ParagraphStyle("lk", parent=base["Normal"], fontName="Times-Roman", fontSize=8.5, leading=11.5, textColor=NAVY, spaceAfter=2),
    }
    return s


S = styles()


def P(text, style="body"):
    return Paragraph(text, S[style])


def bullets(items):
    return [P(f"• {item}", "bullet") for item in items]


def table(headers, rows, widths):
    head = [P(h, "cellb") for h in headers]
    data = [head] + [[P(c, "cell") for c in row] for row in rows]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8edf6")),
        ("TEXTCOLOR", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.3, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8f9fb")]),
    ]))
    return t


def header_footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(NAVY)
    canvas.rect(0, h - 16 * mm, w, 16 * mm, stroke=0, fill=1)
    canvas.setFillColor(RED)
    canvas.rect(0, h - 17.4 * mm, w, 1.4 * mm, stroke=0, fill=1)
    if MARK.exists():
        canvas.drawImage(str(MARK), 14 * mm, h - 14.5 * mm, width=9 * mm, height=9 * mm, mask="auto", preserveAspectRatio=True)
    canvas.setFillColor(colors.white)
    canvas.setFont("Times-Bold", 8)
    canvas.drawString(26 * mm, h - 10.5 * mm, "ONGUARD PROTECTION")
    canvas.setFont("Times-Roman", 7)
    canvas.drawRightString(w - 14 * mm, h - 10.5 * mm, "Legal, Liability & Compliance Pack  |  " + DOC_ID)
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, w, 12 * mm, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont("Times-Roman", 7.5)
    canvas.drawString(14 * mm, 5 * mm, "CONFIDENTIAL — Issued for clients, councils, agencies and tender evaluation panels")
    canvas.drawRightString(w - 14 * mm, 5 * mm, f"Page {doc.page}")
    canvas.restoreState()


def cover_page():
    story = [Spacer(1, 18 * mm)]
    if LOCKUP.exists():
        story.append(Image(str(LOCKUP), width=92 * mm, height=38 * mm, hAlign="CENTER"))
    story += [
        Spacer(1, 8 * mm),
        RuleBar(),
        Spacer(1, 8 * mm),
        P("DOCUMENT CONTROLLED", "cover_kicker"),
        P("Legal, Liability, Refunds<br/>and Compliance Pack", "cover_title"),
        P("Limitation of liability • Australian Consumer Law • ACCC • New South Wales only<br/>Current SLED Class 1 / Class 2 roster rules • ISO alignment • Defence / NV clearances", "cover_sub"),
        Spacer(1, 6 * mm),
        RuleBar(color=NAVY, height=1),
        Spacer(1, 8 * mm),
    ]
    meta = [
        ["Document ID", DOC_ID],
        ["Version", VERSION],
        ["Effective", TODAY],
        ["Issuer", "OnGuard Protection (NSW Master Licence 000110094)"],
        ["Prepared by", PREPARED],
        ["Scope", "New South Wales only. No interstate master-licence claim."],
        ["Classification", "Public-facing contractual instrument + NSW tender annexure"],
        ["Governing law", "Laws of New South Wales and the Commonwealth of Australia"],
        ["Contact", "0432 893 343  •  admin@ogprotection.com.au"],
        ["Website", "https://www.ogprotection.com.au/legal/"],
    ]
    cells = [[P(a, "cellb"), P(b, "cell")] for a, b in meta]
    t = Table(cells, colWidths=[48 * mm, 122 * mm])
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.3, LINE),
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#e8edf6")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t)
    story += [
        Spacer(1, 10 * mm),
        P("<b>Mandatory opening statement.</b> Nothing in this Pack excludes, restricts or modifies any right or remedy a person has under the Australian Consumer Law (Schedule 2 to the <i>Competition and Consumer Act 2010</i> (Cth)) that cannot lawfully be excluded. “No refunds”, “all care no responsibility”, and similar statements are unlawful if they misrepresent those rights. OnGuard Protection will not use them.", "notice"),
        Spacer(1, 6 * mm),
        P("This Pack is issued for commercial, government, council and Defence-adjacent evaluation. It is not a substitute for independent legal advice on a specific contract. Where a written engagement, purchase order or deed is signed, that instrument prevails to the extent of any inconsistency, except that the Australian Consumer Law always prevails.", "small"),
    ]
    return story


def toc():
    items = [
        "1.  Status of this document and how to use it",
        "2.  Parties, definitions and interpretation",
        "3.  Scope of services",
        "4.  Australian Consumer Law, ACCC and refunds",
        "5.  Limitation of liability (where the law allows)",
        "6.  Unfair contract terms and standard-form contracts",
        "7.  Licensing — New South Wales only (SLED)",
        "8.  WHS, dual-PCBU, first-aid currency, privacy and surveillance",
        "9.  ISO, Australian Standards and quality alignment",
        "10. Defence, NV1 / NV2, PSPF, DISP and classified work",
        "11. Commonwealth and NSW government tenders",
        "12. Insurance, indemnities and claims procedure",
        "13. Personnel, subcontractors and modern slavery",
        "14. Confidentiality, intellectual property and records",
        "15. Fees, variations, cancellation and force majeure",
        "16. Complaints, disputes and regulators",
        "17. Governing law, severance and entire agreement",
        "18. Official references and external links",
        "Schedule A  —  NSW licence architecture and individual recognition",
        "Schedule B  —  ACL remedies decision map",
        "Schedule C  —  NSW tender and Defence pathway",
        "Schedule D  —  NSW Class 1 and Class 2 roster rules (current)",
        "Schedule E  —  NSW local government tender threshold",
        "Schedule F  —  Tender attachment checklist",
        "Schedule G  —  Acceptance block",
    ]
    story = [P("Contents", "h1"), RuleBar(color=NAVY, height=1), Spacer(1, 4 * mm)]
    story += [P(i, "toc") for i in items]
    return story


def body():
    w = [32 * mm, 50 * mm, 44 * mm, 44 * mm]
    story = []

    story += [
        P("1. Status of this document and how to use it", "h1"),
        P("This Legal, Liability, Refunds and Compliance Pack (“Pack”) is the public legal framework of OnGuard Protection (“OnGuard”, “we”, “us”). It applies to website enquiries, quotations, standing offers, purchase orders, event bookings, patrol contracts, static-guard deployments, and any invitation to tender, request for quote or panel application issued by a Commonwealth entity, a New South Wales agency, a NSW local council, a government-owned corporation, or a Defence prime <b>for work in New South Wales</b>.", "body"),
        P("The Pack has three jobs: (1) tell clients, in plain English, what the law already requires of us; (2) limit liability only to the extent Australian law permits; and (3) give evaluation panels a single annexure they can file against NSW licensing, WHS, first-aid currency, privacy, ISO alignment, and Defence-adjacent security questions.", "body"),
        P("OnGuard holds New South Wales Security Master Licence <b>000110094</b>, issued under the <i>Security Industry Act 1997</i> (NSW) and administered by the Security Licensing &amp; Enforcement Directorate (SLED). <b>This Pack does not claim an interstate master, firm or agent licence.</b> Mutual recognition may allow an individual operative to work in another jurisdiction where that scheme lawfully applies. It does not authorise OnGuard to carry on a security business outside NSW. Work outside NSW is declined unless a current local master/firm licence is in force and scheduled to the quote.", "body"),
        P("2. Parties, definitions and interpretation", "h1"),
        P("<b>Client</b> means the person or entity that requests or receives services. <b>Consumer</b> has the meaning in s 3 of the Australian Consumer Law and includes a person who acquires services of a kind ordinarily acquired for personal, domestic or household use or consumption, or who acquires services for an amount not exceeding the prescribed threshold (currently $100,000). <b>Services</b> means crowd control, event security, static guarding, mobile patrols, alarm response, corporate concierge, access control and asset protection, and any related labour or advice. <b>Site</b> means the premises, venue, compound or event specified in the booking. <b>Regulator</b> includes the ACCC, SLED, a State or Territory licensing authority, SafeWork / WorkSafe, the OAIC, and a Defence security authority.", "body"),
        P("Headings are for convenience only. A reference to legislation includes amendments and instruments made under it. If a provision is void, the rest of this Pack continues. Nothing in this Pack is a warranty that a particular ISO certificate, DISP membership or security clearance is currently held — those are stated, if at all, only on a signed schedule.", "body"),
        P("3. Scope of services", "h1"),
        P("OnGuard supplies licensed security labour and site presence in New South Wales. We do not, unless a separate written instrument and the matching licence class are scheduled, supply locksmithing, firearms, cash-in-transit, private inquiry, monitoring-centre operations, or covert electronic surveillance. The Client remains responsible for site induction content that only the occupier can provide, for facilities that only the Client controls, and for directions that would require OnGuard to break the law.", "body"),
        P("A quotation is an invitation to treat unless it is stated to be a standing offer. A contract is formed when OnGuard confirms the booking in writing (including email or a signed purchase order) or first deploys personnel to the Site after a clear instruction to proceed.", "body"),
    ]

    story += [
        P("4. Australian Consumer Law, ACCC and refunds", "h1"),
        P("The Australian Consumer Law (“ACL”) is Schedule 2 to the <i>Competition and Consumer Act 2010</i> (Cth). It is applied as a law of each State and Territory. The Australian Competition and Consumer Commission (ACCC) and State and Territory consumer agencies enforce it. OnGuard treats ACL compliance as a non-negotiable operating rule, including on tenders and business-to-business work that still meets the definition of a consumer supply.", "body"),
        P("4.1 Consumer guarantees that cannot be excluded", "h2"),
        P("For services, the ACL implies (among others) that: services will be rendered with due care and skill (s 60); services and any product resulting from them will be reasonably fit for a purpose the Client makes known (s 61); and, if no time is fixed, services will be supplied within a reasonable time (s 62). These guarantees are automatic. They cannot be removed by a website term, a quote footer, a “no refunds” line, or a verbal briefing (s 64).", "body"),
        P("It is misleading (s 18 and related provisions) to tell a client they have no refund rights, or that OnGuard accepts “no liability for any loss”, if that statement would hide a guarantee the law will not let us hide. OnGuard will not publish or say that.", "body"),
        P("4.2 Remedies — major and minor failure", "h2"),
        P("If a guarantee is not met, the remedy depends on whether the failure is major. A major failure in relation to services includes a failure that cannot be remedied within a reasonable time, or that makes the services substantially unfit for their normal purpose or a purpose made known to us. For a major failure the Client may terminate and recover a refund of unused fees, or recover compensation for the reduction in value. For a failure that is not major, OnGuard may remedy by re-supplying the services or paying the reasonable cost of re-supply. See ACL ss 267–269.", "body"),
        P("Change of mind, a Client-caused lock-out, a Client instruction that made the job impossible, or a weather or force-majeure event that is not our failure, is not by itself a failure of a consumer guarantee. In those cases a commercial cancellation fee may apply as set out in section 15, provided it is a genuine pre-estimate and is not an unfair term.", "body"),
        P("4.3 How to claim a refund or remedy", "h2"),
    ]
    story += bullets([
        "Write to admin@ogprotection.com.au or call 0432 893 343 and identify the booking, Site, date and the problem.",
        "We will acknowledge within two business days and investigate, including radio logs, run-sheets and the officer’s report.",
        "If the ACL requires a remedy, we will offer re-supply, a partial refund, or a full refund of unused fees, as the Act requires — not as a gesture.",
        "If we do not agree a guarantee failed, we will say why in writing and name the Client’s right to go to a State tribunal, a court, or a consumer agency.",
        "External help: ACCC (accc.gov.au / 1300 302 502) and the consumer agency in the Client’s State or Territory.",
    ])
    story += [
        P("4.4 Business clients and s 64A", "h2"),
        P("Where the services are <i>not</i> of a kind ordinarily acquired for personal, domestic or household use or consumption, and the ACL still applies, s 64A permits a supplier to limit liability for a failure to comply with a guarantee to re-supplying the services or paying the cost of re-supply. OnGuard relies on that statutory permission in section 5. That limit does not apply to a consumer guarantee that the law will not let us limit, and it does not apply to fraud, wilful misconduct, or personal injury to the extent the law forbids a limit.", "body"),
        P("5. Limitation of liability (where the law allows)", "h1"),
        P("Subject always to section 4 and to any non-excludable right:", "body"),
    ]
    story += bullets([
        "OnGuard’s aggregate liability arising out of a booking is limited to the fees paid (or payable) for the affected shift or, if greater, the cost of re-supplying the affected services.",
        "OnGuard is not liable for consequential or indirect loss (lost profit, lost opportunity, reputational loss, or loss of a tender) except to the extent the ACL or another non-excludable law requires it.",
        "OnGuard is not liable for loss caused by the Client’s incomplete brief, a Site hazard we were not told about, a direction to act unlawfully, or the conduct of third parties we do not control (including patrons, contractors and emergency services).",
        "Nothing limits liability for death or personal injury to the extent a statute forbids that limit, or for fraud or wilful misconduct.",
        "Time bar: a claim must be notified in writing within 12 months of the Client becoming aware of the facts, or any longer period a statute requires.",
    ])
    story += [
        P("This clause is a limitation, not an exclusion of the ACL. If a court or tribunal finds a sentence too wide, that sentence is read down (section 17) rather than used to void the Client’s statutory rights.", "body"),
        P("6. Unfair contract terms and standard-form contracts", "h1"),
        P("The ACL unfair contract terms regime applies to standard-form contracts with consumers and with small businesses (including, under current thresholds, businesses with fewer than 100 employees or turnover under $10 million). A term that causes a significant imbalance, is not reasonably necessary to protect a legitimate interest, and would cause detriment if relied on, may be unfair — and proposing, using or relying on an unfair term can attract penalties.", "body"),
        P("OnGuard will not rely on a term that lets us unilaterally vary price or scope without a genuine reason and a fair process; that lets us avoid our ACL obligations; or that imposes a cancellation fee that is a penalty rather than a genuine pre-estimate of loss. If a Client believes a term is unfair, they should write to us. We will review it.", "body"),
    ]

    story += [
        P("7. Licensing — New South Wales only", "h1"),
        P("Security work in NSW is licensed under the <i>Security Industry Act 1997</i> and the Security Industry Regulation. A master licence authorises the business to provide persons to carry on security activities. Each operative must hold the correct Class 1 or Class 2 subclass for the activity actually performed. OnGuard will not deploy an unlicensed person, or a person whose class does not match the activity.", "body"),
        P("OnGuard’s issued business authority is NSW Master Licence <b>000110094</b>. Clients and evaluation panels should verify it on the SLED public register: https://verify.licence.nsw.gov.au/home/Security", "body"),
        P("Since 1 June 2023, former unarmed-guard (old 1A) and crowd-controller (old 1C) activities sit together under the current <b>Class 1A Security Officer</b> subclass. Current 1C is cash-in-transit. Current 1D is the only subclass that authorises dog work. A Class 1A, 1B, 1C, 1E or 1F licence does not authorise security activity with a dog. Schedule D is the roster rule.", "body"),
        P("Mutual recognition under the <i>Mutual Recognition Act 1992</i> (Cth) and automatic mutual recognition may allow an <i>individual</i> licence to travel, subject to notifications and excluded activities. It does not give OnGuard an interstate master licence. This Pack does not table a multi-state business-licence matrix as if those licences were held.", "body"),
        P("8. Work health and safety, dual-PCBU, first-aid currency, privacy and surveillance", "h1"),
        P("8.1 Dual-PCBU WHS (NSW)", "h2"),
        P("The <i>Work Health and Safety Act 2011</i> (NSW) applies. OnGuard and the Client are typically both persons conducting a business or undertaking (PCBUs) at the Site (ss 5, 16). Each must consult, cooperate and coordinate (s 46). OnGuard officers must be inducted to Site-specific hazards the occupier controls. We will stop work that presents a serious and imminent risk. A worker may cease unsafe work under s 84.", "body"),
        P("8.2 NSW roster rules", "h2"),
        P("Every person provided to carry on a security activity holds a current NSW licence of the matching subclass (Schedule D). The original licence is worn so as to be clearly visible (s 36) — attached to outer clothing, at or above the waist, front or side. The roster records name, licence number, subclass, start and finish for every shift. A licence is not lent, hired or used by another person (s 37). Fatigue, award breaks and maximum hours are treated as WHS and Fair Work duties, not roster convenience.", "body"),
        P("8.3 First-aid currency", "h2"),
        P("For crowd control, event, and other 1A posts where first aid is reasonably required by the Site, the event plan or our SOP, the officer’s first-aid unit (typically HLTAID011 or the unit then specified by SLED / the approved Security Licence Course) must be current. An officer whose first-aid has expired will not be rostered onto those posts. Currency is checked before the first shift of a booking and at each scheduled refresh.", "body"),
        P("8.4 Privacy", "h2"),
        P("If OnGuard is an APP entity under the <i>Privacy Act 1988</i> (Cth), or if a government contract applies the Australian Privacy Principles (APPs) by flow-down, we will handle personal information in accordance with the APPs: collect only what the job needs, use it for the purpose disclosed, secure it, and not disclose it except as the APPs or a law requires. Incident reports, CCTV stills we are given, and officer notes are treated as confidential operational records.", "body"),
        P("8.5 Surveillance and listening devices", "h2"),
        P("Covert optical or listening surveillance is restricted under the <i>Surveillance Devices Act 2007</i> (NSW). OnGuard does not conduct covert surveillance unless a written lawful authority exists. Body-worn cameras, if used, will be used only as the engagement and the Act allow, and people will be notified where the law requires notice.", "body"),
    ]

    story += [
        P("9. ISO, Australian Standards and quality alignment", "h1"),
        P("<b>Alignment is not certification.</b> Alignment means we design jobs, SOPs, incident control and records to the control set named below. Certification means a JAS-ANZ accredited body has issued a current numbered certificate. OnGuard does not, in this Pack, claim a current ISO certificate. If a certificate is later issued, it will be scheduled and attached. Claiming a certificate we do not hold is misleading under the ACL. Evaluation panels must treat “alignment” as not certified.", "body"),
        P("Frameworks we map work to, and that evaluation panels commonly specify:", "body"),
    ]
    story.append(table(
        ["Instrument", "Subject", "Typical buyer", "OnGuard position"],
        [
            ["ISO 9001", "Quality management system", "Councils, agencies, primes", "Alignment. Certificate only if scheduled."],
            ["ISO 18788", "Security operations management", "Security and Defence buyers", "Alignment of SOPs, use-of-force and incident control."],
            ["ISO 27001", "Information security management", "Defence, critical infrastructure", "Alignment. Required for many DISP / ICT packages."],
            ["ISO 31000 / AS ISO 31000", "Risk management", "All government", "Used in job hazard analysis and event plans."],
            ["ISO 45001", "Occupational health and safety", "All government", "Alignment with PCBU duties."],
            ["ISO 14001", "Environmental management", "Some infrastructure tenders", "Applied where the Site specification requires it."],
            ["AS 4421", "Guards and patrols", "Australian security buyers", "Operational reference for patrol and static work."],
            ["PSPF + ISM + Essential Eight", "Commonwealth protective security / cyber", "Commonwealth and DISP", "Applied when the contract classifies information or systems."],
        ],
        [32 * mm, 42 * mm, 42 * mm, 54 * mm],
    ))
    story += [
        Spacer(1, 3 * mm),
        P("10. Defence, NV1 / NV2, PSPF, DISP and classified work", "h1"),
        P("Work for the Department of Defence, the Australian Defence Force, a Defence prime, or a classified Commonwealth program on a NSW Site sits under the Protective Security Policy Framework (PSPF), the Defence Security Principles Framework (DSPF), the Defence Industry Security Program (DISP), the Australian Government Information Security Manual (ISM), and the ASD Essential Eight. DISP is security vetting for Australian businesses. Many Defence contracts require DISP membership at a stated maturity level before a supplier may handle classified information or access a Defence Site.", "body"),
        P("<b>NV1, NV2 and higher clearances.</b> Classified or Defence work that requires an AGSVA Negative Vetting 1, Negative Vetting 2, Positive Vetting or any higher clearance will be declined, or delivered only through a cleared partner under a written subcontract, until OnGuard holds the named clearance and it is scheduled. We will not roster an uncleared officer onto a cleared post. We will not tick “held” on a tender form for a clearance we do not hold.", "body"),
        P("OnGuard will not pretend to hold DISP membership, a facility security clearance, or individual security clearances unless those are current and named on a signed schedule. If a tender requires them, we will either (a) already hold them and evidence them, or (b) decline or partner until the membership is in force. Submitting a Defence tender on a false security status is a security incident and a misleading representation.", "body"),
        P("Where OnGuard is a subcontractor to a DISP member, we will comply with the flow-down clauses we sign: personnel sponsorship, need-to-know, no uncleared devices, incident reporting to the prime’s security officer, and return or destruction of classified material. Officers who are not cleared will not be put on a cleared post.", "body"),
        P("Export-controlled technology, ITAR/EAR flow-down, and the <i>Defence Trade Controls Act 2012</i> are out of scope unless a schedule says otherwise. The <i>Security of Critical Infrastructure Act 2018</i> (SOCI) may apply if the Client is a responsible entity for a critical asset — in that case the Client must tell us before we start.", "body"),
        P("11. Commonwealth and NSW government tenders", "h1"),
        P("Commonwealth procurement for a NSW Site is conducted under the Commonwealth Procurement Rules (CPRs) issued under the <i>Public Governance, Performance and Accountability Act 2013</i>. NSW Government procurement sits under buy.nsw / eTendering. Local government in NSW is under the <i>Local Government Act 1993</i> (NSW) and the council’s procurement policy — a public tender is commonly required above $250,000 including GST, subject to amendment. Confirm the current threshold before you treat this as the award rule.", "body"),
        P("OnGuard will respond to RFTs, RFQs, panels and standing offers with this Pack as Annexure A unless the buyer mandates its own deed. We will not bid a price we cannot resource with licensed NSW labour of the correct subclass. We will declare conflicts, prior adverse findings, and any licence condition that would affect performance. Collusive tendering is prohibited.", "body"),
        P("Primary portals for NSW work:", "body"),
    ]
    story += bullets([
        "Commonwealth — AusTender  https://www.tenders.gov.au",
        "NSW — buy.nsw / eTendering  https://buy.nsw.gov.au",
        "NSW councils — Tenderlink, VendorPanel, or the council’s own portal.",
    ])

    story += [
        P("12. Insurance, indemnities and claims procedure", "h1"),
        P("OnGuard maintains, and will produce certificates of currency for, public liability insurance and workers compensation as required by law in the jurisdiction of the Site. Professional indemnity or other classes are held only if stated on the certificate attached to the quote. Clients (especially councils) should not assume a limit or an insurer until they have the current certificate. OnGuard’s indemnity to the Client covers loss to the extent caused by OnGuard’s negligence or wilful default, reduced to the extent the Client or a third party caused or contributed to it. The indemnity is capped as in section 5 except where the law forbids a cap.", "body"),
        P("Notify claims immediately to 0432 893 343 and admin@ogprotection.com.au. Do not admit liability on our behalf. Preserve radio logs, CCTV the Client controls, and medical records the injured person consents to release.", "body"),
        P("13. Personnel, subcontractors and modern slavery", "h1"),
        P("Every operative on a licensed activity holds a current NSW licence of the correct subclass (Schedule D). We may subcontract to another NSW master-licensed provider; we remain responsible to the Client for the subcontracted performance. The <i>Modern Slavery Act 2018</i> (Cth) reporting obligation applies to entities at or above the consolidated revenue threshold. Whether or not OnGuard is a reporting entity in a given year, we will not use bonded, trafficked or child labour, and we will not subcontract to a provider we know does.", "body"),
        P("Fair Work Act minimums, awards and casual conversion rules apply to our labour. Clients must not dictate rates that would force an award breach.", "body"),
        P("14. Confidentiality, intellectual property and records", "h1"),
        P("Each party must keep the other’s confidential information confidential, except for disclosure to insurers, lawyers, regulators, and as a court or statute requires. Run-sheets, event plans and SOPs we create remain OnGuard intellectual property. The Client receives a licence to use them for the Site and the term. We keep operational records for at least seven years, or longer if a government contract says so.", "body"),
        P("15. Fees, variations, cancellation and force majeure", "h1"),
        P("Fees are as quoted. Variations (extra hours, extra officers, a change of Site) must be agreed in writing where practicable; in an unfolding incident the Client’s authorised person may instruct a variation and we will confirm as soon as practicable. Payment terms are 14 days from invoice unless the quote says otherwise. Overdue amounts may attract interest at the Reserve Bank cash rate plus 4% per annum.", "body"),
        P("Cancellation: if the Client cancels more than 72 hours before start, no fee. Inside 72 hours, a fee not exceeding the unavoidable labour and travel we cannot redeploy — a genuine pre-estimate, not a penalty. If we cancel for a reason other than force majeure or a Client breach, the Client pays nothing for the cancelled portion and may claim an ACL remedy if one applies.", "body"),
        P("Force majeure includes flood, fire, pandemic direction, industrial action we do not control, and a government order that makes the deployment unlawful. Duties are suspended while the event continues. The ACL still applies to any failure that is not genuinely caused by the event.", "body"),
        P("16. Complaints, disputes and regulators", "h1"),
        P("Complain first to OnGuard (section 4.3). If unresolved: NCAT; a court of competent jurisdiction; the ACCC or NSW Fair Trading; SLED for licence conduct; SafeWork NSW for WHS; the OAIC for privacy. Nothing in this Pack is an arbitration clause that blocks a statutory complaint.", "body"),
        P("17. Governing law, severance and entire agreement", "h1"),
        P("This Pack is governed by the laws of New South Wales and the Commonwealth of Australia. The parties submit to the non-exclusive jurisdiction of the courts of New South Wales. If a provision is invalid, it is severed or read down. This Pack plus the accepted quote or purchase order is the entire agreement, except for any non-excludable statutory term. A waiver must be in writing. We may update this Pack on the website; the version cited on the quote is the version that applies to that booking.", "body"),
        P("18. Official references and external links", "h1"),
    ]
    story += [
        P("• ACCC consumer guarantees — https://www.accc.gov.au/consumers/buying-products-and-services/consumer-rights-and-guarantees", "link"),
        P("• Competition and Consumer Act 2010 (Cth) — https://www.legislation.gov.au/C2004A00109", "link"),
        P("• NSW SLED licence register — https://verify.licence.nsw.gov.au/home/Security", "link"),
        P("• Security Industry Act 1997 (NSW) — https://legislation.nsw.gov.au/view/html/inforce/current/act-1997-157", "link"),
        P("• Work Health and Safety Act 2011 (NSW) — https://legislation.nsw.gov.au/view/html/inforce/current/act-2011-010", "link"),
        P("• Commonwealth Procurement Rules — https://www.finance.gov.au/government/procurement/commonwealth-procurement-rules", "link"),
        P("• AusTender — https://www.tenders.gov.au", "link"),
        P("• Protective Security Policy Framework — https://www.protectivesecurity.gov.au", "link"),
        P("• Defence Security Principles Framework / DISP — https://www.defence.gov.au/business-industry/industry-governance/defence-security-principles-framework", "link"),
        P("• ASD Information Security Manual — https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism", "link"),
        P("• Essential Eight — https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight", "link"),
        P("• Privacy Act / APPs — https://www.oaic.gov.au/privacy/australian-privacy-principles", "link"),
        P("• SafeWork NSW — https://www.safework.nsw.gov.au", "link"),
        P("• ISO 18788 overview — https://www.iso.org/standard/63380.html", "link"),
        P("• OnGuard legal page — https://www.ogprotection.com.au/legal/", "link"),
    ]
    return story


def schedules():
    story = [
        P("Schedule A — NSW licence architecture and individual recognition", "h1"),
        P("This Pack is NSW-only. The table is the architecture of the Security Industry Act 1997 (NSW), not a claim that OnGuard holds an interstate master licence.", "small"),
        Spacer(1, 2 * mm),
    ]
    story.append(table(
        ["Instrument", "What it authorises", "OnGuard position"],
        [
            ["NSW Master Licence 000110094", "The business may provide licensed persons to carry on security activities in NSW.", "Held. Verify on the SLED register."],
            ["Class 1 individual licence", "The named person may perform the endorsed subclass (1A–1F).", "Rostered only if the subclass matches the activity. See Schedule D."],
            ["Class 2 individual licence", "Consultant / seller / equipment specialist / trainer as endorsed (2A–2D).", "Only if a named holder is scheduled. Not a current product line for 2B/2C."],
            ["Mutual recognition (individuals)", "An individual licence may travel where the Cth/State scheme lawfully applies.", "Noted for operatives only. Does not authorise OnGuard to carry on a security business outside NSW."],
            ["Interstate master / firm / agent licence", "Would authorise the company to carry on a security business in that State.", "Not held. Not claimed. Work outside NSW is declined unless a local licence is scheduled."],
        ],
        [48 * mm, 62 * mm, 60 * mm],
    ))
    story += [
        Spacer(1, 4 * mm),
        P("Mutual recognition under the <i>Mutual Recognition Act 1992</i> (Cth) and automatic mutual recognition may allow an individual licence to be used across borders, subject to notifications and excluded activities. They do not automatically authorise a company to carry on a security business in a second State without that State’s business/master licence if the local Act requires one.", "body"),
        P("Schedule B — ACL remedies decision map", "h1"),
        P("Read top to bottom. This is a plain-English map of ss 60–62 and 267–269. It is not a substitute for legal advice on a hard case.", "small"),
        Spacer(1, 2 * mm),
    ]
    story.append(table(
        ["Step", "Question", "If yes", "If no"],
        [
            ["1", "Were the services supplied in trade or commerce in Australia?", "Go to 2.", "ACL consumer guarantees do not apply. Contract and other statutes still might."],
            ["2", "Is the Client a consumer (household-type services, or price at or under the threshold)?", "Guarantees apply. Go to 3.", "Guarantees may still apply if the services are of a consumer kind. Otherwise see s 64A and the contract."],
            ["3", "Were the services rendered with due care and skill, fit for the stated purpose, and in a reasonable time?", "No ACL failure. Commercial goodwill only.", "Go to 4."],
            ["4", "Is the failure major (cannot be remedied in time, or substantially unfit)?", "Client may terminate and claim a refund / compensation for reduction in value.", "OnGuard may re-supply or pay the reasonable cost of re-supply."],
            ["5", "Did the Client cause the problem (bad brief, lock-out, unlawful direction)?", "Not an ACL failure of our guarantees. Cancellation terms may apply.", "Remedy under 4. Document the investigation."],
        ],
        [16 * mm, 58 * mm, 48 * mm, 48 * mm],
    ))
    story += [
        Spacer(1, 6 * mm),
        P("Schedule C — Tender and Defence pathway", "h1"),
        P("How an evaluation panel should read OnGuard against a typical government or Defence package. Boxes are sequential.", "small"),
        Spacer(1, 2 * mm),
    ]
    story.append(table(
        ["Gate", "What the buyer asks", "What OnGuard tables", "Stop / go"],
        [
            ["G1 Licensing", "Valid NSW master licence and matching individual subclass", "NSW ML 000110094 on SLED register. Schedule D class match on the roster.", "STOP if the Site is outside NSW without a scheduled local master licence."],
            ["G2 ACL / UCT", "Terms that do not void consumer or small-business rights", "This Pack, ss 4–6. No “no refunds”. s 64A limit only where lawful.", "STOP if the buyer’s own deed forces an unlawful exclusion — we will mark it up."],
            ["G3 WHS / insurance", "PCBU duties, workers compensation, public liability", "Certificates of currency + Site JHA. Dual-PCBU consult.", "STOP if the Client will not induct or will not disclose a known serious hazard."],
            ["G4 ISO / quality", "9001 / 18788 / 27001 / 45001 as specified", "Alignment statement in s 9. Certificates only if scheduled. No fake certs.", "GO on alignment. CONDITIONAL if the RFT mandates a numbered certificate we do not yet hold."],
            ["G5 Privacy / records", "APPs, information handling, seven-year records", "s 8.2 and s 14. Flow-down APPs accepted on government paper.", "GO unless the package requires a full IRAP assessment we have not scoped."],
            ["G6 Defence / classified", "DISP, PSPF, DSPF, NV1/NV2, Essential Eight", "s 10. Honest status. NV work declined or partnered until held.", "STOP on classified work without the required DISP / NV schedule."],
            ["G7 Price and labour", "Sustainable licensed labour, no collusion", "Award-compliant rates. Named licence classes on the roster.", "GO if the roster is licensed and the price can be staffed."],
        ],
        [22 * mm, 48 * mm, 58 * mm, 42 * mm],
    ))
    story += [
        Spacer(1, 8 * mm),
        P("Schedule D — NSW Class 1 and Class 2 roster rules (current post-2023)", "h1"),
        P("Authorities are taken from ss 11–12 of the Security Industry Act 1997 (NSW) as in force after the 1 June 2023 reforms. The class on the officer must match the activity. A Class 1A, 1B, 1C, 1E or 1F licence does not authorise security activity with a dog.", "small"),
        Spacer(1, 2 * mm),
    ]
    story.append(table(
        ["Class", "Authority (Act)", "Typical OnGuard use", "Will not deploy"],
        [
            ["1A Security Officer", "Patrol, protect or guard property while unarmed (static or mobile); and act as a crowd controller or in a similar capacity.", "Core roster: static, patrol, concierge, construction gate, venue door, floor, festival barrier, bag search, event close-out.", "Armed work. Cash-in-transit. Dog teams. A 1A on a 1C/1D/1F post."],
            ["1B Bodyguard", "Act as a bodyguard or in a similar capacity.", "Close personal protection only if the quote names a 1B holder and the principal.", "Unscoped VIP work. A 1A standing in as a bodyguard."],
            ["1C Cash-in-Transit Guard", "Patrol, protect or guard cash-in-transit. Armed CIT also requires 1F plus a firearms authority.", "Not a current OnGuard product line.", "Any CIT run. A 1A used as a cash escort. Claiming old “1C = crowd controller”."],
            ["1D Guard Dog Handler", "Patrol, protect or guard any property with a dog. The only Class 1 subclass that authorises dog work.", "Named dog team on a quote: night static, compound, industrial gate. Handler holds 1D. Dog identified on the run-sheet.", "Improvised animals. A 1A walking a dog. Dog work that is not on the quote."],
            ["1E Monitoring Centre Operator", "Patrol, protect or guard property while carrying on monitoring-centre operations.", "Not a current OnGuard product line.", "Claiming a 1E monitoring post we do not staff."],
            ["1F Armed Guard", "Patrol, protect or guard approved classes of property while armed, and only under a firearms licence/permit under the Firearms Act 1996 (NSW).", "Not offered unless separately licensed, insured and scheduled.", "Firearms on a 1A roster. An armed 1C CIT run without 1F."],
            ["2A Security Consultant", "Sell security methods or principles; act as a consultant by identifying and analysing security risks.", "Only if a 2A holder is named on the quote.", "Unlicensed security consulting sold as “advice from the guard”."],
            ["2B Security Seller", "Sell, and provide advice in relation to, security equipment. Does not authorise install, maintain or repair.", "Not a current OnGuard product line.", "Selling or specifying equipment under a 1A."],
            ["2C Security Equipment Specialist", "Sell, install, maintain, repair and service security equipment (including electronic and barrier equipment) and act as a locksmith.", "Not a current OnGuard product line.", "Locksmithing, alarm install or CCTV install under a Class 1."],
            ["2D Security Trainer", "Provide training, assessment or instruction in relation to any security activity. Does not extend to firearms training.", "Only if a 2D holder (and, where required, an RTO) is named.", "Unlicensed “in-house training” sold as a licensed course. Firearms instruction."],
        ],
        [32 * mm, 48 * mm, 46 * mm, 44 * mm],
    ))
    story += [
        Spacer(1, 3 * mm),
        P("Master licence 000110094 authorises the business to provide licensed persons. It is not a substitute for the individual subclass. Loss-prevention activities formerly under old 1G sit inside current 1A.", "body"),
        P("Schedule E — NSW local government tender threshold", "h1"),
        P("Thresholds move. Confirm the Local Government Act 1993 (NSW), the regulation and the council’s current procurement policy before you treat this as the award rule.", "small"),
        Spacer(1, 2 * mm),
    ]
    story.append(table(
        ["Buyer", "Typical public-tender trigger", "Where to confirm"],
        [
            ["NSW councils", "Often $250,000 including GST (LG Act / regulation — confirm the current figure)", "Office of Local Government + the council procurement policy"],
            ["NSW Government", "buy.nsw / eTendering rules for the relevant scheme", "buy.nsw.gov.au"],
            ["Commonwealth (NSW Site)", "CPR open-tender threshold unless an exemption applies", "finance.gov.au · tenders.gov.au"],
        ],
        [40 * mm, 74 * mm, 56 * mm],
    ))
    story += [
        Spacer(1, 6 * mm),
        P("Schedule F — How to attach this Pack to a tender", "h1"),
    ]
    story += bullets([
        "File this PDF as Annexure A — Legal, Liability and Compliance (NSW).",
        "Attach the current SLED extract for Master Licence 000110094.",
        "Attach certificates of currency (public liability and workers compensation as a minimum).",
        "Attach the named roster for the first four weeks: officer, licence number, subclass, expiry, and first-aid expiry where the post requires it.",
        "If the RFT demands a numbered ISO certificate, DISP membership, NV1, NV2 or a higher clearance — attach the current instrument or mark the requirement as not held / condition subsequent. Do not tick “held” if it is not held.",
        "If a dog team is proposed — attach the 1D licence, animal identification, and the Site’s animal policy.",
        "If the Site is outside NSW — attach the local master/firm licence or do not bid.",
    ])
    story += [
        Spacer(1, 6 * mm),
        P("Schedule G — Acceptance block (optional)", "h1"),
        P("For use when a Client wants to adopt this Pack without a long-form deed. Signing does not waive ACL rights.", "small"),
        Spacer(1, 3 * mm),
    ]
    story.append(table(
        ["Field", "Client", "OnGuard Protection"],
        [
            ["Legal name", " ", "OnGuard Protection"],
            ["ABN / ACN (if any)", " ", "As stated on the quote / invoice"],
            ["Authorised signatory", " ", " "],
            ["Position", " ", " "],
            ["Date", " ", " "],
            ["Document adopted", "OG-LEG-2026-001 v1.0", "OG-LEG-2026-001 v1.0"],
            ["Site / contract reference", " ", " "],
        ],
        [48 * mm, 61 * mm, 61 * mm],
    ))
    story += [
        Spacer(1, 8 * mm),
        P("End of Pack", "h2"),
        P("Issued by OnGuard Protection on " + TODAY + ". Document " + DOC_ID + ", " + VERSION + ". Prepared by " + PREPARED + ". Verify the NSW master licence at https://verify.licence.nsw.gov.au/home/Security. Download this file from https://www.ogprotection.com.au/legal/OnGuard-Protection-Legal-Compliance-Pack.pdf.", "body"),
        P("© 2026 OnGuard Protection. All rights reserved. Official logos of the ACCC, ISO, the Commonwealth and State arms are not reproduced in this Pack; those marks are used by their owners. References are by citation and hyperlink only.", "small"),
    ]
    return story


def build():
    OUT.parent.mkdir(exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=22 * mm,
        bottomMargin=16 * mm,
        title="OnGuard Protection — Legal, Liability and Compliance Pack",
        author="OnGuard Protection",
        subject="NSW-only ACL, SLED Class 1/2 roster rules, ISO alignment, Defence and NSW tenders",
    )
    story = []
    story += cover_page()
    story.append(PageBreak())
    story += toc()
    story.append(PageBreak())
    story += body()
    story.append(PageBreak())
    story += schedules()
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print("Wrote", OUT, "bytes", OUT.stat().st_size)


if __name__ == "__main__":
    build()
