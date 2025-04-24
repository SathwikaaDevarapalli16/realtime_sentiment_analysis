import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import glob

st.set_page_config(page_title="Sentiment Dashboard", layout="wide")

st.title("📊 Twitter Sentiment Analysis Dashboard")

# Load Data
csv_files = glob.glob('output/sentiment_data/*.csv')
if csv_files:
    df_sentiment = pd.concat([pd.read_csv(f, header=None) for f in csv_files], ignore_index=True)
    df_sentiment.columns = ['text', 'sentiment_score']

    # Show Data Table
    st.subheader("📄 Raw Data")
    st.dataframe(df_sentiment.tail(10))

    # Sentiment Score Histogram
    st.subheader("📈 Sentiment Distribution")
    fig, ax = plt.subplots()
    ax.hist(df_sentiment['sentiment_score'], bins=20, color='skyblue', edgecolor='black')
    ax.set_title('Sentiment Score Distribution')
    ax.set_xlabel('Sentiment Score')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Sentiment Summary
    st.subheader("📊 Summary Statistics")
    st.write(df_sentiment['sentiment_score'].describe())

    # Most Positive/Negative
    st.subheader("😊 Most Positive Tweets")
    st.write(df_sentiment.sort_values(by='sentiment_score', ascending=False).head(3))

    st.subheader("😞 Most Negative Tweets")
    st.write(df_sentiment.sort_values(by='sentiment_score').head(3))
else:
    st.warning("No sentiment data found. Please run the streaming script first.")


