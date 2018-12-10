"""
Individual represents a single individual in the population

path        - a list of a permutations of integers that represent the cities and the order they are visited
locations   - a list of the location of each city in the path
fitness     - a floating point number that represents the fitness of the individual
            - to make this a maximization problem, fitness is the inverse of path length

example:
    path        = [1,5,2,0,3,4]
    location    = [3,0,2,4,5,1]

    location of city 0 is at index 3 of path
    location of city 2 is at index 2 of path
    location of city 5 is at index 1 of path
"""
class Individual:

    def __init__(self, path, locations, fitness):
        self.path = path
        self.fitness = fitness
        self.locations = locations

    def __repr__(self):
        return "Path: {} \nLocations: {} \nFitness: {}".format(self.path, self.locations, self.fitness)

    def __str__(self):
        return "Path: {} \nLocations: {} \nFitness: {}".format(self.path, self.locations, self.fitness)
