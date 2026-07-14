"""
Data Cleaning Module

This module contains functions for cleaning and preprocessing the Gurgaon real estate dataset.
"""

import pandas as pd
import numpy as np


def load_data(filepath):
    """
    Load data from CSV file.
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
        
    Returns:
    --------
    pd.DataFrame
        Loaded dataframe
    """
    return pd.read_csv(filepath)


def clean_data(df):
    """
    Clean and preprocess the real estate dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Raw dataframe
        
    Returns:
    --------
    pd.DataFrame
        Cleaned dataframe
    """
    df = df.copy()
    
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Remove leading/trailing spaces
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    
    # Clean numerical columns
    if 'price' in df.columns:
        df['price'] = pd.to_numeric(
            df['price'].astype(str).str.replace(',', '').str.replace('₹', ''),
            errors='coerce'
        )
    
    if 'area' in df.columns:
        df['area'] = pd.to_numeric(
            df['area'].astype(str).str.replace(',', ''),
            errors='coerce'
        )
    
    if 'rate_per_sqft' in df.columns:
        df['rate_per_sqft'] = pd.to_numeric(
            df['rate_per_sqft'].astype(str).str.replace(',', ''),
            errors='coerce'
        )
    
    # Clean categorical columns
    if 'status' in df.columns:
        df['status'] = df['status'].str.strip().str.lower()
    
    if 'rera_approval' in df.columns:
        df['rera_approval'] = df['rera_approval'].str.strip().str.lower()
        df['rera_approval'] = df['rera_approval'].map({
            'approved by rera': 'Approved',
            'not approved by rera': 'Not Approved'
        })
    
    if 'flat_type' in df.columns:
        df['flat_type'] = df['flat_type'].str.strip().str.lower()
    
    # Clean locality names
    if 'locality' in df.columns:
        df['locality'] = df['locality'].str.strip().str.title()
    
    # Clean builder/company names
    if 'company_name' in df.columns:
        df['company_name'] = df['company_name'].str.strip().str.title()
    
    # Remove rows with critical missing values
    critical_columns = ['price', 'area', 'locality', 'bhk_count']
    df = df.dropna(subset=[col for col in critical_columns if col in df.columns])
    
    return df.reset_index(drop=True)


def get_data_summary(df):
    """
    Get summary statistics of the dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned dataframe
        
    Returns:
    --------
    dict
        Summary statistics
    """
    return {
        'total_properties': len(df),
        'avg_price': df['price'].mean(),
        'median_price': df['price'].median(),
        'max_price': df['price'].max(),
        'min_price': df['price'].min(),
        'avg_area': df['area'].mean(),
        'avg_rate_per_sqft': df['rate_per_sqft'].mean(),
        'total_localities': df['locality'].nunique() if 'locality' in df.columns else 0,
        'total_builders': df['company_name'].nunique() if 'company_name' in df.columns else 0,
        'missing_values': df.isnull().sum().sum()
    }
