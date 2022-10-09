import sys
import os
import sys
import time
from datetime import datetime
from pprint import pprint

import ccxt

exchange = ccxt.binance({})
btc_attuale = exchange.fetchTicker("BTC/USDT")["last"]
eth_attuale = exchange.fetchTicker("ETH/USDT")["last"]

if __name__== "__main__":
    print(f"BTC: {btc_attuale}$     ETH: {eth_attuale}$")
    time.sleep(1)