import json
import sys
from dataclasses import dataclass
from typing import List

import pandas as pd
from streamlit.testing.v1 import AppTest

from data_generator import generate_forecast, generate_saas_data


@dataclass
class CheckResult:
    name: str
    passed: bool
    detail: str = ""


def run_data_checks() -> List[CheckResult]:
    leads_df, customers_df = generate_saas_data(
        start_date="2024-01-01",
        end_date="2025-12-31",
        monthly_leads=400,
    )

    checks: List[CheckResult] = []

    no_opp_ok = (
        leads_df.loc[~leads_df["is_opp"], "opp_status"] == "No Opportunity"
    ).all()
    checks.append(CheckResult("no_opportunity_status", bool(no_opp_ok)))

    won_scope = leads_df[leads_df["is_won"] == True]
    won_ok = (
        (won_scope["is_closed"] == True).all()
        and (won_scope["opp_status"] == "Closed Won").all()
        and won_scope["won_date"].notna().all()
    )
    checks.append(CheckResult("won_lifecycle_contract", bool(won_ok)))

    lost_scope = leads_df[leads_df["is_lost"] == True]
    lost_ok = (
        (lost_scope["is_closed"] == True).all()
        and (lost_scope["opp_status"] == "Closed Lost").all()
        and lost_scope["lost_date"].notna().all()
    )
    checks.append(CheckResult("lost_lifecycle_contract", bool(lost_ok)))

    open_scope = leads_df[(leads_df["is_opp"] == True) & (leads_df["is_closed"] == False)]
    open_ok = (
        (open_scope["opp_status"] == "Open").all()
        and open_scope["opp_close_date"].isna().all()
    )
    checks.append(CheckResult("open_lifecycle_contract", bool(open_ok)))

    customers_end = pd.to_datetime("2025-12-31")
    customer_start_ok = pd.to_datetime(customers_df["start_date"]).le(customers_end).all()
    checks.append(CheckResult("customer_start_within_window", bool(customer_start_ok)))

    forecast_df = generate_forecast(customers_df, months_forward=6)
    expected_months = list(range(6))
    months_ok = forecast_df["month"].tolist() == expected_months
    non_negative_ok = (forecast_df[["projected_arr", "projected_churn", "projected_expansion"]] >= 0).all().all()
    checks.append(CheckResult("forecast_month_index", bool(months_ok)))
    checks.append(CheckResult("forecast_non_negative", bool(non_negative_ok)))

    return checks


def run_app_checks() -> List[CheckResult]:
    checks: List[CheckResult] = []

    at = AppTest.from_file("app.py")
    at.run(timeout=30)
    checks.append(CheckResult("app_baseline_load", not bool(at.exception), str(at.exception or "")))
    checks.append(CheckResult("app_tabs_present", len(at.tabs) >= 4, f"tabs={len(at.tabs)}"))

    if at.radio:
        at.radio[0].set_value("At-Risk Focus")
        at.run(timeout=30)
        checks.append(CheckResult("app_at_risk_mode_switch", not bool(at.exception), str(at.exception or "")))

        at.radio[0].set_value("Expansion Focus")
        at.run(timeout=30)
        checks.append(CheckResult("app_expansion_mode_switch", not bool(at.exception), str(at.exception or "")))

    at_filters = AppTest.from_file("app.py")
    at_filters.run(timeout=30)
    if at_filters.multiselect:
        if len(at_filters.multiselect) > 0:
            at_filters.multiselect[0].set_value([])
        if len(at_filters.multiselect) > 1:
            at_filters.multiselect[1].set_value([])
        at_filters.run(timeout=30)
    checks.append(
        CheckResult(
            "app_empty_filter_resilience",
            not bool(at_filters.exception),
            str(at_filters.exception or ""),
        )
    )

    return checks


def main() -> int:
    all_checks = run_app_checks() + run_data_checks()
    failed = [check for check in all_checks if not check.passed]

    summary = {
        "pass": len(all_checks) - len(failed),
        "total": len(all_checks),
        "failed": [
            {"name": check.name, "detail": check.detail}
            for check in failed
        ],
    }
    print(json.dumps(summary, indent=2))

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
