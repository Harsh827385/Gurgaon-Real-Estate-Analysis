"""
Business Insights Page - Key Business Questions and Insights
"""

import streamlit as st

from utils.session import initialize_session_state

initialize_session_state()

st.markdown("# 💡 Business Insights & Key Findings")

st.markdown("""
This page provides answers to critical business questions about the Gurgaon real estate market,
along with visualizations, detailed analysis, and actionable recommendations.
""")

st.markdown("---")

# Get business insights from session state
insights = st.session_state.business_insights

# Question 1: Costliest Flat
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🏆 Question 1")
        st.markdown("**What is the costliest property in the dataset?**")
    
    with col2:
        st.success(insights['costliest_flat']['answer'])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("BHK", f"{insights['costliest_flat']['bhk']} BHK")
    with col2:
        st.metric("Price", f"₹{insights['costliest_flat']['price_cr']:.2f} Cr")
    with col3:
        st.metric("Location", insights['costliest_flat']['locality'])
    
    st.markdown("""
    **Business Insight:** The luxury segment represents the highest value properties in the market.
    These ultra-premium properties command significant price premiums and are concentrated in
    specific high-end localities.
    
    **Recommendation:** Target ultra-high-net-worth individuals (UHNWI) for luxury segment marketing
    and positioning. These properties require specialized sales strategies and high-touch customer service.
    """)

st.markdown("---")

# Question 2: Highest Average Price Locality
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 📍 Question 2")
        st.markdown("**Which locality has the highest average price?**")
    
    with col2:
        st.success(insights['highest_avg_price_locality']['answer'])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "Locality",
            insights['highest_avg_price_locality']['locality']
        )
    with col2:
        st.metric(
            "Average Price",
            f"₹{insights['highest_avg_price_locality']['avg_price']/10000000:.2f} Cr"
        )
    
    st.markdown("""
    **Business Insight:** Certain localities command a significant price premium due to factors like
    proximity to city center, infrastructure development, and demand dynamics.
    
    **Recommendation:** Focus marketing efforts on positioning locality advantages. Consider location
    as a key selling point and benchmark against competitors in the same segment.
    """)

st.markdown("---")

# Question 3: Highest Rate Per Sqft
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 💹 Question 3")
        st.markdown("**Which locality has the highest rate per sqft?**")
    
    with col2:
        st.success(insights['highest_rate_locality']['answer'])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "Locality",
            insights['highest_rate_locality']['locality']
        )
    with col2:
        st.metric(
            "Rate/Sqft",
            f"₹{insights['highest_rate_locality']['rate']:,.0f}"
        )
    
    st.markdown("""
    **Business Insight:** Rate per sqft is a key efficiency metric. Higher rates in certain localities
    indicate better land utilization, demand, and pricing power.
    
    **Recommendation:** Use rate per sqft as a KPI for pricing optimization and inventory management.
    This metric helps compare properties across different sizes on a level playing field.
    """)

st.markdown("---")

# Question 4: Ready vs Under Construction
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🏗️ Question 4")
        st.markdown("**Do ready-to-move cost more than under-construction?**")
    
    with col2:
        st.success(insights['ready_vs_under']['answer'])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "Ready to Move",
            f"₹{insights['ready_vs_under']['ready_avg']/10000000:.2f} Cr"
        )
    with col2:
        st.metric(
            "Under Construction",
            f"₹{insights['ready_vs_under']['under_avg']/10000000:.2f} Cr"
        )
    
    st.markdown("""
    **Business Insight:** Property status (ready vs under construction) significantly impacts pricing.
    This reflects buyer preference, risk perception, and immediate occupancy value.
    
    **Recommendation:** Use status strategically in marketing. Under-construction projects can offer
    discounts to incentivize early bookings. Ready properties can command premium prices for
    immediate delivery assurance.
    """)

st.markdown("---")

# Question 5: RERA Premium
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### ✅ Question 5")
        st.markdown("**Do RERA-approved properties command a price premium?**")
    
    with col2:
        st.success(insights['rera_premium']['answer'])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "RERA Approved",
            f"₹{insights['rera_premium']['approved_avg']/10000000:.2f} Cr"
        )
    with col2:
        st.metric(
            "Not Approved",
            f"₹{insights['rera_premium']['not_approved_avg']/10000000:.2f} Cr"
        )
    with col3:
        st.metric(
            "Premium %",
            f"{insights['rera_premium']['premium']:.1f}%"
        )
    
    st.markdown("""
    **Business Insight:** RERA approval significantly impacts property value and buyer confidence.
    The premium reflects reduced regulatory risk and buyer protection benefits.
    
    **Recommendation:** Prioritize RERA registration for all projects. Highlight RERA approval
    prominently in marketing materials as a trust indicator. This can justify higher pricing.
    """)

st.markdown("---")

# Question 6: Expensive BHK
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🔑 Question 6")
        st.markdown("**Which BHK configuration is most expensive?**")
    
    with col2:
        st.success(insights['expensive_bhk']['answer'])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "BHK Configuration",
            f"{insights['expensive_bhk']['bhk']} BHK"
        )
    with col2:
        st.metric(
            "Rate/Sqft",
            f"₹{insights['expensive_bhk']['rate']:,.0f}"
        )
    
    st.markdown("""
    **Business Insight:** Certain BHK configurations have higher value per square foot,
    indicating stronger demand or premium positioning.
    
    **Recommendation:** Optimize product mix based on per-sqft returns. Market different BHK
    options to different buyer segments. Use pricing strategy to match BHK configuration with target demographics.
    """)

st.markdown("---")

# Question 7: Expensive Property Type
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🏠 Question 7")
        st.markdown("**Which property type is most expensive?**")
    
    with col2:
        st.success(insights['expensive_property_type']['answer'])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "Property Type",
            insights['expensive_property_type']['type'].title()
        )
    with col2:
        st.metric(
            "Rate/Sqft",
            f"₹{insights['expensive_property_type']['rate']:,.0f}"
        )
    
    st.markdown("""
    **Business Insight:** Different property types (apartments, plots, floors) command different
    premiums based on demand, construction complexity, and buyer preferences.
    
    **Recommendation:** Segment marketing by property type. Develop targeted positioning for each
    type. Consider buyer lifecycle: plots for investors, apartments for families, floors for luxury buyers.
    """)

st.markdown("---")

# Question 8: Top Builders
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🏢 Question 8")
        st.markdown("**Which builders price the highest?**")
    
    with col2:
        builders_str = ", ".join(insights['top_builders']['builders'])
        st.success(f"**Top 5 Builders:** {builders_str}")
    
    # Create a simple table for top builders
    builder_data = {
        'Builder': insights['top_builders']['builders'],
        'Rate/Sqft (₹)': [f"₹{rate:,.0f}" for rate in insights['top_builders']['rates']]
    }
    st.dataframe(builder_data, use_container_width=True)
    
    st.markdown("""
    **Business Insight:** Premium builders can command higher rates due to brand value,
    quality reputation, and execution excellence.
    
    **Recommendation:** Focus on brand building and quality delivery. Maintain transparency with
    customers. Premium builders should invest in brand differentiation and customer satisfaction.
    """)

st.markdown("---")

# Question 9: Area Impact
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 📏 Question 9")
        st.markdown("**How does area impact rate per sqft?**")
    
    with col2:
        correlation = insights['area_correlation']['correlation']
        relationship = "positive" if correlation > 0 else "negative"
        st.success(f"Correlation: {correlation:.3f} ({relationship})")
    
    st.metric(
        "Correlation Coefficient",
        f"{insights['area_correlation']['correlation']:.3f}"
    )
    
    st.markdown("""
    **Business Insight:** The relationship between area and rate per sqft indicates market segmentation.
    
    **Recommendation:**
    - If correlation is negative: Larger properties have lower per-sqft rates (bulk advantage)
    - If correlation is positive: Larger properties command premium per-sqft (luxury positioning)
    
    Use this insight for pricing optimization and market segmentation strategies.
    """)

st.markdown("---")

# Summary and Recommendations
st.markdown("## 🎯 Strategic Recommendations")

st.markdown("""
Based on the comprehensive analysis of the Gurgaon real estate market:

### 1. **Market Segmentation**
- Identify and target distinct buyer segments (budget, mid-range, luxury)
- Customize product offerings for each segment
- Use data-driven pricing strategies

### 2. **Location Strategy**
- Premium localities justify higher prices
- Focus on locality-specific marketing
- Highlight location benefits and infrastructure

### 3. **Product Positioning**
- Leverage RERA approval in marketing
- Differentiate based on property status (ready vs under construction)
- Optimize BHK mix based on demand

### 4. **Pricing Strategy**
- Use rate per sqft for competitive benchmarking
- Consider builder brand value in pricing
- Balance volume and margin across segments

### 5. **Risk Management**
- RERA approval reduces buyer risk - prioritize it
- Under-construction requires special buyer incentives
- Quality and brand building are long-term value drivers

### 6. **Market Opportunities**
- Growing demand in emerging localities
- Potential in underserved segments
- Digital marketing for builder brand building
""")

st.markdown("---")

# Methodology
with st.expander("📊 Analysis Methodology"):
    st.markdown("""
    ### Data Sources
    - Gurgaon Real Estate Dataset
    - Property transactions and listings
    - Market data from multiple builders
    
    ### Analysis Techniques
    - Descriptive Statistics
    - Comparative Analysis
    - Correlation Analysis
    - Market Segmentation
    
    ### Time Period
    - Current market snapshot
    - Representative of ongoing market dynamics
    
    ### Limitations
    - Sample represents available listings
    - Market conditions may vary
    - External factors may influence pricing
    """)
