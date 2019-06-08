import json
import random

REGIONS_NUM = 5
data = {}

data['regions'] = []

for i in range(REGIONS_NUM):
    region = {}
    region['name'] = 'Region' + str(i + 1)
    region['data'] = []

    for j in range(30):
        region['data'].append({
            'temperature': random.randint(1, 101),
            'pressure': random.randint(1, 101)
        })
    data['regions'].append(region)

    json_data = json.dumps(data)

with open('data.json', 'w') as exp_data:
    json.dump(data, exp_data)
