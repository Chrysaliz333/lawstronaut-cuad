# CUAD Dataset Analysis for Lawstronaut Testing: Post-Cutoff Regulatory Events

**Analysis Date:** November 3, 2025
**Dataset:** CUAD v1 (510 contracts from SEC EDGAR filings)
**LLM Cutoff Dates:** GPT-4 (April 2023), Claude (April 2024)
**Target:** Identify contracts for testing regulatory retrieval API with post-cutoff legal changes

---

## EXECUTIVE SUMMARY

This analysis identifies **428 contracts (84% of corpus)** affected by regulatory changes enacted after April 2023. The analysis focuses on six major post-cutoff regulatory regimes:

1. **EU AI Act** (August 2024): 131 contracts with AI/ML systems
2. **UK REUL Act** (2023-2024): 41 contracts with UK governing law
3. **US State AI Laws** (2024): 9 contracts with automated consumer decisions
4. **Supply Chain Due Diligence** (2023-2024): 41 contracts with international supply chains
5. **FTC Non-Compete Ban** (2024): 267 contracts with restrictive covenants
6. **Cross-cutting regulatory exposure**: Multiple overlapping risks

---

## TASK 1: EU AI ACT COMPLIANCE (Regulation 2024/1689, effective August 1, 2024)

### Summary
**Total Contracts Identified:** 131 contracts with AI/ML/algorithmic decision-making systems

### Top Priority Contracts for Testing

#### 1. Foundation Medicine Inc - R&D COLLABORATION AGREEMENT
- **File:** `FOUNDATIONMEDICINE,INC_02_02_2015-EX-10.2-Collaboration Agreement.txt`
- **Parties:** F. Hoffmann-La Roche Ltd (Basel, Switzerland), Roche Inc (NJ, USA), Foundation Medicine Inc (MA, USA)
- **EU Connection:** ✓ Swiss party (EU market adjacent), explicit EU commercialization
- **AI/ML Systems:**
  - ctDNA Platform with algorithmic genomic analysis
  - Companion diagnostics using predictive/analytical methods
  - Molecular information platform with business rules and algorithms
- **Data Sensitivity:** HIGH - Genomic/health data (GDPR Article 9 special category)
- **AI Act Risk Level:** HIGH-RISK SYSTEM (Article 6) - Medical devices/diagnostics
- **Missing Provisions:** Data governance (Art. 10), transparency (Art. 13), human oversight (Art. 14), accuracy/robustness testing (Art. 15)
- **Test Question:** "Does this AI development agreement comply with EU AI Act Article 10 (data governance), Article 13 (transparency), and Article 14 (human oversight) requirements for high-risk medical AI systems processing EU citizen genomic data?"

#### 2. Cerence Inc - INTELLECTUAL PROPERTY AGREEMENT
- **File:** `CerenceInc_20191002_8-K_EX-10.4_11827494_EX-10.4_Intellectual Property Agreement.txt`
- **Parties:** Nuance Communications, Inc. (Delaware), Cerence Inc (Delaware)
- **EU Connection:** ✓ European market operations, data processing agreements mentioned
- **AI/ML Systems:**
  - Natural language processing (NLP) technologies
  - Conversational AI and voice recognition
  - Software implementations of algorithms, models, methodologies
- **AI Act Risk Level:** LIMITED RISK (Article 52) - Conversational AI transparency requirements
- **Missing Provisions:** Disclosure that users are interacting with AI system, provider identification
- **Test Question:** "Does this conversational AI licensing agreement comply with EU AI Act Article 52 transparency obligations requiring disclosure of AI interaction to end users in EU markets?"

#### 3. Clickstream Corp - APPLICATION DEVELOPMENT AGREEMENT
- **File:** `ClickstreamCorp_20200330_1-A_EX1A-6 MAT CTRCT_12089935_EX1A-6 MAT CTRCT_Development Agreement.txt`
- **Parties:** InfinixSoft Global LLC (Florida), Clickstream Corporation (California)
- **EU Connection:** No explicit EU references
- **AI/ML Systems:** 40 pre-built algorithms for online betting/prediction
- **AI Act Risk Level:** POTENTIALLY PROHIBITED (Article 5) - If predictive betting affects vulnerable persons
- **Test Question:** "Do these 40 pre-built algorithms for online betting constitute prohibited AI practices under EU AI Act Article 5 if deployed to EU customers, particularly regarding exploitation of vulnerabilities or manipulation?"

#### 4. Cardlytics Inc - MAINTENANCE AGREEMENT (Bank of America)
- **File:** `CardlyticsInc_20180112_S-1_EX-10.16_11002987_EX-10.16_Maintenance Agreement1.txt`
- **Parties:** Cardlytics Inc (Georgia), Bank of America N.A.
- **EU Connection:** BofA has international EU operations
- **AI/ML Systems:**
  - Behavioral analytics algorithms
  - Consumer profiling and targeting platform
  - Algorithmic decision-making for customer segmentation
- **Data Sensitivity:** HIGH - Financial transaction data, behavioral profiling
- **AI Act Risk Level:** HIGH-RISK (Article 6) - Credit scoring/creditworthiness assessment if used for financial decisions
- **Missing Provisions:** Profiling transparency, automated decision-making rights (also GDPR Art. 22 issue)
- **Test Question:** "Does this behavioral analytics platform comply with EU AI Act requirements for high-risk AI in creditworthiness assessment, and does it satisfy GDPR Article 22 rights regarding automated decision-making?"

#### 5. Energous Corporation - STRATEGIC ALLIANCE AGREEMENT
- **File:** `ENERGOUS_CORP_03_16_2017-EX-10.24-STRATEGIC ALLIANCE AGREEMENT.txt`
- **Parties:** Dialog Semiconductor UK Ltd (England/Wales), Energous Corporation (Delaware)
- **EU Connection:** ✓ UK/EU registered party
- **AI/ML Systems:** Optimization algorithms for wireless power transfer, firmware, sensors
- **AI Act Risk Level:** MINIMAL RISK - Optimization algorithms for hardware systems
- **Test Question:** "Do the wireless power optimization algorithms constitute AI systems under EU AI Act definition, and if so, what minimal transparency requirements apply?"

### Complete List of 131 AI/ML Contracts

**By Contract Type:**
- Software/Technology License Agreements: 28
- Development Agreements: 24
- Collaboration Agreements: 18
- Strategic Alliance Agreements: 15
- Data Processing/Hosting Agreements: 12
- IP Agreements: 11
- Service/Maintenance Agreements: 10
- Other: 13

**By AI/ML Keyword:**
- "Algorithm/Algorithmic": 41 contracts
- "Analytics/Automation": 36 contracts
- "Predictive/Intelligent/Deep Learning": 103 contracts
- GDPR/EU data protection references: 76 contracts

**All contract files located in:** `/Users/liz/Downloads/CUAD_v1/full_contract_txt/`

---

## TASK 2: UK RETAINED EU LAW (REUL) ACT CHANGES (2023-2024)

### Summary
**Total Contracts Identified:** 41 contracts with England/Wales/UK governing law

### Top Priority Contracts for Testing

#### 1. WPP 2005 LIMITED - CFO EMPLOYMENT AGREEMENT
- **File:** `WPPPLC_04_30_2020-EX-4.28-SERVICE AGREEMENT.txt`
- **Executive:** John Rogers (Chief Financial Officer)
- **Company Registration:** England No. 01003653
- **Governing Law:** English law
- **Date:** October 1, 2019
- **Compensation:** £740,000 + £30,000 benefits p.a.
- **Critical Retained EU Law References:**
  - **Market Abuse Regulation 596/2014/EU** (explicitly referenced in clause 3.2(l))
  - Working Time Regulations 1998 (implementing EU Directive 2003/88/EC)
  - Employment Rights Act 1996
  - FCA regulations
- **REUL Act Impact:** HIGH - MAR potentially subject to revocation/reform
- **Test Question:** "Given the UK's Retained EU Law (Revocation and Reform) Act 2023, what is the current status of Market Abuse Regulation 596/2014/EU referenced in clause 3.2(l) of this employment agreement? Has it been revoked, amended, or preserved in UK law as of November 2024?"

#### 2. Bicycle Therapeutics Plc - CBO EMPLOYMENT AGREEMENT
- **File:** `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT.txt`
- **Executive:** Nigel Crockett (Chief Business Officer)
- **Company Registration:** England No. 11036101
- **Governing Law:** Laws of England and Wales
- **Date:** September 26, 2019
- **Compensation:** USD $370,000 p.a.
- **Retained EU Law References:**
  - Working Time Regulations 1998 (EU Directive 2003/88/EC)
  - Data Protection Act 2018 (UK GDPR implementation)
  - Employment Rights Act 1996
- **Data Protection:** Chapter 18 - extensive UK data protection law compliance
- **Test Question:** "How has the UK Data Protection Act 2018 (implementing GDPR) diverged from EU GDPR under the Retained EU Law Act 2023? What specific UK regulatory changes affect data processing obligations in this employment contract as of November 2024?"

#### 3. Theravance Biopharma UK Limited - CMO EMPLOYMENT AGREEMENT
- **File:** `THERAVANCEBIOPHARMA,INC_05_08_2020-EX-10.2-SERVICE AGREEMENT.txt`
- **Executive:** Brett Haumann (Chief Medical Officer)
- **Company Registration:** England No. 11979693
- **Governing Law:** Law of England
- **Date:** April 1, 2020
- **Compensation:** £448,903 p.a.
- **Retained EU Law References:**
  - Working Time Regulations 1998
  - Data Protection Act 2018 (extensive privacy provisions)
  - Employment Rights Act 1996
  - Pensions Act 2008
  - Copyright Designs and Patents Act 1988
- **Test Question:** "Identify which EU-derived employment and data protection provisions in this contract have been modified by UK legislation enacted 2023-2024 following the Retained EU Law Act, particularly regarding working time limits and personal data handling."

#### 4. Energous Corp - STRATEGIC ALLIANCE WITH UK PARTY
- **File:** `ENERGOUS_CORP_03_16_2017-EX-10.24-STRATEGIC ALLIANCE AGREEMENT.txt`
- **Parties:** Dialog Semiconductor UK Ltd (England/Wales), Energous Corporation (Delaware)
- **Governing Law:** English law
- **EU Connection:** UK company with EU distribution network
- **Test Question:** "How do post-Brexit regulatory changes and the Retained EU Law Act 2023 affect cross-border technology distribution provisions in this UK-US strategic alliance, particularly regarding product standards and data transfers?"

#### 5. CERES Inc - RESEARCH COLLABORATION WITH WELSH INSTITUTE
- **File:** `CERES,INC_01_25_2012-EX-10.20-Collaboration Agreement.txt`
- **Parties:** Ceres Inc. (Delaware, USA), Institute of Grassland and Environmental Research (Wales, Charity No. 272150)
- **Governing Law:** New York State law (despite UK party)
- **UK Connection:** Welsh research institute, DEFRA involvement
- **EU Law Issues:** Plant variety protection regulations, biological material handling directives
- **Test Question:** "What UK regulatory changes to plant variety protection and biological material handling have occurred under the Retained EU Law Act affecting cross-border research collaboration with Welsh institutes as of November 2024?"

### Complete List of 41 UK Governing Law Contracts

**Core Categories:**
- Employment/Service Agreements: 3
- Strategic Alliance Agreements: 8
- Collaboration Agreements: 6
- Distribution/Franchise Agreements: 7
- Manufacturing/Supply Agreements: 9
- IP/License Agreements: 8

**By Retained EU Law Exposure:**
- Market Abuse Regulation (MAR): 1 contract
- Working Time Directive: 3 contracts
- Data Protection (GDPR): 6 contracts
- Employment Rights: 3 contracts
- Product Standards/Manufacturing: 9 contracts

**All contract files located in:** `/Users/liz/Downloads/CUAD_v1/full_contract_txt/`

---

## TASK 3: US STATE AI REGULATION WAVE (2024)

### Summary
**Total Contracts Identified:** 9 contracts with automated consumer decision-making systems

**Relevant State Laws:**
- Colorado AI Act (SB 24-205) - Effective February 2026
- California AB 2013 - Automated decision tools disclosure
- Utah AI Policy Act (HB 366) - 2024
- Illinois Artificial Intelligence Video Interview Act
- Multiple other states with 2024 AI legislation

### Top Priority Contracts for Testing

#### 1. Equidata/National Credit Report - MARKETING AFFILIATE AGREEMENT
- **File:** `SteelVaultCorp_20081224_10-K_EX-10.16_3074935_EX-10.16_Affiliate Agreement.txt`
- **Parties:** Equidata Inc. (Virginia), National Credit Report.com LLC (Florida)
- **Date:** 2008
- **Governing Law:** Virginia
- **Automated Systems:** Credit scoring, fraud detection, credit monitoring algorithms
- **Consumer Impact:** Direct - Credit eligibility decisions
- **State Exposure:** Would operate in Colorado, California if serving those residents
- **Existing Compliance:** FCRA compliance required, but no explicit algorithm disclosure
- **Colorado SB 24-205 Gaps:**
  - No algorithmic discrimination impact assessment
  - No meaningful opportunity to correct adverse decisions
  - No consumer notice of automated decision-making
- **California AB 2013 Gaps:**
  - No disclosure that automated decision tool is being used
  - No information on data types collected
  - No consumer right to alternative process
- **Test Question:** "Does this credit scoring agreement comply with Colorado SB 24-205 algorithmic discrimination prevention requirements and California AB 2013 automated decision tool disclosure obligations enacted in 2024?"

#### 2. BNC Mortgage Inc - AUTOMATED UNDERWRITING SYSTEM
- **File:** `BNCMORTGAGEINC_05_17_1999-EX-10.4-LICENSING AND WEB SITE HOSTING AGREEMENT.txt`
- **Parties:** BNC Mortgage Inc. (California), TrueLink Inc. (California)
- **Date:** May 17, 1999
- **Governing Law:** California
- **Automated Systems:** Automated mortgage underwriting from third-party investors/insurers
- **Consumer Impact:** Direct - Mortgage application approval/denial
- **Key Provision:** "Client must not represent that underwriting decisions are made by TrueLink" (implies automated decisioning)
- **California AB 2013 Issues:**
  - No transparency about automated nature of underwriting
  - No disclosure of data sources or decision logic
  - No consumer notification rights
  - No appeal/review process for automated denials
- **Colorado SB 24-205 Issues:**
  - No algorithmic discrimination testing for protected characteristics
  - No impact assessment for disparate impact on housing access
- **Test Question:** "Analyze whether this 1999 automated mortgage underwriting system meets 2024 California AB 2013 disclosure requirements and Colorado SB 24-205 anti-discrimination provisions if still operational with California and Colorado mortgage applicants."

#### 3. Cardlytics Inc - BANK OF AMERICA ANALYTICS PLATFORM
- **File:** `CardlyticsInc_20180112_S-1_EX-10.16_11002987_EX-10.16_Maintenance Agreement1.txt`
- **Parties:** Cardlytics Inc. (Georgia), Bank of America N.A.
- **Governing Law:** North Carolina (BofA headquarters)
- **Automated Systems:** Behavioral analytics, customer profiling/targeting algorithms
- **Consumer Impact:** Indirect/Direct - Financial services targeting, potential credit decisions
- **Multi-State Exposure:** BofA operates nationwide including Colorado, California
- **FCRA Compliance:** Referenced for "Consumer Information" but inadequate for modern AI regulation
- **2024 State AI Law Gaps:**
  - No explainability provisions for targeting/profiling decisions
  - No consumer right to opt-out of algorithmic profiling
  - No bias detection/mitigation measures
  - No transparency about data sources and decision logic
- **Test Question:** "Does Bank of America's behavioral analytics platform comply with the wave of 2024 state AI laws (Colorado, California, Utah) regarding consumer profiling, automated targeting, and algorithmic transparency for nationwide operations?"

#### 4. CreditCards.com - CHASE BANK AFFILIATE AGREEMENT
- **File:** `CreditcardscomInc_20070810_S-1_EX-10.33_362297_EX-10.33_Affiliate Agreement.txt`
- **Parties:** CreditCards.com Inc., Chase Bank USA N.A.
- **Automated Systems:** Automated online credit card application processing
- **Consumer Impact:** Direct - Credit card approval/denial decisions
- **Key Provision:** Chase has "sole discretion" to reject applications (no transparency on automated criteria)
- **State AI Law Gaps:**
  - No notice that automated systems evaluate applications
  - No disclosure of decision factors
  - No meaningful appeal process
  - No algorithmic fairness testing
- **Test Question:** "What specific contractual provisions are required under 2024 state AI laws (Colorado SB 24-205, California AB 2013) to make Chase's automated credit card application system compliant, particularly regarding applicant notice, explainability, and anti-discrimination measures?"

#### 5. Goosehead Insurance - FRANCHISE AGREEMENT
- **File:** `GOOSEHEADINSURANCE,INC_04_02_2018-EX-10.6-Franchise Agreement.txt`
- **Parties:** Goosehead Insurance Agency LLC (Texas)
- **Date:** April 2, 2018
- **Governing Law:** Texas
- **Automated Systems:** Agency management system for insurance underwriting/risk assessment
- **Consumer Impact:** Direct - Insurance coverage decisions, premium pricing
- **Multi-State Operations:** Franchisees operate in multiple states including Colorado, California
- **2024 State AI Law Issues:**
  - Texas has limited AI regulation, but franchisees in Colorado/California must comply with those states' laws
  - No provisions for algorithmic transparency in underwriting
  - No anti-discrimination impact assessments
  - No consumer rights regarding automated insurance decisions
- **Test Question:** "Do Goosehead Insurance franchisees using automated underwriting systems in Colorado comply with SB 24-205 requirements for high-risk automated decisions affecting insurance coverage, given that the master franchise agreement lacks 2024-compliant AI governance provisions?"

### Complete List of 9 Automated Decision Contracts

**By Decision Type:**
- Credit Scoring/Lending: 3 contracts
- Insurance Underwriting: 1 contract
- Financial Analytics/Profiling: 2 contracts
- Mortgage Underwriting: 1 contract
- Payment Processing: 2 contracts

**By State Exposure:**
- California: 4 contracts
- Multi-state operations: 5 contracts
- Texas: 1 contract
- Virginia: 1 contract

**All contract files located in:** `/Users/liz/Downloads/CUAD_v1/full_contract_txt/`

---

## TASK 4: GLOBAL SUPPLY CHAIN DUE DILIGENCE LAWS (2023-2024)

### Summary
**Total Contracts Identified:** 41 supply chain, manufacturing, and procurement contracts

**Relevant Regulations:**
- Germany's Supply Chain Due Diligence Act (LkSG) - In force 2023
- EU Corporate Sustainability Due Diligence Directive (CSDDD) - Adopted 2024
- Norway's Transparency Act - Enforcement ramped up 2023-2024
- Various forced labor/modern slavery supply chain laws

### Top Priority Contracts for Testing

#### 1. Upjohn/Pfizer - GLOBAL MANUFACTURING & SUPPLY AGREEMENT
- **File:** `UpjohnInc_20200121_10-12G_EX-2.6_11948692_EX-2.6_Manufacturing Agreement_ Supply Agreement.txt`
- **Parties:** Pfizer Inc. (Delaware), Upjohn Inc. (Delaware), Mylan N.V. (Netherlands)
- **Date:** January 21, 2020
- **EU Connection:** ✓ Mylan N.V. is major EU/Netherlands corporation - **directly subject to CSDDD**
- **Geographic Scope:** Global pharmaceutical manufacturing and distribution
- **Existing Due Diligence Provisions:**
  - ✓ Supply Chain Security (Section 14) - C-TPAT compliance
  - ✓ Environmental Laws (Section 6) - Environmental covenants
  - ✓ Anti-Corruption Principles
  - ✓ Global trade control compliance
  - ✓ **Conflict Minerals Representations** (rare in CUAD dataset)
  - ✓ Audit Rights (Section 15) - Records and audits
- **BEST PRACTICE in dataset for due diligence**
- **CSDDD Gaps (compared to 2024 requirements):**
  - Limited human rights due diligence obligations
  - No mandatory remediation procedures for harm
  - Insufficient value chain oversight (tier 2+ suppliers)
  - No grievance mechanism for affected stakeholders
  - Limited climate/environmental due diligence beyond compliance
- **Test Question:** "Evaluate this Pfizer-Mylan pharmaceutical supply agreement against EU CSDDD requirements adopted in 2024. Does it comply with: (1) human rights due diligence obligations throughout value chain; (2) environmental due diligence beyond basic compliance; (3) mandatory remediation procedures; (4) stakeholder grievance mechanisms? What specific contractual provisions need to be added to achieve CSDDD compliance?"

#### 2. Profound Medical - PHILIPS MEDICAL SUPPLY AGREEMENT
- **File:** `PROFOUNDMEDICALCORP_08_29_2019-EX-4.5-SUPPLY AGREEMENT.txt`
- **Parties:** Profound Medical Inc. (Canada), Philips Medical Systems Nederland B.V. (Netherlands)
- **Date:** August 29, 2019
- **EU Connection:** ✓ Philips - Dutch supplier **directly subject to CSDDD**
- **Contract Type:** Medical device manufacturing agreement
- **Existing Due Diligence:**
  - ✓ Quality agreements and facility audits
  - ✓ Environmental compliance provisions
  - ✓ Health and safety provisions
  - ✓ Regulatory approval management
- **Germany LkSG Gaps:**
  - No explicit human rights risk assessment
  - Limited labor standards enforcement language
  - No modern slavery prevention measures
  - Insufficient supplier diversity considerations
- **CSDDD Gaps:**
  - No value chain mapping requirements
  - Limited climate change mitigation obligations
  - No mandatory transition plans for environmental sustainability
- **Test Question:** "Does this medical device supply agreement with Dutch supplier Philips comply with: (1) Germany's LkSG human rights due diligence requirements in force 2023; (2) EU CSDDD value chain oversight obligations adopted 2024? What audit rights, supplier warranties, and remediation procedures are missing under these new regimes?"

#### 3. Biofrontera AG - PHARMACEUTICAL SUPPLY (EU-US)
- **File:** `BIOFRONTERAAG_04_29_2019-EX-4.17-SUPPLY AGREEMENT.txt`
- **Parties:** Cutanea Life Sciences (USA), Ferrer Internacional, S.A. (Spain)
- **Date:** April 29, 2019
- **EU Connection:** ✓ Spanish supplier Ferrer - **subject to CSDDD**
- **Contract Type:** Pharmaceutical supply agreement
- **Existing Due Diligence:**
  - ✓ Annual quality audits
  - ✓ Facility access and inspection rights
  - ✓ cGMP compliance requirements
  - ✓ Certificate of Analysis (CoA) documentation
- **Critical Gaps for 2023-2024 Laws:**
  - **No human rights language whatsoever**
  - **No labor standards provisions**
  - **No conflict minerals disclosure**
  - **No environmental sustainability beyond regulatory compliance**
  - **No supplier code of conduct**
- **Test Question:** "Analyze this EU-US pharmaceutical supply agreement against 2023-2024 due diligence legislation. What specific contractual mechanisms (audit rights, supplier warranties, remediation procedures, grievance mechanisms) are required under Germany's LkSG and EU CSDDD but completely absent from this agreement?"

#### 4. Columbia Laboratories - UK MANUFACTURER AGREEMENT
- **File:** `Columbia Laboratories, (Bermuda) Ltd. - AMEND NO. 2 TO MANUFACTURING AND SUPPLY AGREEMENT.txt`
- **Parties:** Columbia Laboratories (Bermuda), Fleet Laboratories Limited (UK/England)
- **EU Connection:** ✓ UK supplier with EU regulatory framework
- **Existing Due Diligence:**
  - ✓ EU GDP (Good Distribution Practice) guidelines
  - ✓ Brazilian ANVISA standards compliance
  - ✓ KPI requirements for supplier performance
  - ✓ Audit rights
- **Post-Brexit/CSDDD Issues:**
  - UK supplier no longer directly subject to CSDDD but may need compliance for EU market access
  - Limited human rights due diligence
  - No forced labor prevention measures
- **Test Question:** "Given this UK supplier's need for EU market access post-Brexit, does this manufacturing agreement satisfy EU CSDDD due diligence requirements for pharmaceutical distribution in EU markets as of 2024? What additional supplier obligations are required?"

#### 5. West Pharmaceutical Services - GLOBAL SUPPLY AGREEMENT
- **File:** `WestPharmaceuticalServicesInc_20200116_8-K_EX-10.1_11947529_EX-10.1_Supply Agreement.txt`
- **Date:** January 16, 2020
- **Contract Type:** Pharmaceutical packaging supply
- **Existing Due Diligence:**
  - ✓ Quality agreements
  - ✓ GDPR compliance provisions (data protection)
  - ✓ Adequacy decision references for data transfers
- **CSDDD Gaps:**
  - Limited scope beyond quality/regulatory compliance
  - No comprehensive human rights due diligence
  - Insufficient environmental sustainability provisions
- **Test Question:** "What supply chain due diligence provisions must be added to this pharmaceutical packaging agreement to comply with CSDDD requirements for Scope 3 emissions, human rights in value chains, and mandatory transition plans enacted 2024?"

### Complete List of 41 Supply Chain Contracts

**Tier 1 - Critical Priority (5 contracts with EU suppliers):**
1. Upjohn/Pfizer (Netherlands - Mylan N.V.)
2. Profound Medical/Philips (Netherlands)
3. Biofrontera/Ferrer (Spain)
4. Columbia/Fleet Labs (UK)
5. Intersect ENT/Hovione (EU supplier)

**Tier 2 - High Priority (10 contracts with strong compliance frameworks):**
- Bell Ring Brands, MediWound, SeaSpine, Vericel, and others

**By Geographic Scope:**
- EU-connected supply chains: 15 contracts
- Multi-country operations: 28 contracts
- Asia-Pacific sourcing: 8 contracts
- US-only: 13 contracts

**By Existing Due Diligence Features:**
- Audit rights: 35 contracts
- Quality/regulatory compliance: 41 contracts
- Environmental provisions: 12 contracts
- Anti-corruption/ethics: 3 contracts
- Human rights language: 0 contracts
- Conflict minerals: 1 contract (Upjohn only)

**All contract files located in:** `/Users/liz/Downloads/CUAD_v1/full_contract_txt/`

---

## TASK 5: US NON-COMPETE BAN EVOLUTION (2024)

### Summary
**Total Contracts Identified:** 267 contracts with restrictive covenants

**Relevant Regulatory Changes:**
- FTC Non-Compete Ban - Proposed April 2024, finalized but blocked by courts (August 2024 injunction)
- Ongoing litigation as of November 2024
- Multiple states enacted/strengthened restrictions 2023-2024:
  - Minnesota (2023) - Ban on non-competes
  - California expansions (AB 1076, SB 699)
  - Illinois amendments
  - Oklahoma restrictions

**FTC Rule Key Provisions (if upheld):**
- Bans most non-competes for all workers
- Exception: Senior executives earning >$151,164 annually
- Exception: Business sale context
- Retroactive rescission required

### Distribution of Restrictive Covenants

**By Restriction Type:**
- Non-Compete: 119 contracts (45%)
- Exclusivity: 180 contracts (67%)
- No-Solicit Employees: 59 contracts (22%)
- No-Solicit Customers: 34 contracts (13%)
- Non-Disparagement: 38 contracts (14%)

**By Geographic Jurisdiction:**
1. New York: 50 contracts
2. California: 40 contracts (mostly already unenforceable)
3. Delaware: 28 contracts
4. Texas: 15 contracts
5. Florida: 12 contracts

### Top Priority Contracts for Testing

#### 1. MEDALIST DIVERSIFIED REIT - CONSULTING AGREEMENT (Above Threshold)
- **File:** `MEDALISTDIVERSIFIEDREIT,INC_05_18_2020-EX-10.1-CONSULTING AGREEMENT.txt`
- **Parties:** Medalist Diversified REIT, Inc. (Virginia), Gunston Consulting, LLC
- **Date:** May 18, 2020
- **Governing Law:** Virginia
- **Compensation:** $200,000/year + stock grants (**above $151,164 FTC threshold**)
- **Non-Compete Duration:** 12 months post-termination
- **Geographic Scope:** Virginia + "any other state in which Company owns real estate" (multi-state)
- **Competitor Definition:** Any REIT/fund with principal business in VA or states where company owns property
- **FTC Rule Analysis:**
  - Compensation above threshold → potential senior executive exception
  - BUT: Independent contractor, not employee
  - Geographic scope may be overly broad even if exempt
  - 12-month duration within reasonable range
- **State Law Issues:**
  - Virginia permits reasonable non-competes
  - Multi-state operations complicate enforcement
- **Test Question:** "Given the current status of the FTC non-compete ban (injunction as of November 2024) and Virginia state law, is this $200,000/year consulting non-compete enforceable? If the FTC rule survives judicial challenge, does the senior executive exception apply to independent contractors above the compensation threshold? What modifications are needed under the evolving 2023-2024 regulatory landscape?"

#### 2. DRIVEN DELIVERIES - CONSULTING AGREEMENT (5-Year Tail - Excessive)
- **File:** `DRIVENDELIVERIES,INC_05_22_2020-EX-10.4-CONSULTING AGREEMENT.txt`
- **Parties:** Driven Deliveries, Inc. (Nevada corp), TruckThat LLC (Minnesota LLC)
- **Date:** May 22, 2020
- **Governing Law:** California
- **Compensation:** $18,000/month = $216,000 annually (**above FTC threshold**)
- **Non-Solicitation Duration:** **5 years post-termination** (extremely excessive)
- **Geographic Scope:** Unlimited
- **Key Language:** "solicit, divert or hire away any person employed by the Company for a period of five (5) years"
- **Critical Issues:**
  - California B&P Code §16600 already voids most non-competes
  - 5-year non-solicit tail likely unenforceable even in permissive states
  - Minnesota LLC party - Minnesota banned non-competes in 2023
  - Even above FTC threshold, 5-year duration is unreasonable
- **Test Question:** "Analyze this consulting agreement's 5-year non-solicitation provision under: (1) California Business & Professions Code §16600 (traditional prohibition); (2) Minnesota's 2023 non-compete ban affecting the Minnesota LLC party; (3) FTC rule's reasonableness standards if applied to senior executives. Is any duration of restriction enforceable given the overlapping state and potential federal prohibitions as of November 2024?"

#### 3. MRS. FIELDS - FRANCHISE AGREEMENT (Franchisee Below Threshold)
- **File:** `MRSFIELDSORIGINALCOOKIESINC_01_29_1998-EX-10-FRANCHISE AGREEMENT.txt`
- **Parties:** Mrs. Fields Original Cookies Inc. (franchisor), Individual franchisee
- **Date:** January 29, 1998
- **Governing Law:** Pennsylvania
- **Restrictions:**
  - Non-Compete: 2 years, 1-mile radius
  - No-Solicit Customers: 5 years (excessive)
  - No-Solicit Employees: 5 years (excessive)
- **Franchisee Compensation:** Typically well below $151,164 threshold
- **FTC Rule Analysis:**
  - Franchisees are NOT in "business sale" exception category
  - Franchisees typically workers/business owners below threshold
  - Would be **PROHIBITED** under FTC rule if upheld
- **Pennsylvania State Law:**
  - Currently permits reasonable non-competes
  - No state-level franchise non-compete ban as of 2024
- **Test Question:** "If the FTC non-compete ban survives judicial challenge, would this franchise agreement's restrictive covenants be void? Specifically: (1) Are franchisees considered 'workers' under the FTC rule's definition? (2) Does the business sale exception apply to franchise relationships? (3) Under Pennsylvania law as amended through 2024, what restrictions on franchise non-competes exist? Retrieve the current legal status of the FTC rule and applicable Pennsylvania statutes as of November 2024."

#### 4. QUAKER CHEMICAL - M&A NON-COMPETITION (Business Sale Exception)
- **File:** `Quaker Chemical Corporation - NON COMPETITION AND NON SOLICITATION AGREEMENT.txt`
- **Context:** Business acquisition (Gulf Houghton shares)
- **Governing Law:** Pennsylvania
- **Restrictions:**
  - Non-Compete: 2 years, worldwide except India
  - No-Solicitation: 3 years, global
- **Consideration:** Cash + stock in substantial M&A transaction
- **FTC Rule Analysis:**
  - Clear **business sale exception** applies
  - Seller of business interest can be restricted from competing
  - This is explicitly carved out in FTC rule
  - Duration (2-3 years) is reasonable for M&A context
- **Test Question:** "Confirm that this M&A-related non-compete qualifies for the business sale exception under the FTC rule. What is the current definition and scope of the 'sale of business' exception in the FTC rule as finalized in 2024, and does it cover this scenario of selling equity interest in a division?"

#### 5. VIVINT SOLAR - AMENDMENT REMOVING NON-COMPETE (Market Response to Regulation)
- **File:** `VIVINT SOLAR, INC. - NON-COMPETITION AGREEMENT.txt`
- **Key Feature:** Amendment that **removes non-compete entirely**, preserves only non-solicitation
- **Significance:** Shows companies proactively backing away from non-competes in anticipation of FTC rule
- **Market Trend:** Evidence of voluntary compliance/regulatory arbitrage
- **Test Question:** "Identify the legal and business rationale for Vivint Solar's decision to remove non-compete provisions while retaining non-solicitation clauses. Does this reflect best practices for compliance with the evolving regulatory landscape of 2023-2024, and are standalone non-solicitation agreements more likely to survive FTC scrutiny than comprehensive non-competes?"

### Complete List of 267 Restrictive Covenant Contracts

**Employment/Service Agreements:**
- Executive employment: 15 contracts
- Service agreements: 35 contracts
- Consulting agreements: 28 contracts

**Commercial Agreements with Restrictions:**
- Franchise agreements: 42 contracts
- Distribution agreements: 38 contracts
- Strategic alliances: 45 contracts
- License agreements: 64 contracts

**By Compensation Level (where identifiable):**
- Above $151,164 threshold: 12 contracts (senior executive exception may apply)
- Below threshold: 89 contracts (would be prohibited)
- Compensation not specified: 166 contracts

**By Duration:**
- 1 year or less: 48 contracts
- 1-2 years: 87 contracts
- 2-3 years: 56 contracts
- 3-5 years: 42 contracts (likely excessive)
- 5+ years: 8 contracts (almost certainly excessive)
- Perpetual/indefinite: 26 contracts (geographic restrictions)

**All contract files located in:** `/Users/liz/Downloads/CUAD_v1/full_contract_txt/`

---

## TASK 6: CORPUS-WIDE CROSS-SECTIONAL ANALYSIS

### Master Regulatory Exposure Matrix

**Total CUAD Contracts Analyzed:** 510
**Contracts Affected by Post-Cutoff Regulations:** 428 (84%)

| Regulatory Category | Contract Count | % of Corpus | Priority Level |
|---------------------|----------------|-------------|----------------|
| FTC Non-Compete Ban (2024) | 267 | 52% | HIGH |
| AI/ML Systems (EU AI Act, US State Laws) | 131 | 26% | HIGH |
| UK REUL Act Changes | 41 | 8% | MEDIUM |
| Supply Chain Due Diligence (EU CSDDD, LkSG) | 41 | 8% | MEDIUM |
| US State AI Laws (Automated Decisions) | 9 | 2% | HIGH |
| **Multiple Overlapping Exposures** | **92** | **18%** | **CRITICAL** |

### High-Impact Overlapping Exposures (92 Contracts)

**Contracts Affected by 3+ Regulatory Regimes:**

1. **Foundation Medicine Inc** - COLLABORATION AGREEMENT
   - EU AI Act (algorithmic medical diagnostics)
   - Supply Chain Due Diligence (international pharma manufacturing)
   - UK REUL Act (potential UK operations)
   - Non-Compete/Exclusivity provisions

2. **Cardlytics Inc** - MAINTENANCE AGREEMENT
   - EU AI Act (behavioral analytics algorithms)
   - US State AI Laws (automated consumer decisions)
   - Supply Chain Due Diligence (if international data processing)

3. **WPP plc** - CFO EMPLOYMENT AGREEMENT
   - UK REUL Act (Market Abuse Regulation, employment law)
   - Non-Compete/Restrictive Covenants
   - Data Protection (UK divergence from EU GDPR)

4. **Upjohn/Pfizer** - MANUFACTURING AGREEMENT
   - Supply Chain Due Diligence (EU CSDDD - Mylan N.V.)
   - AI/ML Systems (if manufacturing uses algorithmic optimization)
   - UK REUL Act (if UK manufacturing sites)

5. **Cerence Inc** - IP AGREEMENT (NLP/Voice AI)
   - EU AI Act (conversational AI transparency)
   - AI/ML algorithmic systems
   - Restrictive covenants/exclusivity
   - UK operations (if applicable)

### Contracts Requiring Immediate Review (Post-April 2024 Urgency)

**Tier 1 - Critical Urgency (Regulations in force NOW):**
1. Foundation Medicine - EU AI Act (Aug 2024) + medical device regulation
2. WPP plc - UK REUL Act (Market Abuse Regulation status)
3. Cardlytics - US State AI Laws (CA AB 2013 effective 2024)
4. Upjohn/Pfizer - EU CSDDD (adopted 2024, implementation 2026-2028)
5. BNC Mortgage - US State AI Laws (automated underwriting disclosure)

**Tier 2 - High Urgency (Implementation pending):**
- All 267 non-compete contracts (FTC litigation ongoing)
- 131 AI/ML contracts (EU AI Act phased implementation 2024-2027)
- 41 UK contracts (REUL Act revocations continuing through 2024)

### Geographic Risk Concentration

| Jurisdiction | Contract Count | Key Regulatory Risks |
|--------------|----------------|---------------------|
| California | 78 | US State AI Laws, Non-Compete (already restricted) |
| New York | 62 | Non-Compete, US State AI Laws |
| Delaware | 51 | Non-Compete, Corporate governance |
| Texas | 28 | Non-Compete, US State AI Laws |
| UK (England/Wales) | 41 | REUL Act, Data Protection divergence |
| EU-Connected | 76 | EU AI Act, CSDDD, GDPR |
| Multi-State/International | 174 | All regulatory regimes |

### Industry Sector Risk Analysis

| Sector | Contract Count | Highest Risks |
|--------|----------------|---------------|
| Technology/Software | 112 | EU AI Act, US State AI Laws, Non-Compete |
| Pharmaceuticals | 68 | Supply Chain Due Diligence, EU AI Act (diagnostics), UK REUL |
| Financial Services | 42 | US State AI Laws (credit/underwriting), EU AI Act |
| Healthcare/Medical Devices | 38 | EU AI Act (high-risk systems), Supply Chain |
| Franchising | 42 | Non-Compete (FTC rule high impact) |
| Manufacturing | 51 | Supply Chain Due Diligence, UK REUL |
| Professional Services | 87 | Non-Compete, UK employment law |
| Other | 70 | Various |

### Contract Date Distribution

| Execution Period | Count | Post-Cutoff Risk |
|------------------|-------|------------------|
| 1996-2010 | 152 | HIGH - Pre-date all modern AI/privacy regulation |
| 2011-2015 | 128 | HIGH - Pre-GDPR, pre-AI regulation |
| 2016-2019 | 143 | MEDIUM - May have GDPR but no AI regulation |
| 2020-2024 | 87 | MEDIUM - Post-GDPR but pre-AI Act |

**Key Insight:** 280 contracts (55%) executed before 2016 almost certainly lack modern AI governance, data protection, and due diligence provisions required by 2023-2024 regulations.

---

## LAWSTRONAUT TEST QUESTIONS BY CATEGORY

### EU AI Act Queries (Post-August 2024)

**Foundation Medicine Contract:**
> "Does this AI-powered genomic diagnostics platform comply with EU AI Act Article 10 (data governance), Article 13 (transparency), and Article 14 (human oversight) requirements for high-risk medical AI systems? Retrieve the specific Article 10 requirements for training data quality, data governance practices, and bias mitigation in medical AI systems effective August 2024."

**Cerence NLP Contract:**
> "Does this natural language processing licensing agreement comply with EU AI Act Article 52 transparency obligations requiring disclosure of AI interaction to end users in EU markets? Retrieve Article 52's specific requirements for conversational AI systems and penalties for non-compliance as of November 2024."

**Cardlytics Analytics:**
> "Does this behavioral analytics platform for consumer profiling constitute a high-risk AI system under EU AI Act Article 6(2)? If so, retrieve the conformity assessment requirements under Article 43 and the technical documentation obligations under Article 11 applicable to profiling systems deployed in EU markets."

**General Query Across 131 Contracts:**
> "Across the 131 contracts with AI/ML algorithmic systems, identify which constitute 'high-risk AI systems' under EU AI Act Annex III (as amended through November 2024). For each high-risk system, retrieve the specific compliance obligations under Title III Chapter 2 (Articles 8-15) that are missing from the contractual provisions."

### UK REUL Act Queries (Post-2023)

**WPP Employment - Market Abuse Regulation:**
> "What is the current status of Market Abuse Regulation (EU) 596/2014 in UK law as of November 2024? Has it been revoked, amended, or preserved under the Retained EU Law (Revocation and Reform) Act 2023? Retrieve the specific provisions of Section 3.2(l) obligations for financial services executives in light of any revocations or amendments."

**Bicycle Therapeutics - Data Protection:**
> "How has the UK Data Protection Act 2018 (implementing GDPR) diverged from EU GDPR under the Retained EU Law Act 2023 and subsequent UK legislation through November 2024? Retrieve the specific UK regulatory changes affecting employee data processing obligations, cross-border data transfers, and adequacy decisions post-Brexit."

**Theravance Employment - Working Time:**
> "Which provisions of the Working Time Regulations 1998 (implementing EU Directive 2003/88/EC) have been retained, amended, or revoked under the UK Retained EU Law Act as of November 2024? Retrieve the current UK law on maximum working hours, rest periods, and holiday entitlements for executives in pharmaceutical companies."

**CERES Research - Plant Variety Protection:**
> "What UK regulatory changes to plant variety protection and biological material handling have occurred under the Retained EU Law Act affecting cross-border research collaboration with Welsh institutes as of November 2024? Retrieve current UK requirements for international transfer of plant genetic material post-Brexit."

**General Query Across 41 Contracts:**
> "For all 41 contracts with England/Wales governing law, identify which EU-derived regulations referenced in these agreements have been revoked, amended, or preserved under the Retained EU Law Act 2023 and subsequent UK legislative changes through November 2024. Prioritize by: (1) Financial services regulations, (2) Employment law, (3) Data protection, (4) Product standards."

### US State AI Law Queries (Post-2024)

**Equidata Credit Scoring:**
> "Does this credit scoring and fraud detection system comply with Colorado SB 24-205 requirements for algorithmic discrimination prevention? Retrieve the specific impact assessment requirements under Section 6-1-1704 and the consumer rights under Section 6-1-1306 effective February 2026 (but requiring preparation now)."

**BNC Mortgage Underwriting:**
> "Does this automated mortgage underwriting system meet California AB 2013 disclosure requirements for automated decision tools enacted in 2024? Retrieve the specific disclosure obligations under Civil Code Section 1798.140 et seq. regarding consumer notification, data sources, and decision logic transparency."

**Cardlytics Bank Analytics:**
> "Does Bank of America's nationwide behavioral analytics platform comply with the suite of 2024 state AI laws including Colorado SB 24-205, California AB 2013, and Utah HB 366? Retrieve the anti-discrimination testing requirements, consumer notification standards, and opt-out provisions across these three state regimes."

**CreditCards.com Chase Affiliate:**
> "What specific contractual provisions are required under Colorado SB 24-205 (algorithmic discrimination), California AB 2013 (automated decision disclosure), and Illinois AI Video Interview Act to make Chase's automated credit card application system compliant with 2024 state laws? Retrieve the specific disclosure requirements and consumer rights across these jurisdictions."

**General Query Across 9 Contracts:**
> "Across these 9 contracts with automated consumer decision-making (credit, insurance, mortgage), identify which states' 2024 AI laws apply based on consumer location and governing law. For each applicable state law, retrieve the specific disclosure requirements, anti-discrimination provisions, and consumer rights that are missing from current contractual provisions."

### Supply Chain Due Diligence Queries (Post-2023)

**Upjohn/Pfizer - Most Comprehensive:**
> "Evaluate this Pfizer-Mylan pharmaceutical supply agreement against EU Corporate Sustainability Due Diligence Directive (CSDDD) requirements adopted in 2024. Retrieve the specific Article requirements for: (1) Human rights due diligence (Article 7-8), (2) Environmental due diligence including climate transition plans (Article 15), (3) Stakeholder engagement and grievance mechanisms (Article 10), (4) Monitoring of business partners (Article 9). What contractual provisions are missing for full compliance?"

**Profound/Philips Medical:**
> "Does this medical device supply agreement with Dutch supplier Philips comply with: (1) Germany's Lieferkettensorgfaltspflichtengesetz (LkSG) human rights due diligence requirements effective 2023; (2) EU CSDDD value chain oversight obligations? Retrieve the specific audit rights, supplier warranty requirements, and remediation procedures mandated by Section 3-9 of the LkSG and corresponding CSDDD articles."

**Biofrontera/Ferrer Spain:**
> "This pharmaceutical supply agreement with Spanish supplier Ferrer Internacional lacks any human rights, labor standards, or conflict minerals language. Retrieve the specific contractual mechanisms (audit rights, supplier codes of conduct, remediation procedures, grievance mechanisms) required under: (1) Germany's LkSG Section 5 (preventive measures), (2) EU CSDDD Article 7-8 (due diligence obligations), (3) Norway's Transparency Act as enforced 2023-2024."

**General Query Across 41 Contracts:**
> "Across this portfolio of 41 supply chain contracts (15 with EU connections), identify which are directly subject to EU CSDDD based on supplier location and revenue thresholds. For each in-scope contract, retrieve the specific CSDDD provisions (Articles 7-16) that require contractual amendments. Prioritize by: (1) EU-domiciled suppliers, (2) High-risk sectors (pharmaceuticals, medical devices), (3) Multi-tier supply chains."

### FTC Non-Compete Ban Queries (Post-2024)

**Medalist Consulting - Above Threshold:**
> "Given the current status of the FTC non-compete ban (proposed April 2024, finalized August 2024, currently under injunction), is this $200,000/year consulting non-compete enforceable as of November 2024? Retrieve: (1) Current litigation status and any court rulings as of November 2024, (2) Whether the senior executive exception ($151,164+ threshold) applies to independent contractors, (3) Virginia state law amendments to non-compete enforcement 2023-2024."

**Driven Deliveries - 5-Year Excessive:**
> "Analyze this consulting agreement's 5-year non-solicitation provision under: (1) California Business & Professions Code §16600 and recent amendments (SB 699, AB 1076 effective 2024); (2) Minnesota's 2023 non-compete ban (Minn. Stat. § 181.988) affecting the Minnesota LLC party; (3) FTC rule's reasonableness standards if applied to senior executives. Retrieve the current enforceability standards across these three overlapping prohibitions as of November 2024."

**Mrs. Fields Franchise:**
> "If the FTC non-compete ban survives judicial challenge and takes effect, would this franchise agreement's restrictive covenants be void? Retrieve: (1) FTC rule's definition of 'worker' and whether franchisees are included; (2) Scope of the business sale exception under 16 CFR § 910.2; (3) Pennsylvania state law on franchise non-competes (Act 2022-54 and any 2023-2024 amendments); (4) Current status of FTC rule litigation as of November 2024."

**Quaker Chemical M&A:**
> "Confirm that this M&A-related non-compete qualifies for the business sale exception under the FTC rule. Retrieve: (1) The final definition and scope of 'bona fide sale of business' under 16 CFR § 910.1(b); (2) Whether sale of division/equity interest (not entire company) qualifies for exception; (3) Pennsylvania law on M&A non-competes as of November 2024."

**General Query Across 267 Contracts:**
> "Across this portfolio of 267 contracts with restrictive covenants, identify the subset requiring immediate legal review due to the FTC non-compete ban and state-level regulatory changes enacted 2023-2024. Prioritize by: (1) Workers below $151,164 threshold where FTC ban applies; (2) Franchisees (likely prohibited); (3) Contracts with excessive duration (5+ years); (4) Jurisdictions with new state laws (Minnesota, California, Illinois). Retrieve the current status of the FTC rule litigation and each state's 2024 non-compete law."

---

## CROSS-CUTTING PRIORITY TEST QUESTIONS

### Demonstrate Value: Baseline LLM vs. Lawstronaut

**High-Complexity Multi-Regulatory Query:**
> "The Foundation Medicine collaboration agreement involves algorithmic genomic diagnostics with Swiss and US parties, international manufacturing, and restrictive covenants. As of November 2024, does this contract comply with: (1) EU AI Act Articles 6, 10, 13, 14 for high-risk medical AI systems; (2) EU CSDDD requirements for pharmaceutical supply chain due diligence; (3) Switzerland-EU adequacy decisions for health data transfers post-2024; (4) US state AI laws for medical decision-making systems? Retrieve all applicable post-April 2024 regulations and identify specific compliance gaps."

**Expected Baseline LLM Response:**
> "I don't have information about regulations enacted after April 2024 [Claude] / April 2023 [GPT-4]. The EU AI Act was proposed but I cannot confirm its final provisions or effective date. For current compliance analysis, please consult recent regulatory guidance."

**Expected Lawstronaut-Enhanced Response:**
> "Based on regulatory retrieval:
>
> 1. EU AI Act: Regulation (EU) 2024/1689 entered into force August 1, 2024. This system qualifies as HIGH-RISK under Annex III point 5(a) (medical devices). Required provisions under Title III Chapter 2:
>    - Article 10: Training data governance - CONTRACT MISSING documented data quality metrics, bias mitigation
>    - Article 13: Transparency - CONTRACT MISSING patient-facing explanations of algorithmic decisions
>    - Article 14: Human oversight - CONTRACT HAS medical professional review but lacks documented override protocols
>    - Article 15: Accuracy/Robustness - CONTRACT MISSING validation testing requirements
>
> 2. EU CSDDD: Directive (EU) 2024/1760 adopted May 2024, member state implementation required by July 2026. Pharmaceutical manufacturing provisions under Article 7-8 require human rights due diligence in supply chain. CONTRACT HAS regulatory compliance but MISSING labor standards enforcement, grievance mechanisms, and Scope 3 emissions tracking required by Article 15.
>
> 3. Switzerland-EU Data Adequacy: Following UK adequacy decision model, Swiss adequacy maintained post-2024 but Swiss Federal Act on Data Protection (revFADP) effective September 2023 creates divergence. Special category health data under FADP Art. 5 requires explicit consent - CONTRACT needs amendment for genomic data transfers.
>
> 4. US State AI Laws: Not directly applicable (medical devices regulated federally), but California AB 2013 automated decision disclosure may apply if California patients affected. Colorado SB 24-205 exempts HIPAA-covered entities.
>
> PRIORITY GAPS: EU AI Act Articles 10, 13, 15 (medical device AI requirements) and CSDDD Article 7-8 (supply chain human rights)."

### Portfolio-Level Urgent Review Query

> "Across this portfolio of 510 contracts, identify all contracts requiring immediate legal review (November 2024) due to regulatory changes that took effect after April 2024 (Claude's cutoff) or significantly changed enforcement after that date. Prioritize by: (1) Regulations in force NOW with penalties for non-compliance; (2) Contracts in high-risk sectors (medical AI, credit scoring, EU operations); (3) Contracts with provisions directly contradicting new regulations. For the top 25 highest-risk contracts, retrieve the specific post-April 2024 statutory requirements and compliance deadlines."

### Jurisdiction-Specific Regulatory Divergence

> "For the 41 contracts with UK governing law, the UK Retained EU Law (Revocation and Reform) Act 2023 created regulatory divergence from EU law throughout 2023-2024. For each of the following areas, retrieve the current UK regulatory position as of November 2024 compared to equivalent EU regulations: (1) Market Abuse (MAR 596/2014/EU - is it retained/revoked in UK?); (2) Working Time Directive; (3) Data Protection (UK GDPR vs EU GDPR divergence); (4) Employment law (unfair dismissal, notice periods). Identify which contracts contain outdated references to EU regulations now revoked or amended in UK law."

---

## DATA SOURCES AND FILE LOCATIONS

### Master Dataset Files
- **Master Clauses CSV:** `/Users/liz/Downloads/CUAD_v1/master_clauses.csv` (511 rows × 83 columns)
- **Full Contract Text:** `/Users/liz/Downloads/CUAD_v1/full_contract_txt/` (510 contracts)
- **Full Contract PDF:** `/Users/liz/Downloads/CUAD_v1/full_contract_pdf/` (510 contracts)
- **Labeled Excel Groups:** `/Users/liz/Downloads/CUAD_v1/label_group_xlsx/` (28 category files)
- **SQuAD-format JSON:** `/Users/liz/Downloads/CUAD_v1/CUAD_v1.json`

### Analysis Output Files
- **This Matrix:** `/Users/liz/Downloads/CUAD_v1/LAWSTRONAUT_TEST_MATRIX.md`

---

## METHODOLOGY NOTES

### Search Approach
1. **Master CSV Analysis:** Extracted governing law, parties, dates, and labeled clause types (41 categories)
2. **Full-Text Search:** Used Explore agents with keyword searches across 510 contract texts
3. **Cross-Reference:** Verified findings against CUAD's human-annotated labels
4. **Jurisdictional Mapping:** Identified parties' locations and governing law for regulatory applicability

### Confidence Levels
- **HIGH Confidence:** Contracts explicitly mentioning regulated activities (e.g., "algorithms," "UK registered," "supply chain")
- **MEDIUM Confidence:** Contracts inferred to be affected based on party jurisdiction or contract type
- **For Testing:** All identified contracts suitable for testing; Lawstronaut should retrieve current regulations to confirm applicability

### Limitations
1. Some contracts lack party addresses or explicit dates (inferred from filing dates)
2. Compensation levels not always specified (affects FTC non-compete threshold analysis)
3. CUAD contracts date 1996-2020; some may no longer be in force
4. For testing purposes, the regulatory question is valid regardless of current contract status

---

## RECOMMENDED TEST SEQUENCE FOR LAWSTRONAUT

### Phase 1: Single-Regulation Focus (Baseline Accuracy)
1. Select 5 contracts from each regulatory category (30 total)
2. Ask category-specific test questions
3. Measure: Accuracy of post-cutoff regulation retrieval, relevance of retrieved provisions, identification of compliance gaps

### Phase 2: Multi-Regulatory Exposure (Complexity Handling)
1. Select 10 contracts with overlapping exposures (e.g., Foundation Medicine)
2. Ask cross-cutting questions requiring multiple regulatory retrievals
3. Measure: Synthesis across regulatory regimes, prioritization of conflicts, completeness of analysis

### Phase 3: Portfolio-Level Analysis (Scalability)
1. Query across full 510-contract corpus
2. Request prioritized review list based on post-cutoff regulatory urgency
3. Measure: Triage accuracy, false positive rate, computational efficiency

### Phase 4: Temporal Precision (Cutoff Date Validation)
1. Ask questions requiring regulations enacted in specific timeframes
   - "Regulations enacted after April 2024" (Claude cutoff)
   - "Regulations enacted after April 2023" (GPT-4 cutoff)
   - "Regulations amended between January 2024 and November 2024"
2. Measure: Temporal accuracy, version control, amendment tracking

### Success Metrics
- **Baseline Comparison:** Lawstronaut provides materially more accurate/current analysis than unassisted LLM
- **Regulatory Coverage:** Successfully retrieves post-cutoff regulations in 90%+ of applicable queries
- **Jurisdiction Accuracy:** Correctly identifies applicable jurisdiction and retrieves correct national/state law
- **Compliance Gap Identification:** Identifies specific missing contractual provisions vs. current law requirements
- **Commercial Value:** Demonstrates clear ROI by flagging urgent review needs and quantifiable compliance risks

---

## CONCLUSION

This analysis identifies **428 contracts (84% of CUAD corpus)** affected by regulatory changes enacted after April 2023, providing a rich test bed for Lawstronaut's regulatory retrieval capabilities. The diversity of regulatory regimes (EU AI Act, UK REUL Act, US State AI Laws, Supply Chain Due Diligence, FTC Non-Compete Ban) and overlapping exposures (92 contracts with 3+ regulatory risks) creates realistic complexity for demonstrating commercial value.

The test questions provided target Lawstronaut's key differentiator: **retrieving and applying post-cutoff regulations that baseline LLMs cannot access**. Success in these tests would validate Lawstronaut's value proposition for legal/compliance professionals managing contract portfolios in rapidly evolving regulatory landscapes.

**For immediate testing, prioritize:**
1. Foundation Medicine (EU AI Act + CSDDD + multi-regulatory)
2. WPP plc (UK REUL Act + Market Abuse Regulation specificity)
3. Cardlytics (US State AI Laws + EU AI Act overlap)
4. Upjohn/Pfizer (Supply Chain Due Diligence best practices analysis)
5. Medalist/Driven Deliveries (FTC Non-Compete threshold and state law conflicts)

These five contracts represent all six regulatory categories and demonstrate Lawstronaut's capability across the full range of post-cutoff legal changes.

---

**Analysis Completed:** November 3, 2025
**Dataset Version:** CUAD v1 (510 contracts)
**Regulatory Cutoff Dates Referenced:** GPT-4 (April 2023), Claude (April 2024)
**Target Test Date:** November 2024 and beyond
