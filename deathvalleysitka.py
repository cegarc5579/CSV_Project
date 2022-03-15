import csv
from datetime import datetime
import matplotlib.pyplot as plt


# death valley temps
weather = open("death_valley_2018_simple.csv", "r")
weather_file = csv.reader(weather, delimiter=",")
header_row = next(weather_file)


for index, column_header in enumerate(header_row):
    print(index, column_header)
highs = []
lows = []
dates = []

# sitka temps
weather2 = open("sitka_weather_2018_simple.csv", "r")
weather_file2 = csv.reader(weather2, delimiter=",")
header_row2 = next(weather_file2)

for index, column_header in enumerate(header_row2):
    print(index, column_header)
highs1 = []
lows1 = []
dates = []
