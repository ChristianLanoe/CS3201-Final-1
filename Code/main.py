import sys
import pickle
import random
import os
import serializer
import plot
import initialization
import evaluation
import recombination
import mutation
import parentSelection
import survivorSelection
import csv
from timeit import default_timer as timer

distances = []
summaryData = {}
runData = {}
evals2solution = 0
successfulRun = False
optimalFitness = 1 / 27603


def countEvals(indivFitness):
    global optimalFitness, successfulRun, evals2solution
    if(indivFitness < optimalFitness and not successfulRun):
        evals2solution += 1
    else:
        successfulRun = True


def main():
    distances = load_file(sys.argv[1])
    filename = getTSPfilename(sys.argv[1])

    global summaryData, runData
    string_length = len(distances)
    popsize = 100
    mating_pool_size = int(popsize * 0.5)  # has to be even
    tournament_size = 6
    mut_rate = 0.3
    xover_rate = 0.9
    gen_limit = 2500
    fitnessThreshold = 20
    plot_population = []

    gen = 0

    start = timer()
    population = initialization.permutation(popsize, string_length)

    for i in range(popsize):
        population[i].fitness = evaluation.fitness(population[i], distances)
        countEvals(population[i].fitness)

    # maxFitness = 0
    minPathLength = 0
    totalFitness = 0
    prev_averageFitness = 10000
    convergence_counter = 0
    scramble = False
    while convergence_counter < 100:
        parents = parentSelection.tournament_sel(population, mating_pool_size, tournament_size)
        # parents = parentSelection.MPS(population, mating_pool_size)
        random.shuffle(parents)

        offspring = []
        i = 0

        while len(offspring) < mating_pool_size:

            # RECOMBINATION
            if random.random() < xover_rate:
                if gen < 100:
                    # off1, off2 = recombination.Alternating_Edges(parents[i], parents[i+1])
                    # off1, off2 = recombination.cut_and_crossfill(parents[i], parents[i + 1])
                    # off1, off2 = recombination.OrderCrossover(parents[i], parents[i + 1])
                    # off1, off2 = recombination.PMX(parents[i], parents[i + 1])
                    off1 = recombination.sequential_constructive_crossover(parents[i], parents[i + 1], distances)
                    off2 = recombination.sequential_constructive_crossover(parents[i], parents[i + 1], distances)
                else:
                    # off1, off2 = recombination.Alternating_Edges(parents[i], parents[i+1])
                    # off1, off2 = recombination.cut_and_crossfill(parents[i], parents[i + 1])
                    # off1, off2 = recombination.OrderCrossover(parents[i], parents[i + 1])
                    off1, off2 = recombination.PMX(parents[i], parents[i + 1])
                    # off1 = recombination.sequential_constructive_crossover(parents[i], parents[i+1], distances)
                    # off2 = recombination.sequential_constructive_crossover(parents[i], parents[i+1], distances)
            else:
                off1 = parents[i]
                off2 = parents[i + 1]

            # MUTATION
            if random.random() < mut_rate:
                # off1 = mutation.insert(off1)
                off1 = mutation.inversion(off1)
                # off1 = mutation.scramble(off1)
                # off1 = mutation.swap(off1)
            if random.random() < mut_rate:
                # off2 = mutation.insert(off2)
                off2 = mutation.inversion(off2)
                # off2 = mutation.scramble(off2)
                # off2 = mutation.swap(off2)

            # FITNESS EVALUATION
            off1.fitness = evaluation.fitness(off1, distances)
            offspring.append(off1)
            countEvals(off1.fitness)

            off2.fitness = evaluation.fitness(off2, distances)
            offspring.append(off2)
            countEvals(off2.fitness)

        # SURVIVOR SELECTION
        population = survivorSelection.mu_plus_lambda(population, offspring)
        # population = survivorSelection.mu_lambda(population, offspring)
        # population = survivorSelection.round_robin_tournament(population, offspring)
        # population = survivorSelection.random_uniform(population, offspring)
        # population = survivorSelection.simulated_annealing(population, offspring)

        gen += 1

        minPathLength = 1 / max(i.fitness for i in population)
        totalPathLengths = sum(1 / i.fitness for i in population)
        averagePathLength = totalPathLengths / len(population)

        if (averagePathLength - minPathLength) < 1:
            convergence_counter += 1
        else:
            convergence_counter = 0

        # print("generation {}: Min Path {}, Average Path {}, diff {}"
        #       .format(gen, minPathLength, averagePathLength, averagePathLength - minPathLength))
        if(len(sys.argv) >= 4):
            runData["Best Fitness"] = minPathLength
            runData["Average Fitness"] = averagePathLength
            writeFile = sys.argv[3]
            if(sys.argv[2] == "r"):
                if(not os.path.exists(writeFile)):
                    with open(writeFile, "w+") as f:
                        writer = csv.DictWriter(f, fieldnames=runData.keys())
                        writer.writeheader()
                with open(writeFile, 'a+') as f:
                    writer = csv.DictWriter(f, fieldnames=runData.keys())
                    writer.writerow(runData)
    k = 1
    for i in range(0, popsize):
        if(1 / population[i].fitness) == minPathLength:
            plot_population.append(population[i].path)
            print("best solution {} {} {}".format(k, population[i].path, 1 / population[i].fitness))
            k += 1
    plot.plotTSP(plot_population[0], serializer.readFile(filename))
    end = timer() - start
    if(len(sys.argv) >= 4):
        summaryData["Best Fitness"] = minPathLength
        summaryData["Evaluations to Solution"] = evals2solution
        summaryData["Successful Run"] = successfulRun
        summaryData["Run Time"] = end
        writeFile = sys.argv[3]
        if(sys.argv[2] == "s"):
            if(not os.path.exists(writeFile)):
                with open(writeFile, "w+") as f:
                    writer = csv.DictWriter(f, fieldnames=summaryData.keys())
                    writer.writeheader()

            with open(writeFile, 'a+') as f:
                writer = csv.DictWriter(f, fieldnames=summaryData.keys())
                writer.writerow(summaryData)


# This function loads the serialzed distance list of the specified country
#
# The only countries that are currently accepted are:
#     Canada
#     Uruguay
#     WesternSahara
#
# Args:
#     countryName - The name of the country to load
#
# Returns:
#     The unserialzed list
def load_file(countryName):
    filename = countryName + ".pickle"
    with open(filename, "rb") as f:
        return pickle.load(f)


def getTSPfilename(countryName):
    if countryName == "WesternSahara":
        filename = "../TSP_WesternSahara_29.txt"
    elif countryName == "Uruguay":
        filename = "../TSP_Uruguay_734.txt"
    elif countryName == "Canada":
        filename = "../TSP_Canada_4663.txt"

    return filename


if __name__ == '__main__':
    main()
