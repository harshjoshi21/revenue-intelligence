import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from data_generator import generate_saas_data, generate_forecast
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title="Revenue Intelligence Dashboard",
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
        background: linear-gradient(125deg, var(--navy-900), var(--navy-700));
        color: #ffffff;
        padding: 26px 28px;
        border-radius: 14px;
        margin-bottom: 12px;
        border: 1px solid rgba(212, 162, 76, 0.35);
    }
    .hero-kicker {
        display: inline-block;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #f2d8a6;
        margin-bottom: 10px;
    }
    .hero-title {
        font-size: 2rem;
        line-height: 1.2;
        margin: 0 0 8px 0;
        font-weight: 700;
    }
    .hero-subtitle {
        font-size: 1.02rem;
        margin: 0;
        max-width: 980px;
        opacity: 0.95;
    }
    .trust-strip {
        background: #fff;
        border: 1px solid var(--slate-200);
        border-radius: 12px;
        padding: 12px 14px;
        margin: 0 0 10px 0;
        color: var(--ink-900);
        font-size: 0.95rem;
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
        padding: 14px;
        min-height: 132px;
        margin-bottom: 6px;
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
    }
    .insight-card {
        background: #fff;
        border: 1px solid var(--slate-200);
        border-radius: 10px;
        padding: 12px;
        min-height: 96px;
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
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    leads_df, customers_df = generate_saas_data()
    forecast_df = generate_forecast(customers_df)
    return leads_df, customers_df, forecast_df

leads_df, customers_df, forecast_df = load_data()

# Phase 1: Executive landing layer
st.markdown("""
<div class='hero-wrap'>
    <div class='hero-kicker'>Customer Success and RevOps Intelligence</div>
    <h1 class='hero-title'>Revenue Intelligence Portfolio Dashboard</h1>
    <p class='hero-subtitle'>
        A personal portfolio showcase demonstrating my approach to Customer Success analytics,
        RevOps strategy, implementation operations, and solutions engineering through one executive operating view.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='trust-strip'>
    <strong>Built by Harsh Joshi</strong> | Personal project showcase of decision-grade thinking across Customer Success, RevOps, implementation operations, and solutions engineering.
    <br/>
    <span class='pill'>Customer Success Analytics</span>
    <span class='pill'>RevOps Analytics</span>
    <span class='pill'>Implementation Operations</span>
    <span class='pill'>Solutions Engineering</span>
</div>
""", unsafe_allow_html=True)

col_a, col_b, col_c, col_d = st.columns(4)
with col_a:
    st.markdown("""
    <div class='info-card'>
        <h4>What This Project Is</h4>
        <p>An executive-facing analytics workspace that unifies funnel, retention, expansion, and ARR forecast signals.</p>
    </div>
    """, unsafe_allow_html=True)
with col_b:
    st.markdown("""
    <div class='info-card'>
        <h4>What You Do With It</h4>
        <p>Identify pipeline bottlenecks, prioritize at-risk accounts, focus expansion plays, and pressure-test growth scenarios.</p>
    </div>
    """, unsafe_allow_html=True)
with col_c:
    st.markdown("""
    <div class='info-card'>
        <h4>What It Conveys</h4>
        <p>How operational signals connect to revenue outcomes, and where CS and implementation decisions shift trajectory.</p>
    </div>
    """, unsafe_allow_html=True)
with col_d:
    st.markdown("""
    <div class='info-card'>
        <h4>Why It Is Useful</h4>
        <p>It shortens executive decision cycles by turning fragmented metrics into one practical, action-oriented view.</p>
    </div>
    """, unsafe_allow_html=True)

st.info("Explore from left to right: filters define your operating context, summary insights surface what matters now, and tabs provide investigative depth.")

st.caption("Methodology note: This portfolio uses realistic simulated SaaS data to demonstrate analytical thinking, decision framing, and domain execution patterns.")

# Key metrics at top
st.markdown("### Executive Snapshot")
col1, col2, col3, col4 = st.columns(4)

with col1:
    active_customers = len(customers_df[customers_df['is_churned'] == 0])
    st.metric("Active Customers", active_customers, delta=None)

with col2:
    total_arr = customers_df[customers_df['is_churned'] == 0]['arr'].sum()
    st.metric("Current ARR", f"${total_arr/1e6:.1f}M", delta=None)

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

# Date range filter
date_range = st.sidebar.date_input(
    "Date Range",
    value=(pd.to_datetime('2024-01-01'), pd.to_datetime('2026-03-27')),
    key="date_range"
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
    default=leads_df['channel'].unique()
)

# Segment filter
selected_segments = st.sidebar.multiselect(
    "Customer Segments",
    options=customers_df['segment'].unique(),
    default=customers_df['segment'].unique()
)

# What-if slider: improve conversion
pipeline_improvement = st.sidebar.slider(
    "What-if: Improve SQL→Won Conversion by",
    min_value=0, max_value=50, value=0, step=5,
    help="Adjust to see impact on pipeline"
)

# Filter data
leads_filtered = leads_df[
    (leads_df['channel'].isin(selected_channels)) &
    (leads_df['lead_date'] >= filter_start_date) &
    (leads_df['lead_date'] <= filter_end_date)
]

customers_filtered = customers_df[
    (customers_df['segment'].isin(selected_segments)) &
    (customers_df['start_date'] >= filter_start_date) &
    (customers_df['start_date'] <= filter_end_date)
]

# Phase 1: dynamic executive insight strip
st.markdown("### Top Insights for Current Selection")

if len(leads_filtered) > 0 and len(customers_filtered) > 0:
    n_sql_filtered = leads_filtered['is_sql'].sum()
    n_won_filtered = leads_filtered['is_won'].sum()
    sql_to_won = (n_won_filtered / n_sql_filtered * 100) if n_sql_filtered > 0 else 0

    at_risk_customers = customers_filtered[customers_filtered['churn_risk'] > 70]
    at_risk_share = (len(at_risk_customers) / len(customers_filtered) * 100) if len(customers_filtered) > 0 else 0

    expansion_view = customers_filtered[customers_filtered['is_churned'] == 0].groupby('segment').agg({
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
            <p><strong>{len(at_risk_customers)}</strong> accounts are high risk ({at_risk_share:.1f}% of selected customers), indicating proactive CS intervention need.</p>
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

st.sidebar.divider()
st.sidebar.markdown("**View detailed breakdowns in tabs below.**")

# TABS
tab1, tab2, tab3, tab4 = st.tabs(["📈 Funnel", "⚠️ Churn & Health", "💰 Expansion & Cohorts", "🔮 Forecast"])

# TAB 1: FUNNEL
with tab1:
    st.subheader("Sales Funnel Overview")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Funnel stages with what-if adjustment
        n_leads = len(leads_filtered)
        n_mql = leads_filtered['is_mql'].sum()
        n_sql = leads_filtered['is_sql'].sum()
        n_opp = leads_filtered['is_opp'].sum()
        n_won = leads_filtered['is_won'].sum()
        
        # Apply what-if improvement
        if pipeline_improvement > 0:
            # Boost won deals by improving conversion
            additional_won = int(n_opp * (pipeline_improvement / 100))
            n_won_adjusted = min(n_won + additional_won, n_opp)
        else:
            n_won_adjusted = n_won
        
        funnel_data = {
            'Stage': ['Leads', 'MQLs', 'SQLs', 'Opportunities', 'Closed Won'],
            'Count': [n_leads, n_mql, n_sql, n_opp, n_won_adjusted],
            'Conversion': [
                '100%',
                f"{(n_mql/n_leads*100):.1f}%" if n_leads > 0 else '0%',
                f"{(n_sql/n_mql*100):.1f}%" if n_mql > 0 else '0%',
                f"{(n_opp/n_sql*100):.1f}%" if n_sql > 0 else '0%',
                f"{(n_won_adjusted/n_opp*100):.1f}%" if n_opp > 0 else '0%'
            ]
        }
        
        funnel_df = pd.DataFrame(funnel_data)
        
        fig = go.Figure(data=[
            go.Funnel(
                y=funnel_df['Stage'],
                x=funnel_df['Count'],
                textposition="inside",
                textinfo="value+percent initial",
                marker=dict(color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
            )
        ])
        
        fig.update_layout(height=400, title="Pipeline Funnel (by Stage)")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.metric("Total Pipeline Value", f"${(n_opp * 75000):.0f}")
        st.metric("Expected Closed Won", f"${(n_won_adjusted * 75000):.0f}")
        if pipeline_improvement > 0:
            st.metric("Impact of What-If", f"+${(additional_won * 75000):.0f}", delta="positive")
    
    # Drill-down: stuck deals by channel
    st.markdown("**Stuck Opportunities by Channel**")
    stuck_opps = leads_filtered[
        (leads_filtered['is_opp'] == True) & 
        (leads_filtered['is_won'] == False)
    ].groupby('channel').size().reset_index(name='Count')
    
    if len(stuck_opps) > 0:
        fig = px.bar(stuck_opps, x='channel', y='Count', title="Opportunities Not Closed (by Marketing Source)")
        st.plotly_chart(fig, use_container_width=True)
        
        # Drill into specific channel
        selected_channel_drill = st.selectbox("Drill into channel:", stuck_opps['channel'].unique())
        channel_stuck = leads_filtered[
            (leads_filtered['channel'] == selected_channel_drill) &
            (leads_filtered['is_opp'] == True) &
            (leads_filtered['is_won'] == False)
        ][['lead_id', 'segment', 'opp_date', 'channel']].sort_values('opp_date', ascending=False)
        
        st.dataframe(channel_stuck.head(10), use_container_width=True)

# TAB 2: CHURN & HEALTH
with tab2:
    st.subheader("Customer Health & Churn Risk")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Churn risk heatmap by segment
        risk_by_segment = customers_filtered.groupby('segment').agg({
            'churn_risk': 'mean',
            'customer_id': 'count'
        }).reset_index()
        risk_by_segment.columns = ['Segment', 'Avg Churn Risk', 'Customer Count']
        
        fig = px.bar(
            risk_by_segment,
            x='Segment',
            y='Avg Churn Risk',
            color='Avg Churn Risk',
            color_continuous_scale=['green', 'yellow', 'red'],
            range_color=[0, 100],
            title="Average Churn Risk by Segment"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col1:
        # Engagement vs. Churn scatter
        at_risk = customers_filtered[customers_filtered['churn_risk'] > 70]
        healthy = customers_filtered[customers_filtered['churn_risk'] <= 70]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=healthy['engagement_score'],
            y=healthy['churn_risk'],
            mode='markers',
            marker=dict(size=8, color='green', opacity=0.6),
            text=healthy['customer_id'],
            name='Healthy (Risk < 70)',
            hovertemplate='<b>%{text}</b><br>Engagement: %{x:.0f}<br>Churn Risk: %{y:.0f}<extra></extra>'
        ))
        
        fig.add_trace(go.Scatter(
            x=at_risk['engagement_score'],
            y=at_risk['churn_risk'],
            mode='markers',
            marker=dict(size=10, color='red', opacity=0.7),
            text=at_risk['customer_id'],
            name='At Risk (Risk > 70)',
            hovertemplate='<b>%{text}</b><br>Engagement: %{x:.0f}<br>Churn Risk: %{y:.0f}<extra></extra>'
        ))
        
        fig.add_hline(y=70, line_dash="dash", line_color="orange", annotation_text="Risk Threshold")
        fig.update_layout(
            title="Engagement Score vs. Churn Risk",
            xaxis_title="Engagement Score (0-100)",
            yaxis_title="Churn Risk (0-100)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.metric("At-Risk Customers", len(at_risk), delta=None)
        st.metric("Healthy Customers", len(healthy), delta=None)
        if len(at_risk) > 0:
            st.markdown(f"**Action**: {len(at_risk)} customers need engagement intervention")
    
    # Drill-down: at-risk customers
    st.markdown("**At-Risk Customers Requiring Action**")
    at_risk_detail = customers_filtered[customers_filtered['churn_risk'] > 70].sort_values('churn_risk', ascending=False)[
        ['customer_id', 'segment', 'arr', 'engagement_score', 'churn_risk', 'features_adopted', 'support_sentiment']
    ]
    
    if len(at_risk_detail) > 0:
        st.dataframe(at_risk_detail.head(15), use_container_width=True)

# TAB 3: EXPANSION & COHORTS
with tab3:
    st.subheader("Expansion Revenue & Cohort Retention")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Expansion by segment
        expansion_by_segment = customers_filtered[customers_filtered['is_churned'] == 0].groupby('segment').agg({
            'arr': 'sum',
            'expansion_arr': 'sum'
        }).reset_index()
        expansion_by_segment['expansion_rate'] = (expansion_by_segment['expansion_arr'] / expansion_by_segment['arr'] * 100).round(1)
        expansion_by_segment.columns = ['Segment', 'Base ARR', 'Expansion ARR', 'Expansion Rate (%)']
        
        fig = px.bar(
            expansion_by_segment,
            x='Segment',
            y=['Base ARR', 'Expansion ARR'],
            barmode='stack',
            title="Base vs. Expansion ARR by Segment"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col1:
        # Cohort retention curve
        cohort_analysis = customers_filtered.groupby('cohort').agg({
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
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        total_expansion = expansion_by_segment['Expansion ARR'].sum()
        st.metric("Total Expansion ARR", f"${total_expansion/1e6:.2f}M")
        avg_expansion_rate = expansion_by_segment['Expansion Rate (%)'].mean()
        st.metric("Avg Expansion Rate", f"{avg_expansion_rate:.1f}%")

# TAB 4: FORECAST
with tab4:
    st.subheader("ARR Forecast & Growth Projections")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Build forecast with what-if impact
        current_arr = customers_filtered[customers_filtered['is_churned'] == 0]['arr'].sum()
        churn_rate = customers_filtered['is_churned'].mean()
        expansion_rate = (customers_filtered['expansion_arr'].sum() / customers_filtered['arr'].sum()) if customers_filtered['arr'].sum() > 0 else 0
        
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
            line=dict(color='#1f77b4', width=3),
            fillcolor='rgba(31, 119, 180, 0.2)'
        ))
        
        fig.update_layout(
            title="12-Month ARR Forecast",
            xaxis_title="Months Forward",
            yaxis_title="ARR ($M)",
            height=400,
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        current_arr_m = current_arr / 1e6
        month_6_arr = forecast_df_custom[forecast_df_custom['Month'] == 6]['Projected ARR'].values[0]
        month_12_arr = forecast_df_custom[forecast_df_custom['Month'] == 12]['Projected ARR'].values[0]
        
        st.metric("Current ARR", f"${current_arr_m:.2f}M")
        st.metric("6-Month Projected ARR", f"${month_6_arr:.2f}M", delta=f"${month_6_arr - current_arr_m:.2f}M")
        st.metric("12-Month Projected ARR", f"${month_12_arr:.2f}M", delta=f"${month_12_arr - current_arr_m:.2f}M")
    
    st.markdown("**Key Assumptions:**")
    st.markdown(f"""
    - Current Churn Rate: {churn_rate*100:.1f}%
    - Current Expansion Rate: {expansion_rate*100:.1f}%
    - What-If Conversion Improvement: {pipeline_improvement}%
    """)

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
