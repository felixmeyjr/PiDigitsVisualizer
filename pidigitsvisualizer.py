# PI digits distribution/occurrence visualizer

"""
Get digits of pi
Calculate distribution for given interval
Plot
Repeat for a nice flow

Later:
User Input: how many digits?

"""

from mpmath import mp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def calculateDigits(limit):
    # Using multi precision
    mp.dps = limit  # dps: decimal places

    return list(str(mp.pi))[2:]


def digitsDistribution(digits):
    # distribution = {1: 6, 2: 7, ...}, so {digit: n times in pi}
    distribution = {int(x): digits.count(x) for x in digits}

    return dict(sorted(distribution.items()))


def plot(distribution):
    # Highest n of occ should be green; lowest red
    clrs = []
    for val in distribution.values():
        if val == min(distribution.values()):
            clrs.append("red")
        elif val == max(distribution.values()):
            clrs.append("green")
        else:
            clrs.append("blue")

    plt.bar(range(len(distribution)), list(distribution.values()), color=clrs, align="center")
    plt.xticks(range(len(distribution)), list(distribution.keys()))

    plt.xlabel("Digit")
    plt.ylabel("Number of occurrences")
    plt.title("Distribution of pi digits")
    plt.show()


def main():
    d = calculateDigits(100)
    # print(len(d))
    print(d)
    d1 = digitsDistribution(d)
    print(d1)
    plot(d1)


if __name__ == '__main__':
    main()
