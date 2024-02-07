import requests
import json
import pandas as pd

etherscan_api_key = 'RQCKJ2RUXUBASPGW1W4MM4HW7VDF9VKURJ'
llamapay_factory_address = '0xde1C04855c2828431ba637675B6929A684f84C7F'

etherscan_eventlogs = f'https://api.etherscan.io/api?module=logs&action=getLogs&address={llamapay_factory_address}&apikey={etherscan_api_key}'

request_factory_eventlogs = requests.get(etherscan_eventlogs)

factory_eventlogs = request_factory_eventlogs.json()
with open(f'../../data/etherscan/factory_eventlogs.json', 'w') as fp:
        json.dump(factory_eventlogs, fp)

df = pd.DataFrame(factory_eventlogs['result'])
df.to_csv('../../data/etherscan/factory_eventlogs.csv', index=False)


