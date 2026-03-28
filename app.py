# TAB 4: FORECAST
with tab4:
    st.subheader("ARR Forecast & Growth Projections")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Build forecast with what-if impact
        current_arr = customers_filtered[customers_filtered['is_churned'] == 0]['arr'].sum()
        churn_rate = customers_filtered['is_churned'].mean()
        expansion_rate = (customers_filtered['expansion_arr'].sum() / customers_filtered['arr'].sum()) if customers_filtered['arr'].sum() > 0 else 0
        
        forecast_months = 13  # Changed to 13 so we get months 0-12
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
            height=400
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
st.markdown("""
    <div style='text-align: center; color: #888; font-size: 12px; padding-top: 20px;'>
    Built for RevOps and Growth Leaders | Data refreshed: """ + datetime.now().strftime("%Y-%m-%d %H:%M") + """
    </div>
""", unsafe_allow_html=True)
