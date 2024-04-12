# services will be used to interact with external apis ex coinmarketcap
from .coinmarketcap_service import CoinMarketCapService


def create_coin_market_cap_service():
    return CoinMarketCapService()
