import requests
import json

def calc_eth(value, info):
    
    return(info)

url = 'https://github.com/joemulberry/curio/raw/main/orders.json'
resp = requests.get(url)
orders = json.loads(resp.text)

# print(orders[0])

for order in orders:
    
    d = {
        'token_id': order['asset']['token_id'],
        'name': order['asset']['name'],
        'side': order['side'],
        'eth': calc_eth(order['base_price'], order['payment_token_contract'])

        
    }
    
    if d['token_id'] != '20':
        print(d)
        # print(orders[0].keys())
