def validate_symbol(symbol: str) -> str:
    """Ensure the symbol is uppercase and looks reasonable."""
    symbol = symbol.strip().upper()
    if len(symbol) < 3:
        raise ValueError("Symbol is too short.")
    return symbol

def validate_side(side: str) -> str:
    """Ensure side is either BUY or SELL."""
    side = side.strip().upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")
    return side

def validate_order_type(order_type: str) -> str:
    """Ensure order type is MARKET or LIMIT."""
    order_type = order_type.strip().upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")
    return order_type

def validate_quantity(quantity: float) -> float:
    """Ensure quantity is positive."""
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    return quantity

def validate_price(price: float, order_type: str) -> float:
    """Ensure price is positive if order type is LIMIT."""
    if order_type == "LIMIT" and price <= 0:
        raise ValueError("Price must be greater than zero for LIMIT orders.")
    return price
