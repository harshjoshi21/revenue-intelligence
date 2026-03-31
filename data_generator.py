import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

def generate_saas_data(start_date='2023-01-01', end_date='2026-03-27', monthly_leads=1000):
    """
    Generate realistic SaaS funnel data with channel attribution,
    and customer lifecycle signals for RevOps/Growth Analytics.
    """
    
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    
    # Marketing channels
    channels = ['Organic Search', 'Paid Search', 'Content Marketing', 'Sales Outreach', 'Referral', 'LinkedIn Ads']
    channel_mix = [0.35, 0.25, 0.15, 0.15, 0.05, 0.05]
    
    # Customer segments
    segments = ['Healthcare', 'Finance', 'Tech/SaaS', 'Non-Profit', 'Manufacturing']
    segment_dist = [0.35, 0.25, 0.20, 0.15, 0.05]

    # Opportunity owners for pipeline execution attribution.
    opportunity_owners = [
        'A. Rivera',
        'J. Patel',
        'M. Thompson',
        'S. Kim',
        'R. Gupta',
        'T. Nguyen'
    ]
    owner_weights = [0.20, 0.18, 0.16, 0.16, 0.15, 0.15]
    
    # Deal sizes by segment (ARR)
    deal_sizes = {
        'Healthcare': (30000, 150000),
        'Finance': (40000, 200000),
        'Tech/SaaS': (20000, 100000),
        'Non-Profit': (15000, 80000),
        'Manufacturing': (25000, 120000)
    }
    
    # Sales cycle length (days) by segment
    sales_cycle = {
        'Healthcare': (60, 120),
        'Finance': (75, 150),
        'Tech/SaaS': (45, 90),
        'Non-Profit': (45, 90),
        'Manufacturing': (60, 120)
    }
    
    # Funnel conversion rates (realistic)
    conversion_rates = {
        'Lead to MQL': 0.30,
        'MQL to SQL': 0.25,
        'SQL to Opportunity': 0.40,
        'Opportunity to Won': 0.35
    }
    
    # Generate leads distributed across the date range
    date_range = pd.date_range(start, end, freq='D')
    n_days = len(date_range)
    n_leads = int(n_days / 30 * monthly_leads)
    
    lead_dates = [start + timedelta(days=int(x)) for x in np.random.choice(n_days, n_leads, replace=True)]
    lead_dates = sorted(lead_dates)
    
    leads_df = pd.DataFrame({
        'lead_id': [f'LEAD_{i:06d}' for i in range(len(lead_dates))],
        'lead_date': lead_dates,
        'channel': np.random.choice(channels, len(lead_dates), p=channel_mix),
        'segment': np.random.choice(segments, len(lead_dates), p=segment_dist)
    })
    
    # MQL conversion
    leads_df['is_mql'] = np.random.binomial(1, conversion_rates['Lead to MQL'], len(leads_df))
    leads_df['mql_date'] = leads_df.apply(
        lambda x: x['lead_date'] + timedelta(days=np.random.randint(1, 7)) if x['is_mql'] else pd.NaT,
        axis=1
    )
    
    # SQL conversion
    leads_df['is_sql'] = leads_df['is_mql'] & (np.random.binomial(1, conversion_rates['MQL to SQL'], len(leads_df)) == 1)
    leads_df['sql_date'] = leads_df.apply(
        lambda x: x['mql_date'] + timedelta(days=np.random.randint(3, 14)) if x['is_sql'] else pd.NaT,
        axis=1
    )
    
    # Opportunity conversion
    leads_df['is_opp'] = leads_df['is_sql'] & (np.random.binomial(1, conversion_rates['SQL to Opportunity'], len(leads_df)) == 1)
    leads_df['opp_date'] = leads_df.apply(
        lambda x: x['sql_date'] + timedelta(days=np.random.randint(7, 21)) if x['is_opp'] else pd.NaT,
        axis=1
    )
    leads_df['opportunity_owner'] = None
    opp_indices = leads_df.index[leads_df['is_opp']]
    if len(opp_indices) > 0:
        leads_df.loc[opp_indices, 'opportunity_owner'] = np.random.choice(
            opportunity_owners,
            len(opp_indices),
            p=owner_weights
        )
    
    # Opportunity lifecycle: opportunities can remain open or close as won/lost within the observed window.
    leads_df['opp_decision_days'] = leads_df.apply(
        lambda x: np.random.randint(sales_cycle[x['segment']][0], sales_cycle[x['segment']][1]) if x['is_opp'] else np.nan,
        axis=1
    )
    leads_df['opp_decision_date'] = leads_df.apply(
        lambda x: x['opp_date'] + timedelta(days=int(x['opp_decision_days'])) if x['is_opp'] else pd.NaT,
        axis=1
    )
    leads_df['is_closed'] = leads_df['is_opp'] & (leads_df['opp_decision_date'] <= end)

    won_draw = np.random.binomial(1, conversion_rates['Opportunity to Won'], len(leads_df)) == 1
    leads_df['is_won'] = leads_df['is_closed'] & won_draw
    leads_df['is_lost'] = leads_df['is_closed'] & (~leads_df['is_won'])

    leads_df['won_date'] = leads_df.apply(
        lambda x: x['opp_decision_date'] if x['is_won'] else pd.NaT,
        axis=1
    )
    leads_df['lost_date'] = leads_df.apply(
        lambda x: x['opp_decision_date'] if x['is_lost'] else pd.NaT,
        axis=1
    )
    leads_df['opp_close_date'] = leads_df['won_date'].fillna(leads_df['lost_date'])

    loss_reasons = ['Price', 'No Decision', 'Lost to Competitor', 'Timing', 'Feature Gap']
    loss_reason_weights = [0.28, 0.24, 0.22, 0.16, 0.10]
    leads_df['loss_reason'] = None
    lost_indices = leads_df.index[leads_df['is_lost']]
    if len(lost_indices) > 0:
        leads_df.loc[lost_indices, 'loss_reason'] = np.random.choice(
            loss_reasons,
            len(lost_indices),
            p=loss_reason_weights
        )

    leads_df['opp_status'] = np.select(
        [
            ~leads_df['is_opp'],
            leads_df['is_won'],
            leads_df['is_lost']
        ],
        [
            'No Opportunity',
            'Closed Won',
            'Closed Lost'
        ],
        default='Open'
    )
    
    # ARR for won deals
    leads_df['arr'] = leads_df.apply(
        lambda x: np.random.randint(deal_sizes[x['segment']][0], deal_sizes[x['segment']][1]) if x['is_won'] else 0,
        axis=1
    )
    
    # Create customers (won deals become active customers)
    customers_df = leads_df[leads_df['is_won'] == True].copy()
    customers_df['customer_id'] = [f'CUST_{i:05d}' for i in range(len(customers_df))]
    customers_df['start_date'] = customers_df['won_date']
    customers_df['tenure_months'] = customers_df['start_date'].apply(
        lambda x: (pd.to_datetime(end_date) - x).days / 30 if pd.notna(x) else 0
    )
    
    # Customer health signals
    # Feature adoption breadth (0-10 features)
    customers_df['features_adopted'] = np.random.randint(1, 11, len(customers_df))
    customers_df['features_adopted'] = customers_df['features_adopted'].clip(lower=customers_df['tenure_months'] / 12)
    
    # Monthly active users (% of team)
    customers_df['mau_adoption'] = np.random.uniform(0.2, 1.0, len(customers_df))
    
    # Support ticket sentiment (% positive)
    customers_df['support_sentiment'] = np.random.uniform(0.4, 1.0, len(customers_df))
    
    # Engagement score (0-100)
    customers_df['engagement_score'] = (
        (customers_df['features_adopted'] / 10 * 0.3 +
         customers_df['mau_adoption'] * 0.4 +
         customers_df['support_sentiment'] * 0.3) * 100
    ).round(0)
    
    # Churn prediction (based on engagement, tenure, feature adoption)
    customers_df['churn_risk'] = (
        100 - customers_df['engagement_score'] +
        np.random.normal(0, 15, len(customers_df))
    ).clip(0, 100)
    
    # Actual churn (small % of customers)
    churn_probability = 0.08  # Cohort-level churn incidence probability in the simulated window
    customers_df['is_churned'] = np.random.binomial(1, churn_probability, len(customers_df))
    customers_df['churn_date'] = customers_df.apply(
        lambda x: x['start_date'] + timedelta(days=np.random.randint(60, max(61, int(x['tenure_months'] * 30)))) 
        if x['is_churned'] else pd.NaT,
        axis=1
    )
    
    # Expansion revenue (% of ARR)
    customers_df['expansion_arr'] = customers_df.apply(
        lambda x: x['arr'] * np.random.uniform(0, 0.5) if x['is_churned'] == 0 else 0,
        axis=1
    ).round(0)
    
    # NRR calculation (simplified)
    customers_df['nrr_contribution'] = (customers_df['arr'] + customers_df['expansion_arr']) / customers_df['arr']
    customers_df['nrr_contribution'] = customers_df['nrr_contribution'].fillna(0)
    
    # Cohort (quarter + year)
    customers_df['cohort'] = customers_df['won_date'].dt.to_period('Q').astype(str)
    
    return leads_df, customers_df


def generate_forecast(customers_df, months_forward=6):
    """
    Generate simple forward-looking forecast for ARR, churn, and expansion.
    """
    
    current_arr = customers_df[customers_df['is_churned'] == 0]['arr'].sum()
    current_expansion = customers_df[customers_df['is_churned'] == 0]['expansion_arr'].sum()
    avg_churn_rate = customers_df['is_churned'].mean()
    avg_expansion_rate = (customers_df['expansion_arr'].sum() / customers_df['arr'].sum()) if customers_df['arr'].sum() > 0 else 0
    
    forecast_data = []
    for month in range(months_forward):
        projected_arr = current_arr * (1 - avg_churn_rate) ** month * (1 + avg_expansion_rate) ** month
        forecast_data.append({
            'month': month,
            'projected_arr': projected_arr,
            'projected_churn': current_arr * avg_churn_rate * (1 - avg_churn_rate) ** month,
            'projected_expansion': projected_arr * avg_expansion_rate
        })
    
    return pd.DataFrame(forecast_data)


if __name__ == '__main__':
    leads_df, customers_df = generate_saas_data()
    print(f"Generated {len(leads_df)} leads")
    print(f"Generated {len(customers_df)} customers")
    print(customers_df.head())
