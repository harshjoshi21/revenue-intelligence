# v2.2.2 Release Notes

Released: 2026-03-31  
Tag: v2.2.2  
Branch: main

## Overview

v2.2.2 is a benchmark-consistency release focused on churn interpretation clarity. This update aligns churn threshold logic, benchmark card framing, and playbook language so executive users see one consistent decision model across the app.

## Highlights

- Updated churn benchmark policy to Healthy: <5% and Watch: 5-7%
- Aligned churn benchmark signal logic to trigger Action only above 7%
- Kept churn benchmark and playbook trigger values at 2-decimal precision for interpretation accuracy
- Updated release documentation to promote v2.2.2 as latest stable and archive v2.2.1

## What Changed

### Benchmark Lens and Signal Logic

- Updated benchmark label for Churn Rate to: Healthy: <5% (Watch: 5-7%)
- Updated `get_benchmark_signal("churn", value)` logic:
  - Healthy when churn is below 5%
  - Watch when churn is between 5% and 7% (inclusive)
  - Action when churn is above 7%
- Refined churn signal note text to reflect the new threshold model

### Action Playbook Consistency

- Preserved two-decimal churn formatting in trigger narratives to avoid rounding ambiguity near threshold boundaries
- Ensured playbook wording remains consistent with the benchmark ceiling model

### Documentation and Release Hygiene

- Promoted v2.2.2 as latest stable release in `README.md`
- Set next development target to v2.2.3 on `dev`
- Archived v2.2.1 release note under `docs/archive`
- Kept only the latest release note at repository root

## Validation Summary

- App diagnostics: no errors in `app.py`
- Python compile checks: pass
- Smoke suite (`qa_smoke.py`): pass (12/12)

## Compatibility and Upgrade Notes

- No breaking API changes
- Local run flow unchanged (`pip install -r requirements.txt`, `streamlit run app.py`)
- QA command unchanged (`python qa_smoke.py`)

## GitHub Release Title

v2.2.2 - Churn benchmark alignment and release-doc updates
