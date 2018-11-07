import numpy as np
import random
import os
import pprint as pp

# import initialization
# import evaluation
# import recombination
# import mutation
# import parentSelection
# import survivorSelection

cities = {}


def readFile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        for line in lines:
            parts = line.split()
            cities[parts[0]] = [parts[1], parts[2]]


def main():
    filename = "../TSP_WesternSahara_29.txt"
    readFile(filename)
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