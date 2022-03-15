import csv
from datetime import datetime

# death valley temps
weather = open("death_valley_2018_simple.csv", "r")
weather_file = csv.reader(weather, delimiter=",")
header_row = next(weather_file)

# sitka temps
weather2 = open("sitka_weather_2018_simple.csv", "r")
weather_file2 = csv.reader(weather2, delimiter=",")
header_row2 = next(weather_file2)
