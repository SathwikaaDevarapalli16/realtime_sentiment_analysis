from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, DoubleType
from pyspark.sql.functions import from_json, col, udf
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd
import os
import glob

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("KafkaTweetStreamAnalysis") \
    .getOrCreate()

# Define schema for Kafka message
schema = StructType().add("text", StringType())

# Read data from Kafka topic
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "tweets") \
    .option("startingOffsets", "earliest") \
    .load()

# Convert value from binary to string and parse JSON
df_parsed = df_raw.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json(col("json"), schema).alias("data")) \
    .select("data.*")

# Define UDF for sentiment score
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

sentiment_udf = udf(get_sentiment, DoubleType())
df_with_sentiment = df_parsed.withColumn("sentiment_score", sentiment_udf(col("text")))

# Write output to CSV
query = df_with_sentiment.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("path", "output/sentiment_data") \
    .option("checkpointLocation", "output/checkpoint") \
    .start()

# Let Spark Streaming run for some time to collect data (e.g., 60 seconds)
query.awaitTermination(60)
query.stop()

# Stop Spark session to release resources
spark.stop()

# Load CSV data into Pandas for plotting
csv_files = glob.glob('output/sentiment_data/*.csv')
if csv_files:
    df_list = []
    for f in csv_files:
        df = pd.read_csv(f, header=None)
        if df.shape[1] == 2:
            df.columns = ['text', 'sentiment_score']
        elif df.shape[1] > 2:
            df.columns = ['text', 'sentiment_score'] + [f'col_{i}' for i in range(3, df.shape[1] + 1)]
            df = df[['text', 'sentiment_score']]
        df_list.append(df)

    if df_list:
        df_sentiment = pd.concat(df_list, ignore_index=True)

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.hist(df_sentiment['sentiment_score'], bins=20, color='skyblue', edgecolor='black')
        plt.title('Sentiment Score Distribution')
        plt.xlabel('Sentiment Score')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("output/sentiment_distribution.pdf")
        print("Sentiment distribution plot saved as PDF.")
    else:
        print("No valid CSV data loaded for plotting.")
else:
    print("No CSV data found for plotting.")

