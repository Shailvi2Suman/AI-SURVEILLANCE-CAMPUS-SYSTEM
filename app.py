import streamlit as st
import pandas as pd

# -------------------------------
# Class-wise Metrics (Manually filled)
# -------------------------------

virat_metrics = {
    'Class': ['person', 'helmet', 'no helmet', 'restricted area'],
    'Precision': [0.61, 0.55, 0.40, 0.60],
    'Recall': [0.33, 0.30, 0.20, 0.50],
    'mAP@0.5': [0.33, 0.30, 0.15, 0.34]
}

osf_metrics = {
    'Class': ['person', 'helmet', 'no helmet', 'restricted area'],
    'Precision': [0.34, 0.31, 0.20, 0.25],
    'Recall': [0.17, 0.12, 0.05, 0.10],
    'mAP@0.5': [0.06, 0.05, 0.02, 0.04]
}

# -------------------------------
# App UI
# -------------------------------

st.title("🚨 Helmet & Safety Alert System (YOLOv5-based)")

dataset_choice = st.selectbox("Select Dataset", ["VIRAT", "OSF"])

if dataset_choice == "VIRAT":
    df = pd.DataFrame(virat_metrics)
else:
    df = pd.DataFrame(osf_metrics)

st.subheader("📊 Class-wise Model Performance")
st.dataframe(df.style.format({'Precision': '{:.2f}', 'Recall': '{:.2f}', 'mAP@0.5': '{:.2f}'}))

# -------------------------------
# Alert Simulation
# -------------------------------
st.subheader("🔔 Simulated Alert System")

selected_class = st.selectbox("Choose Class to Simulate Alert", df['Class'])

row = df[df['Class'] == selected_class].iloc[0]
prec, rec = row['Precision'], row['Recall']

if prec < 0.3:
    st.error(f"⚠️ ALERT: Low precision ({prec:.2f}) for '{selected_class}'. System may miss or falsely detect.")
elif prec < 0.5:
    st.warning(f"⚠️ Moderate precision ({prec:.2f}) for '{selected_class}'. Consider reviewing detections.")
else:
    st.success(f"✅ Good precision ({prec:.2f}) for '{selected_class}'. Detection is reliable.")

st.markdown(f"- **Recall**: {rec:.2f}  
- **mAP@0.5**: {row['mAP@0.5']:.2f}")

st.caption("Simulated using training results. No live image detection is performed.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("Developed for Hackathon – *Helmet & Safety Violation Detection* 🚧")
