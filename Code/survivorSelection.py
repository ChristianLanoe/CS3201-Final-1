import random

def mu_plus_lambda(current_pop, offspring):  

    pop = []
    pop += current_pop
    pop += offspring
    pop.sort(key=lambda x: x.fitness, reverse=True)
    pop = pop[:len(current_pop)]

    return pop

def random_uniform(current_pop, offspring):

    pop = []
    pop += current_pop
    pop += offspring
    random.shuffle(pop)
    pop = pop[:len(current_pop)]

    return pop


# Each individual k from the total pop is paired against q others in a tournament
# k is awarded a win if its fitness if over the competitors
# mu individuals with top wins are selected
def round_robin_tournament(current_pop, offspring):

    population = []
    pop = []
    q = 10
    
    fitness = []
    #add current population and offsprings into a list
    pop += current_pop
    pop += offspring

    i = 0
    while i < q:
        wins = 0
        individual = pop[i]
        testPop = pop.copy()
        random.shuffle(testPop)
        competitors = testPop[:q]
        for k in range(0, q):
            if (individual.fitness > competitors[k].fitness):
                wins += 1
        tuple = list(zip(pop, fitness))
        fitness.append(wins)
        i += 1
        # index in fitness corresponds to index in pop
    tuple = list(zip(pop, fitness))
    from operator import itemgetter
    tuple = sorted(tuple, key=itemgetter(1), reverse=True)
    # only take mu indivuduals with top wins
    tuple = tuple[:len(current_pop)]
    pop, fitness = zip(*tuple)
    population = list(pop)

    return population

	#This method exploits the large solution space and accepts bad moves at the start then tapers of
	#when the total distance is very high, then the probability of accepting a bad configuration is high, as the distance gets closer to a local or global max (low), the probability of accepting a bad configuration is low
	#essentially it starts as random uniform with a with a growing cutoff range.
	#This is in between the random walk and hillclimb methods
	#hillclimb always accepts the better individual (which gets stuck in local minimums) and random walk that just goes random
    # copy current pop and offspring, select random index in both and compare
    # while(1 < current pop size)
    # if fitness of offspring is better, replace
    # else if fitness of parent is better, calculate the change of energy diff
    # if the difference is lower than current temp, replace parent with offspring
    # temp is set at beginning as well as cooling rate
    
def simulated_annealing(current_pop, offspring):

    # set these 2 in main and send temp as argument ^
    # test 
    temp = 10000
    coolingRate = 0.003
    
    # copy 
    curPop = current_pop.copy()
    curOff = offspring.copy()

    population = []
    pop = []

    i = 0
    # run loop while length of Population[] is less than length of current population
    while i < len(current_pop):

        # get a random current individual and offspring index
        currentIndex = random.uniform(0, len(current_pop))
        offspringIndex = random.uniform(0, len(offspring))


        # copy those individuals
        currentCopy = current_pop[currentIndex]
        offspringCopy = offspring[offspringIndex]


        # if currentCopy fitness is less than offspringCopy fitness, add offspringCopy to pop
        if (currentCopy.fitness < offspringCopy.fitness):
            population.append(offspring[offspringIndex])
        else:
            diff = currentCopy.fitness - offspringCopy.fitness
            if diff < temp:
                population.append(offspring[offspringIndex])
            else:
                population.append(current_pop[currentIndex])

        # update the coolingRate
        temp *= 1-coolingRate

    return population