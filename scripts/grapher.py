# Graphing utility for csv files
# Chris "Scary" Scaramella

import matplotlib.pyplot as plt # for graphing
import csv # for reading files
import sys

if __name__ == "__main__":
    dates = []
    values = []
    input_file = "../results/mass_effect_andromeda.csv"
    with open(input_file, 'rb') as file:
        data = csv.reader(file, delimiter=',')
        line = 0
        for row in data:
            if line == 0:
                line = 0
            else:
            	dates.append(row[0])
            	values.append(float(row[1]))
            line += 1

    plt.plot(range(len(values)),values)
    plt.xticks(range(len(values)),dates, rotation=30)
    plt.axis([0, len(values),0, 10])
    plt.xlabel("Date")
    plt.ylabel("Average Sentiment Value")
    plt.title("Mass Effect Andromeda")
    plt.show()
