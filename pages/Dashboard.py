"""
Dashboard Page - KPIs and Interactive Filters
"""

import streamlit as st
import pandas as pd
from utils.session import initialize_session_state

initialize_session_state()
from utils.charts import (
    create_price_distribution_histogram,
    create_bhk_distribution_bar,
    create_property_type_bar,
    create_status_pie,
    create_rera_pie,
    create_top_localities_bar,
    create_top_builders_bar
)

st.markdown("# 📊 Interactive Dashboard")

# Key Performance Indicators
st.markdown("## 🎯 Key Performance Indicators (KPIs)")

kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

with kpi_col1:
    st.metric(
        "Total Properties",
        f"{len(st.session_state.df):,}",
        f"₹{st.session_state.data_summary['avg_price']/10000000:.2f}Cr Avg"
    )

with kpi_col2:
    st.metric(
        "Average Price",
        f"₹{st.session_state.data_summary['avg_price']/10000000:.2f}Cr",
        f"Min: ₹{st.session_state.data_summary['min_price']/10000000:.2f}Cr"
    )

with kpi_col3:
    st.metric(
        "Maximum Price",
        f"₹{st.session_state.data_summary['max_price']/10000000:.2f}Cr",
        f"Median: ₹{st.session_state.data_summary['median_price']/10000000:.2f}Cr"
    )

with kpi_col4:
    st.metric(
        "Avg Rate/Sqft",
        f"₹{st.session_state.data_summary['avg_rate_per_sqft']:,.0f}",
        f"Total Builders: {st.session_state.data_summary['total_builders']}"
    )

st.markdown("---")

# Filters
st.markdown("## 🔍 Interactive Filters")

# Create columns for filters
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    selected_locality = st.multiselect(
        "Locality",
        options=sorted(st.session_state.df['locality'].unique()),
        default=None,
        key="filter_locality"
    )

with col2:
    selected_bhk = st.multiselect(
        "BHK",
        options=sorted(st.session_state.df['bhk_count'].unique()),
        default=None,
        key="filter_bhk"
    )

with col3:
    selected_property_type = st.multiselect(
        "Property Type",
        options=st.session_state.df['flat_type'].unique(),
        default=None,
        key="filter_property_type"
    )

with col4:
    selected_status = st.multiselect(
        "Status",
        options=st.session_state.df['status'].unique(),
        default=None,
        key="filter_status"
    )

with col5:
    selected_rera = st.multiselect(
        "RERA Approval",
        options=st.session_state.df['rera_approval'].unique(),
        default=None,
        key="filter_rera"
    )

# Price and Area range sliders
col1, col2 = st.columns(2)

with col1:
    price_range = st.slider(
        "Price Range (₹)",
        min_value=float(st.session_state.df['price'].min()),
        max_value=float(st.session_state.df['price'].max()),
        value=(float(st.session_state.df['price'].min()), float(st.session_state.df['price'].max())),
        step=100000.0
    )

with col2:
    area_range = st.slider(
        "Area Range (sqft)",
        min_value=float(st.session_state.df['area'].min()),
        max_value=float(st.session_state.df['area'].max()),
        value=(float(st.session_state.df['area'].min()), float(st.session_state.df['area'].max())),
        step=100.0
    )

# Apply filters
filtered_df = st.session_state.df.copy()

if selected_locality:
    filtered_df = filtered_df[filtered_df['locality'].isin(selected_locality)]
if selected_bhk:
    filtered_df = filtered_df[filtered_df['bhk_count'].isin(selected_bhk)]
if selected_property_type:
    filtered_df = filtered_df[filtered_df['flat_type'].isin(selected_property_type)]
if selected_status:
    filtered_df = filtered_df[filtered_df['status'].isin(selected_status)]
if selected_rera:
    filtered_df = filtered_df[filtered_df['rera_approval'].isin(selected_rera)]

# Price range filter
filtered_df = filtered_df[(filtered_df['price'] >= price_range[0]) & (filtered_df['price'] <= price_range[1])]
# Area range filter
filtered_df = filtered_df[(filtered_df['area'] >= area_range[0]) & (filtered_df['area'] <= area_range[1])]

# Display filtered count
st.info(f"📊 **Showing {len(filtered_df):,} properties** (Filtered from {len(st.session_state.df):,})")

st.markdown("---")

# Charts
st.markdown("## 📈 Market Analysis Charts")

# Row 1 - Distribution Charts
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        create_price_distribution_histogram(filtered_df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        create_bhk_distribution_bar(filtered_df),
        use_container_width=True
    )

# Row 2 - Property Analysis
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        create_property_type_bar(filtered_df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        create_status_pie(filtered_df),
        use_container_width=True
    )

# Row 3 - Status Analysis
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        create_rera_pie(filtered_df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        create_top_localities_bar(filtered_df, top_n=12),
        use_container_width=True
    )

st.markdown("---")

# Row 4 - Builders
st.plotly_chart(
    create_top_builders_bar(filtered_df, top_n=15),
    use_container_width=True
)

st.markdown("---")

# Data Table
st.markdown("## 📋 Filtered Data Table")

# Sort and display options
col1, col2, col3 = st.columns(3)

with col1:
    sort_by = st.selectbox(
        "Sort by",
        options=['Price (Descending)', 'Price (Ascending)', 'Area (Descending)', 'Area (Ascending)', 'Rate/Sqft (Descending)'],
        key="sort_by"
    )

with col2:
    display_cols = st.multiselect(
        "Display Columns",
        options=filtered_df.columns.tolist(),
        default=['locality', 'bhk_count', 'flat_type', 'price', 'area', 'rate_per_sqft', 'status', 'company_name'],
        key="display_cols"
    )

with col3:
    rows_to_show = st.selectbox(
        "Show rows",
        options=[10, 25, 50, 100, 'All'],
        index=1,
        key="rows_show"
    )

# Sort dataframe
if sort_by == 'Price (Descending)':
    display_df = filtered_df.sort_values('price', ascending=False)
elif sort_by == 'Price (Ascending)':
    display_df = filtered_df.sort_values('price', ascending=True)
elif sort_by == 'Area (Descending)':
    display_df = filtered_df.sort_values('area', ascending=False)
elif sort_by == 'Area (Ascending)':
    display_df = filtered_df.sort_values('area', ascending=True)
else:
    display_df = filtered_df.sort_values('rate_per_sqft', ascending=False)

# Display rows
if rows_to_show != 'All':
    display_df = display_df.head(rows_to_show)

# Format price and rate columns for display
display_df_formatted = display_df[display_cols].copy()
if 'price' in display_df_formatted.columns:
    display_df_formatted['price'] = display_df_formatted['price'].apply(lambda x: f"₹{x:,.0f}")
if 'rate_per_sqft' in display_df_formatted.columns:
    display_df_formatted['rate_per_sqft'] = display_df_formatted['rate_per_sqft'].apply(lambda x: f"₹{x:,.0f}")

st.dataframe(display_df_formatted, use_container_width=True)

# Download button
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Filtered Data (CSV)",
        data=csv,
        file_name="gurgaon_properties.csv",
        mime="text/csv",
        use_container_width=True
    )

with col2:
    excel = pd.ExcelWriter('temp.xlsx', engine='openpyxl')
    filtered_df.to_excel(excel, index=False)
    with open('temp.xlsx', 'rb') as f:
        st.download_button(
            label="📥 Download Filtered Data (Excel)",
            data=f,
            file_name="gurgaon_properties.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )

with col3:
    st.info("💡 Use the filters above to explore the data by different criteria", icon="ℹ️")
