import numpy as np

from individual import Individual

def permutation(pop_size, chrom_length):
    population = []

    for i in range(pop_size):
        population.append(Individual(np.random.permutation(chrom_length).tolist(), 0))

    return population
