# Research notes (2026-11-02)

## pyrsig
- Python client for EPA's RSIG (Remote Sensing Information Gateway) web API. Maintained by Barron Henderson (EPA).
- PyPI: **0.12.0** (2026-02-24), Python >=3.9; deps numpy, **pandas<3**, xarray, requests (extras: geopandas, scipy).
- Docs/gallery: https://barronh.github.io/pyrsig/ ; examples include AirNow vs TEMPO (El Paso), PurpleAir PM2.5, CMAQ-vs-AirNow ozone.
- Per 2024 training notes: API keys only needed for PurpleAir and (at that time) password-protected TEMPO; AirNow is near-real-time, AQS is definitive.
- **Unverified (need prototype):** current TEMPO access requirements, exact request syntax, subset sizes, server reliability.

## Ozone design value (primary source: 40 CFR 50 Appendix U, via Cornell LII mirror)
- DV = annual 4th-highest daily max 8-hr average, averaged over 3 years; compare to 0.070 ppm.
- Daily MDA8 valid if >=13 of 17 8-hr periods (7:00 a.m. to 11:00 p.m.) are valid, or if it exceeds the NAAQS.
- DV above the NAAQS is always valid; DV at/below needs completeness: >=90% of monitoring-season days on average over 3 years and >=75% in any year.
- **Still to verify:** valid-8-hr-average hour count, rounding/truncation, period labeling, exceptional events.

## TEMPO
- Geostationary instrument over North America; products NO2, HCHO, O3 profile/total, clouds; NRT stream (NO2/HCHO/clouds) with ~2-3 h latency aimed at agencies.
- Baseline mission extended to Sept 2026 (check senior-review outcome before the session).
- NASA ARSET runs trainings for air quality managers (2025-26); HAQAST has a surface-ozone tiger team using TEMPO.
- Data availability start date vs the June 2023 smoke event: needs confirming (believed to postdate it).

## Sources
- https://barronh.github.io/pyrsig/api/pyrsig.html
- https://pypi.org/project/pyrsig
- https://gaftp.epa.gov/Air/aqmg/bhenders/presentations/pyrsig/pyrsig_geoxo_2024-05_training.pdf
- https://www.law.cornell.edu/cfr/text/40/appendix-U_to_part_50
- https://www.earthdata.nasa.gov/learn/trainings/geostationary-remote-sensing-trace-gases-air-quality-applications-north-america
- https://www.earthdata.nasa.gov/data/projects/nsite/solutions/tempo-nrt-enhanced-products
- https://haqast.org/tempo-applications-for-surface-ozone-tiger-team/
