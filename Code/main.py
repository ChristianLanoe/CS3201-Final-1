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
import recombination
import mutation
import parentSelection
import survivorSelection

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
        print(population[i])

    for i in range(popsize):
        population[i].fitness = evaluation.fitness(population[i], distances)

    print("After Fitness Evaluation \n ======================")
    for i in range(len(population)):
        print(population[i])

    maxFitness = 0
    while gen < gen_limit:
        parents = parentSelection.tournament_sel(population, mating_pool_size, tournament_size)

        random.shuffle(parents)


        offspring = []
        i = 0

        while len(offspring) < mating_pool_size:

            # RECOMBINATION
            if random.random() < xover_rate:
                off1, off2 = recombination.Alternating_Edges(parents[i], parents[i+1])
                # off1, off2 = recombination.cut_and_crossfill(parents[i], parents[i+1])
                # off1, off2 = recombination.OrderCrossover(parents[i], parents[i+1])
                # off1, off2 = recombination.PMX(parents[i], parents[i+1])
                # off1, off2 = recombination.sequential_constructive_crossover(parents[i], parents[i+1])
            else:
                off1 = population[i].copy()
                off2 = population[i + 1].copy()

            # MUTATION
            if random.random() < mut_rate:
                off1 = mutation.insert(off1)
                # off1 = mutation.inversion(off1)
                # off1 = mutation.random(off1)
                # off1 = mutation.scramble(off1)
                # off1 = mutation.swap(off1)
            if random.random() < mut_rate:
                off2 = mutation.insert(off2)
                # off2 = mutation.inversion(off2)
                # off2 = mutation.random(off2)
                # off2 = mutation.scramble(off2)
                # off2 = mutation.swap(off2)

            # FITNESS EVALUATION
            off1.fitness = evaluation.fitness(off1, distances)
            offspring.append(off1)

            off2.fitness = evaluation.fitness(off2, distances)
            offspring.append(off2)

        # SURVIVOR SELECTION
        population = survivorSelection.mu_plus_lambda(population, offspring)
        # population = survivorSelection.random_uniform(population, offspring)
        # population = survivorSelection.simulated_annealing(population, offspring)

        gen += 1

        maxFitness = max(individual.fitness for individual in population)
        totalFitness = sum(individual.fitness for individual in population)

        print("generation {}: best fitness {} average fitness {}".format(gen, maxFitness, totalfitness/len(population)))
    k = 0
    for i in range(0, popsize):
        if(population[i].fitness) == maxFitness:
            print("best solution {} {} {}".format(k, population[i].path, population[i].fitness))


if __name__ == '__main__':
    main()
