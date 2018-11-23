import random

def mu_plus_lambda(current_pop, offspring):  

    population = []
    pop = []
    #add current population and offsprings into a list
    for i in range(0, len(current_pop)):
        pop.append(current_pop[i])
    for k in range(0, len(offspring)):
        pop.append(offspring[k])
    #sort said list by fitness value
    pop.sort(key=fitness, reverse=False)
    #add first len(nextPopulation) indexes to population
    for j in range(0, len(current_pop)):
        population.append(pop[j])

    return population

def random_uniform(current_pop, offspring):

    population = []
    pop = []
    #add current population and offsprings into a list
    for i in range(0, len(current_pop)):
        pop.append(current_pop[i])
    for k in range(0, len(offspring)):
        pop.append(offspring[k])
    #shuffle said list
    random.shuffle(pop)
    #add first len(nextPopulation) indexes to population
    for i in range(0, len(current_pop)):
        population.append(pop[i])

    return population

	#This method exploits the large solution space and accepts bad moves at the start then tapers of
	#when the total distance is very high, then the probability of accepting a bad configuration is high, as the distance gets closer to a local or global max (low), the probability of accepting a bad configuration is low
	#essentially it starts as random uniform with a with a growing cutoff range.
	#This is in between the random walk and hillclimb methods
	#hillclimb always accepts the better individual (which gets stuck in local minimums) and random walk that just goes random
def simulated_annealing(current_pop, offspring):
    
    population = []


    return population