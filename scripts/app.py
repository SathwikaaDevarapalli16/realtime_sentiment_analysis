import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Twitter Sentiment Analysis Dashboard")

try:
    # Load CSV from data folder
    df = pd.read_csv("sample_tweets.csv")  # Corrected path
    df.columns = ['text', 'sentiment_score']  # Ensure correct columns

    if df['sentiment_score'].isnull().all() or df['sentiment_score'].empty:
        st.warning("No valid sentiment scores found in the data.")
    else:
        st.success("Sentiment data loaded successfully!")

        st.subheader("Sentiment Score Distribution")
        fig, ax = plt.subplots()
        ax.hist(df['sentiment_score'].dropna(), bins=20, color='skyblue', edgecolor='black')
        ax.set_title('Sentiment Score Distribution')
        ax.set_xlabel('Sentiment Score')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)

except Exception as e:
    st.warning(f"No sentiment data found. Error: {e}")

