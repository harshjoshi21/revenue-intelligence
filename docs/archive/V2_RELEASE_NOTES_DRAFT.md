# v2.0.0 Release Notes (Draft)

Archived historical artifact. This document is preserved for release-process history and is superseded by current tagged releases.

Status: Draft for upcoming formal release from `dev` to `main`.

## Highlights

This release transforms the project from a dashboard demo into an executive-ready portfolio experience for Customer Success and RevOps decision support.

## What's New

### 1) Executive-first landing experience
- Added premium hero section with clear portfolio positioning
- Added professional profile panel for credibility and context
- Added first-glance clarity cards that explain purpose, usage, and value
- Added dynamic top-insight summary for immediate signal extraction

### 2) Decision-oriented analytics flow
- Reframed tabs around action outcomes:
  - Pipeline Risks
  - Customer Health Actions
  - Expansion Levers
  - Scenario Forecast
  - Action Playbook
- Added Executive View Mode (All, At-Risk, Expansion) to speed scenario review
- Added KPI glossary popover for leadership-friendly interpretation
- Added benchmark lens for churn, NRR, conversion, and expansion context
- Added benchmark status cards (Healthy, Watch, Action) for faster executive interpretation
- Added funnel bottleneck detection callout to highlight the biggest stage drop

### 3) Visual system upgrade
- Introduced shared executive chart palette and style helpers
- Standardized chart spacing, legends, axes, and readability patterns
- Improved consistency across funnel, risk, expansion, and forecast visuals
- Added tab-shell section treatments and urgency-first drilldown table presentation

### 4) Action intelligence and guided operations
- Added dynamic Quick Win callout that surfaces the highest immediate upside lever
- Added projected ARR impact estimates inside Action Playbook recommendations
- Reordered sidebar flow to executive-first operation mode with clearer helper guidance
- Added one-click reset to recommended defaults for faster leadership review setup

### 5) Portfolio packaging enhancements
- Added in-app evaluator walkthrough (2-minute leadership path)
- Added decisions-enabled framing on landing
- Expanded README with leadership review flow and progress snapshot

### 6) Operational readiness
- Added dev-side release readiness checklist: `V2_READINESS_CHECKLIST.md`
- Validated syntax and local startup smoke tests
- Verified keep-alive workflow execution on production default branch (`main`)

## Why It Matters

v2 focuses on executive comprehension and actionability. The product now communicates business value on first glance and provides a clear path from analytics to owner-level execution decisions.

## Validation Summary

- Python syntax checks: pass (`py_compile` for `app.py` and `data_generator.py`)
- Streamlit local smoke test: pass (HTTP 200)
- VS Code diagnostics for app/docs: no critical errors
- Data-logic sanity checks: pass (single/range date filtering and view-mode subset behavior)
- Keep-alive workflow: latest successful scheduled run confirmed on `main`

## Upgrade Notes

- Branching model remains release-first:
  - `main`: stable releases only
  - `dev`: active development line
- Suggested tag when releasing: `v2.0.0` on `main`

## Suggested Release PR Title

`Release v2.0.0: Executive UX, decision workflows, and portfolio packaging`

## Suggested Release PR Description (Short)

This PR promotes v2 from `dev` to `main` with executive-first UX, action-oriented analytics flow, chart consistency upgrades, and complete portfolio framing updates.
