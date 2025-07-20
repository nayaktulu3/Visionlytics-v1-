# Visionlytics Web Tool (v1)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# --- PAGE SETUP ---
st.set_page_config(page_title="Visionlytics", layout="wide")
st.title("📊 Visionlytics – Your Personal AI Data Analyst")

# --- FILE UPLOAD ---
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# --- RE-UPLOAD OPTION ---
if uploaded_file is not None:
    try:
        # Read CSV file
        df = pd.read_csv(uploaded_file)

        st.success("✅ File uploaded successfully!")

        # Show preview
        st.subheader("👀 Dataset Preview")
        st.dataframe(df.head())

        # Show basic info
        st.subheader("📌 Data Overview")
        st.write("Shape:", df.shape)
        st.write("Missing Values:")
        st.write(df.isnull().sum())

        # Drop missing for simplicity
        df.dropna(inplace=True)

        # --- Visualizations ---
        st.subheader("📈 Auto Visualizations")

        num_cols = df.select_dtypes(include='number').columns
        cat_cols = df.select_dtypes(include='object').columns

        # Numerical histograms
        for col in num_cols[:3]:  # Limit for clean UI
            st.markdown(f"**Histogram: {col}**")
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax, color="skyblue")
            st.pyplot(fig)

        # Categorical bar plots
        for col in cat_cols[:2]:
            st.markdown(f"**Bar Chart: {col}**")
            fig, ax = plt.subplots()
            sns.countplot(x=col, data=df, ax=ax, palette="pastel")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        # Correlation heatmap
        if len(num_cols) >= 2:
            st.markdown("**Correlation Heatmap**")
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)

    except Exception as e:
        st.error("❌ Error reading file. Please upload a valid CSV file.")
        st.warning("Click below to re-upload.")
        st.experimental_rerun()

else:
    st.info("Please upload a `.csv` file to begin.")

# --- Footer ---
st.markdown("---")
st.caption("🚀 Built by Tulu Nayak | Visionlytics v1")
