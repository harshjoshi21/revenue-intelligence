# v2.0.0 Release Notes (Draft)

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

### 3) Visual system upgrade
- Introduced shared executive chart palette and style helpers
- Standardized chart spacing, legends, axes, and readability patterns
- Improved consistency across funnel, risk, expansion, and forecast visuals

### 4) Portfolio packaging enhancements
- Added in-app evaluator walkthrough (2-minute leadership path)
- Added decisions-enabled framing on landing
- Expanded README with leadership review flow and progress snapshot

### 5) Operational readiness
- Added dev-side release readiness checklist: `V2_READINESS_CHECKLIST.md`
- Validated syntax and local startup smoke tests
- Verified keep-alive workflow execution on latest `dev` state

## Why It Matters

v2 focuses on executive comprehension and actionability. The product now communicates business value on first glance and provides a clear path from analytics to owner-level execution decisions.

## Validation Summary

- Python syntax checks: pass
- Streamlit local smoke test: pass (HTTP 200)
- Keep-alive workflow on `dev`: pass

## Upgrade Notes

- Branching model remains release-first:
  - `main`: stable releases only
  - `dev`: active development line
- Suggested tag when releasing: `v2.0.0` on `main`

## Suggested Release PR Title

`Release v2.0.0: Executive UX, decision workflows, and portfolio packaging`

## Suggested Release PR Description (Short)

This PR promotes v2 from `dev` to `main` with executive-first UX, action-oriented analytics flow, chart consistency upgrades, and complete portfolio framing updates.
