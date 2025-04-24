import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Twitter Sentiment Analysis Dashboard")

try:
    # Load CSV from GitHub repo root
    df = pd.read_csv("sentiment_sample.csv", header=None)
    df.columns = ['text', 'sentiment_score']

    st.success("Sentiment data loaded successfully!")

    st.subheader("Sentiment Score Distribution")
    fig, ax = plt.subplots()
    ax.hist(df['sentiment_score'], bins=20, color='skyblue', edgecolor='black')
    ax.set_title('Sentiment Score Distribution')
    ax.set_xlabel('Sentiment Score')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

except Exception as e:
    st.warning(f"No sentiment data found. Error: {e}")

