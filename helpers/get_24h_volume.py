def get_24h_volume2(symbol):
    volume = 0
    info = client.get_exchange_info()
    for coin in info['symbols']:
        if coin['baseAsset'] == symbol:
            print(coin['baseAsset'])
            try:
                symbol_pair = coin['symbol']

                klines = client.get_historical_klines(symbol_pair,
                                                      Client.KLINE_INTERVAL_1MINUTE,
                                                      "1 day ago")
                for history in klines:
                    volume += float(history[5])

            except:
                pass

    formatted = '{:,.2f}'.format(float(volume))
    return formatted
