# Binance Futures Testnet Trading Bot

This is a Python command-line application that allows you to place MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M). It is built with `python-binance` for API interactions and `click` & `rich` for an enhanced CLI user experience.

## Features
- **Place Orders**: Supports MARKET and LIMIT orders.
- **Both Sides**: Supports BUY (Long) and SELL (Short).
- **Interactive CLI**: Prompts for required inputs if not provided via arguments, and shows a summary table before confirming.
- **Logging**: All API interactions and errors are safely logged to `trading_bot.log`.
- **Validation**: Strict input validation to prevent user errors before sending API requests.

## Prerequisites
- Python 3.8+
- Binance Futures Testnet Account

## Setup Steps

1. **Clone/Download the repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Environment**:
   - Copy `.env.example` to a new file named `.env`
   - Open `.env` and fill in your Binance Futures Testnet API Key and Secret Key.
     ```env
     BINANCE_TESTNET_API_KEY=your_testnet_api_key
     BINANCE_TESTNET_SECRET_KEY=your_testnet_secret_key
     ```

## How to Run Examples

You can run the script interactively or by passing arguments directly.

### Interactive Mode
Simply run the script, and it will prompt you for everything:
```bash
python cli.py
```

### Passing Arguments
**Market Order (BUY):**
```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

**Limit Order (SELL):**
```bash
python cli.py --symbol ETHUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 3500
```

## Logging
Logs are automatically written to `trading_bot.log` in the root directory. This contains details of requests, responses, and errors.

## Author

Omansh Thakur  
