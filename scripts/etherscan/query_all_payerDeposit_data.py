import pandas as pd
import requests
import json

payerDepositJson = '/Users/andrewgoldberg/Projects/llamapay-analytics/data/eventscanner/llamapay_events/llamapay_payerDeposit.json'
with open(payerDepositJson) as f:
    payerDeposit = json.loads(f.read)
payerDeposit_df = pd.read_csv(payerDeposit['results'])
print(payerDeposit_df)

# ABI_json = '/Users/andrewgoldberg/Projects/llamapay-analytics/ABI/llamapay_ABI.json'
# # ABI = open(ABI_json)
# with open(ABI_json) as f:
#     abi = json.loads(f.read())