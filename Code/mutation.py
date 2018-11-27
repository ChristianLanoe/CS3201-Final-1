import random
from individual import Individual
# mutate a permutation


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


def insert (individual):
    path = individual.path.copy()

    pointOne = random.randint(0,len(path)-1)
    pointTwo = random.randint(0,len(path)-1)

    while(pointOne == pointTwo or pointOne-pointTwo==-1):
        pointTwo = random.randint(0, len(path)-1)
    temp = path[pointTwo]
    del path[pointTwo]
    path.insert(pointOne+1,temp)
    loc = generate_locations(path)

    return Individual(path, loc, 0)


def inversion (individual):
    path = individual.path.copy()

    pointOne = random.randint(0,len(path)-2)
    pointTwo = random.randint(pointOne+1,len(path)-1)

    path[pointOne:pointTwo+1]=path[pointOne:pointTwo+1][::-1]

    loc = individual.locations.copy()
    for i in range(pointOne, pointTwo +1):
        loc[path[i]] = i

    return Individual(path, loc, 0)


def scramble (individual):
    path = individual.path.copy()
    loc = individual.locations.copy()
    copy = []

    pointOne = random.randint(0,len(path)-2)
    pointTwo = random.randint(pointOne+1,len(path)-1)

    copy = path[pointOne:pointTwo+1]
    random.shuffle(copy)
    path[pointOne:pointTwo+1] = copy

    for i in range(pointOne, pointTwo+1):
        loc[path[i]] = i

    return Individual(path, loc, 0)


def generate_locations(path):
    locations = [-1 for x in range(len(path))]
    for i in range(len(path)):
        locations[path[i]] = i
    return locations
