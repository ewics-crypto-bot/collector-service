from os import environ


class Config(object):
    COIN_MARKET_CAP_KEY = environ.get('COIN_MARKET_CAP_KEY') or 'you-will-never-guess'
    # uncomment this one to use actually key
    #COIN_MARKET_CAP_DOMAIN = environ.get('COIN_MARKET_CAP_DOMAIN') or 'coin-market-domain-failed'
    # Sandbox testing
    COIN_MARKET_CAP_DOMAIN = environ.get('COIN_MARKET_CAP_TEST_DOMAIN') or 'coin-market-domain-failed'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
