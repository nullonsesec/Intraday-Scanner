# README.md

Intraday Scanner Pro

Production-grade NSE/BSE momentum scanner with AI-powered ranking, RSI filters, volume breakout detection, Telegram alerts, GitHub automation, and HTML dashboard generation.

---

Features

* ✅ Full NSE + BSE dynamic stock scanning
* ✅ Multithreaded scanning engine
* ✅ Weekly momentum detection
* ✅ Price filtering (₹220–₹650)
* ✅ RSI-based filtering
* ✅ Volume breakout detection
* ✅ AI momentum ranking
* ✅ Telegram alerts
* ✅ CSV export
* ✅ HTML dashboard generation
* ✅ GitHub Actions automation
* ✅ GitHub Pages deployment support

---

Scanner Logic

Stocks are filtered based on:

| Condition       | Value             |
| --------------- | ----------------- |
| Price Range     | ₹220 – ₹650       |
| Weekly Movement | > ₹20             |
| RSI             | > 55              |
| Volume Breakout | Optional AI boost |

---

AI Ranking System

The AI score is calculated using:

```python
AI Score =
(Movement × 0.5)
+ (RSI × 0.3)
+ Volume Breakout Bonus
```

This helps prioritize:

* Strong momentum
* Healthy RSI
* Unusual volume activity

---

Project Structure

```bash
intraday-scanner-pro/
│
├── scanner/
│   ├── scanner.py
│   ├── fetcher.py
│   ├── filters.py
│   ├── symbols.py
│   ├── telegram.py
│   ├── html_generator.py
│
├── output/
│   ├── stocks.csv
│   ├── stocks.html
│
├── docs/
│   ├── index.html
│   ├── wiki.md
│
├── .github/workflows/
│   ├── daily-scan.yml
│
├── requirements.txt
├── README.md
```

---

Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/intraday-scanner-pro.git

cd intraday-scanner-pro
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

Usage

## Run Scanner

```bash
cd scanner

python scanner.py
```

---

Output

Generated automatically:

| File               | Description            |
| ------------------ | ---------------------- |
| output/stocks.csv  | CSV stock results      |
| output/stocks.html | HTML dashboard         |
| docs/index.html    | GitHub Pages dashboard |

---

GitHub Pages Setup

Enable GitHub Pages:

```text
Settings
→ Pages
→ Deploy from branch
→ main/docs
```

Your dashboard will be available at:

```text
https://YOUR_USERNAME.github.io/intraday-scanner-pro/
```

---

Telegram Alerts Setup

Edit:

```bash
scanner/telegram.py
```

Add your credentials:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"

CHAT_ID = "YOUR_CHAT_ID"
```

---

GitHub Actions Automation

Included workflow:

```text
.github/workflows/daily-scan.yml
```

Runs automatically on weekdays.

---

Future Enhancements

Planned upgrades:

* Candlestick pattern detection
* Backtesting engine
* ML prediction model
* Breakout confidence scoring
* SQLite historical database
* TradingView integration
* Sector-wise scanner
* Swing trading mode

---

Disclaimer

This project is for educational and research purposes only.

The scanner does NOT provide financial advice. Always perform your own due diligence before making investment decisions.

---

Tech Stack

* Python
* Pandas
* yFinance
* Jinja2
* GitHub Actions
* Telegram Bot API

---

Contributing

Pull requests and feature suggestions are welcome.

---

License

MIT License
