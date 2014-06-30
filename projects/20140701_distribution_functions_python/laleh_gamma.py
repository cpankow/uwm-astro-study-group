#!/usr/bin/env python

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# This is to ensure that relevant random variables remain the same between invocations of the random number generator
# Change seed to get new random draws
seed = 0
np.random.seed(0)

# N=10 random variables
shape = 1
scale = 2
data = np.random.gamma(shape, scale, 10)

# Now save to file
with open("gamma_n_10.txt", "w") as fout:
    for x in data:
        print >>fout, x

# Histogram the data
plt.hist(data, bins=5)
plt.grid()
plt.xlabel("draw values")
plt.ylabel("N")
plt.title("Gamma DF with shape=1 and scale=2")
plt.show()

# descriptive statistics
mean = np.mean(data)
var = np.var(data)
skew = stats.skew(data)
kurt = stats.kurtosis(data)
med = np.median(data)
mode = stats.mode(data)[0]

print """
n: 10
mean: %1.2f
variance: %1.2f
skew: %1.2f
kurtosis: %1.2f
median: %1.2f
mode: %1.2f
""" % (mean, var, skew, kurt, med, mode)

# N = 100, 1000, 10000 random variables

for n in (100, 1000, 10000):
    data = np.random.gamma(shape, scale, n)
    mean = np.mean(data)
    var = np.var(data)
    skew = stats.skew(data)
    kurt = stats.kurtosis(data)
    med = np.median(data)
    mode = stats.mode(data)[0]

    print """
n: %d
mean: %1.2f
variance: %1.2f
skew: %1.2f
kurtosis: %1.2f
median: %1.2f
mode: %1.2f
""" % (n, mean, var, skew, kurt, med, mode)

    plt.hist(data, bins=20, normed=True, histtype='stepfilled', alpha=0.7, label="%d samples" % n)
    plt.show()




