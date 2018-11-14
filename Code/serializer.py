"""
This script reads a TSP file and calculates the distance from each city in the
file to all other cities in the file. It saves these distances to a list and 
serializes the list
"""
import pickle
import math
import sys


"""
This function checks if the user has supplied the correct number of command
line arguments

Args:
    None

Returns:
    None
"""
def checkSysArgs():
    if(len(sys.argv) != 3):
        print("usage: python {} TSP_filename Serialized_filename".format(sys.argv[0]))
        sys.exit(2)


"""
This function reads the TSP file and creates a list of the cities and their
x and y coordinates

Args:
    TSP Filename

Returns:
    List of x and y coordinates
"""
def readFile(filename):
    cities = []
    with open(filename) as f:
        lines = f.read().splitlines()
        for line in lines:
            coordinates = line.split()
            cities.append([float(coordinates[1]), float(coordinates[2])])

    return cities


"""
This function takes the list of cities and calculates the distances from the
city to all other cities in the file

Args:
    arr - The list of cities' x and y coordinates

Returns:
    List of distances from each city to all other cities
"""
def calculate_distances(arr):
    distances = []
    for origin in range(len(arr)):
        distances.append([])
        for dest in range(len(arr)):
            if(origin == dest):
                distances[origin].append(0.0)
                continue
            dx = arr[origin][0] - arr[dest][0]
            dy = arr[origin][1] - arr[dest][1]
            distances[origin].append(math.sqrt(dx**2 + dy**2))

    return distances


"""

Args:
    arr - The array to be serialized
    filename - The name of the serialized file
Returns:
    none
"""
def serialize(arr, filename):
    with open(filename,mode='wb') as f:
        pickle.dump(arr, f, pickle.HIGHEST_PROTOCOL)


def main():
    checkSysArgs()
    source = sys.argv[1]
    dest = sys.argv[2]

    cities = readFile(source)
    distances = calculate_distances(cities)
    serialize(distances,dest)

if __name__ == '__main__':
    main()