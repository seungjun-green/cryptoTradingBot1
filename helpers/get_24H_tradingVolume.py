def get_24h_volume(symbol):
    # get trading volumes for the last 24 hours
    trading_volume = 0
    prices = client.get_all_tickers()
    for coin in prices:
        if coin['symbol'].startswith(symbol) and coin['symbol'].startswith('BTCDOWN') == False and coin['symbol'].startswith('BTCUP') == False and coin['symbol'].startswith('BTCST') == False:
            try:
                klines = client.get_historical_klines(coin['symbol'], Client.KLINE_INTERVAL_1MINUTE, "1 day ago")

                for history in klines:
                    trading_volume += float(history[5])

                print(coin['symbol'], trading_volume)
            except:
                pass
