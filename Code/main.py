import numpy as np
import random

import initialization
import evaluation
import recombination
import mutation
import parentSelection
import survivorSelection


def main():
    # string_length = 8
    popsize = 100
    mating_pool_size = int(popsize * 0.5)  # has to be even
    tournament_size = 3
    mut_rate = 0.2
    xover_rate = 0.9
    gen_limit = 50
    fitnessThreshold = 50


if __name__ == '__main__':
    main()