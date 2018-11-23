import random
from individual import Individual
# mutate a permutation

def swap (individual):
    mutant = individual.path.copy()

    pointOne = random.randint(0,len(mutant)-1)
    pointTwo = random.randint(0,len(mutant)-1)

    while(pointOne == pointTwo):
        pointTwo = random.randint(0, len(mutant)-1)
    temp = mutant[pointOne] # hold a value while it gets replaced
    mutant[pointOne] = mutant[pointTwo]
    mutant[pointTwo] = temp
    
    mutant = Individual(mutant,0)

    return mutant

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
