import streamlit as st
import pandas as pd

# -------------------------------
# Run Summary Data (Final YOLOv5 metrics)
# -------------------------------
virat_summary = {
    "Metric": ["Precision", "Recall", "mAP@0.5", "mAP@0.5:0.95"],
    "Value": [0.61022, 0.33333, 0.33564, 0.12963]
}

osf_summary = {
    "Metric": ["Precision", "Recall", "mAP@0.5", "mAP@0.5:0.95"],
    "Value": [0.33441, 0.17446, 0.06868, 0.01682]
}

# -------------------------------
# Streamlit App Layout
# -------------------------------
st.set_page_config(page_title="YOLOv5 Run Summary", layout="centered")

st.title("📊 YOLOv5 Run Summary Dashboard")

dataset = st.selectbox("Select Dataset", ["VIRAT", "OSF"])

if dataset == "VIRAT":
    df = pd.DataFrame(virat_summary)
    st.subheader("🔍 VIRAT Dataset Run Summary")
else:
    df = pd.DataFrame(osf_summary)
    st.subheader("🔍 OSF Dataset Run Summary")

# Display table
st.table(df.style.format({"Value": "{:.5f}"}))

# Footer
st.markdown("---")
st.caption("Developed for the Hackathon – Helmet & Safety Violation Detection 🚧")
