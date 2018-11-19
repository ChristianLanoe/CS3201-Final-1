from individual import Individual
import random


def cut_and_crossfill(parent1, parent2):

    offspring1 = Individual([], 0)
    offspring2 = Individual([], 0)

    crossover_point = random.randint(0, len(parent1.path)-3)

    offspring1.path = parent1.path[:crossover_point+1]
    offspring2.path = parent2.path[:crossover_point+1]

    i = crossover_point + 1
    for x in range(len(parent1.path)):
        if(parent2.path[i] not in offspring1.path):
            offspring1.path.append(parent2.path[i])
        if(parent1.path[i] not in offspring2.path):
            offspring2.path.append(parent1.path[i])
        if(i !=  len(parent1.path) - 1):
            i += 1
        else:
            i = 0

    return offspring1, offspring2
