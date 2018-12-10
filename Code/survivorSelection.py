"""
Survivor Selection Module

This module will contain all functions for survivor selection

Implemented Functions:
    mu_lambda
    mu_plus_lambda
    random_uniform
    round_robin_tournament
"""
import random


# This function performs mu,lambda survivor selection
#
# The current population is sorted by fitness, the worst len(offspring) individuals
# are replaced by the offspring
#
# Args:
#     current_pop - The current population
#     offspring   - The offspring of individuals from the current population
#
# Returns:
#     pop - The len(current_pop) individuals selected to continue to the next generation
def mu_lambda(current_pop, offspring):

    pop = []
    pop += current_pop
    pop.sort(key=lambda x: x.fitness, reverse=True)
    pop = pop[:(len(current_pop) - len(offspring))]
    pop += offspring

    return pop


# This function performs mu + lambda survivor selection
#
# The current population and their offspring are added to the same pool and ranked
# The len(current_pop) best individuals are selected to move on to the next generation
#
# Args:
#     current_pop - The current population
#     offspring   - The offspring of individuals from the current population
#
# Returns:
#     pop - The len(current_pop) best individuals in the combined pool of individuals
def mu_plus_lambda(current_pop, offspring):
    pop = []
    pop += current_pop
    pop += offspring
    pop.sort(key=lambda x: x.fitness, reverse=True)
    pop = pop[:len(current_pop)]

    return pop


# This function performs random uniform survivor selection
#
# The current population and their offspring are added to the same pool
# They are then random shuffled and the first len(current_pop) individuals are
# selected to move on to the next generation
#
# Args:
#     current_pop - The current population
#     offspring   - The offspring of individuals from the current population
#
# Returns:
#     pop - The len(current_pop) random individuals from the combined pool of individuals
def random_uniform(current_pop, offspring):
    pop = []
    pop += current_pop
    pop += offspring
    random.shuffle(pop)
    pop = pop[:len(current_pop)]

    return pop


# Each individual k from the total pop is paired against q others in a tournament
# k is awarded a win if its fitness if over the competitors
# mu individuals with top wins are selected
def round_robin_tournament(current_pop, offspring):
    population = []
    pop = []
    q = 10

    fitness = []
    # add current population and offsprings into a list
    pop += current_pop
    pop += offspring
    random.shuffle(pop)

    i = 0
    # calculate q tournaments for all individuals in the total population
    while i < len(current_pop):
        wins = 0
        individual = pop[i]
        testPop = pop.copy()
        random.shuffle(testPop)
        competitors = testPop[:q]
        for k in range(0, q):
            if (individual.fitness > competitors[k].fitness):
                wins += 1
        fitness.append(wins)
        i += 1
    # index in fitness corresponds to index in pop
    tuple = list(zip(pop, fitness))
    from operator import itemgetter
    tuple = sorted(tuple, key=itemgetter(1), reverse=True)
    # only take mu indivuduals with top wins
    tuple = tuple[:len(current_pop)]
    pop, fitness = zip(*tuple)
    population = list(pop)

    return population
