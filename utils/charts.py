"""
Charts Module

This module contains functions for creating interactive visualizations using Plotly.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np


def create_price_distribution_histogram(df, title="Price Distribution"):
    """Create histogram of price distribution."""
    fig = px.histogram(
        df,
        x='price',
        nbins=50,
        title=title,
        labels={'price': 'Price (₹)'},
        color_discrete_sequence=['#1f77b4']
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=500,
        hovermode='x unified',
        bargap=0.1
    )
    
    return fig


def create_rate_per_sqft_distribution(df, title="Rate per Sqft Distribution"):
    """Create histogram of rate per sqft distribution."""
    fig = px.histogram(
        df,
        x='rate_per_sqft',
        nbins=50,
        title=title,
        labels={'rate_per_sqft': 'Rate per Sqft (₹)'},
        color_discrete_sequence=['#ff7f0e']
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=500,
        hovermode='x unified'
    )
    
    return fig


def create_scatter_area_vs_price(df, title="Area vs Price"):
    """Create scatter plot of area vs price."""
    fig = px.scatter(
        df,
        x='area',
        y='price',
        color='bhk_count',
        size='rate_per_sqft',
        hover_data=['locality', 'company_name'],
        title=title,
        labels={'area': 'Area (sqft)', 'price': 'Price (₹)'},
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=600,
        hovermode='closest'
    )
    
    return fig


def create_scatter_area_vs_rate(df, title="Area vs Rate per Sqft"):
    """Create scatter plot of area vs rate per sqft."""
    fig = px.scatter(
        df,
        x='area',
        y='rate_per_sqft',
        color='bhk_count',
        hover_data=['locality', 'company_name', 'price'],
        title=title,
        labels={'area': 'Area (sqft)', 'rate_per_sqft': 'Rate per Sqft (₹)'},
        color_continuous_scale='Plasma'
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=600,
        hovermode='closest'
    )
    
    return fig


def create_top_localities_bar(df, top_n=15, title="Top Localities by Average Price"):
    """Create bar chart of top localities by average price."""
    locality_data = df.groupby('locality')['price'].mean().sort_values(ascending=False).head(top_n)
    
    fig = px.bar(
        x=locality_data.values,
        y=locality_data.index,
        orientation='h',
        title=title,
        labels={'x': 'Average Price (₹)', 'y': 'Locality'},
        color=locality_data.values,
        color_continuous_scale='Blues'
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=600,
        showlegend=False,
        hovermode='y unified'
    )
    
    return fig


def create_top_builders_bar(df, top_n=15, title="Top Builders by Average Price"):
    """Create bar chart of top builders."""
    builder_data = df.groupby('company_name')['price'].mean().sort_values(ascending=False).head(top_n)
    
    fig = px.bar(
        x=builder_data.values,
        y=builder_data.index,
        orientation='h',
        title=title,
        labels={'x': 'Average Price (₹)', 'y': 'Builder'},
        color=builder_data.values,
        color_continuous_scale='Greens'
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=600,
        showlegend=False,
        hovermode='y unified'
    )
    
    return fig


def create_status_pie(df, title="Ready vs Under Construction"):
    """Create pie chart of property status distribution."""
    status_data = df['status'].value_counts()
    
    fig = px.pie(
        values=status_data.values,
        names=status_data.index,
        title=title,
        color_discrete_sequence=['#00cc96', '#ef553b']
    )
    
    fig.update_layout(template='plotly_dark', height=500)
    
    return fig


def create_rera_pie(df, title="RERA Approval Status"):
    """Create pie chart of RERA approval."""
    rera_data = df['rera_approval'].value_counts()
    
    fig = px.pie(
        values=rera_data.values,
        names=rera_data.index,
        title=title,
        color_discrete_sequence=['#636EFA', '#EF553B']
    )
    
    fig.update_layout(template='plotly_dark', height=500)
    
    return fig


def create_bhk_distribution_bar(df, title="Properties by BHK"):
    """Create bar chart of BHK distribution."""
    bhk_data = df['bhk_count'].value_counts().sort_index()
    
    fig = px.bar(
        x=bhk_data.index,
        y=bhk_data.values,
        title=title,
        labels={'x': 'BHK Count', 'y': 'Number of Properties'},
        color=bhk_data.values,
        color_continuous_scale='Reds'
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=500,
        showlegend=False,
        hovermode='x unified'
    )
    
    return fig


def create_property_type_bar(df, title="Properties by Type"):
    """Create bar chart of property type distribution."""
    prop_data = df['flat_type'].value_counts()
    
    fig = px.bar(
        x=prop_data.index,
        y=prop_data.values,
        title=title,
        labels={'x': 'Property Type', 'y': 'Count'},
        color=prop_data.values,
        color_continuous_scale='Purples'
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=500,
        showlegend=False,
        hovermode='x unified'
    )
    
    return fig


def create_bhk_vs_price_box(df, title="Price Distribution by BHK"):
    """Create box plot of price by BHK."""
    fig = px.box(
        df,
        x='bhk_count',
        y='price',
        title=title,
        labels={'bhk_count': 'BHK', 'price': 'Price (₹)'},
        color='bhk_count',
        color_discrete_sequence=['#00cc96', '#ab63fa', '#ff6692', '#636EFA', '#EF553B']
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=500,
        showlegend=False,
        hovermode='x unified'
    )
    
    return fig


def create_correlation_heatmap(df, title="Correlation Matrix"):
    """Create correlation heatmap."""
    numeric_df = df[['price', 'area', 'rate_per_sqft', 'bhk_count']].corr()
    
    fig = px.imshow(
        numeric_df,
        text_auto=True,
        title=title,
        color_continuous_scale='RdBu_r',
        zmin=-1,
        zmax=1
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=500,
        width=600
    )
    
    return fig


def create_price_by_status_bar(df, title="Average Price by Status"):
    """Create bar chart comparing prices by status."""
    status_price = df.groupby('status')['price'].agg(['mean', 'count']).reset_index()
    status_price.columns = ['Status', 'Average Price', 'Count']
    
    fig = px.bar(
        status_price,
        x='Status',
        y='Average Price',
        title=title,
        labels={'Average Price': 'Average Price (₹)'},
        color='Average Price',
        color_continuous_scale='Teal'
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=500,
        showlegend=False,
        hovermode='x unified'
    )
    
    return fig


def create_rera_vs_price_bar(df, title="Average Price by RERA Status"):
    """Create bar chart comparing prices by RERA status."""
    rera_price = df.groupby('rera_approval')['price'].agg(['mean', 'count']).reset_index()
    rera_price.columns = ['RERA Status', 'Average Price', 'Count']
    
    fig = px.bar(
        rera_price,
        x='RERA Status',
        y='Average Price',
        title=title,
        labels={'Average Price': 'Average Price (₹)'},
        color='Average Price',
        color_continuous_scale='Oranges'
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=500,
        showlegend=False,
        hovermode='x unified'
    )
    
    return fig


def create_top_localities_treemap(df, title="Market Share by Locality"):
    """Create treemap of localities."""

    locality_data = (
        df.groupby("locality")
        .agg(
            Avg_Price=("price", "mean"),
            Count=("price", "count")
        )
        .reset_index()
    )

    locality_data.columns = ["Locality", "Avg Price", "Count"]

    fig = px.treemap(
        locality_data,
        path=["Locality"],
        values="Count",
        color="Avg Price",
        color_continuous_scale="Viridis",
        title=title
    )

    fig.update_layout(
        template="plotly_dark",
        height=600
    )

    return fig


def create_bhk_by_property_type(df, title="BHK Count by Property Type"):
    """Create grouped bar chart of BHK by property type."""
    bhk_prop = pd.crosstab(df['bhk_count'], df['flat_type'])
    
    fig = px.bar(
        bhk_prop,
        title=title,
        barmode='group',
        labels={'value': 'Count', 'bhk_count': 'BHK'},
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=500,
        hovermode='x unified'
    )
    
    return fig


def create_price_trend_line(df, title="Price Trend Analysis"):
    """Create line chart showing price trends."""
    # Create price bins and analyze
    df_sorted = df.sort_values('area')
    window = len(df_sorted) // 20  # Create 20 groups
    
    if window > 0:
        trend_data = df_sorted.groupby(df_sorted.index // window).agg({
            'area': 'mean',
            'price': 'mean'
        }).reset_index(drop=True)
    else:
        trend_data = df.groupby('bhk_count')['price'].mean().reset_index()
        trend_data.columns = ['area', 'price']
    
    fig = px.line(
        trend_data,
        x='area',
        y='price',
        title=title,
        labels={'area': 'Area (sqft)', 'price': 'Average Price (₹)'},
        markers=True
    )
    
    fig.update_traces(
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=8)
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=500,
        hovermode='x unified'
    )
    
    return fig


def create_builder_comparison_bar(df, top_n=10, title="Top Builders by Rate per Sqft"):
    """Create bar chart comparing builders by rate per sqft."""
    builder_rate = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(top_n)
    
    fig = px.bar(
        x=builder_rate.values,
        y=builder_rate.index,
        orientation='h',
        title=title,
        labels={'x': 'Average Rate per Sqft (₹)', 'y': 'Builder'},
        color=builder_rate.values,
        color_continuous_scale='Sunset'
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=600,
        showlegend=False,
        hovermode='y unified'
    )
    
    return fig
