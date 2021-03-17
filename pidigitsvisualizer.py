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


def calculateDigits(limit):
    # Using multi precision
    mp.dps = limit

    return list(str(mp.pi))[2:]


def digitsDistribution(digits):
    # distribution = {1: 6, 2: 7, ...}, so {digit: n times in pi}
    distribution = {int(x): digits.count(x) for x in digits}

    distribution = dict(sorted(distribution.items()))

    return distribution


def plot(distribution):
    plt.bar(range(len(distribution)), list(distribution.values()), align="center")
    plt.xticks(range(len(distribution)), list(distribution.keys()))
    plt.show()


if __name__ == '__main__':
    d = calculateDigits(100)
    # print(len(d))
    print(d)
    d1 = digitsDistribution(d)
    print(d1)
    plot(d1)