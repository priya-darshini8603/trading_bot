def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Quantity must be positive")
