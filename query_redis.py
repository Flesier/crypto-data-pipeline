# retrieves real-time cryptocurrency prices from redis
import redis

# connect to redis
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# get the prices
bitcoin_price = redis_client.get("bitcoin")
ethereum_price = redis_client.get("ethereum")

print(f"Bitcoin Price: ${bitcoin_price}")
print(f"Ethereum Price: ${ethereum_price}")