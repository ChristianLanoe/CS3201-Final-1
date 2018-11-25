import sys
import pickle
import numpy as np
import random
import os

import serializer
import plot
import initialization
import evaluation
import recombination
import mutation
import parentSelection
import survivorSelection

cities = []
distances = []


# This function checks if the user has supplied the correct number of command
# line arguments
#
# Args:
#     None
#
# Returns:
#     None
def checkSysArgs():
    if(len(sys.argv) != 2):
        print("usage: python {} Country_Name")


# This function loads the serialzed distance list of the specified country
#
# The only countries that are currently accepted are:
#     Canada
#     Uruguay
#     WesternSahara
#
# Args:
#     countryName - The name of the country to load
#
# Returns:
#     The unserialzed list
def load_file(countryName):
    filename = countryName + ".pickle"
    with open(filename, "rb") as f:
        return pickle.load(f)


def main():
    checkSysArgs()
    distances = load_file(sys.argv[1])
    string_length = len(distances)
    popsize = 100
    mating_pool_size = int(popsize * 0.5)  # has to be even
    tournament_size = 3
    mut_rate = 0.3
    xover_rate = 0.9
    gen_limit = 2500
    fitnessThreshold = 20
    plot_population = []

    gen = 0
    population = initialization.permutation(popsize, string_length)

    for i in range(popsize):
        population[i].fitness = evaluation.fitness(population[i], distances)

    maxFitness = 0
    totalFitness = 0
    prev_averageFitness = 10000
    convergence_counter = 0
    scramble = False
    gen_points = [50,100,150]
    while convergence_counter < 300:
        parents = parentSelection.tournament_sel(population, mating_pool_size, tournament_size)
        # parents = parentSelection.MPS(population, mating_pool_size)

        random.shuffle(parents)

        offspring = []
        i = 0

        while len(offspring) < mating_pool_size:

            # RECOMBINATION
            if random.random() < xover_rate:
                if gen < gen_points[0]:
                    # off1, off2 = recombination.Alternating_Edges(parents[i], parents[i+1])
                    # off1, off2 = recombination.cut_and_crossfill(parents[i], parents[i + 1])
                    # off1, off2 = recombination.OrderCrossover(parents[i], parents[i + 1])
                    # off1, off2 = recombination.PMX(parents[i], parents[i + 1])
                    off1 = recombination.sequential_constructive_crossover(parents[i], parents[i+1], distances)
                    off2 = recombination.sequential_constructive_crossover(parents[i], parents[i+1], distances)
                else:
                    # off1, off2 = recombination.Alternating_Edges(parents[i], parents[i+1])
                    # off1, off2 = recombination.cut_and_crossfill(parents[i], parents[i + 1])
                    # off1, off2 = recombination.OrderCrossover(parents[i], parents[i + 1])
                    off1, off2 = recombination.PMX(parents[i], parents[i + 1])
                    # off1 = recombination.sequential_constructive_crossover(parents[i], parents[i+1], distances)
                    # off2 = recombination.sequential_constructive_crossover(parents[i], parents[i+1], distances)
            else:
                off1 = parents[i]
                off2 = parents[i + 1]

            # MUTATION
            if random.random() < mut_rate:
                # off1 = mutation.insert(off1)
                off1 = mutation.inversion(off1)
                # off1 = mutation.random(off1)
                # off1 = mutation.scramble(off1)
                # off1 = mutation.swap(off1)
            if random.random() < mut_rate:
                # off2 = mutation.insert(off2)
                off2 = mutation.inversion(off2)
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
        # population = survivorSelection.mu_lambda(population, offspring)
        # population = survivorSelection.round_robin_tournament(population, offspring)
        # population = survivorSelection.random_uniform(population, offspring)
        # population = survivorSelection.simulated_annealing(population, offspring)

        gen += 1

        minPathLength = 1 / max(individual.fitness for individual in population)
        totalPathLengths = sum(1 / individual.fitness for individual in population)
        averagePathLength = totalPathLengths / len(population)

        if (averagePathLength - minPathLength) < 100:
            convergence_counter += 1
        else:
            convergence_counter = 0

        print("generation {}: Min Path {}, Average Path {}, diff {}"
              .format(gen, minPathLength, averagePathLength, averagePathLength -minPathLength))
    k = 1
    for i in range(0, popsize):
        if(1/population[i].fitness) == minPathLength:
            plot_population.append(population[i].path)
            print("best solution {} {} {}".format(k, population[i].path, 1/population[i].fitness))
            k+=1
    plot.plotTSP(plot_population[0], serializer.readFile("../TSP_WesternSahara_29.txt"))


if __name__ == '__main__':
    main()
