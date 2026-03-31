# v2.1.1 Release Notes

Released: 2026-03-31  
Tag: v2.1.1  
Branch: main

## Overview

v2.1.1 is an operational hardening release focused on deployment reliability and documentation hygiene.

## Highlights

- Stabilized Streamlit keep-alive behavior against URL normalization and redirect-loop failure modes
- Improved keep-alive probe logic for root and health endpoint availability checks
- Archived historical release-process artifacts for cleaner public repository structure
- Promoted release documentation alignment on main

## What Changed

### Reliability and Operations

- Normalized keep-alive base URL handling
- Removed unstable redirect-follow probe behavior that caused false negatives
- Kept scheduled health checks focused on deterministic availability outcomes

### Documentation and Repository Hygiene

- Moved historical process docs into `docs/archive`
- Kept current release-facing docs in the project root for easier reviewer access

## Validation Summary

- Keep-alive workflow behavior validated after URL normalization updates
- Repository documentation structure verified after archive moves

## Compatibility and Upgrade Notes

- No breaking API changes
- Local run flow unchanged (`pip install -r requirements.txt`, `streamlit run app.py`)
- QA command unchanged (`python qa_smoke.py`)

## GitHub Release Title

v2.1.1 - Keep-alive reliability and docs hygiene
