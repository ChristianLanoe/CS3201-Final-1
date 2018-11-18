import sys
import pickle
import numpy as np
import random
import os
import pprint as pp
import math

import individual
import initialization
import evaluation
# import recombination
import mutation
# import parentSelection
# import survivorSelection

cities = []
distances = []


"""
This function checks if the user has supplied the correct number of command
line arguments

Args:
    None

Returns:
    None
"""
def checkSysArgs():
    if(len(sys.argv) != 2):
        print("usage: python {} Country_Name")


"""
This function loads the serialzed distance list of the specified country

The only countries that are currently accepted are:
    Canada
    Uruguay
    WesternSahara

Args:
    countryName - The name of the country to load

Returns:
    The unserialzed list
"""
def load_file(countryName):
    filename = countryName+".pickle"
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

    
    gen = 0
    population  = initialization.permutation(popsize, string_length)
    print("Initial Population \n ======================")
    for i in range(len(population)):
        print(str(population[i]))

    for i in range(popsize):
        population[i].fitness = evaluation.fitness(population[i], distances)

    print("After Fitness Evaluation \n ======================")
    for i in range(len(population)):
        print(str(population[i]))


if __name__ == '__main__':
    main()
