# use for environment variables
import os
import time
import calendar
import threading
from binance.client import Client
from datetime import datetime, timedelta
import time
from itertools import count
import json

TESTNET = False

if TESTNET:
    api_key = 'nYH4oc6HQl0P8gCUb7PpW8WHsGc5pmfYbcHyjr3y2oDd9y0690w0vKayZjoIRZw4'
    api_secret = 'r29O1aWoAn48V17SfeePE9jTK6YywXReSiqdqTY8BXWB470yRSiPm5wUMh9gc41v'
    client = Client(api_key, api_secret)
    client.API_URL = 'https://testnet.binance.vision/api'
else:
    api_key = 'f1KzRyDIciGXKW88Z8UvZ55CeefAG5svrMFdUlnjMSHK49MaQAgm343Q1IZvQqgl'
    api_secret = 'fwUAvrW3fbgMX6jlec94W0EcWFWBzrNAWK60QtYAeO7xbGq35vEU0T8bBtW9W5qj'
    client = Client(api_key, api_secret)





def simplify(hash):
    symbol = hash['symbol']
    avg = hash['fills'][0]['price']
    boughtTime = hash['transactTime']

    portfolio = {}
    portfolio['symbol'] = symbol
    portfolio['avg'] = avg
    portfolio['time'] = boughtTime

    return portfolio



# print(calendar.timegm(time.gmtime())) # get current time
raw_data = {'symbol': 'ETHUSDT', 'orderId': 7391031015, 'orderListId': -1, 'clientOrderId': 'xNCb0pAlXJELjmBWCuxpD0', 'transactTime': 1641965637373, 'price': '0.00000000', 'origQty': '0.00320000', 'executedQty': '0.00320000', 'cummulativeQuoteQty': '10.32073600', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'BUY', 'fills': [{'price': '3225.23000000', 'qty': '0.00320000', 'commission': '0.00000320', 'commissionAsset': 'ETH', 'tradeId': 728617066}]}

max_minutes = 10


holdings = 0
simple = {}

def pick_coin():
    print("ETHUSDT picked...")
    return 'ETHUSDT'

def buy(coin='ETHUSDT'):
    try:
        print("buying coin")
        buy_market = client.create_order(symbol='ETHUSDT', side='BUY', type='MARKET', quantity=3.1013)
        simple = simplify(buy_market)
        holdings = 1
        print("coin bought")
    except Exception as e:
        print(e)


def sell(coin='ETHUSDT'):
    try:
        print("selling coin")
        sell_market = client.create_order(symbol='ETHUSDT', side='SELL', type='MARKET', quantity=3.1013)
        simple = {}
        holdings = 0
        print("coin sold")
    except Exception as e:
        print(e)


def main():
    while True:
        if holdings == 0:
            # buy coin
            coin = pick_coin()
            buy(coin)
        else:
            # check time, take profit, stop loss
            time_passed = calendar.timegm(time.gmtime()) - simple['time']

            if time_passed >= 60*max_minutes:
                print("maximum minute passed, selling coins")
                sell(coin)
            else:

                coinInfo = client.get_symbol_ticker(symbol=coin)
                currentPrice = coinInfo['price']
                boughtPrice = simple['bought']
                percentage = ((currentPrice - boughtPrice)/boughtPrice)*100
                print(f"percentage is {percentage}")

                if percentage >= 3.0 or percentage<=-3:
                    sell(coin)
                else:
                    pass



my_account = client.get_account()
total_value = 0

for hashmap in my_account['balances']:
    if float(hashmap['free']) > 0:
        coinName = hashmap['asset']
        if coinName!='USDT':
            coinName+='USDT'
            print(coinName)
            coinInfo = client.get_symbol_ticker(symbol=coinName)
            total_value+=float(coinInfo['price'])*float(hashmap['free'])
        else:
            total_value+=float(hashmap['free'])
    else:
        pass




    print(total_value)






