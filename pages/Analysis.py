"""
Analysis Page - Detailed Statistical Analysis
"""

import streamlit as st

from utils.session import initialize_session_state
# Hide Streamlit toolbar and header
st.markdown("""
<style>
[data-testid="stToolbar"] {
    display: none !important;
}

[data-testid="stDecoration"] {
    display: none !important;
}

[data-testid="stStatusWidget"] {
    visibility: hidden !important;
}

header {
    visibility: hidden !important;
    height: 0px !important;
}
</style>
""", unsafe_allow_html=True)

initialize_session_state()
from utils.analysis import (
    get_locality_analysis,
    get_builder_analysis,
    get_bhk_analysis,
    get_property_type_analysis,
    get_status_analysis,
    get_rera_analysis,
    get_price_statistics
)
from utils.charts import (
    create_scatter_area_vs_price,
    create_scatter_area_vs_rate,
    create_correlation_heatmap,
    create_price_by_status_bar,
    create_rera_vs_price_bar,
    create_top_localities_treemap,
    create_bhk_by_property_type,
    create_bhk_vs_price_box,
    create_builder_comparison_bar
)

st.markdown("# 📈 Detailed Market Analysis")

# Price Statistics
st.markdown("## 💰 Price Statistics")

price_stats = get_price_statistics(st.session_state.df)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Mean Price", f"₹{price_stats['mean']/10000000:.2f}Cr")

with col2:
    st.metric("Median Price", f"₹{price_stats['median']/10000000:.2f}Cr")

with col3:
    st.metric("Std Deviation", f"₹{price_stats['std']/10000000:.2f}Cr")

with col4:
    st.metric("Min Price", f"₹{price_stats['min']/10000000:.2f}Cr")

with col5:
    st.metric("Max Price", f"₹{price_stats['max']/10000000:.2f}Cr")

st.markdown("---")

# Tabs for different analyses
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📍 Locality Analysis",
    "🏢 Builder Analysis",
    "🔑 BHK Analysis",
    "🏠 Property Type",
    "Status Analysis",
    "RERA Analysis"
])

# Locality Analysis
with tab1:
    st.markdown("## 📍 Locality Analysis")
    
    top_n = st.slider("Top N Localities", 5, 20, 10, key="locality_top_n")
    locality_analysis = get_locality_analysis(st.session_state.df, top_n=top_n)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(locality_analysis, use_container_width=True)
    
    with col2:
        st.plotly_chart(
            create_top_localities_treemap(st.session_state.df),
            use_container_width=True
        )
    
    st.markdown("### Key Insights")
    highest_locality = locality_analysis.index[0]
    highest_price = locality_analysis['Avg Price'].iloc[0]
    st.info(f"""
    - **Highest Average Price**: {highest_locality} (₹{highest_price:,.0f})
    - **Total Localities**: {st.session_state.df['locality'].nunique()}
    - **Premium Localities**: {len(locality_analysis[locality_analysis['Avg Price'] > st.session_state.df['price'].mean()])} above market average
    """)

# Builder Analysis
with tab2:
    st.markdown("## 🏢 Builder Analysis")
    
    top_n = st.slider("Top N Builders", 5, 20, 10, key="builder_top_n")
    builder_analysis = get_builder_analysis(st.session_state.df, top_n=top_n)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(builder_analysis, use_container_width=True)
    
    with col2:
        st.plotly_chart(
            create_builder_comparison_bar(st.session_state.df, top_n=top_n),
            use_container_width=True
        )
    
    st.markdown("### Key Insights")
    st.info(f"""
    - **Total Builders**: {st.session_state.df['company_name'].nunique()}
    - **Top Builder**: {builder_analysis.index[0]} (Avg Price: ₹{builder_analysis['Avg Price'].iloc[0]:,.0f})
    - **Price Range (Top 10)**: ₹{builder_analysis['Avg Price'].min():,.0f} - ₹{builder_analysis['Avg Price'].max():,.0f}
    """)

# BHK Analysis
with tab3:
    st.markdown("## 🔑 BHK Analysis")
    
    bhk_analysis = get_bhk_analysis(st.session_state.df)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(bhk_analysis, use_container_width=True)
    
    with col2:
        st.plotly_chart(
            create_bhk_vs_price_box(st.session_state.df),
            use_container_width=True
        )
    
    st.plotly_chart(
        create_bhk_by_property_type(st.session_state.df),
        use_container_width=True
    )
    
    st.markdown("### Key Insights")
    st.info(f"""
    - **Average BHK Count**: {st.session_state.df['bhk_count'].mean():.1f}
    - **Most Common**: {st.session_state.df['bhk_count'].mode()[0]} BHK
    - **Price Premium**: {((bhk_analysis['Avg Price'].max() / bhk_analysis['Avg Price'].min() - 1) * 100):.1f}% between highest and lowest BHK
    """)

# Property Type Analysis
with tab4:
    st.markdown("## 🏠 Property Type Analysis")
    
    prop_analysis = get_property_type_analysis(st.session_state.df)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(prop_analysis, use_container_width=True)
    
    with col2:
        # Create a simple bar chart for property types
        st.bar_chart(prop_analysis['Avg Price'])
    
    st.markdown("### Key Insights")
    highest_prop = prop_analysis['Avg Price'].idxmax()
    highest_prop_price = prop_analysis['Avg Price'].max()
    st.info(f"""
    - **Most Expensive Type**: {highest_prop.title()} (Avg: ₹{highest_prop_price:,.0f})
    - **Total Types**: {len(prop_analysis)}
    - **Most Available**: {prop_analysis['Count'].idxmax().title()} ({prop_analysis['Count'].max():,.0f} properties)
    """)

# Status Analysis
with tab5:
    st.markdown("## Status Analysis (Ready vs Under Construction)")
    
    status_analysis = get_status_analysis(st.session_state.df)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(status_analysis, use_container_width=True)
    
    with col2:
        st.plotly_chart(
            create_price_by_status_bar(st.session_state.df),
            use_container_width=True
        )
    
    st.markdown("### Key Insights")
    ready_count = status_analysis.loc['ready to move', 'Count'] if 'ready to move' in status_analysis.index else 0
    under_count = status_analysis.loc['under construction', 'Count'] if 'under construction' in status_analysis.index else 0
    st.info(f"""
    - **Ready to Move**: {ready_count:,.0f} properties
    - **Under Construction**: {under_count:,.0f} properties
    - **Market Split**: {(ready_count/(ready_count+under_count)*100):.1f}% Ready, {(under_count/(ready_count+under_count)*100):.1f}% Under Construction
    """)

# RERA Analysis
with tab6:
    st.markdown("## RERA Approval Analysis")
    
    rera_analysis = get_rera_analysis(st.session_state.df)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(rera_analysis, use_container_width=True)
    
    with col2:
        st.plotly_chart(
            create_rera_vs_price_bar(st.session_state.df),
            use_container_width=True
        )
    
        st.markdown("### Key Insights")
    approved_count = rera_analysis.loc['Approved', 'Count'] if 'Approved' in rera_analysis.index else 0
    not_approved_count = rera_analysis.loc['Not Approved', 'Count'] if 'Not Approved' in rera_analysis.index else 0

    approved_price = rera_analysis.loc['Approved', 'Avg Price'] if 'Approved' in rera_analysis.index else 0
    not_approved_price = rera_analysis.loc['Not Approved', 'Avg Price'] if 'Not Approved' in rera_analysis.index else 0

    premium = ((approved_price / not_approved_price - 1) * 100) if not_approved_price > 0 else 0

    st.info(f"""
    - **RERA Approved**: {approved_count:,.0f} properties (Avg: ₹{approved_price:,.0f})
    - **Not Approved**: {not_approved_count:,.0f} properties (Avg: ₹{not_approved_price:,.0f})
    - **Price Premium**: {premium:.1f}% for RERA-approved properties
    """)  

st.markdown("---")

# Correlation Analysis
st.markdown("## 🔗 Correlation Analysis")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        create_correlation_heatmap(st.session_state.df),
        use_container_width=True
    )

with col2:
    st.markdown("""
    ### Correlation Interpretation
    
    The correlation matrix shows relationships between key variables:
    
    - **Price vs Area**: Shows how property size affects price
    - **Price vs Rate/Sqft**: Indicates pricing efficiency
    - **Price vs BHK**: Demonstrates BHK impact on price
    - **Area vs Rate/Sqft**: Shows if larger properties have different pricing
    
    Values range from -1 (negative correlation) to +1 (positive correlation).
    """)

st.markdown("---")

# Scatter Plots
st.markdown("## 📊 Detailed Scatter Analysis")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        create_scatter_area_vs_price(st.session_state.df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        create_scatter_area_vs_rate(st.session_state.df),
        use_container_width=True
    )

st.markdown("""
**Insights from Scatter Plots:**
- Hover over points to see property details
- Size represents rate per sqft
- Color represents BHK count
- Look for clusters to identify market segments
""")
