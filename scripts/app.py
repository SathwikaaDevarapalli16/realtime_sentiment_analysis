import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

st.title("📊 Twitter Sentiment Analysis Dashboard")

try:
    # Load CSV with text only
    df = pd.read_csv("sample_tweets.csv")  # No header=None
    df.columns = ['text', 'sentiment_score']

    # Calculate sentiment scores dynamically
    df['sentiment_score'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)

    st.success("Sentiment data loaded and calculated successfully!")

    st.subheader("Sentiment Score Distribution")
    fig, ax = plt.subplots()
    ax.hist(df['sentiment_score'], bins=20, color='skyblue', edgecolor='black')
    ax.set_title('Sentiment Score Distribution')
    ax.set_xlabel('Sentiment Score')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

except Exception as e:
    st.warning(f"No sentiment data found. Error: {e}")

