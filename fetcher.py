import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator

def fetch_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1mo")

        if len(hist) < 10:
            return None

        first_close = hist["Close"].iloc[-7]
        last_close = hist["Close"].iloc[-1]

        movement = last_close - first_close

        avg_volume = hist["Volume"].mean()
        latest_volume = hist["Volume"].iloc[-1]

        volume_breakout = latest_volume > (avg_volume * 1.5)

        rsi = RSIIndicator(hist["Close"]).rsi().iloc[-1]

        ai_score = (
            movement * 0.5 +
            rsi * 0.3 +
            (10 if volume_breakout else 0)
        )

        return {
            "symbol": symbol,
            "price": round(last_close, 2),
            "movement": round(movement, 2),
            "percent": round((movement / first_close) * 100, 2),
            "rsi": round(rsi, 2),
            "volume_breakout": volume_breakout,
            "ai_score": round(ai_score, 2)
        }

    except Exception:
        return None