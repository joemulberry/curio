import requests
import json

def calc_eth(value, info):
    
    return(info)

url = 'https://github.com/joemulberry/curio/raw/main/orders.json'
resp = requests.get(url)
orders = json.loads(resp.text)

# print(orders[0])

orders_data = []

for order in orders:
    token_id = order['asset']['token_id']
    base_price = float(order['base_price'])
    decimals = int(order['payment_token_contract']['decimals'])
    eth_price = float(order['payment_token_contract']['eth_price'])
    currency = order['payment_token_contract']['symbol']
    quantity = int(order['quantity'])
    side = order['side']

    base_price = (base_price / (10 ** decimals)) / quantity
    base_price = base_price * eth_price
    # base_price = float(base_price[:len(base_price)-decimals] + '.' + base_price[len(base_price)-decimals:])
    # base_price = (base_price * eth_price) / quantity
    
    if base_price == 8000000000000000.0:
        print("-"*40)
        print(order)
        print("-"*40)

    if currency != "DAI":
        if side == 0:
            temp = {
                'token_id': token_id, 
                'value': base_price, 
                'type': 'bid',
                'currency': currency,
                'ethprice': eth_price
            }
            orders_data.append(temp)
        else:
            temp = {
                'token_id': token_id,
                'value': base_price,
                'type': 'ask',
                'currency': currency,
                'ethprice': eth_price
            }
            orders_data.append(temp)


print(orders_data)

print(orders[0]['target'])
