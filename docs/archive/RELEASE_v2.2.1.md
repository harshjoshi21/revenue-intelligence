# v2.2.1 Release Notes

Released: 2026-03-31  
Tag: v2.2.1  
Branch: main

## Overview

v2.2.1 is an execution-clarity release focused on the Pipeline Hygiene Execution Control Panel. This update resolves SLA/priority interpretation confusion by aligning sorting, visual emphasis, and summary messaging to a consistent urgency model.

## Highlights

- Reordered owner table to sort by SLA Status first, then Priority and cleanup severity
- Reordered table columns so Priority is second-last and SLA Status is last for cleaner scan flow
- Aligned top SLA signal and packet quotas to breached-owner scope to avoid count mismatches
- Standardized row highlighting to SLA status only (Critical Breach and Watch Breach)
- Added explicit in-panel definitions for SLA Status and Priority logic thresholds
- Removed redundant standup packet narrative line and simplified export caption placement

## What Changed

### Execution Control Panel (Pipeline Hygiene by Owner)

- Added SLA rank mapping and SLA-first sorting for owner rows
- Updated owner table display order to reduce visual confusion in urgency interpretation
- Corrected signal text so breach quota and owner counts use the same breached-owner denominator
- Kept escalation packet line and conditional priority-difference note for edge-case clarity

### UX and Messaging Cleanup

- Added compact logic-definition callout under the owner table:
  - SLA Status threshold rules
  - Priority threshold rules
  - Sorting behavior summary
- Removed redundant standup packet prose from on-screen panel while preserving CSV exports
- Moved export packet note out of an uneven button column layout to avoid blank-space artifacts

### Documentation and Release Hygiene

- Promoted v2.2.1 as the latest stable release in README
- Archived v2.2.0 release note and kept only latest release note at repository root
- Updated release-documentation links to preserve chronological history in `docs/archive`

## Validation Summary

- App diagnostics: no errors in `app.py`
- Python compile checks: pass
- Smoke suite (`qa_smoke.py`): pass (12/12)
- Branch sync verification: dev and main aligned post-release promotion

## Compatibility and Upgrade Notes

- No breaking API changes
- Local run flow unchanged (`pip install -r requirements.txt`, `streamlit run app.py`)
- QA command unchanged (`python qa_smoke.py`)

## GitHub Release Title

v2.2.1 - Execution panel clarity and SLA-priority alignment
