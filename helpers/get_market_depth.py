def get_depth(symbol, client):
    depth = client.get_order_book(symbol=symbol)
    return depth
