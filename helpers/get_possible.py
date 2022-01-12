def get_price():
    '''Return the current price(in USDT) for all coins on binance'''
    initial_price = {}
    prices = client.get_all_tickers()
    possible_set = set()
    for coin in prices:

        # only Return USDT pairs and exclude margin symbols like BTCDOWNUSDT
        if PAIR_WITH in coin['symbol'] and all(item not in coin['symbol'] for item in FIATS):
            possible_set.add(coin['symbol'])


    return possible_set
