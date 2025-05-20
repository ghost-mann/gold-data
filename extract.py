import requests
import os
from dotenv import load_dotenv

load_dotenv()

GOLD_API_KEY = os.getenv('API_KEY')

def fetch_xauusd_data():
    url = f"https://api.twelvedata.com/time_series?symbol=XAU/USD&interval=5min&apikey={GOLD_API_KEY}"
    return requests.get(url).json()
