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
    templ = locs[pointOne]
    path[pointOne] = path[pointTwo]
    locs[pointOne] = locs[pointTwo]
    path[pointTwo] = temp
    locs[pointTwo] = templ

    return Individual(path, locs, 0)


def insert (individual):
    mutant = individual.path.copy()

    pointOne = random.randint(0,len(mutant)-1)
    pointTwo = random.randint(0,len(mutant)-1)
    
    while(pointOne == pointTwo or pointOne-pointTwo==-1):
        pointTwo = random.randint(0, len(mutant)-1)
    temp = mutant[pointTwo]
    del mutant[pointTwo]
    mutant.insert(pointOne+1,temp)
    
    mutant = Individual(mutant,0)

    return mutant

def inversion (individual):
    mutant = individual.path.copy()

    pointOne = random.randint(0,len(mutant)-2)
    pointTwo = random.randint(pointOne+1,len(mutant)-1)

    mutant[pointOne:pointTwo+1]=mutant[pointOne:pointTwo+1][::-1]

    mutant = Individual(mutant,0)

    return mutant

def scramble (individual):
    mutant = individual.path.copy()
    copy = []

    pointOne = random.randint(0,len(mutant)-2)
    pointTwo = random.randint(pointOne+1,len(mutant)-1)
    
    copy = mutant[pointOne:pointTwo+1]
    random.shuffle(copy)
    mutant[pointOne:pointTwo+1] = copy

    mutant = Individual(mutant,0)

    return mutant
