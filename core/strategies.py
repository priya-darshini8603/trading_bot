import time

class TWAPStrategy:
    def __init__(self, order_manager):
        self.om = order_manager

    def execute(self, symbol, side, total_qty, intervals):
        slice_qty = total_qty / intervals

        for i in range(intervals):
            order = self.om.market(symbol, side, slice_qty)
            print(f"TWAP slice executed | qty={slice_qty}")
            time.sleep(5)
