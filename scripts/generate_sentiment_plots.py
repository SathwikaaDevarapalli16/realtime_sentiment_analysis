import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
df = pd.concat([pd.read_csv(f'output/sentiment_data/{f}') for f in os.listdir('output/sentiment_data') if f.endswith('.csv')])

# Plot Histogram
plt.figure(figsize=(8, 6))
df['sentiment_score'].hist(bins=20)
plt.title("Sentiment Score Distribution")
plt.xlabel("Sentiment Score")
plt.ylabel("Frequency")
plt.savefig("sentiment_distribution.pdf")
plt.close()

# Plot Text Sentiment Scatter (Optional)
plt.figure(figsize=(10, 6))
plt.scatter(range(len(df)), df['sentiment_score'])
plt.title("Sentiment Scores over Tweets")
plt.xlabel("Tweet Index")
plt.ylabel("Sentiment Score")
plt.savefig("sentiment_over_tweets.pdf")
plt.close()

print("PDFs saved: sentiment_distribution.pdf, sentiment_over_tweets.pdf")

