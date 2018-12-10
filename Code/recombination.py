"""
Recombination Module

This module will contain all functions for performing recombination
"""
from individual import Individual
import random
import numpy as np


# This function performs the cut and crossfill recombination operator
# It follows the algorithm from the course textbook
#
# Args:
#     parent1 & parent2 - Individuals from the list of individuals selected to be parents 
#
# Returns:
#     Two offspring Individuals
def cut_and_crossfill(parent1, parent2):
    crossover_point = random.randint(0, len(parent1.path) - 3)

    locs1 = [-1 for x in range(len(parent1.path))]
    locs2 = [-1 for x in range(len(parent1.path))]

    path1 = parent1.path[:crossover_point + 1].copy()
    path2 = parent2.path[:crossover_point + 1].copy()

    for i in range(crossover_point + 1):
        locs1[path1[i]] = i
        locs2[path2[i]] = i

    i = crossover_point + 1
    for x in range(len(parent1.path)):
        if(locs1[parent2.path[i]] == -1):
            path1.append(parent2.path[i])
            locs1[parent2.path[i]] = i
        if(locs2[parent1.path[i]] == -1):
            path2.append(parent1.path[i])
            locs2[parent1.path[i]] = i
        if(i != len(parent1.path) - 1):
            i += 1
        else:
            i = 0

    return Individual(path1, locs1, 0), Individual(path2, locs2, 0)


# This function performs the order crossover recombination operator
# It follows the algorithms from the course textbook

# Args:
#     parent1 & parent2  - Individuals from the list of individuals selected to be parents

# Returns:
#     Two offspring Individuals
def OrderCrossover(parent1, parent2):
    path_length = len(parent1.path)
    path1 = [-1 for x in range(path_length)]
    path2 = [-1 for x in range(path_length)]

    locs1 = path1.copy()
    locs2 = path2.copy()

    seg_start = np.random.randint(0, path_length - 1)
    seg_end = np.random.randint(seg_start, path_length - 1)

    path1[seg_start:seg_end + 1] = parent1.path[seg_start:seg_end + 1].copy()
    path2[seg_start:seg_end + 1] = parent2.path[seg_start:seg_end + 1].copy()
    for i in range(seg_start, seg_end + 1):
        locs1[path1[i]] = i
        locs2[path2[i]] = i

    path1 = OrderCrossover_fill(path1, parent2.path, locs1, seg_end)
    path2 = OrderCrossover_fill(path2, parent1.path, locs2, seg_end)

    return Individual(path1, locs1, 0), Individual(path2, locs2, 0)


# Helper function to fill the children from Order Crossover
#
# Args:
#     offspringPath - the path with the segment from its parent
#     parentPath    - the parent that didn't contribute its segment to offspring path
#     seg_end       - the index of the last crossover point
#
# Returns:
#     offspringPath - the completed path
def OrderCrossover_fill(offspringPath, parentPath, locs, seg_end):
    p = seg_end + 1
    c = seg_end + 1
    while(-1 in offspringPath):
        if(parentPath[p] not in offspringPath):
            offspringPath[c] = parentPath[p]
            locs[parentPath[p]] = c
            c += 1
            if(c == len(offspringPath)):
                c = 0
        else:
            p += 1
            if(p == len(parentPath)):
                p = 0
    return offspringPath


# This function performs the Partially Mapped Crossover recombination operator
# It follows the algorithm coverd in the course textbook
#
# Args:
#     parent1 & parent2 - Individuals from the list of individuals selected to be parents
#
# Returns:
#     Two offspring Individuals
def PMX(parent1, parent2):
    # offspring1 = Individual([-1 for x in range(len(parent1.path))], 0)
    # offspring2 = Individual([-1 for x in range(len(parent1.path))], 0)
    path1 = [-1 for x in range(len(parent1.path))]
    path2 = path1.copy()
    locs1 = path1.copy()
    locs2 = path1.copy()

    path_length = len(parent1.path)
    seg_start = random.randint(0, path_length - 1)
    seg_end = random.randint(seg_start, path_length - 1)
    for i in range(seg_start, seg_end + 1):
        path1[i] = parent1.path[i]
        locs1[path1[i]] = i
        path2[i] = parent2.path[i]
        locs2[path2[i]] = i

    offspring1 = PMX_fill_offspring(path1, locs1, parent2, seg_start, seg_end)
    offspring2 = PMX_fill_offspring(path2, locs2, parent1, seg_start, seg_end)

    return offspring1, offspring2


# Helper function to fill the offspring from Partially Mapped Crossover
#
# Args:
#     path        - the current path of an offspring
#     locations   - the locations list of an offspring
#     parent      - the parent that the offspring is mapped from
#     seg_start   - the start index of the segment copied from the other parent
#     seg_eng     - the end index of the segment copied from the other parent
#
# Returns:
#     The completed offspring
def PMX_fill_offspring(path, locations, parent, seg_start, seg_end):
    path_length = len(parent.path)
    for i in range(seg_start, seg_end + 1):
        if(parent.path[i] == path[i]):
            continue
        if(parent.path[i] in path):
            continue
        else:
            insertion_idx = parent.locations[path[i]]
            while(insertion_idx in range(seg_start, seg_end + 1)):
                insertion_idx = parent.locations[path[insertion_idx]]
            if(path[insertion_idx] == -1):
                path[insertion_idx] = parent.path[i]
                locations[parent.path[i]] = insertion_idx

    for i in range(path_length):
        if(path[i] == -1):
            path[i] = parent.path[i]
            locations[path[i]] = i

    return Individual(path, locations, 0)


# Alternating Edges Crossover start by adding the first 2 cities of a parent to the
# offspring. It then adds the city that proceeds from the second parent then the
# city that proceeds from the first parent and so on.
#
# If the next city is already in the offspring we add the first city in a
# randomized list of unvisited cities
def Alternating_Edges(parent1, parent2):
    path1 = []
    path2 = []
    path_length = len(parent1.path)
    loc1 = [-1 for x in range(path_length)]
    loc2 = loc1.copy()
    parents = [parent1, parent2]

    path1.append(parent1.path[0])
    loc1[parent1.path[0]] = 0
    path1.append(parent1.path[1])
    loc1[parent1.path[1]] = 1

    path2.append(parent2.path[0])
    loc2[parent2.path[0]] = 0
    path2.append(parent2.path[1])
    loc2[parent2.path[1]] = 1

    offspring1 = Alternating_Edges_fill_offspring(path1, loc1, parents, 1, path_length)
    offspring2 = Alternating_Edges_fill_offspring(path2, loc2, parents, 0, path_length)

    return offspring1, offspring2


# Helper Function to fill offspring from Alternating Edges Crossover
#
# Args:
#     path - the path of the offspring. Already contains the first 2 cities from
#            one of the parents
#     parents - the array of parent paths
#     curParent - the index of the current currentParent
#     path_length
#
# Returns:
#     offspringPath - the path of the offspring
def Alternating_Edges_fill_offspring(path, locations, parents, curParent, path_length):
    # unvisited_cities = np.random.permutation(path_length).tolist()
    unvisited_cities = list(range(path_length))
    for city in path:
        unvisited_cities.remove(city)

    while(len(path) < path_length):
        city_idx = parents[curParent].locations[path[len(path) - 1]]
        # city_idx = parents[curParent].index(path[len(path) - 1])
        if(city_idx == path_length - 1):
            city_idx = -1
        next_idx = city_idx + 1

        if(parents[curParent].path[next_idx] not in path):
            path.append(parents[curParent].path[next_idx])
            locations[path[len(path) - 1]] = len(path) - 1
        else:
            path.append(unvisited_cities[0])
            locations[path[len(path) - 1]] = len(path) - 1
        unvisited_cities.remove(path[len(path) - 1])
        curParent = (curParent + 1) % len(parents)

    return Individual(path, locations, 0)


# This recombination operator randomly picks which parent to use as a starting point
# From there it picks the edge from the parents that has the shortest distance
#
# If the destination city of the edge is already in the offspring, we pick the
# first element in a list of unvisited cities and use that for comparison
#
# Args:
#     parent1 & parent2
#     distances - the distance matrix
# Returns:
#     The offspring of parent1 and parent2
def sequential_constructive_crossover(parent1, parent2, distances):
    path_length = len(parent1.path)
    unvisited_cities = list(range(path_length))
    # np.random.shuffle(unvisited_cities)
    # unvisited_cities = np.random.permutation(path_length).tolist()

    # We don't need to initialize an Individual just yet
    # All we need right now is the path of the inidividual
    offspring = []
    locs = [-1 for x in range(path_length)]
    # Randomly choosing which parent will be the first to consider
    if(np.random.rand() < .5):
        initial = parent1.path
    else:
        initial = parent2.path

    # Adding first element of initial to offspring path and removing it from
    # the the list of unvisited cities
    offspring.append(initial[0])
    locs[initial[0]] = 0
    unvisited_cities.remove(offspring[0])

    currentCity = initial[0]
    while(len(offspring) < path_length):
        # The next city in the cycle is determined by the city after the current
        # city in each parent
        # next1 - the city after the current city in parent1
        # next2 - the city after the current city in parent2
        next1_idx = parent1.locations[currentCity] + 1
        next2_idx = parent2.locations[currentCity] + 1
        if (next1_idx < path_length) and (locs[parent1.path[next1_idx]] == -1):
            next1 = parent1.path[next1_idx]
        else:
            next1 = unvisited_cities[0]

        if(next2_idx < path_length) and (locs[parent2.path[next2_idx]] == -1):
            next2 = parent2.path[next2_idx]
        else:
            next2 = unvisited_cities[0]

        # If the next city is the same in both parents add it to the offspring
        # and continue
        if(next1 == next2):
            offspring.append(next1)
            locs[next1] = len(offspring) - 1
            unvisited_cities.remove(next1)
            currentCity = next1
            continue

        d1 = distances[currentCity][next1]
        d2 = distances[currentCity][next2]

        if(d1 < d2):
            offspring.append(next1)
            locs[next1] = len(offspring) - 1
            currentCity = next1
        else:
            offspring.append(next2)
            locs[next2] = len(offspring) - 1
            currentCity = next2

        unvisited_cities.remove(currentCity)

    return Individual(offspring, locs, 0)


# Debugging method for formatted printing of individual paths or plain lists
#
# title is printed and padded to contain at least 13 characters
# Each element in path is padded to contain at least 2 digits
#
# Feel free to change these values to suit your needs
#
# Args:
#     path - the path of interest
#     title - the label appended before the path is printed
# Returns:
#     None
def printPath(path, title):
    print("{:13s}".format(title), end=" ")
    for i in range(len(path)):
        print("{:2d}".format(path[i]), end=" ")
    print()


# Helper function to generate the locations list for a given path
#
# Args:
#     path - a complete path
#
# Returns:
#     locations - the locations list
def generate_locations(path):
    locations = [0 for x in range(len(path))]
    for i in range(len(path)):
        locations[path[i]] = i

    return locations
