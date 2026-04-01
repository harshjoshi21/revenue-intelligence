# v2.2.0 Release Notes

Released: 2026-03-31  
Tag: v2.2.0  
Branch: main

## Overview

v2.2.0 advances the app from a strong analytics dashboard into a more guided executive operating experience. This release emphasizes scenario comprehension, negative-signal visibility, and clearer action routing from top-level insights to root-cause diagnostics.

## Highlights

- Refined executive pre-tab flow so leadership can frame decisions faster
- Expanded baseline operating pulse with stale-pipeline and closed-lost visibility
- Added adaptive benchmark behavior based on executive view mode
- Standardized negative metric semantics using inverse/red emphasis
- Added filter-sensitive guidance with examples in key sections
- Elevated root-cause preview into a high-visibility callout with explicit drill path
- Improved readability of instructional callouts (example and next-step line breaks)
- Set Streamlit theme baseline to light for consistent presentation

## What Changed

### Executive Flow and Decision Layer

- Updated evaluator walkthrough and showcase framing to connect to execution governance
- Upgraded Top Insights with pipeline plus hygiene signal and closed-lost reason preview
- Added adaptive fourth Benchmark Lens card:
  - Expansion Rate in Expansion Focus
  - Pipeline Hygiene in other modes

### Pipeline and Root-Cause Clarity

- Added/extended benchmark signal logic for `pipeline_hygiene`
- Strengthened root-cause messaging from low-emphasis caption to explicit risk callout
- Added clear navigation guidance to Pipeline Risks -> Closed Outcome Diagnostics

### Visual and Interaction Semantics

- Applied professional visual refinements while keeping executive readability
- Ensured negative outcomes (closed-lost, at-risk, stale pipeline) are rendered with inverse/red semantics
- Added concise filter-sensitive disclaimers with scenario examples where users are expected to explore what-if context
- Improved callout text layout for scannability by moving example/next-step details onto separate lines

### Documentation and Versioning

- Updated README release status to reflect stable v2.2.0 and next development target
- Added release notes for v2.2.0 and backfilled v2.1.1 release summary for continuity
- Aligned README and in-app methodology summary with planning-led, from-scratch synthetic data generation and AI-assisted workflow context

## Validation Summary

- App diagnostics: no errors in `app.py`
- Python compile checks: pass
- Smoke suite (`qa_smoke.py`): pass (12/12)
- Release docs/metadata alignment: pass (README + release notes synchronized)

## Compatibility and Upgrade Notes

- No breaking API changes
- Local run flow unchanged (`pip install -r requirements.txt`, `streamlit run app.py`)
- QA command unchanged (`python qa_smoke.py`)

## GitHub Release Title

v2.2.0 - Executive guidance, filter clarity, and root-cause visibility
