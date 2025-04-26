Real-Time Twitter Sentiment Analysis Dashboard
This project simulates real-time Twitter sentiment analysis using Apache Kafka and Apache Spark Streaming, with sentiment scoring powered by TextBlob, and visualized through a live Streamlit Dashboard.

Features

🐦 Simulated Tweet Stream with Kafka Producers.
⚡ Real-time Processing with Spark Streaming.
🧠 Sentiment Analysis using TextBlob polarity scores.
📊 CSV Output & PDF Plots for sentiment trends.
🌐 Interactive Streamlit Dashboard for live visualization.
🚀 Deployed on Streamlit Cloud.

Tech Stack

Python 3.10
Apache Kafka
Apache Spark (Structured Streaming)
TextBlob for sentiment scoring.
Pandas & Matplotlib for data handling and plotting.
Streamlit for UI.

Setup & Running Locally

1. Clone the repository:
   git clone git@github.com:YourUsername/realtime_sentiment_analysis.git;
   cd realtime_sentiment_analysis
   
2. Start Kafka and Zookeeper:
   bin/zookeeper-server-start.sh config/zookeeper.properties;
   bin/kafka-server-start.sh config/server.properties
   
3. Run Kafka Producer:
   python3 scripts/simulated_kafka_producer.py
   
4.Start Spark Streaming Job:
  spark-submit scripts/spark_streaming_sql.py
  
5. Launch Streamlit Dashboard:
   streamlit run scripts/app.py
   
Live Demo

https://realtimesentimentanalysis.streamlit.app



   
