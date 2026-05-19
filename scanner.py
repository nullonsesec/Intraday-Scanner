import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

from fetcher import fetch_stock_data
from filters import filter_stocks
from html_generator import generate_html
from telegram import send_telegram_alert
from symbols import get_nse_symbols, get_bse_symbols

MAX_THREADS = 20

def main():
    nse = get_nse_symbols()
    bse = get_bse_symbols()

    symbols = list(set(nse + bse))

    results = []

    print(f"Scanning {len(symbols)} stocks...")

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = {
            executor.submit(fetch_stock_data, symbol): symbol
            for symbol in symbols
        }

        for future in as_completed(futures):
            data = future.result()

            if data:
                results.append(data)

    filtered = filter_stocks(results)

    df = pd.DataFrame(filtered)

    df.to_csv("../output/stocks.csv", index=False)

    generate_html(filtered, "../output/stocks.html")
    generate_html(filtered, "../docs/index.html")

    if not df.empty:
        top = df.iloc[0]

        message = (
            f"TOP STOCK: {top['symbol']}\n"
            f"Move: ₹{top['movement']}\n"
            f"RSI: {top['rsi']}\n"
            f"AI Score: {top['ai_score']}"
        )

        send_telegram_alert(message)

    print(df)

if __name__ == "__main__":
    main()