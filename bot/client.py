from binance.client import Client
from bot.logging_config import logger

class BinanceTestnetClient:
    
    def __init__(self, api_key: str, secret_key: str):
        if not api_key or not secret_key:
            raise ValueError("API Key and Secret Key are required.")
            
        logger.info("Initializing Binance Futures Testnet Client.")
        # testnet=True handles the URL routing correctly for python-binance, 
        # but we explicitly set it here to be absolutely sure we hit the correct endpoint.
        self.client = Client(api_key, secret_key, testnet=True)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        
        # Sync time to avoid timestamp out of bounds errors
        try:
            import time
            server_time = self.client.futures_time()['serverTime']
            local_time = int(time.time() * 1000)
            self.client.timestamp_offset = server_time - local_time
            logger.info(f"Time synced with Binance server. Offset: {self.client.timestamp_offset}ms")
        except Exception as e:
            logger.warning(f"Failed to sync time with server: {e}")        
    def get_client(self):
        return self.client
