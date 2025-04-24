import time
from kafka import KafkaProducer
import json
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

messages = [
    {"text": "I love sunny days!"},
    {"text": "I'm so tired of this weather."},
    {"text": "Absolutely thrilled with the new phone!"},
    {"text": "Feeling great after a morning workout."},
    {"text": "This is the worst movie I've ever seen."}
]

# Loop indefinitely
while True:
    message = random.choice(messages)
    producer.send('tweets', message)
    print(f"Sent: {message}")
    time.sleep(1)  # Sends a message every 1 second

