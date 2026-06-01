from binance.exceptions import BinanceAPIException
from bot.logging_config import logger

def place_order(client, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """
    Places an order on Binance Futures Testnet.
    Returns the order response dictionary.
    """
    logger.info(f"Preparing to place {order_type} {side} order for {quantity} {symbol}")
    
    try:
        if order_type == "MARKET":
            logger.info("Sending MARKET order to Binance API.")
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )
        elif order_type == "LIMIT":
            logger.info(f"Sending LIMIT order to Binance API at price {price}.")
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                timeInForce='GTC',
                quantity=quantity,
                price=str(price)
            )
        else:
            raise ValueError(f"Unsupported order type: {order_type}")
            
        logger.info(f"Order placed successfully. Order ID: {response.get('orderId')}")
        return response
        
    except BinanceAPIException as e:
        logger.error(f"Binance API Exception occurred: {e.message} (Code: {e.status_code})")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        raise
