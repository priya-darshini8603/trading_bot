from binance.enums import *
from utils.validator import *
from core.risk import RiskManager

class OrderManager:
    def __init__(self, client):
        self.client = client

    def market(self, symbol, side, qty):
        validate_side(side)
        validate_quantity(qty)
        RiskManager.check_position_size(qty)

        return self.client.futures_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=qty
        )

    def limit(self, symbol, side, qty, price):
        return self.client.futures_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_LIMIT,
            quantity=qty,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC
        )

    def stop_limit(self, symbol, side, qty, stop, price):
        return self.client.futures_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_STOP,
            quantity=qty,
            stopPrice=stop,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC
        )
