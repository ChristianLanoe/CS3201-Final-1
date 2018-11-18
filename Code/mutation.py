
from random import randint

# mutate a permutation
def swap (individual):
    
    mutant = individual.copy()

    pointOne = randint(0,len(individual.path)-1)
    pointTwo = randint(0,len(individual.path)-1)

    while(pointOne == pointTwo):
        pointTwo = randint(0, len(individual.path)-1)
    temp = mutant[pointOne] # hold a value while it gets replaced
    mutant[pointOne] = mutant[pointTwo]
    mutant[pointTwo] = temp
    
    return mutant