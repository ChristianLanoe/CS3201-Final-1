class Individual:


    def __init__(self, individual, fitness):
        self.individual = individual
        self.fitness = fitness


    def __str__(self):
        return ("Individual: {} \nFitness: {}".format(self.individual, self.fitness))