import logging
import sys

def setup_logger():
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)

    # Don't add multiple handlers if the logger already has them
    if not logger.handlers:
        # File handler for logs
        file_handler = logging.FileHandler("trading_bot.log")
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)

        # We will keep console output simple, rich will handle CLI outputs separately
        # But we can add a simple stream handler for debugging if needed
        # We don't want to clutter the CLI with raw logs.
        # So we'll only log to file by default, unless it's a critical error.
        
        logger.addHandler(file_handler)

    return logger

logger = setup_logger()
