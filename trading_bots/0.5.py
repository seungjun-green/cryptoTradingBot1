import calendar
from binance.client import Client
import time
import json
import math
import random


class Solution:
    def tradeBot(self, testMode, USD, holdings, firstTime, max_min, take_proft, stop_loss):
        TESTNET = testMode
        max_minutes = max_min
        QUANTITY = USD
        portfolio = {}
        possible_set = {'MCOUSDT', 'TORNUSDT', 'GTCUSDT', 'BTGUSDT', 'USDTTRY', 'EGLDUSDT', 'MLNUSDT', 'EOSBEARUSDT', 'XRPBULLUSDT', 'QTUMUSDT', 'PEOPLEUSDT', 'RGTUSDT', 'DREPUSDT', 'BTTUSDT', 'BURGERUSDT', 'GALAUSDT', 'DOGEUSDT', 'CTXCUSDT', 'NUUSDT', 'AMPUSDT', 'STXUSDT', 'BATUSDT', 'DEGOUSDT', 'BZRXUSDT', 'RAYUSDT', 'NKNUSDT', 'DEXEUSDT', 'XZCUSDT', 'HIVEUSDT', 'ONGUSDT', 'AXSUSDT', 'KAVAUSDT', 'KEEPUSDT', 'WAXPUSDT', 'IMXUSDT', 'TOMOUSDT', 'KEYUSDT', 'HOTUSDT', 'LSKUSDT', 'BNBBEARUSDT', 'SOLUSDT', 'FARMUSDT', 'IDEXUSDT', 'CTSIUSDT', 'USDTBRL', 'SUNUSDT', 'AUDIOUSDT', 'COMPUSDT', 'TRUUSDT', 'ENJUSDT', 'SANTOSUSDT', 'BCHSVUSDT', 'ANTUSDT', 'BAKEUSDT', 'BTCUSDT', 'PONDUSDT', 'LINAUSDT', 'RLCUSDT', 'FUNUSDT', 'FORUSDT', 'MBOXUSDT', 'FETUSDT', 'ACMUSDT', 'SYSUSDT', 'USDPUSDT', 'BETAUSDT', 'XRPBEARUSDT', 'MKRUSDT', 'WINGUSDT', 'REEFUSDT', 'YFIIUSDT', 'STRAXUSDT', 'DATAUSDT', 'AVAUSDT', 'LUNAUSDT', 'AVAXUSDT', 'CLVUSDT', 'IOTAUSDT', 'DCRUSDT', 'CITYUSDT', 'INJUSDT', 'PSGUSDT', 'XMRUSDT', 'BEARUSDT', 'NULSUSDT', 'PERPUSDT', 'RIFUSDT', 'AGLDUSDT', 'BCHUSDT', 'PNTUSDT', 'ONEUSDT', 'FIROUSDT', 'BARUSDT', 'GHSTUSDT', 'HARDUSDT', 'FILUSDT', 'VIDTUSDT', 'LENDUSDT', 'AAVEUSDT', 'ALPACAUSDT', 'NANOUSDT', 'ARPAUSDT', 'CFXUSDT', 'NBSUSDT', 'HBARUSDT', 'CHRUSDT', 'VTHOUSDT', 'DIAUSDT', 'SKLUSDT', 'EOSUSDT', 'BADGERUSDT', 'FORTHUSDT', 'CELOUSDT', 'CHZUSDT', 'USDTBIDR', 'CVPUSDT', 'USDSUSDT', 'DAIUSDT', 'BTCSTUSDT', 'WANUSDT', 'OCEANUSDT', 'USDTBKRW', 'MDTUSDT', 'ENSUSDT', 'LRCUSDT', 'WRXUSDT', 'MINAUSDT', 'ZILUSDT', 'RUNEUSDT', 'GXSUSDT', 'LINKUSDT', 'ANKRUSDT', 'RSRUSDT', 'FTTUSDT', 'RNDRUSDT', 'BELUSDT', 'UMAUSDT', 'FIDAUSDT', 'RAMPUSDT', 'PYRUSDT', 'TVKUSDT', 'PAXUSDT', 'TROYUSDT', 'FIOUSDT', 'TRXUSDT', 'BALUSDT', 'XVGUSDT', '1INCHUSDT', 'POWRUSDT', 'THETAUSDT', 'USDTUAH', 'COTIUSDT', 'DGBUSDT', 'BTSUSDT', 'KMDUSDT', 'ETCUSDT', 'TRIBEUSDT', 'QIUSDT', 'ROSEUSDT', 'PUNDIXUSDT', 'OMGUSDT', 'ILVUSDT', 'STORMUSDT', 'HNTUSDT', 'GRTUSDT', 'USDTGYEN', 'AIONUSDT', 'JASMYUSDT', 'BANDUSDT', 'RADUSDT', 'PAXGUSDT', 'ERDUSDT', 'MANAUSDT', 'LTOUSDT', 'LTCUSDT', 'SPELLUSDT', 'XRPUSDT', 'NMRUSDT', 'STORJUSDT', 'ALGOUSDT', 'WAVESUSDT', 'ATAUSDT', 'CHESSUSDT', 'BCCUSDT', 'FRONTUSDT', 'RVNUSDT', 'OGNUSDT', 'BNTUSDT', 'KSMUSDT', 'FLMUSDT', 'ANYUSDT', 'POLYUSDT', 'DNTUSDT', 'ALCXUSDT', 'ONTUSDT', 'BEAMUSDT', 'USDTBVND', 'MITHUSDT', 'DOTUSDT', 'GNOUSDT', 'ORNUSDT', 'TFUELUSDT', 'ELFUSDT', 'SUSHIUSDT', 'CVXUSDT', 'LAZIOUSDT', 'REQUSDT', 'MASKUSDT', 'HIGHUSDT', 'JSTUSDT', 'JOEUSDT', 'ICXUSDT', 'USDTRUB', 'ADXUSDT', 'USDTNGN', 'BNXUSDT', 'MDXUSDT', 'PORTOUSDT', 'XLMUSDT', 'FLUXUSDT', 'XVSUSDT', 'ARDRUSDT', 'AUDUSDT', 'YFIUSDT', 'HCUSDT', 'TCTUSDT', 'MTLUSDT', 'USDCUSDT', 'USDTIDRT', 'CELRUSDT', 'IRISUSDT', 'VETUSDT', 'ADAUSDT', 'AKROUSDT', 'MBLUSDT', 'STPTUSDT', 'BUSDTRY', 'USDSBUSDT', 'OXTUSDT', 'SNXUSDT', 'KLAYUSDT', 'USDTZAR', 'ATOMUSDT', 'QUICKUSDT', 'SHIBUSDT', 'ETHUSDT', 'PERLUSDT', 'CAKEUSDT', 'TLMUSDT', 'VOXELUSDT', 'USDTDAI', 'DARUSDT', 'NEARUSDT', 'USTUSDT', 'AUTOUSDT', 'JUVUSDT', 'FXSUSDT', 'GTOUSDT', 'RENUSDT', 'XEMUSDT', 'BLZUSDT', 'COCOSUSDT', 'DOCKUSDT', 'ZENUSDT', 'ACHUSDT', 'ASRUSDT', 'FISUSDT', 'ICPUSDT', 'GLMRUSDT', 'WINUSDT', 'OOKIUSDT', 'CRVUSDT', 'BCHABCUSDT', 'KNCUSDT', 'MCUSDT', 'PHAUSDT', 'BONDUSDT', 'DYDXUSDT', 'MATICUSDT', 'WTCUSDT', 'DASHUSDT', 'NEOUSDT', 'DENTUSDT', 'UNIUSDT', 'FLOWUSDT', 'RAREUSDT', 'ZRXUSDT', 'DUSKUSDT', 'YGGUSDT', 'SFPUSDT', 'TKOUSDT', 'VENUSDT', 'IOTXUSDT', 'BNBUSDT', 'ERNUSDT', 'KP3RUSDT', 'ZECUSDT', 'COSUSDT', 'ALICEUSDT', 'ETHBULLUSDT', 'MIRUSDT', 'EOSBULLUSDT', 'REPUSDT', 'STRATUSDT', 'FTMUSDT', 'BULLUSDT', 'BNBBULLUSDT', 'ETHBEARUSDT', 'C98USDT', 'SCUSDT', 'SANDUSDT', 'UTKUSDT', 'LPTUSDT', 'POLSUSDT', 'CKBUSDT', 'TWTUSDT', 'VGXUSDT', 'VITEUSDT', 'OGUSDT', 'PLAUSDT', 'WNXMUSDT', 'UNFIUSDT', 'CTKUSDT', 'BICOUSDT', 'TRBUSDT', 'MOVRUSDT', 'SLPUSDT', 'AUCTIONUSDT', 'SXPUSDT', 'ALPHAUSDT', 'ARUSDT', 'NPXSUSDT', 'MFTUSDT', 'CVCUSDT', 'SRMUSDT', 'XECUSDT', 'XTZUSDT', 'ATMUSDT', 'DODOUSDT', 'IOSTUSDT', 'OMUSDT', 'EPSUSDT', 'DFUSDT', 'QNTUSDT', 'STMXUSDT', 'LITUSDT', 'BKRWUSDT'}

        coin_list = []


        if TESTNET:
            api_key = 'nYH4oc6HQl0P8gCUb7PpW8WHsGc5pmfYbcHyjr3y2oDd9y0690w0vKayZjoIRZw4'
            api_secret = 'r29O1aWoAn48V17SfeePE9jTK6YywXReSiqdqTY8BXWB470yRSiPm5wUMh9gc41v'
            client = Client(api_key, api_secret)
            client.API_URL = 'https://testnet.binance.vision/api'
        else:
            api_key = 'f1KzRyDIciGXKW88Z8UvZ55CeefAG5svrMFdUlnjMSHK49MaQAgm343Q1IZvQqgl'
            api_secret = 'fwUAvrW3fbgMX6jlec94W0EcWFWBzrNAWK60QtYAeO7xbGq35vEU0T8bBtW9W5qj'
            client = Client(api_key, api_secret)

        def get_possible():
            FIATS = ['EURUSDT', 'GBPUSDT', 'JPYUSDT', 'USDUSDT', 'DOWN', 'UP']
            PAIR_WITH = 'USDT'
            prices = client.get_all_tickers()
            possible_set = set()
            for coin in prices:

                # only Return USDT pairs and exclude margin symbols like BTCDOWNUSDT
                if PAIR_WITH in coin['symbol'] and all(item not in coin['symbol'] for item in FIATS):
                    possible_set.add(coin['symbol'])

            return possible_set

        ### only used in sell_all()
        def round_decimals_down(number: float, decimals: int):
            """
            Returns a value rounded down to a specific number of decimal places.
            """
            if not isinstance(decimals, int):
                raise TypeError("decimal places must be an integer")
            elif decimals < 0:
                raise ValueError("decimal places has to be 0 or more")
            elif decimals == 0:
                return math.floor(number)

            factor = 10 ** decimals
            return math.floor(number * factor) / factor

        ### func to sell coins, only used when calling sell_all() func
        def sell_inv(coin, qnt):

            try:
                print(f"selling {coin}, {qnt}")
                sell_market = client.create_order(symbol=coin, side='SELL', type='MARKET', quantity=qnt)
            except Exception as e:
                print(e)

        # sell all coins in portfolio into USDT if possible
        def sell_all():
            my_account = client.get_account()
            lot_size = {}
            volume = {}
            for hashmap in my_account['balances']:
                if float(hashmap['free']) > 0:
                    coinName = hashmap['asset']
                    tempName = coinName + 'USDT'
                    if tempName in possible_set:
                        try:
                            info = client.get_symbol_info(tempName)
                            step_size = info['filters'][2]['stepSize']
                            lot_size[tempName] = step_size.index('1') - 1

                            if lot_size[tempName] < 0:
                                lot_size[tempName] = 0

                        except:
                            pass

                        # round down current qnt to fit lot_size format because we can't sell more than we have
                        if tempName not in lot_size:
                            volume[tempName] = round_decimals_down(float(hashmap['free']), 1)
                        else:
                            volume[tempName] = round_decimals_down(float(hashmap['free']), lot_size[tempName])

                        sell_inv(tempName, volume[tempName])

        # update portfolio after buying a new coin
        def update_portfolio_add(hash):
            # when bot bought coin, update the portfolio in simple format
            symbol = hash['symbol']
            coin_bought = {}
            coin_bought['avg'] = hash['fills'][0]['price']
            coin_bought['time'] = hash['transactTime']
            coin_bought['qnt'] = hash['executedQty']
            portfolio[symbol] = coin_bought

        def convertVolume(coin):
            lot_size = {}
            volume = {}
            try:
                info = client.get_symbol_info(coin)
                step_size = info['filters'][2]['stepSize']
                lot_size[coin] = step_size.index('1') - 1

                if lot_size[coin] < 0:
                    lot_size[coin] = 0

            except:
                lot_size[coin] = 1

            volume[coin] = float(QUANTITY / float(currentPirce(coin)))

            if coin not in lot_size:
                volume[coin] = float('{:.1f}'.format(volume[coin]))

            else:
                volume[coin] = float('{:.{}f}'.format(volume[coin], lot_size[coin]))

            return volume[coin], lot_size[coin]

        # func to get current price of certain coin
        def currentPirce(coin):
            coinInfo = client.get_symbol_ticker(symbol=coin)
            return coinInfo['price']

        # func to buy coins
        def buy(coin):
            try:
                qnt, lotsize = convertVolume(coin)
                print(f"buying coin {qnt}")
                buy_market = client.create_order(symbol=coin, side='BUY', type='MARKET', quantity=qnt)
                # update portfolio
                update_portfolio_add(buy_market) # add new holding
            except Exception as e:
                print(e)

        def count_after_dot(s):
            for i in range(len(s)):
                if s[i] == '.':
                    return len(s[i + 1:])

                return 0


        # func to sell coins
        def sell(coin):
            try:
                print(coin)
                print("selling coin", portfolio[coin]['qnt'])
                s = portfolio[coin]['qnt']
                sell_market = client.create_order(symbol=coin, side='SELL', type='MARKET', quantity=s)
                del portfolio[coin]
                print(coin, portfolio)
            except Exception as e:
                print("try selling again ....... ")
                s = portfolio[coin]['qnt']
                d = (float(s) * pow(10, count_after_dot(s)) - 1) / pow(10, count_after_dot(s))
                sell_market = client.create_order(symbol=coin, side='SELL', type='MARKET',quantity=d)
                print("귀여웠던 혁준이")
                del portfolio[coin]
                print(coin, portfolio)

        # get account value in USDT
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

        # update json  file
        def update_json_file(date,value,filename='portfolio_history.json'):
            with open('portfolio_history.json') as json_file:
                data = json.load(json_file)
                temp = data["history"]
                y = {"date": time.ctime(date), 'value': value}
                temp.append(y)

            with open('portfolio_history.json', "w") as f:
                json.dump(data, f, indent=4)

        def create_first_list():
            # get symbols - base aseet in USDT and currently Trading
            print("Creating first coin list ... ")
            coin_list = []
            info = client.get_exchange_info()
            FIATS = ['EURUSDT', 'GBPUSDT', 'JPYUSDT', 'USDUSDT', 'DOWN', 'UP']
            for coin in info['symbols']:
                if coin['symbol'].endswith('USDT') and all(item not in coin['symbol'] for item in FIATS):
                    if coin['status'] == 'TRADING':
                        coin_list.append(coin['symbol'])

            return coin_list

        def get_change(symbol):
            price = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, "5 minutes ago")
            first = float(price[0][2])
            second = float(price[4][2])
            change = ((second - first) / first)*100
            if change>0:
                trading_volume = float(price[4][5]) + float(price[3][5]) + float(price[2][5]) + float(price[1][5]) + float(price[0][5])
                return trading_volume
            else:
                return None


        def create_second_list(coin_list):
            # among the coin_list, pick coins that is higher than 45 minutes ago
            coin_list_middle = {}
            for coin in coin_list:
                tv = get_change(coin)
                if tv is None:
                    pass
                else:
                    coin_list_middle[coin] = tv


            return sorted(coin_list_middle.items(), key=lambda x: x[1], reverse=True)



        def pick_coin():
            # pick randome one from coin_list2
            print(f"coin list is {coin_list}")
            coin_list2 = create_second_list(coin_list)
            print(f"coin list2 is {coin_list2}")


            #create hashmap, key as coin and vlaue as trading volume

            if len(coin_list2) == 0:
                return None
            else:
                for key in coin_list2:
                    print(f"Picked coin is {key}")
                    return key[0]




        if firstTime:
            sell_all()

        coin_list = create_first_list()
        while True:
            if len(portfolio) == 0:
                # buy coin
                print("--------------------")
                print("[BUY]")
                coin = pick_coin()
                if coin is None:
                    continue
                buy(coin)
                update_json_file(calendar.timegm(time.gmtime()), get_account_value())
                print(f"{coin} bought >>> portfolio: {portfolio}")
                print("--------------------")
            else:
                # check time, take profit, stop loss
                print("--------------------")

                time_passed = calendar.timegm(time.gmtime()) - portfolio[coin]['time']/1000

                if time_passed >= 60 * max_minutes:
                    print(f"[TIME LIMIT PASSED] {math.floor(time_passed)} seconds")
                    sell(coin)
                    print(f"{coin} sold >>> portfolio: {portfolio}")
                    update_json_file(calendar.timegm(time.gmtime()),get_account_value())
                    print("--------------------")

                else:
                    print(f"[IN TIME] {math.floor(time_passed)} seconds")
                    coinInfo = client.get_symbol_ticker(symbol=coin)
                    currentPrice = coinInfo['price']
                    boughtPrice = portfolio[coin]['avg']
                    percentage = ((float(currentPrice) - float(boughtPrice)) / float(boughtPrice)) * 100
                    print(f"percentage is {percentage}")

                    if percentage >= take_proft or percentage <= stop_loss:
                        print("[SELL]")
                        if percentage > 0:
                            print(f"profits: {percentage}")
                        else:
                            print(f"loss: {percentage}")

                        sell(coin)
                        print(f"{coin} sold >>> portfolio: {portfolio}")
                        update_json_file(calendar.timegm(time.gmtime()), get_account_value())
                    else:
                        print("[DO NOTHING]")
                        pass

                    print("--------------------")

            time.sleep(5)





bot = Solution()
bot.tradeBot(testMode=False, USD=11, holdings=1, firstTime=False, max_min=5, take_proft=0.1, stop_loss=-1)
