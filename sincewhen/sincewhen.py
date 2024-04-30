import json
from datetime import date

json_file = "sincewhen.json"

with open(json_file) as json_data:
    data = json.load(json_data)

for k in data:
    days = (date.today() - date.fromisoformat(data[k])).days
    if (days > 0):
        print(f'{days} days since {k}')
    elif (days < 0):
        print(f'{abs(days)} days until {k}')
    else:
        print(f'{k} IS TODAY')

