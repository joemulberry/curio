import requests
import json

token_ids = [str(f) for f in range(1,30)]
dicts = []

for token_id in token_ids:
    url = "https://api.opensea.io/wyvern/v1/orders"
    querystring = {"asset_contract_address": "0x73da73ef3a6982109c4d5bdb0db9dd3e3783f313", "bundled": "false", "include_bundled": "false",
                   "include_invalid": "false", "token_id": token_id, "limit": "50", "offset": "0", "order_by": "created_date", "order_direction": "desc"}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    orders=json.loads(response.text)['orders']
    dicts += orders
    
with open('orders.json', 'w') as fout:
    json.dump(dicts, fout)
