#!/usr/bin/env python3
"""Write legal/index.html using shared site chrome."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generate_pages as gp

OUT = Path(__file__).resolve().parent / "index.html"
PDF = "OnGuard-Protection-Legal-Compliance-Pack.pdf"


def block(title, body):
    return f"""<details class="legal-drop">
  <summary>{title}</summary>
  <div class="legal-drop-body">{body}</div>
</details>"""


def page():
    url = f"{gp.SITE}/legal/"
    title = "Legal, Liability & Compliance Pack | OnGuard Protection"
    desc = "ACCC-compliant terms, refunds, limitation of liability, all-state security licensing, ISO alignment, Defence/DISP and government tender conditions. NSW Master Licence 000110094."
    crumbs = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{gp.SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Legal", "item": url},
        ],
    }
    extra = '<link rel="preload" as="image" href="../assets/brand/onguard-lockup-480.webp" type="image/webp">'
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
    <img src="../assets/brand/onguard-lockup-480.webp" width="220" height="90" alt="OnGuard Protection">
    <p class="eyebrow">Document OG-LEG-2026-001 · Version 1.0</p>
    <h1>Legal, liability, refunds and compliance pack</h1>
    <p class="lead">Limitation of liability written to survive the Australian Consumer Law. ACCC. All States and Territories. ISO alignment. Defence and council tenders. This is the long version — the one an evaluation panel can file.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{PDF}" download>Download the full PDF</a>
      <a class="btn btn-ghost" href="https://verify.licence.nsw.gov.au/home/Security" target="_blank" rel="noopener noreferrer">Verify NSW licence 000110094</a>
    </div>
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
      <figcaption>Tender / Defence gates</figcaption>
      <ol class="gate-row">
        <li>Licence</li>
        <li>ACL / UCT</li>
        <li>WHS + insurance</li>
        <li>ISO alignment</li>
        <li>Privacy</li>
        <li>DISP / clearances</li>
        <li>Licensed roster</li>
      </ol>
      <p>A red stop at any gate means we do not bid, or we mark the deed up. We do not invent ISO certificates or DISP membership.</p>
    </figure>
  </div>

  <article class="container legal-prose">
    {block("1. Status of this document and how to use it", '''
      <p>This Pack is the public legal framework of OnGuard Protection. It applies to website enquiries, quotations, purchase orders, event bookings, patrol and static contracts, and any RFT, RFQ, panel or standing offer issued by a Commonwealth entity, a State or Territory agency, a local council, a GOC, or a Defence prime.</p>
      <p>OnGuard currently holds New South Wales Security Master Licence <strong>000110094</strong> under the <em>Security Industry Act 1997</em> (NSW), administered by SLED. We do not represent that we hold a master licence in every other jurisdiction unless a current licence number is stated on the quote. Cross-border work is only accepted once the required licence is in force.</p>
      <p>Where a signed engagement, purchase order or deed exists, that instrument prevails to the extent of inconsistency — except that the Australian Consumer Law always prevails.</p>
    ''')}
    {block("2. Parties, definitions and interpretation", '''
      <p><strong>Client</strong> means the person or entity that requests or receives services. <strong>Consumer</strong> has the meaning in s 3 of the ACL (household-type services, or a price at or under the prescribed threshold — currently $100,000). <strong>Services</strong> means crowd control, event security, static guarding, mobile patrols, alarm response, corporate concierge, access control and asset protection. <strong>Regulator</strong> includes the ACCC, SLED, a State licensing authority, SafeWork / WorkSafe, the OAIC, and a Defence security authority.</p>
      <p>If a provision is void, the rest continues. Nothing in this Pack is a warranty that a particular ISO certificate, DISP membership or security clearance is currently held — those are stated, if at all, only on a signed schedule.</p>
    ''')}
    {block("3. Scope of services", '''
      <p>OnGuard supplies licensed security labour and site presence. We do not, unless a separate written instrument says so, supply locksmithing, firearms, cash-in-transit, private inquiry, or covert electronic surveillance. The Client remains responsible for site induction content only the occupier can provide, and for directions that would require us to break the law.</p>
      <p>A quotation is an invitation to treat unless stated to be a standing offer. A contract is formed when we confirm the booking in writing or first deploy after a clear instruction to proceed.</p>
    ''')}
    {block("4. Australian Consumer Law, ACCC and refunds", '''
      <p>The ACL is Schedule 2 to the <em>Competition and Consumer Act 2010</em> (Cth). It is applied as a law of each State and Territory. The <a href="https://www.accc.gov.au/consumers/buying-products-and-services/consumer-rights-and-guarantees" target="_blank" rel="noopener noreferrer">ACCC</a> and State consumer agencies enforce it.</p>
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
        <li>If we disagree, we say why in writing and name the tribunal, court or consumer agency.</li>
      </ol>
      <p>Help: <a href="https://www.accc.gov.au" target="_blank" rel="noopener noreferrer">ACCC</a> 1300 302 502.</p>
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
    {block("7. Licensing — all Australian States and Territories", '''
      <p>Security is licensed in every jurisdiction. A master (or firm/agent) licence authorises the business. Each officer must hold the correct class. We will not deploy an unlicensed person to a licensed activity.</p>
      <div class="table-wrap"><table class="legal-table">
        <thead><tr><th>Jurisdiction</th><th>Principal Act</th><th>Business licence</th><th>Regulator</th></tr></thead>
        <tbody>
          <tr><td>NSW</td><td>Security Industry Act 1997</td><td>Master licence <strong>000110094</strong></td><td><a href="https://verify.licence.nsw.gov.au/home/Security" target="_blank" rel="noopener noreferrer">SLED register</a></td></tr>
          <tr><td>Victoria</td><td>Private Security Act 2004</td><td>Business (operator) licence</td><td>Victoria Police LRD</td></tr>
          <tr><td>Queensland</td><td>Security Providers Act 1993</td><td>Security firm licence</td><td>Office of Fair Trading</td></tr>
          <tr><td>Western Australia</td><td>Security and Related Activities (Control) Act 1996</td><td>Agent / crowd control agent</td><td>WA Police Licensing</td></tr>
          <tr><td>South Australia</td><td>Security and Investigation Industry Act 1995</td><td>Agent licence</td><td>CBS</td></tr>
          <tr><td>Tasmania</td><td>Security and Investigations Agents Act 2002</td><td>Agent licence</td><td>CBOS</td></tr>
          <tr><td>ACT</td><td>Security Industry Act 2003</td><td>Master licence</td><td>Access Canberra</td></tr>
          <tr><td>Northern Territory</td><td>Private Security Act 1995</td><td>Firm / officer licences</td><td>Licensing NT</td></tr>
        </tbody>
      </table></div>
      <p>Mutual recognition may allow an <em>individual</em> licence to travel. It does not automatically authorise a company to carry on a security business in a second State if that State requires its own master/firm licence. We only accept those jobs once that licence is in force.</p>
    ''')}
    {block("8. WHS, privacy and surveillance", '''
      <p>Model WHS Acts apply in the Commonwealth, NSW, QLD, SA, TAS, ACT and NT. Victoria: <em>OHS Act 2004</em>. WA: <em>WHS Act 2020</em>. OnGuard and the Client are typically both PCBUs and must consult, cooperate and coordinate. We will stop work that presents a serious and imminent risk.</p>
      <p>If we are an APP entity under the <em>Privacy Act 1988</em>, or a government contract flows the APPs down, we collect only what the job needs, secure it, and do not disclose it except as the APPs or a law requires. See the <a href="https://www.oaic.gov.au/privacy/australian-privacy-principles" target="_blank" rel="noopener noreferrer">OAIC APPs</a>.</p>
      <p>Covert optical or listening surveillance is restricted under State surveillance-devices legislation. We do not do it without written lawful authority. Body-worn cameras, if used, are used only as the engagement and the Act allow.</p>
    ''')}
    {block("9. ISO, Australian Standards and quality alignment", '''
      <p>This Pack distinguishes <strong>alignment</strong> (jobs designed to the control set) from <strong>certification</strong> (a JAS-ANZ accredited body has issued a current certificate). We do not, on this page, claim a current ISO certificate. If one is issued, it will be scheduled to the contract. Claiming a certificate we do not hold is misleading under the ACL.</p>
      <div class="table-wrap"><table class="legal-table">
        <thead><tr><th>Instrument</th><th>Subject</th><th>OnGuard position</th></tr></thead>
        <tbody>
          <tr><td><a href="https://www.iso.org/standard/62085.html" target="_blank" rel="noopener noreferrer">ISO 9001</a></td><td>Quality management</td><td>Alignment. Certificate only if scheduled.</td></tr>
          <tr><td><a href="https://www.iso.org/standard/63380.html" target="_blank" rel="noopener noreferrer">ISO 18788</a></td><td>Security operations management</td><td>SOPs, use-of-force, incident control.</td></tr>
          <tr><td>ISO 27001</td><td>Information security</td><td>Alignment. Often required for DISP / ICT packages.</td></tr>
          <tr><td>ISO 31000 / AS ISO 31000</td><td>Risk</td><td>Job hazard analysis and event plans.</td></tr>
          <tr><td>ISO 45001</td><td>OHS</td><td>Alignment with PCBU duties.</td></tr>
          <tr><td>AS 4421</td><td>Guards and patrols</td><td>Operational reference for static and patrol work.</td></tr>
          <tr><td><a href="https://www.protectivesecurity.gov.au" target="_blank" rel="noopener noreferrer">PSPF</a> + <a href="https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism" target="_blank" rel="noopener noreferrer">ISM</a> + <a href="https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight" target="_blank" rel="noopener noreferrer">Essential Eight</a></td><td>Commonwealth protective security</td><td>Applied when the contract classifies information or systems.</td></tr>
        </tbody>
      </table></div>
    ''')}
    {block("10. Defence, military, PSPF, DISP and classified work", '''
      <p>Defence, ADF, Defence-prime and classified Commonwealth work sits under the <a href="https://www.protectivesecurity.gov.au" target="_blank" rel="noopener noreferrer">PSPF</a>, the <a href="https://www.defence.gov.au/business-industry/industry-governance/defence-security-principles-framework" target="_blank" rel="noopener noreferrer">DSPF</a>, the Defence Industry Security Program (DISP), the ISM and the Essential Eight. DISP is security vetting for Australian businesses. Many Defence contracts require it before a supplier may handle classified information or access a Defence site.</p>
      <p><strong>We will not pretend to hold DISP membership, a facility security clearance, or individual clearances unless those are current and named on a signed schedule.</strong> If a tender requires them, we either evidence them or we decline or partner until they are in force. A false security status is a security incident and a misleading representation.</p>
      <p>As a subcontractor to a DISP member we will comply with flow-down: sponsorship, need-to-know, no uncleared devices, incident reporting, and return or destruction of classified material. Uncleared officers will not be put on a cleared post.</p>
      <p>ITAR/EAR and the <em>Defence Trade Controls Act 2012</em> are out of scope unless a schedule says otherwise. If the Client is a SOCI responsible entity, they must tell us before we start.</p>
    ''')}
    {block("11. Commonwealth, State and local government tenders", '''
      <p>Commonwealth procurement runs under the <a href="https://www.finance.gov.au/government/procurement/commonwealth-procurement-rules" target="_blank" rel="noopener noreferrer">Commonwealth Procurement Rules</a> (PGPA Act). Core rules: value for money, non-discrimination, transparency, and open tender on <a href="https://www.tenders.gov.au" target="_blank" rel="noopener noreferrer">AusTender</a> above threshold unless an exemption applies. Local government is under each State’s Local Government Act and the council’s policy (in NSW a public tender is commonly required above $250,000 including GST, subject to amendment).</p>
      <p>This Pack is Annexure A unless the buyer mandates its own deed. We will not bid a price we cannot resource with licensed labour. Collusive tendering is prohibited.</p>
      <ul class="link-list cols">
        <li><a href="https://www.tenders.gov.au" target="_blank" rel="noopener noreferrer">AusTender</a></li>
        <li><a href="https://buy.nsw.gov.au" target="_blank" rel="noopener noreferrer">buy.nsw</a></li>
        <li><a href="https://www.buyingfor.vic.gov.au" target="_blank" rel="noopener noreferrer">Buying for Victoria</a></li>
        <li><a href="https://qtenders.hpw.qld.gov.au" target="_blank" rel="noopener noreferrer">QTenders</a></li>
        <li><a href="https://www.tenders.wa.gov.au" target="_blank" rel="noopener noreferrer">Tenders WA</a></li>
        <li><a href="https://www.tenders.sa.gov.au" target="_blank" rel="noopener noreferrer">SA Tenders</a></li>
        <li><a href="https://www.purchasing.tas.gov.au" target="_blank" rel="noopener noreferrer">Tasmania Purchasing</a></li>
        <li><a href="https://tenders.act.gov.au" target="_blank" rel="noopener noreferrer">Tenders ACT</a></li>
        <li><a href="https://tendersonline.nt.gov.au" target="_blank" rel="noopener noreferrer">NT Tenders Online</a></li>
      </ul>
    ''')}
    {block("12. Insurance, indemnities and claims", '''
      <p>We maintain public liability and workers compensation as required at the Site, and will produce certificates of currency. Do not assume a limit or an insurer until you have the current certificate. Our indemnity covers loss to the extent caused by our negligence or wilful default, reduced by the Client’s or a third party’s contribution, and capped as in section 5 except where the law forbids a cap.</p>
      <p>Notify claims immediately to <a href="tel:+61432893343">0432 893 343</a> and <a href="mailto:admin@ogprotection.com.au">admin@ogprotection.com.au</a>. Do not admit liability on our behalf.</p>
    ''')}
    {block("13. Personnel, subcontractors and modern slavery", '''
      <p>Every operative on a licensed activity holds a current licence of the correct class. We may subcontract to another master-licensed provider and remain responsible to the Client. The <em>Modern Slavery Act 2018</em> (Cth) reporting obligation applies above the revenue threshold. Whether or not we are a reporting entity in a given year, we will not use bonded, trafficked or child labour.</p>
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
      <p>Complain to us first. If unresolved: NCAT, VCAT, QCAT, SACAT, SAT, TASCAT, ACAT or NTCAT as applicable; a court of competent jurisdiction; the ACCC or a State consumer agency; SLED or the local licensing authority; SafeWork / WorkSafe; the OAIC. Nothing here is an arbitration clause that blocks a statutory complaint.</p>
    ''')}
    {block("17. Governing law", '''
      <p>Laws of New South Wales and the Commonwealth of Australia. Non-exclusive jurisdiction of the courts of NSW. Invalid provisions are severed or read down. The Pack plus the accepted quote or purchase order is the entire agreement, except for any non-excludable statutory term. The version cited on the quote is the version that applies to that booking.</p>
    ''')}

    <section class="legal-links">
      <h2>Official references</h2>
      <ul class="link-list cols">
        <li><a href="https://www.accc.gov.au/consumers/buying-products-and-services/consumer-rights-and-guarantees" target="_blank" rel="noopener noreferrer">ACCC consumer guarantees</a></li>
        <li><a href="https://www.legislation.gov.au/C2004A00109" target="_blank" rel="noopener noreferrer">Competition and Consumer Act 2010</a></li>
        <li><a href="https://verify.licence.nsw.gov.au/home/Security" target="_blank" rel="noopener noreferrer">NSW SLED register</a></li>
        <li><a href="https://www.finance.gov.au/government/procurement/commonwealth-procurement-rules" target="_blank" rel="noopener noreferrer">Commonwealth Procurement Rules</a></li>
        <li><a href="https://www.protectivesecurity.gov.au" target="_blank" rel="noopener noreferrer">Protective Security Policy Framework</a></li>
        <li><a href="https://www.defence.gov.au/business-industry/industry-governance/defence-security-principles-framework" target="_blank" rel="noopener noreferrer">DSPF / DISP</a></li>
        <li><a href="https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight" target="_blank" rel="noopener noreferrer">Essential Eight</a></li>
        <li><a href="https://www.oaic.gov.au/privacy/australian-privacy-principles" target="_blank" rel="noopener noreferrer">Australian Privacy Principles</a></li>
        <li><a href="https://www.safeworkaustralia.gov.au" target="_blank" rel="noopener noreferrer">Safe Work Australia</a></li>
        <li><a href="https://www.iso.org/standard/63380.html" target="_blank" rel="noopener noreferrer">ISO 18788</a></li>
      </ul>
      <p><a class="btn btn-primary" href="{PDF}" download>Download the full PDF (all pages)</a></p>
      <p class="form-note">Not legal advice on a specific contract. Have a solicitor mark up any high-value deed. Official ACCC, Commonwealth and ISO logos are not reproduced — those marks belong to their owners.</p>
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
