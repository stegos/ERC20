
import os, math
from pprint import pprint
from airtable import Airtable

base_key = 'app1057waXTA8WK3N'
table_name = 'Balances'
airtable = Airtable(base_key, table_name, api_key=os.environ['AIRTABLE_API_KEY'])
supply = 0
balances = {}

for page in airtable.get_iter(sort='ID'):
    for record in page:
        if 'STG Balance' in record['fields']:
            id = record['fields']['ID']
            address = record['fields']['ETH Wallet Address']
            balance = math.trunc(record['fields']['STG Balance'] * 1_000_000)
            supply += balance
            if address in balances:
                balances[address] += balance
            else:
                balances[address] = balance

print(f'log Transfer(ZERO_ADDRESS, msg.sender, {1_000_000_000_000_000 - supply})')

for k, v in balances.items():
    if v > 0:
        print(f'log Transfer(msg.sender, {k}, {v})')
