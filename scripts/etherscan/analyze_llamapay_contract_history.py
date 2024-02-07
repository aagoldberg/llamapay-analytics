import pandas as pd

llamapay_contract_address = '0x6c87ecf80e7ed91720a85d5bb391ed5777ad2fd0'
history_df = pd.read_csv(f'../../data/etherscan/llamapay_eventlogs_csv/0x{llamapay_contract_address}.csv', index=False)