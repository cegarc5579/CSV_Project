import csv

weather = open("sitka_weather_07-2018_simple.csv", "r")

weather_file = csv.reader(weather, delimiter=",")

header_row = next(weather_file)

print(type(header_row))

# enumerate can be used on any type of list object
# allow you to get more information
# this shows you the index location, and the value in the location
# so this shows you which index belongs to which label basically
for index, column_header in enumerate(header_row):
    print(index, column_header)
# the following code provides a list with all the high temperatures
highs = []
for row in weather_file:
    highs.append(int(row[5]))

print(highs)

# the following code makes a graph of the list of highs
# and makes the line red color
import matplotlib.pyplot as plt

plt.plot(highs, c="red")
# this adds a title to the graphs, also increases font size
# the following code are formatting we have done to the graph
plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
# to actually show the graph
plt.show()
