"""
Parent Selection Module

This module will contain all parent selection functions

Implemented Functions:
    MPS             - Multi-Pointer Selection
    tournament_sel  - Tournament Selection with replacement
"""
import random


# This function performs Multi-Pointer Selection
#
# A cumulative probability list is constructed based on the relative fitness of each individual
# Then, a (mating_pool_size)-armed roulette wheel is used to select the individuals from the population
# that will be parents for the current generation
#
# Args:
#     population          - The individuals in the population
#     mating_pool_size    - The number of individuals to select as parents from the population
#
# Returns:
#     selected - The list of individuals selected to be parents for the current generation
def MPS(population, mating_pool_size):
    selected = []
    cumulative_prob = []

    totalFitness = sum(i.fitness for i in population)
    cumulative_prob.append(population[0].fitness / totalFitness)
    for i in range(1, len(population)):
        cumulative_prob.append(cumulative_prob[i - 1] + (population[i].fitness / totalFitness))

    i = 0
    r = random.uniform(0, 1 / mating_pool_size)
    while len(selected) < mating_pool_size:
        while r <= cumulative_prob[i]:
            selected.append(population[i])
            r += 1 / mating_pool_size
        i += 1

    return selected


# This function performs Tournament Selection with replacement
#
# A subset of individuals is chosen from the population and compared
# The individual in the subset is selected as a parent for current generation
# This is repeated until we have selected a certain number of individuals from the population
#
# Args:
#     population          - The individuals in the population
#     mating_pool_size    - The number of individuals to select as parents from the population
#     tournament_sel      - The number of individuals to compare
#
# Returns:
#     selected - The list of individuals selected to be parents for the current generation
def tournament_sel(population, mating_pool_size, tournament_size):
    selected = []

    while len(selected) < mating_pool_size:
        competitors = random.sample(population, tournament_size)
        competitors.sort(key=lambda x: x.fitness, reverse=True)
        selected.append(competitors[0])
    return selected
