import numpy as np
import random
import os
import pprint as pp
import math

# import initialization
# import evaluation
# import recombination
# import mutation
# import parentSelection
# import survivorSelection

cities = []
distances = {}


def readFile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        for line in lines:
            parts = line.split()
            cities.append([parts[1], parts[2]])


def calculate_distances():
    for origin in sorted(cities.keys()):
        distances[origin] = {}
        for dest in sorted(cities.keys()):
            dx = float(cities[origin][0]) - float(cities[dest][0])
            dy = float(cities[origin][1]) - float(cities[dest][1])
            distances[origin][dest] = math.sqrt(dx**2 + dy**2)


def main():
    filename = "../TSP_WesternSahara_29.txt"
    readFile(filename)
    calculate_distances()
    string_length = len(cities)
    popsize = 100
    mating_pool_size = int(popsize * 0.5)  # has to be even
    tournament_size = 3
    mut_rate = 0.2
    xover_rate = 0.9
    gen_limit = 50
    fitnessThreshold = 20

    # population  = initialization.permutation(popsize)


if __name__ == '__main__':
    main()
