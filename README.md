# Holt at Day 674

- **Author:** Kurt R. Goddard
- **Jurisdiction:** New Brunswick
- **Evidence cutoff:** August 26, 2026
- **Edition:** v1.3

## About this project

Holt at Day 674 is an independent, reproducible analysis of the New Brunswick government's standing at a fixed evidence cutoff. It brings together the methodology, claim ledger, source workbooks, machine-readable data, deterministic seat scenarios, and publication graphics needed to inspect the analysis and reproduce its calculations.

The polling benchmark measures the government's position on August 26, 2026. The seat outputs are deterministic election-held-then scenarios, not forecasts. This package does not publish a numerical October 2028 re-election probability.

The evidence cutoff is 2026-08-26; corrections are logged, never silently applied.

## Disclosure

I am a former provincial and federal Liberal political staffer. This is personal, independent analysis — it was not commissioned, reviewed or endorsed by any party or organization, and it does not reflect the views of my employer.

## Repository guide

- [Project index](KRG_Holt_Day674_Index_v1.dc.html)
- [Methodology](KRG_Holt_Day674_Methodology_v1.dc.html)
- [Claim ledger C01–C39; C36 withdrawn](KRG_Holt_Day674_Claim_Ledger_v1.dc.html)
- [Facts and source notes](FACTS.md)
- [Repair log](REPAIR_LOG.md)
- [Replication data dictionary](replication/DATA_DICTIONARY.md)
- [Replication changelog](replication/CHANGELOG.md)
- [Replication script](replication/code/build.py)
- [Recorded replication output](replication/BUILD_OUTPUT.txt)
- [SHA-256 manifest](MANIFEST.sha256)

## Reproduce the calculations

Python 3.10 or later is required. From the repository root:

```bash
cd replication
python3 code/build.py
```

The script uses only the Python standard library. It prints checks against the stored workbook values; any `DEV` or `DEVIATION` line should be reviewed rather than forced to pass.

## Limitations

The current benchmark is based on only three recent polls, all using non-probability or mixed panels. Historical polling records contain gaps in dates, modes, and denominators, and the number of comparable New Brunswick mandate cases is too small to calibrate a 2028 probability. The riding model applies deterministic uniform proportional swing and does not model candidates, incumbency, turnout correlation, regional shocks, or riding-level error. The resulting seat counts describe election-held-then scenarios only.

## Licence

Kurt-authored text, tables, data, and graphics are licensed under [Creative Commons Attribution 4.0 International](LICENSE). Third-party reports, polling material, government documents, and other source material remain subject to their original rights and are not relicensed merely because they appear in this repository.
