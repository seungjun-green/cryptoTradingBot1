def get_all_coins():
    coins = set()
    for i in info['symbols']:
        coins.add(i['baseAsset'])
    return coins
