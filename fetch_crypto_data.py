import requests
import json
import time
from sqlalchemy import create_engine

API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

DB_URI = "postgresql://crypto_user:betty@localhost:5432/crypto_db"
engine = create_engine(DB_URI)

def fetch_crypto_prices():
    response = requests.get(API_URL)
    data = response.json()
    return data

def store_data():
    data = fetch_crypto_prices()
    for coin, prices in data.items():
        usd_price = prices["usd"]
        query = f"INSERT INTO crypto_prices (coin, price, timestamp) VALUES ('{coin}', {usd_price}, NOW());"
        engine.execute(query)
    print("Data stored successfully.")

if __name__ == "__main__":
    while True:
        store_data()
        time.sleep(60)  # Fetch data every 60 seconds