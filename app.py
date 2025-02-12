from flask import Flask, jsonify
import redis
import json

app = Flask(__name__)

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@app.route('/crypto-prices', methods=['GET'])
def get_crypto_prices():
    bitcoin_price = redis_client.get("bitcoin_price")
    ethereum_price = redis_client.get("ethereum_price")

    if not bitcoin_price or not ethereum_price:
        return jsonify({"error": "No data available"}), 404

    data = {
        "bitcoin": float(bitcoin_price),
        "ethereum": float(ethereum_price)
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
