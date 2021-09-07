import requests
import json

call_offsets = ['0', '50', '100', '150', '200']
dicts = []

for call_offset in call_offsets:

    url = "https://api.opensea.io/wyvern/v1/orders"
    querystring = {"asset_contract_address": "0x73da73ef3a6982109c4d5bdb0db9dd3e3783f313", "bundled": "false", "include_bundled": "false",
                   "include_invalid": "false", "limit": "50", "offset": call_offset, "order_by": "created_date", "order_direction": "desc"}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    orders = json.loads(response.text)['orders']
    dicts += orders

with open('orders.json', 'w') as fout:
    json.dump(dicts, fout)
