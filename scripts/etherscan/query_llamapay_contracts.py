import requests
import json
import pandas as pd

factory_eventlogs = pd.read_csv('../../data/etherscan/factory_eventlogs.csv')
df_llamapay_tokens = factory_eventlogs['data'].apply(lambda x: (x[26:66]))
df_llamapay_contracts = factory_eventlogs['data'].apply(lambda x: (x[66+24:]))


etherscan_api_key = 'RQCKJ2RUXUBASPGW1W4MM4HW7VDF9VKURJ'
for llamapay_contract_address in df_llamapay_contracts:
    etherscan_eventlogs = f'https://api.etherscan.io/api?module=logs&action=getLogs&address=0x{llamapay_contract_address}&apikey={etherscan_api_key}'
    request_llamapay_eventlogs = requests.get(etherscan_eventlogs)
    llamapay_eventlogs = request_llamapay_eventlogs.json()

    with open(f'../../data/etherscan/llamapay_eventlogs_json/0x{llamapay_contract_address}.json', 'w') as fp:
        json.dump(llamapay_eventlogs, fp)
    
    try:
        df = pd.DataFrame(llamapay_eventlogs['result'])
        df.to_csv(f'../../data/etherscan/llamapay_eventlogs_csv/0x{llamapay_contract_address}.csv', index=False)
    except:
        continue
