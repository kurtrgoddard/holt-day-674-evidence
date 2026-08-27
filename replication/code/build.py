#!/usr/bin/env python3
# Holt at Day 674 - recomputation harness (v1.3, 2026-08-27)
# Python 3.10+, standard library only. Run from /replication/:  python3 code/build.py
# Recomputes every model-derived public number from the frozen CSVs, prints PASS/DEV
# against stored values, and EXITS NONZERO if any deviation is unresolved (0 = clean).
import csv, math, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "..", "data")
FAILS = []

def load(name):
    with open(os.path.join(DATA, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def check(label, got, want, tol, unit=""):
    ok = abs(got - want) <= tol
    if not ok: FAILS.append(label)
    print(f"{'PASS ' if ok else 'DEV  '} {label:58s} got {got:>12.6f}  stored {want:>12.6f}  d={got-want:+.6f} {unit}")

def check_seats(label, got, want):
    ok = (got["L"], got["PC"], got["G"]) == want
    if not ok: FAILS.append(label)
    print(f"{'PASS ' if ok else 'DEV  '} seats {label:44s} got {got['L']}-{got['PC']}-{got['G']}  stored {want[0]}-{want[1]}-{want[2]}")

print("=" * 100)
print("1. RECENCY-WEIGHTED ENSEMBLE (weight = 0.5^(age_days/90), normalized over core 2026 polls)")
polls = [p for p in load("current_polls.csv") if p["core_2026"] == "TRUE"]
raw = [(float(p["age_days_midpoint"]), float(p["liberal"]), float(p["pc"]), float(p["green"]),
        float(p["n_decided_or_effective"] or p["n_total"])) for p in polls]
w = [0.5 ** (a / 90.0) for a, *_ in raw]
W = sum(w); w = [x / W for x in w]
bench = [sum(w[i] * raw[i][k] for i in range(len(raw))) for k in (1, 2, 3)]
lead = bench[0] - bench[1]
check("Liberal benchmark", bench[0], 43.1541724958968, 0.005, "pts")
check("PC benchmark", bench[1], 32.964969227287966, 0.005, "pts")
check("Green benchmark", bench[2], 13.449355094858092, 0.005, "pts")
check("Liberal-PC lead", lead, 10.189203268608836, 0.005, "pts")
for i, p in enumerate(polls):
    print(f"      weight {p['pollster']:22s} {w[i]:.6f}  (stored {float(p['normalized_weight']):.6f})")

print("=" * 100)
print("2. REFERENCE INTERVAL (DerSimonian-Laird heterogeneity on the L-PC margin; methodology s4)")
margins = [r[1] - r[2] for r in raw]
v = []
for a, l, pc, g, n in raw:
    p1, p2 = l / 100.0, pc / 100.0
    v.append((p1 + p2 - (p1 - p2) ** 2) / n * 10000.0)
wi = [1.0 / x for x in v]
ybar = sum(wi[i] * margins[i] for i in range(3)) / sum(wi)
Q = sum(wi[i] * (margins[i] - ybar) ** 2 for i in range(3))
tau2 = max(0.0, (Q - 2) / (sum(wi) - sum(x * x for x in wi) / sum(wi)))
se = math.sqrt(sum((w[i] ** 2) * (v[i] + tau2) for i in range(3)))
z90 = 1.6448536269514722
print(f"      per-poll margins {['%.3f' % m for m in margins]}  variances {['%.3f' % x for x in v]}")
check("tau (between-poll SD)", math.sqrt(tau2), 3.8, 0.5, "pts (approx target)")
check("ensemble SE", se, 3.1768, 0.15, "pts")
check("90% interval low", lead - z90 * se, 4.9633, 0.30, "pts")
check("90% interval high", lead + z90 * se, 15.4151, 0.30, "pts")
print("      NOTE: the workbook stores SE as a value; small deviations reflect its exact n assumptions.")

print("=" * 100)
print("3. SEAT MODEL (uniform proportional swing on certified 2024 three-party riding votes)")
ridings = [(r["riding"], float(r["liberal_votes_2024"]), float(r["pc_votes_2024"]), float(r["green_votes_2024"]))
           for r in load("ridings_2024_three_party.csv")]
TL = sum(r[1] for r in ridings); TP = sum(r[2] for r in ridings); TG = sum(r[3] for r in ridings)
TT = TL + TP + TG

def factors(l, pc, g):
    s3 = l + pc + g
    return (l / s3) / (TL / TT), (pc / s3) / (TP / TT), (g / s3) / (TG / TT)

def winner(vl, vp, vg, fL, fP, fG):
    pl, pp, pg = vl * fL, vp * fP, vg * fG      # strict-greater tie rule
    return "L" if (pl > pp and pl > pg) else ("PC" if pp > pg else "G")

def seats(l, pc, g):
    fL, fP, fG = factors(l, pc, g)
    won = {"L": 0, "PC": 0, "G": 0}
    for name, vl, vp, vg in ridings:
        won[winner(vl, vp, vg, fL, fP, fG)] += 1
    return won

for label, shares, want in [
    ("Porter O'Brien 43/39/13", (43, 39, 13), (26, 21, 2)),
    ("Narrative derived", (40.57971014492754, 30.434782608695656, 13.043478260869565), (30, 17, 2)),
    ("Abacus 45/31/14", (45, 31, 14), (32, 15, 2)),
    ("90-day ensemble", tuple(bench), (30, 17, 2)),
    ("5-pt erosion (leaving L +5.2)", (bench[0] - 2.5, bench[1] + 2.5, bench[2]), (27, 20, 2)),
    ("Two-point lead", (39.059570861592384, 37.059570861592384, bench[2]), (25, 22, 2)),
    ("Tie", (38.059570861592384, 38.059570861592384, bench[2]), (23, 23, 3)),
]:
    check_seats(label, seats(*shares), want)

print("=" * 100)
print("4. FIREWALL BOUNDARIES (erosion e: L-e/2 -> PC+e/2; bisection to 1e-6, reported at 3 decimals)")
def seats_at(e): return seats(bench[0] - e / 2.0, bench[1] + e / 2.0, bench[2])
def find_boundary(cond):
    lo_e, hi_e = 0.0, 25.0
    for _ in range(60):
        mid = (lo_e + hi_e) / 2.0
        if cond(seats_at(mid)): hi_e = mid
        else: lo_e = mid
    return hi_e
b_maj = find_boundary(lambda s: s["L"] <= 24)
b_plu = find_boundary(lambda s: s["PC"] > s["L"])
check("majority-loss boundary", b_maj, 8.237, 0.005, "pts erosion")
check("PC-plurality boundary", b_plu, 11.370, 0.005, "pts erosion")
s_maj, s_plu = seats_at(b_maj + 1e-4), seats_at(b_plu + 1e-4)
print(f"      at majority loss: {s_maj['L']}-{s_maj['PC']}-{s_maj['G']} (stored 24-22-3);"
      f"  at plurality: {s_plu['L']}-{s_plu['PC']}-{s_plu['G']} (stored 22-24-3)")

print("=" * 100)
print("5. TIPPING LADDER (first ten Liberal-held seats to flip, by required erosion)")
STORED = [("Quispamsis", 0.034), ("Moncton Northwest", 0.424), ("Hampton-Fundy-St. Martins", 0.780),
          ("Rothesay", 5.318), ("Saint John West-Lancaster", 6.964), ("Kent North", 8.237),
          ("Miramichi Bay-Neguac", 9.191), ("Saint John Portland-Simonds", 11.370),
          ("Fredericton North", 13.456), ("Champdoré-Irishtown", 14.036)]
fL0, fP0, fG0 = factors(*bench)
lib_now = [(n, vl, vp, vg) for n, vl, vp, vg in ridings if winner(vl, vp, vg, fL0, fP0, fG0) == "L"]
flips = []
for name, vl, vp, vg in lib_now:
    lo_e, hi_e = 0.0, 30.0
    for _ in range(50):
        mid = (lo_e + hi_e) / 2.0
        fL, fP, fG = factors(bench[0] - mid / 2.0, bench[1] + mid / 2.0, bench[2])
        if winner(vl, vp, vg, fL, fP, fG) == "L": lo_e = mid
        else: hi_e = mid
    if hi_e < 29: flips.append((hi_e, name))
flips.sort()
norm = lambda s: s.replace("\u2013", "-").casefold()
for i, (want_name, want_e) in enumerate(STORED):
    got_e, got_name = flips[i]
    ok = abs(got_e - want_e) <= 0.02 and norm(got_name) == norm(want_name)
    if not ok: FAILS.append(f"tipping {i+1}: {want_name}")
    print(f"{'PASS ' if ok else 'DEV  '} tip {i+1:2d} got {got_name:34s} {got_e:7.3f}   stored {want_name:34s} {want_e:7.3f}")

print("=" * 100)
print("6. HALF-LIFE SENSITIVITY OF THE LEAD")
for hl, want in [(30, 11.7357), (60, 10.5969), (90, 10.1892), (120, 9.9848)]:
    ww = [0.5 ** (a / hl) for a, *_ in raw]; WW = sum(ww)
    check(f"lead at {hl}-day half-life", sum(ww[i] / WW * (raw[i][1] - raw[i][2]) for i in range(3)), want, 0.01, "pts")
print("      Logged discrepancy: report TEXT prints 11.8 at 30d; workbook computes 11.736 (rounds 11.7).")

print("=" * 100)
print("7. HINDCAST MAEs (governing-party share of valid votes; internal cross-validation only)")
E = {int(r["year"]): r for r in load("elections_2006_2024.csv")}
def share(year, party): return float(E[year][f"{party}_share_valid"])
# (premier, party, election_year, next_election_year, election_share, day674_poll_share)
CASES = [("Graham", "l", 2006, 2010, 47.15760271116861, 51.0),
         ("Alward", "pc", 2010, 2014, 48.79647712660932, 44.0),
         ("Gallant", "l", 2014, 2018, 42.73213195279484, 50.0),
         ("Higgs", "pc", 2018, 2020, 31.890588727084392, 39.0)]
e1 = [abs(share(ny, p) - es) for _, p, ey, ny, es, d in CASES]
e2 = [abs(share(ny, p) - d) for _, p, ey, ny, es, d in CASES]
check("election carry-forward MAE (all 4)", sum(e1) / 4, 9.809, 0.05)
check("election carry-forward MAE (ex-Higgs)", sum(e1[:3]) / 3, 10.594, 0.05)
check("poll carry-forward MAE (all 4)", sum(e2) / 4, 9.610, 0.05)
check("poll carry-forward MAE (ex-Higgs)", sum(e2[:3]) / 3, 12.698, 0.05)
# Leave-one-out on the SHARE DRIFT (next-election share minus day-674 poll share),
# each fold predicting one case from the mean of the others.
drifts = [share(ny, p) - d for _, p, ey, ny, es, d in CASES]
def loo_mae(idx):
    errs = []
    for i in idx:
        others = [j for j in idx if j != i]
        pred = sum(drifts[j] for j in others) / len(others)
        errs.append(abs(drifts[i] - pred))
    return sum(errs) / len(errs)
check("LOO share-drift MAE (all 4; 3 train/fold)", loo_mae([0, 1, 2, 3]), 6.578, 0.01)
check("LOO share-drift MAE (scheduled-term only; 2 train/fold)", loo_mae([0, 1, 2]), 3.848130, 0.001)
print("      v1.3: Higgs is removed from BOTH training and scoring in the ex-Higgs folds; the")
print("      workbook's stored 4.423 (Model Audit!E20) was a mis-sliced fold and is superseded.")
print("      These are internally cross-validated on only four cases, with three training cases")
print("      per fold (two when Higgs is excluded); this is not external validation and cannot")
print("      validate a forecast.")

print("=" * 100)
if FAILS:
    print(f"RESULT: {len(FAILS)} DEVIATION(S) — " + "; ".join(FAILS))
    print("Any deviation is a defect: fix data or workbook, never the print. Exiting 1.")
    sys.exit(1)
print("RESULT: ALL CHECKS PASS (0 deviations). Exiting 0.")
sys.exit(0)
