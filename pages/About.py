"""
About Page - Project Information and Author Details
"""

import streamlit as st
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

st.markdown("# ℹ️ About This Project")

st.markdown("""
This is a **professional portfolio-level data analytics application** showcasing real-world
data analysis, visualization, and machine learning skills.
""")

st.markdown("---")

# Project Overview
st.markdown("## 📋 Project Overview")

st.markdown("""
### Gurgaon Real Estate Market Analysis

This project provides comprehensive analysis and insights into the Gurgaon real estate market.
It demonstrates advanced data science techniques applied to a real-world business problem.

**Dataset:** Gurgaon Residential Properties Market
- Properties across multiple localities
- Various configurations (BHK, floor type)
- Status (ready vs under construction)
- Builder and RERA information
""")

st.markdown("---")

# Features
st.markdown("## ✨ Key Features")

features = [
    ("Interactive Dashboard", "Real-time KPIs, filters, and visualizations"),
    ("Statistical Analysis", "Comprehensive market analysis and trends"),
    ("Business Insights", "Answers to key business questions"),
    ("ML Predictions", "Linear Regression-based price prediction"),
    ("Data Export", "Download filtered data and charts"),
    ("Professional UI", "Modern dark theme with responsive design"),
]

for feature, description in features:
    st.markdown(f"- **{feature}**: {description}")

st.markdown("---")

# Technology Stack
st.markdown("## 🛠️ Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### Core Languages
    - **Python** 3.8+
    - Pandas
    - NumPy
    """)

with col2:
    st.markdown("""
    ### Visualization & Web
    - **Streamlit** - Web Framework
    - **Plotly** - Interactive Charts
    - Seaborn
    - Matplotlib
    """)

with col3:
    st.markdown("""
    ### Machine Learning
    - **Scikit-learn** - Linear Regression
    - Statistical Analysis
    - Predictive Modeling
    """)

st.markdown("---")

# Project Structure
st.markdown("## 📁 Project Structure")

st.code("""
Gurgaon-Real-Estate-Analysis/
│
├── app.py                          # Main Streamlit entry point
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
│
├── dataset/
│   └── data.csv                   # Real estate dataset
│
├── pages/
│   ├── Home.py                    # Landing page
│   ├── Dashboard.py               # Interactive dashboard
│   ├── Analysis.py                # Statistical analysis
│   ├── Business_Insights.py       # Business questions
│   ├── Price_Predictor.py         # ML predictions
│   └── About.py                   # This page
│
├── utils/
│   ├── cleaning.py                # Data cleaning functions
│   ├── analysis.py                # Analysis functions
│   └── charts.py                  # Visualization functions
│
├── assets/
│   ├── logo.png                   # Project logo
│   └── banner.png                 # Banner image
│
└── screenshots/                   # Demo screenshots
""", language="text")

st.markdown("---")

# Key Metrics
st.markdown("## 📊 Dataset Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Properties", f"{len(st.session_state.df):,}")
    st.metric("Total Localities", f"{st.session_state.df['locality'].nunique()}")

with col2:
    st.metric("Total Builders", f"{st.session_state.df['company_name'].nunique()}")
    st.metric("Avg Price", f"₹{st.session_state.data_summary['avg_price']/10000000:.2f}Cr")

with col3:
    st.metric("Price Range", f"₹{st.session_state.data_summary['min_price']/10000000:.2f}Cr - ₹{st.session_state.data_summary['max_price']/10000000:.2f}Cr")
    st.metric("Avg Area", f"{st.session_state.data_summary['avg_area']:.0f} Sqft")

st.markdown("---")

# Skills Demonstrated
st.markdown("## 🎓 Skills Demonstrated")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Data Science Skills
    - ✅ Data Cleaning & Preprocessing
    - ✅ Exploratory Data Analysis (EDA)
    - ✅ Statistical Analysis
    - ✅ Data Visualization
    - ✅ Machine Learning
    - ✅ Feature Engineering
    """)

with col2:
    st.markdown("""
    ### Software Development Skills
    - ✅ Python Programming
    - ✅ Web Application Development
    - ✅ UI/UX Design
    - ✅ Code Organization & Documentation
    - ✅ Git & Version Control
    - ✅ Requirements Management
    """)

st.markdown("---")

# Business Value
st.markdown("## 💼 Business Value Delivered")

st.markdown("""
### Insights & Recommendations

1. **Market Segmentation**: Identified premium vs budget segments
2. **Pricing Strategy**: Data-driven pricing optimization recommendations
3. **Location Analysis**: Locality premium analysis for strategic positioning
4. **Builder Comparison**: Competitive builder analysis
5. **RERA Impact**: Quantified RERA approval value premium
6. **Status Analysis**: Ready vs under-construction pricing insights

### Applications

- Real Estate Professionals: Market analysis and pricing guidance
- Investors: Market opportunity identification
- Developers: Competitive benchmarking
- Buyers: Price validation and property comparison
""")

st.markdown("---")

# How to Use
st.markdown("## 🚀 How to Use This Application")

with st.expander("1️⃣ Setup & Installation", expanded=False):
    st.code("""
# Clone the repository
git clone https://github.com/yourname/Gurgaon-Real-Estate-Analysis.git

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
    """, language="bash")

with st.expander("2️⃣ Navigate the Dashboard", expanded=False):
    st.markdown("""
    - **Home**: Project overview and quick stats
    - **Dashboard**: Real-time KPIs and interactive filters
    - **Analysis**: Detailed statistical analysis
    - **Business Insights**: Key questions and insights
    - **Price Predictor**: ML-based price prediction
    - **About**: Project information
    """)

with st.expander("3️⃣ Tips for Best Results", expanded=False):
    st.markdown("""
    1. Use filters on the Dashboard to narrow down to specific segments
    2. Hover over charts for detailed information
    3. Compare multiple properties using the data table
    4. Check Business Insights for strategic recommendations
    5. Use Price Predictor for property valuation reference
    6. Download filtered data for further analysis
    """)

st.markdown("---")

# Author & Contact
st.markdown("## 👤 Author Information")

st.markdown("""
**Data Analyst & Full Stack Developer**

This portfolio project demonstrates:
- Advanced Python programming
- Data science capabilities
- Full-stack web development
- Professional UI/UX design
- Business analytics skills

### Let's Connect

- 📧 Email: your.email@example.com
- 💼 LinkedIn: [LinkedIn Profile](https://linkedin.com/in/yourprofile)
- 🐙 GitHub: [GitHub Profile](https://github.com/yourprofile)
- 🌐 Portfolio: [Your Website](https://yourwebsite.com)
""")

st.markdown("---")

# License
st.markdown("## 📜 License")

st.markdown("""
This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project with proper attribution.

### License Text

```
MIT License

Copyright (c) 2024 Data Analyst

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```
""")

st.markdown("---")

# Acknowledgments
st.markdown("## 🙏 Acknowledgments")

st.markdown("""
- **Streamlit**: For the amazing web framework
- **Plotly**: For interactive visualizations
- **Pandas & NumPy**: For data manipulation
- **Scikit-learn**: For machine learning capabilities
- **Data Contributors**: For the real estate market data
""")

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 50px;">
    <p><strong>Harshjeet Chauhan</strong></p>
</div>
""", unsafe_allow_html=True)
