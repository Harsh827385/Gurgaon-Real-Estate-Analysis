"""
Gurgaon Real Estate Market Analysis
Professional Portfolio Dashboard built with Streamlit

This application provides comprehensive analysis of the Gurgaon real estate market
with interactive visualizations, filters, and business insights.
"""

import streamlit as st
import pandas as pd
from pathlib import Path

from utils.session import initialize_session_state



# Page configuration
st.set_page_config(
    page_title="Gurgaon Real Estate Market Analysis",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Gurgaon Real Estate Market Analysis | Professional Data Analytics"
    }
)
initialize_session_state()

from utils.cleaning import load_data, clean_data

if "df" not in st.session_state:
    df = load_data("dataset/data.csv")
    df = clean_data(df)
    st.session_state.df = df
    
# Custom CSS for dark theme and professional styling
st.markdown("""
    <style>
    :root {
        --primary-color: #1f77b4;
        --background-color: #0e1117;
        --secondary-background-color: #161b22;
        --text-color: #c9d1d9;
    }
    
    [data-testid="stMetricDelta"] > div:nth-child(1) > div:nth-child(1) {
        font-size: 28px;
    }
    
    .stTabs [data-baseweb="tab-list"] button {
        font-weight: bold;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    
    h1 {
        color: #1f77b4;
        font-size: 2.5rem;
        font-weight: bold;
    }
    
    h2 {
        color: #1f77b4;
        font-size: 1.8rem;
    }
    
    h3 {
        color: #58a6ff;
        font-size: 1.3rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Import utilities
from utils.cleaning import load_data, clean_data, get_data_summary
from utils.analysis import get_business_questions, get_locality_analysis

def init_app():
    """Initialize app by loading data."""
    if 'df' not in st.session_state:
        try:
            data_path = Path(__file__).parent / 'dataset' / 'data.csv'
            st.session_state.df = clean_data(load_data(str(data_path)))
            st.session_state.data_summary = get_data_summary(st.session_state.df)
            st.session_state.business_insights = get_business_questions(st.session_state.df)
        except Exception as e:
            st.error(f"Error loading data: {str(e)}")
            return False
    return True

# Initialize the app
if not init_app():
    st.stop()

# Sidebar
with st.sidebar:
    st.title("🏢 Gurgaon Real Estate")
    st.markdown("---")
    
    # Navigation
    st.markdown("### Navigation")
    page = st.radio(
        "Select Page",
        ["🏠 Home", "📊 Dashboard", "📈 Analysis", "💡 Business Insights", "🤖 Price Predictor", "ℹ️ About"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Dataset info
    st.markdown("### Dataset Information")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Properties", f"{st.session_state.data_summary['total_properties']:,}")
    with col2:
        st.metric("Localities", f"{st.session_state.data_summary['total_localities']}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Builders", f"{st.session_state.data_summary['total_builders']}")
    with col2:
        st.metric("Avg Price", f"₹{st.session_state.data_summary['avg_price']/10000000:.2f}Cr")
    
    st.markdown("---")
    
    # Footer
    st.markdown("""
    **Built with:** Streamlit, Pandas, Plotly
    
    **Author:** Data Analyst
    
    **License:** MIT
    """)

# Page routing
if page == "🏠 Home":
    exec(open("pages/Home.py",encoding="utf-8").read())
elif page == "📊 Dashboard":
    exec(open("pages/Dashboard.py",encoding="utf-8").read())
elif page == "📈 Analysis":
    exec(open("pages/Analysis.py",encoding="utf-8").read())
elif page == "💡 Business Insights":
    exec(open("pages/Business_Insights.py",encoding="utf-8").read())
elif page == "🤖 Price Predictor":
    exec(open("pages/Price_Predictor.py",encoding="utf-8").read())
elif page == "ℹ️ About":
    exec(open("pages/About.py",encoding="utf-8").read())
