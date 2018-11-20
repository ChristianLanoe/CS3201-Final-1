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


def PMX(parent1, parent2):
    offspring1 = Individual([-1 for x in range(len(parent1.path))], 0)
    offspring2 = Individual([-1 for x in range(len(parent1.path))], 0)

    path_length = len(parent1.path)
    seg_start = random.randint(0, path_length-1)
    seg_end = random.randint(seg_start+1, path_length-1)

    for i in range(seg_start, seg_end+1):
        offspring1.path[i] = parent1.path[i]
        offspring2.path[i] = parent2.path[i]

    offspring1 = PMX_fill_offspring(offspring1, parent2, seg_start, seg_end)
    offspring2 = PMX_fill_offspring(offspring2, parent1, seg_start, seg_end)

    return offspring1, offspring2



def PMX_fill_offspring(offspring, parent, seg_start, seg_end):
    path_length = len(parent.path)
    for i in range(seg_start, seg_end+1):
        if(parent.path[i] == offspring.path[i]):
            continue
        if(parent.path[i] in offspring.path):
            continue
        else:
            insertion_idx = parent.path.index(offspring.path[i])
            while(insertion_idx >= seg_start and insertion_idx <= seg_end):
                insertion_idx = parent.path.index(offspring.path[insertion_idx])
            if(offspring.path[insertion_idx] == -1):
                offspring.path[insertion_idx] = parent.path[i]

    for i in range(path_length):
        if(offspring.path[i] == -1):
            offspring.path[i] = parent.path[i]
    return offspring