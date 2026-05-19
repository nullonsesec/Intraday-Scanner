import requests

def get_nse_symbols():
    url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"

    try:
        response = requests.get(url, timeout=10)
        lines = response.text.splitlines()[1:]

        symbols = []

        for line in lines:
            parts = line.split(',')

            if parts:
                symbol = parts[0].strip().replace('"', '')
                symbols.append(f"{symbol}.NS")

        return symbols

    except Exception:
        return []

def get_bse_symbols():
    url = "https://api.bseindia.com/BseIndiaAPI/api/ListofScripData/w"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        symbols = []

        for item in data:
            symbol = item.get("scripcd")

            if symbol:
                symbols.append(f"{symbol}.BO")

        return symbols

    except Exception:
        return []