"""
Analysis Module

This module contains functions for analyzing the Gurgaon real estate dataset.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')


def get_price_statistics(df):
    """Get detailed price statistics."""
    return {
        'mean': df['price'].mean(),
        'median': df['price'].median(),
        'std': df['price'].std(),
        'min': df['price'].min(),
        'max': df['price'].max(),
        'q1': df['price'].quantile(0.25),
        'q3': df['price'].quantile(0.75),
    }


def get_locality_analysis(df, top_n=10):
    """Get top localities by various metrics."""
    locality_stats = df.groupby('locality').agg({
        'price': ['count', 'mean', 'median', 'min', 'max'],
        'area': 'mean',
        'rate_per_sqft': 'mean'
    }).round(2)
    
    locality_stats.columns = ['Properties', 'Avg Price', 'Median Price', 'Min Price', 'Max Price', 'Avg Area', 'Avg Rate/Sqft']
    
    return locality_stats.sort_values('Avg Price', ascending=False).head(top_n)


def get_builder_analysis(df, top_n=10):
    """Get top builders by various metrics."""
    builder_stats = df.groupby('company_name').agg({
        'price': ['count', 'mean'],
        'rate_per_sqft': 'mean',
        'area': 'mean'
    }).round(2)
    
    builder_stats.columns = ['Properties', 'Avg Price', 'Avg Rate/Sqft', 'Avg Area']
    
    return builder_stats.sort_values('Avg Price', ascending=False).head(top_n)


def get_bhk_analysis(df):
    """Get BHK analysis."""
    bhk_stats = df.groupby('bhk_count').agg({
        'price': ['count', 'mean', 'median'],
        'area': 'mean',
        'rate_per_sqft': 'mean'
    }).round(2)
    
    bhk_stats.columns = ['Count', 'Avg Price', 'Median Price', 'Avg Area', 'Avg Rate/Sqft']
    
    return bhk_stats.sort_values('Avg Price', ascending=False)


def get_property_type_analysis(df):
    """Get property type analysis."""
    prop_stats = df.groupby('flat_type').agg({
        'price': ['count', 'mean', 'median'],
        'rate_per_sqft': 'mean',
        'area': 'mean'
    }).round(2)
    
    prop_stats.columns = ['Count', 'Avg Price', 'Median Price', 'Avg Rate/Sqft', 'Avg Area']
    
    return prop_stats.sort_values('Avg Price', ascending=False)


def get_status_analysis(df):
    """Get status analysis (Ready vs Under Construction)."""
    status_stats = df.groupby('status').agg({
        'price': ['count', 'mean', 'median'],
        'rate_per_sqft': 'mean',
        'area': 'mean'
    }).round(2)
    
    status_stats.columns = ['Count', 'Avg Price', 'Median Price', 'Avg Rate/Sqft', 'Avg Area']
    
    return status_stats


def get_rera_analysis(df):
    """Get RERA approval analysis."""
    rera_stats = df.groupby('rera_approval').agg({
        'price': ['count', 'mean', 'median'],
        'rate_per_sqft': 'mean'
    }).round(2)
    
    rera_stats.columns = ['Count', 'Avg Price', 'Median Price', 'Avg Rate/Sqft']
    
    return rera_stats


def get_business_questions(df):
    """Generate answers to key business questions."""
    insights = {}
    
    # Question 1: Costliest flat
    costliest_idx = df['price'].idxmax()
    costliest_flat = df.loc[costliest_idx]
    insights['costliest_flat'] = {
        'bhk': costliest_flat['bhk_count'],
        'locality': costliest_flat['locality'],
        'price': costliest_flat['price'],
        'price_cr': costliest_flat['price'] / 10000000,
        'society': costliest_flat['society'],
        'answer': f"The costliest flat is a {costliest_flat['bhk_count']} BHK in {costliest_flat['locality']} priced at ₹{costliest_flat['price']/10000000:.2f} Cr in {costliest_flat['society']}."
    }
    
    # Question 2: Highest average price locality
    highest_avg_locality = df.groupby('locality')['price'].mean().idxmax()
    avg_price = df[df['locality'] == highest_avg_locality]['price'].mean()
    insights['highest_avg_price_locality'] = {
        'locality': highest_avg_locality,
        'avg_price': avg_price,
        'answer': f"The locality with the highest average price is {highest_avg_locality} with an average of ₹{avg_price:,.0f}."
    }
    
    # Question 3: Highest rate per sqft
    highest_rate_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
    avg_rate = df[df['locality'] == highest_rate_locality]['rate_per_sqft'].mean()
    insights['highest_rate_locality'] = {
        'locality': highest_rate_locality,
        'rate': avg_rate,
        'answer': f"The locality with the highest rate per sqft is {highest_rate_locality} at ₹{avg_rate:,.0f}/sqft."
    }
    
    # Question 4: Ready vs Under Construction
    ready_avg = df[df['status'].str.lower() == 'ready to move']['price'].mean()
    under_avg = df[df['status'].str.lower() == 'under construction']['price'].mean()
    insights['ready_vs_under'] = {
        'ready_avg': ready_avg,
        'under_avg': under_avg,
        'answer': f"Ready-to-move properties average ₹{ready_avg:,.0f}, while under-construction average ₹{under_avg:,.0f}." + 
                  (f" Ready is {((ready_avg/under_avg - 1)*100):.1f}% more expensive." if ready_avg > under_avg else f" Under-construction is {((under_avg/ready_avg - 1)*100):.1f}% more expensive.")
    }
    
    # Question 5: RERA Premium
    rera_approved_avg = df[df['rera_approval'] == 'Approved']['price'].mean()
    rera_not_approved_avg = df[df['rera_approval'] == 'Not Approved']['price'].mean()
    premium_pct = ((rera_approved_avg / rera_not_approved_avg - 1) * 100)
    insights['rera_premium'] = {
        'approved_avg': rera_approved_avg,
        'not_approved_avg': rera_not_approved_avg,
        'premium': premium_pct,
        'answer': f"RERA-approved properties average ₹{rera_approved_avg:,.0f}, commanding a {premium_pct:.1f}% premium over non-approved (₹{rera_not_approved_avg:,.0f})."
    }
    
    # Question 6: Most expensive BHK
    most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
    bhk_rate = df[df['bhk_count'] == most_expensive_bhk]['rate_per_sqft'].mean()
    insights['expensive_bhk'] = {
        'bhk': most_expensive_bhk,
        'rate': bhk_rate,
        'answer': f"The most expensive BHK configuration is {most_expensive_bhk} at ₹{bhk_rate:,.0f}/sqft on average."
    }
    
    # Question 7: Most expensive property type
    most_expensive_property = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
    prop_rate = df[df['flat_type'] == most_expensive_property]['rate_per_sqft'].mean()
    insights['expensive_property_type'] = {
        'type': most_expensive_property,
        'rate': prop_rate,
        'answer': f"The most expensive property type is {most_expensive_property.title()} at ₹{prop_rate:,.0f}/sqft."
    }
    
    # Question 8: Top 5 builders
    top_5_builders = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
    insights['top_builders'] = {
        'builders': list(top_5_builders.index),
        'rates': list(top_5_builders.values),
        'answer': f"Top 5 builders by rate/sqft: {', '.join(top_5_builders.index.tolist())}"
    }
    
    # Question 9: Area impact on price
    correlation = df['area'].corr(df['rate_per_sqft'])
    insights['area_correlation'] = {
        'correlation': correlation,
        'answer': f"Area has a correlation of {correlation:.3f} with rate per sqft, indicating {'positive' if correlation > 0 else 'negative'} relationship."
    }
    
    return insights


def predict_price(data, features):
    """
    Predict property price using Linear Regression.
    
    Parameters:
    -----------
    data : pd.DataFrame
        Training data
    features : dict
        Features for prediction
        
    Returns:
    --------
    float
        Predicted price
    """
    try:
        # Prepare training data
        X = data[['area', 'rate_per_sqft', 'bhk_count']].copy()
        y = data['price'].copy()
        
        # Remove missing values
        mask = X.notna().all(axis=1) & y.notna()
        X = X[mask]
        y = y[mask]
        
        if len(X) < 10:
            return None
        
        # Train model
        model = LinearRegression()
        model.fit(X, y)
        
        # Make prediction
        X_pred = np.array([[features['area'], features['rate_per_sqft'], features['bhk_count']]])
        prediction = model.predict(X_pred)[0]
        
        return max(0, prediction)
    
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return None


def get_top_properties(df, locality=None, bhk=None, property_type=None, status=None, builder=None, rera=None, limit=10):
    """
    Filter and get top properties based on criteria.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset
    locality, bhk, property_type, status, builder, rera : filters
    limit : int
        Number of results
        
    Returns:
    --------
    pd.DataFrame
        Filtered properties
    """
    filtered_df = df.copy()
    
    if locality:
        filtered_df = filtered_df[filtered_df['locality'] == locality]
    if bhk:
        filtered_df = filtered_df[filtered_df['bhk_count'] == bhk]
    if property_type:
        filtered_df = filtered_df[filtered_df['flat_type'] == property_type]
    if status:
        filtered_df = filtered_df[filtered_df['status'] == status.lower()]
    if builder:
        filtered_df = filtered_df[filtered_df['company_name'] == builder]
    if rera:
        filtered_df = filtered_df[filtered_df['rera_approval'] == rera]
    
    return filtered_df.nlargest(limit, 'price')[['locality', 'bhk_count', 'flat_type', 'status', 'price', 'area', 'rate_per_sqft', 'company_name']]
