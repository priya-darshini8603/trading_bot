from config import MAX_POSITION_SIZE

class RiskManager:
    @staticmethod
    def check_position_size(quantity):
        if quantity > MAX_POSITION_SIZE:
            raise Exception("Risk violation: Position size exceeded")
