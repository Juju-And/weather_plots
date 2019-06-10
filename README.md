# Weather plots

This is a simple Python application intended to generate pseudo-random weather data (temperature and pressure) for 5 regions and create plots for each region separately. Each region has calculated it's own standard deviation for temperature and pressure.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install all required modules running pip with the provided file:

```
pip install requirements.txt
```

### Installing

First step is to run the first file in order to generate pseudo-random weather data:

```
$ python3 generate_weather.py 
```

in order to have .pdf files created, run the second file;

```
$ python3 plot_weather.py
```

Ready plots in .pdf format can be found in the results folder.