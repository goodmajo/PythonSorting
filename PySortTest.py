import random
import PySorting
import numpy
import math
import operator as op
from statistics import median

def main():

    randomNumbers = random.sample(range(1, 101), 10)
    print("This list of random numbers is:", randomNumbers)

    stupidSorted = PySorting.StupidSort(randomNumbers, False)
    print("Stupid Sorted:", stupidSorted)


if __name__ == '__main__':
    main()