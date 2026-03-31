# v2.1.0 Release Notes

Released: 2026-03-31  
Tag: v2.1.0  
Branch: main

## Overview

v2.1.0 expands the project into a more execution-ready revenue intelligence operating layer with stronger opportunity lifecycle realism, owner-level pipeline hygiene actions, and repeatable QA automation.

## Highlights

- Added realistic opportunity lifecycle states across Open, Closed Won, and Closed Lost
- Introduced as-of-date pipeline slicing for consistent open/closed analytics behavior
- Expanded pipeline diagnostics with owner hygiene, SLA breach tracking, and weekly cleanup quotas
- Added export packet metadata (packet ID, filter context, generation timestamp) for leadership traceability
- Added reusable QA smoke suite for data contracts and interaction validation
- Added CI workflow to run smoke checks on push and pull request
- Removed Streamlit width deprecations by migrating to the current width API

## What Changed

### Pipeline and Lifecycle Model

- Added open/closed helper slices and lifecycle-aware counts
- Added closed-lost reason diagnostics and quarterly trend analysis (count and share)
- Added owner-level backlog aging signals and cleanup planning exports

### Reliability and QA

- Fixed runtime priority-helper name collision discovered during interaction testing
- Added `qa_smoke.py` to validate core data invariants and Streamlit interaction flow
- Added `.github/workflows/qa-smoke.yml` for automated smoke checks in CI

### UX and Documentation

- Updated README to lead with executive walkthrough and launch path
- Clarified release and branch workflow documentation

## Validation Summary

- Smoke suite: pass (12/12)
- App runtime interaction checks: pass
- CI QA workflow on release commit: successful
- Syntax checks for core Python files: pass

## Compatibility and Upgrade Notes

- No breaking API changes
- Local run flow unchanged (`pip install -r requirements.txt`, `streamlit run app.py`)
- QA command available: `python qa_smoke.py`

## GitHub Release Title

v2.1.0 - Lifecycle hardening and QA automation
