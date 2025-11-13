import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie

# --- Page setup ---
st.set_page_config(page_title="Animated Dashboard", page_icon="📊", layout="centered")

# --- Helper function to load Lottie files ---
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Load animations ---
intro_url = "https://assets4.lottiefiles.com/packages/lf20_jcikwtux.json"
check_url = "https://assets2.lottiefiles.com/packages/lf20_touohxv0.json"
intro_anim = load_lottie_url(intro_url)
check_anim = load_lottie_url(check_url)

# --- Title & Intro ---
st.title("Animated Streamlit Dashboard")
st.write("A clean demonstration of motion and interactivity in Streamlit.")

st.divider()

# --- Lottie intro animation ---
st_lottie(intro_anim, height=240, key="intro")

# --- Loading animation ---
st.subheader("Initializing dashboard...")
progress_bar = st.progress(0)
status_text = st.empty()

for i in range(101):
    progress_bar.progress(i)
    status_text.text(f"Loading components: {i}%")
    time.sleep(0.02)

status_text.text("Loading complete.")
st.success("Dashboard is ready.")
st.divider()

# --- Dynamic text animation ---
st.subheader("System Activity")
placeholder = st.empty()
messages = ["Connecting to server...", "Fetching data...", "Building charts...", "Complete."]
for msg in messages:
    placeholder.markdown(f"#### {msg}")
    time.sleep(0.5)

placeholder.markdown("#### All systems operational.")

# --- Outro animation ---
st_lottie(check_anim, height=180, key="check")

st.markdown("---")
st.caption("Built with Streamlit and Lottie • Minimal Edition")



