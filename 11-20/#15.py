import math


def lattice_paths(num):
    return math.factorial(2 * num) / (math.factorial(num)) ** 2


print(lattice_paths(20))