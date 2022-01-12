import os
import time
import calendar
import threading
from typing import Set

from binance.client import Client
from datetime import datetime, timedelta
import time
from itertools import count
import json

class Solution:
    def tradeBot(self, testMode):
        TESTNET = testMode
        max_minutes = 3
        holdings = 0
        simple = {}
        possible_set = {'MCOUSDT', 'TORNUSDT', 'GTCUSDT', 'BTGUSDT', 'USDTTRY', 'EGLDUSDT', 'MLNUSDT', 'EOSBEARUSDT', 'XRPBULLUSDT', 'QTUMUSDT', 'PEOPLEUSDT', 'RGTUSDT', 'DREPUSDT', 'BTTUSDT', 'BURGERUSDT', 'GALAUSDT', 'DOGEUSDT', 'CTXCUSDT', 'NUUSDT', 'AMPUSDT', 'STXUSDT', 'BATUSDT', 'DEGOUSDT', 'BZRXUSDT', 'RAYUSDT', 'NKNUSDT', 'DEXEUSDT', 'XZCUSDT', 'HIVEUSDT', 'ONGUSDT', 'AXSUSDT', 'KAVAUSDT', 'KEEPUSDT', 'WAXPUSDT', 'IMXUSDT', 'TOMOUSDT', 'KEYUSDT', 'HOTUSDT', 'LSKUSDT', 'BNBBEARUSDT', 'SOLUSDT', 'FARMUSDT', 'IDEXUSDT', 'CTSIUSDT', 'USDTBRL', 'SUNUSDT', 'AUDIOUSDT', 'COMPUSDT', 'TRUUSDT', 'ENJUSDT', 'SANTOSUSDT', 'BCHSVUSDT', 'ANTUSDT', 'BAKEUSDT', 'BTCUSDT', 'PONDUSDT', 'LINAUSDT', 'RLCUSDT', 'FUNUSDT', 'FORUSDT', 'MBOXUSDT', 'FETUSDT', 'ACMUSDT', 'SYSUSDT', 'USDPUSDT', 'BETAUSDT', 'XRPBEARUSDT', 'MKRUSDT', 'WINGUSDT', 'REEFUSDT', 'YFIIUSDT', 'STRAXUSDT', 'DATAUSDT', 'AVAUSDT', 'LUNAUSDT', 'AVAXUSDT', 'CLVUSDT', 'IOTAUSDT', 'DCRUSDT', 'CITYUSDT', 'INJUSDT', 'PSGUSDT', 'XMRUSDT', 'BEARUSDT', 'NULSUSDT', 'PERPUSDT', 'RIFUSDT', 'AGLDUSDT', 'BCHUSDT', 'PNTUSDT', 'ONEUSDT', 'FIROUSDT', 'BARUSDT', 'GHSTUSDT', 'HARDUSDT', 'FILUSDT', 'VIDTUSDT', 'LENDUSDT', 'AAVEUSDT', 'ALPACAUSDT', 'NANOUSDT', 'ARPAUSDT', 'CFXUSDT', 'NBSUSDT', 'HBARUSDT', 'CHRUSDT', 'VTHOUSDT', 'DIAUSDT', 'SKLUSDT', 'EOSUSDT', 'BADGERUSDT', 'FORTHUSDT', 'CELOUSDT', 'CHZUSDT', 'USDTBIDR', 'CVPUSDT', 'USDSUSDT', 'DAIUSDT', 'BTCSTUSDT', 'WANUSDT', 'OCEANUSDT', 'USDTBKRW', 'MDTUSDT', 'ENSUSDT', 'LRCUSDT', 'WRXUSDT', 'MINAUSDT', 'ZILUSDT', 'RUNEUSDT', 'GXSUSDT', 'LINKUSDT', 'ANKRUSDT', 'RSRUSDT', 'FTTUSDT', 'RNDRUSDT', 'BELUSDT', 'UMAUSDT', 'FIDAUSDT', 'RAMPUSDT', 'PYRUSDT', 'TVKUSDT', 'PAXUSDT', 'TROYUSDT', 'FIOUSDT', 'TRXUSDT', 'BALUSDT', 'XVGUSDT', '1INCHUSDT', 'POWRUSDT', 'THETAUSDT', 'USDTUAH', 'COTIUSDT', 'DGBUSDT', 'BTSUSDT', 'KMDUSDT', 'ETCUSDT', 'TRIBEUSDT', 'QIUSDT', 'ROSEUSDT', 'PUNDIXUSDT', 'OMGUSDT', 'ILVUSDT', 'STORMUSDT', 'HNTUSDT', 'GRTUSDT', 'USDTGYEN', 'AIONUSDT', 'JASMYUSDT', 'BANDUSDT', 'RADUSDT', 'PAXGUSDT', 'ERDUSDT', 'MANAUSDT', 'LTOUSDT', 'LTCUSDT', 'SPELLUSDT', 'XRPUSDT', 'NMRUSDT', 'STORJUSDT', 'ALGOUSDT', 'WAVESUSDT', 'ATAUSDT', 'CHESSUSDT', 'BCCUSDT', 'FRONTUSDT', 'RVNUSDT', 'OGNUSDT', 'BNTUSDT', 'KSMUSDT', 'FLMUSDT', 'ANYUSDT', 'POLYUSDT', 'DNTUSDT', 'ALCXUSDT', 'ONTUSDT', 'BEAMUSDT', 'USDTBVND', 'MITHUSDT', 'DOTUSDT', 'GNOUSDT', 'ORNUSDT', 'TFUELUSDT', 'ELFUSDT', 'SUSHIUSDT', 'CVXUSDT', 'LAZIOUSDT', 'REQUSDT', 'MASKUSDT', 'HIGHUSDT', 'JSTUSDT', 'JOEUSDT', 'ICXUSDT', 'USDTRUB', 'ADXUSDT', 'USDTNGN', 'BNXUSDT', 'MDXUSDT', 'PORTOUSDT', 'XLMUSDT', 'FLUXUSDT', 'XVSUSDT', 'ARDRUSDT', 'AUDUSDT', 'YFIUSDT', 'HCUSDT', 'TCTUSDT', 'MTLUSDT', 'USDCUSDT', 'USDTIDRT', 'CELRUSDT', 'IRISUSDT', 'VETUSDT', 'ADAUSDT', 'AKROUSDT', 'MBLUSDT', 'STPTUSDT', 'BUSDTRY', 'USDSBUSDT', 'OXTUSDT', 'SNXUSDT', 'KLAYUSDT', 'USDTZAR', 'ATOMUSDT', 'QUICKUSDT', 'SHIBUSDT', 'ETHUSDT', 'PERLUSDT', 'CAKEUSDT', 'TLMUSDT', 'VOXELUSDT', 'USDTDAI', 'DARUSDT', 'NEARUSDT', 'USTUSDT', 'AUTOUSDT', 'JUVUSDT', 'FXSUSDT', 'GTOUSDT', 'RENUSDT', 'XEMUSDT', 'BLZUSDT', 'COCOSUSDT', 'DOCKUSDT', 'ZENUSDT', 'ACHUSDT', 'ASRUSDT', 'FISUSDT', 'ICPUSDT', 'GLMRUSDT', 'WINUSDT', 'OOKIUSDT', 'CRVUSDT', 'BCHABCUSDT', 'KNCUSDT', 'MCUSDT', 'PHAUSDT', 'BONDUSDT', 'DYDXUSDT', 'MATICUSDT', 'WTCUSDT', 'DASHUSDT', 'NEOUSDT', 'DENTUSDT', 'UNIUSDT', 'FLOWUSDT', 'RAREUSDT', 'ZRXUSDT', 'DUSKUSDT', 'YGGUSDT', 'SFPUSDT', 'TKOUSDT', 'VENUSDT', 'IOTXUSDT', 'BNBUSDT', 'ERNUSDT', 'KP3RUSDT', 'ZECUSDT', 'COSUSDT', 'ALICEUSDT', 'ETHBULLUSDT', 'MIRUSDT', 'EOSBULLUSDT', 'REPUSDT', 'STRATUSDT', 'FTMUSDT', 'BULLUSDT', 'BNBBULLUSDT', 'ETHBEARUSDT', 'C98USDT', 'SCUSDT', 'SANDUSDT', 'UTKUSDT', 'LPTUSDT', 'POLSUSDT', 'CKBUSDT', 'TWTUSDT', 'VGXUSDT', 'VITEUSDT', 'OGUSDT', 'PLAUSDT', 'WNXMUSDT', 'UNFIUSDT', 'CTKUSDT', 'BICOUSDT', 'TRBUSDT', 'MOVRUSDT', 'SLPUSDT', 'AUCTIONUSDT', 'SXPUSDT', 'ALPHAUSDT', 'ARUSDT', 'NPXSUSDT', 'MFTUSDT', 'CVCUSDT', 'SRMUSDT', 'XECUSDT', 'XTZUSDT', 'ATMUSDT', 'DODOUSDT', 'IOSTUSDT', 'OMUSDT', 'EPSUSDT', 'DFUSDT', 'QNTUSDT', 'STMXUSDT', 'LITUSDT', 'BKRWUSDT'}

        if TESTNET:
            api_key = 'nYH4oc6HQl0P8gCUb7PpW8WHsGc5pmfYbcHyjr3y2oDd9y0690w0vKayZjoIRZw4'
            api_secret = 'r29O1aWoAn48V17SfeePE9jTK6YywXReSiqdqTY8BXWB470yRSiPm5wUMh9gc41v'
            client = Client(api_key, api_secret)
            client.API_URL = 'https://testnet.binance.vision/api'
        else:
            api_key = 'f1KzRyDIciGXKW88Z8UvZ55CeefAG5svrMFdUlnjMSHK49MaQAgm343Q1IZvQqgl'
            api_secret = 'fwUAvrW3fbgMX6jlec94W0EcWFWBzrNAWK60QtYAeO7xbGq35vEU0T8bBtW9W5qj'
            client = Client(api_key, api_secret)

        def pick_coin():
            print("ETHUSDT picked...")
            return 'ETHUSDT'



        def simplify(hash):
            # when bot bought coin, update the portfolio in simple format
            symbol = hash['symbol']
            avg = hash['fills'][0]['price']
            boughtTime = hash['transactTime']

            portfolio = {}
            portfolio['symbol'] = symbol
            portfolio['avg'] = avg
            portfolio['time'] = boughtTime

            return portfolio


        def buy(coin='ETHUSDT'):
            try:
                print("buying coin")
                buy_market = client.create_order(symbol='ETHUSDT', side='BUY', type='MARKET', quantity=0.5013)
                return simplify(buy_market), 1
            except Exception as e:
                print(e)


        def sell(coin='ETHUSDT'):
            try:
                print("selling coin")
                sell_market = client.create_order(symbol='ETHUSDT', side='SELL', type='MARKET', quantity=0.5013)
                return {}, 0
            except Exception as e:
                print(e)



        def get_account_value():
            total_value = 0
            my_account = client.get_account()
            for hashmap in my_account['balances']:
                if float(hashmap['free']) > 0:
                    coinName = hashmap['asset']
                    tempName = coinName+"USDT"
                    if tempName in possible_set:
                        coinName += 'USDT'
                        coinInfo = client.get_symbol_ticker(symbol=coinName)
                        total_value += float(coinInfo['price']) * float(hashmap['free'])
                    elif coinName == "USDT":
                        total_value += float(hashmap['free'])
                    else:
                        pass
                else:
                    pass

            return total_value



        def sell_all():
            pass

        def update_portfolio(date,value,filename='portfolio_history.json'):
            with open('portfolio_history.json') as json_file:
                data = json.load(json_file)
                temp = data["history"]
                y = {"date": time.ctime(date), 'value': value}
                temp.append(y)

            with open('portfolio_history.json', "w") as f:
                json.dump(data, f, indent=4)

        sell_all()
        while True:
            if holdings == 0:
                # buy coin
                print("--------------------")
                print("[BUY]")
                coin = pick_coin()
                print(f"Buying {coin}")
                simple, holdings = buy(coin)
                print(f"Now holding {holdings}")
                print(simple)
                print("--------------------")
            else:
                # check time, take profit, stop loss
                print("--------------------")

                time_passed = calendar.timegm(time.gmtime()) - simple['time']/1000

                if time_passed >= 60 * max_minutes:
                    print("[TIME LIMIT PASSED]")
                    print(time_passed)
                    print(f"maximum minute {max_minutes} passed, selling coins")
                    simple, holdings = sell(coin)
                    update_portfolio(calendar.timegm(time.gmtime()),get_account_value())
                    print("--------------------")

                else:
                    print("[TIME LIMIT NOT PASSED]")
                    print(time_passed)
                    coinInfo = client.get_symbol_ticker(symbol=coin)
                    currentPrice = coinInfo['price']
                    boughtPrice = simple['avg']
                    percentage = ((float(currentPrice) - float(boughtPrice)) / float(boughtPrice)) * 100
                    print(f"percentage is {percentage}")

                    if percentage >= 2.0 or percentage <= -1.5:
                        if percentage > 0:
                            print(f"selling with profits: {percentage}")
                        else:
                            print(f"selling with loss: {percentage}")

                        simple, holdings = sell(coin)
                        update_portfolio(calendar.timegm(time.gmtime()), get_account_value())
                    else:
                        print("price didn't hit target")
                        pass

                    print("--------------------")


            time.sleep(5)






#
# bot = Solution()
# bot.tradeBot(True)

