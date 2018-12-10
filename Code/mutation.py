"""
Mutation Module

This module will contain functions for mutation individuals

Implemented Functions:
    insert
    inversion
    scramble
    swap
    generate_locations
"""
import random
from individual import Individual


# This function performs insert mutation on an individual
#
# Two random elements in the individual's path are selected
# The second chosen element is then inserted after the first in the path
# The individual's locations list is updated accordingly
#
# Args:
#     individual - The individual to be mutated
#
# Returns:
#     the mutated individual
def insert(individual):
    path = individual.path.copy()

    pointOne = random.randint(0, len(path) - 1)
    pointTwo = random.randint(0, len(path) - 1)

    while(pointOne == pointTwo or (pointOne - pointTwo) == -1):
        pointTwo = random.randint(0, len(path) - 1)
    temp = path[pointTwo]
    del path[pointTwo]
    path.insert(pointOne + 1, temp)
    loc = generate_locations(path)

    return Individual(path, loc, 0)


# This function performs inversion mutation on an individual
#
# A random segment of the individual is chosen. This segment is then reversed in place
# The locations list of each element in the segment is then updated
#
# Args:
#     individual - The individual to be mutated
#
# Returns:
#     the mutated individual
def inversion(individual):
    path = individual.path.copy()

    pointOne = random.randint(0, len(path) - 2)
    pointTwo = random.randint(pointOne + 1, len(path) - 1)

    path[pointOne:pointTwo + 1] = path[pointOne:pointTwo + 1][::-1]

    loc = individual.locations.copy()
    for i in range(pointOne, pointTwo + 1):
        loc[path[i]] = i

    return Individual(path, loc, 0)


# This function performs scramble mutation on an individual
#
# A random segment of the individual is chose. This segment is then scrambled in place
# The locations list of each element in the segment is then updated
#
# Args:
#     individual - The individual to be mutated
#
# Returns:
#     the mutated individual
def scramble(individual):
    path = individual.path.copy()
    loc = individual.locations.copy()
    copy = []

    pointOne = random.randint(0, len(path) - 2)
    pointTwo = random.randint(pointOne + 1, len(path) - 1)

    copy = path[pointOne:pointTwo + 1]
    random.shuffle(copy)
    path[pointOne:pointTwo + 1] = copy

    for i in range(pointOne, pointTwo + 1):
        loc[path[i]] = i

    return Individual(path, loc, 0)


# This function performs swap mutation on an individual
#
# Two random elements in the individual's path are selected and swapped
# The individual's locations list is also updated to reflect the change in the path
#
# Args:
#     individual - The individual to be mutated
#
# Returns:
#     the mutated individual
def swap(individual):
    path = individual.path.copy()
    locs = individual.locations.copy()

    pointOne = random.randint(0, len(path) - 1)
    pointTwo = random.randint(0, len(path) - 1)

    while(pointOne == pointTwo):
        pointTwo = random.randint(0, len(path) - 1)
    temp = path[pointOne]  # hold a value while it gets replaced
    path[pointOne] = path[pointTwo]
    path[pointTwo] = temp

    # Update the locations of the swapped elements
    locs[path[pointTwo]] = pointTwo
    locs[path[pointOne]] = pointOne
    return Individual(path, locs, 0)


# Helper function to generate the locations list for a given path
#
# Walks through the path and populated the locations list
#
# Args:
#     path list
#
# Returns:
#     locations list
def generate_locations(path):
    locations = [-1 for x in range(len(path))]
    for i in range(len(path)):
        locations[path[i]] = i
    return locations
