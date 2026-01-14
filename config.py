import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
BASE_URL = os.getenv("BINANCE_BASE_URL")

MAX_POSITION_SIZE = 0.05

if not API_KEY or not API_SECRET:
    raise EnvironmentError("API keys not found. Check your .env file.")

DEFAULT_SYMBOL = "BTCUSDT"