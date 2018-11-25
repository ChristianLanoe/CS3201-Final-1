class Individual:

    def __init__(self, path, locations, fitness):
        self.path = path
        self.fitness = fitness
        self.locations = locations

    def __repr__(self):
        return "Path: {} \nLocations: {} \nFitness: {}".format(self.path, self.locations, self.fitness)

    def __str__(self):
        return "Path: {} \nLocations: {} \nFitness: {}".format(self.path, self.locations, self.fitness)
