import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# x_data = {}

with open('data.json', 'r') as json_file:
    x_data = json.load(json_file)

# print(data)

one_region = x_data['regions']

# print(one_region)
for one in one_region:

    regions_name = one['name']
    # # print(one_region)
    # # print(one_region.__class__)
    # # print(one_region.keys())
    weather_data = one['data']
    # # print(weather_data.__class__)
    # # print(weather_data[1])
    temp = []
    press = []
    #
    for record in weather_data:
        # print(record)
        temp.append(int(record['temperature']))
        press.append(int(record['pressure']))
    # print(temp, press)
    df = pd.DataFrame({'temperature': temp, 'pressure': press})
    temp_standDev = round((np.std(temp)), 2)
    # print(temp_standDev)
    press_standDev = round((np.std(press)), 2)

    plt.plot(temp, label='temperatura ({})'.format(temp_standDev))
    plt.plot(press, label='ciśnienie ({})'.format(press_standDev))
    plt.xlabel('Dzień')
    plt.ylabel('Wysokość')
    plt.gca().legend(fontsize='6', fancybox=True, shadow=False, title='LEGENDA')
    plt.grid(True)
    plt.title(regions_name)
    plt.tight_layout()
    plt.show()
    plt.savefig(regions_name + '.pdf')
    plt.clf()

