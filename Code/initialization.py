import numpy as np
from individual import Individual


def permutation(pop_size, chrom_length):
    population = []

    for i in range(pop_size):
        path = np.random.permutation(chrom_length).tolist()
        locations = [-1 for x in range(chrom_length)]
        for j in range(chrom_length):
            locations[path[j]] = j

        population.append(Individual(path, locations, 0))

    return population
