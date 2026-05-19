def filter_stocks(stocks):
    filtered = []

    for stock in stocks:
        if not stock:
            continue

        if (
            220 <= stock["price"] <= 650 and
            stock["movement"] > 20 and
            stock["rsi"] > 55
        ):
            filtered.append(stock)

    return sorted(
        filtered,
        key=lambda x: x["movement"],
        reverse=True
    )