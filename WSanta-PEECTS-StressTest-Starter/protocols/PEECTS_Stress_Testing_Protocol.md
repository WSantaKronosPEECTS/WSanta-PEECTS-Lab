
# PEECTS Stress-Testing Protocol (v1.0) — Life-Safety First

## 0) Non-goals
This protocol is not to “win benchmarks.” It is to decide if PEECTS signals are **actionable earlier** with acceptable false alarms.

## 1) Scope (four tracks)
- **Hurricanes (N. Atlantic/Caribbean):** track & impact cone; 34/50/64-kt wind radii.
- **Solar storms:** CME/flare → Kp/Dst thresholds for grid/satellite risk.
- **Volcanoes:** unrest-to-eruption windows using seismic/tilt/gas proxies.
- **NEOs (experimental):** close-approach corridors; *exploratory only*.

## 2) Life-safety KPIs (thresholded)
- **LTG (Lead-Time Gain):** Δt between PEECTS “actionable” and baseline “actionable.”
- **AAO IoU:** IoU of PEECTS high-risk polygon vs. verifying footprint.
- **SHR:** fraction of events where severity bin matches (within ±1 bin accepted).
- **FAR:** false alerts / total alerts. Target FAR ≤ 0.25 for operational use.

**Actionable** means: threshold crossed that implies preparations (e.g., 34‑kt winds for coastal; Kp≥7; eruption probability above site-specific cut; NEO keyhole corridor flag).

## 3) Datasets (public, examples)
- Hurricanes: best-track & advisories (HURDAT2/NHC); surface obs for verification.
- Solar: CME catalogs and geomagnetic indices (Kp, Dst).
- Volcano: seismic RSAM/tilt/gas (public observatories), Smithsonian GVP logs.
- NEOs: observational arcs and risk tables; verification via close-approach logs.

## 4) Ingestion schema (JSON record)
```json
{
  "domain": "hurricane|solar|volcano|neo",
  "event_id": "string",
  "issue_time_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "region": "string",
  "peects": {
    "prediction": {},
    "risk_polygon": [[lon, lat], ...],
    "severity": "bin/score",
    "actionable_time_utc": "YYYY-MM-DDTHH:MM:SSZ"
  },
  "baseline": {
    "prediction": {},
    "risk_polygon": [[lon, lat], ...],
    "severity": "bin/score",
    "actionable_time_utc": "YYYY-MM-DDTHH:MM:SSZ"
  },
  "verification": {
    "footprint_polygon": [[lon, lat], ...],
    "severity": "bin/score",
    "verify_time_utc": "YYYY-MM-DDTHH:MM:SSZ"
  }
}
```

## 5) Evaluation pipeline (per event)
1. **Assemble inputs** (immutable raw in `data/`).
2. **Run PEECTS** model → prediction, polygons, severity, actionable_time.
3. **Pull baseline** model(s) for the same timestamps (operational references).
4. **Compute KPIs**: LTG, AAO IoU, SHR, FAR.
5. **Write scorecards** to `benchmarks/` and archive JSON to `data/processed/`.
6. **Trigger alerts** (optional) if thresholds are met and FAR guardrails satisfied.

## 6) Decision policy (opinionated defaults)
- Promote to **Operational Trial** if median LTG ≥ 3h and FAR ≤ 0.25 over ≥10 events.
- Trigger **Quiet Advisory** if LTG ≥ 1h with AAO IoU ≥ 0.3 even when severity bin off by 1.
- **Kill switch:** if FAR > 0.5 over last 20 alerts, automatically throttle to “research-only.”

## 7) Reporting rhythm
- **Daily**: rolling dashboard (last 14 days).
- **Weekly**: one-page scorecard (median LTG, AAO IoU, SHR, FAR) + narrative.
- **Post-mortems**: for any miss with human impact, require a root-cause note.

## 8) Ethics & Safety
Prefer **quiet advisories** to public alarms. Share raw outputs with trusted partners; publish only aggregated metrics until robustness is proven.

## 9) First-week boot plan
**Day 1:** create repo from this starter; wire CI; pick one active domain (e.g., hurricanes).  
**Day 2–3:** ingest 3–5 recent events; hand-enter verification footprints.  
**Day 4:** implement PEECTS equations into the selected pipeline (TODO blocks).  
**Day 5:** generate first scorecard; exercise kill-switch logic.  
**Day 6–7:** tune thresholds to maximize LTG at fixed FAR cap (0.25), then add a second domain.

---

*Keep it simple. Save lives > elegance.*
