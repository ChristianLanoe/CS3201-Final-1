import random

#Parent Selection using tournament selection with replacement


#tournament selection with replacement
def tournament_sel(population, mating_pool_size, tournament_size):
    selected = []

    while len(selected) < mating_pool_size:
        competitors = random.sample(population, tournament_size)
        competitors.sort(key=lambda x: x.fitness, reverse=True)
        selected.append(competitors[0])
    return selected


"""
Multi-pointer Selection
"""
def MPS(population, mating_pool_size):
    selected = []
    cumulative_prob = []

    totalFitness = sum(i.fitness for i in population)
    cumulative_prob.append(population[0].fitness/totalFitness)
    for i in range(1, len(population)):
        cumulative_prob.append(cumulative_prob[i-1] + (population[i].fitness/totalFitness))

    i = 0
    r = random.uniform(0, 1 / mating_pool_size)
    while len(selected) < mating_pool_size:
        while r <= cumulative_prob[i]:
            selected.append(population[i])
            r += 1/mating_pool_size
        i += 1

    return selected
