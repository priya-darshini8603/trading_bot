from binance import Client
from config import BASE_URL
from utils.logger import logger

log = logger()

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = BASE_URL
        log.info("Connected to Binance Futures Testnet")

    def futures_order(self, **kwargs):
      try:
        response = self.client.futures_create_order(**kwargs)

        log.info({
            "action": "ORDER_REQUEST",
            "params": kwargs,
            "response": response
        })

        return response

      except Exception as e:
        log.error({
            "action": "ORDER_ERROR",
            "params": kwargs,
            "error": str(e)
        })
        raise
