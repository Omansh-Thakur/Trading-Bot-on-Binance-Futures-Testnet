import os
import click
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from bot.client import BinanceTestnetClient
from bot.orders import place_order
from bot.validators import (
    validate_symbol, validate_side, validate_order_type,
    validate_quantity, validate_price
)
from bot.logging_config import logger

console = Console()

def print_welcome_message():
    """Display a welcome message using rich."""
    console.print(Panel.fit(
        "[bold cyan]Binance Futures Testnet Trading Bot[/bold cyan]\n"
        "A simple CLI tool to place orders on USDT-M testnet.",
        border_style="cyan"
    ))

@click.command()
@click.option('--symbol', prompt='Enter symbol (e.g., BTCUSDT)', help='Trading pair symbol.')
@click.option('--side', prompt='Enter side (BUY/SELL)', type=click.Choice(['BUY', 'SELL'], case_sensitive=False), help='Order side.')
@click.option('--order-type', prompt='Enter order type (MARKET/LIMIT)', type=click.Choice(['MARKET', 'LIMIT'], case_sensitive=False), help='Order type.')
@click.option('--quantity', prompt='Enter quantity', type=float, help='Order quantity.')
@click.option('--price', type=float, default=0.0, help='Order price (required for LIMIT orders).')
def main(symbol, side, order_type, quantity, price):
    """Simple Trading Bot CLI for Binance Futures Testnet."""
    
    print_welcome_message()
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("BINANCE_TESTNET_API_KEY")
    secret_key = os.getenv("BINANCE_TESTNET_SECRET_KEY")

    if not api_key or not secret_key or api_key == "your_testnet_api_key_here":
        console.print("[bold red]Error:[/] API credentials not found or not set in .env file.")
        logger.error("Missing API credentials.")
        return

    # If it's a limit order, we might need to prompt for price if not provided
    if order_type.upper() == "LIMIT" and price <= 0:
        price = click.prompt('Enter price for LIMIT order', type=float)

    # Validation
    try:
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)
    except ValueError as e:
        console.print(f"[bold red]Validation Error:[/] {e}")
        logger.error(f"Validation Error: {e}")
        return

    # Summarize Request
    table = Table(title="Order Summary", show_header=True, header_style="bold magenta")
    table.add_column("Parameter", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Symbol", symbol)
    table.add_row("Side", side)
    table.add_row("Type", order_type)
    table.add_row("Quantity", str(quantity))
    if order_type == "LIMIT":
        table.add_row("Price", str(price))

    console.print(table)
    
    if not click.confirm('Do you want to proceed with placing this order?'):
        console.print("[yellow]Order cancelled by user.[/yellow]")
        logger.info("Order cancelled by user at confirmation step.")
        return

    # Execution
    try:
        console.print("[cyan]Connecting to Binance Testnet...[/cyan]")
        bot_client = BinanceTestnetClient(api_key, secret_key)
        
        with console.status("[bold green]Placing order...") as status:
            response = place_order(bot_client.get_client(), symbol, side, order_type, quantity, price)
        
        # Display Success Response
        console.print("\n[bold green]SUCCESS: Order Placed Successfully![/bold green]")
        
        res_table = Table(title="Order Response Details", show_header=True, header_style="bold blue")
        res_table.add_column("Key", style="cyan")
        res_table.add_column("Value", style="green")
        
        keys_to_show = ['orderId', 'symbol', 'status', 'clientOrderId', 'price', 'origQty', 'executedQty']
        for k in keys_to_show:
            if k in response:
                res_table.add_row(k, str(response[k]))
                
        console.print(res_table)
        
    except Exception as e:
        console.print(f"\n[bold red]ERROR: Failed to place order![/bold red]")
        console.print(f"[red]Error Details:[/] {str(e)}")
        logger.error(f"Failed to place order from CLI: {str(e)}")

if __name__ == '__main__':
    main()
