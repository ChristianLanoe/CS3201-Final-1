from individual import Individual
import random
import numpy as np


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
    seg_end = random.randint(seg_start, path_length-1)
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


"""
This recombination operator randomly picks which parent to use as a starting point
From there it picks the edge from the parents that has the shortest distance

If the destination city of the edge is already in the offspring, we pick the
first element in a list of unvisited cities and use that for comparison

Args:
    parent1 & parent2
    distances - the distance matrix 
Returns:
    The offspring of parent1 and parent2
"""
def sequential_constructive_crossover(parent1, parent2, distances):
    path_length = len(parent1.path)
    unvisited_cities = list(range(path_length))

    # We don't need to initialize an Individual just yet
    # All we need right now is the path of the inidividual
    offspring = []

    # Randomly choosing which parent will be the first to consider
    if(np.random.rand() < .5):
        initial = parent1.path
    else:
        initial = parent2.path

    # Adding first element of initial to offspring path and removing it from
    # the the list of unvisited cities
    offspring.append(initial[0])
    unvisited_cities.remove(offspring[0])

    currentCity = initial[0]
    while(len(offspring) < path_length):
        next1_oob = False
        next1_inOffspring = False

        # The next city in the cycle is determined by the city after the current
        # city in each parent
        # next1 - the city after the current city in parent1
        # next2 - the city after the current city in parent2
        next1_idx = parent1.path.index(currentCity)+1
        next2_idx = parent2.path.index(currentCity)+1
        if(next1_idx<path_length):
            if(parent1.path[next1_idx] not in offspring):
                next1 = parent1.path[next1_idx]
            else:
                next1 = unvisited_cities[0]
                next1_inOffspring = True
        else:
            next1_oob = True
            next1 = unvisited_cities[0]

        if(next2_idx < path_length):
            if(parent2.path[next2_idx] not in offspring):
                next2 = parent2.path[next2_idx]
            else:
                if((next1_inOffspring or next1_oob) and len(unvisited_cities) > 1):
                    next2 = unvisited_cities[1]
                else:
                    next2 = unvisited_cities[0]
        else:
            if((next1_inOffspring or next1_oob) and len(unvisited_cities) > 1):
                next2 = unvisited_cities[1]
            else:
                next2 = unvisited_cities[0]
                
        # If the next city is the same in both parents add it to the offspring
        # and continue
        if(next1 == next2):
            offspring.append(next1)
            unvisited_cities.remove(next1)
            currentCity = next1
            continue

        d1 = distances[currentCity][next1]
        d2 = distances[currentCity][next2]

        if(d1<d2):
            offspring.append(next1)
            currentCity = next1
        else:
            offspring.append(next2)
            currentCity = next2

        unvisited_cities.remove(currentCity)

    
    return Individual(offspring, 0)


"""
Debugging method for formatted printing of individual paths or plain lists

title is printed and padded to contain at least 13 characters
Each element in path is padded to contain at least 2 digits

Feel free to change these values to suit your needs

Args:
    path - the path of interest
    title - the label appended before the path is printed
Returns:
    None
"""
def printPath(path, title):
    print("{:13s}".format(title), end=" ")
    for i in range(len(path)):
        print("{:2d}".format(path[i]), end=" ")
    print()
