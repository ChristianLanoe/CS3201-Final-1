import random

#Parent Selection using tournament selection with replacement


#tournament selection with replacement
def tournament_sel(population, mating_pool_size, tournament_size):
    selected = []
    print(mating_pool_size)
    while len(selected) < mating_pool_size:
        tour_index = random.sample(range(0,len(population)), tournament_size)
        best_fit = -1000
        best_index = -1
        for i in range (0, tournament_size):
            if population[tour_index[i]].fitness > best_fit:
                best_fit = population[tour_index[i]].fitness
                best_index = tour_index[i]
        selected.append(best_index)
    return selected
