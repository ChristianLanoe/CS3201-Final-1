"""
The script plots multiple runs on the same plot
"""
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import sys

data = {}


def csvToDict():
    filenames = []
    for root, dirs, files in os.walk("RunsAverage"):
        filenames = [f for f in files if not f[0] == "."]

    for file in filenames:
        file = os.path.join(os.path.join(os.curdir, "RunsAverage"), file)
        data[file] = {}
        data[file]["Best Fitness"] = []
        data[file]["Average Fitness"] = []
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data[file]["Best Fitness"].append(float(row["Best Fitness"]))
                data[file]["Average Fitness"].append(float(row["Average Fitness"]))


# This function handles the actual plotting of the data
# The 2nd argument in plt.xticks and the 3rd arument in plt.yticks need to be changed
# to fit your needs
def plotFitness():
    min_y = sys.maxsize
    max_y = 0
    for i in range(len(data.keys())):
        key = list(data.keys())[i]
        y = data[key]["Best Fitness"]
        # z = data[key]["Average Fitness"]
        x = list(range(1, len(y) + 1))
        optimal = np.array([27601 for i in range(len(y))])
        colors = ["b", "g", "r", "c", "m", "b--", "g--", "r--", "c--", "m--"]

        if(min(y) < min_y):
            min_y = min(y)
        if(max(y) > max_y):
            max_y = max(y)
        # plt.plot(x, z, colors[i + 1], label="Average Fitness")
        plt.plot(x, y, colors[i], label=key[14:(len(key) - 4)])
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.xticks(np.arange(0, max(x) + 1, 5000))
    plt.yticks(np.arange(min_y, max_y, 10000000))
    plt.plot(x, optimal, "k", label="Optimal Fitness")
    plt.legend(loc="upper right")
    plt.show()


def main():
    csvToDict()
    plotFitness()


if __name__ == '__main__':
    main()
