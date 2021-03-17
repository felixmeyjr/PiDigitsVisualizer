# PI digits distribution/occurrence visualizer

"""
Get digits of pi
Calculate distribution for given interval
Plot
Repeat for a nice flow

Later:
User Input: how many digits?

"""

import math
import matplotlib


def calculateDigits(limit):
    digits = list(str(round(math.pi, limit + 2)))[2:]
    return digits


def digitsDistribution(digits):
    pass


def plot():
    pass


if __name__ == '__main__':
    print(calculateDigits(10))
