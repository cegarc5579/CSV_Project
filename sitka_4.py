# 1) changing the file to include all the data for the year of 2018
# 2) change the title to - Daily low and high temperatures - 2018
# 3) extract low temps from the file and add to chart
# 4) shade in the area between high and low

import csv
from datetime import datetime

weather = open("death_valley_2018_simple.csv", "r")

weather_file = csv.reader(weather, delimiter=",")

header_row = next(weather_file)

# print(header_row)

# enumerate can be used on any type of list object
# allow you to get more information
# this shows you the index location, and the value in the location
# so this shows you which index belongs to which label basically
for index, column_header in enumerate(header_row):
    print(index, column_header)


# the following code provides a list with all the high temperatures
highs = []
dates = []
lows = []

# test_date = datetime.strptime("2018-07-01", "%Y-%m-%d")
# print(test_date)

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


# the following code makes a graph of the list of highs
# and makes the line red color
import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(dates, highs, c="red")
# have to add the same line but switch with lows in order to plot the low temps
plt.plot(dates, lows, c="blue")
# this adds a title to the graphs, also increases font size
# the following code are formatting we have done to the graph
# alpha changes how transparent it is
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.3)
plt.title("Daily low and high temperatures - 2018", fontsize=16)
plt.xlabel("Month of July 2018")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
# to actually show the graph
# this will autoformat it
fig.autofmt_xdate()
plt.show()
