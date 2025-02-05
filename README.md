# Crypto Data Pipeline

This project is designed to collect, process, and analyze cryptocurrency data from various APIs. The pipeline includes data collection, storage, transformation, and visualization.

## Features

- ✅ Collects data from APIs (e.g., CoinGecko, CoinMarketCap, Binance)
- ✅ Stores raw data in a PostgreSQL database
- ✅ Cleans and transforms data using Pandas & SQLAlchemy
- ✅ Loads transformed data into a data warehouse (Google BigQuery / AWS Redshift)
- ✅ Runs analytics and visualizations using Tableau / Metabase

## Tech Stack

- **Python**: Data collection & processing
- **PostgreSQL**: Raw data storage
- **Apache Airflow**: Workflow automation
- **Pandas & SQLAlchemy**: Data processing
- **Google BigQuery / AWS Redshift**: Data warehousing
- **Tableau / Metabase**: Data visualization

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/crypto-data-pipeline.git
    cd crypto-data-pipeline
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv crypto_env
    source crypto_env/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the database**:
    - Update the database connection settings in `config/database.yml`.

5. **Run the pipeline**:
    - Use Apache Airflow to schedule and run the data pipeline tasks.

## Usage

- **Collect Data**: Run the data collection scripts to fetch data from the APIs.