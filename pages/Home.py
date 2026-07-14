"""
Home Page - Landing Page with Project Overview
"""

import streamlit as st
from utils.session import initialize_session_state

initialize_session_state()

st.markdown("""
    <style>
    .hero {
        padding: 40px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
    }
    
    .hero h1 {
        color: white;
        font-size: 3rem;
        margin-bottom: 20px;
    }
    
    .hero p {
        font-size: 1.2rem;
        margin-bottom: 20px;
    }
    
    .feature-box {
        background: #0d1117;
        padding: 20px;
        border-left: 4px solid #1f77b4;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
    
    <div class="hero">
        <h1>🏘️ Gurgaon Real Estate Market Analysis</h1>
        <p>Professional Portfolio Data Analytics Dashboard</p>
        <p>Comprehensive insights into Gurgaon's residential property market</p>
    </div>
""", unsafe_allow_html=True)

# Main content
st.markdown("## 📌 Project Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### What is This Project?
    
    This is a **professional data analytics application** showcasing comprehensive analysis 
    of the Gurgaon real estate market. Built with modern Python technologies, it demonstrates 
    advanced data analysis, visualization, and machine learning capabilities.
    
    ### Key Objectives
    - 📊 Analyze Gurgaon's property market trends
    - 💰 Identify pricing patterns and premium factors
    - 🏗️ Compare builders and localities
    - 🤖 Predict property prices using ML
    - 📈 Provide actionable business insights
    """)

with col2:
    st.markdown("""
    ### 🎯 Business Questions Answered
    
    1. Which properties command premium prices?
    2. How do locality and builder affect pricing?
    3. What's the RERA approval impact on prices?
    4. How does property status affect value?
    5. Which areas have highest growth potential?
    6. How do area and BHK impact rates?
    7. What are the market trends?
    """)

st.markdown("---")

# Features
st.markdown("## ✨ Dashboard Features")

feature_cols = st.columns(3)

features = [
    {
        "icon": "📊",
        "title": "Interactive Dashboard",
        "desc": "Real-time KPIs, filters, and dynamic visualizations"
    },
    {
        "icon": "📈",
        "title": "Detailed Analysis",
        "desc": "Comprehensive statistical analysis and trends"
    },
    {
        "icon": "💡",
        "title": "Business Insights",
        "desc": "Actionable insights with recommendations"
    },
    {
        "icon": "🤖",
        "title": "ML Predictions",
        "desc": "Price prediction using Linear Regression"
    },
    {
        "icon": "📊",
        "title": "Data Export",
        "desc": "Download filtered data and charts"
    },
    {
        "icon": "🔍",
        "title": "Advanced Search",
        "desc": "Filter by multiple criteria"
    }
]

for i, feature in enumerate(features):
    with feature_cols[i % 3]:
        st.markdown(f"""
        <div class="feature-box">
            <h3>{feature['icon']} {feature['title']}</h3>
            <p>{feature['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Tech Stack
st.markdown("## 🛠️ Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### Backend & Analysis
    - **Python** - Core language
    - **Pandas** - Data manipulation
    - **NumPy** - Numerical computing
    - **Scikit-learn** - Machine Learning
    """)

with col2:
    st.markdown("""
    ### Visualization
    - **Plotly** - Interactive charts
    - **Streamlit** - Web framework
    - **Seaborn** - Statistical viz
    - **Matplotlib** - Additional plots
    """)

with col3:
    st.markdown("""
    ### Development
    - **Python 3.8+**
    - **Git** - Version control
    - **GitHub** - Repository hosting
    - **LinkedIn** - Professional network
    """)

st.markdown("---")

# Quick Stats
st.markdown("## 📊 Dataset Snapshot")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Properties",
        f"{st.session_state.data_summary['total_properties']:,}",
        delta=None
    )

with col2:
    st.metric(
        "Average Price",
        f"₹{st.session_state.data_summary['avg_price']/10000000:.2f}Cr",
        delta=None
    )

with col3:
    st.metric(
        "Price Range",
        f"₹{st.session_state.data_summary['min_price']/10000000:.2f}Cr - ₹{st.session_state.data_summary['max_price']/10000000:.2f}Cr",
        delta=None
    )

with col4:
    st.metric(
        "Localities",
        f"{st.session_state.data_summary['total_localities']}",
        delta=None
    )

st.markdown("---")

# Call to Action
st.markdown("## 🚀 Get Started")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📊 View Dashboard", use_container_width=True):
        st.switch_page("pages/Dashboard.py")

with col2:
    if st.button("📈 See Analysis", use_container_width=True):
        st.switch_page("pages/Analysis.py")

with col3:
    if st.button("💡 Business Insights", use_container_width=True):
        st.switch_page("pages/Business_Insights.py")

with col4:
    if st.button("🤖 Try Prediction", use_container_width=True):
        st.switch_page("pages/Price_Predictor.py")

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; margin-top: 50px;'>
    <p><strong>Built by Harshjeet Chauhan ❤️ using Streamlit | Data Science Portfolio Project</strong></p>
    <p>For questions or collaboration: <a href='#'>Contact Me</a></p>
</div>
""", unsafe_allow_html=True)
