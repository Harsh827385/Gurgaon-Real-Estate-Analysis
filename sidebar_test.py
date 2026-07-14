import streamlit as st

st.set_page_config(
    page_title="Sidebar Test",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    st.title("Test Sidebar")
    st.write("Harshjeet Sidebar Test")
    st.radio(
        "Navigation",
        ["Home", "Dashboard", "Analysis"]
    )

st.title("Sidebar Test")

st.write("Sidebar ko close karo aur phir reopen button check karo.")