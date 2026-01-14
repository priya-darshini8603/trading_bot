
# 🚀 Binance Futures Trading Bot (Testnet)

An advanced, modular **Python-based trading bot** built for **Binance USDT-M Futures Testnet**, supporting **Market, Limit, and TWAP strategies** with proper **risk management, logging, validation, and CLI interface**.

---

## 📌 Features

✅ Binance **Futures Testnet (USDT-M)** support  
✅ Market & Limit Orders  
✅ **Advanced Order Strategy: TWAP (Time-Weighted Average Price)**  
✅ Buy & Sell order sides  
✅ Modular, reusable architecture  
✅ Command-Line Interface (CLI)  
✅ Input validation & risk checks  
✅ Centralized logging (API requests, responses, errors)  
✅ Environment-based API key management  
✅ Git-safe (`.env` ignored)

---

## 🧠 Advanced Strategy: TWAP

TWAP splits a large order into **multiple smaller market orders** executed at **fixed intervals** to minimize market impact.

Example:
- Total Quantity: `0.04 BTC`
- Intervals: `4`
- Slice Quantity: `0.01 BTC` every interval

---

## 📁 Project Structure

```

├── README.md
├── requirements.txt
├── terminal output.png
├── utils
│   ├── validator.py        # Input validation logic
│   └── logger.py           # Centralized logging utility
├── core
│   ├── risk.py             # Risk management checks
│   ├── strategies.py       # TWAP and strategy logic
│   ├── client.py           # Binance Futures Testnet client
│   └── order_manager.py    # Order execution layer
├── config.py               # Configuration & constants
├── cli.py                  # Command-line argument parser
├── main.py                 # Application entry point
└── .gitignore

````

---

## ⚙️ Tech Stack

- **Python 3.9+**
- `python-binance`
- Binance Futures **REST API**
- Logging & argparse
- Binance **USDT-M Testnet**

---

## 🔐 Environment Setup

Create a `.env` file in the project root:

```env
API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_api_secret
BASE_URL=https://testnet.binancefuture.com
````

---

## 📦 Installation

```bash
git clone https://github.com/priya-darshini8603/trading_bot.git
cd trading_bot
pip install -r requirements.txt
```

---

## 🖥️ Usage (CLI)

### ▶ Market Order

```bash
python main.py --side BUY --type market --qty 0.01
```

### ▶ Limit Order

```bash
python main.py --side SELL --type limit --qty 0.01 --price 45000
```

### ▶ TWAP Order (Advanced)

```bash
python main.py --side BUY --type twap --qty 0.04 --intervals 4
```

---
