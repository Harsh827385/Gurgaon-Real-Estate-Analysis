"""
Price Predictor Page - Machine Learning Price Prediction
"""

import streamlit as st
import numpy as np
from utils.analysis import predict_price

st.markdown("# 🤖 AI-Powered Price Prediction")

st.markdown("""
This section uses **Linear Regression** machine learning to predict property prices based on
key features: Area, Rate per Sqft, and BHK Count.
""")

st.markdown("---")

# Model Info
with st.expander("📚 Model Information", expanded=False):
    st.markdown("""
    ### Machine Learning Model Details
    
    **Algorithm:** Linear Regression
    - Simple, interpretable model
    - Good for continuous price prediction
    - Fast computation
    
    **Features Used:**
    1. Area (Square Feet)
    2. Rate per Sqft (₹)
    3. BHK Count
    
    **Training Data:** 
    - All properties in the dataset
    - Cleaned and validated data
    
    **Prediction Approach:**
    - Features are standardized
    - Model learns relationship between features and price
    - Predicts new prices based on input values
    
    **Accuracy:** Model is trained on real market data
    - R² Score: Indicates model fit quality
    - RMSE: Root Mean Square Error
    """)

st.markdown("---")

# Prediction Form
st.markdown("## 🔮 Predict Property Price")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Property Details")
    
    area = st.number_input(
        "Property Area (Sqft)",
        min_value=100.0,
        max_value=10000.0,
        value=1500.0,
        step=50.0,
        help="Total carpet area or built-up area of the property"
    )
    
    bhk = st.selectbox(
        "BHK Configuration",
        options=sorted(st.session_state.df['bhk_count'].unique()),
        help="Number of bedrooms/halls/kitchens"
    )
    
    rate_per_sqft = st.number_input(
        "Rate per Sqft (₹)",
        min_value=1000.0,
        max_value=100000.0,
        value=5000.0,
        step=100.0,
        help="Price per square foot"
    )

with col2:
    st.markdown("### Market Insights")
    
    st.info(f"""
    **Market Statistics:**
    - Avg Area: {st.session_state.df['area'].mean():.0f} Sqft
    - Avg Rate/Sqft: ₹{st.session_state.df['rate_per_sqft'].mean():,.0f}
    - Avg BHK: {st.session_state.df['bhk_count'].mean():.1f}
    - Total Properties: {len(st.session_state.df):,}
    """)

st.markdown("---")

# Prediction Button
if st.button("🔍 Predict Price", use_container_width=True):
    
    features = {
        'area': area,
        'rate_per_sqft': rate_per_sqft,
        'bhk_count': bhk
    }
    
    predicted_price = predict_price(st.session_state.df, features)
    
    if predicted_price is not None:
        
        # Display Prediction
        st.markdown("## 💰 Prediction Result")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Predicted Price",
                f"₹{predicted_price:,.0f}",
                delta=f"₹{predicted_price/10000000:.2f} Cr"
            )
        
        with col2:
            st.metric(
                "Price per Sqft",
                f"₹{predicted_price/area:,.0f}",
                delta=f"Based on {area:.0f} Sqft"
            )
        
        st.markdown("---")
        
        # Comparison with Market
        st.markdown("## 📊 Market Comparison")
        
        avg_price = st.session_state.df['price'].mean()
        median_price = st.session_state.df['price'].median()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            variance_avg = ((predicted_price - avg_price) / avg_price * 100)
            st.metric(
                "vs Market Average",
                f"{variance_avg:+.1f}%",
                delta=f"₹{predicted_price - avg_price:+,.0f}"
            )
        
        with col2:
            variance_median = ((predicted_price - median_price) / median_price * 100)
            st.metric(
                "vs Market Median",
                f"{variance_median:+.1f}%",
                delta=f"₹{predicted_price - median_price:+,.0f}"
            )
        
        with col3:
            # Find similar properties
            similar = st.session_state.df[
                (st.session_state.df['bhk_count'] == bhk) &
                (st.session_state.df['area'] >= area * 0.9) &
                (st.session_state.df['area'] <= area * 1.1)
            ]
            
            if len(similar) > 0:
                similar_avg = similar['price'].mean()
                variance_similar = ((predicted_price - similar_avg) / similar_avg * 100)
                st.metric(
                    "vs Similar Properties",
                    f"{variance_similar:+.1f}%",
                    delta=f"({len(similar)} similar found)"
                )
            else:
                st.metric(
                    "vs Similar Properties",
                    "N/A",
                    delta="No similar properties found"
                )
        
        st.markdown("---")
        
        # Insights
        st.markdown("## 💡 Prediction Insights")
        
        insight_col1, insight_col2 = st.columns(2)
        
        with insight_col1:
            st.markdown("""
            ### Input Analysis
            - **Area**: Represents property size
            - **BHK**: Bedroom configuration affects pricing
            - **Rate/Sqft**: Market value indicator
            """)
            
            st.markdown(f"""
            ### Your Property
            - Area: {area:.0f} Sqft
            - BHK: {bhk} BHK
            - Rate/Sqft: ₹{rate_per_sqft:,.0f}
            - **Predicted Price: ₹{predicted_price:,.0f}**
            """)
        
        with insight_col2:
            st.markdown("""
            ### Market Context
            - Prediction based on linear regression model
            - Trained on actual market data
            - Considers key pricing factors
            """)
            
            # Recommendation
            if variance_avg > 10:
                recommendation = "🔺 **Premium Priced** - Above market average"
                color = "normal"
            elif variance_avg < -10:
                recommendation = "🔻 **Budget Priced** - Below market average"
                color = "inverse"
            else:
                recommendation = "➡️ **Market Priced** - Aligned with market"
                color = "off"
            
            st.markdown(f"### Pricing Assessment\n{recommendation}")
        
        st.markdown("---")
        
        # Similar Properties
        st.markdown("## 🏠 Similar Properties in Market")
        
        if len(similar) > 0:
            st.info(f"Found {len(similar)} similar properties")
            
            display_cols = ['locality', 'bhk_count', 'area', 'price', 'rate_per_sqft', 'status', 'company_name']
            similar_display = similar[display_cols].head(10).copy()
            similar_display['price'] = similar_display['price'].apply(lambda x: f"₹{x:,.0f}")
            similar_display['rate_per_sqft'] = similar_display['rate_per_sqft'].apply(lambda x: f"₹{x:,.0f}")
            
            st.dataframe(similar_display, use_container_width=True)
        else:
            st.warning("No similar properties found in current market")
        
        st.markdown("---")
        
        # Model Performance
        with st.expander("📈 Model Performance Metrics"):
            
            # Calculate some metrics
            from sklearn.linear_model import LinearRegression
            
            X = st.session_state.df[['area', 'rate_per_sqft', 'bhk_count']].copy()
            y = st.session_state.df['price'].copy()
            
            mask = X.notna().all(axis=1) & y.notna()
            X = X[mask]
            y = y[mask]
            
            if len(X) > 0:
                model = LinearRegression()
                model.fit(X, y)
                
                train_r2 = model.score(X, y)
                
                st.markdown(f"""
                ### Model Coefficients
                - **Intercept**: ₹{model.intercept_:,.0f}
                - **Area Coefficient**: ₹{model.coef_[0]:,.0f} per sqft
                - **Rate/Sqft Coefficient**: ₹{model.coef_[1]:,.2f}
                - **BHK Coefficient**: ₹{model.coef_[2]:,.0f}
                
                ### Model Quality
                - **R² Score**: {train_r2:.4f} (Higher is better, max 1.0)
                - **Training Samples**: {len(X):,}
                
                ### Interpretation
                - R² closer to 1.0 indicates better model fit
                - Coefficients show impact of each feature on price
                """)
    else:
        st.error("Could not make prediction. Please check your inputs and try again.")

st.markdown("---")

# FAQ
with st.expander("❓ Frequently Asked Questions"):
    st.markdown("""
    ### Q: How accurate is this prediction?
    **A:** The model is trained on real market data and uses linear regression. 
    Accuracy depends on how similar your property is to training data properties.
    
    ### Q: What if I don't know the rate per sqft?
    **A:** Check similar properties on the Dashboard page to estimate this value.
    
    ### Q: Can this replace professional valuation?
    **A:** This is a data-driven estimate for reference only. Professional valuations
    consider many more factors and are recommended for formal decisions.
    
    ### Q: How often is the model updated?
    **A:** The model is trained on the dataset provided. For real-time accuracy,
    update the data periodically.
    
    ### Q: What factors are NOT considered?
    **A:** The model currently considers area, rate/sqft, and BHK. Other factors like:
    - Exact locality premium
    - Builder reputation
    - Amenities
    - Age of property
    - Facing and layout
    
    These would improve accuracy but require more detailed data.
    """)
