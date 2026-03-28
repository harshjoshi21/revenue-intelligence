# V2 Readiness Checklist (dev branch)

Use this checklist before opening any `dev -> main` release PR.

## 1. Product and UX Validation

- [ ] Landing screen clearly answers: what this is, what to do, what it conveys, why useful
- [ ] Executive Snapshot, Top Insights, and Benchmark Lens are coherent
- [ ] Action Playbook recommendations align with filtered data
- [ ] Glossary and view mode controls are understandable to non-technical stakeholders
- [ ] Mobile and desktop layouts remain readable

## 2. Technical Validation

- [ ] `python -m py_compile app.py data_generator.py` passes
- [ ] Streamlit startup smoke test returns HTTP 200
- [ ] No critical errors in VS Code Problems for app files
- [ ] Keep-alive workflow still succeeds on latest commit

## 3. Data and Logic Validation

- [ ] Date range filters work for both single date and date range
- [ ] Executive View Mode (All / At-Risk / Expansion) changes context as intended
- [ ] Funnel calculations and what-if logic are consistent with displayed metrics
- [ ] Forecast assumptions and outputs remain numerically sensible

## 4. Documentation Validation

- [ ] README reflects current tab names and interaction flow
- [ ] README explains audience, decisions enabled, and 2-minute evaluator path
- [ ] Versioning workflow in README matches current branch strategy

## 5. Release Gate (Do not run until ready)

- [ ] `dev` branch contains all intended v2 scope commits
- [ ] Optional pre-release tag created on `dev` (e.g., `v2.0.0-rc.X`)
- [ ] Draft PR from `dev` to `main` prepared with validation notes
- [ ] Stakeholder review completed
- [ ] Final release tag planned on `main` (e.g., `v2.0.0`)

---

## Current Snapshot (auto-updated manually)

- Branch strategy: `main` stable releases, `dev` active development
- Stable baseline tag on `main`: `v1.0.0`
- Current dev milestone tag: `v2.0.0-rc.1`
