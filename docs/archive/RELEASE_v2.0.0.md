# v2.0.0 Release Notes

Released: 2026-03-29  
Tag: v2.0.0  
Branch: main

## Overview

v2.0.0 evolves this project into an executive-ready Customer Lifecycle Intelligence experience for Customer Success and Growth Analytics leaders.

## Highlights

- Brand refresh to Customer Lifecycle Intelligence with sharper leadership-facing narrative
- Executive-first landing experience with clearer intent, usage, and value framing
- Decision-oriented analytics flow across funnel, retention, expansion, and forecast
- Calibrated Action Playbook priorities with clearer benchmark alignment
- Improved playbook card readability and layout consistency
- Data-generation guardrails to prevent future-dated customer starts in the default analysis window

## What Changed

### Product and UX

- Updated hero branding and positioning language for CS and Growth Analytics
- Tightened top-section copy to reduce redundancy and improve executive readability
- Refined tab and section narratives to make action paths clearer

### Decision Logic and Actionability

- Unified KPI derivation for benchmark lens and action playbook consistency
- Improved churn action prioritization so benchmark drift is reflected in playbook urgency
- Updated playbook triggers and impact messaging for more coherent priority rationale

### Data Integrity

- Added date-window control in data generation so modeled wins beyond the configured end date are excluded
- Confirmed filter defaults now align with valid in-range data

### Documentation

- Updated README branding, positioning language, and landing summary copy
- Added/updated release-readiness and release-notes artifacts for v2 finalization

## Validation Summary

- Python syntax checks passed (`py_compile` for `app.py` and `data_generator.py`)
- Local UI/logic sanity checks completed during finalization
- No diagnostics errors in key edited files at release cut

## Compatibility and Upgrade Notes

- No breaking API changes
- Existing local setup remains the same (`pip install -r requirements.txt`, `streamlit run app.py`)

## Recommended GitHub Release Title

v2.0.0 - Customer Lifecycle Intelligence

## Suggested Short Release Description

This release upgrades the project to an executive-ready Customer Lifecycle Intelligence experience with clearer CS/Growth positioning, stronger decision workflows, calibrated playbook logic, and data-window integrity improvements.
