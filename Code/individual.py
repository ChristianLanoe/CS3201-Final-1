class Individual:


    def __init__(self, path, fitness):
        self.path = path
        self.fitness = fitness


    def __str__(self):
        return ("Path: {} \nFitness: {}".format(self.path, self.fitness))