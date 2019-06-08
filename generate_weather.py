import json
import random


# 5 regionów x 30 dni
# Mamy sobię listę regionow gdzie każdy region będzie słownikiem zawierający 2 klucze: 'name' oraz data.
# for x in range(30):
#     print(random.randint(1, 101))

# {
# 			'name': 'Region1',
# 			'data': [
# 				{
# 					'temperature': 100,
# 					'pressure': 100
# 				},

data = {}

data['regions'] = []

for i in range(5):

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

    # print(data)

# data.to_json('modified.json', index=False)

with open('data.json', 'w') as exp_data:
    json.dump(data, exp_data)








