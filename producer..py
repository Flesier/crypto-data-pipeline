# Fetches crypto prices and pushes to kafka
from kafka import KafkaProducer
import requests
import json
import time

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Kafka broker
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize JSON
)

TOPIC_NAME = "crypto_prices"

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin,ethereum", "vs_currencies": "usd"}

    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        # Publish data to Kafka topic
        producer.send(TOPIC_NAME, data)
        print(f"Sent to Kafka: {data}")

    except Exception as e:
        print(f"Error fetching data: {e}")

# Fetch data every 5 seconds
while True:
    fetch_crypto_data()
    time.sleep(5)
