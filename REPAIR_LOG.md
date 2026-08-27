# Repair log — external prepublication audit of 2026-08-27, disposition v1.1

Every row of the auditor's Issue_Log.csv, in order. Status: FIXED (in this project), PARTIAL (fixed with a stated limit), KURT (only the author can complete), or DEFERRED (offered as follow-up work).

## Critical
1. **Canvas sizing** — FIXED. All fixed frames now `box-sizing:border-box`; interiors were designed to the inner grid so no reflow resulted. PNG exports in `/exports/` are exactly 1080×1350 / 1080×1080 / 1080×1920 (the dashboard, a variable-height one-pager, exports at 1080×2727).
2. **Reproducibility code** — FIXED (new). `replication/code/build.py` (Python 3.10+, stdlib only, one command) recomputes ensemble, reference interval, all seat scenarios, both firewall boundaries with tie rule and tolerance, the tipping ladder, half-life sensitivity and hindcast MAEs from the CSVs, printing PASS/DEVIATION against stored values. New input: `data/ridings_2024_three_party.csv` (49 ridings; sums reconcile to 180,806 / 131,332 / 51,558). Known limit: the workbook's LOO-drift definition is under-documented; build.py prints its own definition and reports the stored 6.578/4.423 as an open item rather than forcing a match.
3. **Citations** — FIXED. Methodology §18 now lists full clickable URLs (no ellipses/wildcards) for CONV-S01–S45 and D674-S01–S20, with dates, the S09 release-date conflict disclosed (06-13 vs 06-18), year-only dates stored as text, and a blanket access date (2026-08-26). Archive.org snapshots remain a KURT pre-publication task.
4. **Disclosure + method URL** — HALF RESOLVED (v1.2). Disclosure inserted everywhere from author-confirmed facts (former provincial and federal Liberal staffer; employer views not reflected; employer unnamed) — wording open to veto. Method/data URL still KURT: placeholder stays, no QR until a real URL exists.

## High
5. **Mobile legibility** — PARTIAL. Type floors raised (nothing below ~13px source on 1350 masters; receipts/meta up 1–2px; matrix cell text up). Dense frames (carousel 3/4/7/8, dashboard, matrix) remain information-dense by design for save/zoom use; each keeps a large-type takeaway readable in feed. A split-edition variant (2 frames per dense frame) is offered as follow-up work — flagged in QC as "dense frames noted."
6. **C20–C24 sheet mapping** — FIXED. Now `CONV WB Flagship Policies!B5:K5…B9:K9` (+ Outcomes rows), with workbook names on every claim.
7. **Dashboard claim coverage** — FIXED. Every panel now carries a CLAIMS chip; new ledger entries C37 (absenteeism), C38 (weekly earnings), C39 (labour agreements) cover the previously unledgered rows.
8. **current_polls.csv data** — FIXED. `other_decided_basis` corrected (Narrative 15.942 = 11/69 derived; Abacus 10 = residual incl. published rounding; excluded waves 7/3/8); undecided renamed `undecided_all_respondents` and never mixed with decided denominators.
9. **Facebook history framing** — FIXED. Auditor's revised copy adopted verbatim (three-of-four framing, Higgs explained separately) across LinkedIn/Instagram/Facebook.
10. **"Probably win again"** — FIXED. Same adoption; deterministic language throughout.
11. **Hindcast wording** — FIXED. Gate card: "6.6–9.8 across all four cases (4.4–12.7 excluding Higgs)"; alt text matched; C34 restated.
12. **Civil-service confidentiality** — FIXED. All assets now say public evidence does not establish morale; no references to private accounts or anecdote counts anywhere (carousel 9, card B5, dashboard 5, methodology §10, copy, alt text, transcript).
13. **Dependency robustness** — PARTIAL. `support.js` is local; fonts load from Google Fonts. The canonical delivery for platforms is the validated static PNG set in `/exports/` (fonts rasterized). A fully self-contained offline HTML bundle is available on request.
14. **Exports** — FIXED (new). `/exports/carousel|cards|story|dashboard/` PNGs at exact declared pixels, captured from the corrected masters. LinkedIn document-post PDF (selectable text, 4:5) remains DEFERRED — requires a print-based copy; say the word and I'll build it.

## Medium
15. **"−5 pts" scenario label** — FIXED: "5-pt erosion (leaving L +5.2) → 27 L" (carousel 6, C35, methodology).
16. **Promise total** — FIXED: dashboard row now reads 9 + 39 + 20 + 36 = 104.
17. **Story 6 hypothesis wording** — FIXED: "Is credit keeping pace?"; caption asks rather than asserts.
18. **Methodology §10 framing** — FIXED: "descriptive contrast" + "contrary evidence" language.
19–21. **Contrast tokens** — FIXED: #8B9098→#5A6069 on light, #7A8087→#9BA1A8 on dark, #A8730F→#8A5E0D; published ratios corrected to 13.96:1 / 5.82:1.
22. **Story guides + claim IDs** — FIXED: guides default OFF (Tweaks toggle); claim IDs burned into every frame footer; safe zones moved to 250px top / 340px bottom.
23. **Source ID collisions** — FIXED: CONV-Sxx vs D674-Sxx namespaces throughout.
24. **Claim ID collisions** — FIXED by declaration: public series = PUB-C (C ≡ PUB-C), workbook audit series = AUD-C; stated on ledger and methodology. Footers keep compact "C05" form.
25. **Year-only dates** — FIXED in the public ledger (text dates); the frozen workbooks are preserved as supplied (KURT may fix at source).
26. **Legal citation** — FIXED: Legislative Assembly Act, RSNB 2014, c 116, s 3(3)–(6), encoded URL.
27. **Quarterly threshold overlap** — FIXED: amber band 5–<10 (template + C32).
28. **Reel cover** — FIXED: dedicated S0 cover frame (1080×1920, content inside centre grid-crop zone, crop guides on the Tweaks toggle); Reel-specific bottom clearance noted on the frame strip.

## Low
29. **Contrast statement numbers** — FIXED (13.96:1 / 5.82:1).
30. **Fingerprint point count** — FIXED: "up to three verified points (Holt: two so far)."

## Auditor items intentionally not adopted
- Renaming footer claim chips to "PUB-C05" style — the namespace is declared once on the ledger/methodology instead; frames keep the compact form for legibility.
- Rounding changes to any evidence value — none were requested; none were made. Evidence and cutoff are unchanged.
