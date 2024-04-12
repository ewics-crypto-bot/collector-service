import json
import requests
from flask import current_app
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


class CoinMarketCapService:
    def __init__(self):
        self.api_key = current_app.config['COIN_MARKET_CAP_KEY']
        self.base_url = current_app.config['COIN_MARKET_CAP_DOMAIN']
        self.session = requests.Session()
        self.session.headers.update(self.get_headers())  # Set default headers for the session

    def get_headers(self):
        return {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": self.api_key,
        }

    def get_coin_data(self, coin_id):
        url = f"{self.base_url}cryptocurrency/info?id={coin_id}"
        response = self.session.get(url)  # Use the session to make a request
        response.raise_for_status()
        return response.json()

    def get_latest_listings(self, start, limit, convert):
        try:
            params = {
                'start': start,
                'limit': limit,
                'convert': convert
            }
            url = f"{self.base_url}cryptocurrency/listings/latest"
            response = self.session.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
            else:
                data = {'error': f'Received status code {response.status_code}', 'details': response.text}

            print(data)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            return {'error': str(e)}
        except json.JSONDecodeError as json_err:
            print(f"JSON decode error: {json_err}")
            return {'error': 'Failed to decode JSON response'}

    def close(self):
        self.session.close()
