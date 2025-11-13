import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

st.title("📈 Data Insights Dashboard")

st.write("A clean and simple Streamlit template for professional projects.")

st.sidebar.header("Settings")
user = st.sidebar.text_input("User", "Analyst")
show_time = st.sidebar.checkbox("Show timestamp", True)

if show_time:
    st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

st.subheader(f"Welcome, {user}")
st.write("Use this space to explore your data, visualize metrics, or build reports.")

# Example placeholder charts
import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(20, 3), columns=["Metric A", "Metric B", "Metric C"])
st.line_chart(data)

st.caption("Built with Streamlit — simple, fast, and powerful.")
