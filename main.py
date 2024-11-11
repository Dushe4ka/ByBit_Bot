import asyncio
from services import (
    get_last_price,
    place_order,
    close_position,
    monitor_profit,
    send_telegram_message,
)


async def main():
    symbol = 'BTCUSDT'
    qty = 0.001
    entry_price = get_last_price(symbol)

    order_id = place_order(symbol, 'Buy', qty)
    if order_id:
        await send_telegram_message(f"Открыта позиция: {symbol} по цене {entry_price}")
        # Начинаем отслеживание прибыли
        await monitor_profit(entry_price, symbol, qty)

if __name__ == "__main__":
    asyncio.run(main())