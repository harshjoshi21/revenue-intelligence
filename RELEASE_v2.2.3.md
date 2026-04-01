# v2.2.3 Release Notes

Released: 2026-03-31  
Tag: v2.2.3  
Branch: main

## Overview

v2.2.3 is a decision-governance and usability release focused on making Action Playbook recommendations realistic for executive operations. The playbook now stays anchored to a full-business baseline while still allowing exploratory filters and view modes in the rest of the dashboard.

## Highlights

- Action Playbook recommendations are now fixed to a business-wide baseline (all dates, channels, and segments)
- Filter and Executive View Mode changes no longer re-rank Action Playbook priorities
- Sidebar defaults now load with all channels and all segments selected for a full operating picture
- Playbook cards now maintain uniform sizing with safe internal scrolling for long content
- Decision-scope wording and execution-note copy were tightened for clarity and consistency

## What Changed

### Action Playbook Governance Model

- Updated Playbook scoring to use full-dataset operating metrics (`leads_df`, `customers_df`) rather than filtered/focus slices
- Added explicit in-tab decision-scope callout clarifying that recommendations are anchored to the business-wide baseline
- Removed dependence on filter/lens changes for playbook ranking output

### Default Filter Behavior

- Updated default channel selection to all available channels
- Updated default segment selection to all available segments
- Updated reset action to "Reset to business-wide defaults" for consistent operating context

### Playbook Card UX

- Standardized all three action cards to a consistent size profile
- Added internal vertical scroll handling to prevent layout breakage when card text is long
- Styled scrollbars to stay visually subtle and reduce distraction when sidebar width compresses content

### Messaging Refinement

- Improved Decision Scope and Execution Notes wording to align with the fixed-baseline decision model
- Kept projected-impact language explicitly anchored to business-wide context

## Validation Summary

- App diagnostics: no errors in `app.py`
- Python compile checks: pass
- Smoke suite (`qa_smoke.py`): pass (12/12)

## Compatibility and Upgrade Notes

- No breaking API changes
- Local run flow unchanged (`pip install -r requirements.txt`, `streamlit run app.py`)
- QA command unchanged (`python qa_smoke.py`)

## GitHub Release Title

v2.2.3 - Business-wide Action Playbook baseline and UX polish
