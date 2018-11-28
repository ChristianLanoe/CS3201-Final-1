import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from itertools import compress

data = {}


def csvToDict():
    filenames = []
    for root, dirs, files in os.walk("1runCSV"):
        filenames = [f for f in files if not f[0] == "."]

    for file in filenames:
        file = os.path.join(os.path.join(os.curdir, "1runCSV"), file)
        data[file] = {}
        data[file]["Best Fitness"] = []
        data[file]["Average Fitness"] = []
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data[file]["Best Fitness"].append(float(row["Best Fitness"]))
                data[file]["Average Fitness"].append(float(row["Average Fitness"]))


def plotFitness():
    for i in range(len(data.keys())):
        key = list(data)[i]
        colors = ["r", "g", "b"]
        title = key[14:len(key) - 4]
        bestFitness = data[key]["Best Fitness"]
        averageFitness = data[key]["Average Fitness"]
        x = list(range(1, len(y) + 1))

        # avg = sum(y) / len(y)
        # standardDev = np.std(y)
        # avg_a = np.array([avg for i in range(len(y))])
        # optimal = np.array([27601 for i in range(len(y))])

        plt.plot(x, y, colors[i], label=key)
        # plt.bar(x,y, label="Fitness")
        # plt.plot(x, avg_a, "r", label="Mean Fitness")
        # plt.plot(x, optimal, "g", label="Optimal Fitness")

        # plt.axhline(y=avg - standardDev, color="g", label="1 SD", linestyle="--")
        # plt.axhline(y=avg + standardDev, color="g", linestyle="--")

        plt.legend(loc="upper right")
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        # plt.axis([0, 21, 26.75, 28.25])
        plt.yticks(np.arange(min(y)-100, max(y) + 100, 2000))
        plt.xticks(np.arange(0, max(x) + 1, 50))
        plt.title(title)
    plt.show()


def makeTable():
    plt.figure(figsize=(10, 5))
    ax = plt.subplot()
    ax.axis('off')
    columns = ["SR", "AES"]
    rows = []
    cell_text = []
    for key in data.keys():
        rows.append(key[6:len(key) - 4])

        cell_text.append([])
        successRate = sum(data[key]["Successful Run"]) / len(data[key]["Successful Run"])
        numer = sum(list(compress(data[key]["Evaluations to Solution"], data[key]["Successful Run"])))
        denom = len(list(compress(data[key]["Evaluations to Solution"], data[key]["Successful Run"])))
        aes = numer / denom

        cell_text[len(cell_text) - 1].append(successRate)
        cell_text[len(cell_text) - 1].append(aes)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns,
             colWidths=[0.5 / 2.54, 0.5 / 2.54], cellLoc="center", loc="center right")
    plt.show()


def main():
    csvToDict()
    plotFitness()
    # makeTable()


if __name__ == '__main__':
    main()