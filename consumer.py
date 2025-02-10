# Consumes messages from kafka and stores data in redis
from kafka import KafkaConsumer
import redis
import json

# Initialize Redis Client
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    "crypto_prices",
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Listening for messages...")

for message in consumer:
    data = message.value
    print(f"Received from Kafka: {data}")

    # Store each crypto price in Redis
    for coin, price in data.items():
        redis_client.set(coin, price["usd"])

    print(f"Stored in Redis: {data}")
