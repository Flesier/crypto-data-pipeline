import redis

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

bitcoin_price = redis_client.get("bitcoin_price")
ethereum_price = redis_client.get("ethereum_price")

print(f"Bitcoin Price: ${bitcoin_price}")
print(f"Ethereum Price: ${ethereum_price}")
