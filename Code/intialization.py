import numpy as np

def permutation(pop_size, chrom_length):
    population = []

    for i in range(pop_size):
        population.append(np.random.permutation(chrom_length).tolist())

    return population
