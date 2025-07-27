import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🛡️ Helmet Violation Detection Summary")

# Upload section
st.sidebar.header("📁 Upload Summary CSV")
uploaded_file = st.sidebar.file_uploader("Upload a CSV (Class, Precision, Recall, mAP@0.5, TrueDetections)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Class-wise Metrics")
    st.dataframe(df)

    st.subheader("📉 Metrics Bar Chart")
    fig1, ax1 = plt.subplots()
    df.set_index('Class')[['Precision', 'Recall', 'mAP@0.5']].plot(kind='bar', ax=ax1)
    st.pyplot(fig1)

    if 'TrueDetections' in df.columns:
        st.subheader("📈 True Detection Share")
        fig2, ax2 = plt.subplots()
        ax2.pie(df['TrueDetections'], labels=df['Class'], autopct='%1.1f%%')
        ax2.axis('equal')
        st.pyplot(fig2)

else:
    st.info("👈 Upload your summary CSV file to begin.")

st.markdown("---")
st.caption("Developed for AI Campus Surveillance Hackathon 🚨")

