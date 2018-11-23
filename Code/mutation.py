import random
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
    
    return mutant

def insert (individual):
    mutant = individual.path.copy()

    pointOne = random.randint(0,len(mutant)-1)
    pointTwo = random.randint(0,len(mutant)-1)
    
    while(pointOne == pointTwo or pointOne-pointTwo==-1):
        pointTwo = random.randint(0, len(mutant)-1)
    print("Point 1:",pointOne)
    print("Point 2:",pointTwo)
    temp = mutant[pointTwo]
    del mutant[pointTwo]
    mutant.insert(pointOne+1,temp)
    
    return mutant

def inversion (individual):
    mutant = individual.copy()

    pointOne = random.randint(0,len(mutant)-2)
    pointTwo = random.randint(pointOne+1,len(mutant)-1)

    mutant[pointOne:pointTwo+1]=mutant[pointOne:pointTwo+1][::-1]
    return mutant

def scramble (individual):
    mutant = individual.path.copy()
    copy = []

    pointOne = random.randint(0,len(mutant)-2)
    pointTwo = random.randint(pointOne+1,len(mutant)-1)
    
    copy = mutant[pointOne:pointTwo+1]
    random.shuffle(copy)
    mutant[pointOne:pointTwo+1] = copy
    return mutant