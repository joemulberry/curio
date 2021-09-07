import requests
import json

def calc_eth(value, info):
    value = int(value)
    # dedecimaled = value ^^ int(info['decimals'])
    return info

url = "https://api.opensea.io/wyvern/v1/orders"
querystring = {"asset_contract_address": "0x73da73ef3a6982109c4d5bdb0db9dd3e3783f313", "bundled": "false", "include_bundled": "false",
               "include_invalid": "false", "token_id": "20", "limit": "50", "offset": "0", "order_by": "created_date", "order_direction": "desc"}
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)

orders = json.loads(response.text)['orders']

print(orders[0])

for order in orders:
    
    d = {
        'token_id': order['asset']['token_id'],
        'name': order['asset']['name'],
        'side': order['side'],
        'eth': calc_eth(order['base_price'], order['payment_token_contract'])
        
        
    }
    
    print(format(123000000000000, '.6f'))

print(orders[0].keys())
