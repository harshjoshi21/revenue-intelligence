import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from data_generator import generate_saas_data, generate_forecast
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title="Customer Lifecycle Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    :root {
        --navy-900: #10233d;
        --navy-700: #1f3b5c;
        --gold-500: #d4a24c;
        --slate-50: #f6f8fb;
        --slate-200: #d6dce5;
        --ink-900: #1f2937;
    }
    .hero-wrap {
        background: #ffffff;
        color: var(--ink-900);
        padding: 20px 24px;
        border-radius: 14px;
        margin-bottom: 16px;
        border: 1px solid transparent;
        box-shadow: 0 8px 20px rgba(16, 35, 61, 0.06);
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        text-align: left;
    }
    .hero-kicker {
        display: inline-block;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #8a641b;
        background: #fef4dc;
        border: 1px solid #f3ddb4;
        border-radius: 999px;
        padding: 4px 10px;
        margin-bottom: 10px;
    }
    .hero-stack {
        margin: 0 !important;
        padding: 0 !important;
        display: grid;
        row-gap: 6px;
        width: 100%;
        text-align: left;
    }
    .hero-title-line {
        display: block;
        font-size: 2.25rem;
        line-height: 1.15;
        margin: 0 !important;
        padding: 0 !important;
        font-weight: 700;
        color: var(--navy-900);
        text-align: left;
        width: 100%;
        transform: translateX(-1px);
    }
    .hero-subtitle-line {
        display: block;
        font-size: 1rem;
        margin: 0 !important;
        padding: 0 !important;
        max-width: 900px;
        color: #334155;
        line-height: 1.3;
        text-align: left;
        width: 100%;
    }
    .hero-byline-line {
        display: block;
        font-size: 0.87rem;
        margin: 4px 0 0 0 !important;
        padding: 0 !important;
        color: #475569;
        font-weight: 600;
        line-height: 1.25;
        text-align: left;
        width: 100%;
    }
    .hero-byline-line a {
        color: #475569;
        text-decoration: underline;
        text-underline-offset: 2px;
        font-weight: 700;
    }
    .profile-panel {
        background: #fff;
        border: 1px solid var(--slate-200);
        border-left: 5px solid var(--gold-500);
        border-radius: 12px;
        padding: 14px 16px;
        margin: 0 0 10px 0;
        color: var(--ink-900);
    }
    .profile-label {
        font-size: 0.72rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #64748b;
        font-weight: 700;
        margin-bottom: 6px;
    }
    .profile-title {
        font-size: 1rem;
        color: var(--navy-900);
        font-weight: 700;
        margin-bottom: 4px;
    }
    .profile-text {
        font-size: 0.92rem;
        color: #334155;
        margin: 0;
    }
    .pill {
        display: inline-block;
        background: var(--slate-50);
        border: 1px solid var(--slate-200);
        border-radius: 999px;
        padding: 4px 10px;
        margin: 4px 6px 0 0;
        font-size: 0.78rem;
        color: #334155;
        font-weight: 600;
    }
    .info-card {
        background: #fff;
        border: 1px solid var(--slate-200);
        border-left: 4px solid var(--gold-500);
        border-radius: 10px;
        padding: 16px 16px 22px;
        height: 176px;
        margin-bottom: 12px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    .info-card h4 {
        margin: 0 0 8px 0;
        color: var(--navy-900);
        font-size: 1rem;
    }
    .info-card p {
        margin: 0;
        color: #334155;
        font-size: 0.9rem;
        line-height: 1.35;
        flex: 1;
    }
    .insight-card {
        background: #fff;
        border: 1px solid var(--slate-200);
        border-radius: 10px;
        padding: 12px;
        height: 118px;
        margin-bottom: 12px;
        display: flex;
        flex-direction: column;
    }
    .insight-card h5 {
        margin: 0 0 6px 0;
        color: var(--navy-900);
        font-size: 0.96rem;
    }
    .insight-card p {
        margin: 0;
        color: #334155;
        font-size: 0.88rem;
        line-height: 1.35;
        flex: 1;
    }
    .section-note {
        font-size: 0.86rem;
        color: #475569;
        margin-top: -4px;
        margin-bottom: 8px;
    }
    .metric-card {
        padding: 20px;
        border-radius: 8px;
        background-color: #f0f2f6;
        margin: 10px 0;
    }
    .at-risk {
        background-color: #ffe6e6;
        border-left: 4px solid #ff4444;
    }
    .healthy {
        background-color: #e6ffe6;
        border-left: 4px solid #44ff44;
    }
    .benchmark-card {
        background: #fff;
        border: 1px solid var(--slate-200);
        border-radius: 10px;
        padding: 12px;
        min-height: 122px;
    }
    .benchmark-title {
        margin: 0 0 6px 0;
        color: var(--navy-900);
        font-size: 0.9rem;
        font-weight: 700;
    }
    .benchmark-range {
        margin: 0;
        color: #64748b;
        font-size: 0.78rem;
    }
    .benchmark-value {
        margin: 8px 0 6px 0;
        color: #1f2937;
        font-size: 1rem;
        font-weight: 700;
    }
    .signal-chip {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 700;
        margin-bottom: 6px;
    }
    .signal-healthy {
        background: #dcfce7;
        color: #166534;
    }
    .signal-watch {
        background: #fef3c7;
        color: #92400e;
    }
    .signal-action {
        background: #fee2e2;
        color: #991b1b;
    }
    .benchmark-note {
        margin: 0;
        color: #475569;
        font-size: 0.8rem;
    }
    .section-header-wrap {
        display: flex;
        align-items: center;
        gap: 12px;
        border-bottom: 2px solid rgba(212, 162, 76, 0.45);
        padding-bottom: 10px;
        margin-bottom: 12px;
    }
    .section-header-icon {
        font-size: 1.35rem;
        line-height: 1;
        margin-top: 0;
    }
    .section-header-title {
        margin: 0;
        color: var(--navy-900);
        font-size: 1.34rem;
        font-weight: 700;
    }
    .section-header-desc {
        margin: 4px 0 0 0;
        color: #475569;
        font-size: 0.9rem;
    }
    .context-callout {
        background: #fff8e8;
        border-left: 4px solid var(--gold-500);
        border-radius: 8px;
        padding: 12px;
        margin: 0 0 14px 0;
        color: #4b5563;
        font-size: 0.86rem;
    }
    .table-context {
        margin: 2px 0 8px 0;
        color: #64748b;
        font-size: 0.82rem;
    }
    .quick-win-callout {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-left: 4px solid #16a34a;
        border-radius: 10px;
        padding: 12px 14px;
        margin-top: 16px;
        margin-bottom: 14px;
        color: #14532d;
    }
    .quick-win-title {
        margin: 0;
        font-size: 0.95rem;
        font-weight: 700;
    }
    .quick-win-move {
        margin: 8px 0 0 0;
        font-size: 0.88rem;
        color: #166534;
    }
    .playbook-card {
        background: #ffffff;
        border: 1px solid var(--slate-200);
        border-radius: 12px;
        padding: 18px 18px 10px;
        height: 410px;
        display: flex;
        flex-direction: column;
        margin-bottom: 14px;
        overflow: visible;
    }
    .playbook-critical {
        border-left: 5px solid #c0392b;
        background: #fff6f5;
    }
    .playbook-high {
        border-left: 5px solid #d97706;
        background: #fffbeb;
    }
    .playbook-monitor {
        border-left: 5px solid #2563eb;
        background: #eff6ff;
    }
    .playbook-priority {
        margin: 0;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }
    .playbook-critical .playbook-priority {
        color: #7f1d1d;
    }
    .playbook-high .playbook-priority {
        color: #7c2d12;
    }
    .playbook-monitor .playbook-priority {
        color: #1d4ed8;
    }
    .playbook-signal {
        margin: 8px 0 10px 0;
        font-size: 1rem;
        line-height: 1.3;
        color: #111827;
        font-weight: 700;
    }
    .playbook-line {
        margin: 6px 0;
        color: #374151;
        font-size: 0.86rem;
        line-height: 1.4;
    }
    .playbook-impact {
        margin-top: 8px;
        padding-top: 8px;
        font-size: 0.9rem;
        line-height: 1.35;
        font-weight: 700;
    }
    .playbook-critical .playbook-impact {
        color: #991b1b;
    }
    .playbook-high .playbook-impact {
        color: #92400e;
    }
    .playbook-monitor .playbook-impact {
        color: #1e40af;
    }
    div[data-baseweb="tab-list"] {
        gap: 8px;
        padding-bottom: 10px;
        margin-bottom: 8px;
    }
    button[data-baseweb="tab"] {
        border: 1px solid var(--slate-200) !important;
        border-radius: 10px 10px 0 0 !important;
        background: #f8fafc !important;
        padding: 10px 14px !important;
    }
    button[data-baseweb="tab"] p {
        font-size: 1.02rem !important;
        font-weight: 700 !important;
        color: var(--navy-900) !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        background: #e8f0fb !important;
        border-color: #9bb6d8 !important;
        box-shadow: inset 0 -2px 0 var(--gold-500);
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    leads_df, customers_df = generate_saas_data()
    forecast_df = generate_forecast(customers_df)
    return leads_df, customers_df, forecast_df

leads_df, customers_df, forecast_df = load_data()

# Phase 3: shared visual system for charts
PRIMARY_BLUE = "#1f4e79"
SECONDARY_BLUE = "#3a77b2"
RISK_RED = "#c0392b"
HEALTH_GREEN = "#1f8f6a"
WARNING_AMBER = "#d4a24c"
NEUTRAL_SLATE = "#64748b"


def apply_chart_theme(fig, title, xaxis_title=None, yaxis_title=None, height=400):
    fig.update_layout(
        title=title,
        height=height,
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#1f2937"),
        margin=dict(l=10, r=10, t=60, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    if xaxis_title is not None:
        fig.update_xaxes(title=xaxis_title, gridcolor="#e5e7eb")
    if yaxis_title is not None:
        fig.update_yaxes(title=yaxis_title, gridcolor="#e5e7eb")


def format_currency(value, decimals=1):
    """Format currency consistently as $, k, or M across the dashboard."""
    if pd.isna(value):
        return "$0"

    amount = float(value)
    absolute = abs(amount)

    if absolute >= 1_000_000:
        return f"${amount / 1_000_000:.{decimals}f}M"
    if absolute >= 1_000:
        return f"${amount / 1_000:.{decimals}f}k"
    return f"${amount:,.0f}"


def get_benchmark_signal(metric_name, value):
    """Return benchmark signal label, style class, and interpretation text."""
    metric = metric_name.lower()

    if metric == "churn":
        if value <= 7:
            return "Healthy", "signal-healthy", "Retention baseline is within expected range."
        if value <= 10:
            return "Watch", "signal-watch", "Retention is drifting and needs weekly review."
        return "Action", "signal-action", "Escalate intervention plan for at-risk accounts."

    if metric == "nrr":
        if value >= 110:
            return "Healthy", "signal-healthy", "Expansion and retention are compounding well."
        if value >= 105:
            return "Watch", "signal-watch", "Growth is stable but upside is limited."
        return "Action", "signal-action", "Prioritize churn reduction and expansion motion."

    if metric == "sql_to_won":
        if value >= 25:
            return "Healthy", "signal-healthy", "Late-stage conversion is at target."
        if value >= 20:
            return "Watch", "signal-watch", "Conversion is borderline and needs stage audit."
        return "Action", "signal-action", "Immediate funnel-stage intervention required."

    if metric == "expansion":
        if value >= 12:
            return "Healthy", "signal-healthy", "Expansion contribution supports NRR goals."
        if value >= 10:
            return "Watch", "signal-watch", "Expansion is present but below ambition."
        return "Action", "signal-action", "Trigger focused upsell campaign this cycle."

    return "Watch", "signal-watch", "Monitor trend and reassess next review cycle."


def render_benchmark_card(title, benchmark_range, current_value_text, signal_label, signal_class, note_text):
    st.markdown(
        f"""
        <div class='benchmark-card'>
            <p class='benchmark-title'>{title}</p>
            <p class='benchmark-range'>Benchmark: {benchmark_range}</p>
            <p class='benchmark-value'>Current: {current_value_text}</p>
            <span class='signal-chip {signal_class}'>{signal_label}</span>
            <p class='benchmark-note'>{note_text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def derive_operating_metrics(leads_view, customers_view):
    """Derive one canonical KPI payload for benchmark lens, quick win, and playbook."""
    active_customers = customers_view[customers_view['is_churned'] == 0]
    at_risk_customers = customers_view[customers_view['churn_risk'] > 70]

    sql_count = int(leads_view['is_sql'].sum())
    won_count = int(leads_view['is_won'].sum())
    sql_to_won = (won_count / sql_count * 100) if sql_count > 0 else 0

    total_customers = len(customers_view)
    at_risk_count = len(at_risk_customers)
    at_risk_pct = (at_risk_count / total_customers * 100) if total_customers > 0 else 0

    total_arr = customers_view['arr'].sum()
    active_arr = active_customers['arr'].sum()
    current_expansion = active_customers['expansion_arr'].sum()
    expansion_pct = (customers_view['expansion_arr'].sum() / total_arr * 100) if total_arr > 0 else 0

    churn_rate = customers_view['is_churned'].mean() * 100 if total_customers > 0 else 0
    current_nrr = (active_customers['nrr_contribution'].mean() * 100) if len(active_customers) > 0 else 0

    avg_won_arr = leads_view[leads_view['is_won'] == 1]['arr'].mean() if won_count > 0 else np.nan
    avg_won_arr = float(avg_won_arr) if not pd.isna(avg_won_arr) and avg_won_arr > 0 else 75_000

    expansion_ready_arr = active_customers[active_customers['churn_risk'] <= 70]['arr'].sum()

    has_customer_data = total_customers > 0
    has_pipeline_data = sql_count > 0
    has_expansion_data = active_arr > 0 and total_arr > 0

    return {
        'sql_count': sql_count,
        'won_count': won_count,
        'sql_to_won': sql_to_won,
        'total_customers': total_customers,
        'at_risk_count': at_risk_count,
        'at_risk_pct': at_risk_pct,
        'at_risk_arr': at_risk_customers['arr'].sum(),
        'churn_rate': churn_rate,
        'current_nrr': current_nrr,
        'total_arr': total_arr,
        'active_arr': active_arr,
        'current_expansion': current_expansion,
        'expansion_pct': expansion_pct,
        'avg_won_arr': avg_won_arr,
        'expansion_ready_arr': expansion_ready_arr,
        'has_customer_data': has_customer_data,
        'has_pipeline_data': has_pipeline_data,
        'has_expansion_data': has_expansion_data
    }


def get_action_priority(action_key, metrics):
    """Map each action to Critical, High, or Monitor based on directional thresholds."""
    if action_key == 'churn':
        if not metrics.get('has_customer_data', False):
            return 'Monitor'

        if metrics['at_risk_pct'] > 20:
            at_risk_priority = 'Critical'
        elif metrics['at_risk_pct'] > 15:
            at_risk_priority = 'High'
        else:
            at_risk_priority = 'Monitor'

        churn_rate = metrics.get('churn_rate', 0)
        if churn_rate > 10:
            churn_rate_priority = 'Critical'
        elif churn_rate > 7:
            churn_rate_priority = 'High'
        else:
            churn_rate_priority = 'Monitor'

        priority_rank = {'Monitor': 0, 'High': 1, 'Critical': 2}
        return at_risk_priority if priority_rank[at_risk_priority] >= priority_rank[churn_rate_priority] else churn_rate_priority

    if action_key == 'pipeline':
        if not metrics.get('has_pipeline_data', False):
            return 'Monitor'
        if metrics['sql_to_won'] < 20:
            return 'Critical'
        if metrics['sql_to_won'] < 25:
            return 'High'
        return 'Monitor'

    if action_key == 'expansion':
        if not metrics.get('has_expansion_data', False):
            return 'Monitor'
        if metrics['expansion_pct'] < 10:
            return 'Critical'
        if metrics['expansion_pct'] < 12:
            return 'High'
        return 'Monitor'

    return 'Monitor'


def calculate_action_impacts(leads_view, customers_view, metrics=None):
    """Estimate intervention upside while separating maintain-state guidance from urgent actions."""
    if metrics is None:
        metrics = derive_operating_metrics(leads_view, customers_view)

    churn_priority = get_action_priority('churn', metrics)
    pipeline_priority = get_action_priority('pipeline', metrics)
    expansion_priority = get_action_priority('expansion', metrics)

    if churn_priority == 'Monitor':
        retention_value = 0
        if not metrics.get('has_customer_data', False):
            retention_label = "Insufficient customer sample in current filters to estimate churn exposure reliably."
            retention_quick_win = "Broaden date or segment filters to restore a representative customer health baseline."
        else:
            retention_label = (
                "Retention is operating within control bands. Maintain weekly risk reviews and preserve "
                "proactive success coverage."
            )
            retention_quick_win = "Maintain current retention cadence and monitor emerging high-risk accounts weekly."
    else:
        retention_value = metrics['at_risk_arr'] * 0.50
        if retention_value > 0:
            retention_label = (
                f"Protect up to {format_currency(retention_value, decimals=2)} ARR if 50% of at-risk accounts are retained."
            )
        else:
            retention_label = (
                "Observed churn is above benchmark and requires root-cause intervention, even though the current "
                "high-risk ARR pool is limited in this filter view."
            )
        retention_quick_win = "Start a 48-hour rescue motion for highest-risk accounts and confirm root causes."

    if pipeline_priority == 'Monitor':
        pipeline_value = 0
        if not metrics.get('has_pipeline_data', False):
            pipeline_label = "Insufficient SQL volume in current filters to estimate conversion pressure reliably."
            pipeline_quick_win = "Broaden date or channel scope to recover enough SQL volume for a reliable conversion read."
        else:
            pipeline_label = (
                "Pipeline conversion is at or above the 25% aspirational target. Maintain stage discipline and "
                "run light optimization experiments."
            )
            pipeline_quick_win = "Maintain stage handoff discipline and review conversion quality in weekly ops cadence."
    else:
        target_won_count = int(np.ceil(metrics['sql_count'] * 0.25))
        additional_wins_needed = max(target_won_count - metrics['won_count'], 0)
        pipeline_value = additional_wins_needed * metrics['avg_won_arr']
        pipeline_label = (
            f"Add up to {format_currency(pipeline_value, decimals=2)} ARR by lifting SQL to Won to 25% "
            f"(using current average won ARR of {format_currency(metrics['avg_won_arr'], decimals=1)})."
        )
        pipeline_quick_win = "Run a 72-hour stage handoff audit and recover stalled SQL follow-through this week."

    target_expansion = metrics['active_arr'] * 0.12
    if expansion_priority == 'Monitor':
        if not metrics.get('has_expansion_data', False):
            expansion_value = 0
            expansion_label = "Insufficient active ARR context in current filters to estimate expansion opportunity reliably."
            expansion_quick_win = "Broaden date or segment scope to recover enough active ARR for expansion analysis."
        else:
            expansion_value = metrics['expansion_ready_arr'] * 0.03
            expansion_target_phrase = "above 12%" if metrics['expansion_pct'] > 12 else "at 12%"
            if expansion_value > 0:
                expansion_label = (
                    f"Expansion is {expansion_target_phrase}. Maintain momentum and optionally unlock about "
                    f"{format_currency(expansion_value, decimals=2)} ARR through next-step upsell on healthy accounts."
                )
            else:
                expansion_label = (
                    f"Expansion is {expansion_target_phrase}. Maintain current expansion motion and monitor for "
                    "new upsell-ready cohorts."
                )
            expansion_quick_win = "Maintain quarterly expansion planning and track top expansion-ready accounts."
    else:
        expansion_value = max(target_expansion - metrics['current_expansion'], 0)
        expansion_nrr_lift = (expansion_value / metrics['active_arr'] * 100) if metrics['active_arr'] > 0 else 0
        projected_nrr = metrics['current_nrr'] + expansion_nrr_lift
        expansion_label = (
            f"Capture up to {format_currency(expansion_value, decimals=2)} ARR by moving expansion to 12% "
            f"(potential NRR path: {projected_nrr:.1f}%)."
        )
        expansion_quick_win = "Prioritize top expansion-ready accounts and launch tailored upsell plays."

    impact_rows = [
        {
            'key': 'churn',
            'signal': 'High churn exposure',
            'priority': churn_priority,
            'impact_value': retention_value,
            'impact_label': retention_label,
            'quick_win': retention_quick_win,
            'quick_win_eligible': churn_priority != 'Monitor'
        },
        {
            'key': 'pipeline',
            'signal': 'Pipeline conversion pressure',
            'priority': pipeline_priority,
            'impact_value': pipeline_value,
            'impact_label': pipeline_label,
            'quick_win': pipeline_quick_win,
            'quick_win_eligible': pipeline_priority != 'Monitor'
        },
        {
            'key': 'expansion',
            'signal': 'Expansion underperformance',
            'priority': expansion_priority,
            'impact_value': expansion_value,
            'impact_label': expansion_label,
            'quick_win': expansion_quick_win,
            'quick_win_eligible': expansion_priority != 'Monitor'
        }
    ]

    quick_win_candidates = [
        row for row in impact_rows
        if row['quick_win_eligible'] and row['impact_value'] > 0
    ]
    quick_win = max(quick_win_candidates, key=lambda row: row['impact_value']) if quick_win_candidates else None
    return impact_rows, quick_win


def build_playbook_rows(metrics, impact_by_key):
    """Build playbook rows from canonical priority mapping."""
    churn_priority = get_action_priority('churn', metrics)
    churn_rate = metrics.get('churn_rate', 0)
    if not metrics.get('has_customer_data', False):
        churn_signal = 'Retention signal unavailable'
        churn_trigger = 'No customers in the current filter context.'
        churn_sla = 'Broaden filters before assigning retention owners'
    elif churn_priority == 'Critical':
        churn_signal = 'Retention at intervention level'
        churn_reasons = []
        if metrics['at_risk_pct'] > 20:
            churn_reasons.append(
                f"at-risk share {metrics['at_risk_pct']:.1f}% exceeds 20% "
                f"({metrics['at_risk_count']} of {metrics['total_customers']} accounts)"
            )
        if churn_rate > 10:
            churn_reasons.append(f"observed churn rate {churn_rate:.1f}% is above 10% action threshold")
        churn_trigger = " and ".join(churn_reasons) + "."
        churn_sla = 'Launch owner outreach within 48 hours'
    elif churn_priority == 'High':
        churn_signal = 'Retention gap requiring action'
        churn_reasons = []
        if metrics['at_risk_pct'] > 15:
            churn_reasons.append(
                f"at-risk share {metrics['at_risk_pct']:.1f}% is above 15% early-warning "
                f"({metrics['at_risk_count']} of {metrics['total_customers']} accounts)"
            )
        if churn_rate > 7:
            churn_reasons.append(f"observed churn rate {churn_rate:.1f}% is above the 7% benchmark ceiling")
        churn_trigger = " and ".join(churn_reasons) + "."
        churn_sla = 'Launch focused outreach and churn root-cause review within 5 business days'
    else:
        churn_signal = 'Retention operating in control'
        churn_trigger = (
            f"At-risk share {metrics['at_risk_pct']:.1f}% is within <=15% and observed churn rate "
            f"{churn_rate:.1f}% is within <=7% control bands."
        )
        churn_sla = 'Review risk cohort weekly'

    pipeline_priority = get_action_priority('pipeline', metrics)
    if not metrics.get('has_pipeline_data', False):
        pipeline_signal = 'Pipeline signal unavailable'
        pipeline_trigger = 'No SQLs in the current filter context.'
        pipeline_sla = 'Broaden filters before assigning pipeline intervention'
    elif pipeline_priority == 'Critical':
        pipeline_signal = 'Pipeline conversion intervention required'
        pipeline_trigger = (
            f"SQL->Won conversion {metrics['sql_to_won']:.1f}% is below 20% intervention floor "
            f"and materially off the 25% aspiration."
        )
        pipeline_sla = 'Run stage audit in 72 hours'
    elif pipeline_priority == 'High':
        pipeline_signal = 'Pipeline conversion below target'
        pipeline_trigger = (
            f"SQL->Won conversion {metrics['sql_to_won']:.1f}% is in the 20-25% watch band and below 25% aspiration."
        )
        pipeline_sla = 'Complete stage audit and recovery plan within 5 business days'
    else:
        pipeline_signal = 'Pipeline conversion on target'
        pipeline_trigger = (
            f"SQL->Won conversion {metrics['sql_to_won']:.1f}% is at or above 25% aspirational target."
        )
        pipeline_sla = 'Maintain weekly stage hygiene and monthly calibration'

    expansion_priority = get_action_priority('expansion', metrics)
    if not metrics.get('has_expansion_data', False):
        expansion_signal = 'Expansion signal unavailable'
        expansion_trigger = 'No active ARR context in the current filter selection.'
        expansion_sla = 'Broaden filters before assigning expansion execution'
    elif expansion_priority == 'Critical':
        expansion_signal = 'Expansion gap at intervention level'
        expansion_trigger = (
            f"Expansion rate {metrics['expansion_pct']:.1f}% is below the 10% critical threshold "
            f"(target 12%)."
        )
        expansion_sla = 'Prioritize top 20 expansion candidates in 7 days'
    elif expansion_priority == 'High':
        expansion_signal = 'Expansion below strategic target'
        expansion_trigger = (
            f"Expansion rate {metrics['expansion_pct']:.1f}% is in the 10-12% watch band and below 12% target."
        )
        expansion_sla = 'Launch focused upsell sprint within 10 business days'
    else:
        expansion_signal = 'Expansion operating above target'
        if metrics['expansion_pct'] > 12:
            expansion_trigger = f"Expansion rate {metrics['expansion_pct']:.1f}% is above 12% target."
        else:
            expansion_trigger = f"Expansion rate {metrics['expansion_pct']:.1f}% is at 12% target."
        expansion_sla = 'Maintain monthly expansion planning cadence'

    return [
        {
            'action_key': 'churn',
            'Priority': churn_priority,
            'Signal': churn_signal,
            'Trigger': churn_trigger,
            'Recommended Owner': 'Customer Success Manager',
            'Suggested SLA': churn_sla,
            'Immediate Action': impact_by_key['churn']['quick_win'],
            'Projected Impact': impact_by_key['churn']['impact_label'],
            'execution_order': 1
        },
        {
            'action_key': 'pipeline',
            'Priority': pipeline_priority,
            'Signal': pipeline_signal,
            'Trigger': pipeline_trigger,
            'Recommended Owner': 'RevOps + Sales Leadership',
            'Suggested SLA': pipeline_sla,
            'Immediate Action': impact_by_key['pipeline']['quick_win'],
            'Projected Impact': impact_by_key['pipeline']['impact_label'],
            'execution_order': 2
        },
        {
            'action_key': 'expansion',
            'Priority': expansion_priority,
            'Signal': expansion_signal,
            'Trigger': expansion_trigger,
            'Recommended Owner': 'CS Leadership + Account Strategy',
            'Suggested SLA': expansion_sla,
            'Immediate Action': impact_by_key['expansion']['quick_win'],
            'Projected Impact': impact_by_key['expansion']['impact_label'],
            'execution_order': 3
        }
    ]


def render_section_header(icon, title, description):
    st.markdown(
        f"""
        <div class='section-header-wrap'>
            <div class='section-header-icon'>{icon}</div>
            <div>
                <h3 class='section-header-title'>{title}</h3>
                <p class='section-header-desc'>{description}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_playbook_card(row):
    priority = row['Priority']
    if priority == "Critical":
        priority_class = "playbook-critical"
        priority_icon = "🔴"
    elif priority == "High":
        priority_class = "playbook-high"
        priority_icon = "🟠"
    else:
        priority_class = "playbook-monitor"
        priority_icon = "🔵"

    st.markdown(
        f"""
        <div class='playbook-card {priority_class}'>
            <p class='playbook-priority'>{priority_icon} {priority}</p>
            <p class='playbook-signal'>{row['Signal']}</p>
            <p class='playbook-line'><strong>Trigger:</strong> {row['Trigger']}</p>
            <p class='playbook-line'><strong>Owner:</strong> {row['Recommended Owner']}</p>
            <p class='playbook-line'><strong>SLA:</strong> {row['Suggested SLA']}</p>
            <p class='playbook-line'><strong>Immediate Action:</strong> {row['Immediate Action']}</p>
            <p class='playbook-impact'>Projected Impact: {row['Projected Impact']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Phase 1: Executive landing layer
st.markdown("""
<div class='hero-wrap'>
    <div class='hero-kicker'>Customer Success x Growth Analytics</div>
    <div class='hero-stack'>
        <span class='hero-title-line'>Customer Lifecycle Intelligence</span>
        <span class='hero-subtitle-line'>Predictive Analytics for Retention, Expansion, and Revenue Decisions</span>
        <span class='hero-byline-line'>Built by <a href='https://www.linkedin.com/in/harshjoshi21/' target='_blank' rel='noopener noreferrer'>Harsh Joshi</a></span>
    </div>
</div>
""", unsafe_allow_html=True)

col_a, col_b, col_c, col_d = st.columns(4)
with col_a:
    st.markdown("""
    <div class='info-card'>
        <h4>What This Project Is</h4>
        <p>A unified operating layer that connects lifecycle signals to Customer Success and Growth priorities.</p>
    </div>
    """, unsafe_allow_html=True)
with col_b:
    st.markdown("""
    <div class='info-card'>
        <h4>What You Do With It</h4>
        <p>Identify conversion bottlenecks, prioritize at-risk accounts, focus expansion plays, and stress-test growth scenarios.</p>
    </div>
    """, unsafe_allow_html=True)
with col_c:
    st.markdown("""
    <div class='info-card'>
        <h4>What It Conveys</h4>
        <p>How customer behavior and operating process quality shape retention, expansion, and revenue trajectory.</p>
    </div>
    """, unsafe_allow_html=True)
with col_d:
    st.markdown("""
    <div class='info-card'>
        <h4>Why It Is Useful</h4>
        <p>It helps CS and Growth move in sync, reducing handoff friction and accelerating high-impact action.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <div class='context-callout'>
        <strong>Methodology:</strong> This project uses realistic SaaS simulation to model funnel performance, churn risk, expansion behavior, and scenario outcomes.
        Assumptions are transparent so leaders can validate drivers, calibrate confidence, and translate insights into owner-level execution.
    </div>
    """,
    unsafe_allow_html=True
)

st.info("Navigation guide: Start with sidebar filters to set your operating context, scan the executive signals at the top, then open each tab for deeper analysis.")

with st.expander("🧭 Evaluator Walkthrough (2 minutes)", expanded=True):
    st.markdown("**1) Understand portfolio intent (20 sec)**")
    st.markdown("Read the hero title, methodology note, and first-glance cards to see the strategic framing and analytical intent.")
    st.markdown("**2) Scan executive signals (30 sec)**")
    st.markdown("Use Executive Snapshot and Top Insights to identify immediate risk/opportunity themes.")
    st.markdown("**3) Stress-test context (30 sec)**")
    st.markdown("Change filters and Executive View Mode to see how priorities shift by segment, channel, and scenario.")
    st.markdown("**4) Validate actionability (40 sec)**")
    st.markdown("Open Action Playbook to map data signals to owner, SLA, and expected business impact.")

st.markdown("### What This Showcase Helps You Evaluate")
d1, d2, d3 = st.columns(3)
with d1:
    st.markdown("""
    <div class='insight-card'>
        <h5>Retention Prioritization</h5>
        <p>Which accounts require immediate CS intervention to reduce near-term churn risk.</p>
    </div>
    """, unsafe_allow_html=True)
with d2:
    st.markdown("""
    <div class='insight-card'>
        <h5>Pipeline Intervention</h5>
        <p>Where conversion breakdowns need RevOps and sales process correction.</p>
    </div>
    """, unsafe_allow_html=True)
with d3:
    st.markdown("""
    <div class='insight-card'>
        <h5>Expansion Strategy</h5>
        <p>Which segments and cohorts are best positioned for upsell and NRR improvement.</p>
    </div>
    """, unsafe_allow_html=True)

# Key metrics at top
st.markdown("### Executive Snapshot")
st.caption("Baseline portfolio view (full dataset). Selection-aware metrics and recommendations are shown below in Top Insights, Benchmark Lens, and tabs.")
col1, col2, col3, col4 = st.columns(4)

with col1:
    active_customers = len(customers_df[customers_df['is_churned'] == 0])
    st.metric("Active Customers", active_customers, delta=None)

with col2:
    total_arr = customers_df[customers_df['is_churned'] == 0]['arr'].sum()
    st.metric("Current ARR", format_currency(total_arr, decimals=1), delta=None)

with col3:
    churn_customers = customers_df['is_churned'].sum()
    churn_rate = (churn_customers / len(customers_df) * 100) if len(customers_df) > 0 else 0
    st.metric("Churn Rate", f"{churn_rate:.1f}%", delta=None)

with col4:
    nrr = (customers_df[customers_df['is_churned'] == 0]['nrr_contribution'].mean() * 100) if len(customers_df[customers_df['is_churned'] == 0]) > 0 else 0
    st.metric("Avg NRR", f"{nrr:.0f}%", delta=None)

st.divider()

# SIDEBAR FILTERS
st.sidebar.title("⚙️ Filters & What-If")
st.sidebar.caption("Set your operating context first, then use tabs to investigate root causes and actions.")

data_start = min(leads_df['lead_date'].min(), customers_df['start_date'].min())
data_end = max(leads_df['lead_date'].max(), customers_df['start_date'].max())
default_date_range = (pd.to_datetime(data_start), pd.to_datetime(data_end))

default_channels = leads_df['channel'].value_counts().head(3).index.tolist()
if not default_channels:
    default_channels = leads_df['channel'].unique().tolist()

default_segments = customers_df['segment'].value_counts().index.tolist()
if not default_segments:
    default_segments = customers_df['segment'].unique().tolist()

if st.sidebar.button("Reset to recommended defaults", help="Reset date, filters, what-if, and view mode to the recommended starting context."):
    st.session_state['date_range'] = default_date_range
    st.session_state['selected_channels'] = default_channels
    st.session_state['selected_segments'] = default_segments
    st.session_state['pipeline_improvement'] = 0
    st.session_state['view_mode'] = "All Accounts"
    st.rerun()

view_mode = st.sidebar.radio(
    "Executive View Mode",
    options=["All Accounts", "At-Risk Focus", "Expansion Focus"],
    index=0,
    key="view_mode",
    help="Choose a leadership lens before drilling down: broad health, retention pressure, or expansion upside."
)

# Date range filter
date_range = st.sidebar.date_input(
    "Date Range",
    value=default_date_range,
    key="date_range",
    help="Limit analysis to a specific time window; wider ranges improve trend reliability."
)

if isinstance(date_range, tuple) and len(date_range) == 2:
    filter_start_date = pd.to_datetime(date_range[0])
    filter_end_date = pd.to_datetime(date_range[1])
else:
    filter_start_date = pd.to_datetime(date_range)
    filter_end_date = pd.to_datetime(date_range)

# Channel filter
selected_channels = st.sidebar.multiselect(
    "Marketing Channels",
    options=leads_df['channel'].unique(),
    default=default_channels,
    key="selected_channels",
    help="Start with top-volume channels, then isolate one source to inspect conversion and customer outcomes by acquisition source."
)

# Segment filter
selected_segments = st.sidebar.multiselect(
    "Customer Segments",
    options=customers_df['segment'].unique(),
    default=default_segments,
    key="selected_segments",
    help="Focus on one or two segments to compare retention and expansion dynamics clearly."
)

# What-if slider: improve conversion
pipeline_improvement = st.sidebar.slider(
    "What-if: Improve SQL→Won Conversion by",
    min_value=0, max_value=50, value=0, step=5,
    key="pipeline_improvement",
    help="Test upside scenarios and compare expected ARR movement before committing execution resources."
)

# Filter data
leads_filtered = leads_df[
    (leads_df['channel'].isin(selected_channels)) &
    (leads_df['lead_date'] >= filter_start_date) &
    (leads_df['lead_date'] <= filter_end_date)
]

customers_filtered = customers_df[
    (customers_df['segment'].isin(selected_segments)) &
    (customers_df['channel'].isin(selected_channels)) &
    (customers_df['start_date'] >= filter_start_date) &
    (customers_df['start_date'] <= filter_end_date)
]

if view_mode == "At-Risk Focus":
    customers_view = customers_filtered[customers_filtered['churn_risk'] > 70]
elif view_mode == "Expansion Focus":
    customers_view = customers_filtered[(customers_filtered['is_churned'] == 0) & (customers_filtered['expansion_arr'] > 0)]
else:
    customers_view = customers_filtered.copy()

leads_view = leads_filtered.copy()

# Phase 1: dynamic executive insight strip
st.markdown("### Top Insights for Current Selection")

sql_to_won = 0.0

if len(leads_view) > 0 and len(customers_view) > 0:
    n_sql_filtered = leads_view['is_sql'].sum()
    n_won_filtered = leads_view['is_won'].sum()
    sql_to_won = (n_won_filtered / n_sql_filtered * 100) if n_sql_filtered > 0 else 0

    at_risk_customers = customers_view[customers_view['churn_risk'] > 70]
    at_risk_share = (len(at_risk_customers) / len(customers_view) * 100) if len(customers_view) > 0 else 0

    expansion_view = customers_view[customers_view['is_churned'] == 0].groupby('segment').agg({
        'arr': 'sum',
        'expansion_arr': 'sum'
    }).reset_index()

    if len(expansion_view) > 0:
        expansion_view['expansion_rate'] = np.where(
            expansion_view['arr'] > 0,
            expansion_view['expansion_arr'] / expansion_view['arr'] * 100,
            0
        )
        top_segment_row = expansion_view.sort_values('expansion_rate', ascending=False).iloc[0]
        top_segment_text = f"{top_segment_row['segment']} leads expansion at {top_segment_row['expansion_rate']:.1f}% uplift."
    else:
        top_segment_text = "No active segment expansion signal in this selection yet."

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class='insight-card'>
            <h5>Pipeline Signal</h5>
            <p>SQL→Won conversion is <strong>{sql_to_won:.1f}%</strong>. Use this as your baseline before scenario improvements.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class='insight-card'>
            <h5>Retention Exposure</h5>
            <p><strong>{len(at_risk_customers)}</strong> accounts are high risk ({at_risk_share:.1f}% of current view), indicating proactive CS intervention need.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class='insight-card'>
            <h5>Expansion Opportunity</h5>
            <p>{top_segment_text}</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.warning("Not enough filtered data to generate executive insights. Widen date range or adjust segment/channel filters.")

st.markdown("### Benchmark Lens")
st.caption("Compare current performance against operating benchmarks to decide whether to hold, monitor, or intervene.")

operating_metrics = derive_operating_metrics(leads_view, customers_view)
churn_rate_view = operating_metrics['churn_rate']
nrr_view = operating_metrics['current_nrr']

expansion_ref = operating_metrics['expansion_pct']

bench1, bench2, bench3, bench4 = st.columns(4)
with bench1:
    churn_signal, churn_class, churn_note = get_benchmark_signal("churn", churn_rate_view)
    render_benchmark_card("Churn Rate", "5-7%", f"{churn_rate_view:.1f}%", churn_signal, churn_class, churn_note)
with bench2:
    nrr_signal, nrr_class, nrr_note = get_benchmark_signal("nrr", nrr_view)
    render_benchmark_card("NRR", "105-115%", f"{nrr_view:.0f}%", nrr_signal, nrr_class, nrr_note)
with bench3:
    sql_signal, sql_class, sql_note = get_benchmark_signal("sql_to_won", operating_metrics['sql_to_won'])
    render_benchmark_card("SQL to Won", "20-30%", f"{operating_metrics['sql_to_won']:.1f}%", sql_signal, sql_class, sql_note)
with bench4:
    expansion_signal, expansion_class, expansion_note = get_benchmark_signal("expansion", expansion_ref)
    render_benchmark_card("Expansion Rate", "Target: >=12% (Watch: 10-12%)", f"{expansion_ref:.1f}%", expansion_signal, expansion_class, expansion_note)

impact_rows, quick_win = calculate_action_impacts(leads_view, customers_view, operating_metrics)
if quick_win and quick_win['impact_value'] > 0:
    st.markdown(
        f"""
        <div class='quick-win-callout'>
            <p class='quick-win-title'>Quick Win: {quick_win['signal']} can unlock up to {format_currency(quick_win['impact_value'], decimals=2)} ARR.</p>
            <p class='quick-win-move'><strong>Immediate move:</strong> {quick_win['quick_win']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("Quick Win: No high-confidence upside identified in the current filter context. Broaden scope or adjust view mode.")

st.sidebar.divider()
st.sidebar.markdown("**How to use this view**")
st.sidebar.markdown("1. Pick an executive mode")
st.sidebar.markdown("2. Refine date, channels, and segments")
st.sidebar.markdown("3. Use Benchmark Lens and Quick Win to set priorities")
st.sidebar.markdown("4. Open tabs for root cause and owner-level actions")
with st.sidebar.popover("📘 KPI Glossary"):
    st.markdown("**MQL**: Marketing Qualified Lead")
    st.markdown("**SQL**: Sales Qualified Lead")
    st.markdown("**NRR**: Net Revenue Retention")
    st.markdown("**Cohort**: Group of customers acquired in same period")
    st.markdown("**Churn Risk**: Engagement-derived probability signal (0-100)")

# TABS
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Pipeline Risks",
    "⚠️ Customer Health Actions",
    "💰 Expansion Levers",
    "🔮 Scenario Forecast",
    "🎯 Action Playbook"
])

base_segment_order = ["Healthcare", "Finance", "Tech/SaaS", "Non-Profit", "Manufacturing"]
present_segments = customers_df['segment'].dropna().unique().tolist()
extra_segments = [segment for segment in sorted(present_segments) if segment not in base_segment_order]
segment_axis = [segment for segment in base_segment_order if segment in present_segments] + extra_segments

# TAB 1: FUNNEL
with tab1:
    st.markdown(
        """
        <div class='context-callout'>
            <strong>Section focus:</strong> See where leads drop between stages, compare against conversion targets, and focus intervention on the biggest handoff leak.
        </div>
        """,
        unsafe_allow_html=True
    )

    n_leads = len(leads_view)
    n_mql = int(leads_view['is_mql'].sum())
    n_sql = int(leads_view['is_sql'].sum())
    n_opp = int(leads_view['is_opp'].sum())
    n_won = int(leads_view['is_won'].sum())

    if pipeline_improvement > 0:
        additional_won = int(n_opp * (pipeline_improvement / 100))
        n_won_adjusted = min(n_won + additional_won, n_opp)
    else:
        additional_won = 0
        n_won_adjusted = n_won

    stage_names = ['Leads', 'MQLs', 'SQLs', 'Opportunities', 'Closed Won']
    stage_counts = [n_leads, n_mql, n_sql, n_opp, n_won_adjusted]

    stage_drops = []
    for idx in range(len(stage_names) - 1):
        from_count = stage_counts[idx]
        to_count = stage_counts[idx + 1]
        conversion_pct = (to_count / from_count * 100) if from_count > 0 else 0
        drop_pct = 100 - conversion_pct
        stage_drops.append({
            'from_stage': stage_names[idx],
            'to_stage': stage_names[idx + 1],
            'conversion_pct': conversion_pct,
            'drop_pct': drop_pct
        })

    bottleneck = max(stage_drops, key=lambda row: row['drop_pct']) if stage_drops else None

    transition_labels = ['Leads→MQL', 'MQL→SQL', 'SQL→Opp', 'Opp→Won']
    transition_rates = [
        (n_mql / n_leads * 100) if n_leads > 0 else 0,
        (n_sql / n_mql * 100) if n_mql > 0 else 0,
        (n_opp / n_sql * 100) if n_sql > 0 else 0,
        (n_won_adjusted / n_opp * 100) if n_opp > 0 else 0,
    ]
    transition_targets = [30, 25, 40, 35]
    transition_colors = [
        HEALTH_GREEN if rate >= target else RISK_RED
        for rate, target in zip(transition_rates, transition_targets)
    ]

    funnel_colors = [PRIMARY_BLUE, SECONDARY_BLUE, HEALTH_GREEN, WARNING_AMBER, PRIMARY_BLUE]
    if bottleneck:
        bottleneck_index = stage_names.index(bottleneck['to_stage'])
        if 0 <= bottleneck_index < len(funnel_colors):
            funnel_colors[bottleneck_index] = RISK_RED

    initial_count = stage_counts[0] if stage_counts and stage_counts[0] > 0 else 1
    stage_percentages = [(count / initial_count * 100) for count in stage_counts]
    funnel_hover_data = [
        [stage_names[idx], stage_percentages[idx]]
        for idx in range(len(stage_names))
    ]

    funnel_fig = go.Figure(data=[
        go.Funnel(
            y=stage_names,
            x=stage_counts,
            textposition="outside",
            texttemplate="%{label}: %{x:,}",
            textfont=dict(size=13),
            customdata=funnel_hover_data,
            hovertemplate="<b>%{customdata[0]}</b><br>Count: %{x:,}<br>Share of total leads: %{customdata[1]:.1f}%<extra></extra>",
            marker=dict(color=funnel_colors)
        )
    ])
    apply_chart_theme(funnel_fig, "Pipeline Volume by Stage", height=480)
    st.plotly_chart(funnel_fig, use_container_width=True)

    stage_col1, stage_col2, stage_col3, stage_col4, stage_col5 = st.columns(5)
    with stage_col1:
        st.metric("Leads", f"{n_leads:,}")
    with stage_col2:
        st.metric("MQLs", f"{n_mql:,}")
    with stage_col3:
        st.metric("SQLs", f"{n_sql:,}")
    with stage_col4:
        st.metric("Opportunities", f"{n_opp:,}")
    with stage_col5:
        st.metric("Closed Won", f"{n_won_adjusted:,}")

    rates_fig = go.Figure()
    rates_fig.add_trace(go.Bar(
        x=transition_labels,
        y=transition_rates,
        name="Current",
        marker_color=transition_colors,
        text=[f"{rate:.1f}%" for rate in transition_rates],
        textposition="outside",
        hovertemplate="<b>%{x}</b><br>Current: %{y:.1f}%<extra></extra>"
    ))
    rates_fig.add_trace(go.Scatter(
        x=transition_labels,
        y=transition_targets,
        mode="lines+markers",
        name="Target",
        line=dict(color=WARNING_AMBER, width=2, dash="dash"),
        marker=dict(color=WARNING_AMBER, size=7),
        hovertemplate="<b>%{x}</b><br>Target: %{y:.1f}%<extra></extra>"
    ))
    apply_chart_theme(rates_fig, "Stage Conversion vs Target", "Stage Transition", "Conversion Rate (%)", 380)
    max_rate = max(transition_targets + transition_rates) if transition_rates else max(transition_targets)
    rates_fig.update_yaxes(range=[0, max_rate + 10], ticksuffix="%")
    st.plotly_chart(rates_fig, use_container_width=True)

    if bottleneck:
        st.warning(
            f"Biggest conversion leak: **{bottleneck['from_stage']} to {bottleneck['to_stage']}** "
            f"({bottleneck['drop_pct']:.1f}% drop, {bottleneck['conversion_pct']:.1f}% conversion). "
            "Fix this handoff first to improve pipeline throughput fastest."
        )

    metric_col1, metric_col2, metric_col3 = st.columns(3)
    avg_deal_assumption = operating_metrics['avg_won_arr']
    with metric_col1:
        st.metric("Total Pipeline Value", format_currency(n_opp * avg_deal_assumption, decimals=1))
    with metric_col2:
        st.metric("Expected Closed Won", format_currency(n_won_adjusted * avg_deal_assumption, decimals=1))
    with metric_col3:
        if pipeline_improvement > 0:
            st.metric("What-If Lift", f"+{format_currency(additional_won * avg_deal_assumption, decimals=1)}")
        else:
            st.metric("What-If Lift", "$0")

    st.markdown(
        """
        <div class='context-callout'>
            <strong>Why What-If Lift starts at $0:</strong> The baseline assumes no conversion improvement from the current operating motion.
            When you move the sidebar What-if slider, the model increases expected closed-won opportunities from the current opportunity pool,
            then translates those additional wins into ARR using the same deal-value assumption used in this dashboard. This gives a fast scenario view
            of how conversion process improvements can impact near-term revenue outcomes before operational changes are launched.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Stuck Opportunities by Channel")
    st.markdown(
        """
        <div class='context-callout'>
            <strong>What this means:</strong> This view tracks open opportunities that have remained unresolved for more than 30 days since opportunity creation.
            High counts indicate pipeline delay risk and handoff friction. Start with channels showing the oldest opportunities first.
        </div>
        """,
        unsafe_allow_html=True
    )

    stuck_cutoff_date = pd.to_datetime(filter_end_date) - timedelta(days=30)
    stuck_opps = leads_view[
        (leads_view['is_opp'] == True) & 
        (leads_view['is_won'] == False) &
        (leads_view['opp_date'] <= stuck_cutoff_date)
    ].groupby('channel').size().to_frame('Count').reset_index()
    
    if len(stuck_opps) > 0:
        fig = px.bar(
            stuck_opps,
            x='channel',
            y='Count',
            title="Opportunities Stalled >30 Days by Source Channel",
            color_discrete_sequence=[WARNING_AMBER]
        )
        apply_chart_theme(fig, "Opportunities Stalled >30 Days by Source Channel", "Marketing Channel", "Open Opportunities", 380)
        st.plotly_chart(fig, use_container_width=True)
        
        # Drill into specific channel
        selected_channel_drill = st.selectbox("Drill into channel:", stuck_opps['channel'].unique())
        channel_stuck = leads_view[
            (leads_view['channel'] == selected_channel_drill) &
            (leads_view['is_opp'] == True) &
            (leads_view['is_won'] == False) &
            (leads_view['opp_date'] <= stuck_cutoff_date)
        ][['lead_id', 'segment', 'opp_date', 'channel']].copy()

        channel_stuck['days_stuck'] = (
            pd.to_datetime(filter_end_date).normalize() - pd.to_datetime(channel_stuck['opp_date']).dt.normalize()
        ).dt.days
        channel_stuck['priority'] = np.where(channel_stuck['days_stuck'] >= 60, "Critical", "High")
        channel_stuck['opp_date'] = pd.to_datetime(channel_stuck['opp_date']).dt.date
        channel_stuck = channel_stuck.sort_values('days_stuck', ascending=False)

        channel_stuck_display = channel_stuck[['segment', 'channel', 'opp_date', 'days_stuck', 'priority']].head(10)
        st.markdown(
            f"<p class='table-context'>Showing {len(channel_stuck_display)} of {len(channel_stuck)} stuck opportunities in {selected_channel_drill}, sorted by urgency.</p>",
            unsafe_allow_html=True
        )
        st.dataframe(
            channel_stuck_display,
            use_container_width=True,
            hide_index=True,
            column_config={
                'segment': st.column_config.TextColumn('Segment'),
                'channel': st.column_config.TextColumn('Channel'),
                'opp_date': st.column_config.DateColumn('Opportunity Date'),
                'days_stuck': st.column_config.NumberColumn('Days Stuck', format='%d'),
                'priority': st.column_config.TextColumn('Priority')
            }
        )

        top_stuck_count = int(channel_stuck.head(5).shape[0])
        selected_channel_count = int(stuck_opps[stuck_opps['channel'] == selected_channel_drill]['Count'].iloc[0])
        total_stuck_count = int(stuck_opps['Count'].sum())
        selected_channel_share = (selected_channel_count / total_stuck_count * 100) if total_stuck_count > 0 else 0
        st.markdown(
            f"**Action:** Prioritize follow-up on the oldest {top_stuck_count} opportunities in **{selected_channel_drill}** this week. "
            f"This channel represents **{selected_channel_share:.1f}%** of all currently stuck opportunities."
        )
    else:
        st.info("No opportunities are currently stalled beyond 30 days in this filter view.")

# TAB 2: CHURN & HEALTH
with tab2:
    st.markdown(
        """
        <div class='context-callout'>
            <strong>Section focus:</strong> Prioritize intervention by combining churn risk score, engagement behavior, and account value signals.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class='context-callout'>
            <strong>How to read Avg Churn Risk:</strong> The y-axis shows an average <strong>risk score from 0 to 100</strong>, not a direct churn percentage.
            Higher scores indicate stronger probability of churn behavior and require faster CS intervention.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        risk_by_segment = customers_view.groupby('segment').agg({
            'churn_risk': 'mean',
            'customer_id': 'count'
        }).reset_index()
        risk_by_segment.columns = ['Segment', 'Avg Churn Risk', 'Customer Count']
        risk_by_segment = risk_by_segment.set_index('Segment').reindex(segment_axis, fill_value=0).reset_index()
        
        fig = px.bar(
            risk_by_segment,
            x='Segment',
            y='Avg Churn Risk',
            color='Avg Churn Risk',
            color_continuous_scale=[HEALTH_GREEN, WARNING_AMBER, RISK_RED],
            range_color=[0, 100],
            title="Average Churn Risk Score by Segment (0-100)"
        )
        apply_chart_theme(fig, "Average Churn Risk Score by Segment (0-100)", "Segment", "Avg Churn Risk Score (0-100)", 380)
        fig.update_traces(
            text=[f"n={int(count)}" for count in risk_by_segment['Customer Count']],
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>Avg Risk Score: %{y:.1f}/100<br>%{text}<extra></extra>"
        )
        st.plotly_chart(fig, use_container_width=True)

        if len(customers_view) > 0 and len(risk_by_segment[risk_by_segment['Customer Count'] > 0]) < len(segment_axis):
            st.info("Some segments currently have low or zero customer counts in this filter context, but remain visible for complete comparison.")
    
    with col1:
        at_risk = customers_view[customers_view['churn_risk'] > 70]
        healthy = customers_view[customers_view['churn_risk'] <= 70]

        st.markdown(
            """
            <div class='context-callout'>
                <strong>Engagement Score Formula:</strong>
                30% Feature Adoption + 40% Monthly Active Usage + 30% Support Sentiment, scaled to 0-100.
                Scores below 30 indicate low product engagement risk.
            </div>
            """,
            unsafe_allow_html=True
        )
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=healthy['engagement_score'],
            y=healthy['churn_risk'],
            mode='markers',
            marker=dict(size=8, color=HEALTH_GREEN, opacity=0.65),
            text=healthy['customer_id'],
            name='Healthy (Risk < 70)',
            hovertemplate='<b>%{text}</b><br>Engagement: %{x:.0f}<br>Churn Risk: %{y:.0f}<extra></extra>'
        ))
        
        fig.add_trace(go.Scatter(
            x=at_risk['engagement_score'],
            y=at_risk['churn_risk'],
            mode='markers',
            marker=dict(size=10, color=RISK_RED, opacity=0.72),
            text=at_risk['customer_id'],
            name='At Risk (Risk > 70)',
            hovertemplate='<b>%{text}</b><br>Engagement: %{x:.0f}<br>Churn Risk: %{y:.0f}<extra></extra>'
        ))
        
        fig.add_hline(y=70, line_dash="dash", line_color=WARNING_AMBER, annotation_text="Risk Threshold")
        apply_chart_theme(fig, "Engagement Score vs. Churn Risk", "Engagement Score (0-100)", "Churn Risk (0-100)", 400)
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.metric("At-Risk Customers", len(at_risk), delta=None)
        st.metric("Healthy Customers", len(healthy), delta=None)
        if len(at_risk) > 0:
            st.markdown(f"**Action**: {len(at_risk)} customers need engagement intervention")
    
    # Drill-down: at-risk customers
    st.markdown("**At-Risk Customers Requiring Action**")
    at_risk_detail = customers_view[customers_view['churn_risk'] > 70].sort_values('churn_risk', ascending=False)[
        ['customer_id', 'segment', 'arr', 'engagement_score', 'churn_risk', 'features_adopted', 'support_sentiment']
    ]
    
    if len(at_risk_detail) > 0:
        at_risk_display = at_risk_detail.copy()
        at_risk_display['priority'] = np.select(
            [at_risk_display['churn_risk'] >= 85, at_risk_display['churn_risk'] >= 70],
            ['Critical', 'High'],
            default='Monitor'
        )
        at_risk_display['engagement_flag'] = np.where(at_risk_display['engagement_score'] < 30, 'Low engagement', 'Needs follow-up')
        priority_rank = {'Critical': 0, 'High': 1, 'Monitor': 2}
        at_risk_display['priority_rank'] = at_risk_display['priority'].map(priority_rank)
        at_risk_display = at_risk_display.sort_values(['priority_rank', 'churn_risk'], ascending=[True, False]).drop(columns=['priority_rank'])
        at_risk_display['arr'] = at_risk_display['arr'].map(lambda value: format_currency(value, decimals=1))
        at_risk_display = at_risk_display[[
            'segment', 'arr', 'churn_risk', 'engagement_score', 'engagement_flag', 'priority', 'support_sentiment'
        ]]
        at_risk_table = at_risk_display.head(15)
        st.markdown(
            f"<p class='table-context'>Showing {len(at_risk_table)} of {len(at_risk_display)} at-risk accounts, sorted by intervention urgency.</p>",
            unsafe_allow_html=True
        )
        st.dataframe(
            at_risk_table,
            use_container_width=True,
            hide_index=True,
            column_config={
                'segment': st.column_config.TextColumn('Segment'),
                'arr': st.column_config.TextColumn('ARR'),
                'churn_risk': st.column_config.NumberColumn('Churn Risk', format='%.1f'),
                'engagement_score': st.column_config.NumberColumn('Engagement', format='%.0f'),
                'engagement_flag': st.column_config.TextColumn('Engagement Signal'),
                'priority': st.column_config.TextColumn('Priority'),
                'support_sentiment': st.column_config.TextColumn('Support Sentiment')
            }
        )

# TAB 3: EXPANSION & COHORTS
with tab3:
    st.markdown(
        """
        <div class='context-callout'>
            <strong>Section focus:</strong> Track which segments drive expansion ARR now and use cohort retention to judge long-term customer quality.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class='context-callout'>
            <strong>Why this matters:</strong> Expansion ARR shows immediate upside from existing customers.
            Cohort retention shows whether newly acquired groups are staying longer over time, which is a leading indicator of durable growth.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        expansion_by_segment = customers_view[customers_view['is_churned'] == 0].groupby('segment').agg({
            'arr': 'sum',
            'expansion_arr': 'sum'
        }).reset_index()
        expansion_by_segment = expansion_by_segment.set_index('segment').reindex(segment_axis, fill_value=0).reset_index()
        expansion_by_segment['expansion_rate'] = np.where(
            expansion_by_segment['arr'] > 0,
            (expansion_by_segment['expansion_arr'] / expansion_by_segment['arr'] * 100).round(1),
            0
        )
        expansion_by_segment.columns = ['Segment', 'Base ARR', 'Expansion ARR', 'Expansion Rate (%)']
        expansion_chart_df = expansion_by_segment.copy()
        expansion_chart_df['Base ARR ($M)'] = (expansion_chart_df['Base ARR'] / 1_000_000).round(2)
        expansion_chart_df['Expansion ARR ($M)'] = (expansion_chart_df['Expansion ARR'] / 1_000_000).round(2)
        
        fig = px.bar(
            expansion_chart_df,
            x='Segment',
            y=['Base ARR ($M)', 'Expansion ARR ($M)'],
            barmode='stack',
            title="Base vs Expansion ARR by Segment (in Millions)",
            color_discrete_sequence=[PRIMARY_BLUE, HEALTH_GREEN]
        )
        apply_chart_theme(fig, "Base vs Expansion ARR by Segment (in Millions)", "Segment", "ARR ($M)", 380)
        fig.update_traces(
            hovertemplate="<b>%{x}</b><br>%{fullData.name}: %{y:.2f}M<extra></extra>"
        )
        fig.update_yaxes(tickformat=".2f", ticksuffix="M")
        st.plotly_chart(fig, use_container_width=True)
    
    with col1:
        cohort_analysis = customers_view.groupby('cohort').agg({
            'customer_id': 'count',
            'is_churned': 'sum',
            'arr': 'sum'
        }).reset_index()
        cohort_analysis['retention_rate'] = ((cohort_analysis['customer_id'] - cohort_analysis['is_churned']) / cohort_analysis['customer_id'] * 100).round(1)
        cohort_analysis.columns = ['Cohort', 'Customers', 'Churned', 'ARR', 'Retention (%)']
        cohort_analysis = cohort_analysis.sort_values('Cohort')
        
        fig = px.line(
            cohort_analysis,
            x='Cohort',
            y='Retention (%)',
            markers=True,
            title="Cohort Retention Rate Over Time",
            height=350
        )
        fig.update_traces(line=dict(color=SECONDARY_BLUE, width=3), marker=dict(color=PRIMARY_BLUE, size=8))
        apply_chart_theme(fig, "Cohort Retention Rate Over Time", "Cohort", "Retention (%)", 350)
        st.plotly_chart(fig, use_container_width=True)

        if len(cohort_analysis) > 1:
            oldest_retention = cohort_analysis.iloc[0]['Retention (%)']
            latest_retention = cohort_analysis.iloc[-1]['Retention (%)']
            trend_text = "improving" if latest_retention >= oldest_retention else "declining"
            st.markdown(
                f"**Cohort insight:** Retention is currently **{trend_text}** "
                f"(earliest cohort: {oldest_retention:.1f}%, latest cohort: {latest_retention:.1f}%)."
            )
        else:
            st.info("Not enough cohort points in this filter context to infer a retention trend yet.")
    
    with col2:
        total_expansion = expansion_by_segment['Expansion ARR'].sum()
        st.metric("Total Expansion ARR", format_currency(total_expansion, decimals=2))
        avg_expansion_rate = expansion_by_segment['Expansion Rate (%)'].mean()
        st.metric("Avg Expansion Rate", f"{avg_expansion_rate:.1f}%")

# TAB 4: FORECAST
with tab4:
    st.markdown(
        """
        <div class='context-callout'>
            <strong>Section focus:</strong> Model ARR outcomes under current churn and expansion assumptions, then stress-test the impact of pipeline conversion improvement.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Build forecast with what-if impact
        current_arr = customers_view[customers_view['is_churned'] == 0]['arr'].sum()
        churn_rate = customers_view['is_churned'].mean() if len(customers_view) > 0 else 0
        expansion_rate = (customers_view['expansion_arr'].sum() / customers_view['arr'].sum()) if customers_view['arr'].sum() > 0 else 0
        
        forecast_months = 13  # Generate 0-12 months
        forecast_data_custom = []
        
        for month in range(forecast_months):
            # Account for what-if improvement
            pipeline_multiplier = 1 + (pipeline_improvement / 100 * 0.3)
            
            projected_arr = current_arr * (1 - churn_rate) ** month * (1 + expansion_rate * pipeline_multiplier) ** month
            forecast_data_custom.append({
                'Month': month,
                'Projected ARR': projected_arr / 1e6
            })
        
        forecast_df_custom = pd.DataFrame(forecast_data_custom)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=forecast_df_custom['Month'],
            y=forecast_df_custom['Projected ARR'],
            fill='tozeroy',
            name='Projected ARR',
            line=dict(color=PRIMARY_BLUE, width=3),
            fillcolor='rgba(31, 78, 121, 0.18)'
        ))

        apply_chart_theme(fig, "12-Month ARR Forecast", "Months Forward", "ARR ($M)", 400)
        fig.update_layout(hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        month_6_arr_m = forecast_df_custom[forecast_df_custom['Month'] == 6]['Projected ARR'].values[0]
        month_12_arr_m = forecast_df_custom[forecast_df_custom['Month'] == 12]['Projected ARR'].values[0]
        month_6_arr_value = month_6_arr_m * 1_000_000
        month_12_arr_value = month_12_arr_m * 1_000_000

        st.metric("Current ARR", format_currency(current_arr, decimals=2))
        st.metric(
            "6-Month Projected ARR",
            format_currency(month_6_arr_value, decimals=2),
            delta=format_currency(month_6_arr_value - current_arr, decimals=2)
        )
        st.metric(
            "12-Month Projected ARR",
            format_currency(month_12_arr_value, decimals=2),
            delta=format_currency(month_12_arr_value - current_arr, decimals=2)
        )
    
    st.markdown("**Key Assumptions:**")
    st.markdown(f"""
    - Observed Churn Share (filter cohort proxy): {churn_rate*100:.1f}%
    - Observed Expansion Share (filter cohort proxy): {expansion_rate*100:.1f}%
    - What-If Conversion Improvement: {pipeline_improvement}%
    """)

# TAB 5: PLAYBOOK
with tab5:
    st.markdown(
        """
        <div class='context-callout'>
            <strong>Section focus:</strong> Convert signals into owner-level execution with urgency, SLA, and projected ARR impact in one operating view.
        </div>
        """,
        unsafe_allow_html=True
    )

    impact_by_key = {row['key']: row for row in impact_rows}
    playbook_rows = build_playbook_rows(operating_metrics, impact_by_key)

    playbook_df = pd.DataFrame(playbook_rows)
    playbook_order = {'Critical': 0, 'High': 1, 'Monitor': 2}
    playbook_df['priority_rank'] = playbook_df['Priority'].map(playbook_order)
    playbook_df = playbook_df.sort_values(['priority_rank', 'execution_order']).drop(columns=['priority_rank', 'execution_order', 'action_key'])

    st.markdown(
        f"<p class='table-context'>Showing {len(playbook_df)} prioritized actions for the current filter context, ordered by urgency.</p>",
        unsafe_allow_html=True
    )

    playbook_cols = st.columns(len(playbook_df)) if len(playbook_df) > 0 else []
    for idx, row in enumerate(playbook_df.to_dict(orient='records')):
        with playbook_cols[idx]:
            render_playbook_card(row)

    st.markdown("**Execution Notes:**")
    st.markdown("- Review this playbook after every filter or scenario change.")
    st.markdown("- Priority legend: Critical = intervene now, High = close a gap, Monitor = maintain current performance.")
    st.markdown("- Use it as the operating bridge between analytics and owner-level action planning.")
    st.markdown("- Projected impacts are directional estimates based on the current filtered operating context.")

# Footer
st.divider()
local_now = datetime.now().astimezone()
timezone_label = local_now.tzname() or local_now.strftime("UTC%z")
footer_html = f"""
    <div style='text-align: center; color: #888; font-size: 12px; padding-top: 20px;'>
    Built by Harsh Joshi | Data refreshed: {local_now.strftime("%Y-%m-%d %H:%M")} ({timezone_label})
    </div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
