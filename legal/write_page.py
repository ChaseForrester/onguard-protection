#!/usr/bin/env python3
"""Write legal/index.html using shared site chrome. NSW-only pack."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generate_pages as gp

OUT = Path(__file__).resolve().parent / "index.html"
PDF = "OnGuard-Protection-Legal-Compliance-Pack.pdf"
DOC_ID = "OG-LEG-2026-001"
VERSION = "1.0"
EFFECTIVE = "17 August 2026"


def block(title, body):
    return f"""<details class="legal-drop">
  <summary>{title}</summary>
  <div class="legal-drop-body">{body}</div>
</details>"""


def page():
    url = f"{gp.SITE}/legal/"
    title = "Legal, Liability, Refunds & Compliance Pack (NSW) | OnGuard Protection"
    desc = "NSW-only legal pack: ACL refunds, limitation of liability, SLED Class 1A–1F and Class 2 roster rules, ISO alignment, Defence/NV clearances. Master Licence 000110094."
    crumbs = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{gp.SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Legal", "item": url},
        ],
    }
    extra = '<link rel="preload" as="image" href="../assets/brand/onguard-nav-560.webp" type="image/webp">'
    nav, footer = gp.chrome(1, "legal")
    head = gp.head(
        title, desc, url, 1,
        "assets/brand/onguard-lockup.png", 1360, 560,
        "OnGuard Protection logo",
        [gp.org_schema(), crumbs], extra,
    )

    html = f"""{head}
<body class="inner-page legal-page">
{nav}
<main id="main">
  <nav class="crumbs container" aria-label="Breadcrumb">
    <a href="../index.html">Home</a>
    <span aria-hidden="true">/</span>
    <span>Legal &amp; compliance</span>
  </nav>

  <header class="legal-hero container">
    <p class="legal-scope">NSW only · Security Industry Act 1997</p>
    <p class="eyebrow">Document {DOC_ID} · Version {VERSION} (corrected &amp; expanded {EFFECTIVE})</p>
    <h1>Legal, liability, refunds and compliance pack</h1>
    <p class="lead">Limitation of liability written to survive the Australian Consumer Law. ACCC. New South Wales SLED licensing — current Class 1 subclasses as at the <em>Security Industry Act 1997</em>. ISO alignment (no fabricated certificates). Defence and council tenders. This is the long version an evaluation panel can file.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{PDF}" download>Download the full PDF</a>
      <a class="btn btn-ghost" href="https://verify.licence.nsw.gov.au/home/Security" target="_blank" rel="noopener noreferrer">Verify NSW licence 000110094</a>
    </div>
    <table class="legal-control">
      <tbody>
        <tr><th>Document ID</th><td>{DOC_ID}</td></tr>
        <tr><th>Version</th><td>{VERSION} (corrected &amp; expanded {EFFECTIVE})</td></tr>
        <tr><th>Issuer</th><td>OnGuard Protection — NSW Master Licence 000110094</td></tr>
        <tr><th>Prepared by</th><td>Tech Aid Australia — ABN 33 959 110 665 (Stormy Chase Forrester)</td></tr>
        <tr><th>Contact</th><td><a href="tel:+61432893343">0432 893 343</a> · <a href="mailto:admin@ogprotection.com.au">admin@ogprotection.com.au</a></td></tr>
        <tr><th>Website</th><td><a href="https://www.ogprotection.com.au/legal/">https://www.ogprotection.com.au/legal/</a></td></tr>
        <tr><th>Scope</th><td>New South Wales only. No interstate master-licence claim. Mutual recognition is noted only for individual operatives where lawful.</td></tr>
      </tbody>
    </table>
    <p class="legal-notice"><strong>Mandatory opening statement.</strong> Nothing on this page excludes, restricts or modifies a right or remedy that cannot lawfully be excluded under the Australian Consumer Law (Schedule 2 to the <em>Competition and Consumer Act 2010</em> (Cth)). “No refunds” and “all care no responsibility” are unlawful if they hide those rights. We will not use them.</p>
  </header>

  <div class="container legal-diagrams">
    <figure class="legal-fig">
      <figcaption>ACL remedies map</figcaption>
      <svg viewBox="0 0 640 220" role="img" aria-label="Flowchart of Australian Consumer Law remedies">
        <rect x="8" y="80" width="140" height="56" rx="6" fill="#122556"/>
        <text x="78" y="104" fill="#fff" font-size="11" text-anchor="middle">Service supplied</text>
        <text x="78" y="120" fill="#f3eee6" font-size="10" text-anchor="middle">in trade / commerce</text>
        <path d="M148 108 H188" stroke="#c22712" stroke-width="2"/>
        <rect x="188" y="80" width="140" height="56" rx="6" fill="#122556"/>
        <text x="258" y="104" fill="#fff" font-size="11" text-anchor="middle">Guarantee met?</text>
        <text x="258" y="120" fill="#f3eee6" font-size="10" text-anchor="middle">ss 60–62 ACL</text>
        <path d="M328 108 H368" stroke="#c22712" stroke-width="2"/>
        <rect x="368" y="16" width="128" height="52" rx="6" fill="#0f6b00"/>
        <text x="432" y="46" fill="#fff" font-size="11" text-anchor="middle">No ACL failure</text>
        <path d="M328 108 V42 H368" stroke="#0f6b00" stroke-width="2" fill="none"/>
        <path d="M328 108 V174 H368" stroke="#c22712" stroke-width="2" fill="none"/>
        <rect x="368" y="148" width="128" height="52" rx="6" fill="#c22712"/>
        <text x="432" y="172" fill="#fff" font-size="11" text-anchor="middle">Failure</text>
        <text x="432" y="188" fill="#f3eee6" font-size="10" text-anchor="middle">major or minor?</text>
        <rect x="516" y="80" width="116" height="56" rx="6" fill="#122556"/>
        <text x="574" y="104" fill="#fff" font-size="11" text-anchor="middle">Remedy</text>
        <text x="574" y="120" fill="#f3eee6" font-size="10" text-anchor="middle">ss 267–269</text>
        <path d="M496 174 H574 V136" stroke="#c22712" stroke-width="2" fill="none"/>
      </svg>
    </figure>
    <figure class="legal-fig">
      <figcaption>NSW tender / Defence gates</figcaption>
      <ol class="gate-row">
        <li>NSW ML</li>
        <li>Class match</li>
        <li>ACL / UCT</li>
        <li>WHS + first aid</li>
        <li>ISO alignment</li>
        <li>NV / DISP</li>
        <li>Named roster</li>
      </ol>
      <p>A red stop at any gate means we do not bid, or we mark the deed up. We do not invent ISO certificates, DISP membership or NV clearances.</p>
    </figure>
  </div>

  <article class="container legal-prose">
    {block("1. Status of this document and how to use it", '''
      <p>This Pack is the public legal framework of OnGuard Protection. It applies to website enquiries, quotations, purchase orders, event bookings, patrol and static contracts, and any RFT, RFQ, panel or standing offer issued by a Commonwealth entity, a New South Wales agency, a NSW local council, a GOC, or a Defence prime <strong>for work in New South Wales</strong>.</p>
      <p>OnGuard holds New South Wales Security Master Licence <strong>000110094</strong> under the <em>Security Industry Act 1997</em> (NSW), administered by the Security Licensing &amp; Enforcement Directorate (SLED). <strong>This Pack does not claim an interstate master, firm or agent licence.</strong> Mutual recognition may allow an <em>individual</em> operative to work in another jurisdiction where that scheme lawfully applies. It does not authorise OnGuard to carry on a security business outside NSW. Work outside NSW is declined unless a current local master/firm licence is in force and scheduled to the quote.</p>
      <p>Where a signed engagement, purchase order or deed exists, that instrument prevails to the extent of inconsistency — except that the Australian Consumer Law always prevails.</p>
    ''')}
    {block("2. Parties, definitions and interpretation", '''
      <p><strong>Client</strong> means the person or entity that requests or receives services. <strong>Consumer</strong> has the meaning in s 3 of the ACL (household-type services, or a price at or under the prescribed threshold — currently $100,000). <strong>Services</strong> means crowd control, event security, static guarding, mobile patrols, alarm response, corporate concierge, access control, asset protection and, only if scheduled, a Class 1D dog team. <strong>Regulator</strong> includes the ACCC, SLED, SafeWork NSW, the OAIC, and a Defence security authority.</p>
      <p>If a provision is void, the rest continues. Nothing in this Pack is a warranty that a particular ISO certificate, DISP membership, NV1, NV2 or higher clearance is currently held — those are stated, if at all, only on a signed schedule attached to the booking.</p>
    ''')}
    {block("3. Scope of services", '''
      <p>OnGuard supplies licensed security labour and site presence in New South Wales. We do not, unless a separate written instrument and the matching licence class are scheduled, supply locksmithing, firearms, cash-in-transit, private inquiry, monitoring-centre operations, or covert electronic surveillance. The Client remains responsible for site induction content only the occupier can provide, and for directions that would require us to break the law.</p>
      <p>A quotation is an invitation to treat unless stated to be a standing offer. A contract is formed when we confirm the booking in writing or first deploy after a clear instruction to proceed.</p>
    ''')}
    {block("4. Australian Consumer Law, ACCC and refunds", '''
      <p>The ACL is Schedule 2 to the <em>Competition and Consumer Act 2010</em> (Cth). It applies as a law of New South Wales. The <a href="https://www.accc.gov.au/consumers/buying-products-and-services/consumer-rights-and-guarantees" target="_blank" rel="noopener noreferrer">ACCC</a> and NSW Fair Trading enforce it.</p>
      <h3>Guarantees that cannot be excluded</h3>
      <ul>
        <li>Services rendered with due care and skill (s 60).</li>
        <li>Reasonably fit for a purpose the Client makes known (s 61).</li>
        <li>Supplied within a reasonable time if no time is fixed (s 62).</li>
      </ul>
      <p>These cannot be removed by a website term, a quote footer, a “no refunds” line, or a verbal briefing (s 64). Telling a client they have no refund rights, or that we accept “no liability for any loss”, is misleading if it hides a guarantee the law will not let us hide.</p>
      <h3>Major and minor failure</h3>
      <p>A major failure includes a failure that cannot be remedied in a reasonable time, or that makes the services substantially unfit. The Client may then terminate and recover unused fees or compensation for reduction in value. For a non-major failure we may re-supply or pay the reasonable cost of re-supply (ss 267–269).</p>
      <p>Change of mind, a Client-caused lock-out, or a force-majeure event that is not our failure is not by itself an ACL failure. A commercial cancellation fee may then apply if it is a genuine pre-estimate and is not an unfair term.</p>
      <h3>How to claim</h3>
      <ol>
        <li>Email <a href="mailto:admin@ogprotection.com.au">admin@ogprotection.com.au</a> or call <a href="tel:+61432893343">0432 893 343</a> with the booking, site, date and problem.</li>
        <li>We acknowledge within two business days and investigate run-sheets, radio logs and officer reports.</li>
        <li>If the ACL requires a remedy, we offer re-supply or a refund as the Act requires — not as a gesture.</li>
        <li>If we disagree, we say why in writing and name NCAT, a court, NSW Fair Trading or the ACCC.</li>
      </ol>
      <p>Help: <a href="https://www.accc.gov.au" target="_blank" rel="noopener noreferrer">ACCC</a> 1300 302 502 · <a href="https://www.fairtrading.nsw.gov.au" target="_blank" rel="noopener noreferrer">NSW Fair Trading</a> 13 32 20.</p>
    ''')}
    {block("5. Limitation of liability (only where the law allows)", '''
      <p>Where services are <em>not</em> of a kind ordinarily acquired for personal, domestic or household use, s 64A ACL permits a limit to re-supply or the cost of re-supply. Subject always to section 4:</p>
      <ul>
        <li>Aggregate liability for a booking is limited to the fees for the affected shift or the cost of re-supplying those services.</li>
        <li>No liability for consequential loss (lost profit, lost tender, reputation) except where a non-excludable law requires it.</li>
        <li>No liability for a loss caused by an incomplete brief, an undisclosed site hazard, an unlawful direction, or third parties we do not control.</li>
        <li>Nothing limits death or personal injury where a statute forbids that limit, or fraud or wilful misconduct.</li>
        <li>Notify claims within 12 months of becoming aware of the facts, or any longer statutory period.</li>
      </ul>
      <p>If a sentence is too wide, it is read down. It is never used to void statutory rights.</p>
    ''')}
    {block("6. Unfair contract terms", '''
      <p>The ACL unfair-terms regime applies to standard-form contracts with consumers and small businesses (including, under current thresholds, fewer than 100 employees or turnover under $10 million). Proposing or relying on an unfair term can attract penalties.</p>
      <p>We will not rely on a term that lets us unilaterally vary price without a fair process, that avoids ACL obligations, or that imposes a cancellation fee that is a penalty rather than a genuine pre-estimate.</p>
    ''')}
    {block("7. Licensing — New South Wales only", '''
      <p>Security work in NSW is licensed under the <em>Security Industry Act 1997</em> and the Security Industry Regulation. A <strong>master licence</strong> authorises the business to provide persons to carry on security activities. Each operative must hold the <strong>correct Class 1 or Class 2 subclass</strong> for the activity actually performed. We will not deploy an unlicensed person, or a person whose class does not match the activity.</p>
      <p>OnGuard’s issued business authority is NSW Master Licence <strong>000110094</strong>. Verify it on the <a href="https://verify.licence.nsw.gov.au/home/Security" target="_blank" rel="noopener noreferrer">SLED public register</a>.</p>
      <p>Since 1 June 2023, former unarmed-guard (old 1A) and crowd-controller (old 1C) activities sit together under the current <strong>Class 1A Security Officer</strong> subclass. Current 1C is cash-in-transit. Current 1D is the only subclass that authorises dog work. Schedule D is the roster rule.</p>
      <p>Mutual recognition under the <em>Mutual Recognition Act 1992</em> (Cth) and automatic mutual recognition may allow an <em>individual</em> licence to travel, subject to notifications and excluded activities. <strong>It does not give OnGuard an interstate master licence.</strong> We do not table a multi-state licence matrix as if we hold those business licences.</p>
    ''')}
    {block("8. WHS, dual-PCBU, first-aid currency, privacy and surveillance", '''
      <p>The <em>Work Health and Safety Act 2011</em> (NSW) applies. OnGuard and the Client are typically both persons conducting a business or undertaking (PCBUs) at the Site (ss 5, 16). Each must consult, cooperate and coordinate (s 46). OnGuard officers must be inducted to Site-specific hazards the occupier controls. We will stop work that presents a serious and imminent risk. A worker may cease unsafe work under s 84.</p>
      <h3>NSW roster rules</h3>
      <ul>
        <li>Every person provided to carry on a security activity holds a current NSW licence of the matching subclass (Schedule D).</li>
        <li>The original licence is worn so as to be clearly visible (s 36) — attached to outer clothing, at or above the waist, front or side.</li>
        <li>The roster records name, licence number, subclass, start and finish for every shift.</li>
        <li>A licence is not lent, hired or used by another person (s 37).</li>
        <li>Fatigue, award breaks and maximum hours are treated as WHS and Fair Work duties, not roster convenience.</li>
      </ul>
      <h3>First-aid currency</h3>
      <p>For crowd control, event, and other 1A posts where first aid is reasonably required by the Site, the event plan or our SOP, the officer’s first-aid unit (typically HLTAID011 or the unit then specified by SLED / the approved Security Licence Course) must be <strong>current</strong>. An officer whose first-aid has expired will not be rostered onto those posts. Currency is checked before the first shift of a booking and at each scheduled refresh.</p>
      <h3>Privacy and surveillance</h3>
      <p>If we are an APP entity under the <em>Privacy Act 1988</em>, or a government contract flows the APPs down, we collect only what the job needs, secure it, and do not disclose it except as the APPs or a law requires. See the <a href="https://www.oaic.gov.au/privacy/australian-privacy-principles" target="_blank" rel="noopener noreferrer">OAIC APPs</a>.</p>
      <p>Covert optical or listening surveillance is restricted under the <em>Surveillance Devices Act 2007</em> (NSW). We do not do it without written lawful authority. Body-worn cameras, if used, are used only as the engagement and the Act allow.</p>
    ''')}
    {block("9. ISO, Australian Standards and quality alignment", '''
      <p><strong>Alignment is not certification.</strong> Alignment means we design jobs, SOPs, incident control and records to the control set named below. Certification means a JAS-ANZ accredited body has issued a current numbered certificate. OnGuard does not, in this Pack, claim a current ISO certificate. If a certificate is issued, it will be scheduled and attached. Claiming a certificate we do not hold is misleading under the ACL (s 18 and related provisions). Evaluation panels must treat “alignment” as <em>not certified</em>.</p>
      <div class="table-wrap"><table class="legal-table">
        <thead><tr><th>Instrument</th><th>Subject</th><th>OnGuard position</th></tr></thead>
        <tbody>
          <tr><td><a href="https://www.iso.org/standard/62085.html" target="_blank" rel="noopener noreferrer">ISO 9001</a></td><td>Quality management</td><td>Alignment of quote, roster, incident and complaint controls. Certificate only if scheduled and attached.</td></tr>
          <tr><td><a href="https://www.iso.org/standard/63380.html" target="_blank" rel="noopener noreferrer">ISO 18788</a></td><td>Security operations management</td><td>Alignment of SOPs, use-of-force, human-rights and incident control. Not a certificate claim.</td></tr>
          <tr><td>ISO 27001</td><td>Information security</td><td>Alignment of handling rules when a contract classifies information. Certificate only if scheduled.</td></tr>
          <tr><td>ISO 31000 / AS ISO 31000</td><td>Risk</td><td>Used in job hazard analysis and event plans.</td></tr>
          <tr><td>ISO 45001</td><td>OHS</td><td>Alignment with PCBU duties under the WHS Act 2011 (NSW).</td></tr>
          <tr><td>AS 4421</td><td>Guards and patrols</td><td>Operational reference for static and patrol work.</td></tr>
          <tr><td><a href="https://www.protectivesecurity.gov.au" target="_blank" rel="noopener noreferrer">PSPF</a> + <a href="https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism" target="_blank" rel="noopener noreferrer">ISM</a> + <a href="https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight" target="_blank" rel="noopener noreferrer">Essential Eight</a></td><td>Commonwealth protective security</td><td>Applied when the NSW Site contract classifies information or systems. Not a DISP claim.</td></tr>
        </tbody>
      </table></div>
    ''')}
    {block("10. Defence, NV1 / NV2, PSPF, DISP and classified work", '''
      <p>Defence, ADF, Defence-prime and classified Commonwealth work on a NSW Site sits under the <a href="https://www.protectivesecurity.gov.au" target="_blank" rel="noopener noreferrer">PSPF</a>, the <a href="https://www.defence.gov.au/business-industry/industry-governance/defence-security-principles-framework" target="_blank" rel="noopener noreferrer">DSPF</a>, the Defence Industry Security Program (DISP), the ISM and the Essential Eight.</p>
      <p><strong>NV1, NV2 and higher clearances.</strong> Classified or Defence work that requires an AGSVA Negative Vetting 1, Negative Vetting 2, Positive Vetting or any higher clearance will be <strong>declined</strong>, or delivered only through a cleared partner under a written subcontract, <strong>until OnGuard holds the named clearance and it is scheduled</strong>. We will not roster an uncleared officer onto a cleared post. We will not tick “held” on a tender form for a clearance we do not hold.</p>
      <p><strong>We will not pretend to hold DISP membership, a facility security clearance, or individual clearances unless those are current and named on a signed schedule.</strong> If a tender requires them, we either evidence them or we decline or partner until they are in force. A false security status is a security incident and a misleading representation.</p>
      <p>As a subcontractor to a DISP member we will comply with flow-down: sponsorship, need-to-know, no uncleared devices, incident reporting, and return or destruction of classified material.</p>
      <p>ITAR/EAR and the <em>Defence Trade Controls Act 2012</em> are out of scope unless a schedule says otherwise. If the Client is a SOCI responsible entity, they must tell us before we start.</p>
    ''')}
    {block("11. Commonwealth and NSW government tenders", '''
      <p>Commonwealth procurement for a NSW Site runs under the <a href="https://www.finance.gov.au/government/procurement/commonwealth-procurement-rules" target="_blank" rel="noopener noreferrer">Commonwealth Procurement Rules</a> (PGPA Act). NSW Government procurement sits under buy.nsw / eTendering. Local government in NSW is under the <em>Local Government Act 1993</em> (NSW) and the council’s procurement policy — a public tender is commonly required above $250,000 including GST, subject to amendment. Confirm the current threshold before you treat this as the award rule.</p>
      <p>This Pack is Annexure A unless the buyer mandates its own deed. We will not bid a price we cannot resource with licensed NSW labour of the correct subclass. Collusive tendering is prohibited.</p>
      <ul class="link-list cols">
        <li><a href="https://www.tenders.gov.au" target="_blank" rel="noopener noreferrer">AusTender</a></li>
        <li><a href="https://buy.nsw.gov.au" target="_blank" rel="noopener noreferrer">buy.nsw</a></li>
        <li><a href="https://www.tenders.nsw.gov.au" target="_blank" rel="noopener noreferrer">NSW eTendering</a></li>
      </ul>
    ''')}
    {block("12. Insurance, indemnities and claims", '''
      <p>We maintain public liability and workers compensation as required at the NSW Site, and will produce certificates of currency. Do not assume a limit or an insurer until you have the current certificate. Our indemnity covers loss to the extent caused by our negligence or wilful default, reduced by the Client’s or a third party’s contribution, and capped as in section 5 except where the law forbids a cap.</p>
      <p>Notify claims immediately to <a href="tel:+61432893343">0432 893 343</a> and <a href="mailto:admin@ogprotection.com.au">admin@ogprotection.com.au</a>. Do not admit liability on our behalf.</p>
    ''')}
    {block("13. Personnel, subcontractors and modern slavery", '''
      <p>Every operative on a licensed activity holds a current NSW licence of the correct subclass (Schedule D). We may subcontract to another NSW master-licensed provider and remain responsible to the Client. The <em>Modern Slavery Act 2018</em> (Cth) reporting obligation applies above the revenue threshold. Whether or not we are a reporting entity in a given year, we will not use bonded, trafficked or child labour.</p>
    ''')}
    {block("14. Confidentiality, IP and records", '''
      <p>Each party keeps the other’s confidential information confidential except for insurers, lawyers, regulators, and as a court or statute requires. Run-sheets, event plans and SOPs we create remain our IP; the Client gets a licence for the Site and the term. We keep operational records for at least seven years, or longer if a government contract says so.</p>
    ''')}
    {block("15. Fees, variations, cancellation and force majeure", '''
      <p>Fees are as quoted. Variations must be agreed in writing where practicable. Payment is 14 days from invoice unless the quote says otherwise.</p>
      <p>Cancellation more than 72 hours before start: no fee. Inside 72 hours: a fee not exceeding unavoidable labour and travel we cannot redeploy — a genuine pre-estimate, not a penalty. If we cancel other than for force majeure or Client breach, the Client pays nothing for the cancelled portion and may claim an ACL remedy if one applies.</p>
      <p>Force majeure includes flood, fire, pandemic direction, industrial action we do not control, and a government order that makes the deployment unlawful. The ACL still applies to any failure not genuinely caused by the event.</p>
    ''')}
    {block("16. Complaints, disputes and regulators", '''
      <p>Complain to us first. If unresolved: NCAT; a court of competent jurisdiction; the ACCC or NSW Fair Trading; SLED for licence conduct; SafeWork NSW for WHS; the OAIC for privacy. Nothing here is an arbitration clause that blocks a statutory complaint.</p>
    ''')}
    {block("17. Governing law", '''
      <p>Laws of New South Wales and the Commonwealth of Australia. Non-exclusive jurisdiction of the courts of NSW. Invalid provisions are severed or read down. The Pack plus the accepted quote or purchase order is the entire agreement, except for any non-excludable statutory term. The version cited on the quote is the version that applies to that booking.</p>
    ''')}
    {block("Schedule D — NSW individual licence classes (current post-2023)", '''
      <p>Authorities below are taken from s 11 and s 12 of the <em>Security Industry Act 1997</em> (NSW) as in force after the 1 June 2023 reforms. The class on the officer must match the activity. This is the roster rule, not a training brochure. A Class 1A, 1B, 1C, 1E or 1F licence <strong>does not</strong> authorise security activity with a dog.</p>
      <div class="table-wrap"><table class="legal-table">
        <thead><tr><th>Class</th><th>Authority (Act)</th><th>Typical OnGuard use</th><th>Will not deploy</th></tr></thead>
        <tbody>
          <tr>
            <td><strong>1A Security Officer</strong></td>
            <td>Patrol, protect or guard property while unarmed (static or mobile); <em>and</em> act as a crowd controller or in a similar capacity.</td>
            <td>Core roster: static, patrol, concierge, construction gate, venue door, floor, festival barrier, bag search, event close-out.</td>
            <td class="will-not">Armed work. Cash-in-transit. Dog teams. A 1A on a 1C/1D/1F post.</td>
          </tr>
          <tr>
            <td><strong>1B Bodyguard</strong></td>
            <td>Act as a bodyguard or in a similar capacity.</td>
            <td>Close personal protection only if the quote names a 1B holder and the principal.</td>
            <td class="will-not">Unscoped VIP work. A 1A standing in as a bodyguard.</td>
          </tr>
          <tr>
            <td><strong>1C Cash-in-Transit Guard</strong></td>
            <td>Patrol, protect or guard cash-in-transit. Armed CIT also requires 1F plus a firearms authority.</td>
            <td>Not a current OnGuard product line.</td>
            <td class="will-not">Any CIT run. A 1A used as a cash escort. Claiming old “1C = crowd controller”.</td>
          </tr>
          <tr>
            <td><strong>1D Guard Dog Handler</strong></td>
            <td>Patrol, protect or guard any property <em>with a dog</em>. The only Class 1 subclass that authorises dog work.</td>
            <td>Named dog team on a quote: night static, compound, industrial gate. Handler holds 1D. Dog is identified on the run-sheet.</td>
            <td class="will-not">Improvised animals. A 1A walking a dog. Dog work that is not on the quote.</td>
          </tr>
          <tr>
            <td><strong>1E Monitoring Centre Operator</strong></td>
            <td>Patrol, protect or guard property while carrying on monitoring-centre operations.</td>
            <td>Not a current OnGuard product line.</td>
            <td class="will-not">Claiming a 1E monitoring post we do not staff.</td>
          </tr>
          <tr>
            <td><strong>1F Armed Guard</strong></td>
            <td>Patrol, protect or guard approved classes of property while armed, and only under a firearms licence/permit under the <em>Firearms Act 1996</em> (NSW).</td>
            <td>Not offered unless separately licensed, insured and scheduled.</td>
            <td class="will-not">Firearms on a 1A roster. An armed 1C CIT run without 1F.</td>
          </tr>
          <tr>
            <td><strong>2A Security Consultant</strong></td>
            <td>Sell security methods or principles; act as a consultant by identifying and analysing security risks.</td>
            <td>Only if a 2A holder is named on the quote.</td>
            <td class="will-not">Unlicensed security consulting sold as “advice from the guard”.</td>
          </tr>
          <tr>
            <td><strong>2B Security Seller</strong></td>
            <td>Sell, and provide advice in relation to, security equipment. Does not authorise install, maintain or repair.</td>
            <td>Not a current OnGuard product line.</td>
            <td class="will-not">Selling or specifying equipment under a 1A.</td>
          </tr>
          <tr>
            <td><strong>2C Security Equipment Specialist</strong></td>
            <td>Sell, install, maintain, repair and service security equipment (including electronic and barrier equipment) and act as a locksmith.</td>
            <td>Not a current OnGuard product line.</td>
            <td class="will-not">Locksmithing, alarm install or CCTV install under a Class 1.</td>
          </tr>
          <tr>
            <td><strong>2D Security Trainer</strong></td>
            <td>Provide training, assessment or instruction in relation to any security activity. Does not extend to firearms training.</td>
            <td>Only if a 2D holder (and, where required, an RTO) is named.</td>
            <td class="will-not">Unlicensed “in-house training” sold as a licensed course. Firearms instruction.</td>
          </tr>
        </tbody>
      </table></div>
      <p>Master licence 000110094 authorises the <em>business</em> to provide licensed persons. It is not a substitute for the individual subclass. Loss-prevention activities formerly under old 1G sit inside current 1A.</p>
    ''')}
    {block("Schedule F — Tender attachment checklist", '''
      <ul>
        <li>This PDF as Annexure A — Legal, Liability and Compliance (NSW).</li>
        <li>Current SLED extract for Master Licence 000110094.</li>
        <li>Certificates of currency (public liability and workers compensation as a minimum).</li>
        <li>Named roster for the first four weeks: officer, licence number, subclass, expiry, first-aid expiry where the post requires it.</li>
        <li>If the RFT demands a numbered ISO certificate, DISP membership, NV1, NV2 or a higher clearance — attach the current instrument <em>or</em> mark the requirement as not held / condition subsequent. Do not tick “held” if it is not held.</li>
        <li>If a dog team is proposed — 1D licence, animal identification, and the Site’s animal policy.</li>
        <li>If the Site is outside NSW — do not bid unless a local master/firm licence is attached.</li>
      </ul>
    ''')}

    <section class="legal-links">
      <h2>Official references</h2>
      <ul class="link-list cols">
        <li><a href="https://www.accc.gov.au/consumers/buying-products-and-services/consumer-rights-and-guarantees" target="_blank" rel="noopener noreferrer">ACCC consumer guarantees</a></li>
        <li><a href="https://www.legislation.gov.au/C2004A00109" target="_blank" rel="noopener noreferrer">Competition and Consumer Act 2010</a></li>
        <li><a href="https://legislation.nsw.gov.au/view/html/inforce/current/act-1997-157" target="_blank" rel="noopener noreferrer">Security Industry Act 1997 (NSW)</a></li>
        <li><a href="https://verify.licence.nsw.gov.au/home/Security" target="_blank" rel="noopener noreferrer">NSW SLED register</a></li>
        <li><a href="https://legislation.nsw.gov.au/view/html/inforce/current/act-2011-010" target="_blank" rel="noopener noreferrer">Work Health and Safety Act 2011 (NSW)</a></li>
        <li><a href="https://www.finance.gov.au/government/procurement/commonwealth-procurement-rules" target="_blank" rel="noopener noreferrer">Commonwealth Procurement Rules</a></li>
        <li><a href="https://buy.nsw.gov.au" target="_blank" rel="noopener noreferrer">buy.nsw</a></li>
        <li><a href="https://www.protectivesecurity.gov.au" target="_blank" rel="noopener noreferrer">Protective Security Policy Framework</a></li>
        <li><a href="https://www.defence.gov.au/business-industry/industry-governance/defence-security-principles-framework" target="_blank" rel="noopener noreferrer">DSPF / DISP</a></li>
        <li><a href="https://www.oaic.gov.au/privacy/australian-privacy-principles" target="_blank" rel="noopener noreferrer">Australian Privacy Principles</a></li>
        <li><a href="https://www.safework.nsw.gov.au" target="_blank" rel="noopener noreferrer">SafeWork NSW</a></li>
        <li><a href="https://www.iso.org/standard/63380.html" target="_blank" rel="noopener noreferrer">ISO 18788</a></li>
      </ul>
      <p><a class="btn btn-primary" href="{PDF}" download>Download the full PDF (all pages)</a></p>
      <p class="form-note">Prepared by Tech Aid Australia (ABN 33 959 110 665). Not legal advice on a specific contract. Have a solicitor mark up any high-value deed. Official ACCC, Commonwealth and ISO logos are not reproduced — those marks belong to their owners.</p>
    </section>
  </article>
  {gp.quote_form()}
</main>
{footer}
</body>
</html>"""
    OUT.write_text(html, encoding="utf-8")
    print("Wrote", OUT)


if __name__ == "__main__":
    page()
