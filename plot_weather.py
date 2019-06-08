import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('data.json', 'r') as json_file:
    x_data = json.load(json_file)

regions = x_data['regions']

for one in regions:

    regions_name = one['name']
    weather_data = one['data']

    temp = []
    press = []

    for record in weather_data:
        temp.append(int(record['temperature']))
        press.append(int(record['pressure']))

    df = pd.DataFrame({'temperature': temp, 'pressure': press})
    temp_standDev = round((np.std(temp)), 2)
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
    plt.savefig('results/{}.pdf'.format(regions_name))
    plt.clf()
