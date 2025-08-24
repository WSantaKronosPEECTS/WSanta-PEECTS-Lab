
# WSanta-PEECTS Stress-Test Starter (Life-Safety Focus)

**Purpose:** Turnkey scaffold to *stress-test PEECTS predictions under real hazards* (hurricanes, solar storms, volcanoes, NEOs) with one goal: **does it enable earlier, safer actions?**

## What’s inside
- `protocols/PEECTS_Stress_Testing_Protocol.md` – step-by-step playbook.
- `pipelines/` – placeholder Python modules for each hazard + common metrics.
- `benchmarks/` – scorecard templates for weekly reporting.
- `alerts/` – config example and SMS placeholder.
- `.github/workflows/` – CI + link-check to keep the repo healthy.
- `tests/` – minimal unit tests for the metrics.

## Quick start
1. **Clone** this repository (or unzip) into your working folder.
2. Put public datasets in `data/` (see protocol). Keep raw data immutable.
3. Implement your PEECTS equations inside each pipeline module’s TODO sections.
4. Run:  
   ```bash
   python -m pipelines.hurricane_pipeline
   python -m pipelines.solar_pipeline
   python -m pipelines.volcano_pipeline
   python -m pipelines.neo_pipeline
   ```
5. Run tests:  
   ```bash
   python -m pytest -q
   ```
6. Commit and push. GitHub Actions will run CI and link-checkers.

## Life-safety KPIs (operational)
- **Lead-Time Gain (LTG):** minutes/hours of earlier actionable signal vs. baseline.
- **Actionable Area Overlap (AAO IoU):** intersection-over-union of high-risk polygons.
- **Severity Hit Rate (SHR):** correct classification of impact/wind/Kp/eruption class.
- **False Alarm Ratio (FAR):** alerts with no verifying event.

> Opinionated guidance: optimize for **lead time and recall** under a cap on FAR, not for RMSE alone.
