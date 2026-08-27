# FACTS — Holt at Day 674 (reconciled against workbooks, 2026-08-27) · v1.1 post-audit
All values verified against: Day674 WB (Susan_Holt_Mandate_Day_674_Data_Model.xlsx) and Conversion WB (Susan_Holt_Mandate_Conversion_Data_Model_2026-08-26.xlsx).

## Clocks
Election 2024-10-21. Sworn in 2024-11-02. Cutoff 2026-08-26 = day 674 (election clock) = day 662 (office clock). Ordinary election 2028-10-16 (Legislative Assembly Act s.3; dissolution discretion intact) = 782 days after cutoff.

## Benchmark (recency-weighted, 90-day half-life, 3 polls)
L 43.1541724958968 | PC 32.964969227287966 | G 13.449355094858092 | Lead 10.189203268608836
Weights: Porter O'Brien 0.2666, Narrative 0.2970, Abacus 0.4364. Formula: weight=0.5^(age/90), ages from exact field-midpoints (PO 87.5d, Narr 73.5d, Abacus 23.5d). SUMPRODUCT in Current Polls!D11:F11.
Reference interval (L-PC): SE 3.1768 -> 90%: +4.9633 to +15.4151 (Model Audit!B12:B14). tau~3.8 (DerSimonian-Laird); diagnostic, NOT classical CI (non-probability panels; Narrative eff n=342 derived from 69-pt denominator; Abacus total n=601 used, decided base undisclosed).
Half-life sensitivity (lead): 30d 11.7357, 60d 10.5969, 90d 10.1892, 120d 9.9848. NOTE: report TEXT says "11.8" at 30d; workbook = 11.736 -> rounds 11.7. Recorded as discrepancy; public graphics use 90d only.

## Three qualifying 2026 polls (basis differences preserved)
PO: field May27-Jun3, n=802/decided 603, mixed opt-in+SMS, decided basis: L43 PC39 G13, lead 4. All-respondent: L32 PC29 G10 und21.
Narrative: Jun10-17, n=495, online panel, DERIVED decided normalization (rounded all-eligible L28 PC21 G9 Lib6 NDP4 oth1 /69): L40.58 PC30.43 G13.04, lead 10.14. eff n~342 (not pollster-reported).
Abacus: Jul29-Aug7, n=601, online panel, decided: L45 PC31 G14, lead 14. Values sum 99 (rounding). Green=14 (13 was a corrected transcription error).
Excluded (recency=0): Abacus Oct2025 53/29/11 (lead 24); PO Nov2025 49/40/8 (lead 9); Angus Reid Nov2025 49/32/11 (lead 17).

## Election-held-now (deterministic proportional-swing on certified 2024 riding votes; scenario, NOT forecast)
2024 certified: 31L 16PC 2G; valid-vote shares L48.2586 PC35.0536 G13.7612 (L 180,806; PC 131,332; G 51,558 of 374,661 valid). Majority 25 of 49.
PO 43/39/13 -> 26L 21PC 2G | Narrative -> 30L 17PC 2G | Abacus -> 32L 15PC 2G | Ensemble -> 30L 17PC 2G.
Illustrations (no probabilities): mild -5pt -> 27/20/2; full-term median replay -> 16/29/4; +2 lead -> 25/22/2; tie -> 23/23/3.
Riding-ledger reconciliation: 162 withdrawn-NDP votes (Saint John Portland-Simonds) excluded to match official 374,661.

## Firewall (Conversion WB Firewall!B5:B6; deterministic; round 8.2/11.4 publicly)
Majority-loss boundary: 8.237 pts adverse L-PC erosion -> margin +1.953 -> L39.036 PC37.083 G13.449 -> 24L 22PC 3G.
PC-plurality boundary: 11.370 -> margin -1.181 -> L37.469 PC38.650 G13.449 -> 22L 24PC 3G.
Tipping ladder (erosion pts): Quispamsis 0.034; Moncton Northwest 0.424; Hampton-Fundy-St. Martins 0.780; Rothesay 5.318; Saint John West-Lancaster 6.964; Kent North 8.237 (flips GREEN; 6th loss = majority gone); Miramichi Bay-Neguac 9.191; Saint John Portland-Simonds 11.370 (PC plurality); Fredericton North 13.456; Champdore-Irishtown 14.036.
Porter O'Brien sensitivity: from 26 seats, +2.925 more -> majority lost (24/23/2); +5.272 -> PC plurality (23/24/2).
Ecological stress routes (majority loss | PC plurality): direct L->PC 4.118 | 5.685 per 100 baseline votes; L turnout withdrawal 7.251 | 9.313; PC recruits from non-voters 9.072 | 11.549; L->Green 5.681 | 9.313. Stylized aggregates, not voter flows.

## Day-674 comparators (Day674 WB Day 674 sheet)
Graham(L, 2006 share 47.158) poll 51 | retention 108.1% | lead +15 | swing +3.84 | final margin -14.343 | drift -29.343 | Lost gov 2010 | day674 2008-07-23 | input: May 2008 CRA, exact dates NOT FOUND | grade A- retrospective
Alward(PC, 2010 48.796) 44 | 90.2% | +12 | -4.80 | -8.084 | -20.084 | Lost gov 2014 | 2012-08-01 | -71d (2012-05-22 CRA) | B
Gallant(L, 2014 42.732) 50 | 117.0% | +22 | +7.27 | +5.913 | -16.087 | Vote plurality, lost gov 2018 | 2016-07-27 | -15d (MQO 2016-07-12) | A- archived
Higgs(PC, 2018 31.891) 39 | 122.3% | +13 | +7.11 | +4.996 | -8.004 | Re-elected majority 2020 (47 days later; minority; COVID rally; AR n=199) | 2020-07-29 | -68d | A
Holt(L, 2024 48.259) 43.154 | 89.4% (0.89423) | +10.19 | -5.10 | ? | ? | Unknown | 2026-08-26 | -23.5d latest component | A/A- derived ensemble
Gov/leader measures at day674 (separate question types): Graham sat 59, pref premier 38; Alward sat 45, pp 37; Gallant sat 49 (separate CRA wave), MQO leadership 4.8/10; Higgs sat 81, AR approval 80; Holt Narrative sat 35 (online), AR approval 41.
Higgs May 2020 pollster disagreement: PC39/L26 online vs PC48/L30 telephone.
Elections dataset: 2006 L47.16/PC47.46 -> 29L 26PC (55 seats, maj 28); 2010 PC48.80/L34.45 -> 42PC 13L; 2014 L42.73/PC34.65 -> 27L 21PC 1G (49 seats); 2018 L37.80/PC31.89/G11.88 -> 22PC 21L 3G 3PA (PC formed gov); 2020 PC39.34/L34.35/G15.24 -> 27PC 17L 3G 2PA; 2024 L48.26/PC35.05/G13.76 -> 31L 16PC 2G.
Boundaries/assembly changed 2010->2014 and pre-2024; historical seat counts not used to calibrate 2024 map.

## Model gate (2028 NOT ESTIMABLE)
Reasons: only 3 recent polls, all non-probability/mixed panels; historical ledger gaps (dates/modes/denominators, esp. pre-2014); only 3 comparable full-term analogues (Higgs 47-day horizon non-exchangeable); no verified 30+ mandate Canadian training set at primary-source standard; regional/riding error not calibrated; PC leadership election 2026-10-17 AFTER cutoff.
Hindcast MAE (all4|exHiggs): election carry-forward 9.809|10.594; poll carry-forward 9.610|12.698; LOO drift 6.578|4.423 — n too small to validate.
Trajectory cones 3/6/12/18/24 months: NOT ESTIMABLE. Withdrawn: state-space, Canadian hierarchical, Monte Carlo seat sim.
Random seed reserved 20260826; published analysis deterministic. Stack: Python, pandas, NumPy, lxml.

## Government/leader indicators (separate series, never pooled)
AR Holt approval (online Forum, small NB n): 2024-12 53/28; 2025-03 60/28; 2025-06 58/33; 2025-09 52/38; 2025-11 56/35; 2026-03 54/40; 2026-06 41/49 (net -8).
Narrative gov satisfaction: 2025-05 59/29 (phone), 2025-08 63/30 (phone), 2026-06 35/37 (ONLINE — mode break).
Abacus 2026-08: gov handling 32/37; Holt favourability 35/32; right direction 34/45.
Abacus Oct2025 -> Aug2026 (provider/weighting changed; 2025 wave post-Throne-Speech): handling 42->32; consulting/communicating 40->36; trust 39->33; positive change 38->32; people at centre 38->31; ground running 43->36; net fav +21->+3; decided L 53->45.
Issue handling Aug 2026: health 29; cost of living 25; housing 29; budget mgmt 27; spending 23; wildfire = highest rating.
Opposition: PC opposition approval 17%; ~half cannot rate leadership candidates; 56% unsure whom preferred.
Regional (descriptive only, small/undisclosed bases): Abacus North L65; Central L27 PC38 G29. PO: Moncton + rural-Francophone L lead (franco cell n=97); rural-Anglophone PC lead.
By-election Miramichi West 2025-10-06: PC 57.40% vs 57.08% in 2024.

## Promise universe (Conversion WB)
102 raw bullets -> 108 atomic -> 104 canonical (4 dup/xref). Tracker: COMPLETE 20; IN PROGRESS 48; NO PUBLIC TRACKER STATUS 35; NO STATUS 1. Analyst public-evidence stage: fully operational 9; legislation/authority 12; operational begun 16; funding appropriated 11; partially available 7; design/consultation 13; not verifiable 36. Domains: health 35; education 16; econ dev 15; affordability+housing 14; trusted leadership 13; environment 11.

## Five flagships (chain: promise -> funded -> implementation -> output -> outcome -> recognition)
1 Primary care: 30 clinics by end-2028; $30m x2 + $170.4m physician agreement + $50m digital. 15 announced by 2026-05-04; 14 clinics: 6,853 attachments (22,204 expected); 67 net new MDs (15 family). OUTCOME: permanent provider 77%->73% (2024->2025, NBHC; fieldwork Oct25-Jan26 too early to attribute); timely access 34%; ~52% ED visits non-urgent. Recognition: health handling 29%. Verdict: implementation advancing; effectiveness not established.
2 Affordability: 10% rebate on eligible consumption (~$216/yr avg); carbon-adjuster removed Dec 2025; 3% rent cap. Rates +9.7% Apr2025 residential, +4.29% Apr2026 all-class; CPI 2025 1.7% (food 3.1, shelter 2.9). Recognition: cost-of-living 25%. Verdict: instruments operational; net effect/adequacy mixed. NOT "10% off power bills".
3 Housing: starts 6,169(2024)->7,587(2025) (highest since 1955; target 6,000); affordable starts 343 vs 59/yr 2019-23 baseline (+194 Jan-Mar 2026); tracked chronic homelessness 1,050(2024)->996(Dec25)->932(May26) (wording/coverage caution, 3 urban centres). Starts != completions. Recognition: housing 29%. Verdict: strongest leading outputs; final outcome not established.
4 School food: breakfast 136 schools -> all schools Sept 2025 ($13m fed-prov); $26m pay-what-you-can lunch to begin Sept 2026 (~1 yr behind costing assumption). No reach/outcome series yet. Verdict: breakfast delivered; lunch pending at cutoff; outcomes NOT YET OBSERVED.
5 Balanced budgets: promise "balance the budget in each year of our mandate" (Disclosure L-003). 2024-25 actual deficit $104.4m (transition yr); 2025-26 Q3 projection $1.328b; 2026-27 budget $1.394b deficit; net debt to $15.902b. Recognition: budget 27%, spending 23%. Verdict: clear promise miss / off trajectory.

## Communications / delivery-legibility
OBSERVED: implementation-to-public-evaluation gap (outputs coexist with 25-32% evaluations). HYPOTHESES (not diagnoses): output-to-outcome credit conversion; weak mandate compression (6 coequal priorities under rotating frames: fresh start, brighter future, change in motion, accelerating change, building the foundation, putting New Brunswickers first). NOT supported: generic channel failure (comms measure fell 4 vs 10 overall), universal messenger blockade (wildfire highest rating), broad French-language failure (supply bilingual; North strongest; franco cell n=97 — reception unmeasured). SUPPORTED in one event: consultation-to-closure failure (post-secondary options paper; final budget froze grants). Decision rule: measure awareness+attribution+adequacy+experience in same respondents.
Admin health: senior civil-service morale UNOBSERVED (no representative survey/turnover/vacancy/sick-leave series). Amber strain mechanisms: 12% Part I reduction over 3 yrs (~$100m, announced 2026-03-17); RTIPPA 59.5% within 30 business days, 62% of professionals affirm tools/resources; AG Tourism-Heritage-Culture reporting gap; Finance/HR dual-hatting. Labour: CUPE 1190 ratified 95%; tentative NBU master agreement; federation warns on attrition. Leadership record: mostly internal moves/retirements — continuity, not exodus.

## Watchlist W01-W12 (status at cutoff)
W01 two-poll L-PC margin: G>=10, A5-10, R<5 x2 — current 10.189 GREEN-EDGE. W02 nowcast L seats: G>=27, A25-26, R<=24 consecutive — 30 GREEN. W03 gov handling: G>=40+net pos, A30-39, R<30&dis>50 — 32/37 AMBER. W04 leader: R approval<45 & net neg x2 — fav 35/32, AR 41/49 AMBER-RED. W05 positive change/trust/issues: 32/33/25-29 AMBER. W06 primary-care provider: target 81 — 73 RED. W07 housing completions/rents: starts only AMBER. W08 school food reach: breakfast universal, lunch pre-launch AMBER. W09 fiscal: $1.33b proj/$1.39b budget RED. W10 Part I workforce pulse: no public series GREY/UNOBSERVED. W11 PC leader recognition: ~half can't rate GREEN-FOR-LIBERALS/UNSTABLE. W12 regional firewall replication: Central/rural-Anglophone weak AMBER.

## Conditional paths (no probabilities)
Re-election: broad retention (stay above ~+2 boundary); delivery+credit conversion; competitive shelter. Defeat: PC consolidation (4.1 direct switch removes majority); turnout/regional breach (7.3 withdrawal); capacity+credibility cascade. Each path carries a disconfirming test (audit s10).

## Corrections log (carried into methodology)
1) Riding total 374,823 -> 374,661 (162 withdrawn-NDP votes excluded). 2) Narrative decided basis derived (L40.58/PC30.43/G13.04, denom 69) — flagged. 3) Narrative satisfaction mode break separated. 4) 2028 probability: none (confirmed). 5) Civil-service morale UNOBSERVED. 6) Abacus Aug-2026 Green 13->14 transcription fix. 7) Window-robustness claim corrected to explicit offsets (Alward/Higgs outside +-30d; Graham dates not found). 8) Comms diagnosis downgraded to hypothesis pair. 9) "Independent stage audit" relabelled "analyst-coded public-evidence audit". 10) NEW (this design edition): report text prints 30-day half-life lead as 11.8; workbook value is 11.736 (rounds 11.7). Graphics use the 90-day benchmark only.

## GRAPHIC CLAIM LEDGER (design-series IDs; map to sources + workbook cells)
C01 2024 certified 31-16-2; L 48.26% valid — fact — S01; Elections!Q10:S10.
C02 Cutoff 2026-08-26 = day 674 (election clock) / 662 (office) — fact/calc — S05.
C03 Ordinary date 2028-10-16; 782 days out; dissolution possible — fact — LAA s.3.
C04 Benchmark L43.2/PC33.0/G13.4 — calculation — CurrentPolls!D11:F11 (weights .267/.297/.436).
C05 Lead +10.2 (10.189) — calculation — ModelAudit!B11.
C06 90% reference interval +5.0..+15.4 (SE 3.177; tau~3.8); diagnostic not CI — calculation — ModelAudit!B12:B14.
C07 Three polls + bases (PO decided; Narrative derived-decided; Abacus decided, n-total variance base) — facts — S06,S07,S08.
C08 Poll-specific seats 26-32; ensemble 30-17-2 — scenario/calc — NowcastScenarios!G5:I8.
C09 Majority 25 of 49 — fact — Elections!W10.
C10 Majority-loss boundary 8.237 (~8.2) -> 24-22-3 — scenario — Firewall!B5.
C11 PC-plurality boundary 11.370 (~11.4) -> 22-24-3 — scenario — Firewall!B6.
C12 Retention ~89% (0.8942) = 43.154/48.259; NOT a probability — calculation — Day674!O9.
C13 Comparator table (leads 15/12/22/13/10.2; retention 108/90/117/122/89) — calc/facts — Day674 sheet.
C14 Graham/Alward/Gallant later lost; drifts -29.3/-20.1/-16.1 — facts/calc — Day674!Y5:Y7.
C15 Higgs: minority, COVID, 47 days to election, drift -8.0, re-elected — facts — Day674 row8.
C16 2028 probability NOT ESTIMABLE (6-reason model gate) — non-finding — ModelAudit!G17:J22; Historical!A31:F37.
C17 Gov/leader measures (sat 35/37; handling 32/37; direction 34/45; AR 41/49; fav 35/32) — facts — S06,S08,S09.
C18 Abacus wave deltas (lead 24->14 etc.; provider/weighting changed) — facts w/ caution — S06,S36.
C19 Promise counts (104; 20/48/35/1; stages 9/12/16/11/7/13/36) — coding — PromiseSummary.
C20 Primary care chain (15 clinics; 6,853; 77->73) — facts — S15,S16,S17.
C21 Affordability chain ($216; +9.7%/+4.29%; 3% cap; CPI) — facts — S32,S33,S21.
C22 Housing chain (7,587 starts; 343 affordable; homeless 1050->932 caution) — facts — S10.
C23 School food (breakfast all schools; lunch Sept 2026; outcomes not yet observed) — facts — S13,S34,S35.
C24 Balanced-budget miss ($104.4m; $1.328b; $1.394b; $15.902b) — facts — S19,S20,S21,S22.
C25 Delivery-legibility gap: observed gap + hypothesis pair — hypothesis — Communications sheet.
C26 Civil-service morale UNOBSERVED + amber mechanisms — non-finding/inference — AdminHealth.
C27 Opposition shelter (17%; ~half can't rate; 56% unsure; leadership 2026-10-17) — facts — S06 + PCNB.
C28 Regional descriptive (North 65; Central 27/38/29; franco n=97) — facts w/ caution — S06,S07.
C29 Ecological stress routes (4.1/7.3/9.1/5.7; 5.7/9.3/11.5/9.3) — scenario — StressTests!A15:K23.
C30 Tipping ladder (0.03..14.0; Kent North 8.24; SJPS 11.37) — scenario — Firewall!A10:F31.
C31 PO sensitivity (+2.9 majority; +5.3 plurality) — scenario — Firewall!A34:I37.
C32 Watchlist statuses W01-W12 — coding — Watchlist sheet.
C33 Half-life sensitivity 11.7/10.6/10.2/10.0 — calculation — ModelAudit!D5:H8 (+discrepancy note).
C34 Hindcast MAEs 9.8|10.6, 9.6|12.7, 6.6|4.4 — calculation — ModelAudit!A18:E20.
C35 Illustrative scenarios (-5pt 27-20-2; median replay 16-29-4; +2 25-22-2; tie 23-23-3) — scenario — NowcastScenarios!A9:I12.
C36 Miramichi West by-election PC 57.40 vs 57.08 — fact — day674 ledger S14.

## Source ledger (conversion numbering S01-S45; key URLs)
S01 Elections NB 41st GE report (2025-06-02, A) https://www.electionsnb.ca/content/dam/enb/pdf/october-21-2024-forty-first-provincial-general-election.pdf
S06 Abacus 2026-08-14 (A-) https://abacusdata.ca/holts-liberals-maintain-strong-lead-as-pcs-search-for-new-leader/
S07 Porter O'Brien 2026-06-23 (A) https://www.porterobrien.com/post/porter-o-brien-releases-first-public-semi-annual-new-brunswick-poll-liberals-narrowly-lead-pcs-amo
S08 Narrative 2026-07-02 (A) https://narrativeresearch.ca/low-provincial-government-satisfaction-levels-reflected-in-voter-intentions-across-atlantic-canada/
S09 Angus Reid June 2026 (A) https://angusreid.org/premiers-performance-june-2026/
S10 Affordability/housing tracker https://www2.gnb.ca/content/gnb/en/corporate/promo/government-priorities/affordability-housing.html | S11 report card .../report-card.html | S12 econ dev | S13 education | S14 environment | S31 leadership (all GNB priority pages, A)
S15 clinics midway 2026-05-04 https://www.gnb.ca/en/news/n-b.2026.05.province-reaches-midway-point-collaborative-care-clinic-commitment.html
S16 health update 2026-04-29 https://www.gnb.ca/en/news/n-b.2026.04.government-provides-update-health-care-system.html
S17 NBHC primary care https://nbhc.ca/nb-primarycare2025-access-experience-equity | S18 https://nbhc.ca/surveys/2025-primary-care-survey
S19 Disclosure L-003 https://nbliberal.ca/wp-content/uploads/disclosure-l-003-balanced-budgets-1.pdf
S20 Public Accounts https://www.gnb.ca/en/news/n-b.2025.09.public-accounts-for-2024-25.html
S21 Main Estimates https://www.gnb.ca/content/dam/GNB3/gov/budget/docs/main-estimates-budget-principal-2026-2027.pdf
S22 Budget release https://www.gnb.ca/en/news/n-b.2026.03.budget-2026-27-putting-new-brunswickers-first.html
S23 leadership 2025-03 | S24 2025-08 | S25 2026-04 (gnb.ca news)
S26 RTIPPA review https://www.gnb.ca/content/dam/GNB3/gov/rtippa-ldipvp/docs/rtippa-review-report.pdf
S27 AG grants https://www.agnb-vgnb.ca/uploads/volume_section_translations/697/file/agnb-VI-C4-2026-En.pdf
S28 self-sufficiency plan | S29 Throne 2025 | S30 State of Province 2026 (gnb.ca)
S32 rebate https://www2.gnb.ca/content/gnb/en/corporate/promo/electricity-rebate.html | S33 NB Power rate decision
S34 breakfast | S35 lunch (gnb.ca news) | S36 Abacus 2025-11 https://abacusdata.ca/abacus-data-new-brunswick-poll-one-year-in-susan-holts-liberals-strengthen-their-lead/
S37/S38 University Affairs (B) | S39 wildfire closures | S40 CUPE 1190 | S41 NBFL (B)
S42 prior day-674 model (Reproducible derived, local) | S43 Cdn Parliamentary Review 2011 (B) | S44 Gallant Throne https://www.legnb.ca/content/house_business/58/1/throne_speech/ThroneSpeech2014-e.pdf | S45 Higgs Throne https://www.legnb.ca/content/house_business/59/2/journals/01181120e.pdf
Day674 WB extras: LAA https://laws.gnb.ca/en/document/cs/2014,c.116 | Premier's office gnb.ca | PCNB leadership https://pcnb.ca/event/pcnb-leadership-election/ (2026-10-17) | Miramichi West https://www1.gnb.ca/leglibbib/en/Resources/NBElections.aspx/ElectionResults/10-6-2025 | CRA 2008 tables + CRA 2016 + MQO 2016 + AR 2020 + Narrative 2020 archives (day674 Sources S10-S24).

## Public-link status (updated v1.2)
No public methodology URL exists yet -> clearly marked placeholder "[method + data link — to be inserted before publication]". NO QR code until a real URL exists. Disclosure FILLED (v1.2, author-confirmed): "I am a former provincial and federal Liberal political staffer. This is personal, independent analysis — it was not commissioned, reviewed or endorsed by any party or organization, and it does not reflect the views of my employer." — wording open to Kurt's veto.


## v1.1 post-audit changes (2026-08-27, external prepublication audit adopted)
- Canvas sizing: all fixed frames now border-box → export at exactly declared px (1080×1350 / 1080×1080 / 1080×1920).
- Contrast: essential grey #8B9098→#5A6069 on light; #7A8087→#9BA1A8 on dark; amber #A8730F→#8A5E0D. Type floors raised (min ~13px on 1350 masters).
- Wording: morale = "not established in public evidence" (no private-source references); Story 6 = "Is credit keeping pace?"; gate hindcast = 6.6–9.8 all-four / 4.4–12.7 ex-Higgs; "-5 pts" scenario = "5-pt erosion (leaving L +5.2)"; fingerprint = "up to three verified points (Holt: two)"; "uniform proportional swing" standardized.
- Namespaces: sources CONV-Sxx (conversion WB) vs D674-Sxx (day-674 WB); public claim IDs = PUB-C series (C≡PUB-C), workbook audit IDs = AUD-C.
- current_polls.csv: other_decided_basis corrected (Narrative 15.942=11/69; Abacus 10=residual incl. rounding; excluded waves 7/3/8); undecided column renamed undecided_all_respondents.
- C36 (Miramichi West by-election) WITHDRAWN from public use pending raw-vote sourcing (not in replication CSVs; used in no graphic).
- New claims: C37 chronic absenteeism 32.3→31.0 (CONV WB Outcomes!A12:L12, different windows); C38 avg weekly earnings +3.7% 2025 vs 3.0% target, was +3.8% 2024 (Outcomes!A18:L18); C39 labour agreements CUPE 1190 95% + NBU tentative (CONV-S40 + audit §7).
- Replication: ridings_2024_three_party.csv (49 ridings, sums reconcile 180,806/131,332/51,558) + code/build.py recomputation harness (stdlib Python; recomputes ensemble, interval, seats, firewall, tipping ladder, half-life, hindcast MAEs; prints PASS/DEVIATION vs stored values).
- S09 release-date conflict disclosed: 2026-06-13 (CONV WB) vs 2026-06-18 (D674 WB).
- Story safe zones: 250px top / 340px bottom; guides default off; claim IDs burned into frames; Reel cover frame added (420×654 cover crop guidance).
- LinkedIn: sized PNGs export now; selectable-text 4:5 PDF document post = remaining production task (print-based copy).
- Higgs framing in copy: always "three of four full-term-adjacent comparators lost; Higgs re-elected (minority/pandemic/47-day runway)".