# Revenue Intelligence Dashboard

A data-driven RevOps and Growth Analytics tool that provides real-time visibility across your SaaS funnel, customer health, expansion opportunities, and forward-looking forecasts.

## V2 Progress Snapshot (In Development on `dev`)

Completed so far:
- **Phase 1**: Executive landing experience (hero framing, profile panel, first-glance clarity cards, dynamic insight row)
- **Phase 2**: Decision-oriented analytics flow (action-focused tabs, benchmark lens, glossary, executive view mode, action playbook)
- **Phase 3**: Visual system upgrade (shared chart theme, executive palette, improved chart readability and consistency)
- **Phase 4**: Portfolio packaging (in-app evaluator walkthrough, decisions-enabled framing, leadership review path)
- **Phase 5 (prep)**: Dev-side readiness gate (technical smoke checks and [V2_READINESS_CHECKLIST.md](V2_READINESS_CHECKLIST.md))

Current status:
- `main` remains stable at **v1.0.0**
- `dev` is the active **v2** development line
- Formal release to `main` will happen only after final v2 validation

## Portfolio Context (For Senior Leaders)

This is a personal portfolio project that showcases how I think about Customer Success analytics, RevOps strategy, implementation operations, and solutions engineering through an executive-style revenue intelligence experience.

## Why This Matters: Three Operating Decisions You Can Make Right Now

This project is designed to demonstrate practical decision support, not just reporting. It helps answer:
- Which accounts should Customer Success prioritize this week to reduce churn exposure?
- Where is the pipeline conversion process breaking, and which stage needs intervention?
- Which customer segments/cohorts offer the strongest expansion and NRR opportunity?

It also provides scenario visibility for how ARR trajectory can shift under different conversion and operating assumptions.

On first glance, the landing screen now answers:
- **What this project is**: A unified revenue intelligence workspace for CS and RevOps decisions
- **What to do with it**: Prioritize pipeline, retention, and expansion actions
- **What it conveys**: How operational patterns influence growth trajectory
- **Why it is useful**: Faster, clearer decisions with measurable business impact

## How to Evaluate This Project in 60 Seconds

1. Read the landing hero and first-glance cards to understand purpose and audience fit.
2. Review **Executive Snapshot** and **Top Insights for Current Selection** for immediate risk/opportunity framing.
3. Use the sidebar filters to simulate different operating contexts.
4. Open tabs to investigate funnel bottlenecks, churn drivers, expansion leverage, and forecast scenarios.

## How to Evaluate This Project in 2 Minutes (Leadership Review)

1. **Intent and credibility (0:00-0:30)**: Read the landing hero and professional profile panel.
2. **Signal quality (0:30-1:00)**: Review Executive Snapshot, Top Insights, and Benchmark Lens.
3. **Operational depth (1:00-1:30)**: Toggle Executive View Mode and inspect one segment/channel scenario.
4. **Actionability (1:30-2:00)**: Use Action Playbook to connect findings to owner-level execution.

## Methodology Note

The app uses realistic simulated SaaS data to demonstrate analytical approach, decision framing, and domain depth in customer success, implementation operations, and RevOps workflows.

## Features

**📈 Sales Funnel Analysis**
- Visualize conversion rates at each stage (Leads → MQLs → SQLs → Opportunities → Won)
- Identify stuck deals by marketing channel
- Drill down into specific channels to see individual opportunities

**⚠️ Customer Health & Churn Risk**
- Heat map of churn risk across customer segments
- Engagement vs. churn scatter plot to identify at-risk customers
- Actionable list of customers requiring intervention
- Signals: engagement score, feature adoption, support sentiment

**💰 Expansion & Cohort Analysis**
- Base vs. expansion ARR breakdown by segment
- Cohort retention curves over time
- Track which cohorts are expanding fastest

**🔮 ARR Forecast**
- 12-month forward projection based on churn and expansion trends
- What-if scenarios: test impact of improving sales conversion
- Forecast adjusts automatically with your filters

## Key Metrics at a Glance

- **Active Customers**: Number of current customers (not churned)
- **Current ARR**: Total annual recurring revenue from active customers
- **Churn Rate**: Percentage of customers lost (all-time)
- **NRR**: Net Revenue Retention (expansion revenue / base revenue)

## How to Use

### Filters & What-If Analysis (Left Sidebar)
- **Date Range**: Focus on a specific time period
- **Marketing Channels**: Filter by organic search, paid ads, referrals, etc.
- **Customer Segments**: Drill into healthcare, finance, tech, non-profit, manufacturing
- **Executive View Mode**: Switch between all accounts, at-risk focus, and expansion focus
- **What-If Slider**: Test impact of improving SQL→Won conversion rate

### Drilling Into the Data
1. **Pipeline Risks**: Identify conversion bottlenecks and unresolved opportunities
2. **Customer Health Actions**: Prioritize high-risk accounts and intervention signals
3. **Expansion Levers**: Understand segment-level expansion and cohort retention momentum
4. **Scenario Forecast**: Model ARR outcomes under different assumptions
5. **Action Playbook**: Map observed signals to owner-level actions and SLA guidance

## Data Simulation

This dashboard uses realistic SaaS funnel data:
- **1000+ leads/month** across 6 marketing channels
- **200+ active customers** across 5 industry segments
- **Deal sizes**: $15K–$200K ARR (realistic for mid-market/enterprise)
- **Sales cycles**: 45–150 days depending on segment
- **Churn patterns**: 8% monthly churn, influenced by engagement
- **Expansion**: 10–50% ARR expansion from existing customers

All data is statistically realistic and includes seasonality.

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

## Deployment

Deploy to Streamlit Cloud, Heroku, or any cloud platform that supports Python.

## Versioning and Release Workflow

This project follows a release-first branching model for portfolio clarity.

1. `main` = stable, formal releases only.
2. `dev` = active development and testing for the next major/minor release.
3. Feature branches should be created from `dev` and merged back into `dev`.
4. When a release is ready, merge `dev` into `main` and create a release tag on `main` (for example: `v2.0.0`, `v3.0.0`).
5. Optional milestone tags can be created on `dev` as pre-release checkpoints (for example: `v2.0.0-rc.1`).

Current baseline:
- `v1.0.0` is the stable release baseline on `main`.
- `dev` is the active v2 development line.

Release preparation checklist:
- See [V2_READINESS_CHECKLIST.md](V2_READINESS_CHECKLIST.md) for the full pre-release validation gate on `dev`.
- Draft release notes for final cut: [V2_RELEASE_NOTES_DRAFT.md](V2_RELEASE_NOTES_DRAFT.md)

## Keep-Alive Automation (GitHub Actions)

This repo includes a scheduled workflow at [.github/workflows/streamlit-keep-alive.yml](.github/workflows/streamlit-keep-alive.yml) that pings your deployed Streamlit app every 15 minutes and runs a separate HTTP health check.
The workflow targets Streamlit's health endpoint (`/_stcore/health`) to avoid redirect loops and get a stable status response.

### One-time setup

1. Go to your GitHub repo -> Settings -> Secrets and variables -> Actions.
2. Create a new repository secret named `STREAMLIT_APP_URL`.
3. Set its value to your deployed Streamlit URL (for example: `https://revenue-intelligence.streamlit.app/`).
4. Merge this workflow to `main` (scheduled workflows run from the default branch).

### Manual run

You can trigger it anytime from GitHub -> Actions -> `Streamlit Keep Alive` -> `Run workflow`.

Note: This helps reduce cold starts but platform-level sleep policies may still apply.

---

**Built by Harsh Joshi.**
