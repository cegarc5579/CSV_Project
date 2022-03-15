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
dates1 = []

# use this structure!!
for row in weather_file:

    try:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])

    except ValueError:
        # this is a new way to print something else
        # putting an f in the beginning allows you to put curly brackets and anything else
        print(f"Missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)


print(highs)
print(dates)
