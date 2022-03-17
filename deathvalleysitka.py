import csv
from datetime import datetime
import matplotlib.pyplot as plt

temps = ["sitka_weather_2018_simple.csv","death_valley_2018_simple.csv"]

name1 = []
caption = "Temperature comparison between"
fig, ax = plt.subplots(2)

for t in range(len(temps)):
    highs = []
    lows = []
    dates = []
    indexes = {}

    temperature = open(temps[t], 'r')
    temp_file = csv.reader(temperature, delimiter=",")
    header_row = next(temp_file)

    for index, column_header in enumerate(header_row):
        indexes[column_header] = index
    
    for row in temp_file:
        try:
            high = int(row[indexes["TMAX"]])
            low = int(row[indexes["TMIN"]])
            current_date = datetime.strptime(row[indexes["DATE"]], "%Y-%m-%d")
            name2 = row[indexes["NAME"]]
            if name2 not in name1:
                name1.append(name2)
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(int(row[indexes["TMAX"]]))
            lows.append(int(row[indexes["TMIN"]]))
            dates.append(current_date)

    temperature.close

    ax[t].plot(dates, highs, c = 'red')
    ax[t].plot(dates,lows, c = 'blue')
    ax[t].fill_between(dates,highs,lows, facecolor='blue',alpha=0.25)
    ax[t].set_title(name2)

    if t > 0:
        caption += " " + "and" + " " + name1[t]
    else:
        caption += " " + name1[t]


fig.autofmt_xdate()
fig.suptitle(caption) 
plt.show()


'''
THIS CODE PLOTTED THE CHARTS THEM TOGETHER DO NOT GRADE 
#opening death valley file and reading it 
dv = open("death_valley_2018_simple.csv", "r")
dv_file = csv.reader(dv, delimiter=",")
header_row = next(dv_file)

for index, column_header in enumerate(header_row):
    print(index, column_header)


# the following code provides a list with all the high temperatures
dvhighs = []
dvlows = []
dates = []

for row in dv_file:
    try:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dvhighs.append(int(row[4]))
        dvlows.append(int(row[5]))
        dates.append(current_date)

dv.close()
#reading sitka file, doing the same as above 
sitka = open("sitka_weather_2018_simple.csv", "r")
s_file = csv.reader(sitka, delimiter=',')
header_row1 = next(s_file)

for index, column_header in enumerate(header_row1):
    print(index, column_header)

sitlows = []
sithighs = []
for row in s_file:
        sithighs.append(int(row[5]))
        sitlows.append(int(row[6]))

sitka.close()

fig, ax = plt.subplots(1)
ax.plot(dates, sithighs,c='red')
ax.plot(dates,sitlows, c = 'blue')
plt.fill_between(dates, sithighs, sitlows, facecolor="blue", alpha=0.2)
ax.plot(dates,dvhighs,c='red')
ax.plot(dates,dvlows,c='blue')
plt.fill_between(dates, dvhighs, dvlows, facecolor="blue", alpha=0.2)
plt.show()

'''