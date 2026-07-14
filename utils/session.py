import streamlit as st
from pathlib import Path

from utils.cleaning import load_data, clean_data, get_data_summary
from utils.analysis import get_business_questions


def initialize_session_state():
    """
    Initialize dataset, summary and business insights
    for all Streamlit pages.
    """

    if "df" not in st.session_state:
        data_path = Path(__file__).parent.parent / "dataset" / "data.csv"

        df = load_data(data_path)
        df = clean_data(df)

        st.session_state.df = df

    if "data_summary" not in st.session_state:
        st.session_state.data_summary = get_data_summary(
            st.session_state.df
        )

    if "business_insights" not in st.session_state:
        st.session_state.business_insights = get_business_questions(
            st.session_state.df
        )