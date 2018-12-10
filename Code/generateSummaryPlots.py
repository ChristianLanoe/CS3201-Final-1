import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from itertools import compress

data = {}


def csvToDict():
    filenames = []
    for root, dirs, files in os.walk("summaryCSV"):
        filenames = [f for f in files if not f[0] == "."]

    for file in filenames:
        file = os.path.join(os.path.join(os.curdir, "summaryCSV"), file)
        data[file] = {}
        data[file]["Best Fitness"] = []
        data[file]["Evaluations to Solution"] = []
        data[file]["Successful Run"] = []
        data[file]["Run Time"] = []
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data[file]["Best Fitness"].append(float(row["Best Fitness"]))
                data[file]["Evaluations to Solution"].append(float(row["Evaluations to Solution"]))
                if(row["Successful Run"] == "True"):
                    data[file]["Successful Run"].append(True)
                elif(row["Successful Run"] == "False"):
                    data[file]["Successful Run"].append(False)
                data[file]["Run Time"].append(float(row["Run Time"]))


def plotFitness():
    for key in data.keys():
        # title = key[13:len(key) - 4]
        y = data[key]["Best Fitness"]
        x = list(range(1, len(y) + 1))

        avg = sum(y) / len(y)
        standardDev = np.std(y)
        avg_a = np.array([avg for i in range(len(y))])
        optimal = np.array([27601 for i in range(len(y))])

        plt.plot(x, y, "b", label="Fitness")
        plt.plot(x, avg_a, "r", label="Mean Fitness")
        plt.plot(x, optimal, "g", label="Optimal Fitness")

        plt.axhline(y=avg - standardDev, color="g", label="1 SD", linestyle="--")
        plt.axhline(y=avg + standardDev, color="g", linestyle="--")

        plt.legend(loc="upper right")
        plt.xlabel("Run Number")
        plt.ylabel("Best Fitness")
        plt.yticks(np.arange(min(y) - 100, max(y) + 100, 1000))
        plt.xticks(np.arange(0, max(x) + 1, 10))
        plt.show()


def makeTable():
    plt.figure(figsize=(10, 5))
    ax = plt.subplot()
    ax.axis('off')
    columns = ["SR", "AES", "ART"]
    rows = []
    cell_text = []
    for key in data.keys():
        rows.append(key[13:len(key) - 4])

        cell_text.append([])
        lenData = len(data[key]["Successful Run"])
        if(lenData == 0):
            successRate = 0
        else:
            successRate = sum(data[key]["Successful Run"]) / lenData
        numer = sum(list(compress(data[key]["Evaluations to Solution"], data[key]["Successful Run"])))
        denom = len(list(compress(data[key]["Evaluations to Solution"], data[key]["Successful Run"])))
        if(denom == 0):
            aes = -1
        else:
            aes = numer / denom

        totalRT = sum(data[key]["Run Time"])
        art = totalRT / len(data[key]["Run Time"])

        cell_text[len(cell_text) - 1].append(successRate)
        cell_text[len(cell_text) - 1].append(aes)
        cell_text[len(cell_text) - 1].append(art)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns,
             colWidths=[0.5 / 2.54, 0.5 / 2.54, 0.5 / 2.54], cellLoc="center", loc="center right")
    plt.show()


def main():
    csvToDict()
    plotFitness()
    makeTable()


if __name__ == '__main__':
    main()
