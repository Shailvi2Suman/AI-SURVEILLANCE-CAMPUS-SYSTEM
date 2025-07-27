import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# Streamlit App Title
# -------------------------------
st.set_page_config(page_title="Helmet Violation Detection", layout="wide")
st.title("🛡️ YOLOv5 Helmet & Safety Violation Summary Dashboard")

# -------------------------------
# Dataset Selector
# -------------------------------
dataset_choice = st.selectbox("Select Dataset", ["VIRAT", "OSF"])

# Map dataset to file
file_map = {
    "VIRAT": "virat_summary.csv",
    "OSF": "osf_summary.csv"
}

file_path = file_map[dataset_choice]

# -------------------------------
# Read CSV
# -------------------------------
if not os.path.exists(file_path):
    st.error(f"❌ Summary CSV for {dataset_choice} not found: `{file_path}`")
    st.stop()

df = pd.read_csv(file_path)

# -------------------------------
# Show Summary Table
# -------------------------------
st.subheader("📋 Class-wise Metrics")
st.dataframe(df.style.format({'Precision': '{:.2f}', 'Recall': '{:.2f}', 'mAP@0.5': '{:.2f}'}))

# -------------------------------
# Plot 1: Bar chart - Class-wise Metrics
# -------------------------------
st.subheader("📉 Detection Metrics by Class")

fig1, ax1 = plt.subplots(figsize=(10, 5))
df.set_index('Class')[['Precision', 'Recall', 'mAP@0.5']].plot(kind='bar', ax=ax1)
ax1.set_ylabel("Score")
ax1.set_title(f"{dataset_choice} - Detection Performance")
ax1.grid(True, axis='y')
plt.ylim(0, 1)
st.pyplot(fig1)

# -------------------------------
# Plot 2: Pie chart - True Detection Count
# -------------------------------
if 'TrueDetections' in df.columns:
    st.subheader("🧮 Distribution of True Detections")
    fig2, ax2 = plt.subplots()
    ax2.pie(df['TrueDetections'], labels=df['Class'], autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')
    st.pyplot(fig2)
else:
    st.info("ℹ️ No 'TrueDetections' column found in CSV. Pie chart skipped.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Developed for Hackathon - AI Campus Surveillance 🚨")
