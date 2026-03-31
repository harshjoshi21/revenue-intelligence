# Customer Lifecycle Intelligence

## [Launch the App](https://revenue-intelligence.streamlit.app/)

Note: First-time loads and wake-ups from sleep mode can take about 1-2 minutes. If the app does not load immediately, refresh or reopen it once, then wait about a minute.

## Executive Brief

This project is designed as an executive operating view that helps leadership teams align Customer Success, RevOps, and Growth around one question:

How do we protect and grow ARR this quarter with the highest-confidence actions first?

Key decisions this supports:
- Which accounts should Customer Success prioritize this week to reduce churn exposure?
- Where is the pipeline conversion process breaking, and which stage needs intervention?
- Which customer segments/cohorts offer the strongest expansion and NRR opportunity?

It also provides scenario visibility for how ARR trajectory shifts under different operating assumptions.

## Executive Walkthrough (2 Minutes)

Use this sequence for a fast leadership review:
1. Open Executive Snapshot and Top Insights to frame risk and upside quickly.
2. Set one realistic scenario with date, channel, segment, and executive view mode.
3. Review pipeline quality and hygiene to identify conversion leakage.
4. Review churn risk and engagement signals to identify ARR exposure.
5. Review expansion and cohort trends to identify growth acceleration opportunities.
6. Use forecast and what-if controls, then confirm execution owners and SLA windows in Action Playbook.

## Portfolio Context (For Senior Leaders)

This is a personal portfolio project that demonstrates how I structure decision support across Customer Success analytics, RevOps strategy, implementation operations, and solutions engineering.

## Methodology Note

The app uses realistic SaaS simulation to model funnel performance, churn risk, expansion behavior, and scenario outcomes. Assumptions are intentionally transparent so leaders can validate drivers, calibrate confidence, and translate insights into owner-level execution.

## Features

**📈 Sales Funnel Analysis**
- Two-panel pipeline diagnostics: stage volume funnel + stage conversion vs target chart
- Auto-identify the largest stage-to-stage conversion drop for immediate intervention
- Track stuck opportunities by channel (defined as currently open opportunities older than 30 days)
- Opportunity lifecycle realism: open, closed-won, and closed-lost states are simulated within the analysis window
- Drill into oldest opportunities to prioritize channel-level follow-up
- Pipeline hygiene by owner table with SLA status and weekly cleanup quota targets
- SLA severity highlighting and downloadable weekly owner cleanup plan (CSV)
- Breached-owner CSV export for leadership standup packets (Critical/Watch breaches only)
- Critical Breach-only CSV export for immediate escalation review
- Export files include packet ID and filter snapshot metadata for traceable leadership reviews
- Closed outcome diagnostics: loss-reason mix and cycle-time distribution by won vs lost outcomes
- Closed-lost trend by quarter in both count and share terms to identify recurring root-cause mix shifts
- Explicit denominator contract: conversion and stuck metrics are tied to the filtered cohort and as-of-date state

**⚠️ Customer Health & Churn Risk**
- Segment chart uses average churn risk score on a 0-100 scale (higher score = higher churn likelihood)
- Always-visible segment comparison (including low-volume segments) for complete context
- Engagement vs. churn scatter plot to identify at-risk customers
- Engagement score formula shown in-app: 30% feature adoption + 40% monthly usage + 30% support sentiment
- Actionable list of customers requiring intervention
- Signals: engagement score, feature adoption, support sentiment

**💰 Expansion & Cohort Analysis**
- Base vs. expansion ARR breakdown by segment with ARR displayed in millions (max 2 decimals)
- Cohort retention curve with business interpretation (what it means and why it matters)
- Track which cohorts are expanding fastest and whether retention trend is improving or declining

**🔮 ARR Forecast**
- 12-month forward projection based on churn and expansion trends
- What-if scenarios: test impact of improving sales conversion
- Forecast adjusts automatically with your filters

**🎯 Benchmark Lens Interpretation**
- Compare Churn, NRR, SQL→Won, and Expansion against target benchmark ranges
- Adaptive fourth benchmark card: Expansion Rate in Expansion Focus, Pipeline Hygiene in other modes
- Use status signals (Healthy, Watch, Action) to quickly decide where intervention is needed

**⚡ Quick Win + Projected Action Impact**
- Surface the highest immediate upside lever based on the active filtered context
- Translate each playbook action into directional ARR impact estimates for faster prioritization

**🧭 Scenario Readability and Guidance**
- Filter-sensitive disclaimers are shown in executive and tab sections to prompt scenario testing
- Each disclaimer includes a short example so users understand how to drive metric changes
- Root-cause preview is elevated as a high-visibility callout with direct guidance to Closed Outcome Diagnostics
- Negative outcome metrics (for example Closed-Lost and stale pipeline counts) use inverse/red semantics

**🧭 Action Playbook Cards**
- Executive-style priority cards (Critical/High/Monitor) with owner, SLA, trigger, and immediate action
- Priority assignment is calibrated using benchmark drift and leading indicators (not severity labeling alone)
- Projected ARR impact highlighted in each card for faster execution prioritization

## Key Metrics at a Glance

- **Active Customers**: Number of current customers (not churned)
- **Current ARR**: Total annual recurring revenue from active customers
- **Churn Rate**: Observed churn share in the current analysis cohort
- **NRR**: Average account-level net retention proxy from simulated base + expansion ARR

## How to Use

### Filters & What-If Analysis (Left Sidebar)
- **Reset to recommended defaults**: Return to the suggested executive starting context in one click
- **Guided usage flow**: Executive mode first, then filters, then benchmark/quick-win review
- **Date Range**: Focus on a specific time period
- **Marketing Channels**: Filter by organic search, paid ads, referrals, etc.
- **Customer Segments**: Drill into healthcare, finance, tech, non-profit, manufacturing
- **Executive View Mode**: Switch between all accounts, at-risk focus, and expansion focus
- **What-If Slider**: Test impact of improving SQL→Won conversion rate

### Drilling Into the Data
1. **Pipeline Risks**: Identify conversion bottlenecks, compare conversion rates against target, and isolate currently open stuck opportunities older than 30 days
2. **Customer Health Actions**: Prioritize high-risk accounts and intervention signals
3. **Expansion Levers**: Understand segment-level expansion and cohort retention momentum with interpretation context
4. **Scenario Forecast**: Model ARR outcomes under different assumptions
5. **Action Playbook**: Use priority cards to map observed signals to owner-level actions, SLA, and projected impact
6. **Quick Win Signal**: Use the highlighted top opportunity to decide what should be executed first this cycle

Each core tab includes a denominator contract note so benchmark interpretation remains defensible when filters change.

## Data Simulation

This dashboard uses realistic SaaS funnel data:
- **1000+ leads/month** across 6 marketing channels
- **200+ active customers** across 5 industry segments
- **Deal sizes**: $15K–$200K ARR (realistic for mid-market/enterprise)
- **Sales cycles**: 45–150 days depending on segment
- **Churn patterns**: ~8% churn incidence flag in the generated cohort, with risk score influenced by engagement
- **Expansion**: 0–50% ARR expansion sampled for active (non-churned) customers

All data is statistically realistic for portfolio demonstration and intentionally assumption-driven.

## Use Cases

**For RevOps teams:**
- Identify pipeline bottlenecks and stuck deals
- Forecast revenue with confidence
- Detect early churn signals before they become problems

**For Growth leaders:**
- Understand which channels and segments drive expansion
- Model impact of improving conversion rates
- Make data-driven decisions on customer prioritization

**For Customer Success:**
- Find at-risk customers needing intervention
- Understand which engagement signals predict churn
- Track cohort retention over time

## Technical Stack

- **Streamlit**: Interactive dashboard framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **NumPy**: Numerical simulation

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Quick QA Smoke Check

Run this before sharing updates to validate core data contracts and main Streamlit interaction flows:

```bash
python qa_smoke.py
```

### CI Smoke Automation

This repo also runs the same smoke suite automatically via GitHub Actions using [.github/workflows/qa-smoke.yml](.github/workflows/qa-smoke.yml).

- Triggered on pushes to `main` and `dev`
- Triggered on pull requests targeting `main` and `dev`
- Can be run manually from GitHub Actions via `Run workflow`

The workflow installs dependencies from `requirements.txt` and runs `python qa_smoke.py`.

## Deployment

Deploy to Streamlit Cloud, Heroku, or any cloud platform that supports Python.

## Versioning and Release Workflow

This project follows a release-first branching model for portfolio clarity.

1. main = stable, formal releases only.
2. dev = active development and validation branch.
3. Feature branches should be created from dev and merged back into dev.
4. When a release is ready, promote dev to main, then create a release tag on main.
5. Direct commits to main should be avoided unless explicitly required.

Current release status:
- Latest stable release tag: v2.1.1
- Current development release target: v2.2.0 (on dev, pending promotion to main)
- main carries stable tagged releases; dev is the active development branch

Supporting release documentation:
- Current development release notes: [RELEASE_v2.2.0.md](RELEASE_v2.2.0.md)
- Latest stable release summary: [RELEASE_v2.1.1.md](RELEASE_v2.1.1.md)
- Historical readiness checklist: [docs/archive/V2_READINESS_CHECKLIST.md](docs/archive/V2_READINESS_CHECKLIST.md)
- Historical release draft notes: [docs/archive/V2_RELEASE_NOTES_DRAFT.md](docs/archive/V2_RELEASE_NOTES_DRAFT.md)
- Prior stable release summary: [RELEASE_v2.1.0.md](RELEASE_v2.1.0.md)
- Historical v2.0 summary: [docs/archive/RELEASE_v2.0.0.md](docs/archive/RELEASE_v2.0.0.md)

## Keep-Alive Automation (GitHub Actions)

This repo includes a scheduled workflow at [.github/workflows/streamlit-keep-alive.yml](.github/workflows/streamlit-keep-alive.yml) that pings your deployed Streamlit app every 15 minutes and runs a separate HTTP health check.
The workflow normalizes your deployment URL, probes both root and health endpoints, and fails fast if availability checks do not pass.

### One-time setup

1. Go to your GitHub repo -> Settings -> Secrets and variables -> Actions.
2. Create a new repository secret named `STREAMLIT_APP_URL`.
3. Set its value to your deployed Streamlit URL.
4. Merge this workflow to `main` (scheduled workflows run from the default branch).

### Manual run

You can trigger it anytime from GitHub -> Actions -> `Streamlit Keep Alive` -> `Run workflow`.

Note: This helps reduce cold starts but platform-level sleep policies may still apply.

---
