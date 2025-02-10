import json
import redis
from kafka import KafkaConsumer

# Connect to Redis
redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

consumer = KafkaConsumer(
    "crypto_prices",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

print("Listening for messages...")

for message in consumer:
    data = message.value
    if "bitcoin" in data and "ethereum" in data:
        redis_client.set("bitcoin_price", data["bitcoin"]["usd"])
        redis_client.set("ethereum_price", data["ethereum"]["usd"])
        print(f"Stored in Redis: {data}")
