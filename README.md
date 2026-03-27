# Revenue Intelligence Dashboard

A data-driven RevOps and Growth Analytics tool that provides real-time visibility across your SaaS funnel, customer health, expansion opportunities, and forward-looking forecasts.

## Features

**📈 Sales Funnel Analysis**
- Visualize conversion rates at each stage (Leads → MQLs → SQLs → Opportunities → Won)
- Identify stuck deals by marketing channel
- Drill down into specific channels to see individual opportunities

**⚠️ Customer Health & Churn Risk**
- Heat map of churn risk across customer segments
- Engagement vs. churn scatter plot to identify at-risk customers
- Actionable list of customers requiring intervention
- Signals: engagement score, feature adoption, support sentiment

**💰 Expansion & Cohort Analysis**
- Base vs. expansion ARR breakdown by segment
- Cohort retention curves over time
- Track which cohorts are expanding fastest

**🔮 ARR Forecast**
- 12-month forward projection based on churn and expansion trends
- What-if scenarios: test impact of improving sales conversion
- Forecast adjusts automatically with your filters

## Key Metrics at a Glance

- **Active Customers**: Number of current customers (not churned)
- **Current ARR**: Total annual recurring revenue from active customers
- **Churn Rate**: Percentage of customers lost (all-time)
- **NRR**: Net Revenue Retention (expansion revenue / base revenue)

## How to Use

### Filters & What-If Analysis (Left Sidebar)
- **Date Range**: Focus on a specific time period
- **Marketing Channels**: Filter by organic search, paid ads, referrals, etc.
- **Customer Segments**: Drill into healthcare, finance, tech, non-profit, manufacturing
- **What-If Slider**: Test impact of improving SQL→Won conversion rate

### Drilling Into the Data
1. **Funnel Tab**: Click into stuck opportunities by channel to identify bottlenecks
2. **Churn Tab**: See individual at-risk customers and their engagement signals
3. **Expansion Tab**: Understand which segments and cohorts are expanding
4. **Forecast Tab**: Model future ARR under different scenarios

## Data Simulation

This dashboard uses realistic SaaS funnel data:
- **1000+ leads/month** across 6 marketing channels
- **200+ active customers** across 5 industry segments
- **Deal sizes**: $15K–$200K ARR (realistic for mid-market/enterprise)
- **Sales cycles**: 45–150 days depending on segment
- **Churn patterns**: 8% monthly churn, influenced by engagement
- **Expansion**: 10–50% ARR expansion from existing customers

All data is statistically realistic and includes seasonality.

## Use Cases

**For RevOps teams:**
- Identify pipeline bottlenecks and stuck deals
- Forecast revenue with confidence
- Detect early churn signals before they become problems

**For Growth leaders:**
- Understand which channels and segments drive expansion
- Model impact of improving conversion rates
- Make data-driven decisions on customer prioritization

**For Customer Success:**
- Find at-risk customers needing intervention
- Understand which engagement signals predict churn
- Track cohort retention over time

## Technical Stack

- **Streamlit**: Interactive dashboard framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **NumPy**: Numerical simulation

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deployment

Deploy to Streamlit Cloud, Heroku, or any cloud platform that supports Python.

---

**Built for RevOps leaders and growth-focused teams.**
