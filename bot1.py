import calendar
from binance.client import Client
import time
import json
import math



class Solution:
    def tradeBot(self, testMode, qnt, holdings, firstTime):
        TESTNET = testMode
        max_minutes = 1
        QUANTITY = qnt
        portfolio = {}
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


        # pick coin to buy
        def pick_coin():
            print("...ETHUSDT picked...")
            return 'ETHUSDT'

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
            coin_bought['qnt'] = hash['origQty']

            # update portfolio
            portfolio[symbol] = coin_bought

        # convert volume
        # ex.) 10USDT -> 0.0063 ETH
        # We round up when formatting qnt to fit the lot size
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
                pass

            volume[coin] = float(QUANTITY / float(currentPirce(coin)))

            if coin not in lot_size:
                volume[coin] = float('{:.1f}'.format(volume[coin]))

            else:
                volume[coin] = float('{:.{}f}'.format(volume[coin], lot_size[coin]))

            return volume[coin]

        # func to get current price of certain coin
        def currentPirce(coin):
            coinInfo = client.get_symbol_ticker(symbol=coin)
            return coinInfo['price']

        # func to buy coins
        def buy(coin):
            try:
                print("buying coin")
                buy_market = client.create_order(symbol='ETHUSDT', side='BUY', type='MARKET', quantity=convertVolume(coin))
                # update portfolio
                update_portfolio_add(buy_market) # add new holding
            except Exception as e:
                print(e)

        # func to sell coins
        def sell(coin):
            try:
                print(coin)
                print("selling coin")
                sell_market = client.create_order(symbol='ETHUSDT', side='SELL', type='MARKET', quantity=portfolio[coin]['qnt'])
                del portfolio[coin]
                print(coin, portfolio)
            except Exception as e:
                print(e)

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

        if firstTime:
            sell_all()

        while True:
            if len(portfolio) == 0:
                # buy coin
                print("--------------------")
                print("[BUY]")
                coin = pick_coin()
                buy(coin)
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

                    if percentage >= 1.5 or percentage <= -1.5:
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




#
# bot = Solution()
# bot.tradeBot(testMode=True, qnt=13, holdings=1, firstTime=False)
#
#
api_key = 'f1KzRyDIciGXKW88Z8UvZ55CeefAG5svrMFdUlnjMSHK49MaQAgm343Q1IZvQqgl'
api_secret = 'fwUAvrW3fbgMX6jlec94W0EcWFWBzrNAWK60QtYAeO7xbGq35vEU0T8bBtW9W5qj'
client = Client(api_key, api_secret)
# my_account = client.get_account()
# possible_set = {'MCOUSDT', 'TORNUSDT', 'GTCUSDT', 'BTGUSDT', 'USDTTRY', 'EGLDUSDT', 'MLNUSDT', 'EOSBEARUSDT',
#                 'XRPBULLUSDT', 'QTUMUSDT', 'PEOPLEUSDT', 'RGTUSDT', 'DREPUSDT', 'BTTUSDT', 'BURGERUSDT', 'GALAUSDT',
#                 'DOGEUSDT', 'CTXCUSDT', 'NUUSDT', 'AMPUSDT', 'STXUSDT', 'BATUSDT', 'DEGOUSDT', 'BZRXUSDT', 'RAYUSDT',
#                 'NKNUSDT', 'DEXEUSDT', 'XZCUSDT', 'HIVEUSDT', 'ONGUSDT', 'AXSUSDT', 'KAVAUSDT', 'KEEPUSDT', 'WAXPUSDT',
#                 'IMXUSDT', 'TOMOUSDT', 'KEYUSDT', 'HOTUSDT', 'LSKUSDT', 'BNBBEARUSDT', 'SOLUSDT', 'FARMUSDT',
#                 'IDEXUSDT', 'CTSIUSDT', 'USDTBRL', 'SUNUSDT', 'AUDIOUSDT', 'COMPUSDT', 'TRUUSDT', 'ENJUSDT',
#                 'SANTOSUSDT', 'BCHSVUSDT', 'ANTUSDT', 'BAKEUSDT', 'BTCUSDT', 'PONDUSDT', 'LINAUSDT', 'RLCUSDT',
#                 'FUNUSDT', 'FORUSDT', 'MBOXUSDT', 'FETUSDT', 'ACMUSDT', 'SYSUSDT', 'USDPUSDT', 'BETAUSDT',
#                 'XRPBEARUSDT', 'MKRUSDT', 'WINGUSDT', 'REEFUSDT', 'YFIIUSDT', 'STRAXUSDT', 'DATAUSDT', 'AVAUSDT',
#                 'LUNAUSDT', 'AVAXUSDT', 'CLVUSDT', 'IOTAUSDT', 'DCRUSDT', 'CITYUSDT', 'INJUSDT', 'PSGUSDT', 'XMRUSDT',
#                 'BEARUSDT', 'NULSUSDT', 'PERPUSDT', 'RIFUSDT', 'AGLDUSDT', 'BCHUSDT', 'PNTUSDT', 'ONEUSDT', 'FIROUSDT',
#                 'BARUSDT', 'GHSTUSDT', 'HARDUSDT', 'FILUSDT', 'VIDTUSDT', 'LENDUSDT', 'AAVEUSDT', 'ALPACAUSDT',
#                 'NANOUSDT', 'ARPAUSDT', 'CFXUSDT', 'NBSUSDT', 'HBARUSDT', 'CHRUSDT', 'VTHOUSDT', 'DIAUSDT', 'SKLUSDT',
#                 'EOSUSDT', 'BADGERUSDT', 'FORTHUSDT', 'CELOUSDT', 'CHZUSDT', 'USDTBIDR', 'CVPUSDT', 'USDSUSDT',
#                 'DAIUSDT', 'BTCSTUSDT', 'WANUSDT', 'OCEANUSDT', 'USDTBKRW', 'MDTUSDT', 'ENSUSDT', 'LRCUSDT', 'WRXUSDT',
#                 'MINAUSDT', 'ZILUSDT', 'RUNEUSDT', 'GXSUSDT', 'LINKUSDT', 'ANKRUSDT', 'RSRUSDT', 'FTTUSDT', 'RNDRUSDT',
#                 'BELUSDT', 'UMAUSDT', 'FIDAUSDT', 'RAMPUSDT', 'PYRUSDT', 'TVKUSDT', 'PAXUSDT', 'TROYUSDT', 'FIOUSDT',
#                 'TRXUSDT', 'BALUSDT', 'XVGUSDT', '1INCHUSDT', 'POWRUSDT', 'THETAUSDT', 'USDTUAH', 'COTIUSDT', 'DGBUSDT',
#                 'BTSUSDT', 'KMDUSDT', 'ETCUSDT', 'TRIBEUSDT', 'QIUSDT', 'ROSEUSDT', 'PUNDIXUSDT', 'OMGUSDT', 'ILVUSDT',
#                 'STORMUSDT', 'HNTUSDT', 'GRTUSDT', 'USDTGYEN', 'AIONUSDT', 'JASMYUSDT', 'BANDUSDT', 'RADUSDT',
#                 'PAXGUSDT', 'ERDUSDT', 'MANAUSDT', 'LTOUSDT', 'LTCUSDT', 'SPELLUSDT', 'XRPUSDT', 'NMRUSDT', 'STORJUSDT',
#                 'ALGOUSDT', 'WAVESUSDT', 'ATAUSDT', 'CHESSUSDT', 'BCCUSDT', 'FRONTUSDT', 'RVNUSDT', 'OGNUSDT',
#                 'BNTUSDT', 'KSMUSDT', 'FLMUSDT', 'ANYUSDT', 'POLYUSDT', 'DNTUSDT', 'ALCXUSDT', 'ONTUSDT', 'BEAMUSDT',
#                 'USDTBVND', 'MITHUSDT', 'DOTUSDT', 'GNOUSDT', 'ORNUSDT', 'TFUELUSDT', 'ELFUSDT', 'SUSHIUSDT', 'CVXUSDT',
#                 'LAZIOUSDT', 'REQUSDT', 'MASKUSDT', 'HIGHUSDT', 'JSTUSDT', 'JOEUSDT', 'ICXUSDT', 'USDTRUB', 'ADXUSDT',
#                 'USDTNGN', 'BNXUSDT', 'MDXUSDT', 'PORTOUSDT', 'XLMUSDT', 'FLUXUSDT', 'XVSUSDT', 'ARDRUSDT', 'AUDUSDT',
#                 'YFIUSDT', 'HCUSDT', 'TCTUSDT', 'MTLUSDT', 'USDCUSDT', 'USDTIDRT', 'CELRUSDT', 'IRISUSDT', 'VETUSDT',
#                 'ADAUSDT', 'AKROUSDT', 'MBLUSDT', 'STPTUSDT', 'BUSDTRY', 'USDSBUSDT', 'OXTUSDT', 'SNXUSDT', 'KLAYUSDT',
#                 'USDTZAR', 'ATOMUSDT', 'QUICKUSDT', 'SHIBUSDT', 'ETHUSDT', 'PERLUSDT', 'CAKEUSDT', 'TLMUSDT',
#                 'VOXELUSDT', 'USDTDAI', 'DARUSDT', 'NEARUSDT', 'USTUSDT', 'AUTOUSDT', 'JUVUSDT', 'FXSUSDT', 'GTOUSDT',
#                 'RENUSDT', 'XEMUSDT', 'BLZUSDT', 'COCOSUSDT', 'DOCKUSDT', 'ZENUSDT', 'ACHUSDT', 'ASRUSDT', 'FISUSDT',
#                 'ICPUSDT', 'GLMRUSDT', 'WINUSDT', 'OOKIUSDT', 'CRVUSDT', 'BCHABCUSDT', 'KNCUSDT', 'MCUSDT', 'PHAUSDT',
#                 'BONDUSDT', 'DYDXUSDT', 'MATICUSDT', 'WTCUSDT', 'DASHUSDT', 'NEOUSDT', 'DENTUSDT', 'UNIUSDT',
#                 'FLOWUSDT', 'RAREUSDT', 'ZRXUSDT', 'DUSKUSDT', 'YGGUSDT', 'SFPUSDT', 'TKOUSDT', 'VENUSDT', 'IOTXUSDT',
#                 'BNBUSDT', 'ERNUSDT', 'KP3RUSDT', 'ZECUSDT', 'COSUSDT', 'ALICEUSDT', 'ETHBULLUSDT', 'MIRUSDT',
#                 'EOSBULLUSDT', 'REPUSDT', 'STRATUSDT', 'FTMUSDT', 'BULLUSDT', 'BNBBULLUSDT', 'ETHBEARUSDT', 'C98USDT',
#                 'SCUSDT', 'SANDUSDT', 'UTKUSDT', 'LPTUSDT', 'POLSUSDT', 'CKBUSDT', 'TWTUSDT', 'VGXUSDT', 'VITEUSDT',
#                 'OGUSDT', 'PLAUSDT', 'WNXMUSDT', 'UNFIUSDT', 'CTKUSDT', 'BICOUSDT', 'TRBUSDT', 'MOVRUSDT', 'SLPUSDT',
#                 'AUCTIONUSDT', 'SXPUSDT', 'ALPHAUSDT', 'ARUSDT', 'NPXSUSDT', 'MFTUSDT', 'CVCUSDT', 'SRMUSDT', 'XECUSDT',
#                 'XTZUSDT', 'ATMUSDT', 'DODOUSDT', 'IOSTUSDT', 'OMUSDT', 'EPSUSDT', 'DFUSDT', 'QNTUSDT', 'STMXUSDT',
#                 'LITUSDT', 'BKRWUSDT'}
# lot_size = {}
# volume = {}
# for hashmap in my_account['balances']:
#     coinName = hashmap['asset']
#     coin = coinName + 'USDT'
#     try:
#         info = client.get_symbol_info(coin)
#         step_size = info['filters'][2]['stepSize']
#         lot_size[coin] = step_size.index('1') - 1
#
#         if lot_size[coin] < 0:
#             lot_size[coin] = 0
#
#     except:
#         pass
#
#
#
#     if coin not in lot_size:
#         print(coin)
#
#     else:
#         print("--")
#
#     time.sleep(2)




def get_24h_volume(symbol):
    # get trading volumes for the last 24 hours
    trading_volume = 0
    prices = client.get_all_tickers()
    for coin in prices:
        if coin['symbol'].endswith(symbol):
            try:
                klines = client.get_historical_klines(coin['symbol'],
                                                        Client.KLINE_INTERVAL_1MINUTE,
                                                        "1 day ago")
                for history in klines:
                    trading_volume += float(history[7])

            except:
                pass



    return trading_volume



# result = get_24h_volume('ETH')
# print("{:,}".format(result))
# trade = 0
# klines = client.get_historical_klines('ETHUSDT',
#                                         Client.KLINE_INTERVAL_1MINUTE,
#                                         "1 day ago")
#
#
#
# volume = 0
#
# for history in klines:
#     volume+=float(history[5])
#
# print('{:,.2f}'.format(float(volume)))


volume = 0



prices = client.get_all_tickers()
for coin in prices:
    if coin['symbol'].endswith('DOGE'):
        try:
            print(coin['symbol'])
            klines = client.get_historical_klines(coin['symbol'],
                                                  Client.KLINE_INTERVAL_1MINUTE,
                                                  "1 day ago")
            for history in klines:
                volume += float(history[7])

        except:
            pass

print('{:,.2f}'.format(float(volume)))



