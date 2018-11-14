import sys
import pickle
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

def checkSysArgs():
    if(len(sys.argv) != 2):
        print("usage: python {} Country_Name")


def load_file(country_Name):
    filename = country_Name+".pickle"
    with open(filename, "rb") as f:
        return pickle.load(f)


def main():
    checkSysArgs()
    distances = load_file(sys.argv[1])
    string_length = len(distances)
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
