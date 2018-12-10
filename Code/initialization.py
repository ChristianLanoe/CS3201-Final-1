"""
Initialization Module

This module will contain functions for creating an initial population

Implemented Functions:
    permutation
"""
import numpy as np
from individual import Individual


# This function generates a random permutation for the path of an individual
# Once the path is generated, it's corresponding locations array is also generated
#
# Args:
#     pop_size        - The number of individuals in the population
#     chrom_length    - The length of the path of each individual
#
# Returns:
#     population - The list of generated individuals
#                - These individuals will be our starting population
def permutation(pop_size, chrom_length):
    population = []

    for i in range(pop_size):
        path = np.random.permutation(chrom_length).tolist()
        locations = [-1 for x in range(chrom_length)]
        for j in range(chrom_length):
            locations[path[j]] = j

        population.append(Individual(path, locations, 0))

    return population
