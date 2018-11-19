import numpy

def mu_plus_lambda(current_pop, offspring):  

    population = []

    #append offspring onto parents

    pop = []

    for i in range(0, len(current_pop)):
        pop.append(current_pop[i])
    for k in range(0, len(offspring)):
        pop.append(offspring)

    pop.sort(key=fitness, reverse=False)

    for j in range(0, len(current_pop)):
        population.append(pop.j)

    return population

def random_uniform(current_pop, offspring):

    population = []

    pop = []

    for i in range(0, len(current_pop)):
        pop.append(current_pop[i])
    for k in range(0, len(offspring)):
        pop.append(offspring)

    test = [numpy.random.choice(len(pop), len(current_pop))]

    for i in range(0, len(test)):
        population.append(pop[test[i]])

    return population
