# Function to calculate the fitness of an individual
# Fitness is the inverse of the path length
#
# Args:
#     individual
#     distances - the distances from each city to all other cities
# Returns:
#     the inverse of the path length
def fitness(individual, distances):
    distance = 0

    # Calculating the distance from the first city in the path to the last
    for i in range(0, len(individual.path) - 1):
        origin = individual.path[i]
        destination = individual.path[i + 1]
        distance += distances[origin][destination]

    # Adding the distance from the last city back to the start
    distance += distances[individual.path[len(individual.path) - 1]][individual.path[0]]

    return 1 / distance
